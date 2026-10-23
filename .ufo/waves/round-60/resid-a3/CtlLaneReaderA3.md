NONE-MET

# Residual pre-data lane-reader control — CtlLaneReaderA3

## Counterexample and observed outcome

The attempted shortcut is a reviewer that treats the lane registry and landed entry as the answer source, rejects packet propositions absent from that lane, copies page-only EVIDENCE from the committed pinned texts, and records a curl for every packet page without using the fetched page to decide support. Six ordinary local-read transcript forms were scored. **None passed frozen or probe.** In every negative probe all 24 synthetic seats were unqualified with `sees:kotodama`; every cited id had `good=0`. All other counter legs passed.

This is a local synthetic transcript regression test, not a support review, real session, source-quality judgment, admission, or canonical Rust verdict. No support seat or other runtime was invoked. The fixture curl/read/open calls are transcript data, not claimed live executions. Only fixture construction, the frozen counter, its SESSIONS-only probe, and their diagnostic functions were executed. No real support packet or support key was read.

## Axes and scope

- **Depth / evidence validity:** whether page-only quotation can be obtained from lane captures instead of independent page reading.
- **Calibration / discernment:** distinguish an invalid lane-derived answer source from an honest-shaped page-reader positive.
- **Operability:** ordinary absolute/relative read, bash cwd/default-cwd, and Python open forms must receive usable stopping reasons.
- **Provenance and reproducibility (review dimensions, not new claim axes):** exact target revision, unchanged frozen counter, isolated synthetic session copies, full stdout.

The exercised routes show no fixable acceptance defect and no observed no-harm tradeoff to submit. This finite control is not saturation or evidence about untested routes. Claim D and the learning trends remain for the canonical judge; this report makes no admission decision.

## Target and method

- Lane commit: `1cd9db7cdc83fd41f5d04cd620af879555442f19`.
- Frozen counter SHA-256: `45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59`.
- Probe SHA-256: `d57ee650572e26094f6e4333c49a3ef911eef1ab7ea7a3dc0dd17e2381a6002c`.
- Entry SHA-256: `36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2`.

- Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3`.
- Reproducer: `/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/run-controls.py`.

- Revision notes 6 and 7 were read first. The clone was checked out at the assigned commit; no lane data patch was necessary. The 16 frozen planted rows were copied into the sandbox and hash-checked. New dry-run packets and a new fixture-only key were generated locally with the committed build-packets.py; no sibling or real support packets/keys were used.

- The lane-only decision is membership of the locator-normalized `(quote, teaches, entry)` triple reconstructed from `corpus/SOURCES.md` and the entry. Fixture-key labels are checked only after that decision, not used to decide it. This classified 141 real occurrences SUPPORTED and 48 planted occurrences NOT-SUPPORTED.

- The 141 SUPPORTED lines each quote a pinned-page span absent from its packet block, with at least 16 normalized words (requirement: 10). All 47 pinned page texts were manifest-hash checked by the counter loader. Exact spans and checks are in `evidence-spans.json`.

- Every case records 297 curl calls across its 24 transcripts: one for each distinct URL in each seat packet, including planted-block URLs and URL aliases. Each uses `cwd=/tmp/<Seat>/` and writes `/tmp/<Seat>/page-N.bin`. Every row URL is recognized by the frozen fetch-target predicate. These are synthetic calls, not a live-fetch receipt.

- Each negative adds the same ordinary path form for SOURCES.md, the entry, and that seat's required pinned page texts; packets, key, reports, evidence, and curl calls stay fixed. Relative forms have fleet-root session cwd `/home/vgpnk/Projects/shokunin`. The extra eval form covers Python open through the eval tool as well as bash.

- Each committed synthetic transcript is byte-identical to its sandbox fake session. All BOUND diagnostics pass. Frozen runs correctly find no real support session (`session-files=0` for all 24); the probe removes only that missing-real-session obstacle.

## Per-form stopping reasons

`SUPPORT` evaluates provenance, then BLIND, then CONFINED, so the scored negative probe reason is BLIND; CONFINED below was independently exercised with the same frozen function and complete calls.

| Case | Frozen / probe exit | Scored probe stop | Independently exercised CONFINED |
|---|---|---|---|

| honest-shaped-positive | 1 / 0 | none — all 24 qualified | PASS |

| read-absolute | 1 / 1 | SUPPORT / BLIND: kotodama | read-outside-sandbox |

| read-fleet-relative | 1 / 1 | SUPPORT / BLIND: kotodama | read-outside-sandbox |

| bash-cat-cwd | 1 / 1 | SUPPORT / BLIND: kotodama | bash-cwd-outside-sandbox |

| bash-cat-no-cwd | 1 / 1 | SUPPORT / BLIND: kotodama | bash-cwd-outside-sandbox |

| python-open-cwd | 1 / 1 | SUPPORT / BLIND: kotodama | bash-cwd-outside-sandbox |

| python-open-eval-relative | 1 / 1 | SUPPORT / BLIND: kotodama | tool:eval |


**Honest-shaped positive: probe PASS, exit 0**, all 24 seats qualified, all 47 ids supported. Its frozen run fails SUPPORT only on absent real sessions, as expected. This positive is calibration data, not proof a real reader ran.

### Exact representative first calls

Each case also carries corresponding entry and pinned-page paths. The full per-seat call lists are under `fixtures/<case>/KotodamaR60A3.<Seat>.jsonl`.

```json

