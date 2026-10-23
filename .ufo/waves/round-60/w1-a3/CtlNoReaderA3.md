NONE-MET

# CtlNoReaderA3 — no-reader SUPPORT mutation probe

## Scope and result

- Declared axis: **depth**. Probe axes: detector discrimination, isolated fixtures, exact-byte restoration.
- Frozen revision: `14e6413820d482913f723432b62d566967ccd1a6`; frozen counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.
- Eight assigned bad-evidence cases (a, b, c1–c4, d, e): **FAIL under both counters**. The six non-SUPPORT legs pass in every run.
- **Mutation verdict: killed under the SESSIONS-only probe.** Read and curl positive calibrations both pass the probe before mutation and after exact restoration. The frozen counter rejects the synthetic positive calibrations at PROVENANCE; frozen rejection alone is therefore **inconclusive**, not an independent mutation kill.
- No real support seat was dispatched, contacted, or used. Synthetic transcripts model the specified calls; no page request was executed by this harness. In (d), “fetches” means the counter recognises curl-call records for every page, not an assertion of actual network access. The synthetic positive fixtures are detector calibrations, not evidence that claim D is supported.
- Only the isolated scratch clone was changed. No integration, claim judgment, counter repair, lane-source edit, git/jj lane write, install/update, background job, or additional runtime/agent invocation.

## Inputs and construction

Read claims.json first. Cloned the lane with --no-hardlinks and checked out the frozen revision, with Git environment overrides removed. The harness `/fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/run-probes.py` applied the supplied L1 build.patch only in that clone, copied L1 captures, and ran the frozen build-packets.py. It borrowed only the frozen planted-row bytes from the prior attempt; no prior receipt was credited.

Candidate patch SHA-256: `e37abc6d6403a26ecaeb8aa6434dba3d3ffd02775a7e53ce9d1c8090a9ef2d61`. Candidate entry SHA-256: `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`. Candidate SOURCES SHA-256: `53b5a5f293cdf4199e7db1b8fc42d37bea4b4d830e1d9c375c50dcfad2028fca`. Frozen planted rows SHA-256: `1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682`. These identify the mechanical fixture only; no source-support verdict is implied.

Packet-builder stdout (exit=0):

```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
```

Capture input hashes:

```text
2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a  S648.bin
945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea  S649.bin
5e353d2f81f4c6ee4dca42362a36ec56981c6e4247dadc95a108f5e1bb432ef5  S650.bin
8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79  S651.bin
49d98b8360af88f13c989afcfe306c28e0f4dace2e26b64b19aad3507f2ed745  manifest.json
```

The positive fixtures keep each dispatched packet byte-for-byte in session_init.task, bind its entry_sha256, mirror committed synthetic transcripts into fake sessions, and bind report verdicts to the transcript’s last own-report write. All 24 seats reject their two planted labels; 47 real ids have three assignments each (141 total). Read-shaped and curl-shaped positive calibrations have 141/141 syntactically counted fetches. No key, quote, entry, capture, or registry change was made between mutants. Only evidence-presence/fetch-call shape changes; (d) changes the report and matching own-write verdicts to all SUPPORTED.

## Sole probe delta

Probe SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`. A direct equality assertion required the probe to equal the frozen counter with only this SESSIONS-string replacement; frozen counter bytes were never edited.

```diff
--- frozen-accept-d.py
+++ sessions-only-probe.py
@@ -191,7 +191,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
 def tool_calls(transcript):
