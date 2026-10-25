# RevDanceEntryShape — round 71, wave 1 (claim C: entry acceptance shape)

Seat: L1Kotodama71.RevDanceEntryShape (leaf; no delegation, no background jobs, read-only).

## 0. Scope of this seat

Define the acceptance shape the claim-C entry must meet (draft criteria; the L1 freezes), then
apply it to the scratch structure produced by ExecDraftEntryShell. Nothing here edits bytes;
every criterion below is a draft for the L1 freeze.

Sources read: `reports/round-71/claims.json` (frozen), `corpus/QUALITY.md`, `tools/check-cited-lines.py`
(including its selftest cases), `corpus/SOURCES.md` head, sibling entries
(`hair-grooming-codes.md`, `footwear-codes-terminology.md`, `masks-masquerade.md`), and the shell
draft `/tmp/round71-claimC-entry-shell.md` (written 2026-10-25 by ExecDraftEntryShell; the wave
report `.ufo/waves/round-71/w1/ExecDraftEntryShell.md` confirms it as the deliverable).

---

## 1. Acceptance shape — draft criteria (for the L1 freeze)

Each criterion cites its QUALITY/claim basis. All of 1–10 must hold on the **landed** entry
(corpus path `corpus/knowledge/culture-material/dance-performance-movement-codes.md`), not on
the shell.

### P. Target and file
1. The entry exists at `corpus/knowledge/culture-material/dance-performance-movement-codes.md`
   (claims.json C: after, predicate, kill rule — "entry absent" fails).
2. Partition landings: `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
   prints culture-material 36 and corpus 243; `find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l` = 36 (claims.json C: after/`/counting_command).

