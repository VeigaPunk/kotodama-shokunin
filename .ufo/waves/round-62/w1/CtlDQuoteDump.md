# CtlDQuoteDump — claim D pre-data quote-dump controls

Seat: `KotodamaR62.CtlDQuoteDump`. Assigned axis: **depth**. Probe axes: exact-copy rejection, near-copy sensitivity, preservation of the source's hedge/open list, and exact restoration. This is a scoped detector receipt, not a lane judgment or an implementation.

## Scope and detector

Read `reports/round-62/claims.json`, round-61 verifier section 7, and the frozen counter's docstring before mutation. Created the isolated clone using the prescribed clone/check-out sequence with `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` unset:

- Clone: `/fast/scratch/hyaku/kotodama-r62/CtlDQuoteDump/clone`
- Revision: `f0173481047a93c46798f90b68d71d4f169d2642`
- Detector: `reports/round-62/accept-d.py`
- SHA-256: `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`
- Every scoring command, from that clone: `timeout 900 python3 -B reports/round-62/accept-d.py; echo exit=$?`. Hash preambles, where present below, used `timeout 30 sha256sum`.
- No counter, locator, checker, registry, or sibling source was modified. No source access or new row was invented. No tools were installed. All invoked processes completed; no background jobs or services were started.

## Mutants and expected detector

1. **verbatim**: replace exactly entry lines 63, 74, 75, and 93 with their current row's verbatim anchor quote plus its original S-id. Keep bullet syntax. Expected: COPY rejects all four because the quotes have 23, 18, 16, and 17 normalised words. OPEN/HEDGE should pass; the literal S665 quote does not name its caption, and S687 remains tier C.
2. **every12**: the same fixture, replacing the twelfth normalised quote word: `worn→used`, `Western→West`, `a→the`, and `pedila→pédila`. Each quote has fewer than 24 normalised words, so there is exactly one replacement per quote. Expected: COPY passes because each replacement interrupts the otherwise copied sequence before 13 consecutive words. This does not repair the caption attribution or tier-C sole support.

Retained fixture specifications, sufficient to reproduce the four replacements from the frozen clone:

- `/fast/scratch/hyaku/kotodama-r62/CtlDQuoteDump/verbatim.fixture.txt`
- `/fast/scratch/hyaku/kotodama-r62/CtlDQuoteDump/every12.fixture.txt`

## Full outputs and receipts

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

RECEIPT CtlDQuoteDump/pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### Verbatim quote dump

```text
3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4  reports/round-62/accept-d.py
716e82ea13db1abb50e090aac2f914399f3b850024271a072deb89cbc002f6a6  corpus/knowledge/culture-material/footwear-codes-terminology.md
eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2  corpus/SOURCES.md
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY FAIL bad=['63:run=23', '74:run=18', '75:run=16', '93:run=17']
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDQuoteDump/verbatim counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=CAPTION,SOLE,ROWS,COPY,LOCATE

### One changed word every twelve words

```text
3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4  reports/round-62/accept-d.py
332c27c2ad369361ef700fbaddf9646eef6b0d7904afc79304de74157d2ab9d6  corpus/knowledge/culture-material/footwear-codes-terminology.md
eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2  corpus/SOURCES.md
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
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

RECEIPT CtlDQuoteDump/every12 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=CAPTION,SOLE,ROWS,LOCATE

### Restored

```text
3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4  reports/round-62/accept-d.py
eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72  corpus/knowledge/culture-material/footwear-codes-terminology.md
eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2  corpus/SOURCES.md
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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDQuoteDump/restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

## Verdict

NONE-MET verbatim — frozen predicate FAIL; COPY explicitly rejects all four pasted quotes. No counter change is needed to stop this fixture. Full mutation-kill verdict: **INCONCLUSIVE**, not killed, because pristine already fails.

NONE-MET every12 — frozen predicate FAIL, despite COPY PASS; CAPTION, SOLE, ROWS, and LOCATE stop it. No counter change is needed to stop this fixture. Full mutation-kill verdict: **INCONCLUSIVE**, not survived, because pristine already fails. At the COPY-leg level only, the near-copy survives; this is evidence that COPY measures consecutive copying, not total copying or independent synthesis. A hypothetical 13-word match allowing one substitution would reject these near-copies, but that is an unrun contract change, not a fix applied here.

**Does a pasted quote meet every other leg? No.** Literal paste passes SET, ONEID, NOMARK, OPEN, HEDGE, APPEND, LINK, ACCESS, and LINT; it fails CAPTION, SOLE, ROWS, and LOCATE independently of COPY. The every12 variant has the same other-leg outcomes. Neither fixture added caption attribution or replaced S687 with a new A/B row, intentionally preserving the assigned literal quote-dump control rather than silently repairing those separate requirements. No all-green calibration was established, so there is no claim that a near-copy could pass the entire predicate after those independent repairs.

### Shortcut versus honest repair — three lines

- Shortcut: copying with periodic token substitutions performs no demonstrated synthesis, and these fixtures leave the caption and sole-support defects unresolved.
- Honest repair: an exact, properly attributed quotation can faithfully restore the original hedge and open list without introducing a paraphrase's extra claims.
- Boundary: frozen D separately requires caption/A-B support repairs and forbids runs over twelve words; raw quotation fails that contract, whereas sparse substitutions pass COPY alone without proving either understanding or full repair.

## Exact restoration evidence

SHA-256 before → verbatim → every12 → restored:

- ENTRY: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` → `716e82ea13db1abb50e090aac2f914399f3b850024271a072deb89cbc002f6a6` → `332c27c2ad369361ef700fbaddf9646eef6b0d7904afc79304de74157d2ab9d6` → `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.
- SOURCES: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` at all four stages.
- Counter: `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` at all stages.

The restored detector reproduces the pristine failing-leg set. Only the four assigned entry lines were mutated; their file's original SHA-256 is restored exactly. No lane implementation bytes were touched. This report is the seat's sole lane write.
