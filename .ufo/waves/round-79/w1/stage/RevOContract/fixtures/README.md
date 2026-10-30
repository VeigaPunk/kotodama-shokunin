# RevOContract fixtures — oracle

Target of every fixture: the O guard `tools/ledger-token-guard.py` (absent at base,
probe P1). These are CONTRACT fixtures: each file states one mutation, the O clause
it is the red-before for, and the exact expected verdict. ExecGuard, ExecOCounter,
CritNoopO, MutObserved, MutVacuous, MutRevision, MutPath and L1 can run the whole
set without further design.

- `fx-guard-clean-ledger.json` — truthful 3-pair ledger against the isolated fixture
  repo at commit `362e71615521ddb23f1af02306251a9262a1acdb`; every `observed_at_base`
  was measured by the verbatim commands in `../probes/fixture-measure.txt`.
  Expected: ACCEPT. This is the green baseline every mutant is judged against
  (QUALITY 23 addendum limb 2: a mutant's redness counts only against a green clean
  run in the same run).
- `fx-mut-fabobs-c.json` — clause (c): recorded observation fabricated (`green-7`→`1`,
  the R78-M1 / ScoutLogPairs D01–D10 class). Expected: REJECT pair OC-A1.
- `fx-mut-nomismatch-d.json` — clause (d): stated old token set equal to the actual
  observation (the ScoutLogPairs D11 "not red at base" class). Expected: REJECT OC-A1.
- `fx-mut-headrev-b.json` — clause (b): `HEAD` in revision position (the MutCaLedger
  e1 survivor class the ancestor grammar accepted). Expected: REFUSE.
- `fx-mut-branchrev-b.json` — clause (b): `main` in revision position. Expected: REFUSE.
- `fx-mut-treerev-b.json` — clause (b): 40-hex **tree** id in revision position
  (immutable bytes but not a commit). Expected: REFUSE.
- `fx-mut-echo-b.json` — clause (b): `["echo","green-7"]` (QUALITY 25 J4). Expected: REFUSE.
- `fx-mut-pyprint-b.json` — clause (b): `["python3","-c","print('green-7')"]` (J4b).
  Expected: REFUSE.
- `fx-mut-shellstring-b.json` — clause (a): `observe_cmd` as one shell string, not an
  argv array (round-76 H2 / round-77 draft argv rule). Expected: REFUSE.
- `fx-mut-pathtrav.json` — clause (a): path operand `../outside.txt`. Expected: REFUSE.
- `fx-mut-optinject.json` — clause (a): operand `-c` after `--`. Expected: REFUSE.
- `fx-donothing.json` — do-nothing control: `pairs: []`. Expected: REJECT (never PASS).
- `fx-dupid.json` — structural: duplicate pair id. Expected: REJECT.

Regeneration: see `../commands.md` (FIXTURE-REPO reproduces the repo and commit hash
byte-for-byte; `python3 make-fixtures.py` regenerates every mutant).
