- Seat: A03 | verifier | claim A | date 2026-10-19 | baseline 9bccc9b

# A03 — independent verification of A01 (scope watch + bleed scan)

## Verdict

**A01 had not landed at verification time**, so this fragment is an
independent reproduction of the evidence base A01's scope/bleed claims rest
on, not a verdict on A01's written assertions. `reports/round-38/adj/` did not
exist when this seat sampled (`ls reports/round-38/adj` → No such file or
directory, twice, including the final pre-write sample); the only round-38
bytes were `claims.json`, `targets.json`, and the two telemetry files. A01's
claim-specific comparison is therefore owed (see `## Owed`).

Everything I could reproduce independently reproduces. The pre-dispatch tree
is exactly the declared baseline, no out-of-lane path is Git-visible, and each
bleed surface A01 is meant to scan behaves as the r36/r37 records say.

## Independent reproduction

Method: read-only Git census; `sha256sum`; and gates executed **only** in
`git archive HEAD` copies under `.scratch` (never in-tree; no
`reports/round-*/run-validation.py` run; no `--freeze`).

| surface | A01/origin assertion | my independent result |
|---|---|---|
| baseline | HEAD is `9bccc9b` | `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` |
| tracked cleanliness | no tracked change | `git diff --name-status 9bccc9b` empty; `git diff --cached --name-status` empty; `git diff --stat 9bccc9b` empty |
| untracked scope | all round-38 | `git status --short --untracked-files=all` = 4 rows, all `?? reports/round-38/…`; zero non-round-38 rows |
| r33 census | 90/79 | `da68a6d` total=90 report=79 |
| r34 census | 83/79 | `4a7aede` total=83 report=79 |
| r35 census | 92/78 | `ce103bf` total=92 report=78 |
| r36 census | 47/43 | `57c8409` total=47 report=43 |
| r37 census | (this round's own) | `fa90c77` total=77 report=75; `9bccc9b` total=1 report=0 |
| out-of-lane paths | none | no `.ufo/` or `tools/gates/frozen/` path in any of the six commits; r37 non-report paths = `LOG.md`, `corpus/README.md`; `9bccc9b` = `SCORECARD.md` only |
| frozen bytes | pinned | `git diff --name-status HEAD -- tools/gates/frozen/` empty |
| roster asymmetry | packet 13 vs read set 12 | `D4_COMPONENTS` = **12** members (`tools/exercise-handoff-e2e.py:157-170`); packet manifest = **13** component rows (`examples/culture-d4/packet.d4.yml:2876-2888`); r7 read set (`reports/round-34/handoff/declared-in-r7/expected.json` `inputs`) = **12** D4 component rows, `13-register-law.yml` absent |
| 13th component pin | digest matches | live `examples/culture-d4/components/13-register-law.yml` = `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` = the packet manifest pin; archive copy same |
| r7 packet pin | `45f57132…` | `sha256sum reports/round-34/handoff/declared-in-r7/packet.md` = `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| r7 twin pin | `0e229138…` | `sha256sum …/twin.json` = `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599` |
| baseline legs | green | isolated copy: `argot-derivation-gate.py examples/culture-d4/packet.d4.yml` exit 0 (`records=187 register_scoped=14 derived_pairs=8 violations=0`); `register-law-gate.py …` exit 0 (`law_rows=5 findings=0`); `typed-pipeline-gate.py …` exit 0 (`20/20 legs passed`) |
| v3 chain | exit 0, packet pin held | isolated `exercise-handoff-e2e.py --profile v3 --quiet` exit 0, `links=105/105 packet_sha256=45f57132…` |
| gate selftests | green | isolated: `register-law-gate.py --selftest` → `45/45 checks passed`; `argot-derivation-gate.py --selftest` → `27/27 checks passed` |

## Bleed surfaces (claim A scan targets)

- **F-6 counters absent (confirmed).** `grep -rl 'derived_forms\|derived_ok' examples tools --exclude-dir=__pycache__` → exit 1, no match, matching the r36 K01 census (`reports/round-36/scout/K01-register-scout.md:115,210-211`). The only producer under a live name is `derived_pairs` (`tools/gates/argot-derivation-gate.py:567,917`); the live coverage block carries no derivation counters (`examples/culture-d4/typed-labels.d4.yml:29-47`). So the round-38 D claim's declared *before* state holds.
- **RL-8 era leg absent (confirmed).** `register-law-gate.py` checks only RGL-05 *row presence* (`:107-112,403`); it has no era concept, and `examples/culture-d4/components/13-register-law.yml:57` states the era leg (RGL-05) is "specified and unimplemented". The D claim's second residue is real.
- **Read-set roster defect carried (confirmed).** It is filed in the r37 defect queue as rows `R36-R7-READSET-13` and `r37-A01-readset-roster-defect`, both `carried-with-owner` (`reports/round-37/op/defect-queue.json`). The round-38 O claim targets exactly this.
- **Named D/O artifacts — baseline digests recorded** (integrator diffs these post-landing; this seat does not verify un-landed drafts): `tools/gates/argot-derivation-gate.py` `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`; `tools/gates/register-law-gate.py` `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169`; `examples/culture-d4/typed-labels.d4.yml` `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`; `tools/exercise-handoff-e2e.py` `bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`.
- **Scope/credential sweep of the round-38 drafts (clean).** The only `oauth` occurrences are the lane name `xai-oauth` (`claims.json:8`; `telemetry/dispatch-declared.json:7`; `telemetry/availability-attempt-1.json:6`); no `bearer`/`authorization`/`api-key`/`secret`/`token`/`password` value is present. `freshness_pause_in_force: true` and `no freshness axis-move` non-goal are present (`claims.json:11,26`).

## Limits

This is a Git-visible census: it does not observe untracked filesystem writes outside the repository, and it sampled the tree at one time per command, so counts are time-specific and not reconstructable later (same limit r37 A03/A06 recorded). It is also a pre-dispatch snapshot; A01's landed fragment may have been written after my last sample, and nothing here validates its prose.

## Owed

- `reports/round-38/adj/A01-scope.md` (A01's landed fragment) did not exist at verification time; the claim-specific comparison of A01's written scope census and bleed findings against the reproduction above is owed to the integrator (or a re-run of this seat once A01 lands). This seat's own output is `reports/round-38/adj/A03-verify.md`.

## Citations

- Binding rules and my out path: `reports/round-38/targets.json:3-8` (shared rules; A01 row `adj/A01-scope.md`, A03 row `adj/A03-verify.md`); `reports/round-38/claims.json:25-30`; `REGIMEN.md:60-69`.
- Roster asymmetry: `tools/exercise-handoff-e2e.py:157-170,1939-1953`; `examples/culture-d4/packet.d4.yml:2876-2888`; `reports/round-34/handoff/declared-in-r7/expected.json` (`inputs`, 12 D4 component rows).
- F-6 residue: `reports/round-36/scout/K01-register-scout.md:115,210-211`; `reports/round-36/validation.json:53,165` (D rejected, stale premise); `tools/gates/argot-derivation-gate.py:567,917`; `examples/culture-d4/typed-labels.d4.yml:29-47`.
- RL-8 era leg: `examples/culture-d4/components/13-register-law.yml:49,57`; `tools/gates/register-law-gate.py:107-112,403`; `reports/round-27/law/impl-8.md:68`.
- Carried defect rows: `reports/round-37/op/defect-queue.json` (`R36-R7-READSET-13`, `r37-A01-readset-roster-defect`).
- Command outputs reproduced in this report: `git rev-parse HEAD`, `git diff`/`git diff --cached`/`git diff --stat 9bccc9b`, `git status --short --untracked-files=all`, `git diff-tree --no-commit-id --name-status -r --no-renames` for `da68a6d 4a7aede ce103bf 57c8409 fa90c77 9bccc9b`, `sha256sum` of the r7 pair and the four named artifacts, and isolated `git archive HEAD` runs of the argot/law/typed gates, both gate selftests, and `tools/exercise-handoff-e2e.py --profile v3 --quiet`. No in-tree `run-validation.py` and no `--freeze` was executed.
