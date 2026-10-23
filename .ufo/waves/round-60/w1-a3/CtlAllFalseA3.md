NONE-MET

# CtlAllFalseA3 — pre-data all-false and single-dissent controls

Recorded 2026-10-23T07:09:53.854Z. Scope: assigned control review only, not a claim judgment or admission.

## Axes

- **Depth** (declared axis): retain the whole 47-id judged object and all four repaired propositions.
- **Reject-all resistance:** planted-row qualification must not make an all-NOT reviewer sufficient.
- **Single-dissent sensitivity:** two counted positives must never overrule a mapped NOT-SUPPORTED.
- **Provenance / reproducibility:** distinguish the untouched counter from a SESSIONS-only synthetic probe.

## Counterexamples and evidence

All three intended counterexamples were rejected by both counters (exit 1). In the final, source-derived-text fixtures, SET, LINES, OLDWORD, ROWS, PINNED and JUDGED all pass; only SUPPORT fails. No claimed work was actually performed by a reviewer: all session records and verdict files are visibly marked synthetic, no live support seat was dispatched, contacted, or used, and no page fetch was executed.

| Final fixture | Real verdict distribution | Probe evidence | Result |
|---|---|---|---|
| a-all-false-raw | Every shown verdict NOT-SUPPORTED: 141 real-label negatives; all 48 planted-label negatives | All 24 seats qualify synthetically, but every id has zero counted positives and explicit rejections | SUPPORT FAIL |
| b-one-negative-per-id-raw | Each of 47 real ids has exactly 1 negative and 2 positives on 3 distinct seats; all planted labels negative | All 24 seats qualify; SUPPORT lists all 47 mapped rejections and **no good-count deficit** | SUPPORT FAIL |
| c-single-S648-negative-raw | Exactly 1 real negative in the entire fixture, on S648; its other 2 seats positive; all other 46 ids have 3 positives | All 24 seats qualify; the entire unsupported list is exactly `['S648:NOT/SupportA60']` | SUPPORT FAIL |

The single-dissent mapping is SupportA60/P01, SupportG60/P05, SupportM60/P01. Only the first mapping is negative in case c; the latter two remain SUPPORTED in both each fixture report and its synthetic own-write transcript. The counter therefore exercises the unconditional veto, not a missing-second-review shortcut.

Local code evidence at frozen revision: `reports/round-60/accept-d.py:557-571` checks provenance/blindness/confinement/binding and qualification; `:574-579` records every mapped real-label NOT before packet-match/counting checks; `:588-594` separately requires two counted positives and rejects any nonempty rejection list. The final c probe output below isolates that exact path.

### Fixable defect versus tradeoff; smallest safe correction

**No predicate defect found by this assigned control.** Keep the frozen single-NOT kill rule and existing unconditional rejection collection. A majority-vote or two-positive override would weaken the declared predicate; it is not a safe correction. The intentional tradeoff is that a single genuine false-negative verdict fails the entire claim, even with redundant positive reviewers. This review does not adjudicate that tradeoff for the canonical judge.

The only correction made was **inside fresh control fixtures**: the first six runs had an additional S648 PINNED failure because `pdftotext -layout` interleaved the PDF’s two columns. Unedited `pdftotext -raw` output retained the source order and hyphen boundary; fresh fixtures with its hash passed PINNED. The original fixtures and all six confounded runs are preserved below; no verdict, entry, row, or capture of a scored fixture was rewritten. This fixture repair is not evidence that the inherited PDF passes the canonical locator’s PDF conversion, and this review makes no source-support finding.

## Provenance, construction and limits

