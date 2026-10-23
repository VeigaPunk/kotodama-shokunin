# CtlDJunkTokens — frozen Claim D junk-token control

## Scope and result

Axes: semantic-depth challenge, frozen-leg coverage, smallest content-word budget, exact restoration.

Only the isolated clone at `/fast/scratch/hyaku/kotodama-r62/CtlDJunkTokens/clone` was mutated. It was cloned and checked out at `f0173481047a93c46798f90b68d71d4f169d2642` with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset. The frozen counter was not edited. No new source row, network fixture, alternate counter, or tool installation was used.

**Cheapest demonstrated junk:** the `five-content-minimum` fixture passes every frozen leg except **SOLE, ROWS, LOCATE**. It has five content words per line, the counter's minimum. OPEN, HEDGE, CAPTION, LINK and COPY all pass despite token-salad wording. The full predicate remains FAIL; this is not a CONTROL-MET receipt. The pristine predicate already fails, so the whole-predicate mutation verdict is **inconclusive**, not a killed mutant. The targeted semantic challenge survives all five target legs.

Fixture record: `/fast/scratch/hyaku/kotodama-r62/CtlDJunkTokens/junk-fixtures.json`. It retains pristine lines and every replacement after restoration of the clone.

## Mutation and expected detector

Defect: replace only entry lines 63, 74, 75 and 93 with unrelated token salad, keeping one proper S-id per bullet and the superficial OPEN/HEDGE/CAPTION tokens. Retain S687 on line 93; deliberately do not perform the new-row work, so SOLE, ROWS and LOCATE are expected to fail throughout.

Expected frozen behavior: bare regex tokens fail LINK; three added quote words are insufficient on lines 74 and 75 because ordered coverage requires at least four words. Four ordered quote-content words plus one arbitrary content word meet the lexical LINK threshold. COPY should pass because no long quote span is copied. The same bounded, unmodified detector was run on pristine, each mutant, and restored bytes.

### Case tokens-only

```text
63: - Belgium etc quasar mango nebula banana. (S692)
74: - Caption quasar mango nebula banana. (S665)
75: - BBC we have quasar mango nebula banana comet. (S666)
93: - Talaria quasar mango nebula banana. (S687)
```

### Case add-three

Adds exactly three ordered quote words per line: `shoe single block`, `heel European invention`, `earliest evidence someone`, and `Hermes wore winged`. Belgium and talaria already supplied one quote word on lines 63 and 93.

```text
63: - shoe single block Belgium etc quasar mango nebula banana. (S692)
74: - Caption heel European invention quasar mango nebula banana. (S665)
75: - BBC we have earliest evidence someone quasar mango nebula banana comet. (S666)
93: - Hermes wore winged talaria quasar mango nebula banana. (S687)
```

### Case five-content-minimum

```text
63: - shoe single block quasar Belgium etc. (S692)
74: - caption heel European invention Western. (S665)
75: - BBC we have earliest evidence someone quasar wearing. (S666)
93: - Hermes wore winged quasar talaria. (S687)
```

This uses five counted content words on each line and four in quote order; `BBC`, `we have` and `etc` add no counted content words. The arbitrary word `quasar` is not supported by the relevant quotes. The line-74 caption token plus four disconnected quote words also does not state the caption's proposition.

## Commands and hashes

Every case ran from the isolated clone with:

```sh
timeout 900 python3 -B reports/round-62/accept-d.py; printf 'exit=%s\n' "$?"
```

Each run was preceded by bounded `sha256sum` on the frozen counter and entry; pristine and restored runs also hashed SOURCES and the locator. No process ran in the background. All started commands completed; no process tree remains to kill.

Entry SHA-256 by case:

| Case | SHA-256 |
| --- | --- |
| pristine | eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72 |
| tokens-only | d2c6b4dbd28b940f44eadc94554038377cb0d7fd8543a195d7e4b399edf78f36 |
| add-three | 854d933cb5a7294053f0885499b8eba3cb65d917d9e7becee463a24827cd3fa2 |
| five-content-minimum | 74484865a707bb781b6ae3f39673f48cec7d39a29606b9b8e6ac30626b0104d1 |
| restored | eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72 |

Other hashes, identical before and after:

```text
3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4  reports/round-62/accept-d.py
eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2  corpus/SOURCES.md
39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390  reports/round-61/reopen-quote.py
```

## Full detector stdout and exit codes

### Pristine

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:56Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDJunkTokens/pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### tokens-only

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK FAIL bad=['63:content=5 shared=1 order=1/4', '74:content=5 shared=0 order=0/4', '75:content=5 shared=0 order=0/4', '93:content=5 shared=1 order=1/4']
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDJunkTokens/tokens-only counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE,ROWS,LINK,LOCATE

### add-three

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK FAIL bad=['74:content=8 shared=3 order=3/4', '75:content=8 shared=3 order=3/4']
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDJunkTokens/add-three counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE,ROWS,LINK,LOCATE

### five-content-minimum

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDJunkTokens/five-content-minimum counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE,ROWS,LOCATE

### Restored

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDJunkTokens/restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

## Verdict and restoration

NONE-MET CtlDJunkTokens/junk-tokens: no tested fixture passes ACCEPT-D-62. `junk-fixtures.json` case `five-content-minimum` meets the assigned narrower target (all legs except SOLE/ROWS/LOCATE); no full-control survivor is claimed. [INFERENCE] The one-line change `ORDER_MIN = 5` would stop this exact fixture at LINK, but adding more quote words could defeat that threshold too; it would not establish semantic entailment. This counter change was not applied or scored.

Whole-predicate mutation verdict: **inconclusive** because the pristine baseline fails. Target-leg finding: **survived** OPEN/HEDGE/CAPTION/LINK/COPY with the minimum content budget. Bare-token and three-added-word cases were rejected by LINK, as shown, but those FAIL outputs do not establish a killed whole-predicate mutant.

Restoration is exact: entry SHA-256 before and after is `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`; counter, registry and locator hashes also match before/after. Restored detector output returns to the pristine failing legs. All recorded control fixtures are outside the lane; the only lane write by this seat is this report. No installation or update occurred.
