# ScribeIndex — round 76 w1 (draft scribe: README index + SOURCES search log)

Seat: ScribeIndex (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`98c486bdb4650ba5b8e651d332910e8ee60ad121`. Round-76 `CLAIMS-DRAFT.md` was read and **not edited**;
no claim, axis or route was decided here.

## Verdict

Both assigned drafts exist and are internally consistent with the base file and with simulated
installs at `n = 4/3/2`. Two draft defects found by self-check were fixed before finalising (F3, F5);
two base-state facts contradict the claim text as written (F1, F2) and are reported, not repaired.

## Artefacts

| path (relative to lane root) | bytes | content |
|---|---|---|
| `.ufo/waves/round-76/w1/drafts/readme-index.md` | 9690 | four conditional index rows (byte-ordered insertion), `## culture-material/` heading variants for n=4/3/2, `Counts checked` footer variants for n=4/3/2, four pre-install checks |
| `.ufo/waves/round-76/w1/drafts/sources-search-log.md` | 10195 | one `## Paths` row, one PRISMA-shaped `## Search log` note with `<<FILL:n>>` slots, installer notes, measured-count command block |

Verification command for the byte counts: `ls -la .ufo/waves/round-76/w1/drafts/` — `readme-index.md
9690`, `sources-search-log.md 10195`.

## What the drafts prescribe

**Index rows** — four, all marked CONDITIONAL in §1.3 of the draft (the Gate decides; the claim counts
`n >= 2` over these four paths only):

- three rows inserted immediately before the existing `- \`calendar-festival-systems.md\``
  (`…-23c.md`, `…-24-r10.md`, `…-24.md`), and one before `- \`era-periodization-models.md\``
  (`…-23b.md`), i.e. byte order, not append-at-end.
- each row is ``- `name.md` — <the entry's own `- topic:` text>``, the wrapped `- topic:` continuation
  lines joined to one line with indentation collapsed and **no word changed**.

Ground truth for "verbatim": the four `- topic:` fields were extracted from the staged entries and
compared byte-for-byte to the drafted row payloads:

```
drafted rows: 4
   - `calendar-festival-systems.amend-2026-10-23c.md` — the standard's own clause t ... len 480
   - `calendar-festival-systems.amend-2026-10-24-r10.md` — the authoritative copy's ... len 197
   - `calendar-festival-systems.amend-2026-10-24.md` — what GB/T 33661-2017 actuall ... len 228
   - `era-periodization-models.amend-2026-10-23b.md` — one institution's own dating ... len 368
topic payloads byte-identical to entries' - topic: fields: True
```

(the `ok` flag is `payload != ref` over all four; printed `True`.)

**Heading** — `## culture-material/ (40)` replaced by `(44)` / `(43)` / `(42)` for n=4/3/2.

**Footer** — appended as a new block after the round-75 block (older footers stay byte-identical), three
variants: total `256`/`255`/`254` with vector `32/32/44/29/24/95` / `32/32/43/29/24/95` /
`32/32/42/29/24/95`.

**`## Paths` row** — one bullet, chain `S898 → S896 → S897 → S895` (promulgation report → registry
record → closed-route statement → declared reproduction), with the archival leg `S894` deliberately read
beside the chain, not through it; per-row degradation rules given for a partial Gate.

**`## Search log` note** — one paragraph carrying question, where searched, date, identified / screened /
included / excluded, exclusion reasons and stop rationale, with `<<FILL:screened>>`,
`<<FILL:included>>`, `<<FILL:rows>>`, `<<FILL:excluded>>`, `<<FILL:unreachable>>` left for the scouts.

## Base-state measurements (each number with its command)

Base partition counts, one command per partition
(`git ls-tree -r --name-only 98c486b corpus/knowledge/<d> | grep -c '\.md$'`):

```
civilizations 95   culture-material 40   linguistics 32
myth-symbol 32     synthesis 29          verification 24
total 252
```

— 252 total: `git ls-tree -r --name-only 98c486b corpus/knowledge | grep -c '\.md$'` → `252`.
Matches the base footer (`(total 252 files; directory totals 32/32/40/29/24/95)`) and the base heading
`## culture-material/ (40)`.

Package inventory (read-only tree):
`find /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge -type f -name '*.md' | wc -l`
→ `40`; per partition → `culture-material 9`, `linguistics 17`, `myth-symbol 5`, `verification 9`
(sum 40). `find …/merge/kotodama/amendments -type f | wc -l` → `4`.

Id census: `wc -l .ufo/waves/round-76/assimilation/{staged-ids,reg-ids,collisions}` →
`132 staged-ids`, `817 reg-ids`, `35 collisions`.

Which staged culture-material files the lane already holds:

```
comm -12 <staged sorted> <held sorted>   -> 4
comm -23 <staged sorted> <held sorted>   -> 5
```

The 4 held: `heritage-taxonomy-models.md`, `heritage-taxonomy-models.amend-2026-10-24-r13.md`,
`worldbuilding-setting-practice.md`, `worldbuilding-setting-practice.amend-2026-10-23.md`. The 5 not
held: the four candidates plus `era-periodization-models.amend-2026-10-23.md` (the older amendment the
package's own merge report flags as a duplicate target). Direct confirmation for that one:
`git cat-file -e 98c486b:corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23.md`
→ `fatal: path … does not exist in '98c486b'`.

## Simulated install (draft self-check, scratch only)

Rows inserted in byte order into a scratch copy of `git show 98c486b:corpus/README.md`, heading
replaced, footer appended; four invariants re-run per variant:

```
base   rows= 40 heading= 40 match=True inversions=1 footer=('252', '32/32/40/29/24/95')
n=4    rows= 44 heading= 44 match=True inversions=1 footer=('256', '32/32/44/29/24/95')
n=3    rows= 43 heading= 43 match=True inversions=1 footer=('255', '32/32/43/29/24/95')
n=2    rows= 42 heading= 42 match=True inversions=1 footer=('254', '32/32/42/29/24/95')

files-vs-rows check on the simulated n=4 tree:
rows-not-files: [] | files-not-rows: []
```

Numeric checks read: vector sums `32+32+44+29+24+95 = 256`, `…43… = 255`, `…42… = 254`, matching the
total line in each variant. Inversion count is unchanged at 1 in every variant, so the insert adds no
new disorder (F1 explains why 1, not 0).

## Findings

**F1 — the base culture-material index is not strictly sorted (pre-existing, round 74).**
`git show 98c486b:corpus/README.md | sed -n '/^## culture-material\//,/^## synthesis\//p' | grep -o
'^- \`[^\`]*\`'` gives 40 names with exactly one adjacent inversion:

```
writing-media-surface-economy.md > worldbuilding-setting-practice.amend-2026-10-23.md
```

Round 74 appended the two `worldbuilding-setting-practice*` rows at the end instead of before
`writing-media-surface-economy.md`. Consequence: the "section is byte-sorted" assumption is false and a
`sorted -c` gate would be red at base. My draft therefore states the observed convention accurately
(38 of 40 sorted, one known inversion), offers append-at-end as the round-74-consistent alternative, and
replaces the sorted-check with an **inversion-count** check whose base value is 1 and must stay 1. This
is a report item only; the round-76 draft must not be blamed for a base inversion.

**F2 — the claim's before-state grep is false as literally written.**
Claim: `git grep -l -E 'GB/T 33661' 98c486b -- corpus` and `…'digital\.archives\.go\.jp'…` each print
nothing (exit 1). Observed at base:

```
git grep -l -E 'GB/T 33661' 98c486b -- corpus
98c486b:corpus/lessons/round-68.md
98c486b:corpus/lessons/round-69.md
exit=0

git grep -l -E 'digital\.archives\.go\.jp' 98c486b -- corpus
98c486b:corpus/lessons/round-68.md
exit=0
```

Scoped to the knowledge corpus the claim holds: both commands with `-- corpus/knowledge` print nothing,
`exit=1` (run; output empty). So the *expectation* is right and the *command scope* is wrong — the
lessons discuss the package row by name (round-69 line 111 names "the package's GB/T 33661-2017 row").
The draft's Search log note and command block state the `corpus/knowledge` form and warn against writing
the unscoped one.

**F3 — my own first draft carried a broken shell idiom (fixed).** The name-extraction step used
`tr -d '\`- '`, which `tr` reads as a collating range:
`tr: range-endpoints of '\`- ' are in reverse collating sequence order` (observed), and the pipeline then
produced `0` instead of the true inversion count. Replaced with `sed 's/^- \`//; s/\`$//'` in both the
inversion check and the rows-vs-files check; re-run prints `1` and the expected three leading names.
Worth a lesson entry: a check whose output is a plausible number can be silently wrong — the `tr`
version returned `0`, which would have read as "clean" on a section that has one inversion.

**F4 — package size figures disagree and are unresolved.** The package's own
`MERGE-REPORT.md` states "proposed knowledge entries: **56**" and "proposed rows accepted: **132**",
while the tree holds 40 staged `.md` files under `knowledge/` and 4 under `amendments/` (44 files). 56 is
not reachable from 40+4 by any counting I performed. The `Search log` note's `Identified 40` is therefore
flagged in the draft as needing settlement before it lands; I did not adopt 56 and did not invent a
reconciliation.

**F5 — `n` variants are arithmetic-only.** The heading/footer variants are parameterised on `n`; which
four-to-two entries actually land is the Gate's decision, so the draft ships all four rows marked
CONDITIONAL rather than guessing an admission order. No `n = 0/1` variant exists because the claim's kill
rule fails there.

## Not run (reported as unrun)

- No Gate admission check, no quarantine verdict, no census run — those are L1/other-seat work.
- No document opening: I did not fetch any URL, so no access-tier, UA or capture claim is made here. The
  Search log's screened/included/excluded/unreachable counts are `<<FILL:…>>` slots by design.
- The §4 checks in `readme-index.md` were exercised against a **simulated** install in scratch, not
  against the frozen commit (it does not exist yet); the simulated numbers are the ones quoted above.
- Registry rows (S894–S898) were **not** drafted: that is another seat's artefact, and one row per
  document depends on the scouts' document map.

## Mutations, installs, scratch

- Writes: exactly two files, both under `.ufo/waves/round-76/w1/drafts/` (the two artefacts above).
  Lane git state untouched — `git status --porcelain` in the lane prints only the pre-existing
  `?? .ufo/waves/round-76/` and `?? reports/round-76/`; no add/commit/checkout/stash anywhere, no jj.
- Fleet repo, sibling lanes, `/home/vgpnk/Projects/shokuknow/**`, `scripts/`, `templates/`, `.ufo/state`,
  LOG/SCORECARD/SKILL/SHONEN, `corpus/**`, `reports/round-75/**`: no writes (none attempted).
- Installs/upgrades: none — no tool was needed for this seat, so nothing to record.
- Scratch: `/fast/scratch/hyaku/kotodama-r76/ScribeIndex/` (topic extracts, sorted name lists) is
  deleted before yield; no `/tmp` path is cited anywhere above and no git fixture was created.
