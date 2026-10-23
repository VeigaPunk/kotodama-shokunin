# Round 59 claim D shortcut controls — CtlDShortcuts59
Axes: shortcut rejection; frozen-detector fidelity; exact-byte restoration.
Declaration: `1b80ee41f544d17c0410733a47a3eecac01bf25e`; claim base: `39c9ce8a6be5e5625d8befb54df53d621a3a7929`. The assigned clone and every independent case clone are under `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/`. No counter, frozen specification, lane entry or sibling file was edited.
All nine requested negative controls were rejected. Two strict kills (append-keep-old, kongo-only); the other seven requested negatives are INCONCLUSIVE as mutation kills because their own pristine green run failed live CARRY. A passing green comparator is recorded below; failing green runs are also retained, not discarded. CRLF extra bytes survive KONGO/SPEECH, but the full CRLF run failed CARRY, so it is not MEETS-COUNTER. No control had SUPPORT as its only failing leg; no MEETS-MECHANICAL designation applies.
Every detector invocation below is the unmodified command `timeout 900 python3 -B reports/round-59/accept-d.py`, executed from that case clone root. Each case was first set to the genuine application, scored pristine, mutated and scored, restored to the identical genuine bytes and scored, and finally returned to its original declaration bytes. Only the requested two entry files were replaced as complete sandbox fixtures. Raw stdout/stderr and hashes are also in `CtlDShortcuts59/evidence.json`.
Tooling: no tools installed or updated by this seat. The frozen locator itself uses its declared `uv run --with pypdf==5.4.0` PDF path. All explicitly started subprocesses were bounded with `timeout`, returned, and were joined; no background jobs or subagents were started.
## Scored controls
### Do-nothing declaration and CARRY discrimination

CONTROL do-nothing-declaration | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO, SPEECH]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] new_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146']
SPEECH FAIL equal=False old_ids_left={'S135': 16, 'S141': 2, 'S147': 3, 'S151': 2, 'S159': 4}
CARRY PASS located=14/14 at=2026-10-23T02:45Z failing=[]
ACCEPT-D-59: FAIL
```

CARRY located all 14 frozen support quotes on the unchanged declaration tree. The overall predicate still failed KONGO and SPEECH, as it should. This is the declared behavior, not a successful shortcut. The later independent do-nothing case is retained below including its transient CARRY failure.

### Genuine application — positive reference

This is the pristine green comparator in the append-keep-old case, before its append mutation. Its hashes equal the genuine application in every other case. MEETS-COUNTER is expected here: it does the claimed work.

CONTROL green-reference-MEETS-COUNTER | claim D | exit 0 | ACCEPT-D-59: PASS | failing legs: []

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/append-keep-old/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:47Z failing=[]
ACCEPT-D-59: PASS
```

### do-nothing

Mutant: No entry changes.

Expected detector: FAIL KONGO and SPEECH; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL do-nothing | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO, SPEECH, CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/do-nothing/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] new_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146']
SPEECH FAIL equal=False old_ids_left={'S135': 16, 'S141': 2, 'S147': 3, 'S151': 2, 'S159': 4}
CARRY FAIL located=13/14 at=2026-10-23T02:49Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 HTTPError; https://web.archive.org/web/20230210060841id_/https://jo']
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:47Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 HTTPError; https://web.archive.org/web/20230210060841id_/https://jo']
ACCEPT-D-59: FAIL
```

restored: exit 0; failing legs []; MEETS-COUNTER (genuine reference)

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:52Z failing=[]
ACCEPT-D-59: PASS
```

### append-keep-old

Mutant: Append all 14 new strings; retain every old string; speech is genuine.

Expected detector: FAIL KONGO; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL append-keep-old | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/append-keep-old/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:49Z failing=[]
ACCEPT-D-59: FAIL
```

Verdict: **KILLED: green pristine and restored runs passed; mutated run rejected.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 0; failing legs []; MEETS-COUNTER (genuine reference)

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:47Z failing=[]
ACCEPT-D-59: PASS
```

