
## Post-wave update — round 74 ledger finalization (L1 follow-up)

Base moved to `f7104cbce186bc2e1522abf0cfd619cc834628bb` (lane HEAD at this seat). Inputs read:
`reports/round-74/claims.json` (claim Ca, 11 legs), `.ufo/waves/round-74/w1/RevClaimsFidelity.md` F3/F4/F5/F6/F13,
`.ufo/waves/round-74/w1/CritCaVacuity.md`, `.ufo/waves/round-74/w1/ScoutLedgerSweep{A,B,C}.md`,
`reports/round-73/ledger.json` (the frozen round-73 schema), and the draft counter the L1 will install,
`.ufo/waves/round-74/counters/accept-ca.py`. The round-74 wave-1 draft
(`.ufo/waves/round-74/drafts/ledger-draft.json`) is kept untouched; wave-1 seat reports were other
seats' work and were not depended on.

### Files written

| path | content |
|---|---|
| `.ufo/waves/round-74/drafts/ledger-final.json` (52 880 B) | 13 pairs, 4 deleted pairs, 11 annotate rows, 2 repair edits, 6 must_track pins, 6 content pins, 8 controls, 11 grammar rules, inventory/sweep provenance |
| `.ufo/waves/round-74/drafts/annotate-rows.md` (7 795 B) | the 4-column SCORECARD table (id, old token, new token, re-derivation command) |
| `.ufo/waves/round-74/drafts/repair-edits.md` (5 763 B) | the 2 physical edits with verbatim old/new lines and counter prerequisites |
| `.ufo/waves/round-73/w1/ExecLedger.md` | this section |

Scratch: `/tmp/ExecLedger74/clone` (full clone at base, used to run every argv through the counter's
own guard). No tool installs, no pacman, no fetch, no write to the fleet root or to any sibling path.

### (a)–(g) satisfied, with the deviations stated

- **(a) Deleted** LC-04, LC-05, LC-13, LC-14 (the four absence pairs), recorded in `deleted_pairs`
  with the reason: the absence is now carried by the RECEIPTS leg. Grammar R1 is kept but unused.
- **(b) Kept** LC-01, LC-02, LC-03, LC-06, LC-07, LC-08, LC-09, LC-11, LC-12 and **added** LC-15,
  LC-16, LC-17, LC-18 — **13 pairs**, floor 12, hard floor 10. Three mapping corrections, each
  measured, not assumed:
  - ScoutLedgerSweepC's LC-15 (`corpus/README.md:736` 243 → 247) is **byte-identical to kept LC-07**
    (same stated_at, same stated_text, same observed token). A second copy would break the LEDGER
    leg's unique-pair requirement, so it is filed as control **K7** and the L1's "LC-15" slot is
    given to the next unledgered sweep-C candidate, **sweep C's LC-16** (`corpus/lessons/round-73.md:138`
    "reachable" vs the lesson's own wall "present").
  - **LC-17 and LC-18** come from sweep A's M9 and M8 (README revision-block registry ranges): the
    blocks state `753 → 776` (round 66) and `752 → 776` (round 67) while the registry held
    701 → 724 and 728 → 752. Both were exercised at their own landing commits
    (`65fe857282…`, `c5f09921…`, `94209e8f…`), each named as a full 40-hex operand alongside the
    pinned base (see (c) and the guard findings below).
  - **LC-10 was dropped as a pair, not as a repair.** Its honest observation is 93 = civilization
    `.md` files minus the two `*primary-sources.md` maps, which needs a `:(exclude)` pathspec; the
    draft counter's H2 guard refuses `:(exclude)*primary-sources.md` ("does not resolve in the
    clone"), and the only bracket workaround, `*[!s].md`, measures **90** (five civilization files
    end in `s.md`), not 93. The token is still fixed by LC-09's in-place edit (same line), so
    nothing is left false; it simply cannot be graded as its own pair. Filed in `dropped_candidates`
    and in `open_questions_for_L1`.
- **(c) README discipline.** No README line is a REPAIR pair. All six README tokens (LC-06, LC-07,
  LC-08, LC-15, LC-17, LC-18) are ANNOTATE. The three revision-block pairs are measured at their own
  landing commits *and* name the pinned base, because the counter's ANNOTATE leg requires the base
  revision as an operand of every numeric pair; the parse keys on the historical revision literal,
  so neither operand can move when claim C appends to `corpus/README.md`.
- **(d) must_track** = six `{path, sha256}` entries, recomputed now with `sha256sum` (all six match
  the wave-1 values and no mtime has moved since 20:47:30):
  `CritEntryAmendFinal.md 290a6ccd839cb8cd09fc5089d1360dc4bcfabdea38f7a83733063159185c50aa`,
  `ExecSelftestAll.md dfc8fe0d2c54442bd5fa1a8f122c37751b89c861aeec2b5e77c041f66c11e71c`,
  `ScribeLogScorecard.md db254d8896d7cbce3377dc1d3f56ca41312063383a9c319324bf1c1a02e445b3`,
  `SimplifierEntries.md 9469d4d689aeb1f32a4127b9d2a0388236c622d206995df4ff8f11a201bdd481`,
  `drafts/log-entry.md 079728a53490714a350ec17195bc72b1034d1878130b6f491a200de53bf6ca6a`,
  `RevengerOrigins.md 7d14591923aff7b1dd5a28bc73d4933faf9cf721e4a7b113f6f7178206d581ed`.
  `content_pins` keeps each path's base/worktree blob ids so TRACKED never depends on checkout filters.
