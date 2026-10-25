# ScoutAdj — r69 w1 adjacency scan: supersession / registry-correction-chain / SOURCES-governance surfaces across sibling lanes

Seat: ScoutAdj (leaf, read-only), kotodama round 69 wave 1, 2026-10-24.
Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base `793f79746712a79f915bb481215e54bbea8b5e7a`).
Question: does any sibling lane own a supersession/registry-correction-chain or
SOURCES-registry-governance surface that kotodama's planned
`### Registry correction chains` SKILL.md decision table (claim D2) would
duplicate — i.e. does the table stay in-lane or bleed?

Method: fleet-root enumeration, marker greps for `supersedes S`, `SOURCES.md`,
`correction chain`, `settlement`, plus heading/taxonomy-uniqueness greps and
targeted reads. Read-only everywhere; no production bytes touched; nothing
installed (none needed — the RULES.md gate was therefore not exercised).

## Key trap found and corrected

The nested `*-shokunin/` lanes are **gitignored from the fleet root**
(fleet `AGENTS.md:6`, `:31`). Default ripgrep searches from
`/home/vgpnk/Projects/shokunin` therefore **skip every lane repo**: the first
`supersedes S` sweep returned 291 hits and **zero** lane-internal paths, and
`correction chain` returned exactly one fleet-runtime hit. Any adjacency scan
that stops there would falsely report "clean fleet". All lane-internal
conclusions below come from `include_ignored` searches and per-lane reads.

## Marker matrix (lane-internal surfaces only)

### `supersedes S` — sibling lanes use the same row contract on their OWN registries

- `chousa-shokunin/corpus/SOURCES.md:39-42` (live registry, 7 such rows):
  `| S029 | Cochrane Handbook ch. IV … | supersedes S019 — Cochrane reviews
  should be assessed periodically … | mined | … | corpus/knowledge/metadata-screen-r25.md, …`
  — chousa's own rows in chousa's own repo.
- `kama-shokunin/SKILL.md:759`: "S078–S086 (superseding S066–S074).
  Historical source rows and prose remain" — a real multi-row chain in kama's
  registry; `kama-shokunin/SKILL.md:1004` "Superseded registry reading."
- `mado-shokunin/SKILL.md:606` (gate `mado-source-merge`, selftest asserts
  "`supersedes` policy"); `:624` (probe `mado-supersede-sweep`, ledger
  `.ufo/waves/round-19/supersessions.json`, rows S090/S096, scope incl.
  `SKILL.md`, `PROVINCE.md`, `tools/*`) — mado-owned SOURCES governance.
