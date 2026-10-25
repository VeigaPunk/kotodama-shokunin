# In-place edits for the REPAIR pairs (round 74, claim Ca)

Two REPAIR pairs, **two** physical edits: LC-01 rewrites `SHONEN.md:6`; LC-09 rewrites
`SKILL.md:594` and its one edit carries both of that line's false tokens (94 → 95 and 92 → 93).
Everything else in both files is byte-identical at `<lands>`.

Base revision: `f7104cbce186bc2e1522abf0cfd619cc834628bb`.

## Edit 1 — `SHONEN.md` line 6 (pair LC-01)

`old_line` (verbatim at base):

```
  asserted: `SKILL.md:20` (Decision table), `:505` (Error patterns), `:564` (Checklist); sources registered in `corpus/SOURCES.md` (412 rows after round 56 — 367 mined, 35 queued, 10 rejected — census exit 0 in `reports/round-56/telemetry/final-measures.txt`; 358 rows, 313/35/10 after round 55; 284 rows, 240/34/10 after round 54; the round-53 figure 194/35/9 became 194/34/10 in the round-54 prerequisite `d761ee8`); no non-author verifier on record. Pointers `:468`/`:522` corrected to `:505`/`:564` in round 73 (ledger pairs L04/L05; `grep -n '^## Error patterns$' SKILL.md` and `grep -n '^## Checklist' SKILL.md`).
```

`new_line`:

```
  asserted: `SKILL.md:20` (Decision table), `:505` (Error patterns), `:564` (Checklist); sources registered in `corpus/SOURCES.md` (804 rows after round 73 — 709 mined, 58 queued, 37 rejected — census exit 0 in `reports/round-73/telemetry/census-end.txt`; 412 rows, 367/35/10 after round 56 — census exit 0 in `reports/round-56/telemetry/final-measures.txt`; 358 rows, 313/35/10 after round 55; 284 rows, 240/34/10 after round 54; the round-53 figure 194/35/9 became 194/34/10 in the round-54 prerequisite `d761ee8`); no non-author verifier on record. Pointers `:468`/`:522` corrected to `:505`/`:564` in round 73 (ledger pairs L04/L05; `grep -n '^## Error patterns$' SKILL.md` and `grep -n '^## Checklist' SKILL.md`).
```

What changes and why:

- `412 rows after round 56` → `804 rows after round 73`: box 1 is the only statement of registry
  size and its leading figure stopped 17 rounds ago. 804 is measured at base
  (`git grep -c -E '^. S[0-9]{3}' f7104cb… -- corpus/SOURCES.md` = 804), statuses 709 mined /
  58 queued / 37 rejected, last id S880.
- The census receipt moves with the figure: 804 rows carry
  `reports/round-73/telemetry/census-end.txt` (`exit=0`); pointing the new figure at the round-56
  receipt would have created a fresh falsehood.
- The old chain is **kept** as dated history but re-labelled to match its own receipt:
  `412 rows, 367/35/10 after round 56 — census exit 0 in reports/round-56/telemetry/final-measures.txt`.
  The 358/313/35/10, 284/240/34/10 and `d761ee8` items re-derive exactly (sweep A R-S2) and are
  untouched.
- `no non-author verifier on record` is left as filed: sweep M13 flagged it as a wording ruling
  (25 spot-check records exist; none promotes a box), not as this pair's defect.

Verified: `statement_after` `(?s).*\((\d+) rows after round 73` over the new line captures `804`;
the base `stated_text` is absent from the new line; the token differs from base (`412`).

## Edit 2 — `SKILL.md` line 594 (pair LC-09; the same edit carries the line's second token)

`old_line` (verbatim at base):

```
- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
```

`new_line`:

```
- `corpus/knowledge/civilizations/` — 95 entries: 93 earlier-civilization
```

What changes and why:

- `94 entries` → `95 entries` (the graded token of LC-09):
  `git diff --shortstat <empty-tree> f7104cb… -- 'corpus/knowledge/civilizations/*.md'` prints
  `95 files changed`. The count went 94 → 95 at `767040e` (round 56) and was never repaired;
  `corpus/README.md:503` already reads `## civilizations/ (95)`.
- `92 earlier-civilization` → `93 earlier-civilization` (same edit, **not** a separate pair): with
  `':(exclude)*primary-sources.md'` the same command prints `93 files changed` — the 95 files are 93
  civilization bases plus the two source maps (`africa-primary-sources.md`,
  `mesoamerica-primary-sources.md`) named on lines 595-596. The token cannot be its own pair because
  the counter's H2 guard refuses the `:(exclude)` pathspec (`does not resolve in the clone`), and the
  `*[!s].md` workaround measures 90 (five civilization files end in `s.md`), not 93. See
  `dropped_candidates` in `ledger-final.json`.
- Lines 595-596 stay byte-identical:
  ```
    bases plus two source maps (`africa-primary-sources.md`,
    `mesoamerica-primary-sources.md`), each
  ```
- Verified: `statement_after` `(?s).*civilizations/\` — (\d+) entries` over the new line captures
  `95`; the base `stated_text` (`94 entries: 92 earlier-civilization`) is absent from the new line.

## Counter prerequisites for these edits

1. **APPENDONLY span list.** The round-73 guard allows in-place hunks in SKILL.md only inside
   §Gates and probes, and in `corpus/README.md`/`README.md` only inside `footer_range()`. This round
   needs: SKILL.md spans `{ §Gates and probes, §Corpus map (`^## Corpus map$`) }` and SHONEN.md added
   to the in-place path set with a box-1 span (line 6). Without the SKILL span, LC-09 must be
   re-dispositioned ANNOTATE (pair count 12).
2. **Line-level APPENDONLY.** Every changed line must be a `stated_at` line of a REPAIR pair plus
   appended lines: `SHONEN.md:6` (LC-01) and `SKILL.md:594` (LC-09) satisfy this.
3. **No README edit.** All six `corpus/README.md` tokens are ANNOTATE (grammar R10); claim C appends
   the culture-material index rows and a new Counts-checked footer to that file this round.
4. **Frozen bytes untouched.** `LOG.md`, `SCORECARD.md`, `corpus/lessons/round-74.md`,
   `corpus/lessons/round-73.md`, `corpus/lessons/round-72.md`, `reports/round-73/claims.json` and
   `reports/round-73/ledger.json` keep zero removed lines.
