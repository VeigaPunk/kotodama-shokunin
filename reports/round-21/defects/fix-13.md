# R21-O13 — R20 foreign-tree mirror wart

- **Disposition:** closed by the final R20 control; no further code or pin edit is authorized here.
- **Finding:** R19's D4 adapter selftest copied the unrelated D2 example tree into its mirror, masking a missing family boundary. The interim R20 review is not the close receipt; it captured an in-flight state.
- **Control:** the final `reports/round-20/validation.json` was produced by `python3 reports/round-20/run-validation.py` (2026-10-18) and records `foreign_tree_copy_in_adapter: false` plus an exit-zero `python3 tools/assemble-d4-typed.py --selftest` run with `12/12` checks (2026-10-18). R20's independent no-D2 mirror probe is also recorded in `reports/round-20/regression.md` §1: `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` exited zero at 2026-10-18 10:15:28 -03:00.
- **Bounded action:** close this wart by pointer to the final control; preserve the report trail and do not reopen it from the earlier intermediate review alone.
- **Limit:** the independent probe checks the projector in a no-D2 mirror; the final runner marker and adapter selftest are the controls for the adapter copy behavior. Neither is a semantic approval of the D4 projection.
