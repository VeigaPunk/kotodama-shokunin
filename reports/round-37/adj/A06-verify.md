- Seat: A06 | verifier | claim A | date 2026-10-19 | baseline 57c8409

# A06 — independent verification of A01–A04

Baseline rechecked: `git rev-parse HEAD` → `57c8409ba16d9f9e692297198d95e8f2ce5a1937`. I did not run any `reports/round-*/run-validation.py` and did not use `--freeze`. The A01 verification and mutation control ran only in temporary `git archive HEAD` copies under `.scratch`; no baseline or filed r7 bytes were written.

## Findings

### A01 — rerender and D4 read-set asymmetry

The filed r7 packet/twin digests match the committed baseline: `sha256sum` reports packet `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` and twin `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`; `expected.json` records those same values. Independently, this safe isolated command passed:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
workdir=$(mktemp -d "$TMPDIR/a06-r7-verify.XXXXXX")
trap 'rm -rf "$workdir"' EXIT
git archive HEAD | tar -x -C "$workdir"
(cd "$workdir" && python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --json)
```

Output: exit 0; 58 input digests matched; 26/26 component digests and 8/8 D4 pins matched; packet and twin checks matched the two SHA-256 values above; 105/105 links resolved. A separate temporary archive with an appended comment in `13-register-law.yml`, run with `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` (no `--freeze`), exited 1 with `E2E-DIGEST` for that component. The roster asymmetry is also directly visible: `D4_COMPONENTS` has 12 paths (`tools/exercise-handoff-e2e.py:157-170`), r7 `expected.json:146-157` has 12 D4 component inputs, while the packet manifest has 13 (`examples/culture-d4/packet.d4.yml:2875-2888`). The current verifier traverses the packet component maps (`tools/exercise-handoff-e2e.py:2208-2222`), so the evidence supports A01’s verdict: the frozen pair re-renders to the pinned digests; the 13th path is omitted from the direct read-set roster, not a documented skip, but its component digest is checked transitively.

A01’s filed `--freeze`/`cmp` invocation was not repeated: `--freeze` is expressly forbidden for this verification. The non-freezing verifier independently checks the generated packet and twin digests against the pinned expected values; it is not a reproduction of the prohibited invocation itself.

### A02 — eleven entries, couples, and language scan

The two stated corpus-delta commands reproduce ten round-35 additions (`git diff --name-status 4a7aede ce103bf -- corpus/knowledge`) and one round-36 addition (`git diff --name-status ce103bf 57c8409 -- corpus/knowledge`). Independent read-only measurement matched A02’s per-entry reference counts and SHA-256 prefixes. Applying the exact `LANG_TOKENS` / `LANG_ALLOW` / `LANG_FRAME` predicate cited from `reports/round-34/run-validation.py:283-308` to the eleven entry files produced 0 affirmative frame hits; the round-34 runner itself was not executed.

There is a resolution-method discrepancy, not a proven missing-file set. Using the documented resolver in `reports/round-19/audit/entry-audit.py:74-96` yields 319/334 direct path resolutions and 15 unresolved basename-only refs in `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`, matching K04’s output. A02’s separately declared unique-corpus-basename fallback finds exactly one matching file for each of those 15: 334 per-entry refs, 319 direct, 15 unique fallback, 0 ambiguous, 0 unresolved after fallback. Thus the target files exist uniquely, but they do not resolve under the documented three-base resolver. Whether the extra fallback is an accepted `couples:` rule remains unadjudicated; A02’s reported `0 unresolved` is contingent on that fallback and should not replace the strict-resolver finding until the integrator resolves the policy. Also, 334 is the sum of per-entry-deduplicated refs; a global union contains 222 distinct path strings (112 repeated occurrences).

The separate “PROVINCE-derived” lexical-family scan is described only by its categories, not by exact patterns or a runnable command, so its zero counts are not independently reproducible from A02. K04 additionally records coupling and person-scope interfaces requiring integrator routing (`reports/round-37/scout/K04-entries-scout.md:47-65`); these are filed findings, not proof of unauthorized ownership or canon claims. A02’s narrow lexical predicate does not settle those adjacency issues.

### A03 — Git scope census

The four cited round commits’ `git diff-tree --no-commit-id --name-status -r --no-renames` path counts and report-tree counts reproduce exactly: r33 `90/79`, r34 `83/79`, r35 `92/78`, r36 `47/43`; each non-report path list matches A03. At the current pre-A06 snapshot, `git diff --name-status 57c8409` and `git diff --cached --name-status` were empty; `git status --short --untracked-files=all` had 57 rows, all `?? reports/round-37/...`. A03’s earlier 20/40-row snapshots are time-specific and cannot be reconstructed from this later moving tree. The Git-only limitation on external filesystem writes is correctly stated.

Boundary note: `git log cdd66d7..57c8409` includes one additional non-round commit, `139e3b6`, deleting `.ufo/reports/round-32/kotodama.md`. That path is outside A03’s stated r33-r36 round-commit census; the reproduced counts remain valid for those four target commits, but the result must not be read as a claim that the entire raw Git interval contains no `.ufo` path.

### A04 — contested contract and freshness pause

`sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` reproduces the live digest `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`. Lore’s K1 record names `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1` and explicitly labels it informational, not ratification (`lore-shokunin/.ufo/waves/round-93/K1.md:4-5`); Lore’s current L0 row says it holds no acknowledgement and asks for the digest/revision ruling (`lore-shokunin/l0-questions.md:6`). A fresh `git -C <lore> grep -n -e 'kotodama-lore-adjacency' HEAD -- corpus` returned no matches (exit 1); a read-only search of the Lore tree for the current `5f4c…` digest found none. Contract §1 requires both lanes’ same-digest records (`corpus/knowledge/synthesis/worldbible-integration-contract.md:14-16`), so bilateral acknowledgement remains unverified and contested scope remains routed.

The freshness pause is confirmed: round-37 claims set `freshness_pause_in_force: true`, omit freshness from `axes_in_play`, and list “no freshness axis-move” as a non-goal (`reports/round-37/claims.json:9-11,32-34`); `REGIMEN.md:27-33` keeps the pause pending operator ruling. A04 does not claim to absorb that axis or make a Lore/canon decision.

**Overall:** A01, A03, and A04 evidence is reproduced within the limits above. A02’s narrow language predicate and fallback result are reproducible, but its couplings verdict conflicts with the documented resolver and its broader lexical scan lacks a reproducible predicate. Claim A therefore still has an adjacency-method/routing question; do not treat the current evidence as an unconditional clean pass.

## Owed

- Integrator: decide and document whether unique corpus-basename fallback is permitted for `couples:`; otherwise normalize the 15 basename-only refs in `sacred-kingship-mythic-charter.md:37` and rerun the documented resolver. Clarify whether the count is per-entry refs or globally distinct targets.
- Integrator: route K04’s named funerary/afterlife, afterlife/world-end, bathing/fire, timekeeping/fire, and binding-speech/kingship coupling/scope findings (`reports/round-37/scout/K04-entries-scout.md:59-65`); keep unresolved ownership contested rather than absorbed. A02’s broad lexical screen needs its exact predicates/command if its zero-count is used as closure evidence.
- Integrator: route A01’s direct read-set roster/documentation correction to a future baseline revision; preserve the declared-in-r7 bytes.
- Integrator/operator: resolve the live `5f4c…` versus Lore-recorded `50c4…` contract digest and same-revision read/acknowledgement; keep freshness paused pending the operator ruling.

## Citations

- Assignment, baseline and no-freeze/no-runner rules: `reports/round-37/targets.json:3-8,49-54`; `reports/round-37/claims.json:25-34`.
- A01 evidence: `reports/round-37/adj/A01-freeze-adjudication.md:7-31`; `tools/exercise-handoff-e2e.py:157-170,1937-1963,2208-2222,3811-3966,4643-4690`; `reports/round-34/handoff/declared-in-r7/expected.json:124-195`; `examples/culture-d4/packet.d4.yml:2875-2888`.
- A02/K04 evidence: `reports/round-37/adj/A02-entries-bleed.md:7-47`; `reports/round-37/scout/K04-entries-scout.md:11-43,47-65`; `reports/round-19/audit/entry-audit.py:31-42,74-96`; `reports/round-34/run-validation.py:283-308` (read for its predicate only); `corpus/QUALITY.md:13-20`.
- A03 evidence: `reports/round-37/adj/A03-scope.md:5-36`; reproduced `git diff-tree` outputs for `da68a6d`, `4a7aede`, `ce103bf`, `57c8409`; `git show 139e3b6` → delete `.ufo/reports/round-32/kotodama.md`.
- A04 evidence: `reports/round-37/adj/A04-contested.md:5-24`; `reports/round-33/adj/contract-read-record.md:1-9`; `corpus/knowledge/synthesis/worldbible-integration-contract.md:14-16`; `REGIMEN.md:27-33`; Lore read-only records `lore-shokunin/.ufo/waves/round-93/K1.md:4-5` and `lore-shokunin/l0-questions.md:6`.
- Commands/results reproduced in this report: isolated non-freeze v3 verifier and mutation control; SHA-256 measurements; round-35/36 corpus diffs and 11-entry inline resolver/language-predicate audit; four-commit Git path census; current Git status and diff checks; Lore corpus grep and read-only digest search.
