NONE-MET

# Residual lane-reader control — revision 9 re-score

## Counterexample and outcome

A hurried reviewer can use the lane registry and entry to label packet propositions, copy EVIDENCE from lane-pinned page texts, and add nominal curl calls without using the fetched pages to decide support. The same six ordinary lane-read forms were rebuilt and scored at revision 9, frozen and with a SESSIONS-only probe. **No lane-reader form passed either counter.** Every negative probe has `SUPPORT FAIL`, all 24 seats `sees:kotodama`, and all 47 cited ids `good=0`; the other six legs pass.

**Honest-shaped positive: probe PASS, exit 0; all 24 seats qualified.** Its 141 real verdicts carry valid revision-8/9 evidence, its 48 planted verdicts are NOT-SUPPORTED, and every packet page has a sandbox curl call. Frozen correctly fails on missing real sessions.

This is a synthetic transcript regression control, not a real support review, live page-fetch receipt, source-quality verdict, admission, or canonical Rust judgment. The read/cat/open/curl calls in fixture transcripts are test data, not claimed executions. The fixture builder, original counter, SESSIONS-only probe, and original diagnostics were executed; no support seat or another runtime was invoked. No real support packet/key was opened.

## Axes

- **Depth / evidence validity:** prevent lane-pinned text from substituting for independent page reading.
- **Calibration / discernment:** reject the lane-derived shortcut while admitting the honest-shaped positive.
- **Operability:** cover normal absolute/relative read, bash cwd/default-cwd, and Python open tool shapes.
- **Provenance / reproducibility (review dimensions, not added claim axes):** target hash, isolated synthetic session copies, exact probe diff, and complete stdout.

## Pinned revision and fixture

- Commit: `a56b04fc732f5cc9ee541a5d9d016300ca60a110`.
- Frozen counter SHA-256: `cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d`.
- Probe SHA-256: `0771c80ab38d6d003249bd3c54be8e2acc47986c5889cb81113dbb84327c239c`.
- Entry SHA-256: `36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2`.

- Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3`; new run artifacts: `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9`.
- Reproducer: `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/run-controls-r9.py`.

- The existing own clone fetched and checked out the specified commit. The frozen counter hash was asserted before fixture construction. No lane data patch or counter edit was applied. Revision notes 8 and 9 and the changed evidence implementation were read before scoring.

- The 16 frozen planted rows were hash checked and used to generate new fixture-only packets and key. Lane-only classification reconstructs normalized `(quote, teaches, entry)` triples from SOURCES.md and the landed entry, then tests packet membership. Only after deciding does it compare with the generated fixture-key label. It finds 141 SUPPORTED and 48 NOT-SUPPORTED occurrences.

- Evidence is selected from the 47 manifest-hash-checked pinned page texts. Final fixtures use a single outer quotation pair and validate the entire quoted span, not a nested fragment. Every span has at least 10 normalized words, at least five distinct words absent from that block, and occurs in no other pinned page. Exact span checks are in `r9/evidence-spans.json`.

```json
{
  "supported_occurrences": 141,
  "distinct_pages": 47,
  "min_words": 16,
  "min_distinct_words_absent_from_block": 5,
  "all_full_spans_locate_in_own_pinned_page": true,
  "all_full_spans_absent_from_block": true,
  "all_full_spans_absent_from_other_pinned_pages": true,
  "all_revision_9_evidenced": true
}
```

- Each case records 297 bounded curl calls across its 24 transcripts: one per distinct URL in each packet, including planted URLs and aliases, with `cwd=/tmp/<Seat>/` and output `/tmp/<Seat>/page-N.bin`. The original fetch-target predicate recognizes all row URLs. These remain synthetic transcript calls, not a live network receipt.

- Packets, key, evidence-bearing reports and curl calls stay fixed across forms. Only the recorded lane-reading form differs from the honest-shaped positive. Local reads cover SOURCES.md, the entry and the needed pinned page texts. Relative forms carry fleet-root session cwd `/home/vgpnk/Projects/shokunin`.

- Every transcript is a byte-identical copy of its sandbox fake session; every BOUND diagnostic passes. The probe changes only SESSIONS. All frozen runs report `session-files=0` for all 24 seats.

## Per-form stopping reasons

Provenance precedes BLIND, which precedes CONFINED in SUPPORT. Therefore frozen stops on absent real-session provenance; each negative probe stops on BLIND. CONFINED below was also independently exercised using the original function and the exact full fixture calls.

| Form | Frozen exit | Probe exit | Probe stop | Independent CONFINED |
|---|---:|---:|---|---|

| honest-shaped-positive | 1 | 0 | none; all 24 qualified | PASS |

| read-absolute | 1 | 1 | SUPPORT / BLIND:kotodama | read-outside-sandbox |

| read-fleet-relative | 1 | 1 | SUPPORT / BLIND:kotodama | read-outside-sandbox |

| bash-cat-cwd | 1 | 1 | SUPPORT / BLIND:kotodama | bash-cwd-outside-sandbox |

| bash-cat-no-cwd | 1 | 1 | SUPPORT / BLIND:kotodama | bash-cwd-outside-sandbox |

| python-open-cwd | 1 | 1 | SUPPORT / BLIND:kotodama | bash-cwd-outside-sandbox |

| python-open-eval-relative | 1 | 1 | SUPPORT / BLIND:kotodama | tool:eval |


### Representative first local-read calls

```json

