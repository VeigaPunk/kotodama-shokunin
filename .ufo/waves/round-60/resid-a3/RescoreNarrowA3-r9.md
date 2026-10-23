NONE-MET

# RescoreNarrowA3 — revision-9 residual narrowing re-score

## Axes and pinned authority

- Claim axis: **depth**. Review axes: immutable judged identity, original-dissent preservation, one frozen 24-seat authority, page-specific evidence sensitivity, and reproducible provenance.
- Read revision_note_8 and revision_note_9 before rebuilding. This report covers only the assigned eight narrowing controls plus the honest-shaped positive; dissent-seed and stable-map re-key companions are also exercised. It is not claim judgment, admission, integration or shipping.
- Observed own-clone HEAD: `a56b04fc732f5cc9ee541a5d9d016300ca60a110`; frozen counter SHA-256 `cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d`.
- SESSIONS-only probe SHA-256: `1a2f9384a4de04d22229d90bb5f81e73bbd57b123a5990c91a0ad222ccc262b5`. No other counter byte differs.
- Committed claim-D entry SHA-256: `36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2`. The frozen official packet builder was rerun, producing `cited=47 planted_rows=16 seats=24 planted_per_seat_min=2`, exit 0.

## Counterexample, evidence, impacted axes and correction

**No surviving counterexample among the requested controls.** All eight mutations (a, b, c, d, e, f, f2, g) FAIL frozen and probe, exit 1. Stable-map c2 also FAILS. The honest-shaped positive reaches probe PASS, exit 0, with revision-8/9-compliant evidence on every SUPPORTED line.

**Strongest attempt: (g), deleting the dissenting seat’s report entirely while retaining its session.** The only change from the dissent seed is deletion of `.ufo/waves/round-60/support/SupportJ60.md`. Probe stdout is `SUPPORT FAIL unsupported=['S648:NOT/SupportJ60']`; it also reports `SupportJ60:missing`, 23 qualified seats, and no `good=` deficit. Thus original dissent, not lost redundancy or synthetic-provenance masking, stops this case. The original session and committed transcript still contain `VERDICT P04 NOT-SUPPORTED`.

**Fixed universe:** (e) yields both `S648:NOT/SupportJ60` and `roster`, with `roster-not-the-frozen-24`. Cases (f)/(f2) yield only `roster` while all original 24 seats qualify. The 25th dissenter is not a frozen seat; it cannot silently amend the authority because its addition fails the exact-roster guard. The identity and verdict-preservation axes remain protected in these exercised cases.

**Re-key isolation:** random case (c) fails SUPPORT through mixed CONFINED/BOUND reasons after its new assignment. In c2, labels and URL sets stay unchanged: all 24 seats instead report `packet-not-in-dispatched-task`. Case (d) includes valid revision-9 EVIDENCE on its rewritten landed SUPPORTED line, so its failure is not a missing-evidence shortcut: `report-not-its-own-write` and the original S648 NOT remain, with no coverage deficit.

Local pinned implementation: `accept-d.py:599-603` enforces the exact frozen roster; `:678-692` scans every frozen seat’s report and original-session report write independently of report presence or qualification. The unchanged `bound` and own-write matching checks stop the isolated packet/report rewrites.

**Smallest safe correction:** none indicated by these assigned cases; preserve the exact-roster guard, original-dispatch binding and all-frozen-seat original-session dissent scan. No source/counter fix was made. These are scoped regression receipts, not saturation, authentic support provenance, a claim PASS, or an authority/operability tradeoff proposed for the canonical Rust judge to accept.

## Honest-shaped positive: new evidence rule met

