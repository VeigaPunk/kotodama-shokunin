# CriticPreO — pre-data attack on accept-o.py + check-supersession-settlement.py

Seat: L1-kotodama-r68.CriticPreO. Targets: `tools/check-supersession-settlement.py`
(332 lines, frozen at lane tip) and `reports/round-68/accept-o.py` (frozen, pre-data
rev 0). Every attack below was executed against the committed tool in /tmp/crob;
exit codes and output lines are copied verbatim.

## CONFIRMED BREAKS (tool truthfulness)

### BREAK-1 — pending chain hidden by malformed row: scan prints `chains=0`, exit 0
`parse_registry` (line 85-87) marks any row whose `|`-split does not yield exactly
11 cells as `{"malformed": True}`, and `classify` (line 117) silently skips it.
Fixture: a 10-cell `| S002 | … | supersedes S001 — fix | queued | d | 90d |` row
against a mined S001.

    SETTLEMENT: pending=0 chains=0 usedby_paths=1 missing_paths=0   exit=0

The malformed row produces NO chain line, NO malformed diagnostic, and is absent
from `missing_paths`. The scan's exit code is therefore not just "pending alone"
(the docstring admits that) — it is blind to un-parseable debt. A lands commit that
drops or adds one cell in a pending s-row (all 34 s-ids are in the MUTABLE set for
status/recheck/used-by, but nothing in accept-o checks that only those cells moved)
makes a chain vanish from every leg. No accept-o leg counts malformed rows.
Smallest correction: `classify` should emit a `MALFORMED S###` line and fold
`malformed>0` into the scan exit code and the SETTLEMENT summary; PENDING leg's
regex should require `malformed=0` alongside `pending=0 missing_paths=0`.

### BREAK-2 — SUP_RE phrasing evasion: case/lexeme variants make chains invisible
`SUP_RE = re.compile(r"supersedes\s+(S\d{3,})")` (line 53) is case-sensitive and
literal. `Supersedes S001`, `supersede S001`, `supersedesS001`...:

    | S002 | … | Supersedes S001 — fix | queued | … |    ->
    SETTLEMENT: pending=0 chains=0   exit=0

Also, SUP_RE is searched **only in the teaches cell** — a `supersedes S###` in the
source/access-note cell (the real registry already stores prose like
"(supersedes S367 — …)" inside the *source* cell of S482, line 485 of
corpus/SOURCES.md) is never seen. Today the 34 chains all use the canonical
lowercase teaches-initial phrasing, so pending=34 at base is real; the hole is
forward-looking: a lands-time appended row (NEW_IDS, declared supersedes-appends)
written as `Supersedes` or with the phrase in another cell creates debt the tool
cannot see. Smallest correction: `re.I` + search the full row text (or at least
source+teaches), and report rows matching `/supersed/i` that don't parse as
suspicious rather than absent.

### BREAK-3 — SETTLED-SPLIT accepts a meaningless limiter
`SPLIT_RE = r"for\s+(entry|line|row|cell|clause)\b.{0,40}\bonly\b"` (line 54).
Teaches text `supersedes S001 for cell only` — a limiter that names no scope —

    SETTLED-SPLIT S002>S001 s=mined t=mined same_url=True used_by=1   exit=0

`for row only`, `for clause only`, `for cell only` all satisfy it: the pattern
requires a slice-noun and the word `only` but never that anything specific is
named between them (`.{0,40}` includes zero). Both rows stay mined and the debt
is declared "split". Smallest correction: require at least one non-space token
between the noun and `only` (`\b.{1,40}\S.*\bonly\b` semantics) or an explicit
enumerated-limiter grammar; alternatively gate split rulings to the frozen
KEEP_SETTLED set (S575>S420 is the only legitimate split — any *new* split
outside KEEP_SETTLED should be a finding).

### BREAK-4 — used-by path that exists but never cites: settled-active
`scan` only checks `os.path.exists` on used-by paths (line 162-164, "citation
truth is review work"). S002 mined + used-by `corpus/knowledge/empty.md` (file
exists, cites nothing) + S001 queued:

    SETTLED-ACTIVE S002>S001 … missing_paths=0   exit=0

The docstring promises "A row whose used-by names a path that does not contain
the row's own id is STALE-USED-BY (reported)" — the code never implements this:
`stale` (line 138-144) collects *every* used-by path, not non-citing ones, and
nothing is printed per-stale-row anyway. So a settlement that re-points nothing —
s-status flipped to mined, used-by pointed at any existing file, t-status queued —
reads as settled-active end-to-end. This is the strongest false-settlement vector:
accept-o's PENDING leg then passes on a registry where zero entry re-points
happened. Smallest correction: implement the promised check — for each used-by
path, read the file and require `\bS###\b` of the owning row; print
STALE-USED-BY lines; fold stale>0 into run_pending's required summary.

## CONFIRMED BREAKS (ledger semantics)

### BREAK-5 — validate_ledger never checks that `related` is the chain target
Ledger `S002 | S009 | u | activate | repoint | corpus/knowledge/a.md | bogus`
against a registry where S002 does supersede S001 (not S009):

    LEDGER: rows=1 findings=0   exit=0

