# MutEntryClass — entry-class mutation probe of ACCEPT-C-67 rev0

Seat: mutation-tester, r67 wave 1. Instrument probed: frozen `reports/round-67/accept-c.py`
sha256 `3e5f1a58…aa97a5` (identical to the sha printed in `telemetry/dry-run-c.txt`; the instrument
was not edited). Detector: the whole counter, one run per mutant. Fixture root:
`/tmp/r67-mut-entry/repo` = `git clone --no-local --single-branch --branch main` of the lane at
`b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21`, plus one committed fixture commit
`c6d8c8cd38b9b7ab0a8139872b9abb32cae928a2` (lands). No lane file was touched.

## Fixture (green baseline, a prerequisite for interpreting mutants)

24 synthetic rows S805–S828 (11 cells: paper/A/mined/2026-10-24/used-by entry; live URL
`https://hostN.example.org/docN` + capture `https://web.archive.org/web/20251024NNNNNNid_/<same>`),
entry with 24 paren-cited bullets under 4 `##`, README row + `## culture-material/ (34)` +
totals 241 + footer 241/30/29/34/29/24/95 so the inherited SWEEP leg is green.

```
STAMP PASS … FILE PASS … SET PASS … ROWS PASS … ONEID PASS … RESTATE PASS … HOSTS PASS hosts=24
LINK PASS … APPEND PASS … NOHARM PASS … SWEEP PASS exit=0 … CAPTURE PASS … TOPIC PASS
ACCEPT-C-67: PASS      (exit 0)
```

Baseline hashes: entry `a2958dbb244e7954656bcae88e3a63fa5cb25b56f8dfb7a5052e8b30ca7a2323`
(42 lines), fixture `corpus/SOURCES.md` `38b25c50…16df`, fixture `corpus/README.md` `2f8a0c2d…1a30`.
Variants and their hashes: `.ufo/waves/round-67/stage/mut-entry/variants/` (+ `MANIFEST.json`);
builder: `.ufo/waves/round-67/stage/mut-entry/gen-fixture.py`.

**The green baseline is itself the strongest finding**: a structurally perfect but wholly
fabricated entry — reserved `example.org` hosts, invented quotes, invented paraphrases, capture URLs
that are nothing but the live URL with an archive prefix — satisfies every leg. ACCEPT-C-67 measures
shape, never sourcing.

## Assigned mutants — predicted vs observed

| # | mutant | predicted catcher | observed catcher | verdict |
|---|--------|-------------------|------------------|---------|
| M1 | missing `- topic:` | FILE, TOPIC | FILE (`topic=False`), TOPIC, **SWEEP** (NO_TOPIC_FIELD) | killed (prediction incomplete: SWEEP also fires) |
| M2 | one `### ` heading | FILE | FILE (`h3=1`) only | killed |
| M3 | 251 lines | FILE | FILE (`lines=251`) only | killed |
| M4 | bullet `… (S805) (S099)` | ONEID | ONEID (`S099:out_of_claim_set`) only | killed |

All four target defects are caught. M2/M3 fail exactly one leg (as predicted), so the file-shape
ceilings are effective but single-leg: a defect there is invisible to every other leg.

## Additional mutants (entry class + receipt)

| # | mutant | observed | verdict |
|---|--------|----------|---------|
| M5 | foreign id **without** parentheses: `(S805), see S099` | **PASS** (exit 0) | **SURVIVED** |
| M6 | duplicate citation on one bullet: `(S805) (S805)` | ONEID (`citations=2`) only; RESTATE blind (per-line `setdefault`) | killed |
| M7 | drop the S828 bullet | ONEID (`citations=0`) + RESTATE (`bullets=0`) | killed |
| M8 | cross-wire bullets S805↔S806 (ids kept, bodies swapped) | RESTATE (`S805:quote_words=0`, `S806:quote_words=0`) only | killed |
| M9 | uncommitted tier flip on a registry row (worktree ≠ lands) | **PASS**, `STAMP PASS … dirty_tracked=True` | **SURVIVED** |
| M10 | extra bullet, fabricated quote, **no citation at all** | **PASS** | **SURVIVED** |
| M12 | 24 rows drawn from only **10 distinct hosts** (repeat host, distinct paths) | **PASS**, `HOSTS PASS hosts=10` | **SURVIVED** |

M6/M8 detail worth routing: RESTATE aggregates bullets per *line* (`setdefault(...).append`), so two
citations in one line still count as one bullet — duplicate detection rests entirely on ONEID's
whole-text count, which is format-sensitive (`\((S\d{3,})\)`). A foreign id written bare, or a
citation in any other bracket style, is invisible to both ONEID and RESTATE.

## Gaps to route to r68 (mutants that PASS the counter)

1. **Fabricated-anchor class passes unconditionally** (baseline + M10). Nothing resolves a URL,
   compares the archive capture to the live body, or checks the anchor quote appears in the source.
   The CAPTURE leg only asserts that the capture URL string equals the live URL string. A row with
   `example.org` + invented quote is indistinguishable from a verified row. Suggested leg: row
   provenance — live host not in a reserved/example TLD set and capture path matching the live path
   *plus* an offline quote-in-capture fixture, or an explicit "unverified source" tier divisor.