- 141 SUPPORTED lines; minimum 16 locator-normalised words per EVIDENCE span and minimum 5 distinct span words absent from that line’s packet block. Each span locates in its pinned page and **no other pinned page**. These are checked by the unmodified revision-9 `evidenced` predicate and recorded individually in `evidence-audit.json`.
- Pinned page texts are loaded using the frozen manifest/hash checks. The fixture builder reads these page texts, not just packet blocks, to construct the spans. All 48 planted occurrences are NOT-SUPPORTED.
- Example: `VERDICT P04 SUPPORTED EVIDENCE "p s popularity is also illustrated by the distribution of images outside mesopotamia which were found"` for SupportJ60 / S648. It has 16 words, 13 distinct words absent from the packet block, and locates in no other pinned page.
- 300 synthetic curl-shaped calls cover every packet URL, including planted and alternative URLs; each has cwd `/tmp/<Seat>/` and output under that seat directory. These are transcript fixture data, not live fetches executed by this control.
- Reports, transcripts and fake original sessions are explicitly synthetic; no real support seat or support packet/key was read or invoked. Frozen positive fails original-session PROVENANCE (`session-files=0` for every seat), as it should. Probe PASS is a mechanical positive only, not authentic review provenance.
- Cases (a)–(e), (g) and c2 start from the same original dissent seed. Cases (f)/(f2) start from the passing positive, avoiding a frozen-seat NOT that could mask the roster check. Fake sessions copy the original synthetic transcripts, never the mutable landed report. For (g), session existence and its original NOT were asserted before scoring.

## Results and named legs

| Case | Frozen / probe (exit) | Stopping leg / mechanism |
|---|---|---|
| honest-shaped | FAIL (1) / PASS (0) | Probe PASS. Frozen SUPPORT fails original-session PROVENANCE: session-files=0. |
| dissent-seed | FAIL (1) / FAIL (1) | SUPPORT: S648:NOT/SupportJ60; all 24 seats qualify in probe. |
| a-delete-line-and-row | FAIL (1) / FAIL (1) | SET, LINES, ROWS, PINNED, JUDGED, SUPPORT. |
| b-reword-line | FAIL (1) / FAIL (1) | JUDGED entry-hash mismatch; SUPPORT also fails. |
| c-rekey-edited-entry | FAIL (1) / FAIL (1) | SUPPORT: every seat unqualified, through CONFINED bash-url-not-in-packet or BOUND packet-not-in-dispatched-task. Random re-key is not an isolated BOUND test. |
| c2-stable-rekey | FAIL (1) / FAIL (1) | SUPPORT: all 24 fail BOUND packet-not-in-dispatched-task; original S648 dissent remains. |
| d-rewrite-landed-report | FAIL (1) / FAIL (1) | SUPPORT: report-not-its-own-write and original S648:NOT/SupportJ60; no positive-coverage deficit. |
| e-drop-dissenting-member | FAIL (1) / FAIL (1) | SUPPORT: roster-not-the-frozen-24 plus S648:NOT/SupportJ60; no positive-coverage deficit. |
| f-add-25th-member | FAIL (1) / FAIL (1) | SUPPORT: roster-not-the-frozen-24; only unsupported reason is roster while all original 24 qualify. |
| f2-add-25th-dissenter | FAIL (1) / FAIL (1) | SUPPORT: roster-not-the-frozen-24; only unsupported reason is roster. The extra seat is outside the frozen universe, but adding it cannot pass. |
| g-delete-dissenting-report | FAIL (1) / FAIL (1) | SUPPORT: S648:NOT/SupportJ60 retained from its original session despite SupportJ60:missing; no positive-coverage deficit. |

## SESSIONS-only probe diff

```diff
--- frozen/accept-d.py
+++ probe/accept-d.py
@@ -263,7 +263,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
 def tool_calls(transcript):
```

## Receipts

`exit=` records frozen exit; `probe-exit=` records probe exit. PROVENANCE, BOUND and CONFINED are SUPPORT subchecks, not separately printed legs.