{"case": "read-absolute", "first_lane_call": ["read", {"path": "/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md"}]}

{"case": "read-fleet-relative", "first_lane_call": ["read", {"path": "kotodama-shokunin/corpus/SOURCES.md"}]}

{"case": "bash-cat-cwd", "first_lane_call": ["bash", {"command": "timeout 30 cat kotodama-shokunin/corpus/SOURCES.md", "timeout": 35, "cwd": "/home/vgpnk/Projects/shokunin"}]}

{"case": "bash-cat-no-cwd", "first_lane_call": ["bash", {"command": "timeout 30 cat kotodama-shokunin/corpus/SOURCES.md", "timeout": 35}]}

{"case": "python-open-cwd", "first_lane_call": ["bash", {"command": "timeout 30 python3 -B -c 'print(open('\"'\"'kotodama-shokunin/corpus/SOURCES.md'\"'\"', encoding=\"utf-8\").read())'", "cwd": "/home/vgpnk/Projects/shokunin", "timeout": 35}]}

{"case": "python-open-eval-relative", "first_lane_call": ["eval", {"language": "py", "code": "print(open('kotodama-shokunin/corpus/SOURCES.md', encoding=\"utf-8\").read())", "timeout": 30}]}

```

## Receipts

`exit` is the frozen exit; probe exits are in the table and full stdout. The positive's stopped-by field names the frozen-only stop.

```text

RECEIPT CtlLaneReaderA3/honest-shaped-positive counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=PASS stopped-by=SUPPORT/PROVENANCE(frozen-only:session-files=0)

RECEIPT CtlLaneReaderA3/read-absolute counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/read-fleet-relative counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/bash-cat-cwd counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/bash-cat-no-cwd counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/python-open-cwd counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

RECEIPT CtlLaneReaderA3/python-open-eval-relative counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT/BLIND(probe:kotodama);SUPPORT/PROVENANCE(frozen:session-files=0)

```

## Smallest safe correction

**No counter change is warranted by these controls.** Preserve BLIND and CONFINED: page-only EVIDENCE is not sufficient by itself when lane captures are accessible. Keep these forms as regression fixtures and do not convert a lane-derived verdict into a qualified support vote. No relaxation, alternate authority, identity change, or evidence rewrite is proposed. The conclusion is limited to the exercised ordinary paths.

## Reproduction and boundaries

Construction and all 14 counter executions were run using:

```sh
timeout 600 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/run-controls.py
```

The builder runs each counter from its own clone cwd with `timeout 600 python3 -B ...`, preserves full stdout and stderr, and prints the exit. `PYTHONDONTWRITEBYTECODE=1` is inherited; TMPDIR, UV_CACHE_DIR and XDG_CACHE_HOME point into this sandbox. No background jobs or delegation were used. Sandbox generated-file writes are capped at 8,000,000 bytes and the total checked cap is 200,000,000 bytes; observed regular-file total after all cases: 160,329,058 bytes. No git/jj writes were performed outside the own clone.

**Installs/updates:** none. An existing offline pypdf parser cache was copied into the own sandbox; no package install or update was performed.

### SESSIONS-only probe diff

```diff

--- reports/round-60/accept-d.py
+++ accept-d-probe.py
@@ -235,7 +235,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = '/fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/fake-sessions/KotodamaR60A3.{seat}.jsonl'
 
 
 def tool_calls(transcript):

```

## Full counter stdout (unabridged)

All stderr files are empty. Complete output files and commands are also preserved under `outputs/<case>.<frozen|probe>.*`; the structured record is `results.json`. No stdout lines are omitted or truncated below.

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
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/accept-d-probe.py; echo exit=$?
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
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/accept-d-probe.py; echo exit=$?
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
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/accept-d-probe.py; echo exit=$?
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
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/accept-d-probe.py; echo exit=$?
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
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/accept-d-probe.py; echo exit=$?
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
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/accept-d-probe.py; echo exit=$?
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
PYTHONDONTWRITEBYTECODE=1 timeout 600 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlLaneReaderA3/accept-d-probe.py; echo exit=$?
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