2. **Uncited prose passes** (M10): the entry may carry fabricated quotations with no `(S###)` and no
   leg notices; every leg is keyed on the citation regex.
3. **False stamp on a dirty worktree** (M9, and every mutant run — `dirty_tracked=True` while
   `STAMP PASS`). `stamp_ok` checks `rev-parse main == --lands` but not that the evaluated bytes are
   the lands bytes: `FILE/ONEID/RESTATE/TOPIC/SWEEP` read the worktree, `ROWS/CAPTURE` read the
   worktree registry, while only `APPEND`/`BASE` read git. The printed "evaluated revision" is a
   revision *name*, not the measured bytes; `dirty_flag` is computed and then discarded. The claim's
   own receipt discipline ("counters run inside a materialized clone at the lands commit, never a
   moved worktree") is therefore review-enforced, not counter-enforced. Fix: fail STAMP on
   `dirty_tracked`, or read every input via `git show <lands>:<path>`.
4. **Citation-format bypass** (M5): a foreign/extra id is only caught inside ASCII parens;
   `see S099`, `[S099]`, `S099:` all pass ONEID. Fix: count `\bS\d{3,}\b` occurrences outside the
   citation form and fail on any unconsumed id.
5. **Source-diversity floor is 10, not 24** (M12): `HOSTS >= 10` lets 24 mined rows come from ten
   domains; nothing requires distinct registrable domains per row (LINK only forbids byte-identical
   normalized URLs). If the claim means 24 independently mined sources, the leg should be
   `len(hosts) >= len(NEW_IDS)` (or a declared host-count bound).
6. **Tier cell is unconstrained** (M9): `c[3] in ("A","B")` accepts either; no evidence binds a tier
   to a row property, so tier inflation is a cell edit that no leg can see (APPEND explicitly allows
   status/recheck/used-by flips, and ROWS is re-read from the worktree).

## Restoration evidence

- Fixture clone restored: `git reset --hard c6d8c8cd…`; `git status --porcelain --untracked-files=no`
  → 0 lines; entry sha256 back to `a2958dbb…a2323`.
- Lane untouched: HEAD `b78f8b8e…`; tracked status 0 lines;
  `corpus/SOURCES.md` `8811130821ec…e266e`, `corpus/README.md` `f6e0cb8721…252ce` (the README sha
  equals the `readme_sha256` in `telemetry/dry-run-c.txt`), entry file absent.
- Writes confined to `.ufo/waves/round-67/stage/mut-entry/` and `/tmp/r67-mut-entry/`.
- Tool installs: none.

## Addendum — C APPEND vs Ca D4 (CriticFrontier alert, parent resolution)

Confirmed by code read: `accept-c.py` APPEND computes `appended_ids` against BASE and fails on any
id outside `NEW_IDS ∪ EXTRA_IDS` (`S805-S828 ∪ S801-S804`), while `accept-ca.py` D4 requires
`>=2` **rejected** rows `opened 2026-10-24` beyond S801-S804. So a single shared lands commit that
carries Ca's S829+ reject rows makes ACCEPT-C-67 print `APPEND FAIL extra=['S829',…]` no matter how
correct claim C is. L1 ruling: per-claim lands — A_r (S801-S804 + r66 dispositions) < A_c
(S805-S828 only) < A_ca (adds S829+ rejects + lesson). At A_c the bound is satisfied
(`appended=24 extra=[]` in the green baseline above, whose registry has exactly S805-S828 over BASE);
at A_ca claim C must not be re-run. D4's own threshold is `rej_opened_today < len(R66_REJECTS)+2`
i.e. six today-dated rejected rows (S801-S804 plus two), matching the parent's ">=6 at A_ca"; its
`new_rejects` variable is computed and never used.

Probe on the green fixture (same lands `c6d8c8cd`): appending S829+S830 as `rejected` / `2026-10-24`
rows with `REJECTED: flip:` teaches gives

```
STAMP PASS … SET PASS … ROWS PASS bad=[] n=0
APPEND FAIL missing_old=[] appended=26 extra=['S829', 'S830'] immutable_violations=[]
ACCEPT-C-67: FAIL
```

so the conflict is mechanical and would fire at any shared lands, not a draft quality issue.

Residual risk to route to r68: claim C's receipt is only valid at A_c, but nothing in
`accept-c.py` records or checks *which* claim-relative lands it is measuring beyond `--lands`; a
reviewer re-running C at the lane tip (A_ca or later) gets a legitimate-looking `APPEND FAIL` and
could mistake a sequenced-predicate violation for a C defect, or — worse — "fix" it by widening
`EXTRA_IDS`, which would make APPEND blind to any future row appended under a claimed id. The
sequenced predicate is satisfiable only while the receipt pins A_c; the counter cannot express that
pin, so it is review-enforced. Fix candidate: give C a `--lands` that must be an ancestor of the
lane's claim-C receipt commit, or record A_c in claims.json and have the counter print/compare it.

Reproduce: build fixture with `gen-fixture.py <clone-root>`, commit, then per variant
`git reset --hard <lands>; python3 gen-fixture.py <clone-root> <variant>;
python3 -B reports/round-67/accept-c.py --root <clone-root> --lands <lands>`; M9/M12 are registry
rewrites applied uncommitted (documented inline above).