- `tameshi-shokunin/SKILL.md:1573` ("A stale expected row is replaced by later
  evidence | Keep its raw observation and explicitly supersede the row"),
  `:1829` ("A registry row stops holding its admitted outcome |
  `registry-check.py` reports `differs`, exit 1 | A row leaves `active` only
  as `superseded` with `superseded_by`, and still runs"), `:1841`
  (`REGISTRY_CHECK: held=N/M superseded=K`) — tameshi's 2-state registry
  lifecycle as decision-table rows in tameshi's own SKILL.md.
- `tabi-shokunin/SKILL.md:2128`: "#### Registry correction — supersedes
  :2098-2102 exit, kind, invocation and write-scope cells" — nearest prior art
  BY NAME, but it is a single corrective section superseding cells of tabi's
  own earlier table, not a chain-state taxonomy. `:1614`: tabi's own
  `check-sources.mjs` census gate selftest includes "a `supersedes` correction
  that must stay clean, an `S0010`-vs-`S001` id-boundary case".
- `kagi-shokunin/.ufo/waves/round-23/falsify/CritSupersession.md:1-7`: critic
  seat auditing that kagi rows "carry their supersession only as prose
  (`supersedes S0NN —` in `teaches`)" — runtime evidence siblings actively
  govern this contract; not an owned standing surface.
- `kotoba-shokunin`: zero matches for `settlement|supersedes S` in
  SKILL.md / corpus/SOURCES.md / corpus/knowledge/*.md / PROVINCE.md.

### `settlement` — a HOMONYM, not a competing owner

- `kaidoku-shokunin/tools/round-30/settle-gate.py:2`: "Seat-settlement gate
  (round-30; round-29 routed defect 4 …)" — settles dispatched wave seats
  (`.ufo/waves/round-N/settle.tsv`) against swarm registries. Disjoint concept.
- `chousa-shokunin/.ufo/waves/round-44/make-settle-tables.py:2`: "build the
  round-44 wave settlement tables" — seat outcomes. Runtime only.
- No sibling owns any standing tool whose name matches `*supersess*` /
  `*settle*` outside `.ufo` runtime (`find` over all lanes returned only
  `.ufo/waves/...` files plus kaidoku's seat gate).

### `correction chain` — no lane-owned table

- Fleet-level: `.ufo/waves/shokunin-train-20261101-w17/tasks/g3d-scribe.md:5`.
- Lane-internal (`grep -ril` over `*-shokunin`, excl `.git/.jj/worktrees/
  node_modules`, 35.9 s, 10 files): nearest is
  `game-dev-3d-shokunin/reports/round-86/r86-scribe.md:208` —
  "### 5. r84-scribe's 12-vs-11 correction chain" — a leg-COUNT correction in
  a round report, not a registry chain. `audio-shokunin/LOG.md:1240,1263`
  ("Correction chain: critic F1 …") — critic-finding bookkeeping. Remaining
  hits are `.ufo/waves/` runtime files (kaidoku, mado, mori, tameshi) and
  kotodama's own r69 wave critiques.

### `### Registry correction chains` heading and the five-state taxonomy — unique to kotodama

- `grep 'Registry correction chains' --glob '**/SKILL.md'` (include_ignored,
  completed, 11.7 s): **no matches** in any lane. All 88 fleet hits are
  kotodama's own `.ufo/waves/round-69/w1/prompts/*` and wave files.
- `grep 'settled-split|chain-left-pending|entry-not-repointed|retired-row-mined|closed-chain-kept|scope-limiter-missing'`
  (include_ignored, partial at the tool's 20 s): 41 results, **all kotodama**
  (`tools/`, `reports/round-68/*`, `reports/round-69/*`, `.scratch/smoke/*`,
  `.ufo/waves/round-69/*`). Zero sibling paths.
- Taxonomy source is kotodama-owned:
  `tools/check-supersession-settlement.py:6-22` (docstring: SETTLED-ACTIVE /
  SETTLED-RETIRED / SETTLED-CLOSED / SETTLED-SPLIT / pending + STALE-USED-BY),
  `classify()` at `:112-137`. `reports/round-69/accept-d.py:35-37` freezes the
  heading and the five states the table must carry.

### Fleet-level SSOT is operator-owned, not sibling-owned

- `CORPUS.md:116-118`: "Append-only. … A correction is a new row whose
  `teaches` opens `supersedes S0NN —`." `scripts/sources-census.sh` validates
  registries fleet-wide. Fleet `AGENTS.md:31`: each lane owns its own
  `SKILL.md`, `PROVINCE.md`, `corpus/`; `:79-81`: lane edits to operator-side
  fleet files are out of scope — name the correction in the round report.

## Verdicts

- VERDICT: NO-DUPLICATE-OWNER — no sibling lane owns a supersession /
  registry-correction-chain decision table, the `### Registry correction chains`
  heading, or the five-state chain taxonomy (`pending`, `settled-active`,
  `settled-retired`, `settled-closed`, `settled-split`) and its five error
  signatures. Nearest prior art is per-lane and weaker in kind:
  tameshi's `active→superseded_by` lifecycle rows
  (`tameshi-shokunin/SKILL.md:1573`, `:1829`, `:1841`), tabi's
  `#### Registry correction` corrective section
  (`tabi-shokunin/SKILL.md:2128`) and census `supersedes` selftest case
  (`:1614`), mado's supersedes-policy gate + supersede-sweep ledger
  (`mado-shokunin/SKILL.md:606`, `:624`), kama's supersession chains
  (`kama-shokunin/SKILL.md:759`), chousa's live `supersedes S0NN` rows
  (`chousa-shokunin/corpus/SOURCES.md:39-42`).
- VERDICT: IN-LANE — the kotodama table stays in-lane and does not bleed. It
  documents kotodama-owned code (`tools/check-supersession-settlement.py`),
  cites a kotodama registry row (S859, used-by SKILL.md), and lands in
  kotodama's own SKILL.md. No sibling file, tool, or section is superseded,
  shadowed, or duplicated by it.
- VERDICT: HOMONYM-RISK (informational) — "settlement" already names
  SEAT-settlement gates in sibling lanes (`kaidoku-shokunin/tools/round-30/
  settle-gate.py`, `chousa-shokunin/.ufo/waves/round-44/make-settle-tables.py`).
  kotodama's names already carry the qualifier (`supersession-settlement`);
  keep the `supersession-` qualifier in any cross-lane prose so the two
  concepts are not conflated.
- BLEED GUARD — if D2's guidance were ever promoted into fleet operator files
  (`CORPUS.md`, `PROTOCOL.md`), that WOULD bleed: `CORPUS.md:118` already
  holds the operator-owned supersedes row contract and fleet `AGENTS.md:79-81`
  forbids lane edits there. Keep the table inside kotodama SKILL.md; if the
  fleet ever wants it, name the correction in the round report instead.

## Evidence limits

- Two fleet-wide `include_ignored` greps hit the tool's 20 s cap on sibling
  `.git/.jj`/sandbox trees and returned PARTIAL result sets (labeled above).
  The no-duplicate-owner verdict rests on the COMPLETED SKILL.md-scoped
  heading grep (zero sibling matches) plus the all-kotodama state/signature
  grep and targeted per-lane reads — not on the truncated sweeps alone.
- The `correction chain` lane scan excluded `.git`, `.jj`, `worktrees`,
  `node_modules` (grep -r, completed in 35.9 s); sandbox copies under
  `kagi-shokunin/.ufo/.../sandboxes/` were deduplicated by eye.
- No sibling SKILL.md was read end-to-end; sibling conclusions rest on the
  quoted marker lines, which were all read with line numbers from real grep
  output (quotes above are verbatim excerpts).

## Commands (exact, with representative real output)

```
ls -1 /home/vgpnk/Projects/shokunin                  # 20 *-shokunin lanes + operator files
Grep 'supersedes S' /home/vgpnk/Projects/shokunin            -> 291 hits, 0 lane-internal (lanes gitignored)
grep -oE '...-shokunin/[^:]+' <saved-output> | sort | uniq -c  -> (empty)
Grep -i 'correction chain' (default ignores)                  -> 1 hit: .ufo/waves/shokunin-train-.../g3d-scribe.md:5
Grep -i 'supersed' --glob '**/SKILL.md' (include_ignored)     -> 3620 hits (partial); chousa:86,91,105,134 / kama:511,561,647,694,759,836,881,935,1004-1005,1227,1318 / mado:248,495,519,606,624,737,789,810,851,1804-1805,1846,1872,1920,1928,1977 / tameshi:737,1064,1192,1360,1558,1573,1597,1635,1681,1698,1828,1829,1838,1841,1869,1932,2055,2082 / tabi:786,803,809,911,1017,1029,1204,1463,1542,1591,1614,1623,1719,1794,1989,2015,2045,2105,2128,2148,2255,2351 / tsukuroi:127,217,463,467,510,549,558,627
Grep -i 'supersed' --glob '**/SOURCES.md' (include_ignored)   -> 12804 lines saved (row-level hits across lanes)
Grep -i 'settlement' --glob '**/*-shokunin/**' (include_ignored) -> 8967 hits (partial); lane surfaces: kaidoku tools/round-30/settle-gate.py, chousa .ufo/waves/round-44/make-settle-tables.py + w*-settle.tsv, mado SKILL.md:495(pacman pause context)/others runtime
Grep 'Registry correction chains' --glob '**/SKILL.md' (include_ignored) -> no matches (COMPLETE)
Grep 'Registry correction chains' (include_ignored)           -> 88 hits (partial), shown 20/20 = kotodama .ufo/waves/round-69/w1/prompts/*
Grep 'settled-split|chain-left-pending|entry-not-repointed|retired-row-mined|closed-chain-kept|scope-limiter-missing' (include_ignored) -> 41 results (partial, 20s), all kotodama paths
grep -ril --include='*.md' --exclude-dir=.git --exclude-dir=.jj --exclude-dir=worktrees --exclude-dir=node_modules 'correction chain' *-shokunin
  -> audio-shokunin/LOG.md; game-dev-3d-shokunin/reports/round-86/r86-scribe.md;
     kaidoku (2, .ufo runtime); kotodama (3, own wave critiques); mado (1, .ufo);
     mori (1, .ufo); tameshi (1, .ufo)
find *-shokunin -type f \( -iname '*supersess*' -o -iname '*settle*' \) (pruned .git/.jj/worktrees)
  -> only .ufo runtime files + kaidoku-shokunin/tools/round-30/settle-gate.py
Read: reports/round-69/accept-d.py; tools/check-supersession-settlement.py:1-140;
      kaidoku tools/round-30/settle-gate.py:1-30; chousa .ufo/waves/round-44/make-settle-tables.py:1-25;
      kagi .ufo/waves/round-23/falsify/CritSupersession.md:1-14; CORPUS.md:108-125; fleet AGENTS.md
Grep 'settlement|supersedes S' kotoba-shokunin/{SKILL.md,corpus/SOURCES.md,corpus/knowledge/*.md,PROVINCE.md} -> no matches
```

All observations read-only; the only file written by this seat is this report.