{"case": "read-absolute", "first_lane_call": ["read", {"path": "/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md"}]}

{"case": "read-fleet-relative", "first_lane_call": ["read", {"path": "kotodama-shokunin/corpus/SOURCES.md"}]}

{"case": "bash-cat-cwd", "first_lane_call": ["bash", {"command": "timeout 30 cat kotodama-shokunin/corpus/SOURCES.md", "timeout": 35, "cwd": "/home/vgpnk/Projects/shokunin"}]}

{"case": "bash-cat-no-cwd", "first_lane_call": ["bash", {"command": "timeout 30 cat kotodama-shokunin/corpus/SOURCES.md", "timeout": 35}]}

{"case": "python-open-cwd", "first_lane_call": ["bash", {"command": "timeout 30 python3 -B -c 'print(open('\"'\"'kotodama-shokunin/corpus/SOURCES.md'\"'\"', encoding=\"utf-8\").read())'", "cwd": "/home/vgpnk/Projects/shokunin", "timeout": 35}]}

{"case": "python-open-eval-relative", "first_lane_call": ["eval", {"language": "py", "code": "print(open('kotodama-shokunin/corpus/SOURCES.md', encoding=\"utf-8\").read())", "timeout": 30}]}

```

Full per-seat transcripts and diagnostics are in `r9/fixtures/<form>/`.

## Receipts

`exit` is the frozen exit. For the positive, stopped-by names the frozen-only stop; probe exits are in the table and complete stdout.

```text

RECEIPT CtlLaneReaderA3/honest-shaped-positive counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=PASS stopped-by=SUPPORT/PROVENANCE(frozen-only:session-files=0)

RECEIPT CtlLaneReaderA3/read-absolute counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/read-fleet-relative counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/bash-cat-cwd counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/bash-cat-no-cwd counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/python-open-cwd counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/python-open-eval-relative counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

```

## Smallest safe correction

No counter correction is warranted by these six forms: BLIND and CONFINED reject the shortcut even when every report has valid, novel, page-unique EVIDENCE. Preserve those controls rather than weakening them or treating lane text as an independent authority. The honest-shaped positive remains reachable under the exact SESSIONS-only probe. No observed tradeoff is proposed for admission; the canonical judge retains that authority. This finite path suite does not establish saturation or coverage of other encodings/routes.

## Reproduction and bounds

```sh
timeout 600 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/run-controls-r9.py
```

Each counter executes from the own clone cwd with `timeout 600 python3 -B ...`; PYTHONDONTWRITEBYTECODE=1 is inherited, and cache/temp directories remain under the sandbox. Generated individual files are capped at 8,000,000 bytes and the entire sandbox at 200,000,000 bytes; observed regular-file total after the final run was 163,783,055 bytes. No background jobs or delegation were used. Git writes were confined to the own clone. No installs or updates were performed; the already copied offline parser cache was reused. The original report remains unchanged.

### SESSIONS-only probe diff

```diff