### H. Header block, in order
3. The entry **opens** with the provenance trio as the first three content lines after the title,
   in the order `- source:`, `- verified-at:`, `- recheck:` (round-71 seat contract: "the entry
   opens with source/verified-at/recheck"; `ExecDraftEntryShell` prompt lists the trio first).
   - `- source:` keys to the round-71 SOURCES block and must **not** enumerate multiple S-ids on
     the one line (a list or range like `S861–S879` is a MULTI-ID finding; see §3.2) — prose block
     reference or a single id is acceptable.
   - `- verified-at:` is dated 2026-10-25 and states what was checked (census, sweeps, per-row
     spot-check once rows land); no `<FILL>` placeholder survives to landing.
   - `- recheck:` names the triggers (dated practices, etymologies, occasion bindings, row quotes).
   - This trio must be contiguous and open the entry; it must not be split by `- couples:` or
     `- sources:` (QUALITY criterion 1 provenance; corpus convention in round-61+ entries).
4. `- gap filled:` names the **sweep(s) that showed the gap** — both claim-before commands,
   verbatim, with their measured zero results:
   - `find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'` → prints nothing;
   - `grep -rniE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md` → prints nothing.
   It may also carry the base partition census (culture-material 35) and one-way partial-owner
   pointers (claims.json C: after — "its `- gap filled:` line names the sweep that showed the gap";
   convention in `hair-grooming-codes.md:4`, `footwear-codes-terminology.md:4`).
5. `- topic:` is exactly one line (contract: "one line"); it may carry no citation of its own.
6. `- sources:` bullet list: every cited bullet carries exactly one distinct S-id (see 9);
   the list counts the cited rows (see 11).
7. `- couples:` lines name the connected files/systems; if the entry couples nothing it must say
   so (QUALITY criterion 3).
8. `- scope:` line **refuses canon**: it decides nothing about any world, names no canon fact,
   records no promotion/clearance verdict, and ends at the handoff (QUALITY criterion 5 —
   canon hygiene: canon recording/consistency belongs to lore-shokunin; compare
   `hair-grooming-codes.md`, `sacred-registers-liturgical-language.md`).

### C. Citation hygiene
9. Each line carrying an S-id carries **exactly one distinct S-id**; a line repeating the same id
   is permitted; no line carries two or more distinct ids (QUALITY criterion 15; `check-cited-lines.py`
   MULTI-ID finding — including ranges `S612-S615` → `S612,S615`).
10. No table row (a line starting with `|` after leading whitespace) carries any S-id (QUALITY
    criterion 15; TABLE-ID finding). Tables may reference sections/slots by prose, never by id.
11. `python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md`
    exits 0 — zero MULTI-ID and zero TABLE-ID findings (QUALITY criterion 15 check; also claim C
    counting command and kill rule — "check-cited-lines non-zero" fails).

### R. Rows and count
12. The entry cites **≥12 new SOURCES rows opened this round** (cell `opened` = 2026-10-25), each
    tier A or B (never C as sole support; QUALITY criterion 6 and SOURCES tiers), status `mined`,
    `used-by` listing the entry path; the registry row count increases by exactly the number of
    new rows opened for the claim (claims.json C: after/predicate/kill; "fewer than 12 new rows
    cited by the entry" and "any cited used-by path missing" fail). New ids land at S861+ (max row
    S860 at base).
13. Each cited row's quote is opened and quoted in the round lesson Gate (claim C predicate).
14. NOHARM: the round diff is exactly the new entry + the new rows + README/lesson/scorecard/log
    appends (claim C predicate).

### Notes for the freeze
- "How many cited bullets" = the number of citation lines each carrying exactly one distinct S-id
  = the number of distinct real S-ids cited. Binding floor: **12** (claim). There is no upper
  ceiling; the shell drafts 19 slots, which is compliant.
- "How many SOURCES rows" = same count, **≥12**, all new this round, A/B, mined, used-by the entry.
- Placeholders `<S###>` are not S-ids (`\bS\d{3,}\b` does not match them); they satisfy nothing
  until replaced by real ids, and the lint must be re-run after substitution.

---

## 2. Application to the shell (`/tmp/round71-claimC-entry-shell.md`)

The shell is a structure draft and does not yet contain real S-ids, so criterion C9–C11 can only be
checked structurally; count criteria are checked against the 19 slot slots.

### Findings (severity-ordered)

**H1 — MEDIUM: the provenance trio does not open the entry, and is split.** In the shell the first
content lines are `- topic:` (10), `- gap filled:` (12), `- sources:` (14), `- source:` (38),
`- couples:` (40), `- verified-at:` (55), `- recheck:` (57). Criterion 3 requires the trio
(`- source:` → `- verified-at:` → `- recheck:`) contiguous as the opening block. The shell's own
report claims "Provenance trio" as item 1, but the file places it mid-header and split. Fix at
final fill: move `- source:` / `- verified-at:` / `- recheck:` to the top of the header block, in
that order, before `- gap filled:`.
  Evidence: shell lines 10/12/14/38/40/55/57; ExecDraftEntryShell prompt (spec.json item
  "ExecDraftEntryShell") lists "provenance trio (source: S### lines, verified-at, recheck)" first.

**H2 — LOW/MEDIUM: §7 design-prompt table is planned to cite S-ids in rows.** Shell line 113:
"Design-prompt table … each row cites its slot's row." Any table row carrying an S-id is a TABLE-ID
finding (criterion 15) and fails C10. Fix: keep the table's rows id-free; reference the slot/section
(prose) or list ids outside the table.
  Evidence: shell line 113; `check-cited-lines.py` TABLE-ID (`line.lstrip().startswith("|")` + id).

**H3 — LOW: `- verified-at:` carries a `<FILL>` placeholder.** The shell marks the M11 final sweep
`<FILL>` until rows land; criterion 3 requires a completed verified-at on the landed entry. This is
expected for a pre-rows shell but must be closed before landing (the executor already flags it).

**H4 — PASS: gap-filled naming.** The shell embeds both claim-before sweeps verbatim with their zero
results plus the 35 census and one-way partial owners (lines 12) — satisfies criterion 4.

**H5 — PASS: scope refuses canon.** `- scope:` (59) "decides nothing about any world, names no canon
fact, makes no promotion or clearance verdict, and ends at the handoff"; `- refuses:` (61) names the
non-decisions — satisfies criterion 8 (QUALITY 5).

**H6 — PASS: couples.** 13 couples targets, all verified to exist at this HEAD (lines 40–53) —
satisfies criterion 7 (QUALITY 3).

**H7 — PASS: topic one line, seven assigned section headings present.** §1 movement vocabulary, §2
space & stage types, §3 choreographic codification, §4 music-dance-voice coupling, §5 festival-ritual
performance, §6 power-and-social roles of performance, §7 worldbuilding application (plus standard
tails §8–§10) — matches the assignment list.

**H8 — PASS: row-slot count exceeds the floor.** 19 external-shelf slots (MV/SP/CH/MD/FR/PR/WB/CB)
≥ 12 minimum, one row per bullet, no line planned to cite more than one S id (lines 17–36, 66–119).

**H9 — PASS: no S-id-bearing table row in the current shell** (the only table is planned, §2-H2) and
no line currently carries two ids; the placeholder `<S###>` is not a regex S-id, so the lint passing
now proves nothing until fill.

### Verification gaps (to close at landing)
- Real S-ids must replace every `<S###>`; then re-run `check-cited-lines.py` (must exit 0) — C11.
- ScoutOpenSourcesC must deliver ≥12 tier-A/B rows opened 2026-10-25, status mined, used-by the entry
  path; row count must rise by exactly that number — R12.
- Round lesson Gate must quote each cited row — R13.
- Couples targets re-checked at the measured revision; verified-at filled with the actual readings — H3/R.
- Kill-rule legs not re-checked here: inventory counts (36/243), find count, registry delta.

---

## 3. Citation anchors (QUALITY)

- Criterion 15 (`corpus/QUALITY.md:47`): "Cited lines are clause-scoped — … each line that cites a
  source carries exactly one distinct S-id, and no table row carries one"; check
  `python3 -B tools/check-cited-lines.py <entry>` exits 0 (MULTI-ID and TABLE-ID findings exit 1);
  headed or one-id lines holding two clauses pass the lint, so clause scope stays review-only.
- `tools/check-cited-lines.py:44-61` (SID `\bS\d{3,}\b`; MULTI-ID when ≥2 distinct ids; TABLE-ID when
  leading `|` carries ≥1 id), `:141-167` (selftest: ranges `S612-S615` → `S612,S615`; repeated one id
  passes; table-two-ids yields both findings; pipe after prose is not a table row).
- Criterion 5 (`QUALITY.md:18-20`): canon hygiene — no entry decides what is true in any world; canon
  recording/consistency belongs to lore-shokunin; entries end at the handoff.
- Criterion 1 (`QUALITY.md:5-8`): provenance — every factual claim carries a cited, checkable source;
  unverifiable claims carry `(to-verify)` inline.
- Criterion 3 (`QUALITY.md:13-15`): coupling — `- couples:` names the connected systems/files; an
  entry that couples nothing must say so.
- Criterion 6 (`QUALITY.md:29`): source authority claim-scoped; publisher blurbs/abstracts are tier B;
  tier A only when primary/authoritative for the exact scope; tier C never sole support.
- Claim C frozen text (`reports/round-71/claims.json:19-23`): after (entry exists; gap-filled names the
  sweep; cites ≥12 new rows opened this round, tier A/B, each mined, used-by the entry; partition
  35→36, corpus 243; registry row count rises by exactly the new rows), predicate, counting command,
  kill rule.
- Entry-head conventions applied in corpus (`footwear-codes-terminology.md:3-10`, `masks-masquerade.md:3-12`,
  `hair-grooming-codes.md:3-5`): topic one line; gap filled with sweep command+result; sources block;
  couples; source/verified-at/recheck; scope refusing canon.

## 4. Tooling record

No tools installed or updated (strictly read-only review; nothing was needed).

## 5. Scope compliance

Leaf seat: no subagent dispatch, no background jobs, no mutations. Read-only; wrote only this report
at `.ufo/waves/round-71/w1/RevDanceEntryShape.md`.
