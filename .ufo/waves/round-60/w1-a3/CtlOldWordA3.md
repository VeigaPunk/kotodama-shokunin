CONTROL-MET: CtlOldWordA3/c-synonyms

# Old-wording control — revision 5

**Probe only, not a frozen-counter PASS.** Trivial synonyms preserve the rejected over-reach while passing every non-SUPPORT leg. The frozen counter rejects fabricated sessions. The authorized SESSIONS-only probe admits them and returns PASS when their synthetic verdicts endorse every real block. Supplying rejection verdicts instead makes SUPPORT alone fail. This is the expected semantic boundary: only genuine blind SUPPORT stands between (c) and PASS after provenance is satisfied. This report does not judge or admit the claim, and does not recommend treating synthetic verdicts as evidence.

## Axes and counterexample

- **Depth (declared axis):** token overlap and absence of four literal phrases do not establish source-supported scope, comparison or certainty.
- **Calibration (diagnostic impact, not another claim):** a mechanical PASS must not be represented as independent semantic support.
- **Provenance/control integrity:** fabricated reports and transcripts fail the frozen counter; the probe deliberately removes only the session-file-location barrier.

Strongest counterexample, `c-synonyms`:

| Row | Trivial change | Over-reach retained |
|---|---|---|
| S648 / S602 | `usually aimed` → `typically aimed`; teaches `favoured` → `preferred` | A general statement about protective objects inferred from Pazuzu's particular use. |
| S649 / S616 | `power lay` → `power resided`; `picked` → `selected`; teaches `favourite` → `preferred` | Material-versus-carving comparison still asserted. Both old hematite prose sentences are on one physical line, so the six-word requirement is not weakened or bypassed. |
| S650 / S623 | `highly worn` → `heavily worn`; `act as` → `function as`; teaches `shielded` → `protected` | The apotropaic interpretation is still stated as fact, not a theory. |
| S651 / S643 | Entry `contain` → `hold`; teaches `credited to those contents rather than to the metal shell` → `ascribed to those contents instead of to the metal shell` | The contents-versus-shell contrast remains in teaches. The original entry sentence did not itself contain that contrast. |

Observed shared quote-word counts for (c): **7, 8, 12, 12**. All four quotes locate in the fixture captures using the frozen locator. These lexical properties do not cure the rejected meanings.

## Fixture and evidence provenance

Read `reports/round-60/claims.json` first. Scored the counter from a private clone checked out at `14e6413820d482913f723432b62d566967ccd1a6`; frozen SHA256 **b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc**.

Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/`.

- `build-controls.py` constructs the fixtures; `score-case.py` performs all eight counter invocations and preserves each full stdout, stderr, exit and counter digest in `<case>-<mode>.json` and `.stdout`.
- The requested `/fast/scratch/hyaku/kotodama-r59/entry/amulets-talismans-apotropaic-marks.md` contains **none** of S602/S616/S623/S643; it is the narrowed object (SHA256 `4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d`). I used the surviving as-reviewed `/fast/scratch/hyaku/kotodama-r59/cand/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md`, SHA256 `556ddb27c7e8066ab5b13bb4b1c1f58be118daa13651c1d030574561a10dcf19`. That matches the judged-object hash identified in `corpus/lessons/round-59-verifier-spotcheck.md` §2. The extract is saved as `as-reviewed-extract.txt`.
- (a) substitutes the new ids into the old prose and replaces the four new-id lines of L1's `candidate-entry.md`; all other candidate lines remain. The two hematite prose sentences share one physical line. It retains the inherited new rows and captures.
- (b) uses the same entry as (a), and copies the four frozen rejected Registry rows exactly except their new ids and the required `supersedes <old> —` teaches prefix. Consequently their old `rejected` status and `—` used-by remain; the report separates those failures from the copy/phrase failures.
- (c) uses those old source/quote rows, trivial synonyms in their teaches, `mined` status and the entry used-by; it preserves every substantive old over-reach. `c-rejected` has the same entry/rows/captures as (c), but synthetic verdicts reject the four repaired ids.
- Fixture captures come from L1's inherited `captures/` (untrusted capture provenance, not newly fetched evidence). HTML bytes are copied unchanged. The Pazuzu PDF is converted in full with existing `pdftotext 26.08.0 -raw` to preserve reading order and line-end hyphens; raw PDF SHA256 `2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a`, full extracted-text SHA256 `9b1ca822012b59d97e57669333ee2d5d2de4250869de355eac5e492337bc8183`. Preliminary layout/default extractions did not locate; they were corrected before any counter invocation. No fabricated quote-only capture was used.
- Real blocks and frozen planted blocks are packetized with the pinned `build-packets.py`. Synthetic transcripts contain packet-bound tasks, allowed page `read` calls and matching report writes; **no actual page read or actual reviewer verdict is claimed**. All fake session files are under this sandbox. No live review seat was invoked, messaged or altered. No session file under `~/.omp/` was written.
- The prior outside spot-check §2/§3 records why the old meanings failed; this control does not independently re-open the live pages or replace the later blind review.

Each invocation ran from `.../CtlOldWordA3/clone` with `PYTHONDONTWRITEBYTECODE=1`:

```text
timeout 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/clone/reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/fixtures/<case>
timeout 120 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/fixtures/<case>/reports/round-60/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/fixtures/<case>
```

## Receipts

```text
RECEIPT CtlOldWordA3/a-old-entry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:OLDWORD,ROWS,SUPPORT;probe:OLDWORD,ROWS
RECEIPT CtlOldWordA3/b-old-rows counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:OLDWORD,ROWS,SUPPORT;probe:OLDWORD,ROWS
RECEIPT CtlOldWordA3/c-synonyms counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none
RECEIPT CtlOldWordA3/c-rejected counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT
```

### a-old-entry — frozen, full stdout; exit 1

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed', 'so the amulet s power lay in its material as much as in its carving', 'concealed shoes highly worn and often patched act as apotropaic devices']
ROWS FAIL bad=['S650:line-shares-2-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### a-old-entry — probe, full stdout; exit 1

Counter SHA256 `2035deb9fad2e2e513908437ea2686825a6db6b65ee28129a3dc86f3c22ec04d`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed', 'so the amulet s power lay in its material as much as in its carving', 'concealed shoes highly worn and often patched act as apotropaic devices']
ROWS FAIL bad=['S650:line-shares-2-quote-words']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### b-old-rows — frozen, full stdout; exit 1

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed', 'so the amulet s power lay in its material as much as in its carving', 'concealed shoes highly worn and often patched act as apotropaic devices']
ROWS FAIL bad=['S648:status=rejected,used-by,teaches-copies-S602', 'S649:status=rejected,used-by,teaches-copies-S616', 'S650:status=rejected,used-by,teaches-copies-S623', 'S651:status=rejected,used-by,teaches-copies-S643,old-phrase-in-row']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### b-old-rows — probe, full stdout; exit 1

Counter SHA256 `823154c0c0086308ffc89b692631788f9a025dd30bde8b84527b78aedd0e0446`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD FAIL present=['a protective object is usually aimed', 'so the amulet s power lay in its material as much as in its carving', 'concealed shoes highly worn and often patched act as apotropaic devices']
ROWS FAIL bad=['S648:status=rejected,used-by,teaches-copies-S602', 'S649:status=rejected,used-by,teaches-copies-S616', 'S650:status=rejected,used-by,teaches-copies-S623', 'S651:status=rejected,used-by,teaches-copies-S643,old-phrase-in-row']
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### c-synonyms — frozen, full stdout; exit 1

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### c-synonyms — probe, full stdout; exit 0

Counter SHA256 `6b212f417da617187e582a6a1cf81334efc1d0027c1d6f4badcd3a3415f03455`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
exit=0
```

