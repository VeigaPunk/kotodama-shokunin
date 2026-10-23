CONTROL-MET: e-drop-dissenting-member; f-add-25th-member; f2-add-25th-dissenter

# CtlNarrowA3 — post-verdict narrowing controls

Review completed 2026-10-23T07:08:35Z. This is a scoped pre-data critic receipt, not a claim judgment or admission.

## Axes and authority

- Judged axis: **depth**. Diagnostic axes: immutable judged identity, verdict preservation, fixed seat universe, and reproducible provenance.
- Declaration read first: `reports/round-60/claims.json`, especially predicate and kill_rule. Frozen instrument revision: `14e6413820d482913f723432b62d566967ccd1a6`.
- Frozen counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`; observed matches the assigned digest.
- SESSIONS-only probe SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.
- Fixture entry SHA-256: `0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0`; constructed from L1/candidate-entry.md, the four rows in L1/build.patch, L1/captures, the revision-5 locator/base files, and the frozen planted rows.
- The frozen packet builder produced `cited=47 planted_rows=16 seats=24 planted_per_seat_min=2`. All real blocks have three original seat assignments.
- All transcripts/session copies and verdicts in these controls are **synthetic**. No real support seat was invoked, contacted, or impersonated; the simulated page-read calls are not evidence that a human/model checked those pages. The positive probe is an honest-shaped mechanical fixture only.
- Every frozen run fails SUPPORT through original-session PROVENANCE (`session-files=0`); no frozen PASS was observed. The allowed probe is what exercises the later legs. The failures and passes below must not be reported as real review provenance.

## Counterexample and evidence

**Critical fixable defect: a post-verdict registry edit erases dissent.** The positive fixture passes the probe. Introducing one original `NOT-SUPPORTED` on real S648 makes it fail SUPPORT. Removing only that dissenting member from registry.json restores `ACCEPT-D-60: PASS` (exit 0), although its unchanged original report, dispatched packet, transcript, and key mapping remain present. All 47 propositions remain; three-way coverage leaves two approving reviewers for each affected id. No entry, row, key, capture, packet, report, or transcript was edited in this mutation.

Only e-case changed file: `.ufo/waves/round-60/support/registry.json`, SHA-256 `e58f99c2b64bf0c41f282784053580de03fdefb93d630f65e495b873a209897f` → `5fbcd8c00059a7f4a4d04df5fd69c068550d8a41922b3f9bd0b8a429b4943871`. The dissent remains `VERDICT P04 NOT-SUPPORTED` in both original report and session write for the fixture target recorded in results.json. The transcript hash remains `06d96b98d76de8d87cbb3f2895932d1c16fa7faa2602bcc7b03ba6e09075c742` from the dissent seed.

**Second manifestation: a 25th registry member is silently ignored.** Appending only an additional reviewer to the original passing registry also reaches probe PASS. A stronger companion adds that member’s complete key mapping, packet, synthetic original session and report rejecting S648; it still passes. This is not merely an unqualified seat: the member is omitted before verdict scanning.

Local cause at frozen `reports/round-60/accept-d.py:514-519`: registry members are filtered into a set only if their name, role and agentId match SEATS. There is no assertion that the raw registry is exactly the frozen 24-member universe. At lines 541-542 only this filtered set is scanned, so a removed dissenter is never added to `rejected` at lines 574-579. The SUPPORT predicate at 593-594 checks remaining support counts and rejections, not roster integrity. The mutable registry has become a second authority for who was declared, instead of checking the frozen SEATS authority.

## Smallest safe correction

Before any data dispatch, L1 should revise the counter so SUPPORT fails unless the raw registry has exactly one member for every frozen SEATS name, each with the required reviewer role and exact AGENT_PREFIX identity; reject missing, duplicate, extra, or malformed members rather than filtering them away. Keep SEATS as the sole authority and scan that frozen universe for dissent, even when a member cannot qualify. Do not discard a dissent merely because the member was removed or invalidated after verdicts. This preserves two-of-three positive redundancy without allowing post-verdict selection.

This is a repairable control defect, not an acceptable depth-versus-operability tradeoff. Reinterpreting “declared” as only the surviving registry members would weaken the frozen kill rule; the canonical judge must not be asked to admit that trade. No counter fix, integration, claim judgment, or canonical judge invocation was performed by this seat.

## Requested six controls

| Control | Probe result | Failing leg / mechanism |
|---|---|---|
| (a) Delete rejected S648 line and row | FAIL, exit 1 | SET, LINES, ROWS, PINNED, JUDGED, SUPPORT; original dissent survives |
| (b) Reword rejected line | FAIL, exit 1 | JUDGED and SUPPORT |
| (c) Rebuild key/packets for edited entry | FAIL, exit 1 | SUPPORT; packet re-dispatch binding, also confinement after random reassignment |
| (c2) Stable-map re-key, no changed URLs/labels | FAIL, exit 1 | SUPPORT; all 24 report `packet-not-in-dispatched-task` (isolated BOUND guard) |
| (d) Rewrite landed NOT to SUPPORTED | FAIL, exit 1 | SUPPORT; `report-not-its-own-write`, original S648 NOT still counted |
| (e) Drop dissenting registry member | **PASS, exit 0** | **No leg fails: control met** |
| (f) Add 25th registry member | **PASS, exit 0** | **No leg fails: control met** |
| (f2) Add complete 25th member rejecting S648 | **PASS, exit 0** | **No leg fails: control met** |

(a)–(e) each start from the same original dissent seed after the original packet dispatch/verdict write. (f) starts from the original 24-seat passing verdicts to isolate unexpected-member rejection; (f2) supplies dissent in the additional member itself. Restoring an original dissent before (f) would trivially FAIL for that unrelated dissent and would not test the 25th-member guard.

## Probe diff

```diff
--- frozen/accept-d.py
+++ probe/accept-d.py
@@ -191,7 +191,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
 def tool_calls(transcript):
