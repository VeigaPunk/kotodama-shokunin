# MutLandedC — claim C mutation probe

Verdict: **PARTIAL** — completed M1 only; M2–M14 were not executed, so no full claim verdict is established.

## Baseline

Ran the specified `python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2535c2c06c51627dc2736c40183847cae1 --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 --fleet-root /home/vgpnk/Projects/shokunin` inside the scratch clone. Output: `ACCEPT-C-75: PASS legs=13/13`, exit 0. Stamped/evaluated/measured revision was `4f5e3b2535c2c06c51627dc2736c40183847cae1`.

## Mutation table

| Mutant | Expected red leg | Fired legs | Killed? |
|---|---|---|---|
| M1: deleted the S890 `source:` line from `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` | ROWS (used-by no longer matches citing entry) | ROWS only; 12/13 pass | Yes |
| M2–M14 | Not run | — | — |

M1 mutant commit: `1a17ba2d2f5df5497331525637ddc738630fd674` (fixture identity). Mutated-file SHA-256: `a9d2a74351bca898b20de57e89d0a397c36a4b29dfde975901355bc773575057`. Restored lands-file SHA-256: `3ea4d6f80715460423fada252499dac9a95010a3bb4dd292c7ea834eab78fc13` (matches pristine pre-mutation hash). The scratch clone was reset to the lands commit after the run.

No tools were installed.
