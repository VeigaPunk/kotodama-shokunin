- Seat: A11 | verifier | claim A | date 2026-10-19 | baseline 57c8409

# A11 — final adjacency audit assembly draft

**Status: dependency-limited draft for integrator finalization; no claim-A verdict.** Claim A covers rounds 33–37 and requires evidence-backed per-surface verdicts, adjudication of the r7 13-component asymmetry using an isolated-copy re-render comparison, re-verification of the eleven r35/r36 corpus entries, and routed-not-absorbed contested scope (`reports/round-37/claims.json:25-34`). This draft separates historical leads from round-37 verification; missing evidence is not treated as a pass.

**Snapshot.** `git rev-parse HEAD` → `57c8409ba16d9f9e692297198d95e8f2ce5a1937`, matching the declared baseline (`reports/round-37/claims.json:6-7`). `git status --porcelain` → `?? reports/round-37/`. The first fragment scan found only `A05-receipt.md`; the latest scan found A01, A03, A04, A05, A07, A09, A10, and this A11 draft. A02, A06, and A08 remain absent (Glob outputs, 2026-10-19). A05 labels its own content dependency-limited and makes no adjacency verdict (`reports/round-37/adj/A05-receipt.md:3-5,14-24`).

## 1. Per-surface assembly table

| Surface / required decision | Draft disposition | Evidence and limit |
|---|---|---|
| r7 packet vs frozen read set: does the current render faithfully reproduce the frozen pair, and is the 13-component asymmetry a defect or documented skip? | **PAIR RENDER VERIFIED; READ-SET ROSTER DEFECT (A01 result; independent verification pending)** | A01's isolated archive re-render produced packet and twin bytes identical to the filed r7 pair; the 13th D4 component is in the packet manifest but absent from `D4_COMPONENTS`/the frozen inputs. A01's isolated mutation control showed the separate manifest-digest check detects changed component bytes transitively. A07's chronology finds no documented skip and shows the omission predates r7 (`reports/round-37/adj/A01-freeze-adjudication.md:5-31`; `A07-gap-fill.md:7-19`). This is a read-set roster/completeness defect, not a demonstrated integrity bypass; no filed r7 bytes were changed or re-frozen. |
| Ten r35 corpus entries plus the r36 timekeeping entry: cross-domain language and couples resolution | **TO-VERIFY** | A10 provides the ten r35 entry paths and the r36 timekeeping entry (`reports/round-37/adj/A10-scribe.md:11-15`); A02's required cross-domain/couples scan is absent, so neither “clean” nor “zero dangling couples” is established (`reports/round-37/targets.json:50`; `claims.json:27-30`). |
| Git-based write-scope census across rounds 33–37 | **PASS, GIT-VISIBLE CENSUS ONLY (A03 result)** | A03 found no out-of-lane paths in the r33–r36 commit census and only round-37 report-tree untracked paths at its sample; tracked diff from the baseline was empty. Its method cannot establish absence of arbitrary external filesystem writes (`reports/round-37/adj/A03-scope.md:5-9,13-24`). |
| Contested scope: bilateral read, current contract digest, freshness pause | **VERIFIED ROUTED, NOT ABSORBED (A04 seat result; independent verification pending)** | A04 measured the live contract digest as `5f4c02bf…`, matching the kotodama-side read record, while the cited Lore record is informational and names `50c4c2f2…`; Lore's L0 row says no current acknowledgement exists. A04 therefore does not claim a bilateral read of the live digest. The round-37 freshness pause remains active; no threshold or contract-version ruling is made (`reports/round-37/adj/A04-contested.md:5-16`; `claims.json:9-11,32-34`). |
| r33 D3 computational snapshot invalidation (distinct from A01's r7 D4 question) | **REPRODUCED; CARRY FORWARD, NOT FIXED** | A09 re-ran the frozen coupling check at HEAD: exit 2 with one `D3-SNAPSHOT` mismatch (`4e24bd3b…` declared vs `adfd7895…` current); the unfrozen check exits 0. A09 recommends carrying the existing owner and record-only disposition; do not call this surface green or conflate it with the D4 component asymmetry (`reports/round-37/adj/A09-gap-fill.md:5-24,26-28`; prior finding `reports/round-35/adj/audit-assembled.md:280-293`). |
| All audited surfaces / zero unfiled bleed | **NOT ESTABLISHED** | A02's bleed/couples scan and independent verifiers are still missing. A01, A03, A04, and A09 cover only their assigned slices; no overall green or zero-unfiled-bleed claim follows (`reports/round-37/targets.json:49-56`; `claims.json:28-30`). |

## 2. Integration notes

- Keep three evidence classes distinct: r37 seat re-runs, prior-round findings carried forward, and unresolved items. A01's isolated comparison now adjudicates the render pair and read-set asymmetry; A06/A08 still need to independently verify the relevant commands and conclusion.
- A10 supplies a descriptive change census for rounds 33–36, including the exact ten r35 entry paths and the r36 timekeeping entry; it explicitly is not a bleed or per-surface audit (`reports/round-37/adj/A10-scribe.md:5-21`). Use it as the population inventory, not as evidence that any entry passes.
- A09 independently reproduced the pre-existing D3 snapshot invalidation and routes it as a carry-forward finding, separate from A01's D4 read-set asymmetry. Preserve the `D3-SNAPSHOT` red and the existing owner; do not repair or relabel it green in this draft (`reports/round-37/adj/A09-gap-fill.md:5-28`).
- A04 reports the contested scope remains routed: the current contract digest differs from Lore's older informational digest, no current bilateral acknowledgement is claimed, and the freshness pause remains active. The open digest/version choice and freshness-threshold ruling remain with the integrator/operator (`reports/round-37/adj/A04-contested.md:5-16`).
- Integrator should fold A01/A03's evidence and A02's eventual scan into the complete surface table, then reconcile each relevant result against A06 and A08's independent verification. Preserve named mismatches and routed items; do not smooth them into a green summary.
- No `reports/round-*/run-validation.py` was run; no filed r7 freeze operation or protected-path write was performed (`reports/round-37/targets.json:4-8`; `A01-freeze-adjudication.md:9-22`).

## Owed

- `reports/round-37/adj/A02-entries-bleed.md` — cross-domain language and couples-resolution re-scan of all eleven entries.
- `reports/round-37/adj/A06-verify.md` and `reports/round-37/adj/A08-verify.md` — independent verification results needed before the integrator finalizes per-surface verdicts.
- Integrator: route the r7 read-set roster/documentation correction to a future baseline revision; do not rewrite or re-freeze the filed r7 pair (`reports/round-37/adj/A01-freeze-adjudication.md:31,33-35`).
- Integrator: carry the D3 snapshot invalidation with its existing owner and record-only disposition, or file a separately evidenced remedy decision; the frozen check remains red (`A09-gap-fill.md:26-28`).
- Integrator/operator: adjudicate the `5f4c…` versus `50c4…` contract-digest/version question and freshness-threshold ruling; A04 reports the current state as routed, not resolved (`A04-contested.md:13-16`).
- Integrator finalization of the full audit remains open; this fragment is not an acceptance, canon, clearance, promotion, or closure decision (`reports/round-37/claims.json:32-34`; `targets.json:54,56,59`).

## Citations

- `reports/round-37/claims.json:6-7,25-34` — declared baseline, claim-A scope/threshold, and non-goals.
- `reports/round-37/targets.json:4-8,49-59` — shared rules and A01–A11 assignments.
- `reports/round-37/adj/A01-freeze-adjudication.md:5-31,33-45` — isolated re-render, pair comparison, asymmetry adjudication, and follow-up.
- `reports/round-37/adj/A03-scope.md:5-24,26-36` — git-visible scope census and its external-write limitation.
- `reports/round-37/adj/A04-contested.md:5-16,18-24` — live digest comparison, bilateral-read state, freshness pause, routed disposition.
- `reports/round-37/adj/A05-receipt.md:3-5,14-24,26-40` — dependency-limited receipt at its earlier cut.
- `reports/round-37/adj/A07-gap-fill.md:7-19,21-24` — omission chronology and no documented-skip evidence.
- `reports/round-37/adj/A09-gap-fill.md:5-24,26-36` — reproduced D3 snapshot invalidation and carried disposition.
- `reports/round-37/adj/A10-scribe.md:5-21,23-40` — descriptive change census and explicit limits.
- `reports/round-36/scout/K01-register-scout.md:145-181` — prior-round 13-vs-12 freeze/read-set signal and transitive verifier behavior.
- `reports/round-34/handoff/declared-in-r7/freeze.txt:1-10`; `tools/exercise-handoff-e2e.py:157-170` — filed freeze summary and D4 component tuple.
- `reports/round-35/plan/P01-c-plan.md:155-166` — ten r35 corpus-entry slugs; `SCORECARD.md:660` — r36 timekeeping entry.
- `reports/round-35/adj/audit-assembled.md:347-360` — historical contested-scope routing and freshness pause.
- Command outputs (2026-10-19, repo root, `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD` → `57c8409ba16d9f9e692297198d95e8f2ce5a1937`; `git status --porcelain` → `?? reports/round-37/`; first `Glob reports/round-37/adj/*.md` → `A05-receipt.md` only; latest scan → A01, A03, A04, A05, A07, A09, A10, A11; A02/A06/A08 absent at that scan; no round runner or filed r7 re-freeze command executed.
