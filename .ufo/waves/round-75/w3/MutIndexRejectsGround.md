# W3 mutation probe — INDEX, REJECTS, GROUND

**Verdict: INCONCLUSIVE (probe not executed).**

Scratch clone: `/fast/scratch/hyaku/kotodama-r75/MutIndexRejectsGround/tmp.9XFNA7itgI/lane`, checked out at `4f5e3b2535c2c06c51627dc2736c40183847cae1`; toplevel matched the required clone path. Frozen claims blob SHA-1 at freeze and claim-C both matched: `e54df48240fea66dee854da0907d2ec58246127d`. Counter SHA-256: `315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261`.

## Pristine detector run

Command used the scratch clone, required `--lands` and `--freeze`, and scratch-only `--work`. Actual result: `ACCEPT-C-75: FAIL legs=12/13`; INDEX, REJECTS, and GROUND all PASS, but unrelated CENSUS failed because `scripts/sources-census.sh` was absent from this scratch clone. This is a baseline failure, so the requested mutation outcomes cannot be classified under the mutation protocol. No mutant was applied; consequently no per-mutant output is available.

## Requested cases (not run)

| Mutant | Expected leg | Fired legs |
|---|---|---|
| README row order swap | INDEX | not run — baseline inconclusive |
| paraphrased README row | INDEX | not run — baseline inconclusive |
| duplicated README row | INDEX | not run — baseline inconclusive |
| README row moved to another section | INDEX | not run — baseline inconclusive |
| latest footer total 251 | INDEX | not run — baseline inconclusive |
| latest footer vector transposed | INDEX | not run — baseline inconclusive |
| older footer edited | INDEX | not run — baseline inconclusive |
| row appended in trailing block outside sections | INDEX | not run — baseline inconclusive |
| extra section heading | INDEX | not run — baseline inconclusive |
| trailing space in README row | INDEX | not run — baseline inconclusive |
| triage count 3/6/30 | REJECTS | not run — baseline inconclusive |
| lesson prose lists family names without reasons | REJECTS | not run — baseline inconclusive |
| delete S870 disposition | REJECTS | not run — baseline inconclusive |
| change Quarantine verdict count | REJECTS | not run — baseline inconclusive |
| flip dash in refused-family row | REJECTS | not run — baseline inconclusive |
| global-only reason sentence | REJECTS | not run — baseline inconclusive |
| receipt names 807-row registry | GROUND | not run — baseline inconclusive |
| fragment's zero changed to 1 | GROUND | not run — baseline inconclusive |
| delete a fragment line | GROUND | not run — baseline inconclusive |
| base registry already names a fragment | GROUND | not run — baseline inconclusive |

No mutant bytes were introduced, so restoration is exact by non-mutation. Scratch clone and run outputs were retained at report creation; scratch cleanup was not performed because the baseline blocker prevented completing the assigned probe.