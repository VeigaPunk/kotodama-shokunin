# RevOContract — round-79 W1 seat report (O predicate contract review)

Seat: RevOContract (reviewer, lane leaf). Scope: the O claim predicate and each of
its clauses; reject unsupported universal security/coverage claims. No shared files
edited; all artifacts under `.ufo/waves/round-79/w1/stage/RevOContract/`.
Base: `44f76d456c1b326a71ffdb381590af825cbf11be` (lane read-only throughout).

## Evidence basis (all executed this seat, raw output preserved)

- `stage/RevOContract/probes/recon-2026-10-30.txt` — P1 guard absent at base
  (`git cat-file -e 44f76d45:tools/ledger-token-guard.py` → exit 128);
  P2 S897 row count 0 at base, last registry id S896; P3 the drifted token
  `…amend-2026-10-24-r13.md` never existed in any commit (`git log --all` empty);
  P4 registry S884 used-by at the recorded round-78 revision `4b255745…` is
  `…amend-2026-10-23.md` while `reports/round-78/telemetry/census-end.txt:33`
  records `…amend-2026-10-24-r13.md` (the mismatch the O/Ca records build on);
  P5 census-end sha256 `05b5011a…` matches
  `reports/round-79/telemetry/baseline-census-mismatch.json`; P9 `4b255745` is an
  ancestor of base (exit 0).
- `stage/RevOContract/probes/fixture-measure.txt` — verbatim observe outputs
  behind every truthful `observed_at_base` in the fixtures, run against an isolated
  fixture repo (root verified before its single commit; the only git mutation this
  seat performed).
- Committed ancestor evidence read (not re-run): `.ufo/waves/round-77/w2/MutCaLedger.md`
  (mutant table incl. the HEAD survivor e1), `ScoutLogPairs.md` (D01–D10 fabricated
  observations, D11 not-red-at-base), `corpus/lessons/round-78.md` R78-M1 and routed
  defects 2/3, `reports/round-76/accept-ca.py` (H2 guard, REV_NAMES at :1070).

## Clause map

Delivered at `stage/RevOContract/o-clause-map.md`: O0–O8, one row per clause with
its mechanical check, its red fixture, its executed red-before, and its named
review-only residue. Load-bearing check: no clause is redundant; O4/O5 are disjoint
classes (fabricated record vs void correction); O2/O3 are disjoint refusal channels.
Review-only clauses that claims.json must name (QUALITY 11): observation-to-statement
*pertinence* and approval provenance (O1), per-pair parse fitness (O4), the physical
definition of `stated_token` until frozen (O5), counter independence of judgment (O6),
S897 tier fit (O8 — RevSource seat owns the row itself).

## Findings — unsupported universal security/coverage claims, rejected or bounded

- **F1 (HIGH, must-fix at freeze). "refuses … constant printers" is claimed
  universally; universality is unsupportable.** Detecting whether an arbitrary
  command constant-prints is undecidable; QUALITY 11 requires each clause be shown
  able to fail, and a universal clause can never be shown satisfied. Bounded
  supportable form (and the only executed precedent): refuse the frozen classes —
  shell-string `observe_cmd`, interpreter argv[0], echo/printf/true printers
  (QUALITY 25 J4), J4b-style evasive printers reading no clone byte — each
  demonstrated red (`fx-mut-echo-b`, `fx-mut-pyprint-b`, `fx-mut-shellstring-b`).
  Claims.json must carry the bounded wording, not the universal one.
- **F2 (HIGH, must-decide at freeze). "refuses mutable revisions" is stronger than
  the only executed ancestor grammar.** The round-76/77 grammar *accepted* `HEAD`
  (and `HEAD^`, `HEAD~1`, `@`) in revision position — MutCaLedger e1 SURVIVED with
  `LEDGER-CHECK-77: PASS` exit 0; root cause `REV_NAMES=("HEAD","HEAD^","HEAD~1","@")`
  at `reports/round-76/accept-ca.py:1070`. `HEAD` is a mutable ref. As drafted, O's
  sentence therefore requires the guard to refuse the HEAD class (`fx-mut-headrev-b`
  must be red). If ExecGuard instead admits HEAD, the sentence must narrow to
  "branch/tag names refused; HEAD admitted" — MutCaLedger §2 documents exactly this
  contract delta for the ancestor round. One of the two must be frozen; the draft
  text as written binds option (a).