```

## Case-specific stop points

All cited line numbers refer to the frozen accept-d.py (the probe keeps the same line numbering). PROVENANCE is checked at lines 289–297 and 557–560; the frozen counter prints session-files=0 in every complete-transcript fixture. Case (a) stops earlier at missing files.

### a-reports-only

SUPPORT, lines 547–549: packet/transcript absence prevents the seat from being considered. Both counters print `:missing` for all 24 seats.

Measured predicate facts: `{"counts":{"missing_seats":24},"confinement_reasons":{}}`.

### b-no-page-fetch

SUPPORT, lines 573–585 and 590–592: no fetch targets, so no real assignment has fetched=true. All 24 seats otherwise qualify; all 47 ids print good=0.

Measured predicate facts: `{"counts":{"blind_ok":24,"confined_ok":24,"bound_ok":24,"own_report_matches":24,"session_copies_match":24,"plant_rejects":48,"real_assignments":141,"fetched_real_assignments":0},"confinement_reasons":{}}`.

### c1-echo-only

SUPPORT, lines 327–351, 585 and 590: echo is not a fetch verb. All 24 seats qualify, but the recorded URLs count as zero page fetches.

Measured predicate facts: `{"counts":{"blind_ok":24,"confined_ok":24,"bound_ok":24,"own_report_matches":24,"session_copies_match":24,"plant_rejects":48,"real_assignments":141,"fetched_real_assignments":0},"confinement_reasons":{}}`.

### c2-cdx-only

SUPPORT, lines 252–256 and 557–559: read-url-not-in-packet for every seat. Independently, lines 355–361 exclude the nested query URL from names_page; zero real assignments count as fetched.

Measured predicate facts: `{"counts":{"blind_ok":24,"confined_ok":0,"bound_ok":24,"own_report_matches":24,"session_copies_match":24,"plant_rejects":48,"real_assignments":141,"fetched_real_assignments":0},"confinement_reasons":{"read-url-not-in-packet":24}}`.

### c3-search-only

SUPPORT, lines 252–256 and 557–559: read-url-not-in-packet for every seat. The URL occurs only after search?q=; lines 355–361 do not count it as fetching the row page.

Measured predicate facts: `{"counts":{"blind_ok":24,"confined_ok":0,"bound_ok":24,"own_report_matches":24,"session_copies_match":24,"plant_rejects":48,"real_assignments":141,"fetched_real_assignments":0},"confinement_reasons":{"read-url-not-in-packet":24}}`.

### c4-own-report-only

SUPPORT, lines 316–324 and 335–337: own_report_call is skipped before fetch_targets can collect URLs. All 24 seats qualify, but all 47 ids have good=0.

Measured predicate facts: `{"counts":{"blind_ok":24,"confined_ok":24,"bound_ok":24,"own_report_matches":24,"session_copies_match":24,"plant_rejects":48,"real_assignments":141,"fetched_real_assignments":0},"confinement_reasons":{}}`.

### d-curl-planted-blind

SUPPORT, lines 569–571: each planted label must have NOT-SUPPORTED and no SUPPORTED. All labels were stamped SUPPORTED; zero seats qualify despite 141/141 real assignments matching fetch calls.

Measured predicate facts: `{"counts":{"blind_ok":24,"confined_ok":24,"bound_ok":24,"own_report_matches":24,"session_copies_match":24,"plant_rejects":0,"real_assignments":141,"fetched_real_assignments":141},"confinement_reasons":{}}`.

### e-different-page-same-host

SUPPORT, lines 243–256 and 557–559: a different path on the same host is read-url-not-in-packet. Lines 355–361 and 585 also find zero matching page fetches.

Measured predicate facts: `{"counts":{"blind_ok":24,"confined_ok":0,"bound_ok":24,"own_report_matches":24,"session_copies_match":24,"plant_rejects":48,"real_assignments":141,"fetched_real_assignments":0},"confinement_reasons":{"read-url-not-in-packet":24}}`.

The (c) shapes are respectively `echo <listed URL>` with confined cwd; `read https://web.archive.org/cdx/search/cdx?url=https://<normalised listed page>`; `read https://www.google.com/search?q=https://<normalised listed page>`; and listing every URL only inside the exempt own-report write. Case (b) has only the report write. Case (e) preserves each URL’s scheme and host but replaces the entire path with `/__control_different_page__` and removes its query. Case (a) retains reports and their keyed verdicts but removes all packets and committed transcripts. Case (d) retains the exact confined curl-call shape of its passing curl calibration and changes only verdict labels.

