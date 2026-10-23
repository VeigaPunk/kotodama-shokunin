CONTROL-MET: e-right-url-pasted-bytes

# CtlEchoA3 — assigned echo / self-made-capture control

## Result and scope

Four URL substitutions were killed by ROWS and PINNED. The right-URL / wrong-page-bytes mutant survived both legs under the frozen counter and reached `ACCEPT-D-60: PASS` under the permitted SESSIONS-only probe. **No frozen whole-counter PASS occurred:** every frozen run of the complete fixture failed SUPPORT because its synthetic transcripts have no real session-file provenance. This is a PINNED authenticity coverage finding, not an actual supported claim or a data-seat verdict.

Axes: source-page identity (ROWS), capture authenticity (PINNED), reproducible detection, exact-byte restoration. One defect family, five assigned cases; no additional mutation probe. All work stayed in `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/`; the only lane write is this report. No reviewer runtime or real support seat was dispatched, contacted, or used.

## Instrument and fixture

- Revision: `14e6413820d482913f723432b62d566967ccd1a6`. Clone checked out this exact commit, then applied `/fast/scratch/hyaku/kotodama-r60a3/L1/build.patch` and copied its `captures/`.
- Frozen counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Unchanged throughout.
- Probe SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. The only change is the SESSIONS constant shown below.
- Target: S649, canonical Met object 464456. Its quote, teaches, entry sentence, and primary URL remain unchanged in every case; cases (a)–(d) replace only its secondary capture URL in the source cell plus matching manifest metadata/capture bytes. Case (e) changes only capture bytes and matching manifest fields; its URLs and every source/entry/packet/transcript byte remain unchanged.
- A complete synthetic control-shaped support fixture was built using the frozen `build-packets.py` and the frozen planted-rows file (SHA-256 `1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682`). Synthetic JSONL records list packet-page read calls and key-driven verdicts; **those calls are fixture data, not executed page reads or actual judgments.** Fake session files exist only under this sandbox. The probe checks all normal legs against these fixtures; it does not bypass any leg other than relocating provenance input.
- Baseline: ROWS and PINNED PASS under both detectors; full probe PASS/0. Full frozen FAIL/1 solely on SUPPORT (`session-files=0`), so its whole-counter baseline is inconclusive for mutation-kill attribution. The target legs have a positive baseline and identical restored results.
- All detector processes ran from the clone with `timeout 120`, `PYTHONDONTWRITEBYTECODE=1`, `python3 -B`, `UV_OFFLINE=1`, and TMPDIR inside this sandbox. The encompassing harness was capped at 55 seconds and completed in 18.75 seconds. No background jobs, network fetches, tool installs/updates, or lane git/jj writes. Final sandbox size observed: 165M, below 200 MB.

```diff
--- reports/round-60/accept-d.py
+++ accept-d-probe.py
@@ -191,7 +191,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
 def tool_calls(transcript):
```

Quote used verbatim:

> Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems

Original capture URL: `https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456`.

Donor bytes were read afresh from `/fast/scratch/hyaku/kotodama-r60a2/AuditRows01/s601_wb.html` (212855 bytes, SHA-256 `2955346a97afc8ced376770ee8cd27ed9841a218f7efa485ddc41567c84c8c9f`). That file identifies itself as **Wedjat eye amulet**, canonical object **566845** (HTML lines 15 and 20), not hematite object 464456. The unmodified donor does not locate the S649 quote under the lane locator. This is re-use of local page bytes, not a claim of a new live fetch. Case (e) appends exactly a `<p data-control="pasted-quote">…</p>` containing the quote to those different-page bytes and records the new hash/size. The lane locator then locates it.

## Five cases

| Case | Frozen ROWS / PINNED | Frozen ACCEPT / exit | Probe ACCEPT / exit | Target-leg verdict | Stopping leg detail |
|---|---|---|---|---|---|
| a-echo | FAIL / FAIL | FAIL / 1 | FAIL / 1 | KILLED | ROWS: extra-url-not-a-capture-of-the-page; PINNED: url-not-row-page-or-refused (denied-host) |
| b-codehost | FAIL / FAIL | FAIL / 1 | FAIL / 1 | KILLED | ROWS: extra-url-not-a-capture-of-the-page; PINNED: url-not-row-page-or-refused (denied-host) |
| c-wayback-other-page | FAIL / FAIL | FAIL / 1 | FAIL / 1 | KILLED | ROWS: extra-url-not-a-capture-of-the-page; PINNED: url-not-row-page-or-refused (different page) |
| d-wayback-quote-path | FAIL / FAIL | FAIL / 1 | FAIL / 1 | KILLED | ROWS: extra-url-not-a-capture-of-the-page; PINNED: url-not-row-page-or-refused (url-reflects-quote) |
| e-right-url-pasted-bytes | PASS / PASS | FAIL / 1 | PASS / 0 | SURVIVED | No ROWS/PINNED stop; frozen SUPPORT only (provenance) |