### c-rejected — frozen, full stdout; exit 1

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S650:NOT/SupportA60', 'S650:NOT/SupportB60', 'S650:NOT/SupportE60', 'S649:NOT/SupportF60', 'S649:NOT/SupportG60', 'S649:NOT/SupportI60', 'S651:NOT/SupportJ60', 'S651:NOT/SupportO60', 'S648:NOT/SupportP60', 'S648:NOT/SupportS60', 'S651:NOT/SupportT60', 'S648:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### c-rejected — probe, full stdout; exit 1

Counter SHA256 `b2910087c2921f04fa618c862ebcdb36a02b0c346fbc0c52f0b9c06a9799cfdf`.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S650:NOT/SupportA60', 'S650:NOT/SupportB60', 'S650:NOT/SupportE60', 'S649:NOT/SupportF60', 'S649:NOT/SupportG60', 'S649:NOT/SupportI60', 'S651:NOT/SupportJ60', 'S651:NOT/SupportO60', 'S648:NOT/SupportP60', 'S648:NOT/SupportS60', 'S651:NOT/SupportT60', 'S648:NOT/SupportX60', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

All eight runs had empty stderr. No other counter invocation was performed.

## Complete probe differences

Only `SESSIONS` changes, separately for each fixture. Frozen counter bytes remain untouched.

```diff
--- frozen/accept-d.py
+++ a-old-entry/accept-d-probe.py
@@ -193,3 +193,3 @@
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/fake-sessions/a-old-entry/KotodamaR60A3.{seat}.jsonl"  # synthetic control only
 
```

```diff
--- frozen/accept-d.py
+++ b-old-rows/accept-d-probe.py
@@ -193,3 +193,3 @@
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/fake-sessions/b-old-rows/KotodamaR60A3.{seat}.jsonl"  # synthetic control only
 
```

```diff
--- frozen/accept-d.py
+++ c-synonyms/accept-d-probe.py
@@ -193,3 +193,3 @@
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/fake-sessions/c-synonyms/KotodamaR60A3.{seat}.jsonl"  # synthetic control only
 
```

```diff
--- frozen/accept-d.py
+++ c-rejected/accept-d-probe.py
@@ -193,3 +193,3 @@
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlOldWordA3/fake-sessions/c-rejected/KotodamaR60A3.{seat}.jsonl"  # synthetic control only
 
```

## Smallest safe correction and review boundary

1. For wording, keep the candidate's source-scoped repair rather than any synonymized generalization; remove the material/carving and contents/shell comparisons, and preserve the source's uncertainty about concealed shoes. Correct teaches as well as entry text.
2. For control interpretation, retain the frozen semantic SUPPORT requirement and provenance checks. Expanding a phrase blacklist cannot certify entailment. The observed probe PASS is an expected limit, not evidence that the live frozen counter accepts fake provenance or that the candidate is supported.
3. Before any data, the integration owner should classify and commit this receipt under the canonical pre-data rules. I make no admission, predicate change or canonical Rust judgment. No reviewed row or line was removed after any real verdict.

No installs or updates. All processes were timeout-capped and completed synchronously; no background job or live service was started. Last measured sandbox size: **107,076,746 bytes**, below 200 MB. The clone uses `--no-hardlinks --no-checkout` plus sparse checkout of `corpus` and `reports/round-60`, then checkout of the required revision, to avoid copying unrelated large reports. Only this report was written in the lane; all other generated files are inside this seat's sandbox.
