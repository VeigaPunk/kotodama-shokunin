# O claim clause map — RevOContract (round-79 W1)

Source sentence under review (CLAIMS-DRAFT.md, O paragraph):

> "O / operability: acquire a bounded ledger-token guard for this lane's calibration
> records. It re-runs approved read-only observations against immutable committed
> bytes; refuses mutable revisions/constant printers; rejects an observed_at_base
> differing from the actual observation and rejects stated_token equal to the actual
> observation. Success: committed red/green fixtures, mutation controls, selftest and
> independent acceptance counter all pass at lands. The target is one working guard
> (base: absent), not historical truth certification. Own-work source S897 will cite
> the opened R77 mismatch evidence; no external-source or new knowledge coverage claim."

"Actual observation" below means, per pair: the stdout of that pair's own frozen
`observe_cmd` re-run at the ledger's frozen 40-hex base revision, reduced by that
pair's frozen `parse`. Any other reading makes O4/O5 vacuous.

| # | Clause (draft words) | Mechanical check (the command/shape that grades it) | Red fixture (this stage) | Red-before evidence (executed, committed) | Review-only residue (name it, QUALITY 11) |
|---|---|---|---|---|---|
| O0 | "acquire a bounded ledger-token guard … (base: absent)" | `git cat-file -e <base>:tools/ledger-token-guard.py` fails at base (probe P1: exit 128); at lands the path exists, is executable, and ships a `--selftest` receipt committed pre-dispatch (QUALITY 23) | do-nothing landing without the tool | probe P1, probes/recon-2026-10-30.txt | "bounded" is an unreviewable adjective until the bound table (input bytes, pair count, argv length, wall timeout, output cap, UTF-8) is frozen; SentinelLimits seat owns the table — until then O0 is only half-checkable |
| O1 | "re-runs approved read-only observations against immutable committed bytes" | guard executes each pair's `observe_cmd` only after the structural grammar passes (argv array, argv[0] in frozen read-only allowlist, `git -C <pinned repo>` first, `--` before paths, revision position = the frozen 40-hex); reads only via git at that revision; the worktree is never read; the run happens at `--lands` in a materialized clone or over `git show <rev>:<path>` bytes (QUALITY 19) | fx-mut-shellstring-b, fx-mut-pathtrav, fx-mut-optinject (+ fx-mut-treerev-b with O2) | reports/round-76/accept-ca.py H2 guard + `_git_grep_problem` role parsing (read-only, lines ~989–1092); MutCaLedger c1/c2/d killed | "approved" has no mechanical test beyond frozen-at-freeze argv + grammar: whether an observation is *pertinent* to its statement (does the command measure what the statement asserts?) is not decidable by shape — approval provenance and pertinence are review-only and must be named as such in claims.json |
| O2 | "refuses mutable revisions" | every revision operand must match `^[0-9a-f]{40}$`, resolve to a **commit** object in the pinned repo, and equal the frozen base; symbolic refs refused: branch names, tags, `HEAD`, `HEAD^`, `HEAD~N`, `@`, `:/…`, `v1.2^{…}` | fx-mut-headrev-b, fx-mut-branchrev-b, fx-mut-treerev-b | **HEAD-class survived the only executed ancestor grammar**: `.ufo/waves/round-77/w2/MutCaLedger.md` e1 SURVIVED (`LEDGER-CHECK-77: PASS`, exit 0) because `REV_NAMES=("HEAD","HEAD^","HEAD~1","@")` at reports/round-76/accept-ca.py:1070; e2 (`main`) killed | none, *if* the refused set is enumerated; see finding F2 — as drafted the sentence is stronger than the ancestor grammar, so the guard must refuse HEAD or the sentence must be narrowed |
| O3 | "refuses … constant printers" | argv[0] ∈ frozen read-only allowlist; no shell string `observe_cmd`; no interpreter argv[0]; the frozen printer fixtures refused | fx-mut-echo-b (J4), fx-mut-pyprint-b (J4b) | QUALITY 25 fixtures J4/J4b; MutCaLedger c1 (`python3 -c print` killed), c2 (`echo` killed) | universal "refuses constant printers" is UNSUPPORTABLE (undecidable for arbitrary commands); supportable form is fixture-bounded, see finding F1 |
| O4 | "rejects an observed_at_base differing from the actual observation" | per pair: re-run `observe_cmd` at frozen base, apply frozen `parse`, string-compare to recorded `observed_at_base`; any inequality (or a re-run exit ≠ 0) → reject the pair | fx-mut-fabobs-c | R78-M1 (corpus/lessons/round-78.md): ScoutLogPairs.md D01–D10 carried recorded `"1"` vs actual `"149"` and passed structural check; routed defect 3 says the fix is not yet shown able-to-fail — this clause is exactly that demonstration, so the red-before must be *executed* at W2, not cited as hypothetical | the frozen `parse` per pair must actually capture the token: a wrong-but-frozen parse makes a pair vacuously green; parse fitness is review-only |
| O5 | "rejects stated_token equal to the actual observation" | per pair: the stated old token (frozen field, or parsed from `stated_text` at `stated_at` — the definition must be frozen) vs the re-observed token; equality → reject the pair (no mismatch exists; do-nothing/lying correction) | fx-mut-nomismatch-d | ScoutLogPairs.md D11: stated 243 = observed 243, "not red at base"; round-77 CLAIMS-DRAFT kill rule "any ledger pair not red at base" | which physical field is `stated_token` (field vs parse of `stated_text`) must be frozen; MutVacuous/RevMalformed seats probe the boundary; review-only until frozen |
| O6 | "Success: committed red/green fixtures, mutation controls, selftest and independent acceptance counter all pass at lands" | guard `--selftest` receipt (verdict line + exit + counter sha256) committed at freeze and run at the freeze commit too (QUALITY 23); accept-o.py takes required `--lands <40hex>`, `--freeze <40hex>`, explicit `--work`; every constant read via `git show <freeze>:…`; LEGCOUNT refusal when its leg table differs from frozen `legs[]`; junk/control receipts red-before; grading at `--lands`, never the worktree (QUALITY 19) | fx-donothing (empty pairs), the full mutant set, counter-level junk fixtures (J-set) | QUALITY 25(b) junk receipt discipline; round-73/74 red-befores | "independent acceptance counter" = authored by a seat other than ExecGuard: provable from the wave roster, but independence of *judgment* is review-only |
| O7 | "The target is one working guard … not historical truth certification" | exactly one new tool path lands for O; zero changes under corpus/knowledge; O's claims.json row names no external source and no knowledge-coverage axis | any second tool path or knowledge touch → ENTRIES-scope fail | probe P2: S897 has 0 rows at base (last id S896) — the id is free for the own-work row | the disclaimer itself is honest and load-bearing; see finding F5 on what it must not be read as |
| O8 | "Own-work source S897 will cite the opened R77 mismatch evidence; no external-source or new knowledge coverage claim" | S897 lands as an own-work registry row whose evidence cells quote the lane-internal R77 W2 records verbatim (ScoutLogPairs/MutCaLedger) and whose `used-by` does not point into corpus/knowledge | S897 already present at base (probe P2: 0) or citing an external URL | probe P2; `.ufo/waves/round-77/w2/ScoutLogPairs.md`, `MutCaLedger.md` exist and are quoted | "opened" for an internal row means the cited records exist at the pinned revision and the quote matches byte-for-byte — review-only once the row is drafted (RevSource seat owns the tier) |

## Load-bearing check (draft requirement: each clause load-bearing)

- O4 and O5 are independent failure classes with disjoint fixtures (fabricated record vs void correction); removing either re-opens a routed defect (R78-M1 / D11).
- O2 and O3 are independent refusal channels (revision position vs argv[0]); removing either re-opens e1/J4 classes.
- O1 is the execution substrate; without the "re-run at frozen revision" semantics, O4/O5 have no oracle.
- No clause is redundant; no two clauses collapse to the same check.

## Overclaim rejections (unsupported universal security/coverage claims)

See the report `.ufo/waves/round-79/w1/RevOContract.md` findings F1–F6 for the full text.
Short form: F1 constant-printer universality is fixture-bounded, not universal;
F2 "mutable revisions" must include the HEAD class or the sentence narrows;
F3 "immutable" is a pinning chain, not a property of git alone;
F4 "approved" needs its frozen operational definition, pertinence stays review-only;
F5 the guard is a calibration checker, not a security boundary (no history-rewrite resistance claim);
F6 zero external-source / knowledge-coverage claims ride on O — verified S897 free at base.