```

No counter constant or code other than SESSIONS changed. Both runs use the frozen clone as cwd and --root pointing at the same bounded fixture tree. The installed extractor adapter adds only an offline deadline and Python -B to the frozen locator’s exact uv/pypdf invocation; it does not alter the locator, PDF bytes, or extraction script.

## Receipts

`exit=` is the frozen process exit; `probe-exit=` is the probe process exit. Full stdout and the captured subprocess return code for every run follow below. PROVENANCE is a SUPPORT qualification subcheck, not a separately printed leg.

```text
RECEIPT CtlNarrowA3/honest-shaped counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:none probe-exit=0
RECEIPT CtlNarrowA3/dissent-seed counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:SUPPORT probe-exit=1
RECEIPT CtlNarrowA3/a-delete-line-and-row counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT;probe:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT probe-exit=1
RECEIPT CtlNarrowA3/b-reword-line counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:JUDGED,SUPPORT;probe:JUDGED,SUPPORT probe-exit=1
RECEIPT CtlNarrowA3/c-rekey-edited-entry counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:SUPPORT probe-exit=1
RECEIPT CtlNarrowA3/d-rewrite-landed-report counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:SUPPORT probe-exit=1
RECEIPT CtlNarrowA3/e-drop-dissenting-member counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:none probe-exit=0
RECEIPT CtlNarrowA3/f-add-25th-member counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:none probe-exit=0
RECEIPT CtlNarrowA3/f2-add-25th-dissenter counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:none probe-exit=0
RECEIPT CtlNarrowA3/c2-stable-rekey counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT[PROVENANCE:session-files=0];probe:SUPPORT probe-exit=1
```

## Every run — unabridged stdout and exit

### honest-shaped

Synthetic positive control: all 47 real blocks supported; all frozen planted blocks rejected; 24 seats, 3 per real block.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
```
Captured exit: `0`.

Stderr: empty.

### dissent-seed

Original dispatched packet and verdicts now include one real NOT-SUPPORTED; report and synthetic original session agree.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportE60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportE60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

### a-delete-line-and-row