`related` is validated only for *shape* (S\d+) and *existence*, never that
`rows[rid]["supersedes"] == related` (or that the pair is a frozen CHAIN_PAIR).
An activate ruling can therefore name the wrong target and still read as a clean
disposition. Composite with BREAK-4: pending=0 + findings=0 + full id coverage
while no actual re-point/settlement occurred anywhere.

### BREAK-6 — ruling/status consistency checked on `id` only, direction-agnostic
`S001 | S002 | u | activate | …` — activate ruled on the *target* row (S001 mined
in fixture) — `findings=0 exit=0`. The status checks (lines 206-212) ask only
"is the row the ruling names in the right status" — activate↔mined, retire↔
rejected, keep-reject↔rejected — never whether that row is the s-side. The
L1 activate-on-queued control *is* correctly flagged
(`LEDGER-FINDING L1:S002:activate_but_status=queued`, exit 1 — verify verbatim),
so the cell-flip check works; it is just direction-blind.

### BREAK-7 — keep-* rulings are vacuous; empty related/evidence accepted
`S002 | | u | keep-successor | none | | ` → `findings=0 exit=0`.
keep-successor, keep-split, and keep-reject (status check aside) carry no
semantic validation: an all-`keep-successor` ledger over the full required id
set passes the LEDGER leg's `findings=0` + coverage + no-dup requirements while
ruling nothing. The claim is saved only because PENDING must independently print
0 — i.e. the ledger's evidentiary value is coverage-only by construction. Worth
a leg note in claims.json ("review_only" already says this — low priority);
the fixable part is requiring `related` for activate/retire rulings.

## accept-o.py instrument gaps

- **No tool pin.** SHA leg compares live-tool sha to `lands:` blob — proves the
  measured file is committed, not that it equals the declared instrument.
  `claims.json` freezes the *source text* conceptually but no leg hashes the
  declaration-time tool. A selectively-weakened tool (e.g. SUP_RE gutted to
  `r"(?!)"`, or `classify` special-casing the 34 real chains while the fixture
  still behaves) passes SELFTEST+EXEC+MUT — mutants are generated from the
  lands tool itself, so weakening and the "non-mutant" reference degrade
  together. Smallest correction: freeze `sha256(tools/check-supersession-settlement.py)`
  in claims.json at T0 and add a TOOL-PIN leg comparing lands blob to it.
- **PENDING trusts tool stdout.** `run_pending` regex-matches the tool's own
  summary; the counter never re-derives pending count from SOURCES.md itself.
  Combined with no tool pin, this is a single point of trust.
- **LEDGER leg doesn't require `related` pairing for chain s-ids.** Coverage is
  set-membership only; ruling quality is "review-only" per separability note —
  acceptable if the tool's validate_ledger is fixed (BREAK-5/6), structural
  otherwise.
- **Un-tracked-files hole (minor).** `dirty` check uses `--untracked-files=no`;
  an untracked `tools/check-supersession-settlement.py` shadowing would matter
  only if git checkout semantics allowed it — a clone materialization makes it
  moot, and SHA leg reads the working file; on a moved worktree an untracked
  replacement tool would change live_sha vs lands blob → SHA leg catches it. Not
  exploitable.

## Attack surface NOT exploitable (verified)

- activate-on-queued → correctly flagged (L1 verbatim above).
- Ledger field count, bad id, dup id, ghost id, bad ruling token — all flagged
  (selftest covers the ghost/dup path; bad ruling `bogus-ruling` exits 1 in the
  MUT leg design).
- STAMP leg fails-closed: `git rev-parse main` unresolvable → STAMP FAIL →
  early return before any other leg. Moved-worktree PASS requires evaluated==stamped.
- `--scan` on missing registry exits 2 (selftest unreadable-exit-2 PASS).

## Impacted axes / smallest safe corrections

Operability claim O as specified ("scan classifies every chain") is overstated
wherever a chain can hide (BREAK-1/2) or fake-settle (BREAK-3/4); the ledger's
"0 findings" is currently direction- and linkage-blind (BREAK-5/6/7). All seven
breaks are fixable defects inside the tool + one leg addition, not tradeoffs the
Rust judge must reject:

1. malformed → visible + counted (BREAK-1);
2. SUP_RE case-insensitive, searched across the row, unmatched `supersed*`
   reported (BREAK-2);
3. SPLIT_RE requires named content or restrict split to KEEP_SETTLED (BREAK-3);
4. implement the promised STALE-USED-BY citation check and gate it (BREAK-4);
5. validate_ledger: `related` required for activate/retire and must equal the
   row's own `supersedes` target or the frozen pair's counterpart (BREAK-5/6/7);
6. accept-o: TOOL-PIN leg vs a claims.json-frozen tool sha (instrument gap).

If only one fix lands before integration: BREAK-4 — it is the difference between
"the registry claims settlement" and "the corpus actually re-pointed."

Installs/updates: none (system Python + repo tool only).
