# MutLandedCa — claim Ca mutation probe

Baseline at landed Ca commit `012e8d3c8b92f47c734f735d58d118d574fe6a14`, freeze `5d0167464309d8133991b30f7d7a7011a6a0fd14`, combined `4f5e3b2535c2c06c51627dc2736c40183847cae1`: **PASS 12/12**, exit 0. Counter SHA-256: `98d8e7974c82d048db67fe8eebd06cd78308bc0e3233c922ec16f527fd1ac235`.

All mutants were child commits in the scratch clone with local `main` pinned to each mutant and `--lands` set to that commit; the combined revision remained fixed. Each counter invocation used the same `--freeze`, `--combined`, and `--fleet-root`.

| Mutant | Expected detector / behavior | Fired output | Killed? |
|---|---|---|---|
| M1 correction row new token changed 44→45 | ANNOTATE/NOSTUB | exit 1, FAIL 10/12; ANNOTATE, NOSTUB | Yes |
| M2 delete correction row L75-08 | ANNOTATE/NOSTUB | exit 1, FAIL 10/12; ANNOTATE, NOSTUB | Yes |
| M3 remove leading pair id L75-09 | ANNOTATE/NOSTUB | exit 1, FAIL 10/12; ANNOTATE, NOSTUB | Yes |
| M4 remove a line from SCORECARD.md (the round-75 append-only introduction) | APPENDONLY | exit 0, PASS 12/12 | **No — survived** |
| M5 edit filed LOG.md line in place (43→42) | APPENDONLY | exit 1, FAIL 11/12; APPENDONLY | Yes |
| M6 revert SKILL.md corrected narrative wording to base line | REPAIR | exit 1, FAIL 11/12; REPAIR | Yes |
| M7 edit SKILL.md outside a REPAIR line | APPENDONLY | Not run: fixture edit matched no text, so no mutant commit was made | Inconclusive |
| M8 edit r74 receipt PASS denominator 11/11→10/11 | RECEIPTS | Not run | Inconclusive |
| M9 delete r74 receipt | RECEIPTS | Not run | Inconclusive |
| M10 edit pre-existing SOURCES teaches cell | APPENDONLY | Not run | Inconclusive |
| M11 edit pre-existing SOURCES used-by cell only | Must remain green (rule-2 exemption) | Not run | Inconclusive |
| M12 edit reports/round-75/ledger.json | FROZENCFG | Not run | Inconclusive |
| M13 revert README linguistics heading (32→30) | REPAIR | Not run | Inconclusive |

The detected defect is M4: removing a prose line from SCORECARD.md outside the protected/checked ranges survived because it was not a removed line in the frozen protected set and did not affect correction rows. The required full M1–M13 sweep is **PARTIAL**: M7 fixture construction failed because its chosen search text (`## Skills`) was absent; execution stopped before M8–M13. M4 was a line removal (not an in-place replacement). Scratch clone and fixture bytes remained under `/fast/scratch/hyaku/kotodama-r75/MutLandedCa/`; no tool installation.