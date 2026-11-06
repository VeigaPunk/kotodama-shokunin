# PINS-FOR-OWNER — paste-ready selftest pins (tool owner only)

The 7 mutation survivors (W1, W2, A2, L1, L2, L4, C4) are killed by the six pins below. Each pin
was validated against the current tool: it PASSES on pristine bytes and FAILS on its target mutant
(`validate_pins.py`, rc 0). Insert the list entries inside `selftest_pins()`'s returned list; no
other change is needed (`st_json_pin` already accepts `evid=` and `scoped=`).

```python
        ('B10-window-boundary-79-80',
         lambda w: st_json_pin(w, 'B10', st_entry(REC, '| tradition | practice |', '|---|---|',
                                                 ['| Alpha | alpha beta |', '| Gamma | gamma delta |'],
                                                 ['The Alpha and Gamma rows report the cases (S9101).']),
                               1, [('UNSUPPORTED-CELL', 'Gamma', 'practice')],
                               best={('UNSUPPORTED-CELL', 'Gamma', 'practice'): (1, 2)}, scoped=1,
                               evid={'S9101': 'alpha ' + ' '.join(['lorem'] * 78) + ' beta gamma '
                                              + ' '.join(['lorem'] * 79) + ' delta'})),
        ('B11-threshold-two-of-three',
         lambda w: st_json_pin(w, 'B11', st_entry(REC, '| tradition | practice |', '|---|---|',
                                                 ['| Alpha | alpha beta zulu |'],
                                                 ['The Alpha row reports the case (S9102).']),
                               1, [('UNSUPPORTED-CELL', 'Alpha', 'practice')],
                               best={('UNSUPPORTED-CELL', 'Alpha', 'practice'): (2, 3)}, scoped=1,
                               evid={'S9102': 'alpha beta lorem lorem lorem'})),
        ('B12-label-token-length-three',
         lambda w: st_json_pin(w, 'B12', st_entry(REC, '| tradition | practice |', '|---|---|',
                                                 ['| Ewe | alpha beta |'],
                                                 ['The Ewe row reports the case (S9103).']),
                               0, [], scoped=1,
                               evid={'S9103': 'alpha beta'})),
        ('B13-label-token-length-two-excluded',
         lambda w: st_json_pin(w, 'B13', st_entry(REC, '| tradition | practice |', '|---|---|',
                                                 ['| If | alpha beta |'],
                                                 ['The If row reports the case (S9104).']),
                               1, [('UNBOUND-ROW', 'If', '')], scoped=1,
                               evid={'S9104': 'alpha beta'})),
        ('B14-label-and-excluded',
         lambda w: st_json_pin(w, 'B14', st_entry(REC, '| tradition | practice |', '|---|---|',
                                                 ['| Salt and iron | alpha beta |'],
                                                 ['The wind and rain report the case (S9105).']),
                               1, [('UNBOUND-ROW', 'Salt and iron', '')], scoped=1,
                               evid={'S9105': 'alpha beta'})),
        ('B15-caption-two-line-extent',
         lambda w: st_json_pin(w, 'B15', st_entry('The recorded cases fill this table.\nDesign notes follow.',
                                                 '| tradition | practice |', '|---|---|',
                                                 ['| Alpha | alpha beta |'],
                                                 ['The Alpha row reports the case (S9106).']),
                               0, [], scoped=1,
                               evid={'S9106': 'alpha beta'})),
```

Pin-to-mutant map: B10 kills W1 (`WINDOW = 80` -> 79, extra Alpha finding) and W2 (-> 81, no
finding); B11 kills A2 (2/3 makes the cell pass); B12 kills L1 (>= 4 drops `Ewe`); B13 kills L2
(>= 2 binds on `if`); B14 kills L4 (`and` binds); B15 kills C4 (one-line caption loses the scope).

Expected after insertion: `SELFTEST PASS 39/39`, battery100 still 28/28, and mutants100 36/36
killed with 0 survived and 0 broken-pattern.
