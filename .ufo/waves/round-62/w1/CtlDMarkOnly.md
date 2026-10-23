# CtlDMarkOnly — round 62 pre-data control

## Result

**CONTROL-MET; calibrated mutant SURVIVED.** The frozen counter accepted unrepaired claims when their positive/negative regexes read inline defect annotations instead of the assertion. Honest calibration, hidden-mark mutant, and exact honest restoration all printed `ACCEPT-D-62: PASS`, exit 0. The final scratch checkout was restored to the original frozen bytes.

Axes: semantic detection, annotation/edit cost, exact isolation/restoration. No lane implementation or counter was changed.

- Scratch clone: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/clone`; checked out `f0173481047a93c46798f90b68d71d4f169d2642` with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset.
- Counter: `reports/round-62/accept-d.py`, SHA-256 `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` for every run.
- Locator: `reports/round-61/reopen-quote.py`, SHA-256 `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390`.
- Same bounded detector throughout: `timeout --kill-after=5 900 python3 -B reports/round-62/accept-d.py`, cwd the clone (the initial pristine run used `timeout 900` without the extra kill grace). The collector recorded actual stdout and process exit status; stderr was empty in all 20 runs.
- Exact entry snapshots: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/<case>.entry.md`; matching registry snapshot and full records are named in `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/receipts.json`.

## Cheapest tested mark-only controls

All ten requested suffix marks were separately appended to all four otherwise unchanged lines: `(to-verify)`, `[overstated]`, `(unconfirmed)`, `(hedged: we have)`, `†`, `(per BBC)`, `(caption)`, `(list continues: etc.)`, `{{disputed}}`, and `<!-- check -->`.

`(to-verify)` and `[overstated]` failed NOMARK. All eight other spellings passed NOMARK. Suffix `(caption)` also passed CAPTION. No suffix-only specimen passed OPEN or HEDGE: their negative substring guards still saw the original closed list and unhedged sentence. These FAIL runs are **inconclusive as killed-mutant evidence**, because the pristine checkout already fails the full predicate.

The cheapest tested combined marker specimen adds 30 UTF-8 bytes, deletes no original words, and changes no original claims:

- line 63: insert `(Belgium etc)` immediately after `France,`;
- line 74: append `(caption)` immediately after `(S665)`;
- line 75: insert `(BBC)` immediately after `evidence`;
- line 93: append `†` immediately after `(S687)`.

`inline-parenthetical-bbc` passed **SET ONEID NOMARK OPEN HEDGE CAPTION APPEND LINK COPY ACCESS LINT**. It failed only SOLE, ROWS, LOCATE because no new row existed. The visible-mark version with the honest row and honest line 93 passed every leg; annotations on the first three lines cost only 27 added bytes.

The less ambiguous do-nothing specimen uses HTML comments: `<!--Belgium etc-->` inside the closed-list guard, `<!--BBC-->` inside the unhedged guard, and `<!--caption-->` after S665. Removing those comments recovers the original first three lines byte-for-byte; none of their displayed assertions was repaired. With the honest row and honest line 93, this also passed every leg.

## All four original claims retained, with one real new row

Fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/four-claims-retained-with-row.entry.md` plus `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-with-S693.md`.

```text
63: - A sabot is a hollowed shoe made from one wooden block, worn especially by farmers and workers in the Netherlands, France,<!--Belgium etc--> and Belgium. (S692)
74: - A heel originated in Western Asia for horseback riding before Europeans adopted it. (S665)<!--caption-->
75: - The earliest evidence<!--BBC--> of someone wearing heels comes from a 10th-century Persian bowl. (S666)
93: - Hermes' talaria were winged leather boots. (S693)<!--helmet winged-->
```

All four original assertions are recovered exactly by removing the HTML comments and reversing only S693→S687 on line 93. The fixture adds 62 bytes of comments plus the required same-length citation replacement. The real row's quote supports the honest calibration sentence, **not the retained leather-boots claim**; hidden `helmet winged` supplies LINK's missing ordered content words. This is a coverage finding, not a proposed contract or entry change.

Actual full counter result: **every leg PASS**, `ACCEPT-D-62: PASS`, exit 0. Compared with the passing honest calibration, this mutant **SURVIVED**.

CONTROL-MET CtlDMarkOnly/mark-only — `four-claims-retained-with-row.entry.md` (also `hidden-marks-with-honest-row.entry.md` and `parenthetical-marks-with-honest-row.entry.md`); smallest frozen-counter change stopping the hidden fixtures: add `"<!--"` to MARKS. Adding `"(caption)"` stops the tested parenthetical specimen. These are narrow counter changes, not executed fixes; a durable detector must distinguish marker/comment text from the asserted clause rather than merely extend a finite blacklist.

## Honest row and positive calibration

Row snippet: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/S693-calibration-row.txt`. New row S693 is docs / tier B, mined, opened 2026-10-23, 180d, used-by the footwear entry. The source is Mark Cartwright's edited World History Encyclopedia article, published 2019-08-28, updated 2025-04-18. Its **Questions & Answers / How is Hermes shown in art?** answer is body text, not an image caption:

