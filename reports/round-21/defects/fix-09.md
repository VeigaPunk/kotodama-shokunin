# R21-O09 — R17 worker-seat arithmetic

- **Disposition:** closed at the declaration level by the R18 allocation; preserve the filed declarations.
- **Finding:** R17 declared 64 workers but its target allocations sum to 60. Read-only control run 2026-10-18:

  ```sh
  python3 - <<'PY'
  import json
  from pathlib import Path
  root = Path('.')
  for r in (17, 18):
      claims = json.loads((root / f'reports/round-{r}/claims.json').read_text())
      targets = json.loads((root / f'reports/round-{r}/targets.json').read_text())['workers']
      print(f'R{r}: declared={claims["workers"]} allocated={sum(targets.values())} seats={targets}')
  PY
  date -I
  ```

  Output: `R17: declared=64 allocated=60`; `R18: declared=64 allocated=64` (allocation 20+28+10+6). This is consistent with `reports/round-17/scope.md` F-X02-1 and `reports/round-18/scope.md` §4, both dated 2026-10-18.
- **Bounded action:** record R17 as a declaration mismatch superseded by R18's balanced declaration. Do not add/remove seats or rewrite either filed round.
- **Limit / owner:** the JSON arithmetic does not prove actual dispatch or attendance; that operational history is `to-verify` unless the operator has a dispatch log. No historical validator was run.
