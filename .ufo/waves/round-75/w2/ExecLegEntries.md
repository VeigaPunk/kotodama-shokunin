# ExecLegEntries — round 75, wave 2: claim-C `leg_entries` (ENTRIES)

Seat: `ExecLegEntries` (executor, leaf; no spawn, no background job, no delegation). Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` at base `f556d1049fe651d3d63975600b13acd9fb686f15`.
Wrote exactly two things: the part file below and this report. Read-only git everywhere; no lane
index/jj/git state touched; the fleet repo, `scripts/`, `templates/`, `.ufo/state`, sibling lanes and
`/home/vgpnk/Projects/shokuknow` untouched. No tool installed or upgraded (nothing needed: `git`,
`python3` 3.x stdlib sufficed), no pacman, no network fetch.

## 1. Deliverable

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75/w2/parts/leg-entries.py`

- 7182 bytes, `sha256 a40c768aaa4bc73e75d3660a3b8b1559666d06f4225a1d5447d1f81a3abe3c9a`
- defines only `leg_entries(ctx)` plus private helpers `_entries_placeholder`,
  `_entries_body_words`, `_entries_floor`, and two module constants
  (`_ENTRIES_WORD_FLOOR = 478`, `_ENTRIES_HEADING_RE`, `_ENTRIES_FIELD_RE`); no imports, no
  top-level executable code. Helper prefix is the contract's `_<legfile>_` stem with the file's dash
  written as an underscore (`leg-entries` → `_entries_`); nothing collides with PART A or with the
  shared part-cfg helper names.
- Shared helpers are **called, never redefined**: `read_tree`, `Missing`, `header_block`,
  `header_field_names`, `norm_label`, `H2_RE`, `ANGLE_RE`, `PLACEHOLDERS`, `HEADER_FIELDS`,
  `dedupe`, `leg` (PART A) and `_min_entry_words` (part-cfg).
- `python3 -B -m py_compile` on `PART A (lines 1-510) + cfg stub + this part` → rc 0.

## 2. The leg wording as I read it (verbatim from the frozen draft, claim C legs[0])

> ENTRIES: the frozen entries exist at <lands>, absent at base, provenance header
> (source/verified-at/recheck/ground/topic/gap-filled/sources/couples/scope) first, no header field
> value in {TODO, TBD, FIXME, XXX, n/a, ?, —}, none matching `<[^>]+>`, at least one `## ` section,
> and a body of at least 478 words (the smallest corpus/knowledge entry at base); ENTRIES is a
> length-and-shape gate only

Implementation, predicate by predicate:

| clause | implementation |
|---|---|
| exist at `<lands>` | `read_tree(mat, path)` for every path in `cfg["entries"]`; a `Missing` (or, see R6, a non-UTF-8 body) is a FAIL |
| absent at base | `os.path.isfile(mat_base/<path>)` → FAIL "present at base (not uncovered ground)" |
| provenance header first | the nine `HEADER_FIELDS` must all be present in `header_field_names(text)` — which PART A derives only from the block **before the first `## ` section**, so a header placed after the body is invisible → FAIL |
| no placeholder value | `_entries_placeholder` over each header **field value** (R2) |
| none matching `<[^>]+>` | `ANGLE_RE` over each header **field value** (R3) |
| >= 1 `## ` section | `H2_RE` (PART A: `^##\s`) must match at least one line |
| body >= 478 words | `_entries_body_words`: every line from the first `## ` to EOF **minus heading lines** (R4), against the frozen 478 |
| length-and-shape gate only | no prose, source-truth, id-resolution or repetition predicate is added (see §5) |

## 3. Ambiguities and how each was resolved

- **R1 "provenance header … first".** The wording fixes the field *set* and the field *position*
  ("first"), not their order. Resolved: presence of all nine fields inside the pre-`## ` block, any
  order. `header_field_names` (PART A) is exactly that reading, and it makes a header written below
  the body a FAIL (mutant M9) without grading a cosmetic ordering the frozen text never states.
- **R2 "no header field value in {TODO, …}".** Literal set membership is trivially evaded by
  `gap-filled: TBD — pending`. Resolved: a value is a placeholder when, casefolded and stripped of
  the surrounding dash/space, it is a `PLACEHOLDERS` member — **or when its leading whitespace token
  is** (so `TBD — pending` fails). The empty value is a placeholder because PART A's `PLACEHOLDERS`
  carries `""`. Both spellings are exercised (M3 exact, M3b with an excuse). Residual false-positive
  risk: a field value that legitimately *begins* with `—`, `?` or `n/a`; no base entry, staged file or
  round-75 draft does, and the landed drafts' values (checked) do not.
