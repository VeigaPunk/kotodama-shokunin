# Round-73 counter revisions (append-only; claims.json is not edited)

| rev | file | sha256 | when | change | predicate |
|---|---|---|---|---|---|
| r1 | reports/round-73/accept-ca.py | f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865 | af65165 (freeze) | as frozen | unchanged |
| r2 | reports/round-73/accept-ca.py | see `sha256sum` below | after the Ca landing commit e62d731 was first graded | BUG FIX: `load_ledger` passed the clone dict to `git -C`, so the `git show <lands>:reports/round-73/ledger.json` read always failed and the counter silently read the WORKTREE ledger (receipt header `source=worktree-uncommitted`). It now reads the ledger from the committed bytes at `<lands>` as the LEDGER leg text (and the docstring) always said. | unchanged: the claims.json LEDGER leg ("committed ... at <lands>'s ancestry") already required committed bytes; r2 makes the counter enforce it. r1 over-accepted a worktree-only ledger; no pair, leg, token or kill rule moved. |

r1 receipt that exposed the bug (graded at e62d731, SEPARABLE red for a separate reason): `ACCEPT-CA-73: FAIL legs=8/9`, header `ledger: reports/round-73/ledger.json source=worktree-uncommitted` — recorded here, not erased.
be1917950bfb992dc4be30be00c0f1bf3b317b6fc88bea2431344cafaec4cde0  reports/round-73/accept-ca.py
