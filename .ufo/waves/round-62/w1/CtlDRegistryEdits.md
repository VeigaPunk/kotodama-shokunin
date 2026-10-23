# CtlDRegistryEdits — frozen ACCEPT-D-62 pre-data controls

## Scope and axes

Axes: depth/registry immutability, whole-predicate evasion sensitivity, exact restoration/reproducibility.

Frozen revision: `f0173481047a93c46798f90b68d71d4f169d2642`. Counter SHA-256: `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` on **every** run. No counter was edited, copied into a PROBE, or substituted. Only this report was written in the lane; all fixtures and mutations were isolated under `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/`.

Read first: claims.json, round-61-verifier-spotcheck.md §7, godspeed skill, and operator RULES.md. No tools installed or updated. No delegation, background jobs, alternate agent runtimes, or git/jj lane writes. All detector children completed synchronously under `timeout 900`; no child process remains from these probes.

## Main finding

**CONTROL-MET: a NEW row reusing an existing registry URL is not stopped by any leg.**

- `copied-s688-url-heading`: S693 copies S688's exact live URL, asserts tier A, quotes the located heading/byline `Talaria Article by James Yates, M.A., F.R.S., on pp1094`, and changes line 93 into a byline statement. Every leg PASS; exit 0. This does not perform the claimed talaria-fact repair or discover a new source.
- `copied-s687-url-body`: independently removes the heading confound. S693 copies S687's exact Theoi URL **and verbatim body anchor**, merely relabels its tier C as A, lists a capture-shaped URL, and line 93 paraphrases the original body quote. Every leg PASS; exit 0. Thus even a body quote with talaria/Hermes does not make URL reuse detectable.
- Minimal proposed counter change (not applied): in ROWS, compare every NEW row live URL against the URLs from BASE's registry and fail on intersection (or add FRESH). Reusing the same literal URL is enough to demonstrate the gap; URL canonicalization is not needed to stop these fixtures.

Both fixtures deliberately list synthetic `20261023000000id_` same-page Wayback URLs. These are **control data, not verified archive captures or proposed SOURCES rows**. The live pages located first, so those URLs were never needed. The success therefore does not establish archive availability. The CDX request attempted by ordinary read returned HTTP 403; no challenge was passed or bypassed.

## Results on an all-PASS calibration

The all-PASS calibration itself is the cheap `copied-s688-url-heading` fixture, not a claim of honest completed work. This supplies a passing detector baseline for registry sensitivity. Each `cal-*` mutation was run between passing bytes and exactly restored passing bytes; the preceding restoration supplies the next pristine baseline. The first base-only matrix is kept below but is globally **inconclusive**, not a kill, because the unmodified claimed object already FAILs SET/OPEN/HEDGE/CAPTION/SOLE/ROWS/LOCATE.

Expected detector: APPEND must fail forbidden edits/deletion/reordering and S700 insertion, allow only S687's used-by change, and restrict new canonical row ids to S693–S699. For the exact S688 copy, ROWS should require the cited new row/capture and SOLE should require talaria/Hermes in its quote. URL reuse needs an independent freshness comparison, which revision 0 lacks.

| Mutant | Case | Observed detector | Verdict |
|---|---|---|---|
| S665 anchor quote Western→Eastern | `cal-s665-quote` | APPEND FAIL | killed |
| S687 tier C→A | `cal-s687-tier` | APPEND FAIL | killed |
| S692 kind book→docs | `cal-s692-kind` | APPEND FAIL | killed |
| S687 used-by entry→— (allowed) | `cal-s687-used-by` | all PASS | survived, expected allowance |
| S687 teaches boots→sandals | `cal-s687-teaches` | APPEND FAIL | killed |
| Delete base S688 | `cal-delete-s688` | APPEND FAIL | killed |
| Insert S700 | `cal-insert-s700` | APPEND FAIL | killed |
| Insert S650b | `cal-insert-s650b` | all PASS; APPEND does not recognize the row | survived, parser coverage finding |
| Swap base S687/S688 | `cal-reorder-s687-s688` | APPEND FAIL | killed |
| Exact S688 copied as S693, A; capture and supported citation added | `cal-exact-s688-copy-cited` | SOLE FAIL only | killed, but not for duplicate URL |
| S688 live URL reused by S693, A; heading/byline quote | `copied-s688-url-heading` | all PASS | survived |
| S687 live URL and body quote reused by S693, C relabelled A | `copied-s687-url-body` | all PASS | survived |

Seven forbidden registry changes are killed by APPEND alone. S687 used-by passes intentionally. S650b is invisible to ROWID (`^\|\s*(S\d{3,})\s*\|`), so neither APPEND nor ACCESS regards it as a registry row. This is a parser coverage finding under the requested test, not permission to broaden the frozen literal `S###` contract.