- **R3 "none matching `<[^>]+>`".** The clause hangs off the header-field enumeration, so it is
  graded on header field **values** only — not on the H1 title and not on the body (a body that
  legitimately writes `<doc>` in prose is not this leg's business). M4 exercises the `source:`
  value.
- **R4 "a body of at least 478 words".** Two sub-readings fixed here:
  1. *Where the body starts / what counts.* Body = lines from the first `## ` section to EOF with
     **all heading lines removed**. Counting headings (as round 74's `leg_entries` did by joining
     from the `## ` line inclusive) lets a 200-heading, zero-prose file reach the floor; excluding
     them makes the floor a prose floor. Mutant M8 is exactly that padding attack and fails at 0
     words.
  2. *478 vs the shared helper.* The frozen constant is the gate. `_min_entry_words(mat_base)` is
     called only to **confirm** the parenthetical provenance; a mismatch is emitted as a parenthetical
     note in the detail, never as a FAIL, because the frozen text ends with "ENTRIES is a
     length-and-shape gate only" — the parenthetical is a provenance statement about the constant,
     not a second, moving predicate. In the mock, `_min_entry_words(mat_base)` returns exactly 478
     (`heritage-taxonomy-models.amend-2026-10-24-r13.md`, 478 words), so the note never fires.
- **R5 "absent at base".** "Absent" = no file at that path in the tree materialized from the frozen
  claim base. A directory at the path in the base tree would also count as absent-in-file-terms;
  no such case exists or is plausible.
- **R6 (new, forced by robustness).** `read_tree` (PART A, fixed) opens UTF-8 and lets
  `UnicodeDecodeError` escape. An entry path holding binary bytes would therefore crash the whole
  counter instead of failing a leg. Resolved: the leg catches `UnicodeDecodeError` and FAILS with
  "is not UTF-8 text" — still inside the shape gate's wording (such a file cannot carry the header or
  a countable body), and no leg may crash the counter. M13 exercises it.
- **Detail length.** The contract caps a leg's detail first line at 300 characters. `leg()` prints
  `"     %s" % detail`, so the detail is cut at 295 characters (5 + 295 = 300) with a trailing
  `...`; without the cut a three-entry stacked landing prints 305 (measured before the fix).

## 4. Test setup (real, not simulated)

Scratch root `/fast/scratch/hyaku/kotodama-r75/ExecLegEntries` (created with `mkdir -p`, passed
explicitly, deleted before yield; nothing under `/tmp`).

Mock construction, all by absolute path:

1. `git clone --quiet --shared <lane> $S/lane` → `git -C $S/lane rev-parse --show-toplevel` printed
   `/fast/scratch/hyaku/kotodama-r75/ExecLegEntries/lane` **before** any commit-worthy action;
   `git -C $S/lane checkout --detach f556d1049…` → HEAD = base.
2. `git -C $S/lane archive --format=tar <base> | tar -x -C $S/mat_base` (the graded base tree).
3. `cp -a $S/mat_base/. $S/mat/` and into `$S/mat/corpus/knowledge/myth-symbol/` copied the three
   **unlanded** drafts `narrative-structure-frameworks.md`, `.amend-2026-10-23.md`,
   `.amend-2026-10-23b.md` from `.ufo/waves/round-75/drafts/` (draft bytes at test time: 22571 /
   11957 / 10186 B).
4. Appended rows 840-848 (`S885`…`S893`) of
   `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md` to `$S/mat/corpus/SOURCES.md`
   (808 → **817** rows, verified) and copied the probe captures
   `.ufo/waves/round-75/counters/probe-receipts/S88*.txt` into `$S/mat/reports/round-75/evidence/`
   (S885, S886, S887, S888, S889, S890, S892). Neither the registry nor the evidence files are read
   by this leg; they are present so the mock is the tree the wave will grade.