- **(e) fleet_pin** `dad39efd27988bd28b1fe41f5e327529f0472d3c` re-verified: the commit resolves, the
  blob is `d104dfa4342078ca258bb0399a1ae241e2e1d684`, `sha256` of the pinned file is
  `000bab3a36648498b67b78ea3d7db3f2e8dd17a3ad762aa528d95ef169132bdd`, and the same path at fleet
  HEAD hashes to the same value.
- **(f) annotate rows** — `.ufo/waves/round-74/drafts/annotate-rows.md`: 11 rows, exactly 4 columns,
  each command guard-clean and each returning its new token. The JSON carries the same rows as argv
  arrays (`annotate_rows`), so the counter can use argv directly and the markdown is the SCORECARD
  rendering.
- **(g) repair edits** — `.ufo/waves/round-74/drafts/repair-edits.md`: edit 1 = `SHONEN.md:6`
  (LC-01), edit 2 = `SKILL.md:594` (LC-09, carrying the same line's second token 92 → 93). Both
  `old_line` strings byte-match the base blobs; simulating the edits, the `statement_after` re-reads
  capture `804` and `95`, the base stated_texts are absent, and the tokens differ from base.

### Schema (description requested by the L1)

Compatible core with `reports/round-73/ledger.json`: `id`, `stated_at`, `stated_text`, `stated_parse`,
`observe_cmd` (argv), `parse`, `expected_after`, `disposition`, `rederive`, and `statement_after`
(REPAIR only). Extensions: `observed_at_base`, `red_at_base`, `why`, `stated_fleet` (fleet-side
statement for LC-03), plus top-level `schema.pair_semantics` (field-by-field semantics), `deleted_pairs`,
`annotate_rows`, `annotate_rows_note`, `repair_edits`, `receipts_required`, `controls`,
`dropped_candidates`, `sweep_inputs`, `grammar_requirements` (R1–R11), `inplace_spans`, `content_pins`,
`must_track`, `must_track_note`, `fleet_pin`, `fleet_pin_note`, `fleet_report`, `min_pairs`,
`pair_count`, `status`, `frozen_note`. Legacy `reports/round-73/ledger.json` keys that this file does
not repeat: none — every round-73 key is present or superseded by a described extension.

### Verification actually exercised (not inferred)

Every `observe_cmd` and every `rederive` was executed **through the draft counter's own code** —
`observe_problem(argv, clone)` then `run_observe(clone, argv)` — in `/tmp/ExecLedger74/clone`, a full
clone at base. Results (stated → observed, all red):

```
LC-01 412 -> 804   LC-02 9 -> 10     LC-03 9 -> 10      LC-06 243 -> 247
LC-07 243 -> 247   LC-08 30 -> 32    LC-09 94 -> 95     LC-11 23443 -> 97656
LC-12 no -> two    LC-15 776 -> 724  LC-16 reachable -> present
LC-17 752 -> 728   LC-18 753 -> 701
```

Each pair additionally passed: stated_text present on its stated_at line at base (fleet line at the
fleet pin for LC-03), guard verdict `None`, `expected_after` == observed, and `rederive` re-executing
to the same token. The 11 annotate rows were parsed from the markdown table, shlex-split, guard-checked
and executed: each returned its new token and each row contains both tokens. The two repair edits were
byte-compared to the base lines and simulated through the counter's REPAIR predicate.

### Counter-derived design constraints found (they changed the ledger)

1. **`_git_problem` refuses a non-40-hex revision operand for `git grep`.** `65fe857` is treated as a
   path ("does not exist in the clone"). Fixed by pinning the three historical revisions by full hash.
2. **The ANNOTATE leg requires `cfg["base"]` as an operand of every numeric pair.** Fixed by naming
   both the historical revision and the base in those argvs; the parse keys on the historical hash.
3. **The guard's glob existence test is non-recursive.** `corpus/knowledge/*.md` resolves to nothing
   (the knowledge root holds no direct `.md` files); `corpus/knowledge/*/*.md` is required and git
   counts the same 247.
4. **The guard refuses `>` in any argv element**, so the ASCII arrow in the S879 evidence line is
   matched with `.*` instead.
5. **`SEPARABLE` scans the WHOLE frozen ledger text** (`ledger_raw`) for `S<id> >= 881` and for the
   claim-C path family, so this ledger carries **no** literal separator id and **no** family string:
   LC-16's `stated_text` is a shorter verbatim substring of its line ("are reachable and span-present"),
   and ids are described, never written, in `why`/`open_questions`. Verified: zero ids at or above the
   separator, zero family occurrences, in `ledger-final.json`, `annotate-rows.md` and `repair-edits.md`.
   Note for the L1: the corrections block *is* scanned, so a note cell pasted into SCORECARD must also
   stay free of those literals.
6. `git grep -c` is accepted by the installed guard (probed), and the pipe-free row regex
   `^. S[0-9]{3}` measures identically to the claims' own row regex (804 / 724 / 752).

### Risks / open questions (also in `open_questions_for_L1`)

- LC-12 and LC-16 *state* their claims on lines that cite campaign-namespace ids at or above the
  separator (not lane rows; the lane registry ends at S880). A counter that scans `stated_at` lines
  for those ids needs the "lane id" qualifier; one that scans only the ledger text passes as frozen.
- LC-09's REPAIR needs the `§Corpus map` in-place span added to APPENDONLY; LC-01 needs SHONEN.md in
  the in-place path set. Without the SKILL span, LC-09 must become ANNOTATE (12 pairs).
- The two round-73 receipts (`accept-{c,ca}-73-at-lands.txt`) and their flags are prerequisites of
  the RECEIPTS leg; the round-73 counters print 10/11 and 8/9 without `--census-sh`/`--main`.
- LC-10 is not graded anywhere; if the L1 wants it, relax the guard's pathspec handling rather than
  accepting the 90-file bracket reading.