Expected detector: ROWS should reject a secondary URL not a Wayback capture of the canonical page; PINNED should reject an echo/code host, a different page, or a quote-smuggling URL. The assigned self-made-byte control challenges whether PINNED can distinguish source bytes from an arbitrary document with the quote pasted in. It cannot here: `accept-d.py:478-493` checks a self-declared hash, matching URL string/refusal rule, and quote location, without authenticating the fetched origin of the bytes. The surviving result does not authorize changing the declared contract; integration and any pre-data revision belong to L1.

### a-echo

- Substituted manifest/capture URL: `https://postman-echo.com/get?data=Hematite%20was%20believed%20to%20stop%20the%20flow%20of%20blood%20and%20was%20a%20favorite%20medium%20for%20amulets%20related%20to%20female%20reproductive%20health%20and%20menstrual%20problems`.
- Locator URL refusal: `denied-host`; quote located in fixture bytes: `true`.
- Capture SHA-256: before/restored `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` → mutated `fc6f120fe44881742afabd982941b94b6dfedfbd74781e9de72bdb063467f0c3` (218 bytes).
- Mutated 88-file fingerprint: `957d6380c88e61d150f5794a7a60b7cb8a4ee185301e87ed964978071ed60dd6`.

`RECEIPT CtlEchoA3/a-echo counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:ROWS,PINNED,SUPPORT;probe:ROWS,PINNED probe-counter-sha256=8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad probe-exit=1`

### b-codehost

- Substituted manifest/capture URL: `https://raw.githubusercontent.com/example/fixture/main/amulet.txt`.
- Locator URL refusal: `denied-host`; quote located in fixture bytes: `true`.
- Capture SHA-256: before/restored `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` → mutated `68f4b5d56a64ee23b66657a3c492cea116116278bc1b5c341e354dab401a15c5` (147 bytes).
- Mutated 88-file fingerprint: `99f46ae63d2a44c09124332e414aca83d7571cc7ccb76c5972e3eebedf07d9d1`.

`RECEIPT CtlEchoA3/b-codehost counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:ROWS,PINNED,SUPPORT;probe:ROWS,PINNED probe-counter-sha256=8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad probe-exit=1`

### c-wayback-other-page

- Substituted manifest/capture URL: `https://web.archive.org/web/20250125005512id_/https://www.metmuseum.org/art/collection/search/566845`.
- Locator URL refusal: `(none)`; quote located in fixture bytes: `false`.
- Capture SHA-256: before/restored `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` → mutated `2955346a97afc8ced376770ee8cd27ed9841a218f7efa485ddc41567c84c8c9f` (212855 bytes).
- Mutated 88-file fingerprint: `81e230d67c6a47f525566aaf2b1d13fab1b29b2ff7d09ef193efb81c31927856`.

`RECEIPT CtlEchoA3/c-wayback-other-page counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:ROWS,PINNED,SUPPORT;probe:ROWS,PINNED probe-counter-sha256=8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad probe-exit=1`

### d-wayback-quote-path

- Substituted manifest/capture URL: `https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456/Hematite%20was%20believed%20to%20stop%20the%20flow%20of%20blood%20and%20was%20a%20favorite%20medium%20for%20amulets%20related%20to%20female%20reproductive%20health%20and%20menstrual%20problems`.
- Locator URL refusal: `url-reflects-quote`; quote located in fixture bytes: `true`.
- Capture SHA-256: before/restored `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` → mutated `86f6edcf5ddab0550595746520799e3ffd42ad6bc1d3e5ee52c0b7c7a6d15e6d` (179 bytes).
- Mutated 88-file fingerprint: `eb0026760aa85973099690ce7ba0b2bb41efd529f26be76846cc511822994b96`.

`RECEIPT CtlEchoA3/d-wayback-quote-path counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:ROWS,PINNED,SUPPORT;probe:ROWS,PINNED probe-counter-sha256=8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad probe-exit=1`

### e-right-url-pasted-bytes

- Substituted manifest/capture URL: `https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456`.
- Locator URL refusal: `(none)`; quote located in fixture bytes: `true`.
- Capture SHA-256: before/restored `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` → mutated `9e2dfd7f95d1a7aae29ae9bac925ec0278c74f7d946feb08efad58e98fdd646d` (213038 bytes).
- Mutated 88-file fingerprint: `60505beac691798ed2f99f49eae74775671cc9ed22a2aef4dc456076fe3cdc2e`.