5. Assembly executed in one namespace: `PART A = accept-c.py lines 1-510`, then a **cfg stub**
   (`part-cfg.py` is not written yet — `parts/` held no other file at test time, so the contract's
   "build the cfg dict by hand" branch applies), then `leg-entries.py`. The stub carries only
   `_min_entry_words` (round-74 lines 738-745 semantics) and the `cfg` dict per
   `CFG-CONTRACT.md` (`entries` = the three frozen paths; the rest of the keys present with the
   contract's shapes).
6. `ctx` = `{"root": $S/lane, "lands": <base>, "mat": $S/mat|$S/mutants/<m>, "mat_base":
   $S/mat_base|$S/mutants/m11_base, "cfg": cfg, "fleet_root":
   /home/vgpnk/Projects/shokunin, "scratch": $S}`.

## 5. Positive and mutant table (every row executed; `LEG PASS/FAIL ENTRIES` plus its detail)

| # | fixture | verdict | detail (first line of the leg's output) |
|---|---|---|---|
| — | **POSITIVE** — base tree + the three draft entries at the frozen paths | **PASS** | *(no detail: all three bodies 3012 / 1398 / 1094 words after heading removal; nine fields each; no placeholder, no `<…>`)* |
| — | POSITIVE with `mat_base=None` (degenerate ctx) | PASS | `base tree unreadable: absent-at-base unconfirmed` |
| M1 | header-only stub: H1 + nine fields, **no `## ` section** | FAIL | `…/narrative-structure-frameworks.md has no `## ` section (header-only stub)` |
| M2 | header + one section + 100-word body | FAIL | `… body has 100 words (floor 478 = the smallest knowledge entry at base)` |
| M3 | `- ground: TBD` | FAIL | `… header field 'ground' carries a placeholder value 'TBD'` |
| M3b | `- sources: — pending the Gate` | FAIL | `… header field 'sources' carries a placeholder value '— pending the Gate'` |
| M4 | `- source: <document-url>` | FAIL | `… header field 'source' carries a <...> template token` |
| M5 | `- couples:` line deleted | FAIL | `… provenance header before the first `## ` missing: couples` |
| M6 | empty body: header + `## 1. Premise` and nothing after | FAIL | `… body has 0 words (floor 478 …)` |
| M7 | **filler-padded stub**: 600 filler words inside a header field, 30-word body | FAIL | `… body has 30 words (floor 478 …)` |
| M8 | heading padding: 200 × `## filler filler filler`, no prose | FAIL | `… body has 0 words (floor 478 …)` |
| M9 | header block moved **below** the body (header not first) | FAIL | `… provenance header before the first `## ` missing: source,verified-at,recheck,ground,topic,gap-filled,sources,couples,scope` |
| M10 | one entry deleted at lands | FAIL | `…amend-2026-10-23b.md missing at lands` |
| M11 | one entry present in the base tree (not uncovered ground) | FAIL | `…amend-2026-10-23.md present at base (not uncovered ground)` |
| M12 | stacked: all three entries with `couples: TBD` + `scope: <fill>` | FAIL | detail cut at exactly 300 printed chars (`… 'couples' carries a placeholder value 'TBD'; …`) |
| M13 | entry body replaced by binary bytes | FAIL | `…amend-2026-10-23.md is not UTF-8 text` |
| M14 | entry path is a directory | FAIL | `…amend-2026-10-23b.md missing at lands` |
| M15 | zero-byte entry | FAIL | `…/narrative-structure-frameworks.md empty (no body)` |

Positive: **1/1 PASS**, run twice with byte-identical stdout (deterministic). Mutants: **15/15 FAIL**,
each with a reason naming the clause it violates. Largest printed detail line: exactly 300 characters
(M12).

## 6. What this leg deliberately does not reject (and why that is correct for this wave)

`CritCCounterVacuity` §"Ranked predicate repairs" item 7 proposes a **source-linked minimum** for
ENTRIES ("a Gate quote or ≥20-character NFKC overlap with the evidence window"). That proposal was
**not frozen** into claim C, whose leg text ends "ENTRIES is a length-and-shape gate only" and whose
`kill_rule` binds entry prose to sources through other legs (REPOINTED/ROWS/GATE/EVIDENCE). A
>=478-word filler body with a well-formed header therefore **passes this leg by design**, and the
w1 survivors it buys must be caught by the frozen kill rule, not by silently strengthening this
predicate. I made no such strengthening. Concretely: the seat brief's "filler-padded stub must fail"
is honoured for the *shape* attack that this wording does cover — filler counted outside the body
(M7, padding in the header) and filler made of headings (M8) — while prose filler inside a genuine
≥478-word body stays out of scope and is reported here as the leg's known survivor.

## 7. Risks / notes for the L1

1. **Interface dependency** — the part calls `_min_entry_words(mat_base)` (part-cfg). If ExecCtrCfgMain
   drops or renames it, `_entries_floor` degrades to the frozen 478 with a silent `except Exception`;
   the leg stays correct but loses the provenance confirmation line. No other part-cfg helper is used.
2. **478 is hardcoded** with the frozen-text justification in the comments; if freeze changes the
   parenthetical (it should not — base is frozen), the constant must change with it. The counter does
   not read it from `cfg` because `CFG-CONTRACT.md`'s cfg schema carries no word floor.
3. **R2 strictness**: values beginning with `—`/`?`/`n/a` are placeholders. The three staged drafts
   and the base corpus are clean of this; a scribe rewriting a header to start with an em dash would
   be failed, and that is the reading I want.
4. **`window`/`terms`/`owned_inplace`/multi-id rows** — none are read here: the leg's inputs are
   `cfg["entries"]`, `mat` and `mat_base` only, so the round-75 deltas that touch other legs
   (multi-id `row_staged`, `row_doc`, `window-scope`, README partition exemption, `owned_inplace`)
   cannot make this leg lie. The three entry paths are the frozen list, including the two amendment
   files SimplifierRows §7 and ScribeEntryAmend argued for.
5. Mock realism gap: the landed entries will differ from the drafts (locator re-points, id
   normalisation). The leg grades only shape, so the drafts are a faithful positive; if a landed
   entry drops below 478 body words the leg fails, which is the intended reading (staged 23b at 366
   total words is *below* the floor as staged — SimplifierRows §7 — and the combined amendment must
   stand at ≥478).

## 8. Scratch

`/fast/scratch/hyaku/kotodama-r75/ExecLegEntries/` (lane clone, `mat_base`, `mat`, 16 mutant trees,
`concat_accept_c.py`) — deleted before yield; every value this report cites is reproduced in this
file, and no `/tmp` path is used or cited. Nothing was installed.