## Required receipts

`counter-sha256` identifies the frozen invocation; `probe-counter-sha256` identifies the second invocation on the same fixture. `exit` is the frozen Python exit code; `probe-exit` is the probe Python exit code. The stopped-by field names the failing leg, with its local reason.

```text

RECEIPT CtlNoReaderA3/baseline-read counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT:PROVENANCE,probe:none(calibration) probe-exit=0 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/a-reports-only counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:missing,probe:SUPPORT:missing probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/b-no-page-fetch counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:PROVENANCE,probe:SUPPORT:FETCHED probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/c1-echo-only counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:PROVENANCE,probe:SUPPORT:FETCHED probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/c2-cdx-only counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:PROVENANCE,probe:SUPPORT:CONFINED+FETCHED probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/c3-search-only counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:PROVENANCE,probe:SUPPORT:CONFINED+FETCHED probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/c4-own-report-only counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:PROVENANCE,probe:SUPPORT:FETCHED probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/e-different-page-same-host counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:PROVENANCE,probe:SUPPORT:CONFINED+FETCHED probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/restored-read counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT:PROVENANCE,probe:none(calibration) probe-exit=0 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/baseline-curl counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT:PROVENANCE,probe:none(calibration) probe-exit=0 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/d-curl-planted-blind counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT:PROVENANCE,probe:SUPPORT:QUALIFIED probe-exit=1 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

RECEIPT CtlNoReaderA3/restored-curl counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT:PROVENANCE,probe:none(calibration) probe-exit=0 probe-counter-sha256=3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d

```

## Before, mutated, and restored hashes

Hash definition: SHA-256 of the sorted concatenation of each UTF-8 relative filename, a NUL byte, and the raw SHA-256 digest of that file’s bytes. The measured state includes entry, SOURCES, frozen counter, key-hash file, complete support tree, captures, and synthetic sessions. This is a byte-content fingerprint, not a Git commit.


Read pristine/restored fingerprint: `58bc72927908be85c8fd7469f100484b7dc11a14e3e270f6f65d69fd146d5143` = `58bc72927908be85c8fd7469f100484b7dc11a14e3e270f6f65d69fd146d5143`.

Curl pristine/restored fingerprint: `4fbfcb4693f03768865b72e6a86206ddede8ea4ec27b4d06aa7844d7eec39113` = `4fbfcb4693f03768865b72e6a86206ddede8ea4ec27b4d06aa7844d7eec39113`.

Each mutation was followed by exact restoration to the read baseline (all 12 equality assertions passed). The curl baseline was additionally reconstructed byte-for-byte and scored again after (d).

| Case | Mutated state SHA-256 |
|---|---|

| a-reports-only | `59354b59bc43a56bbc61f202ac6f86c698b25e692feb7cd8b7c712f12db2bade` |

| b-no-page-fetch | `f8871d7860df7d8f6ddd2dd1578cbd4babd67db15ce5d47ebf69769741acf3b0` |

| c1-echo-only | `3a0e929460eda290f72747825c645022c0e5ffa26c58450c45fb035c8ac0e7f4` |

| c2-cdx-only | `2e7c6c1bf2e7cd4ab4a332c87966ecb0f6b5448f3f391551239951ca1541b839` |

| c3-search-only | `008ed86a1c59fba15f59b3e33a0cc25d2c0aec7e30d2e827d859cadc3a49da47` |

| c4-own-report-only | `d06ce88f59aca5648ab84d7f5a6016dcdef6e0635f3154c2244214e794eb0a20` |

| e-different-page-same-host | `075c881d5ac1478dc3c45e729b4b56943338bf569e14f201e6ead7c0f4f7e62a` |

| d-curl-planted-blind | `8777bb3f6f95bde438242cb01c5050866f38e9c6d0ea07c1968d076adf3b18ea` |