```text
RECEIPT RescoreNarrowA3/honest-shaped counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0
RECEIPT RescoreNarrowA3/dissent-seed counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/a-delete-line-and-row counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT;probe:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/b-reword-line counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:JUDGED,SUPPORT;probe:JUDGED,SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/c-rekey-edited-entry counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/c2-stable-rekey counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/d-rewrite-landed-report counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/e-drop-dissenting-member counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/f-add-25th-member counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/f2-add-25th-dissenter counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/g-delete-dissenting-report counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=a56b04fc732f5cc9ee541a5d9d016300ca60a110 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```

## Every counter invocation — full stdout and exit

All 22 counter invocations run from `/fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/clone`, with `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`. Counter deadline is 45 seconds (stricter than 600 maximum); outer fixture runners are also deadline-bounded. Dependency resolution is offline; cache and TMPDIR stay in the assigned sandbox. The stdout below is captured raw output, without terminal-display truncation.

### honest-shaped

24 synthetic seats; all real verdicts SUPPORTED with revision-9-valid EVIDENCE, all planted verdicts NOT-SUPPORTED.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

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
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

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
Captured exit: 0.

Full stderr: empty.

### dissent-seed

Set S648 / SupportJ60 / P04 to NOT-SUPPORTED in both its original synthetic session write and its landed report copy.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### a-delete-line-and-row