After S648 dissent, remove its entire citing entry line and Registry row; leave the original key, packet, report and transcript in place.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET FAIL cited=46 want=47 missing=['S648'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None']
PINNED FAIL bad=['S648:no-row-or-manifest']
JUDGED FAIL entry_sha256 key=0073da7ed7e0 landed=1781cdbede35
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET FAIL cited=46 want=47 missing=['S648'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None']
PINNED FAIL bad=['S648:no-row-or-manifest']
JUDGED FAIL entry_sha256 key=0073da7ed7e0 landed=1781cdbede35
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

### b-reword-line

After S648 dissent, insert explicitly into its entry line; do not rebuild its judged key or dispatched packets.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=0073da7ed7e0 landed=e893ab99ed8e
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=0073da7ed7e0 landed=e893ab99ed8e
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

### c-rekey-edited-entry

After S648 dissent and the same entry edit as b, rerun the frozen official packet builder and refresh planted-key.sha256; preserve every already-dispatched transcript and verdict report.

Packet rebuild stdout:
```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
exit=0
```

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S649:NOT/SupportA60', 'S605:NOT/SupportA60', 'S600:NOT/SupportB60', 'S636:NOT/SupportB60', 'S621:NOT/SupportC60', 'S612:NOT/SupportC60', 'S607:NOT/SupportD60', 'S650:NOT/SupportD60', 'S646:NOT/SupportE60', 'S637:NOT/SupportE60', 'S635:NOT/SupportF60', 'S622:NOT/SupportG60', 'S642:NOT/SupportH60', 'S608:NOT/SupportH60', 'S631:NOT/SupportI60', 'S622:NOT/SupportI60', 'S621:NOT/SupportJ60', 'S612:NOT/SupportJ60', 'S629:NOT/SupportK60', 'S601:NOT/SupportK60', 'S625:NOT/SupportL60', 'S607:NOT/SupportL60', 'S605:NOT/SupportN60', 'S627:NOT/SupportO60', 'S644:NOT/SupportO60', 'S604:NOT/SupportP60', 'S611:NOT/SupportQ60', 'S610:NOT/SupportR60', 'S600:NOT/SupportR60', 'S612:NOT/SupportS60', 'S630:NOT/SupportS60', 'S634:NOT/SupportT60', 'S614:NOT/SupportU60', 'S641:NOT/SupportW60', 'S633:NOT/SupportW60', 'S644:NOT/SupportX60', 'S618:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S649:NOT/SupportA60', 'S605:NOT/SupportA60', 'S600:NOT/SupportB60', 'S636:NOT/SupportB60', 'S621:NOT/SupportC60', 'S612:NOT/SupportC60', 'S607:NOT/SupportD60', 'S650:NOT/SupportD60', 'S646:NOT/SupportE60', 'S637:NOT/SupportE60', 'S635:NOT/SupportF60', 'S622:NOT/SupportG60', 'S642:NOT/SupportH60', 'S608:NOT/SupportH60', 'S631:NOT/SupportI60', 'S622:NOT/SupportI60', 'S621:NOT/SupportJ60', 'S612:NOT/SupportJ60', 'S629:NOT/SupportK60', 'S601:NOT/SupportK60', 'S625:NOT/SupportL60', 'S607:NOT/SupportL60', 'S605:NOT/SupportN60', 'S627:NOT/SupportO60', 'S644:NOT/SupportO60', 'S604:NOT/SupportP60', 'S611:NOT/SupportQ60', 'S610:NOT/SupportR60', 'S600:NOT/SupportR60', 'S612:NOT/SupportS60', 'S630:NOT/SupportS60', 'S634:NOT/SupportT60', 'S614:NOT/SupportU60', 'S641:NOT/SupportW60', 'S633:NOT/SupportW60', 'S644:NOT/SupportX60', 'S618:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:read-url-not-in-packet', 'SupportB60:X2/sees:read-url-not-in-packet', 'SupportC60:X2/sees:read-url-not-in-packet', 'SupportD60:X2/sees:read-url-not-in-packet', 'SupportE60:X2/sees:read-url-not-in-packet', 'SupportF60:X2/sees:read-url-not-in-packet', 'SupportG60:X2/sees:read-url-not-in-packet', 'SupportH60:X2/sees:read-url-not-in-packet', 'SupportI60:X2/sees:read-url-not-in-packet', 'SupportJ60:X2/sees:read-url-not-in-packet', 'SupportK60:X2/sees:packet-not-in-dispatched-task', 'SupportL60:X2/sees:read-url-not-in-packet', 'SupportM60:X2/sees:read-url-not-in-packet', 'SupportN60:X2/sees:read-url-not-in-packet', 'SupportO60:X2/sees:read-url-not-in-packet', 'SupportP60:X2/sees:read-url-not-in-packet', 'SupportQ60:X2/sees:read-url-not-in-packet', 'SupportR60:X2/sees:read-url-not-in-packet', 'SupportS60:X2/sees:packet-not-in-dispatched-task', 'SupportT60:X2/sees:read-url-not-in-packet', 'SupportU60:X2/sees:read-url-not-in-packet', 'SupportV60:X2/sees:packet-not-in-dispatched-task', 'SupportW60:X2/sees:read-url-not-in-packet', 'SupportX60:X2/sees:read-url-not-in-packet']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

### d-rewrite-landed-report

After S648 dissent, rewrite only the landed report to SUPPORTED; the original session write remains NOT-SUPPORTED.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportE60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportE60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:X2/sees:report-not-its-own-write', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

### e-drop-dissenting-member

After S648 dissent, delete only the dissenting registry member; keep the original dissent report, packet, transcript and packet-key mapping byte-identical. Three-way block coverage leaves two approving seats.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
```
Captured exit: `0`.

Stderr: empty.

### f-add-25th-member

After the passing original 24 verdict reports, append one 25th reviewer to registry.json only; this isolates the declared 24-member cardinality rule.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
```
Captured exit: `0`.

Stderr: empty.

### f2-add-25th-dissenter

Append a fully shaped 25th reviewer, its key mapping, packet, report and synthetic original session; that new member rejects real S648. Refresh only the key digest. Original 24 members and verdicts are untouched.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT PASS unsupported=[] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: PASS
```
Captured exit: `0`.

Stderr: empty.

### c2-stable-rekey

After the same original S648 dissent, edit its entry wording, recompute key entry_sha256 and its digest, and rebuild each packet hash line and affected entry field WITHOUT shuffling labels or URLs. Original session task and report verdicts are unchanged. This isolates BOUND from random packet reassignment and CONFINE.

#### frozen

Counter SHA-256: `b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B reports/round-60/accept-d.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportE60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

#### probe

Counter SHA-256: `7e16fa7fb72067a691d649674c2792f5c9785ef2943b6923e23243c11423b1fb`.

Command (cwd `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/clone`):
```sh
timeout 120 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/accept-d-probe.py --root /fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/fixture
```

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportE60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:packet-not-in-dispatched-task', 'SupportB60:X2/sees:packet-not-in-dispatched-task', 'SupportC60:X2/sees:packet-not-in-dispatched-task', 'SupportD60:X2/sees:packet-not-in-dispatched-task', 'SupportE60:X2/sees:packet-not-in-dispatched-task', 'SupportF60:X2/sees:packet-not-in-dispatched-task', 'SupportG60:X2/sees:packet-not-in-dispatched-task', 'SupportH60:X2/sees:packet-not-in-dispatched-task', 'SupportI60:X2/sees:packet-not-in-dispatched-task', 'SupportJ60:X2/sees:packet-not-in-dispatched-task', 'SupportK60:X2/sees:packet-not-in-dispatched-task', 'SupportL60:X2/sees:packet-not-in-dispatched-task', 'SupportM60:X2/sees:packet-not-in-dispatched-task', 'SupportN60:X2/sees:packet-not-in-dispatched-task', 'SupportO60:X2/sees:packet-not-in-dispatched-task', 'SupportP60:X2/sees:packet-not-in-dispatched-task', 'SupportQ60:X2/sees:packet-not-in-dispatched-task', 'SupportR60:X2/sees:packet-not-in-dispatched-task', 'SupportS60:X2/sees:packet-not-in-dispatched-task', 'SupportT60:X2/sees:packet-not-in-dispatched-task', 'SupportU60:X2/sees:packet-not-in-dispatched-task', 'SupportV60:X2/sees:packet-not-in-dispatched-task', 'SupportW60:X2/sees:packet-not-in-dispatched-task', 'SupportX60:X2/sees:packet-not-in-dispatched-task']
ACCEPT-D-60: FAIL
```
Captured exit: `1`.

Stderr: empty.

## Isolation, tooling and reproducibility

- All 20 counter invocations are reproduced above: 10 cases × frozen/probe. No additional counter run was omitted.
- Artifacts and runnable fixture builders: `/fast/scratch/hyaku/kotodama-r60a3/CtlNarrowA3/prepare-fixture.py`, `run-cases.py`, `rekey-stable.py`, `results.json`, `probe.diff`, `outputs/`. results.json records per-case changed-file hashes and exact raw process output. The fixture was restored exactly to its original positive-control bytes after both transactions, as recorded by `restored_exactly=true` and `restored_exactly_after_c2=true`; no extra post-restoration score was run.
- Sandbox observed at 169 MiB (cap 200 MB); no background jobs or live support runtime were started. Every shell/process invocation was deadline-bounded; all synchronous child processes returned before report writing.
- Tool install: pypdf 5.4.0, official PyPI distribution through existing uv 0.13.0 `uv run --with`, cached only under this sandbox; needed by the unchanged pinned-PDF locator. No global tool update, pacman operation, host service change, or outside-sandbox dependency cache write was performed.
- The only lane write by this seat is this assigned report. No lane git/jj write command, corpus mutation, integration, data-seat dispatch, admission, or canonical Rust judgment was performed.
- Recommended L1 acceptance check after its own pre-data revision: rerun these same controls with an exact-roster check; (e), (f), and (f2) must then FAIL SUPPORT while the honest-shaped probe remains PASS. This recommendation is not an exercised result.