> Hermes is usually shown in art with either a winged helmet or winged sandals.

- [Live page](https://www.worldhistory.org/Hermes/)
- [Same-page capture](https://web.archive.org/web/20261004070302id_/https://www.worldhistory.org/Hermes/)
- CDX query `https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.worldhistory.org%2FHermes%2F&output=json&limit=-5&filter=statuscode%3A200` returned that timestamp and status 200. The capture was also opened through the read tool.
- Registry search for `worldhistory\.org/Hermes|worldhistory\.org/image/4604|HomericHymns1` returned no matches before insertion; neither added URL was reused from SOURCES.
- Required ordinary locator command, from the clone: `timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://www.worldhistory.org/Hermes/ "Hermes is usually shown in art with either a winged helmet or winged sandals."`

Full output of that separate locator run:

```text
LOCATED https://www.worldhistory.org/Hermes/
exit=0
```

The honest calibration entry repairs the first three lines and makes line 93: `- Hermes is represented in art wearing either a winged helmet or winged sandals. (S693)`. It is only a scratch calibration, not a lane build or admission.

## Hash and restoration evidence

Registry aliases below resolve to exact SHA-256 values:

- base / final restored SOURCES: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`
- with S693: `0fc4488196ef4229eb8c35fc6ef6b66cf34e7d494305b3f8802c879915adf3af`

| State | Entry SHA-256 | Registry SHA-256 |
|---|---|---|
| pristine before | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` |
| honest baseline before mutant | `2c514ec8c8293573f88646733325105c34dd468e5f0bd1ee805265fbe8bf5e00` | `0fc4488196ef4229eb8c35fc6ef6b66cf34e7d494305b3f8802c879915adf3af` |
| retained-four-claims mutant | `af46fe31ef833425ac3416f1d2142f30f5d50e5c5544220604c4a82698e0b409` | `0fc4488196ef4229eb8c35fc6ef6b66cf34e7d494305b3f8802c879915adf3af` |
| honest exact restoration | `2c514ec8c8293573f88646733325105c34dd468e5f0bd1ee805265fbe8bf5e00` | `0fc4488196ef4229eb8c35fc6ef6b66cf34e7d494305b3f8802c879915adf3af` |
| pristine exact final restoration | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` |

Honest before/after hash dictionaries compared equal; detector PASS before and after. Pristine before/final hash dictionaries compared equal; detector FAIL with the same failed legs before and after. Counter hash remained frozen throughout. No full-predicate FAIL specimen is claimed killed on the failing pristine baseline.

Per-run mutated entry hashes (all counter hashes equal the frozen hash above):

| Case | Entry SHA-256 | Registry | Full verdict |
|---|---|---|---|
| pristine | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | base | FAIL |
| suffix-to-verify | `4c35d111ed43ae8f95efce8203489b898e2f691e0c448ae31101c5d9c0c3b7e3` | base | FAIL |
| suffix-overstated | `1e17bc387a83e94198822336361771b42e54ad78476b6e948c624c53e77fdb51` | base | FAIL |
| suffix-unconfirmed | `e8a98a7681443a0ec6e0c76c0e342f9a794fcc5d84e6e59ae4fd7fbf5be6f35f` | base | FAIL |
| suffix-hedged-we-have | `38d9c519505afd43d334a743f6d6fe16a964dd68c860f70362462e5217c423c3` | base | FAIL |
| suffix-dagger | `6b45804c011c5eae79dd9f0d1b6e6b137312b81854a7f63e34a9ae009f75b69f` | base | FAIL |
| suffix-per-bbc | `c7b5325a3aab8871fdd30e81049c9bd632d923583918fba99637aca295dc60d5` | base | FAIL |
| suffix-caption | `14a46fbafbcba6e2574a6d492362c19e877f2ba84e852f404aa5d551644358ef` | base | FAIL |
| suffix-list-continues | `4a1d8ebc28c7e19313da212355bc5bdf06db1fb8dcd08cbb5c15553e57e6ec56` | base | FAIL |
| suffix-disputed | `82954fdec23eba23d1c38e66981afa74db4884ba7bf6ccee9dec485c76d8372a` | base | FAIL |
| suffix-html-check | `af83a49040d662e1c4fd760468ebcd98eea863209c76a8731ec5bc56174dee34` | base | FAIL |
| inline-hidden-mark-only | `2548cf8b430a76453bbbfd994f667dfc716e9f1c9518fa52e0757bf3976ba6cc` | base | FAIL |
| inline-hidden-bbc | `bd44a13de4a96612cbf6fe79af9b9484af1b44c83a5de74e1b03d9e215eb9744` | base | FAIL |
| inline-parenthetical-bbc | `27007a6d049e005f542e3133fb04b87d4accb2f74befb2039658a1690ce174e8` | base | FAIL |
| honest-positive | `2c514ec8c8293573f88646733325105c34dd468e5f0bd1ee805265fbe8bf5e00` | with S693 | PASS |
| hidden-marks-with-honest-row | `0805a1ededc57f8d2893fbf2f123bba65060cf76bb183e73fc53e69ac1808078` | with S693 | PASS |
| parenthetical-marks-with-honest-row | `1f4e46377667b51c6b4ef597a232a79f51e38c0ccb0d71fdd0a8c4343e037ead` | with S693 | PASS |
| four-claims-retained-with-row | `af46fe31ef833425ac3416f1d2142f30f5d50e5c5544220604c4a82698e0b409` | with S693 | PASS |
| honest-restored | `2c514ec8c8293573f88646733325105c34dd468e5f0bd1ee805265fbe8bf5e00` | with S693 | PASS |
| pristine-restored | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | base | FAIL |

## Full detector receipts

Each block contains the full frozen detector stdout and its recorded exit code. The RECEIPT line is the required summary, not detector stdout. No counter was edited; no PROBE counter was used.

### pristine

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/pristine.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

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

RECEIPT CtlDMarkOnly/pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-to-verify

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-to-verify.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK FAIL marked=[63, 74, 75, 93]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-to-verify counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=NOMARK,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-overstated

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-overstated.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK FAIL marked=[63, 74, 75, 93]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-overstated counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=NOMARK,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-unconfirmed

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-unconfirmed.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-unconfirmed counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-hedged-we-have

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-hedged-we-have.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-hedged-we-have counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-dagger

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-dagger.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-dagger counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-per-bbc

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-per-bbc.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-per-bbc counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-caption

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-caption.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION PASS ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-caption counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,SOLE,ROWS,LOCATE

### suffix-list-continues

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-list-continues.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-list-continues counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-disputed

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-disputed.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-disputed counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### suffix-html-check

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/suffix-html-check.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/suffix-html-check counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### inline-hidden-mark-only

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/inline-hidden-mark-only.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/inline-hidden-mark-only counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE,ROWS,LOCATE

### inline-hidden-bbc

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/inline-hidden-bbc.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/inline-hidden-bbc counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE,ROWS,LOCATE

### inline-parenthetical-bbc

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/inline-parenthetical-bbc.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/inline-parenthetical-bbc counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE,ROWS,LOCATE

### honest-positive

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/honest-positive.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-with-S693.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:02Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDMarkOnly/honest-positive counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### hidden-marks-with-honest-row

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/hidden-marks-with-honest-row.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-with-S693.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:03Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDMarkOnly/hidden-marks-with-honest-row counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### parenthetical-marks-with-honest-row

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/parenthetical-marks-with-honest-row.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-with-S693.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:03Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDMarkOnly/parenthetical-marks-with-honest-row counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### four-claims-retained-with-row

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/four-claims-retained-with-row.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-with-S693.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDMarkOnly/four-claims-retained-with-row counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### honest-restored

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/honest-restored.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-with-S693.md`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=B
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDMarkOnly/honest-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### pristine-restored

Entry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/pristine-restored.entry.md`. Registry fixture: `/fast/scratch/hyaku/kotodama-r62/CtlDMarkOnly/fixtures/SOURCES-base.md`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDMarkOnly/pristine-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

## Bounds

No subagents, background jobs, headless browser, challenge bypass, git/jj lane writes, installation, or counter changes. All process calls were bounded at 900 seconds or less and completed synchronously; no started process tree remains running. Evidence files are individually below 5 MB. The only lane write is this one-shot report. Tool installs/updates: none. A read-tool URL-selector collision on an unescaped CDX `statuscode:200` query was reported through `xd://report_issue`; retrying the same ordinary query with `%3A` returned the JSON.