An unadorned S688→S693 copy (id and tier only) passes APPEND but fails ROWS (uncited and no capture), against an already failing base. After adding a cited line and capture metadata, its **exact original quote** passes ROWS/APPEND/LINK/COPY/LOCATE but fails **SOLE only**, because the anchor says neither talaria nor Hermes. No leg identifies the duplicate URL. The heading and Theoi-body variants above satisfy that name check and pass completely.

## Per-item control verdicts

NONE-MET S665-quote: `cal-s665-quote.patch`, killed by APPEND; no change required for this mutation.
NONE-MET S687-tier: `cal-s687-tier.patch`, killed by APPEND; no change required.
NONE-MET S692-kind: `cal-s692-kind.patch`, killed by APPEND; no change required.
NONE-MET S687-used-by: `cal-s687-used-by.patch`, allowed PASS by the frozen contract; no change required.
NONE-MET S687-teaches: `cal-s687-teaches.patch`, killed by APPEND; no change required.
NONE-MET delete-base-row: `cal-delete-s688.patch`, killed by APPEND; no change required.
NONE-MET S700: `cal-insert-s700.patch`, killed by APPEND; no change required.
CONTROL-MET S650b: `cal-insert-s650b.patch`, full PASS; smallest stopping change is to recognize all inserted S-prefixed table-row ids and reject noncanonical/out-of-block ids rather than silently ignoring S650b. The fixture includes the already demonstrated cheap calibration.
NONE-MET reorder-base-rows: `cal-reorder-s687-s688.patch`, killed by APPEND; no change required.
NONE-MET exact-S688-copy: `cal-exact-s688-copy-cited.patch`, killed by SOLE only; do not misreport this as a duplicate-URL check.
CONTROL-MET reused-existing-URL: `copied-s688-url-heading.patch` and `copied-s687-url-body.patch`, both full PASS; smallest stopping change is NEW-live-URL disjointness from BASE registry URLs in ROWS/FRESH.

## Fixture paths and restoration

All named `.patch` fixtures are relative to the frozen clone's inputs and saved in `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/`. `cal-*` patches include the shared passing calibration plus the one tested mutation. Artifacts:

- Clone, restored to exact original target bytes: `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/clone`.
- Passing calibration registry: `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/calibration.SOURCES.txt`.
- Passing calibration entry: `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/calibration.entry.txt`.
- Machine-readable complete run evidence: `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/runs.json`.

Exact byte equality was asserted after each restoration, and finally for registry, entry, and counter. Final detector output returns to the original base failure. The passing calibration registry SHA-256 is `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`; its entry SHA-256 is `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

| File | Initial SHA-256 | Final restored SHA-256 |
|---|---|---|
| corpus/SOURCES.md | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` |
| footwear entry | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` |
| accept-d.py | `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` | `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4` |

## Retained patch fixtures

- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/s687-tier.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/s692-kind.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/s687-used-by.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/s687-teaches.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/delete-s688.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/insert-s700.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/insert-s650b.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/reorder-s687-s688.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/duplicate-s688-as-s693.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/s665-quote.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/copied-s688-url-heading.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-s665-quote.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-s687-tier.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-s692-kind.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-s687-used-by.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-s687-teaches.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-delete-s688.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-insert-s700.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-insert-s650b.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-reorder-s687-s688.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/cal-exact-s688-copy-cited.patch`
- `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/copied-s687-url-body.patch`

## Full detector receipts

All 46 executions are included without stdout truncation. Working directory on each run: `/fast/scratch/hyaku/kotodama-r62/CtlDRegistryEdits/clone`. Command: `timeout 900 python3 -B reports/round-62/accept-d.py`; stdout and actual exit are below. All stderr streams were empty. No counter revision or live-leg bypass was used. The initial standalone run is included as `initial-pristine`; later outputs were captured directly from the bounded subprocess. Receipt `stopped-by` lists legs only, excluding the final aggregate label.

### initial-pristine

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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

RECEIPT CtlDRegistryEdits/initial-pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### pristine

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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

RECEIPT CtlDRegistryEdits/pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### s665-quote

Registry SHA-256: `f0ccb78f8b0907186c33b101f369b85a722a9728e8f4bc8a76cf2795f6bb3078`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND FAIL base_lines=746 matched=619 missing=['S665', 'S666', 'S667', 'S668', 'S669'] inserted_rows=['S665', 'S666', 'S667', 'S668', 'S669', 'S670', 'S671', 'S672', 'S673', 'S674', 'S675', 'S676', 'S677', 'S678', 'S679', 'S680', 'S681', 'S682', 'S683', 'S684', 'S685', 'S686', 'S687', 'S688', 'S689', 'S690', 'S691', 'S692']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:57Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s665-quote counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,APPEND,LOCATE