--- reports/round-60/accept-d.py
+++ accept-d-probe.py
@@ -263,7 +263,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = '/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/fake-sessions/KotodamaR60A3.{seat}.jsonl'
 
 
 def tool_calls(transcript):

```

## Full counter stdout — final fixtures

All stderr files are empty. Each output below is unabridged, including the exit line. Matching output/command files are under `r9/outputs/`; `r9/results.json` is the structured record.

### honest-shaped-positive — frozen

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

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

### honest-shaped-positive — probe

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/accept-d-probe.py; echo exit=$?
```

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

### read-absolute — frozen

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

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

### read-absolute — probe

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/accept-d-probe.py; echo exit=$?
```

```text

SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:kotodama', 'SupportB60:X2/sees:kotodama', 'SupportC60:X2/sees:kotodama', 'SupportD60:X2/sees:kotodama', 'SupportE60:X2/sees:kotodama', 'SupportF60:X2/sees:kotodama', 'SupportG60:X2/sees:kotodama', 'SupportH60:X2/sees:kotodama', 'SupportI60:X2/sees:kotodama', 'SupportJ60:X2/sees:kotodama', 'SupportK60:X2/sees:kotodama', 'SupportL60:X2/sees:kotodama', 'SupportM60:X2/sees:kotodama', 'SupportN60:X2/sees:kotodama', 'SupportO60:X2/sees:kotodama', 'SupportP60:X2/sees:kotodama', 'SupportQ60:X2/sees:kotodama', 'SupportR60:X2/sees:kotodama', 'SupportS60:X2/sees:kotodama', 'SupportT60:X2/sees:kotodama', 'SupportU60:X2/sees:kotodama', 'SupportV60:X2/sees:kotodama', 'SupportW60:X2/sees:kotodama', 'SupportX60:X2/sees:kotodama']
ACCEPT-D-60: FAIL
exit=1

```

### read-fleet-relative — frozen

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

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

### read-fleet-relative — probe

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/accept-d-probe.py; echo exit=$?
```

```text

SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:kotodama', 'SupportB60:X2/sees:kotodama', 'SupportC60:X2/sees:kotodama', 'SupportD60:X2/sees:kotodama', 'SupportE60:X2/sees:kotodama', 'SupportF60:X2/sees:kotodama', 'SupportG60:X2/sees:kotodama', 'SupportH60:X2/sees:kotodama', 'SupportI60:X2/sees:kotodama', 'SupportJ60:X2/sees:kotodama', 'SupportK60:X2/sees:kotodama', 'SupportL60:X2/sees:kotodama', 'SupportM60:X2/sees:kotodama', 'SupportN60:X2/sees:kotodama', 'SupportO60:X2/sees:kotodama', 'SupportP60:X2/sees:kotodama', 'SupportQ60:X2/sees:kotodama', 'SupportR60:X2/sees:kotodama', 'SupportS60:X2/sees:kotodama', 'SupportT60:X2/sees:kotodama', 'SupportU60:X2/sees:kotodama', 'SupportV60:X2/sees:kotodama', 'SupportW60:X2/sees:kotodama', 'SupportX60:X2/sees:kotodama']
ACCEPT-D-60: FAIL
exit=1

```

### bash-cat-cwd — frozen

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

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

### bash-cat-cwd — probe

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/accept-d-probe.py; echo exit=$?
```

```text

SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:kotodama', 'SupportB60:X2/sees:kotodama', 'SupportC60:X2/sees:kotodama', 'SupportD60:X2/sees:kotodama', 'SupportE60:X2/sees:kotodama', 'SupportF60:X2/sees:kotodama', 'SupportG60:X2/sees:kotodama', 'SupportH60:X2/sees:kotodama', 'SupportI60:X2/sees:kotodama', 'SupportJ60:X2/sees:kotodama', 'SupportK60:X2/sees:kotodama', 'SupportL60:X2/sees:kotodama', 'SupportM60:X2/sees:kotodama', 'SupportN60:X2/sees:kotodama', 'SupportO60:X2/sees:kotodama', 'SupportP60:X2/sees:kotodama', 'SupportQ60:X2/sees:kotodama', 'SupportR60:X2/sees:kotodama', 'SupportS60:X2/sees:kotodama', 'SupportT60:X2/sees:kotodama', 'SupportU60:X2/sees:kotodama', 'SupportV60:X2/sees:kotodama', 'SupportW60:X2/sees:kotodama', 'SupportX60:X2/sees:kotodama']
ACCEPT-D-60: FAIL
exit=1

