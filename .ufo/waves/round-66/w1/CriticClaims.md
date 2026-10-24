# CriticClaims — round-66 v2 cross-claim audit of claims.json

Seat: CriticClaims (attack/calibration). Target: reports/round-66/claims.json
predicates + counters + frozen controls. Read-only audit; no repo mutation.

## Answers to the three assigned questions

**(1) Causally separable in practice? Mostly no for Ca.** C and O verify
standalone (each counter reads its own lands; O's legs are self-contained
fixtures). Ca does not: D2 consumes `final-measures-{c,o,ca}.txt` — receipts
that only exist after all three counters have run and been receipted — and
D4 consumes `separability-real.txt`, which can only be *produced* by O's
upgraded tool (the declared check `--jobs 4 --timeout 120 --budget 300` uses
flags the base tool refuses, per controls-o.txt). claims.json declares
Ca→REC but the REC receipt mechanism converts a real Ca→O production
dependency into a file read: the manifest's expected_findings name only the
land-path/acceptance class, not the tool-provenance chain. claims.json's own
separability note says undeclared Ca→O is "a real defect." Additionally the
separability instrument is O's claim object — the checker measuring claim
separability is itself inside the claim set under adjudication
(self-reference). And `reports/round-66/separability-manifest.json` does not
yet exist on disk (REC land, pending): the declared check cannot currently
run, so all separability claims are prospective, not demonstrated.

**(2) Same axis twice? The axes are distinct (coverage/operability/
calibration), but the underlying work items are not.** Two routed items are
claimed on two axes each:
- R65-D4: O claims the fix ("capability hardening"); Ca claims the
  disposition record (leg D4). Same defect, two claims.
- S776 supersession repair: C's statement claims it inside C's registry
  lands ("registry 701 -> 725+ rows including the S776 supersession repair
  and disposition rows"), while Ca's D1 owns the actual deliverable bytes
  (games-entry citation swap + s753-recapture.txt are Ca lands). See F3 —
  this is not just double-booking, it is a counter contradiction.

**(3) Claim O restates the defect as the claim — yes, and it is repair
inflation.** The statement opens verbatim with the R65-D4 defect text then
arrows into the fix ("R65-D4: tools/check-claim-separability.py timed out at
its 600s per-run cap ... -> the upgraded tool returns a verdict inside a
round's budget"). Returning a verdict in-round is the instrument's baseline
contract, not a new capability; the closure routed this as a defect to
repair. The genuinely novel content is the honest-partial semantics
(SEPARABILITY_PARTIAL exit 2, UNRESOLVED naming, bounded --max-runs) — real
but a repair-hardening increment, not an axis move. Worse, the claim was
already satisfied pre-data — see F1.

## Findings

### F1 (HIGH): O's do-nothing control is invalid — claim saturated pre-wave
Evidence: `git status` shows ` M tools/check-claim-separability.py` and
`?? reports/round-66/` — the upgrade and the whole claim package are
uncommitted, `main` == base 94209e8f. Yet telemetry/dry-run-o.txt records
`ACCEPT-O-66: PASS` (all 9 legs: SELFTEST 63/63, DIFF diff_lines=428,
MUT mutants=4, FIXTURES lanes=2). accept-o.py's DIFF leg is `git diff BASE`
— worktree vs base — so the counter measured uncommitted upgrade bytes.
The controls clause requires each counter FAIL on a base-bytes tree before
data; the recorded O dry-run is a PASS, and controls-o.txt is a narrative
--help inspection, not a counter run. Two defects: (a) the frozen control
was executed against post-land bytes — a do-nothing tree demonstrably
passes O; (b) O's lands (upgrade + 4 mutants) were already in the worktree
before the wave opened — the claim carries zero verifiable in-round delta
and a counter that cannot observe commit-state (DIFF on worktree, unlike
C's `git diff BASE main`). Impact: operability axis integrity, controls
discipline, premature saturation.

### F2 (HIGH): hidden Ca→O dependency laundered through REC receipts
Evidence: accept-ca.py:156-161 D4 greps separability-real.txt for
`^SEPARABILITY: \d+ findings$` + `acceptance_runs=` + no PARTIAL; the file
is a committed receipt producible only by the upgraded tool (declared check
flags refused at base per controls-o.txt). expected_findings declares only
"Ca->REC via land path 'final-measures-c.txt'" and the generic acceptance
class — it does not name the O-tool provenance. The same laundering applies
to D3 (seat-evidence.txt) and D1 (s753-recapture.txt): Ca's counter cannot
distinguish a real bounded run from a hand-written receipt matching the
regex (false-provenance surface). Correction: declare the production
dependency explicitly in expected_findings (Ca→REC *produced-by* O), or add
a provenance check (e.g., receipt must carry the upgraded tool's sha/output
shape the base tool cannot emit).

### F3 (HIGH): S776 repair double-claimed; C's APPEND contradicts C's statement
Evidence: accept-c.py:271-278 APPEND implements strict line-set append-only
(`missing_old = [l for l in base_set if l not in tip_set]`; any edited old
line FAILs) while the leg text (claims.json:22) allows "status/used-by flips
logged in the lesson." If the S776 supersession flips S776's registry row
(used-by re-point to the games entry — part of Ca's D1 repair), C's APPEND
FAILS exactly when Ca's repair lands. If SOURCES.md is untouched, C's
statement clause "including the S776 supersession repair" describes bytes C
never lands (the games-entry edit is a Ca land; NOHARM merely allowlists it,
accept-c.py:281-287 — permissive, not a check). Either reading yields a
defect: C not separable from Ca's deliverable, or C's statement overclaims.
Correction (smallest): drop the supersession clause from C's statement (it
is Ca's claim), implement the leg-text flip allowance in APPEND, and mark
the games-entry NOHARM allowance as a declared Ca-land, not silent slack.

### F4 (MED): manifest needs_git mislabel for O
Evidence: claims.json:113 `"O": {... "needs_git": false}` but accept-o.py
runs `git diff BASE` (DIFF leg) and builds temp git lanes (FIXTURES via
`git init`). Under a needs_git-provisioned overlay O's counter fails
spuriously — the manifest would manufacture false findings. Also noted:
C's NOHARM and Ca's D2 measure committed history while FILE/ROWS/etc. read
worktree bytes — mixed provenance inside single counters; during the wave
(uncommitted) NOHARM is vacuously true (dry-run-c.txt: `NOHARM PASS diff=[]`).

### F5 (LOW): Ca QUOTES is satisfiable on phantom ids
accept-ca.py:174-177 greps the lesson for ids S776-S800 (regex covers
S776-800, requires >=25 distinct) but never checks they exist in
SOURCES.md. If C's rows never land, Ca still passes while its Gate names
nonexistent rows — cross-claim coherence hole, not a separability violation
(the dep runs text→text, no land read).

## Smallest safe corrections (ordered)
1. Re-run O's control honestly: counter against a base-bytes checkout of the
   tool, record FAIL before data; keep upgrade unlanded until after.
2. claims.json: drop S776-repair from C's statement; declare Ca→O production
   dep for D4 in expected_findings; fix O unit `needs_git: true`.
3. accept-c.py APPEND: implement the used-by/status flip allowance the leg
   text already promises, or tighten leg text to strict append-only.
4. accept-ca.py D4: require a token only the upgraded tool emits
   (e.g., `SEPARABILITY:` line plus --budget-era fields), not just regex shape.
5. Commit separability-manifest.json before any separability verdict is cited
   as evidence.

## Tooling
No installs performed; repo evidence sufficed (git status/diff, file reads).

Report: .ufo/waves/round-66/w1/CriticClaims.md