### s665-quote-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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

RECEIPT CtlDRegistryEdits/s665-quote-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### s687-tier

Registry SHA-256: `44e6ca4198dee905d943f297d6731b625d1663183f45216d112adcef18114c9f`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=A
ROWS FAIL cited=[] registry=[] bad=[]
APPEND FAIL base_lines=746 matched=641 missing=['S687', 'S688', 'S689', 'S690', 'S691'] inserted_rows=['S687', 'S688', 'S689', 'S690', 'S691', 'S692']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s687-tier counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,APPEND,LOCATE

### s687-tier-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s687-tier-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### s692-kind

Registry SHA-256: `3b529943a50038e898806b00818b64c58356bcdbf8803f72fc1c02d085f86ac6`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND FAIL base_lines=746 matched=646 missing=['S692', '', '## Paths', '', '- Typology evidence chain — S001 → S002 '] inserted_rows=['S692']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s692-kind counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,APPEND,LOCATE

### s692-kind-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s692-kind-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### s687-used-by

Registry SHA-256: `8c64098065e0a03eaf43d48f71272c766ccd3534f2da0e7fc21f8c10a9ca44a7`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s687-used-by counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### s687-used-by-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s687-used-by-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### s687-teaches

Registry SHA-256: `a220dcbb2b71e586ebeba1c605a2ab9536d057792ad491b961f51f7256d1de8e`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND FAIL base_lines=746 matched=641 missing=['S687', 'S688', 'S689', 'S690', 'S691'] inserted_rows=['S687', 'S688', 'S689', 'S690', 'S691', 'S692']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:58Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s687-teaches counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,APPEND,LOCATE

### s687-teaches-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/s687-teaches-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### delete-s688

Registry SHA-256: `2c24ae535afb26c82898895e70e267dfb8493b996069c5ed442067ad53adef15`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND FAIL base_lines=746 matched=642 missing=['S688', 'S689', 'S690', 'S691', 'S692'] inserted_rows=['S689', 'S690', 'S691', 'S692']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/delete-s688 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,APPEND,LOCATE

### delete-s688-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/delete-s688-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### insert-s700

Registry SHA-256: `2d26bc48449fa1972c10a661d00854b628c464d02969ae3c7661d4963ad5c404`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND FAIL base_lines=746 matched=746 missing=[] inserted_rows=['S700']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/insert-s700 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,APPEND,LOCATE

### insert-s700-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/insert-s700-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### insert-s650b

Registry SHA-256: `bd2b72cb1dfd9c12ca655dc9a36445e71f3550f5d3b70477157bc225cc839f23`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/insert-s650b counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### insert-s650b-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/insert-s650b-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### reorder-s687-s688

Registry SHA-256: `800fd1de26e4fcfd4c71efef4610a81a3e16b623f0e158bfa894ab6b796cceb1`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND FAIL base_lines=746 matched=642 missing=['S688', 'S689', 'S690', 'S691', 'S692'] inserted_rows=['S688', 'S689', 'S690', 'S691', 'S692']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/reorder-s687-s688 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,APPEND,LOCATE

### reorder-s687-s688-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/reorder-s687-s688-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### duplicate-s688-as-s693

Registry SHA-256: `05998c6bff167acb921678330d8effcdf481c3d02c0bea2e343801aaab344831`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=['S693'] bad=['S693:urls']
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/duplicate-s688-as-s693 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### duplicate-s688-as-s693-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/duplicate-s688-as-s693-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### copied-s688-url-heading

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:01Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDRegistryEdits/copied-s688-url-heading counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-s665-quote