From the dissent seed, delete the entire S648 entry line and the S648 SOURCES Registry row; preserve the original key, dispatched packets, sessions and verdicts.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET FAIL cited=46 want=47 missing=['S648'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None']
PINNED FAIL bad=['S648:no-row-or-manifest']
JUDGED FAIL entry_sha256 key=36bd628b6af6 landed=3f8d84e592c5
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET FAIL cited=46 want=47 missing=['S648'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None']
PINNED FAIL bad=['S648:no-row-or-manifest']
JUDGED FAIL entry_sha256 key=36bd628b6af6 landed=3f8d84e592c5
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### b-reword-line

From the dissent seed, replace “The IDD article describes Pazuzu” with “The IDD article explicitly describes Pazuzu”; retain the original judged key and packets.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=36bd628b6af6 landed=751d48637b50
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED FAIL entry_sha256 key=36bd628b6af6 landed=751d48637b50
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:missing', 'SupportB60:missing', 'SupportC60:missing', 'SupportD60:missing', 'SupportE60:missing', 'SupportF60:missing', 'SupportG60:missing', 'SupportH60:missing', 'SupportI60:missing', 'SupportJ60:missing', 'SupportK60:missing', 'SupportL60:missing', 'SupportM60:missing', 'SupportN60:missing', 'SupportO60:missing', 'SupportP60:missing', 'SupportQ60:missing', 'SupportR60:missing', 'SupportS60:missing', 'SupportT60:missing', 'SupportU60:missing', 'SupportV60:missing', 'SupportW60:missing', 'SupportX60:missing']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### c-rekey-edited-entry

From the dissent seed, make the same entry edit, run the exact official packet builder again, and refresh the key digest; retain original sessions and reports.

Packet rebuild command: `timeout 45 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/clone/.ufo/waves/round-60/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/clone/.ufo/waves/round-60/support`.

Full builder stdout:
```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
```
Builder exit: 0; full stderr: "".

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S640:NOT/SupportA60', 'S605:NOT/SupportA60', 'S611:NOT/SupportB60', 'S646:NOT/SupportB60', 'S648:NOT/SupportC60', 'S604:NOT/SupportC60', 'S612:NOT/SupportD60', 'S621:NOT/SupportD60', 'S648:NOT/SupportE60', 'S639:NOT/SupportE60', 'S635:NOT/SupportF60', 'S638:NOT/SupportG60', 'S615:NOT/SupportH60', 'S605:NOT/SupportI60', 'S614:NOT/SupportI60', 'S635:NOT/SupportJ60', 'S618:NOT/SupportJ60', 'S626:NOT/SupportK60', 'S625:NOT/SupportL60', 'S633:NOT/SupportL60', 'S646:NOT/SupportM60', 'S642:NOT/SupportN60', 'S620:NOT/SupportO60', 'S639:NOT/SupportP60', 'S631:NOT/SupportP60', 'S615:NOT/SupportQ60', 'S641:NOT/SupportQ60', 'S610:NOT/SupportR60', 'S600:NOT/SupportR60', 'S608:NOT/SupportS60', 'S617:NOT/SupportS60', 'S600:NOT/SupportT60', 'S610:NOT/SupportT60', 'S618:NOT/SupportU60', 'S609:NOT/SupportU60', 'S628:NOT/SupportV60', 'S647:NOT/SupportW60', 'S621:NOT/SupportW60', 'S632:NOT/SupportX60', 'S614:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S640:NOT/SupportA60', 'S605:NOT/SupportA60', 'S611:NOT/SupportB60', 'S646:NOT/SupportB60', 'S648:NOT/SupportC60', 'S604:NOT/SupportC60', 'S612:NOT/SupportD60', 'S621:NOT/SupportD60', 'S648:NOT/SupportE60', 'S639:NOT/SupportE60', 'S635:NOT/SupportF60', 'S638:NOT/SupportG60', 'S615:NOT/SupportH60', 'S605:NOT/SupportI60', 'S614:NOT/SupportI60', 'S635:NOT/SupportJ60', 'S618:NOT/SupportJ60', 'S626:NOT/SupportK60', 'S625:NOT/SupportL60', 'S633:NOT/SupportL60', 'S646:NOT/SupportM60', 'S642:NOT/SupportN60', 'S620:NOT/SupportO60', 'S639:NOT/SupportP60', 'S631:NOT/SupportP60', 'S615:NOT/SupportQ60', 'S641:NOT/SupportQ60', 'S610:NOT/SupportR60', 'S600:NOT/SupportR60', 'S608:NOT/SupportS60', 'S617:NOT/SupportS60', 'S600:NOT/SupportT60', 'S610:NOT/SupportT60', 'S618:NOT/SupportU60', 'S609:NOT/SupportU60', 'S628:NOT/SupportV60', 'S647:NOT/SupportW60', 'S621:NOT/SupportW60', 'S632:NOT/SupportX60', 'S614:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:bash-url-not-in-packet', 'SupportB60:X2/sees:bash-url-not-in-packet', 'SupportC60:X2/sees:bash-url-not-in-packet', 'SupportD60:X2/sees:bash-url-not-in-packet', 'SupportE60:X2/sees:bash-url-not-in-packet', 'SupportF60:X2/sees:bash-url-not-in-packet', 'SupportG60:X2/sees:bash-url-not-in-packet', 'SupportH60:X2/sees:packet-not-in-dispatched-task', 'SupportI60:X2/sees:packet-not-in-dispatched-task', 'SupportJ60:X2/sees:bash-url-not-in-packet', 'SupportK60:X2/sees:bash-url-not-in-packet', 'SupportL60:X2/sees:bash-url-not-in-packet', 'SupportM60:X2/sees:bash-url-not-in-packet', 'SupportN60:X2/sees:packet-not-in-dispatched-task', 'SupportO60:X2/sees:bash-url-not-in-packet', 'SupportP60:X2/sees:bash-url-not-in-packet', 'SupportQ60:X2/sees:bash-url-not-in-packet', 'SupportR60:X2/sees:bash-url-not-in-packet', 'SupportS60:X2/sees:bash-url-not-in-packet', 'SupportT60:X2/sees:bash-url-not-in-packet', 'SupportU60:X2/sees:packet-not-in-dispatched-task', 'SupportV60:X2/sees:bash-url-not-in-packet', 'SupportW60:X2/sees:packet-not-in-dispatched-task', 'SupportX60:X2/sees:bash-url-not-in-packet']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### c2-stable-rekey

Isolated companion: make the same edit, refresh the entry hash, key digest and packet headers/entry text WITHOUT changing label mappings or URL sets; preserve original sessions/reports.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:packet-not-in-dispatched-task', 'SupportB60:X2/sees:packet-not-in-dispatched-task', 'SupportC60:X2/sees:packet-not-in-dispatched-task', 'SupportD60:X2/sees:packet-not-in-dispatched-task', 'SupportE60:X2/sees:packet-not-in-dispatched-task', 'SupportF60:X2/sees:packet-not-in-dispatched-task', 'SupportG60:X2/sees:packet-not-in-dispatched-task', 'SupportH60:X2/sees:packet-not-in-dispatched-task', 'SupportI60:X2/sees:packet-not-in-dispatched-task', 'SupportJ60:X2/sees:packet-not-in-dispatched-task', 'SupportK60:X2/sees:packet-not-in-dispatched-task', 'SupportL60:X2/sees:packet-not-in-dispatched-task', 'SupportM60:X2/sees:packet-not-in-dispatched-task', 'SupportN60:X2/sees:packet-not-in-dispatched-task', 'SupportO60:X2/sees:packet-not-in-dispatched-task', 'SupportP60:X2/sees:packet-not-in-dispatched-task', 'SupportQ60:X2/sees:packet-not-in-dispatched-task', 'SupportR60:X2/sees:packet-not-in-dispatched-task', 'SupportS60:X2/sees:packet-not-in-dispatched-task', 'SupportT60:X2/sees:packet-not-in-dispatched-task', 'SupportU60:X2/sees:packet-not-in-dispatched-task', 'SupportV60:X2/sees:packet-not-in-dispatched-task', 'SupportW60:X2/sees:packet-not-in-dispatched-task', 'SupportX60:X2/sees:packet-not-in-dispatched-task']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### d-rewrite-landed-report

From the dissent seed, rewrite only landed P04 NOT-SUPPORTED back to its original SUPPORTED line, including its valid revision-9 EVIDENCE. Preserve the original session NOT.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:X2/sees:report-not-its-own-write', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### e-drop-dissenting-member

From the dissent seed, remove only SupportJ60 from registry.json; preserve its dissent report, original session, transcript, packet and key mapping.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60', 'roster', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60', 'roster'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### f-add-25th-member

From the passing positive, append AdditionalReviewer60 only to registry.json. No pre-existing dissent can mask the roster test.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['roster', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['roster'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### f2-add-25th-dissenter

From the passing positive, append AdditionalReviewer60 with a complete packet, key mapping, report and adapted synthetic original session rejecting S648/P04; refresh the key digest. All original 24 verdicts remain unchanged.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['roster', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['roster'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### g-delete-dissenting-report

From the dissent seed, delete only SupportJ60.md. Its synthetic original session and committed transcript still contain VERDICT P04 NOT-SUPPORTED.

#### frozen

Command: `timeout 45 python3 -B reports/round-60/accept-d.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:missing', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportJ60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:missing', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

## Reproduction artifacts and boundaries

- New artifacts: `/fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/residual-controls.py`, `baseline.zip`, `results.json`, `evidence-audit.json`, `probe.diff`, `outputs/`, and `fake-sessions/`. Every case’s changed-file hashes and exact stdout/stderr/exit are retained in `results.json`.
- Exact stored assignment can be rerun with `timeout 18 env PYTHONDONTWRITEBYTECODE=1 python3 -B residual-controls.py <case-name>` from the new r9 directory. The runner restores its archived baseline after each case; no extra post-restoration counter run was performed.
- To remain below the 200 MB sandbox cap, reused the existing own clone and fetched/checked out the assigned new commit there only. Saved the old frozen counter as `../accept-d-r7.py`; retained the earlier baseline archive, captured result/output files and first report without editing them. No lane git/jj write command was run.
- Sandbox observed at 179 MiB (below 200 MB). Each new fixture/result file is limited to 8 MiB; captured process output is bounded. No delegation or background jobs.
- Runner SHA-256: `0b40d1d6bd3b04dfe2f69c7c2d8b6adde6154415bad3ad86783bc90eaa30b441`.
- Results SHA-256: `eb3938baab8b058d962b5e366f540c53faa0410047e477ec60f5a488c598c94e`.
- Baseline archive SHA-256: `347db0f48be382f8037ca1d7754e1c9bf2cda18f98cae273db3ef004f77c2066`.
- Tool installs/updates: **none**. Reused the copied existing offline pypdf==5.4.0 cache and unchanged extraction adapter (offline mode, Python -B and deadline only). No pacman transaction, dependency download, host service change, support dispatch, canonical judgment, admission, integration or shipping.
- The only new lane write is this report, via the write tool at `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-60/resid-a3/RescoreNarrowA3-r9.md`. The earlier `RescoreNarrowA3.md` was not touched.

## Selected mutation manifests

Hashes are from the scored mutation relative to its appropriate positive/dissent seed; full manifests for every case remain in `results.json`.

### d-rewrite-landed-report

```json
{
  ".ufo/waves/round-60/support/SupportJ60.md": {
    "before": "8d596019cd9c052ce81404a8237b794921a33252b4b6cbc6cea891f80a74712d",
    "after": "75299262581184805bbb34e520934f786c0e41f1179aec69d9d6a41cbaf9ed8b"
  }
}
```

### e-drop-dissenting-member

```json
{
  ".ufo/waves/round-60/support/registry.json": {
    "before": "c1efad39bbb1141eee61a0f0c78d6a3d296b19a67cd5db5db2317131b65627e4",
    "after": "e9ed37df0934f1b0ede686acf278de381a6ef46a30b8ca6ca0cb2f3c5eacc1bc"
  }
}
```

### f-add-25th-member

```json
{
  ".ufo/waves/round-60/support/registry.json": {
    "before": "c1efad39bbb1141eee61a0f0c78d6a3d296b19a67cd5db5db2317131b65627e4",
    "after": "281e37f53c0e98a333fa59dc0e06c263e0d26243e872bc9e2575618b3905fcaa"
  }
}
```

### f2-add-25th-dissenter

```json
{
  ".ufo/waves/round-60/support/AdditionalReviewer60.md": {
    "before": null,
    "after": "8d596019cd9c052ce81404a8237b794921a33252b4b6cbc6cea891f80a74712d"
  },
  ".ufo/waves/round-60/support/packet-AdditionalReviewer60.md": {
    "before": null,
    "after": "6847bc17712e13cee2795dcc2d9a68cc83312bdfa352802cf6435ca8848c131c"
  },
  ".ufo/waves/round-60/support/planted-key.json": {
    "before": "ba3fcbbb9cde5fe8f43b5fca0b46243ece16d69ce06a2c7e18408a62dccf10c0",
    "after": "d52da4464d4e78ececc1bc827d5fdc2eebab5169321bc6b4b409a13d550f1dca"
  },
  ".ufo/waves/round-60/support/registry.json": {
    "before": "c1efad39bbb1141eee61a0f0c78d6a3d296b19a67cd5db5db2317131b65627e4",
    "after": "281e37f53c0e98a333fa59dc0e06c263e0d26243e872bc9e2575618b3905fcaa"
  },
  ".ufo/waves/round-60/support/transcripts/KotodamaR60A3.AdditionalReviewer60.jsonl": {
    "before": null,
    "after": "c4ebb11e01057ec08b2086de58b2db0c9895cf40918e05c93ed7e1efcd1e8113"
  },
  "reports/round-60/planted-key.sha256": {
    "before": "479844247529f95bfaca2e3f169d1db9073f2803768a1150715cf4ce50f2be3c",
    "after": "32e3aa819414e48c346e6f8582da14814f4eb618071c779d293dc45fcec9c2a7"
  }
}
```

### g-delete-dissenting-report

```json
{
  ".ufo/waves/round-60/support/SupportJ60.md": {
    "before": "8d596019cd9c052ce81404a8237b794921a33252b4b6cbc6cea891f80a74712d",
    "after": null
  }
}
```