restored: exit 0; failing legs []; MEETS-COUNTER (genuine reference)

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:52Z failing=[]
ACCEPT-D-59: PASS
```

### ids-only

Mutant: Complete speech remap; Kongo untouched.

Expected detector: FAIL KONGO; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL ids-only | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO, CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/ids-only/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] new_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146']
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:50Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 HTTPError; https://web.archive.org/web/20230210060841id_/https://jo']
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:48Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

restored: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:52Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

### kongo-only

Mutant: All 14 Kongo fixes; speech untouched.

Expected detector: FAIL SPEECH; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL kongo-only | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [SPEECH, CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/kongo-only/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH FAIL equal=False old_ids_left={'S135': 16, 'S141': 2, 'S147': 3, 'S151': 2, 'S159': 4}
CARRY FAIL located=13/14 at=2026-10-23T02:50Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

Verdict: **KILLED: green pristine and restored runs passed; mutated run rejected.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 0; failing legs []; MEETS-COUNTER (genuine reference)

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:47Z failing=[]
ACCEPT-D-59: PASS
```

restored: exit 0; failing legs []; MEETS-COUNTER (genuine reference)

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:52Z failing=[]
ACCEPT-D-59: PASS
```

### thirteen

Mutant: Apply the first 13 frozen fixes, omit fix 146; speech is genuine.

Expected detector: FAIL KONGO; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL thirteen | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO, CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/thirteen/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=['146'] new_absent=['146']
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:50Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:48Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

restored: exit 0; failing legs []; MEETS-COUNTER (genuine reference)

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:52Z failing=[]
ACCEPT-D-59: PASS
```

### extra-edit

Mutant: All genuine changes plus unrelated one-word title change Kingdom -> Empire.

Expected detector: FAIL KONGO; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL extra-edit | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO, CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/extra-edit/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:50Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:48Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

restored: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:52Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

### junk

Mutant: Replace every old string with JUNK-<fix-id>; speech is genuine.

Expected detector: FAIL KONGO; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL junk | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO, CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/junk/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=[] new_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146']
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:50Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:48Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

restored: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:52Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

### delete-old

Mutant: Delete every old string and add no replacements; speech is genuine.

Expected detector: FAIL KONGO; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL delete-old | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [KONGO]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/delete-old/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO FAIL equal=False fixes=14 old_still_present=[] new_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146']
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:50Z failing=[]
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:48Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

restored: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:52Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

### sixth-id

Mutant: All genuine changes plus whole-word S136 -> S575 (2 extra tokens).

Expected detector: FAIL SPEECH; CARRY should remain independent of entry changes and passes only when its live fetches locate all 14 quotes.

CONTROL sixth-id | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [SPEECH]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/sixth-id/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH FAIL equal=False old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY PASS located=14/14 at=2026-10-23T02:51Z failing=[]
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:48Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

restored: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:52Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

### green-reference

Mutant: Exactly the 14 frozen fixes and the five whole-word remaps; no other change.

Expected detector: PASS all three legs. Its actual live run below is not silently substituted by the passing comparator above.