Final cleanup restored the checkout’s original bytes, not merely the positive fixture: `original_restored_exact=true`. Original-before = original-after = `f47afd3765046f87dffb45efc78954b3e05da38576347b0ab403cd1002288ea2`. Support/captures/key-hash/fake-session files that were originally absent were removed.

| Original file | Before SHA-256 | After SHA-256 |
|---|---|---|

| clone/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md | `4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d` | `4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d` |

| clone/corpus/SOURCES.md | `35627babb0e3182f8d548cdd0ca71a461eceeadaaeff81511465b325555cc64b` | `35627babb0e3182f8d548cdd0ca71a461eceeadaaeff81511465b325555cc64b` |

| clone/reports/round-60/accept-d.py | `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` | `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` |


Raw stdout/stderr for every counter invocation, machine-readable results, the harness, original-byte snapshot and probe diff remain under `/fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/`. Randomised packets were temporary and restored away; the receipts and recorded fingerprints are the retained evidence, not a claim of exact packet-replay from a retained seed. Final measured sandbox size: 165 MiB (du -sm). All harness/counter subprocesses exited; none was backgrounded. Every Python invocation used PYTHONDONTWRITEBYTECODE=1 and python3 -B; outer harness deadline 580 s and each counter deadline 300 s. No tools installed. Completed: 2026-10-23T07:07:15.695270+00:00.

## Full counter stdout and exit codes

Every invocation used the clone as cwd. The shell echoes the Python status immediately after the bounded invocation; each stdout block below is copied in full from that invocation.

### baseline-read / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### baseline-read / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **0**.

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


Stderr: empty.

