# R21-O14 — malformed era-alias values fail open

- **Disposition:** open; route implementation and full CLI regression to the R22 owner of `tools/d2-typed-labels.py`.
- **Finding:** the current `packet_alias_rows()` code stringifies every declared tag and labels the resulting row `confirmed` (`tools/d2-typed-labels.py:2486-2492`). A direct no-file probe against that production helper on 2026-10-18 used:

  ```sh
  export TMPDIR=$PWD/.scratch
  export PYTHONDONTWRITEBYTECODE=1
  python3 - <<'PY'
  import runpy
  namespace = runpy.run_path('tools/d2-typed-labels.py')
  aliases, rows, key = namespace['packet_alias_rows']({'era_aliases': {'era-9': [1, 2]}})
  print(f'key={key!r} aliases={aliases!r} rows={rows!r}')
  PY
  date -I
  ```

  Output included `aliases={'era-9': '[1, 2]'}` and `status: 'confirmed'`. This agrees with the dated R20 M9 finding in `reports/round-20/wart/review.md` §2–3. No historical round validator or full projection command was run here.
- **R22 route / owner:** reject non-string or grammar-invalid tags before projection and add a named negative control that proves malformed declarations cannot be emitted as confirmed. Re-run the relevant projector controls in an isolated fixture/mirror and record the command/date before closing.
- **Limit:** the probe above exercises the helper directly, not the full packet/CLI path; end-to-end refusal remains `to-verify` until the owner supplies that control.