`RECEIPT CtlEchoA3/e-right-url-pasted-bytes counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-counter-sha256=8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad probe-exit=0`

## Exact-byte restoration

All five transactions restore in `finally`, then rerun **both same detectors** on restored bytes. Every restored stdout (including exit status) exactly equals its corresponding pristine stdout. The 88-file manifest is a SHA-256 of the sorted JSON map of relative paths to individual SHA-256 values; before and after fingerprints are `ee65636efb7b04c8c43dc22c712dd347e6fefa89d909cae445429bc611726a7d` and `ee65636efb7b04c8c43dc22c712dd347e6fefa89d909cae445429bc611726a7d`. Every recorded file is byte-identical, and all sandbox fake-session files were restored exactly. This baseline is the applied candidate plus its explicitly synthetic control fixture, not a claim that the clone equals the unbuilt frozen tree.

| Fixed input | Before = final restored SHA-256 |
|---|---|
| `corpus/SOURCES.md` | `53b5a5f293cdf4199e7db1b8fc42d37bea4b4d830e1d9c375c50dcfad2028fca` |
| `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` | `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0` |
| `reports/round-60/accept-d.py` | `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc` |
| `reports/round-60/captures/S648.bin` | `2dafb2a2aee493c42143314f6d8431e197d5e655d83e76bc98493c44b0b32d1a` |
| `reports/round-60/captures/S649.bin` | `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` |
| `reports/round-60/captures/S650.bin` | `5e353d2f81f4c6ee4dca42362a36ec56981c6e4247dadc95a108f5e1bb432ef5` |
| `reports/round-60/captures/S651.bin` | `8e4cf0198005310cc619f48830658bcd1fe2ddda8bdba64d5c86e98128f67c79` |
| `reports/round-60/captures/manifest.json` | `49d98b8360af88f13c989afcfe306c28e0f4dace2e26b64b19aad3507f2ed745` |

For the survivor, the only differing files at mutation were:

- `reports/round-60/captures/S649.bin`: `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea` → `9e2dfd7f95d1a7aae29ae9bac925ec0278c74f7d946feb08efad58e98fdd646d` → `945d52a2933d3d8737e322e1eb0ebe3d63e7cfe178918d49aa3f24bfac7ca8ea`.
- `reports/round-60/captures/manifest.json`: `49d98b8360af88f13c989afcfe306c28e0f4dace2e26b64b19aad3507f2ed745` → `10146261756e15b4f63c37b2a7683e4eab49715522e2a9e799dc0a1c34aff276` → `49d98b8360af88f13c989afcfe306c28e0f4dace2e26b64b19aad3507f2ed745`.

Evidence retained in the sandbox: `run-controls.py`, `results.json` (all stdout/stderr/status, per-case changed-file hashes, restorations), `before-hashes.json`, `after-hashes.json`, `probe.diff`, and `outputs/`. No fix, integration, or claim judgment was performed.

## Full detector stdout and actual exit codes

No stdout is abbreviated below. All stderr streams for the 22 harness detector runs were empty. Each `exit=` value is the observed subprocess return code, recorded by the harness (the initial direct tool run reported exit 1).

### Initial candidate, before synthetic support fixture — frozen

Command, cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`:

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

### pristine / baseline / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
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

### pristine / baseline / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
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

### a-echo / mutated / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### a-echo / mutated / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### a-echo / restored / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
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

### a-echo / restored / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
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

### b-codehost / mutated / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### b-codehost / mutated / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### b-codehost / restored / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
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

### b-codehost / restored / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
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

### c-wayback-other-page / mutated / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### c-wayback-other-page / mutated / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### c-wayback-other-page / restored / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
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

### c-wayback-other-page / restored / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
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

### d-wayback-quote-path / mutated / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
exit=1
```

### d-wayback-quote-path / mutated / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
```

```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS FAIL bad=['S649:extra-url-not-a-capture-of-the-page']
PINNED FAIL bad=['S649:url-not-row-page-or-refused']
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
```

### d-wayback-quote-path / restored / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
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

### d-wayback-quote-path / restored / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
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

### e-right-url-pasted-bytes / mutated / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
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

### e-right-url-pasted-bytes / mutated / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
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

### e-right-url-pasted-bytes / restored / frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B reports/round-60/accept-d.py; echo exit=$?
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

### e-right-url-pasted-bytes / restored / probe

Counter SHA-256: `8d71be99283383772e3065cf9a5ba83a01223ed76aa223e57a9f0f630f5dd2ad`. Cwd: `/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/clone`.

```sh
timeout 120 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlEchoA3/accept-d-probe.py; echo exit=$?
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