Registry SHA-256: `7740eafcaeb1c0795e0f216a72e68b246be1e74b2922e34f8fbfea528467e60e`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND FAIL base_lines=746 matched=619 missing=['S665', 'S666', 'S667', 'S668', 'S669'] inserted_rows=['S665', 'S666', 'S667', 'S668', 'S669', 'S670', 'S671', 'S672', 'S673', 'S674', 'S675', 'S676', 'S677', 'S678', 'S679', 'S680', 'S681', 'S682', 'S683', 'S684', 'S685', 'S686', 'S687', 'S688', 'S689', 'S690', 'S691', 'S692', 'S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:02Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-s665-quote counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=APPEND

### cal-s665-quote-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-s665-quote-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-s687-tier

Registry SHA-256: `b6e2e7436b8019fe6b6dbf1a81e67803f212660be5870836b28803287f9e4886`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND FAIL base_lines=746 matched=641 missing=['S687', 'S688', 'S689', 'S690', 'S691'] inserted_rows=['S687', 'S688', 'S689', 'S690', 'S691', 'S692', 'S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:02Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-s687-tier counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=APPEND

### cal-s687-tier-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-s687-tier-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-s692-kind

Registry SHA-256: `4ba29af130808686397efd6c665785d738d3c1ebf9348f149280be7f1d8ef9a5`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND FAIL base_lines=746 matched=646 missing=['S692', '', '## Paths', '', '- Typology evidence chain — S001 → S002 '] inserted_rows=['S692', 'S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:03Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-s692-kind counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=APPEND

### cal-s692-kind-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-s692-kind-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-s687-used-by

Registry SHA-256: `4f9c7f3ccfca77b6be503cf657fe9865b6e5f48ca0f96107c6263a4e51aab45f`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-s687-used-by counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-s687-used-by-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-s687-used-by-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-s687-teaches

Registry SHA-256: `f653bae9a937a593cc9df5e91f403df92e8a802e07e46deb75d29a493c9d4c23`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND FAIL base_lines=746 matched=641 missing=['S687', 'S688', 'S689', 'S690', 'S691'] inserted_rows=['S687', 'S688', 'S689', 'S690', 'S691', 'S692', 'S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:03Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-s687-teaches counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=APPEND

### cal-s687-teaches-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-s687-teaches-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-delete-s688

Registry SHA-256: `ec2bc930149334c70df9933053348009c9403400e82c9a9f4efa79fe52b72696`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND FAIL base_lines=746 matched=642 missing=['S688', 'S689', 'S690', 'S691', 'S692'] inserted_rows=['S689', 'S690', 'S691', 'S692', 'S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-delete-s688 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=APPEND

### cal-delete-s688-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-delete-s688-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-insert-s700

Registry SHA-256: `b147b2839075cc5b6e1b75b7d25b492da08688eded0a68fcea1eb4b8d7543382`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND FAIL base_lines=746 matched=746 missing=[] inserted_rows=['S693', 'S700']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:04Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-insert-s700 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=APPEND

### cal-insert-s700-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-insert-s700-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-insert-s650b

Registry SHA-256: `535f429f6032cf1b430a6a4d62e9a530865334b62e8d26b8e05f8c286a70bdbe`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-insert-s650b counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-insert-s650b-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
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

RECEIPT CtlDRegistryEdits/cal-insert-s650b-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-reorder-s687-s688

Registry SHA-256: `49c88b430d626e532d15c47cd49c7ac90e8ca021fbc5ea19c04bf1d66db8414b`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND FAIL base_lines=746 matched=642 missing=['S688', 'S689', 'S690', 'S691', 'S692'] inserted_rows=['S688', 'S689', 'S690', 'S691', 'S692', 'S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-reorder-s687-s688 counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=APPEND

### cal-reorder-s687-s688-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDRegistryEdits/cal-reorder-s687-s688-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### cal-exact-s688-copy-cited

Registry SHA-256: `22b462f31512203068afbb84f06a7cb8c2bdece7b9efcc0e7e682df4fa01b01a`. Entry SHA-256: `33a2ff4c862d5c1a84e5c57acdd87971509ad4112b59dc0ee4e555084a0a217c`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE FAIL id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/cal-exact-s688-copy-cited counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SOLE

### cal-exact-s688-copy-cited-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDRegistryEdits/cal-exact-s688-copy-cited-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### copied-s687-url-body

Registry SHA-256: `c648aec953ed16fe0973a2853d76297a3083ecb3c4dea916d86139ac8238be96`. Entry SHA-256: `a6fbfa997fd7168ccd7b44750ece19a0b6f561236713abde58fa25037547b851`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:05Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDRegistryEdits/copied-s687-url-body counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### copied-s687-url-body-restored

Registry SHA-256: `857502e15c29b5c8c530aaf8ba54943c4f14c5adb44e316268a0a1c7256c8019`. Entry SHA-256: `93269655a4d5b6fddc46b0f4af05679ca5f530664edcef06291b3f9ec5a6f508`.

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S693']
NOMARK PASS marked=[]
OPEN PASS ids=['S692']
HEDGE PASS ids=['S666']
CAPTION PASS ids=['S665']
SOLE PASS id=S693 tier=A
ROWS PASS cited=['S693'] registry=['S693'] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=['S693']
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE PASS located=1 cited=1 at=2026-10-23T11:06Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: PASS
exit=0
```

RECEIPT CtlDRegistryEdits/copied-s687-url-body-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=-

### final-pristine-restored

Registry SHA-256: `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2`. Entry SHA-256: `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72`.

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
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:06Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT CtlDRegistryEdits/final-pristine-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

