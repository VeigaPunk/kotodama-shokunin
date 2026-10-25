# Round-73 counter revisions (append-only; claims.json is not edited)

| rev | file | sha256 | when | change | predicate |
|---|---|---|---|---|---|
| r1 | reports/round-73/accept-ca.py | f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865 | af65165 (freeze) | as frozen | unchanged |
| r2 | reports/round-73/accept-ca.py | see `sha256sum` below | after the Ca landing commit e62d731 was first graded | BUG FIX: `load_ledger` passed the clone dict to `git -C`, so the `git show <lands>:reports/round-73/ledger.json` read always failed and the counter silently read the WORKTREE ledger (receipt header `source=worktree-uncommitted`). It now reads the ledger from the committed bytes at `<lands>` as the LEDGER leg text (and the docstring) always said. | unchanged: the claims.json LEDGER leg ("committed ... at <lands>'s ancestry") already required committed bytes; r2 makes the counter enforce it. r1 over-accepted a worktree-only ledger; no pair, leg, token or kill rule moved. |

r1 receipt that exposed the bug (graded at e62d731, SEPARABLE red for a separate reason): `ACCEPT-CA-73: FAIL legs=8/9`, header `ledger: reports/round-73/ledger.json source=worktree-uncommitted` — recorded here, not erased.
be1917950bfb992dc4be30be00c0f1bf3b317b6fc88bea2431344cafaec4cde0  reports/round-73/accept-ca.py

| r3 | reports/round-73/accept-ca.py | 222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89 | before the claim-C landing commit | `load_ledger` refuses to read the DEFAULT ledger path from the worktree (only an explicit `--ledger` may); selftest gains scenario 7b "worktree-only ledger" (LEDGER must FAIL). Red-before: `reports/round-73/telemetry/red-before-r3.txt` — the same selftest with only that guard removed prints `SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'`. | unchanged (the frozen LEDGER leg already required committed bytes) |

claim-C counter reports/round-73/accept-c.py stays at r1 (sha256 95aee88166023f4b0dc78cda5f0f3a769e94de476f5558bd6e33650922fea416); its selftest receipt is reports/round-73/telemetry/selftest-r2.txt / selftest-r3.txt.