- Frozen revision: `14e6413820d482913f723432b62d566967ccd1a6`. Clone was created with the prescribed no-hardlinks command and checked out at that revision; its counter hash was observed as `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.
- The inherited L1 patch was applied **only in this seat’s scratch clone**. Candidate entry hash `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`; patch hash `e37abc6d6403a26ecaeb8aa6434dba3d3ffd02775a7e53ce9d1c8090a9ef2d61`. Its entry matched L1/candidate-entry.md byte-for-byte during construction.
- Packets came from the frozen packet builder, not an old verdict fixture. Builder stdout: `cited=47 planted_rows=16 seats=24 planted_per_seat_min=2`. The planted bytes were read from the surviving attempt-2 frozen planted file and rehashed, not inferred from its prior results. Frozen planted hash: `1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682`; generated key hash: `3854d13f06a282948b466c2b4f9fed0458d1b11a02cd4fa9f230905f76596981`.
- Each real id has three distinct packet seats. Case b chooses exactly one of those per id for rejection; case c changes only the S648 mapping stated above. Each seat has two frozen planted blocks, exact dispatched-packet binding, a matching report/own-write verdict sequence, page-URL-shaped read calls, and byte-identical fake-session/transcript bytes. These are fabricated control inputs, **not actual page reads or omp-origin transcripts**.
- Untouched frozen runs fail the internal provenance check with `session-files=0`, so no fabricated reviewer qualifies. The probe changes only SESSIONS to this seat’s fake files; all 24 seats then qualify and the requested rejection semantics remain effective. Only the probe establishes the two-counted-positive condition; the frozen run alone would not. No session file was written under ~/.omp.
- Captures S649–S651 were copied byte-for-byte from L1/captures after checking the supplied manifest hashes. S648 is explicitly a local text derivative of its real L1 PDF, not a quote-only fake page. Final derivative hash `9b1ca822012b59d97e57669333ee2d5d2de4250869de355eac5e492337bc8183`; final fixture manifest hash `1d388f3b6002596481a909f382d30c6dde4a42386c55c29047b79c4a09431f1a`.
- Probe counter hash: `cc7360312fe98d9896838f4cf7f8fef3c58c6c29625cb5e84e4794c8498c81b8`. No rule, threshold, mapping, planted row, or other counter byte changed.
- No network, browser, external judgment runtime, package install/update, background job, lane git/jj write, or unrelated lane-file write was used. All finite shell/subprocess calls were timeout-capped; no child process remains from these completed calls. Last measured sandbox size: 178 MiB (below 200 MiB).
- Reproduction artifacts: `/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/build-controls.py`, `finish-controls.py`, `results.json`, `final-results.json`, `fixtures/`, `outputs/`, and `probe.diff`. No end-to-end live-support, network reachability, canonical PDF-locator, or scholarly wording check is claimed.

## SESSIONS-only probe diff

```diff
--- frozen/accept-d.py
+++ probe/accept-d-probe.py
@@ -192,5 +192,5 @@
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
```

## Control receipts

Each receipt’s `counter-sha256` and `exit` refer to the untouched frozen counter. The probe hash above applies to every probe run; every probe exit was also 1. `stopped-by` lists actual failing printed legs (identical in frozen/probe for each case); provenance appears inside SUPPORT, not as a separately printed leg.

```text
RECEIPT CtlAllFalseA3/a-all-false counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=PINNED,SUPPORT
RECEIPT CtlAllFalseA3/b-one-negative-per-id counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=PINNED,SUPPORT
RECEIPT CtlAllFalseA3/c-single-S648-negative counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=PINNED,SUPPORT
RECEIPT CtlAllFalseA3/a-all-false-raw counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT
RECEIPT CtlAllFalseA3/b-one-negative-per-id-raw counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT
RECEIPT CtlAllFalseA3/c-single-S648-negative-raw counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT
```

## Full stdout and exit codes — every counter run

All counters ran from `/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone`, with `PYTHONDONTWRITEBYTECODE=1`, a sandbox TMPDIR, and a 120-second process timeout. No stdout line has been omitted, shortened, or substituted. Every stderr was empty unless printed explicitly below.

### a-all-false / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/a-all-false
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S614:NOT/SupportF60', 'S640:NOT/SupportF60', 'S605:NOT/SupportF60', 'S649:NOT/SupportF60', 'S632:NOT/SupportF60', 'S624:NOT/SupportF60', 'S604:NOT/SupportG60', 'S613:NOT/SupportG60', 'S622:NOT/SupportG60', 'S648:NOT/SupportG60', 'S639:NOT/SupportG60', 'S631:NOT/SupportG60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S651:NOT/SupportI60', 'S626:NOT/SupportI60', 'S608:NOT/SupportI60', 'S617:NOT/SupportI60', 'S634:NOT/SupportI60', 'S642:NOT/SupportI60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S600:NOT/SupportK60', 'S628:NOT/SupportK60', 'S636:NOT/SupportK60', 'S645:NOT/SupportK60', 'S610:NOT/SupportK60', 'S619:NOT/SupportK60', 'S627:NOT/SupportL60', 'S618:NOT/SupportL60', 'S609:NOT/SupportL60', 'S635:NOT/SupportL60', 'S644:NOT/SupportL60', 'S648:NOT/SupportM60', 'S604:NOT/SupportM60', 'S613:NOT/SupportM60', 'S639:NOT/SupportM60', 'S622:NOT/SupportM60', 'S631:NOT/SupportM60', 'S644:NOT/SupportN60', 'S618:NOT/SupportN60', 'S609:NOT/SupportN60', 'S635:NOT/SupportN60', 'S627:NOT/SupportN60', 'S649:NOT/SupportO60', 'S624:NOT/SupportO60', 'S605:NOT/SupportO60', 'S632:NOT/SupportO60', 'S640:NOT/SupportO60', 'S614:NOT/SupportO60', 'S651:NOT/SupportP60', 'S626:NOT/SupportP60', 'S642:NOT/SupportP60', 'S608:NOT/SupportP60', 'S617:NOT/SupportP60', 'S634:NOT/SupportP60', 'S633:NOT/SupportQ60', 'S641:NOT/SupportQ60', 'S607:NOT/SupportQ60', 'S625:NOT/SupportQ60', 'S650:NOT/SupportQ60', 'S615:NOT/SupportQ60', 'S646:NOT/SupportR60', 'S629:NOT/SupportR60', 'S611:NOT/SupportR60', 'S637:NOT/SupportR60', 'S601:NOT/SupportR60', 'S620:NOT/SupportR60', 'S610:NOT/SupportS60', 'S645:NOT/SupportS60', 'S628:NOT/SupportS60', 'S619:NOT/SupportS60', 'S600:NOT/SupportS60', 'S636:NOT/SupportS60', 'S637:NOT/SupportT60', 'S611:NOT/SupportT60', 'S646:NOT/SupportT60', 'S620:NOT/SupportT60', 'S629:NOT/SupportT60', 'S601:NOT/SupportT60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60', 'S625:NOT/SupportV60', 'S615:NOT/SupportV60', 'S641:NOT/SupportV60', 'S633:NOT/SupportV60', 'S607:NOT/SupportV60', 'S650:NOT/SupportV60', 'S603:NOT/SupportW60', 'S638:NOT/SupportW60', 'S612:NOT/SupportW60', 'S647:NOT/SupportW60', 'S621:NOT/SupportW60', 'S630:NOT/SupportW60', 'S647:NOT/SupportX60', 'S638:NOT/SupportX60', 'S612:NOT/SupportX60', 'S621:NOT/SupportX60', 'S630:NOT/SupportX60', 'S603:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### a-all-false / probe

Counter sha256: `cc7360312fe98d9896838f4cf7f8fef3c58c6c29625cb5e84e4794c8498c81b8`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/a-all-false
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S614:NOT/SupportF60', 'S640:NOT/SupportF60', 'S605:NOT/SupportF60', 'S649:NOT/SupportF60', 'S632:NOT/SupportF60', 'S624:NOT/SupportF60', 'S604:NOT/SupportG60', 'S613:NOT/SupportG60', 'S622:NOT/SupportG60', 'S648:NOT/SupportG60', 'S639:NOT/SupportG60', 'S631:NOT/SupportG60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S651:NOT/SupportI60', 'S626:NOT/SupportI60', 'S608:NOT/SupportI60', 'S617:NOT/SupportI60', 'S634:NOT/SupportI60', 'S642:NOT/SupportI60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S600:NOT/SupportK60', 'S628:NOT/SupportK60', 'S636:NOT/SupportK60', 'S645:NOT/SupportK60', 'S610:NOT/SupportK60', 'S619:NOT/SupportK60', 'S627:NOT/SupportL60', 'S618:NOT/SupportL60', 'S609:NOT/SupportL60', 'S635:NOT/SupportL60', 'S644:NOT/SupportL60', 'S648:NOT/SupportM60', 'S604:NOT/SupportM60', 'S613:NOT/SupportM60', 'S639:NOT/SupportM60', 'S622:NOT/SupportM60', 'S631:NOT/SupportM60', 'S644:NOT/SupportN60', 'S618:NOT/SupportN60', 'S609:NOT/SupportN60', 'S635:NOT/SupportN60', 'S627:NOT/SupportN60', 'S649:NOT/SupportO60', 'S624:NOT/SupportO60', 'S605:NOT/SupportO60', 'S632:NOT/SupportO60', 'S640:NOT/SupportO60', 'S614:NOT/SupportO60', 'S651:NOT/SupportP60', 'S626:NOT/SupportP60', 'S642:NOT/SupportP60', 'S608:NOT/SupportP60', 'S617:NOT/SupportP60', 'S634:NOT/SupportP60', 'S633:NOT/SupportQ60', 'S641:NOT/SupportQ60', 'S607:NOT/SupportQ60', 'S625:NOT/SupportQ60', 'S650:NOT/SupportQ60', 'S615:NOT/SupportQ60', 'S646:NOT/SupportR60', 'S629:NOT/SupportR60', 'S611:NOT/SupportR60', 'S637:NOT/SupportR60', 'S601:NOT/SupportR60', 'S620:NOT/SupportR60', 'S610:NOT/SupportS60', 'S645:NOT/SupportS60', 'S628:NOT/SupportS60', 'S619:NOT/SupportS60', 'S600:NOT/SupportS60', 'S636:NOT/SupportS60', 'S637:NOT/SupportT60', 'S611:NOT/SupportT60', 'S646:NOT/SupportT60', 'S620:NOT/SupportT60', 'S629:NOT/SupportT60', 'S601:NOT/SupportT60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60', 'S625:NOT/SupportV60', 'S615:NOT/SupportV60', 'S641:NOT/SupportV60', 'S633:NOT/SupportV60', 'S607:NOT/SupportV60', 'S650:NOT/SupportV60', 'S603:NOT/SupportW60', 'S638:NOT/SupportW60', 'S612:NOT/SupportW60', 'S647:NOT/SupportW60', 'S621:NOT/SupportW60', 'S630:NOT/SupportW60', 'S647:NOT/SupportX60', 'S638:NOT/SupportX60', 'S612:NOT/SupportX60', 'S621:NOT/SupportX60', 'S630:NOT/SupportX60', 'S603:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### b-one-negative-per-id / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/b-one-negative-per-id
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### b-one-negative-per-id / probe

Counter sha256: `cc7360312fe98d9896838f4cf7f8fef3c58c6c29625cb5e84e4794c8498c81b8`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/b-one-negative-per-id
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### c-single-S648-negative / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/c-single-S648-negative
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### c-single-S648-negative / probe

Counter sha256: `cc7360312fe98d9896838f4cf7f8fef3c58c6c29625cb5e84e4794c8498c81b8`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/c-single-S648-negative
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED FAIL bad=['S648:not-located']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### a-all-false-raw / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/a-all-false-raw
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S614:NOT/SupportF60', 'S640:NOT/SupportF60', 'S605:NOT/SupportF60', 'S649:NOT/SupportF60', 'S632:NOT/SupportF60', 'S624:NOT/SupportF60', 'S604:NOT/SupportG60', 'S613:NOT/SupportG60', 'S622:NOT/SupportG60', 'S648:NOT/SupportG60', 'S639:NOT/SupportG60', 'S631:NOT/SupportG60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S651:NOT/SupportI60', 'S626:NOT/SupportI60', 'S608:NOT/SupportI60', 'S617:NOT/SupportI60', 'S634:NOT/SupportI60', 'S642:NOT/SupportI60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S600:NOT/SupportK60', 'S628:NOT/SupportK60', 'S636:NOT/SupportK60', 'S645:NOT/SupportK60', 'S610:NOT/SupportK60', 'S619:NOT/SupportK60', 'S627:NOT/SupportL60', 'S618:NOT/SupportL60', 'S609:NOT/SupportL60', 'S635:NOT/SupportL60', 'S644:NOT/SupportL60', 'S648:NOT/SupportM60', 'S604:NOT/SupportM60', 'S613:NOT/SupportM60', 'S639:NOT/SupportM60', 'S622:NOT/SupportM60', 'S631:NOT/SupportM60', 'S644:NOT/SupportN60', 'S618:NOT/SupportN60', 'S609:NOT/SupportN60', 'S635:NOT/SupportN60', 'S627:NOT/SupportN60', 'S649:NOT/SupportO60', 'S624:NOT/SupportO60', 'S605:NOT/SupportO60', 'S632:NOT/SupportO60', 'S640:NOT/SupportO60', 'S614:NOT/SupportO60', 'S651:NOT/SupportP60', 'S626:NOT/SupportP60', 'S642:NOT/SupportP60', 'S608:NOT/SupportP60', 'S617:NOT/SupportP60', 'S634:NOT/SupportP60', 'S633:NOT/SupportQ60', 'S641:NOT/SupportQ60', 'S607:NOT/SupportQ60', 'S625:NOT/SupportQ60', 'S650:NOT/SupportQ60', 'S615:NOT/SupportQ60', 'S646:NOT/SupportR60', 'S629:NOT/SupportR60', 'S611:NOT/SupportR60', 'S637:NOT/SupportR60', 'S601:NOT/SupportR60', 'S620:NOT/SupportR60', 'S610:NOT/SupportS60', 'S645:NOT/SupportS60', 'S628:NOT/SupportS60', 'S619:NOT/SupportS60', 'S600:NOT/SupportS60', 'S636:NOT/SupportS60', 'S637:NOT/SupportT60', 'S611:NOT/SupportT60', 'S646:NOT/SupportT60', 'S620:NOT/SupportT60', 'S629:NOT/SupportT60', 'S601:NOT/SupportT60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60', 'S625:NOT/SupportV60', 'S615:NOT/SupportV60', 'S641:NOT/SupportV60', 'S633:NOT/SupportV60', 'S607:NOT/SupportV60', 'S650:NOT/SupportV60', 'S603:NOT/SupportW60', 'S638:NOT/SupportW60', 'S612:NOT/SupportW60', 'S647:NOT/SupportW60', 'S621:NOT/SupportW60', 'S630:NOT/SupportW60', 'S647:NOT/SupportX60', 'S638:NOT/SupportX60', 'S612:NOT/SupportX60', 'S621:NOT/SupportX60', 'S630:NOT/SupportX60', 'S603:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### a-all-false-raw / probe

Counter sha256: `cc7360312fe98d9896838f4cf7f8fef3c58c6c29625cb5e84e4794c8498c81b8`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/a-all-false-raw
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S614:NOT/SupportF60', 'S640:NOT/SupportF60', 'S605:NOT/SupportF60', 'S649:NOT/SupportF60', 'S632:NOT/SupportF60', 'S624:NOT/SupportF60', 'S604:NOT/SupportG60', 'S613:NOT/SupportG60', 'S622:NOT/SupportG60', 'S648:NOT/SupportG60', 'S639:NOT/SupportG60', 'S631:NOT/SupportG60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S651:NOT/SupportI60', 'S626:NOT/SupportI60', 'S608:NOT/SupportI60', 'S617:NOT/SupportI60', 'S634:NOT/SupportI60', 'S642:NOT/SupportI60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S600:NOT/SupportK60', 'S628:NOT/SupportK60', 'S636:NOT/SupportK60', 'S645:NOT/SupportK60', 'S610:NOT/SupportK60', 'S619:NOT/SupportK60', 'S627:NOT/SupportL60', 'S618:NOT/SupportL60', 'S609:NOT/SupportL60', 'S635:NOT/SupportL60', 'S644:NOT/SupportL60', 'S648:NOT/SupportM60', 'S604:NOT/SupportM60', 'S613:NOT/SupportM60', 'S639:NOT/SupportM60', 'S622:NOT/SupportM60', 'S631:NOT/SupportM60', 'S644:NOT/SupportN60', 'S618:NOT/SupportN60', 'S609:NOT/SupportN60', 'S635:NOT/SupportN60', 'S627:NOT/SupportN60', 'S649:NOT/SupportO60', 'S624:NOT/SupportO60', 'S605:NOT/SupportO60', 'S632:NOT/SupportO60', 'S640:NOT/SupportO60', 'S614:NOT/SupportO60', 'S651:NOT/SupportP60', 'S626:NOT/SupportP60', 'S642:NOT/SupportP60', 'S608:NOT/SupportP60', 'S617:NOT/SupportP60', 'S634:NOT/SupportP60', 'S633:NOT/SupportQ60', 'S641:NOT/SupportQ60', 'S607:NOT/SupportQ60', 'S625:NOT/SupportQ60', 'S650:NOT/SupportQ60', 'S615:NOT/SupportQ60', 'S646:NOT/SupportR60', 'S629:NOT/SupportR60', 'S611:NOT/SupportR60', 'S637:NOT/SupportR60', 'S601:NOT/SupportR60', 'S620:NOT/SupportR60', 'S610:NOT/SupportS60', 'S645:NOT/SupportS60', 'S628:NOT/SupportS60', 'S619:NOT/SupportS60', 'S600:NOT/SupportS60', 'S636:NOT/SupportS60', 'S637:NOT/SupportT60', 'S611:NOT/SupportT60', 'S646:NOT/SupportT60', 'S620:NOT/SupportT60', 'S629:NOT/SupportT60', 'S601:NOT/SupportT60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60', 'S625:NOT/SupportV60', 'S615:NOT/SupportV60', 'S641:NOT/SupportV60', 'S633:NOT/SupportV60', 'S607:NOT/SupportV60', 'S650:NOT/SupportV60', 'S603:NOT/SupportW60', 'S638:NOT/SupportW60', 'S612:NOT/SupportW60', 'S647:NOT/SupportW60', 'S621:NOT/SupportW60', 'S630:NOT/SupportW60', 'S647:NOT/SupportX60', 'S638:NOT/SupportX60', 'S612:NOT/SupportX60', 'S621:NOT/SupportX60', 'S630:NOT/SupportX60', 'S603:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### b-one-negative-per-id-raw / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/b-one-negative-per-id-raw
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### b-one-negative-per-id-raw / probe

Counter sha256: `cc7360312fe98d9896838f4cf7f8fef3c58c6c29625cb5e84e4794c8498c81b8`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/b-one-negative-per-id-raw
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S604:NOT/SupportA60', 'S622:NOT/SupportA60', 'S613:NOT/SupportA60', 'S631:NOT/SupportA60', 'S639:NOT/SupportA60', 'S646:NOT/SupportB60', 'S620:NOT/SupportB60', 'S637:NOT/SupportB60', 'S611:NOT/SupportB60', 'S629:NOT/SupportB60', 'S601:NOT/SupportB60', 'S644:NOT/SupportC60', 'S627:NOT/SupportC60', 'S618:NOT/SupportC60', 'S609:NOT/SupportC60', 'S635:NOT/SupportC60', 'S608:NOT/SupportD60', 'S642:NOT/SupportD60', 'S626:NOT/SupportD60', 'S651:NOT/SupportD60', 'S634:NOT/SupportD60', 'S617:NOT/SupportD60', 'S649:NOT/SupportE60', 'S605:NOT/SupportE60', 'S624:NOT/SupportE60', 'S640:NOT/SupportE60', 'S614:NOT/SupportE60', 'S632:NOT/SupportE60', 'S650:NOT/SupportH60', 'S641:NOT/SupportH60', 'S615:NOT/SupportH60', 'S625:NOT/SupportH60', 'S607:NOT/SupportH60', 'S633:NOT/SupportH60', 'S628:NOT/SupportJ60', 'S610:NOT/SupportJ60', 'S600:NOT/SupportJ60', 'S636:NOT/SupportJ60', 'S619:NOT/SupportJ60', 'S645:NOT/SupportJ60', 'S603:NOT/SupportU60', 'S630:NOT/SupportU60', 'S612:NOT/SupportU60', 'S621:NOT/SupportU60', 'S638:NOT/SupportU60', 'S647:NOT/SupportU60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### c-single-S648-negative-raw / frozen

Counter sha256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/c-single-S648-negative-raw
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### c-single-S648-negative-raw / probe

Counter sha256: `cc7360312fe98d9896838f4cf7f8fef3c58c6c29625cb5e84e4794c8498c81b8`.

```sh
# cwd: /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/clone
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/tmp python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlAllFalseA3/fixtures/c-single-S648-negative-raw
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportA60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

## Impact and correction

- **Depth / kill-rule integrity:** the entire 47-id veto survives these controls; no narrowing or row deletion was needed.
- **Reject-all resistance:** passing planted negatives alone is insufficient.
- **False provenance:** only the explicitly weakened provenance probe counts the synthetic seats; do not reuse its results as data support or frozen acceptance.
- **Smallest safe correction:** none to the counter for the tested shapes. Retain the original failure receipts plus the isolated raw-text receipts, and do not reinterpret two positives as permission to discard a NOT.

No admission, integration, shipping decision, or canonical judgment is made here.
