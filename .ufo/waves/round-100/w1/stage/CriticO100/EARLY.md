# EARLY — CriticO100: contract violation in check-table-support.py (LOW severity)

**STATUS: FIXED.** Confirmed on build `271c42fa…`; the `blocked` branch was removed in build
`3ad56147…` (08:48:25) and fixture A10 now returns rc 1 `NO-CAPTURE S9001`, matching the contract
and the pinned ref. Kept as the regression recipe. The OSError wrappers for unreadable capture /
support files remain (contract silent there: gap, not violation).

Tool tested: `tools/check-table-support.py` sha256
`271c42fa192884acd96a5511adc787524c2ec534ce4fabd65953dc9ff262cf46` (mtime 2026-11-06 08:45:23).
Contract: `reports/round-100/claims.json` claims.O.contract, `findings` + `output` clauses.

## Violation: a non-file named `<S-id>.txt` in an evidence dir gives rc 2, contract requires NO-CAPTURE (rc 1)

The contract's `output` clause enumerates the rc-2 conditions: "a missing or non-UTF-8 entry, a
missing evidence dir or no --evidence". The `findings` clause requires `NO-CAPTURE {sid}` when the
binding line's S-id has no capture. A directory named `S9001.txt` is not a capture, so the contract
expects rc 1 with `{"id":"NO-CAPTURE","sid":"S9001"}`; the tool exits 2 with
`TABLE_SUPPORT_ERROR capture unreadable: S9001` and no JSON.

Exact recipe (fixture `A10` in `attacks_critic100.py`, run under scratch):

```
mkdir -p <fixture>/ev/S9001.txt          # a directory, not a file
entry: caption 'The columns are filled from the recorded cases this entry cites.'
       | tradition | practice | / |---|---|
       | River | leader calls each line |
       binding lines: 'The River row reports the river (S9001).'
                      'The River row also reports the river (S9002).'   # S9002 is a real capture
run:   python3 -B tools/check-table-support.py --entry <fixture>/entry.md \
         --evidence <fixture>/ev --json
observed: rc 2, stdout 'TABLE_SUPPORT_ERROR capture unreadable: S9001', no JSON
contract + feasibility ref: rc 1, findings [('NO-CAPTURE','S9001')]
```

Cause: `check()` in the tool (only divergence from the pinned reference besides OSError wrapping):

```python
path = None; blocked = False
for d in evdirs:
    p = os.path.join(d, sid + '.txt')
    if os.path.isfile(p): path = p; break
    if os.path.exists(p): blocked = True
if path is None:
    if blocked: raise ToolError(f'capture unreadable: {sid}')
```

Smallest fix: delete the `blocked` branch (a non-file is simply absent -> NO-CAPTURE), or raise
only when `os.path.isfile(p)` is true and `open()` fails. The two `except OSError -> ToolError`
wrappers are the same family but the contract is silent on unreadable files (gap, not violation).

Impact on claim O legs: none. battery100 never creates a non-file capture (28/28 unaffected);
O3/O4 do not read this path. This is a frozen-contract conformance defect, not a leg failure.