CONTROL green-reference | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/green-reference/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:50Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE positive-reference live run: CARRY failed; identical green bytes passed in other recorded comparator runs.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:48Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 HTTPError; https://web.archive.org/web/20230210060841id_/https://jo']
ACCEPT-D-59: FAIL
```

restored: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:53Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

### crlf-extra

Mutant: All genuine changes, then rewrite both LF entries to CRLF; unrelated byte changes challenge the byte-for-byte invariant.

Expected detector: FAIL KONGO and SPEECH under the claimed byte-for-byte contract. Actual text-mode comparison accepts both changed files.

CONTROL crlf-extra | claim D | exit 1 | ACCEPT-D-59: FAIL | failing legs: [CARRY]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/cases/crlf-extra/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:51Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

Verdict: **INCONCLUSIVE: pristine green baseline failed CARRY; not counted as a killed mutant.**

Pristine and restored detector evidence (green reference, not additional shortcut controls):

pristine: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=13/14 at=2026-10-23T02:48Z failing=['93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

restored: exit 1; failing legs [CARRY]; no pass designation

```sh
timeout 900 python3 -B reports/round-59/accept-d.py
```

```text
KONGO PASS equal=True fixes=14 old_still_present=[] new_absent=[]
SPEECH PASS equal=True old_ids_left={'S135': 0, 'S141': 0, 'S147': 0, 'S151': 0, 'S159': 0}
CARRY FAIL located=11/14 at=2026-10-23T02:53Z failing=['141: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '82: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-chu', '93: https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError; https://web.archive.org/web/20230210060841id_/https://jou']
ACCEPT-D-59: FAIL
```

## CARRY unrelated-URL probe

Diagnostic only, not a replacement acceptance counter: the unchanged rowcheck locator was asked to locate every frozen support quote at each of four unrelated public pages (Example Domain, IANA reserved domains, RFC 2119, Python built-ins). One cached ordinary GET per URL; no substitutions to d-fixes.json, no proxy, challenge handling or forged responses. All 56 attempts were genuine quote-absent results, with no fetch errors. No unrelated-page location was observed in this bounded sample; this is not an exhaustive assertion about all URLs.

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/clone`

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlDShortcuts59/carry-offsite.py
```

Exit: 0

```text
URL https://example.com/ located=[] quote_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] other=[]
URL https://www.iana.org/domains/reserved located=[] quote_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] other=[]
URL https://www.rfc-editor.org/rfc/rfc2119.txt located=[] quote_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] other=[]
URL https://docs.python.org/3/library/functions.html located=[] quote_absent=['18', '65', '82', '84a', '84b', '85', '89', '93', '97a', '97b', '110', '140', '141', '146'] other=[]
OFFSITE-QUOTE-PROBE: located=0/56 quote_absent=56/56 other=0/56 hits=[]
```

The exact probe is retained at `CtlDShortcuts59/carry-offsite.py`. It imports the frozen locator and does not feed an alternate URL into accept-d.py. The unchanged full counter's do-nothing CARRY result is recorded above.

## Hash and restoration evidence

All hashes are SHA-256 of raw bytes. For every detector run the recorded after-hashes equal the before-hashes; the detector did not mutate either entry. Every case had the same green pristine hashes, was restored to those identical hashes before its restored run, and was finally restored to its original declaration hashes. The main assigned clone remained at the original declaration bytes throughout.

| Entry | Original declaration / final restoration | Genuine pristine / scored green restoration |
|---|---|---|
| `corpus/knowledge/civilizations/kongo-kingdom.md` | `fddc8404675887fc80583929dcc896424af7007f8ccaf78bb7c0afbc295d004a` | `0e1b415f653f31b783e1eedd1c27a9ea845ddbc91ad70c1a6278ce446ac115df` |
| `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | `d7b43b78bc85173f495bbd741e147009665465c73610b7d6b6bd13d12d0a19ac` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |

| Mutant | Kongo raw SHA-256 before = after detector | Speech raw SHA-256 before = after detector |
|---|---|---|
| do-nothing | `fddc8404675887fc80583929dcc896424af7007f8ccaf78bb7c0afbc295d004a` | `d7b43b78bc85173f495bbd741e147009665465c73610b7d6b6bd13d12d0a19ac` |
| append-keep-old | `e5ae3eae9a5015eadf71eae9e19f1965762b2f2d45c7476810dc013c1cd38728` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |
| ids-only | `fddc8404675887fc80583929dcc896424af7007f8ccaf78bb7c0afbc295d004a` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |
| kongo-only | `0e1b415f653f31b783e1eedd1c27a9ea845ddbc91ad70c1a6278ce446ac115df` | `d7b43b78bc85173f495bbd741e147009665465c73610b7d6b6bd13d12d0a19ac` |
| thirteen | `bf89631b27cfaf352aeb390cf62b420391754478c8037610088e5b93da9a9245` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |
| extra-edit | `65d5077c189d23d8052fe2525af693fd31df8c7eadda42fb5459de080dc53714` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |
| junk | `e6c90f6befd8065447722be1493723c307abcd87356f2ce9ae591e78acd7084c` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |
| delete-old | `36fcd464d75a96c5991533abd45f630f093a759ca92a525b2092c3cd360e6c3a` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |
| sixth-id | `0e1b415f653f31b783e1eedd1c27a9ea845ddbc91ad70c1a6278ce446ac115df` | `453705aefded40e799482463d8fc83f4f78f7f0e5556a390f5e6ddddc3ebe71b` |
| green-reference | `0e1b415f653f31b783e1eedd1c27a9ea845ddbc91ad70c1a6278ce446ac115df` | `e1d5d26b46b2ec75774870f0f3bccbc8d31bb66c9b62fcc12863420cb4d695eb` |
| crlf-extra | `84a39d7eaff87da49322aa0fe75c891ba6ed0d627b3e5c495ee9125cd6041571` | `97db07d92805e12e0b708021b0066bfa17905f3320c58c2a55cbb65f3389ee40` |

All eleven green restorations and all eleven final declaration restorations matched their respective expected hash pairs exactly. The CRLF files have different raw hashes from genuine green files even though both equality legs printed PASS.

Frozen input hashes (identical before/after every run and after final restoration):

- `reports/round-59/accept-d.py`: `8194bc579c6459a064d734633f7e258ab5da7ab5df80993d8421a31221578814`
- `reports/round-59/accept-c.py`: `2d42deb5b84a06db06ec13cef49e4209f219e66b02cf4b21caa7d61a8197ea5e`
- `reports/round-59/rowcheck.py`: `d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e`
- `reports/round-59/reopen-quote.py`: `64e78c749b4dc334217499d7411671dbcb904f793b168bfae85dc69b68ab16f8`
- `reports/round-59/d-fixes.json`: `46a3daec145a32dccb46c45c6e9d07146721dc363872a5c10c30cb177ca9e350`
- `reports/round-59/claims.json`: `96744ac5bd40d0f245d01178d028fd66f08348f7b6a7fc6fd91f1dffef628e0a`

## counter weaknesses:

- **Byte-for-byte predicate is implemented as newline-normalized text equality.** `accept-d.py:68-69` opens both tips in default text mode, so the fully fixed CRLF rewrite changed both raw hashes yet KONGO and SPEECH still printed `PASS equal=True`. The CRLF full run exited 1 only because live CARRY failed; its green pristine/restored runs also failed CARRY, so the full mutation verdict is INCONCLUSIVE, not a killed mutant or an observed full-counter survivor. Fix before data: preserve line endings when loading tips (`read_bytes().decode("utf-8")`, matching the existing base-byte decode, or `open(..., newline="")`), and retain this CRLF mutation as a rejection regression. Do not relax the frozen contract to accommodate the mutant.
- **Live-source flapping limits kill evidence.** Identical green hashes sometimes passed CARRY 14/14 and sometimes failed fixes 93 and/or 82/141 through HTTPError/URLError. All outputs are retained; no failures were rescaled or called kills. This is availability sensitivity explicitly declared by FETCH-59, not evidence of a shortcut meeting the full predicate. Preserve truthful per-run receipts and distinguish mechanical rejection from inconclusive live baselines.
- No tested do-nothing, append, ids-only, Kongo-only, partial, unrelated-title edit, junk, deletion or sixth-id shortcut met the full counter. CARRY correctly passed on the first do-nothing run while KONGO/SPEECH kept the overall predicate false; no unrelated-URL quote location was found in the 56 diagnostic attempts.