- **F3 (MEDIUM). "immutable committed bytes" is a pinning chain, not a git
  property.** Supportable only as: 40-hex commit id + commit-object type check
  (a tree/blob id is 40-hex and immutable but is not a commit — `fx-mut-treerev-b`
  must be refused) + reads only via git at that revision + repo pinned (a different
  repo's commits are also "committed bytes") + tree hash pinned (QUALITY 17) + run
  at `--lands`, never the worktree (QUALITY 19). Claims/receipt language implying
  bytes are self-evidently immutable is an overclaim.
- **F4 (MEDIUM). "approved read-only observations" — "approved" needs a frozen
  operational definition.** The only mechanical content available: frozen-at-freeze
  argv + the structural grammar (allowlist argv[0], `git -C <pinned>` first, `--`
  before paths, 40-hex revision position). Whether an observation is *pertinent* to
  what its statement asserts is not mechanically decidable (ScoutLogPairs D01–D10
  passed every structural check while observing something unrelated to the pair's
  statement). Pertinence and approval provenance must be declared review-only in
  claims.json; a predicate claiming mechanical pertinence coverage is unsupported.
- **F5 (MEDIUM). "not historical truth certification" is the right disclaimer —
  keep it, and reject any security framing that drifts from it.** The guard grades
  committed bytes at a pinned revision; it gives no resistance to history rewriting
  (force-push/rebase) and no authentication of authorship. Any receipt or SKILL
  registry wording presenting the guard as a security boundary (tamper-evidence,
  attack resistance) is an overclaim. Related: "bounded" (O0) is unreviewable until
  SentinelLimits' bound table (input bytes, pair count, argv length, wall timeout,
  output cap, UTF-8) is frozen.
- **F6 (LOW, verified). No external-source or knowledge-coverage claim rides on
  O.** S897 has zero rows at base (last id S896) so the own-work row is free; the
  O claim touches no corpus/knowledge path; the draft's own disclaimer is accurate.
  Contractual note only: if the frozen claims.json O row or S897's used-by cell
  points into corpus/knowledge or cites an external URL, that is a new claim
  requiring its own gate — flag at freeze review.

## Fixtures delivered (all under `stage/RevOContract/fixtures/`)

13 contract fixtures + generator + README: one clean truthful ledger (green
baseline; every observation measured verbatim), 11 single-field mutants mapped to
clauses (c), (d), (b), (a), and the do-nothing + duplicate-id controls. Expected
verdicts are stated per file; `make-fixtures.py` regenerates the set deterministically
from the clean ledger; `commands.md` reproduces the fixture repo (commit
`362e71615521ddb23f1af02306251a9262a1acdb`) byte-for-byte.

## Residual risk / verification gaps

- I did not run the guard (it does not exist at base and implementing it is
  ExecGuard's seat; running an unbuilt implementation check is exactly what this
  seat must not claim). Fixture verdicts are contract expectations, not observed
  pass/fail.
- The r77-e1 evidence is committed-ancestor text I read, not re-executed; re-running
  that probe needs the round-77 candidate check environment (noted in MutCaLedger
  as w2-scoped). The code-path citation (`accept-ca.py:1070`) is verified from
  committed bytes at base.
- F2's resolution (guard refuses HEAD vs sentence narrows) is a freeze-owner
  decision; this seat records that the draft text binds the stricter reading.
- Tool installs: none (no installs or updates performed; nothing to record).

Checks for L1 to run after integration: execute the 13 fixtures against the landed
guard and confirm each expected verdict; run `accept-o.py` do-nothing and junk
controls (QUALITY 25) at the freeze commit; confirm claims.json carries the F1
bounded wording and the F2 decision.