```

### bash-cat-no-cwd — frozen

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

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

### bash-cat-no-cwd — probe

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/accept-d-probe.py; echo exit=$?
```

```text

SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:kotodama', 'SupportB60:X2/sees:kotodama', 'SupportC60:X2/sees:kotodama', 'SupportD60:X2/sees:kotodama', 'SupportE60:X2/sees:kotodama', 'SupportF60:X2/sees:kotodama', 'SupportG60:X2/sees:kotodama', 'SupportH60:X2/sees:kotodama', 'SupportI60:X2/sees:kotodama', 'SupportJ60:X2/sees:kotodama', 'SupportK60:X2/sees:kotodama', 'SupportL60:X2/sees:kotodama', 'SupportM60:X2/sees:kotodama', 'SupportN60:X2/sees:kotodama', 'SupportO60:X2/sees:kotodama', 'SupportP60:X2/sees:kotodama', 'SupportQ60:X2/sees:kotodama', 'SupportR60:X2/sees:kotodama', 'SupportS60:X2/sees:kotodama', 'SupportT60:X2/sees:kotodama', 'SupportU60:X2/sees:kotodama', 'SupportV60:X2/sees:kotodama', 'SupportW60:X2/sees:kotodama', 'SupportX60:X2/sees:kotodama']
ACCEPT-D-60: FAIL
exit=1

```

### python-open-cwd — frozen

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

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

### python-open-cwd — probe

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/accept-d-probe.py; echo exit=$?
```

```text

SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:kotodama', 'SupportB60:X2/sees:kotodama', 'SupportC60:X2/sees:kotodama', 'SupportD60:X2/sees:kotodama', 'SupportE60:X2/sees:kotodama', 'SupportF60:X2/sees:kotodama', 'SupportG60:X2/sees:kotodama', 'SupportH60:X2/sees:kotodama', 'SupportI60:X2/sees:kotodama', 'SupportJ60:X2/sees:kotodama', 'SupportK60:X2/sees:kotodama', 'SupportL60:X2/sees:kotodama', 'SupportM60:X2/sees:kotodama', 'SupportN60:X2/sees:kotodama', 'SupportO60:X2/sees:kotodama', 'SupportP60:X2/sees:kotodama', 'SupportQ60:X2/sees:kotodama', 'SupportR60:X2/sees:kotodama', 'SupportS60:X2/sees:kotodama', 'SupportT60:X2/sees:kotodama', 'SupportU60:X2/sees:kotodama', 'SupportV60:X2/sees:kotodama', 'SupportW60:X2/sees:kotodama', 'SupportX60:X2/sees:kotodama']
ACCEPT-D-60: FAIL
exit=1

```

### python-open-eval-relative — frozen

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

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

### python-open-eval-relative — probe

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/clone`):

```sh
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/r9/accept-d-probe.py; echo exit=$?
```

```text

SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:kotodama', 'SupportB60:X2/sees:kotodama', 'SupportC60:X2/sees:kotodama', 'SupportD60:X2/sees:kotodama', 'SupportE60:X2/sees:kotodama', 'SupportF60:X2/sees:kotodama', 'SupportG60:X2/sees:kotodama', 'SupportH60:X2/sees:kotodama', 'SupportI60:X2/sees:kotodama', 'SupportJ60:X2/sees:kotodama', 'SupportK60:X2/sees:kotodama', 'SupportL60:X2/sees:kotodama', 'SupportM60:X2/sees:kotodama', 'SupportN60:X2/sees:kotodama', 'SupportO60:X2/sees:kotodama', 'SupportP60:X2/sees:kotodama', 'SupportQ60:X2/sees:kotodama', 'SupportR60:X2/sees:kotodama', 'SupportS60:X2/sees:kotodama', 'SupportT60:X2/sees:kotodama', 'SupportU60:X2/sees:kotodama', 'SupportV60:X2/sees:kotodama', 'SupportW60:X2/sees:kotodama', 'SupportX60:X2/sees:kotodama']
ACCEPT-D-60: FAIL
exit=1

```