### a-reports-only / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### a-reports-only / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### b-no-page-fetch / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### b-no-page-fetch / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### c1-echo-only / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### c1-echo-only / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### c2-cdx-only / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### c2-cdx-only / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:read-url-not-in-packet', 'SupportB60:X2/sees:read-url-not-in-packet', 'SupportC60:X2/sees:read-url-not-in-packet', 'SupportD60:X2/sees:read-url-not-in-packet', 'SupportE60:X2/sees:read-url-not-in-packet', 'SupportF60:X2/sees:read-url-not-in-packet', 'SupportG60:X2/sees:read-url-not-in-packet', 'SupportH60:X2/sees:read-url-not-in-packet', 'SupportI60:X2/sees:read-url-not-in-packet', 'SupportJ60:X2/sees:read-url-not-in-packet', 'SupportK60:X2/sees:read-url-not-in-packet', 'SupportL60:X2/sees:read-url-not-in-packet', 'SupportM60:X2/sees:read-url-not-in-packet', 'SupportN60:X2/sees:read-url-not-in-packet', 'SupportO60:X2/sees:read-url-not-in-packet', 'SupportP60:X2/sees:read-url-not-in-packet', 'SupportQ60:X2/sees:read-url-not-in-packet', 'SupportR60:X2/sees:read-url-not-in-packet', 'SupportS60:X2/sees:read-url-not-in-packet', 'SupportT60:X2/sees:read-url-not-in-packet', 'SupportU60:X2/sees:read-url-not-in-packet', 'SupportV60:X2/sees:read-url-not-in-packet', 'SupportW60:X2/sees:read-url-not-in-packet', 'SupportX60:X2/sees:read-url-not-in-packet']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### c3-search-only / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### c3-search-only / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:read-url-not-in-packet', 'SupportB60:X2/sees:read-url-not-in-packet', 'SupportC60:X2/sees:read-url-not-in-packet', 'SupportD60:X2/sees:read-url-not-in-packet', 'SupportE60:X2/sees:read-url-not-in-packet', 'SupportF60:X2/sees:read-url-not-in-packet', 'SupportG60:X2/sees:read-url-not-in-packet', 'SupportH60:X2/sees:read-url-not-in-packet', 'SupportI60:X2/sees:read-url-not-in-packet', 'SupportJ60:X2/sees:read-url-not-in-packet', 'SupportK60:X2/sees:read-url-not-in-packet', 'SupportL60:X2/sees:read-url-not-in-packet', 'SupportM60:X2/sees:read-url-not-in-packet', 'SupportN60:X2/sees:read-url-not-in-packet', 'SupportO60:X2/sees:read-url-not-in-packet', 'SupportP60:X2/sees:read-url-not-in-packet', 'SupportQ60:X2/sees:read-url-not-in-packet', 'SupportR60:X2/sees:read-url-not-in-packet', 'SupportS60:X2/sees:read-url-not-in-packet', 'SupportT60:X2/sees:read-url-not-in-packet', 'SupportU60:X2/sees:read-url-not-in-packet', 'SupportV60:X2/sees:read-url-not-in-packet', 'SupportW60:X2/sees:read-url-not-in-packet', 'SupportX60:X2/sees:read-url-not-in-packet']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### c4-own-report-only / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### c4-own-report-only / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### e-different-page-same-host / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### e-different-page-same-host / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:read-url-not-in-packet', 'SupportB60:X2/sees:read-url-not-in-packet', 'SupportC60:X2/sees:read-url-not-in-packet', 'SupportD60:X2/sees:read-url-not-in-packet', 'SupportE60:X2/sees:read-url-not-in-packet', 'SupportF60:X2/sees:read-url-not-in-packet', 'SupportG60:X2/sees:read-url-not-in-packet', 'SupportH60:X2/sees:read-url-not-in-packet', 'SupportI60:X2/sees:read-url-not-in-packet', 'SupportJ60:X2/sees:read-url-not-in-packet', 'SupportK60:X2/sees:read-url-not-in-packet', 'SupportL60:X2/sees:read-url-not-in-packet', 'SupportM60:X2/sees:read-url-not-in-packet', 'SupportN60:X2/sees:read-url-not-in-packet', 'SupportO60:X2/sees:read-url-not-in-packet', 'SupportP60:X2/sees:read-url-not-in-packet', 'SupportQ60:X2/sees:read-url-not-in-packet', 'SupportR60:X2/sees:read-url-not-in-packet', 'SupportS60:X2/sees:read-url-not-in-packet', 'SupportT60:X2/sees:read-url-not-in-packet', 'SupportU60:X2/sees:read-url-not-in-packet', 'SupportV60:X2/sees:read-url-not-in-packet', 'SupportW60:X2/sees:read-url-not-in-packet', 'SupportX60:X2/sees:read-url-not-in-packet']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### restored-read / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### restored-read / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **0**.

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


Stderr: empty.

### baseline-curl / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### baseline-curl / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **0**.

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


Stderr: empty.

### d-curl-planted-blind / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### d-curl-planted-blind / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **1**.

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2', 'SupportB60:X2', 'SupportC60:X2', 'SupportD60:X2', 'SupportE60:X2', 'SupportF60:X2', 'SupportG60:X2', 'SupportH60:X2', 'SupportI60:X2', 'SupportJ60:X2', 'SupportK60:X2', 'SupportL60:X2', 'SupportM60:X2', 'SupportN60:X2', 'SupportO60:X2', 'SupportP60:X2', 'SupportQ60:X2', 'SupportR60:X2', 'SupportS60:X2', 'SupportT60:X2', 'SupportU60:X2', 'SupportV60:X2', 'SupportW60:X2', 'SupportX60:X2']
ACCEPT-D-60: FAIL
exit=1
```


Stderr: empty.

### restored-curl / frozen

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py; echo exit=$?`

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; Python exit: **1**.

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


Stderr: empty.

### restored-curl / probe

Command: `timeout 300 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNoReaderA3/probe-accept-d.py; echo exit=$?`

Counter SHA-256: `3c90dbb5a59c6a428df98c2c800a90b74899777c2b146836e96515b6b59b364d`; Python exit: **0**.

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


Stderr: empty.
