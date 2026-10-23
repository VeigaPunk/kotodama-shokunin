NONE-MET

# RescoreNarrowA3 — revision-7 post-verdict narrowing controls

## Axes and authority

- Claim axis: **depth**. Diagnostic axes: immutable judged identity, original-verdict preservation, a single frozen 24-seat authority, page-evidence sensitivity, and reproducible provenance.
- Read `claims.json` revision_note_6 and revision_note_7 before fixture work. This is the assigned residual critic re-score, not a claim judgment or admission.
- Assigned and observed clone HEAD: `1cd9db7cdc83fd41f5d04cd620af879555442f19`. Frozen counter SHA-256: `45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59`.
- SESSIONS-only probe SHA-256: `9abbe01b596503f492572e14eea40d3d7757e8644b8badba9fd232cbe89ed123`; no other counter byte changes.
- Rebuilt using the claim-D bytes committed at this revision, entry SHA-256 `36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2`, rather than retaining the earlier control’s candidate-entry bytes. Reran the exact official packet builder and enforced the frozen planted-file digest.

## Counterexample, evidence, impacted axes, smallest safe correction

**No surviving counterexample among these controls.** All eight requested mutations (a, b, c, d, e, f, f2, g) FAIL frozen and probe, exit 1. The stable-map re-key companion also FAILS. The honest-shaped positive reaches probe PASS, exit 0.

**Strongest counterexample attempted: (g), delete the dissenting lane report entirely while its session remains.** Only `.ufo/waves/round-60/support/SupportP60.md` is removed. The original S648/P06 NOT remains in its unchanged synthetic session and transcript. Probe stdout is `SUPPORT FAIL unsupported=['S648:NOT/SupportP60']`, with `SupportP60:missing`, 23 qualified seats and no `good=` deficit. This isolates preserved dissent: the failure is not insufficient positive redundancy or provenance masking. Verdict preservation and immutable review identity survive this strongest missing-report case.

For (e), removing only the dissenting registry member now yields both `S648:NOT/SupportP60` and `roster`, with `roster-not-the-frozen-24`. For (f)/(f2), all original 24 seats qualify and the only unsupported reason is `roster`. The extra dissenter is intentionally outside the frozen dissent universe, but its addition cannot pass. These cases protect the single frozen authority without treating the surviving mutable registry as a replacement authority.

At the pinned counter, `accept-d.py:571-575` enforces the exact roster, `:616-619` binds qualification to original dispatch/report contents, and `:649-663` scans every frozen seat’s report and original-session report write even if its report is missing or it cannot qualify. The stable-map companion isolates BOUND: all 24 seats report `packet-not-in-dispatched-task`. The randomized official rebuild first trips CONFINED because reassigned packet URLs no longer match the original sessions, so it is not by itself an isolated BOUND result.

**Smallest safe correction:** none indicated for these assigned cases; retain exact-roster enforcement, original-dispatch binding and the all-frozen-seat original-session dissent scan. No source/counter correction was made. This is scoped evidence that the tested narrowing regressions are stopped, not saturation, authentic support provenance, a claim PASS, or a tradeoff proposed for the canonical Rust judge to accept.

## Honest-shaped positive and isolation

- Official builder: `cited=47 planted_rows=16 seats=24 planted_per_seat_min=2`, exit 0. Each real block has three distinct seat assignments.
- Generated **141 SUPPORTED lines**, each carrying an `EVIDENCE` span of **16 locator-normalised words** located in its id’s pinned page text and absent from its packet block. All **48 planted occurrences** are NOT-SUPPORTED. `evidence-audit.json` records every span and page/block check; pinned texts are loaded through the frozen counter’s manifest/hash validation.
- Example, SupportP60/P06 (S648): `VERDICT P06 SUPPORTED EVIDENCE "p s popularity is also illustrated by the distribution of images outside mesopotamia which were found"`.
- Every packet URL has a synthetic `bash`/`curl` call with cwd `/tmp/<Seat>/` and output under that directory: 300 calls, including planted blocks and alternative listed URLs. These are transcript fixture data, not executed live fetches. The fixture builder reads the frozen pinned page texts to construct evidence; it is not a packet-only fixture.
- All verdicts, reports, transcript copies and session files are explicitly synthetic. No real support seat, support packet/key, or support runtime was read or invoked. The positive frozen run correctly fails original-session PROVENANCE with `session-files=0` for every seat. The positive probe proves mechanical acceptance only, never authentic review provenance.
- Cases (a)–(e), (g) and c2 start from the same original dissent seed. Cases (f)/(f2) start from the positive, so pre-existing frozen-seat dissent cannot conceal the roster check. Each case restores the same archived baseline before mutation. Fake sessions copy original synthetic transcripts, not the landed report. For (g), session existence and its original NOT were asserted before scoring.

## Requested results

| Case | Frozen / probe (exit) | Failing leg / mechanism |
|---|---|---|
| honest-shaped | FAIL (1) / PASS (0) | Probe PASS; frozen SUPPORT fails PROVENANCE (session-files=0). |
| dissent-seed | FAIL (1) / FAIL (1) | SUPPORT: S648:NOT/SupportP60; all 24 seats qualify in probe. |
| a-delete-line-and-row | FAIL (1) / FAIL (1) | SET, LINES, ROWS, PINNED, JUDGED, SUPPORT. |
| b-reword-line | FAIL (1) / FAIL (1) | JUDGED entry-hash mismatch; SUPPORT also fails. |
| c-rekey-edited-entry | FAIL (1) / FAIL (1) | SUPPORT: all 24 fail CONFINED (bash-url-not-in-packet) after random reassignment; c2 isolates BOUND. |
| c2-stable-rekey | FAIL (1) / FAIL (1) | SUPPORT: all 24 fail BOUND (packet-not-in-dispatched-task); original S648 dissent also remains. |
| d-rewrite-landed-report | FAIL (1) / FAIL (1) | SUPPORT: report-not-its-own-write; S648:NOT/SupportP60 remains, with no positive-coverage deficit. |
| e-drop-dissenting-member | FAIL (1) / FAIL (1) | SUPPORT: roster-not-the-frozen-24 AND S648:NOT/SupportP60; no positive-coverage deficit. |
| f-add-25th-member | FAIL (1) / FAIL (1) | SUPPORT: roster-not-the-frozen-24; only unsupported reason is roster although all original 24 seats qualify. |
| f2-add-25th-dissenter | FAIL (1) / FAIL (1) | SUPPORT: roster-not-the-frozen-24; only unsupported reason is roster. Extra seat cannot amend the frozen universe. |
| g-delete-dissenting-report | FAIL (1) / FAIL (1) | SUPPORT: S648:NOT/SupportP60 from its retained session despite SupportP60:missing; no positive-coverage deficit. |

## SESSIONS-only probe diff

```diff
--- frozen/accept-d.py
+++ probe/accept-d.py
@@ -235,7 +235,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
 def tool_calls(transcript):
```

## Receipts

`exit=` is frozen exit; `probe-exit=` is probe exit. PROVENANCE, BOUND and CONFINED are SUPPORT subchecks, not separately printed legs.

```text
RECEIPT RescoreNarrowA3/honest-shaped counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0
RECEIPT RescoreNarrowA3/dissent-seed counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/a-delete-line-and-row counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT;probe:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/b-reword-line counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:JUDGED,SUPPORT;probe:JUDGED,SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/c-rekey-edited-entry counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/c2-stable-rekey counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/d-rewrite-landed-report counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/e-drop-dissenting-member counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/f-add-25th-member counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/f2-add-25th-dissenter counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/g-delete-dissenting-report counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```

## Every counter run — full stdout and exit

All commands use cwd `/fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/clone`, `PYTHONDONTWRITEBYTECODE=1`, `python3 -B`, a copied offline dependency cache and sandbox TMPDIR. The 45-second counter deadline is stricter than the permitted 600-second maximum; fixture runners also have bounded outer deadlines. All 22 counter invocations follow. These are captured raw strings, not terminal-display truncation.

### honest-shaped

Positive: all 24 synthetic seats; real verdicts SUPPORTED with page-only EVIDENCE and all planted verdicts NOT-SUPPORTED.

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

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

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

Set SupportP60/P06 (S648) to NOT-SUPPORTED in both its original synthetic session write and lane-report copy.

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
SUPPORT FAIL unsupported=['S648:NOT/SupportP60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportP60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### a-delete-line-and-row

From the dissent seed, delete the entire S648 entry line and S648 SOURCES Registry row; preserve dispatched packets and original verdicts.

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

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

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

From the dissent seed, replace “The IDD article describes Pazuzu” with “The IDD article explicitly describes Pazuzu”; preserve the original key and packets.

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

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

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

From the dissent seed, make the same entry edit, rerun the frozen official packet builder, and refresh the key digest; preserve original sessions and reports.

Packet rebuild command: `timeout 45 python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/clone/.ufo/waves/round-60/support/planted-rows.md /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/clone/.ufo/waves/round-60/support`.

Full builder stdout:
```text
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
```
Builder exit: 0; stderr: "".

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
SUPPORT FAIL unsupported=['S634:NOT/SupportA60', 'S621:NOT/SupportB60', 'S647:NOT/SupportB60', 'S631:NOT/SupportC60', 'S631:NOT/SupportD60', 'S630:NOT/SupportE60', 'S621:NOT/SupportE60', 'S615:NOT/SupportF60', 'S645:NOT/SupportG60', 'S600:NOT/SupportG60', 'S611:NOT/SupportH60', 'S627:NOT/SupportI60', 'S618:NOT/SupportI60', 'S628:NOT/SupportJ60', 'S632:NOT/SupportK60', 'S612:NOT/SupportL60', 'S613:NOT/SupportM60', 'S622:NOT/SupportM60', 'S607:NOT/SupportN60', 'S641:NOT/SupportN60', 'S624:NOT/SupportO60', 'S614:NOT/SupportO60', 'S620:NOT/SupportP60', 'S629:NOT/SupportP60', 'S634:NOT/SupportQ60', 'S617:NOT/SupportQ60', 'S605:NOT/SupportR60', 'S632:NOT/SupportR60', 'S641:NOT/SupportS60', 'S636:NOT/SupportU60', 'S611:NOT/SupportV60', 'S601:NOT/SupportV60', 'S644:NOT/SupportW60', 'S608:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S634:NOT/SupportA60', 'S621:NOT/SupportB60', 'S647:NOT/SupportB60', 'S631:NOT/SupportC60', 'S631:NOT/SupportD60', 'S630:NOT/SupportE60', 'S621:NOT/SupportE60', 'S615:NOT/SupportF60', 'S645:NOT/SupportG60', 'S600:NOT/SupportG60', 'S611:NOT/SupportH60', 'S627:NOT/SupportI60', 'S618:NOT/SupportI60', 'S628:NOT/SupportJ60', 'S632:NOT/SupportK60', 'S612:NOT/SupportL60', 'S613:NOT/SupportM60', 'S622:NOT/SupportM60', 'S607:NOT/SupportN60', 'S641:NOT/SupportN60', 'S624:NOT/SupportO60', 'S614:NOT/SupportO60', 'S620:NOT/SupportP60', 'S629:NOT/SupportP60', 'S634:NOT/SupportQ60', 'S617:NOT/SupportQ60', 'S605:NOT/SupportR60', 'S632:NOT/SupportR60', 'S641:NOT/SupportS60', 'S636:NOT/SupportU60', 'S611:NOT/SupportV60', 'S601:NOT/SupportV60', 'S644:NOT/SupportW60', 'S608:NOT/SupportX60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:bash-url-not-in-packet', 'SupportB60:X2/sees:bash-url-not-in-packet', 'SupportC60:X2/sees:bash-url-not-in-packet', 'SupportD60:X2/sees:bash-url-not-in-packet', 'SupportE60:X2/sees:bash-url-not-in-packet', 'SupportF60:X2/sees:bash-url-not-in-packet', 'SupportG60:X2/sees:bash-url-not-in-packet', 'SupportH60:X2/sees:bash-url-not-in-packet', 'SupportI60:X2/sees:bash-url-not-in-packet', 'SupportJ60:X2/sees:bash-url-not-in-packet', 'SupportK60:X2/sees:bash-url-not-in-packet', 'SupportL60:X2/sees:bash-url-not-in-packet', 'SupportM60:X2/sees:bash-url-not-in-packet', 'SupportN60:X2/sees:bash-url-not-in-packet', 'SupportO60:X2/sees:bash-url-not-in-packet', 'SupportP60:X2/sees:bash-url-not-in-packet', 'SupportQ60:X2/sees:bash-url-not-in-packet', 'SupportR60:X2/sees:bash-url-not-in-packet', 'SupportS60:X2/sees:bash-url-not-in-packet', 'SupportT60:X2/sees:bash-url-not-in-packet', 'SupportU60:X2/sees:bash-url-not-in-packet', 'SupportV60:X2/sees:bash-url-not-in-packet', 'SupportW60:X2/sees:bash-url-not-in-packet', 'SupportX60:X2/sees:bash-url-not-in-packet']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### c2-stable-rekey

Isolated companion: make the same edit, refresh entry hash, key digest and packet headers/entry text WITHOUT changing label mappings or URL sets; preserve original sessions and reports.

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
SUPPORT FAIL unsupported=['S648:NOT/SupportP60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportP60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:packet-not-in-dispatched-task', 'SupportB60:X2/sees:packet-not-in-dispatched-task', 'SupportC60:X2/sees:packet-not-in-dispatched-task', 'SupportD60:X2/sees:packet-not-in-dispatched-task', 'SupportE60:X2/sees:packet-not-in-dispatched-task', 'SupportF60:X2/sees:packet-not-in-dispatched-task', 'SupportG60:X2/sees:packet-not-in-dispatched-task', 'SupportH60:X2/sees:packet-not-in-dispatched-task', 'SupportI60:X2/sees:packet-not-in-dispatched-task', 'SupportJ60:X2/sees:packet-not-in-dispatched-task', 'SupportK60:X2/sees:packet-not-in-dispatched-task', 'SupportL60:X2/sees:packet-not-in-dispatched-task', 'SupportM60:X2/sees:packet-not-in-dispatched-task', 'SupportN60:X2/sees:packet-not-in-dispatched-task', 'SupportO60:X2/sees:packet-not-in-dispatched-task', 'SupportP60:X2/sees:packet-not-in-dispatched-task', 'SupportQ60:X2/sees:packet-not-in-dispatched-task', 'SupportR60:X2/sees:packet-not-in-dispatched-task', 'SupportS60:X2/sees:packet-not-in-dispatched-task', 'SupportT60:X2/sees:packet-not-in-dispatched-task', 'SupportU60:X2/sees:packet-not-in-dispatched-task', 'SupportV60:X2/sees:packet-not-in-dispatched-task', 'SupportW60:X2/sees:packet-not-in-dispatched-task', 'SupportX60:X2/sees:packet-not-in-dispatched-task']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### d-rewrite-landed-report

From the dissent seed, rewrite only the landed P06 NOT-SUPPORTED to its original SUPPORTED line, including valid EVIDENCE. Leave the original session write unchanged.

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
SUPPORT FAIL unsupported=['S648:NOT/SupportP60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportP60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:X2/sees:report-not-its-own-write', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### e-drop-dissenting-member

From the dissent seed, delete only SupportP60 from registry.json; preserve its dissent report, original session, transcript, packet and key mapping.

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
SUPPORT FAIL unsupported=['S648:NOT/SupportP60', 'roster', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportP60', 'roster'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2'] roster-not-the-frozen-24
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

### f-add-25th-member

From the passing positive, append AdditionalReviewer60 to registry.json only; no pre-existing dissent masks the roster test.

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

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

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

From the passing positive, append AdditionalReviewer60 with a complete packet, key mapping, report and adapted synthetic original session rejecting S648/P06; refresh the key digest. Original 24 verdicts remain positive.

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

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

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

From the dissent seed, delete only SupportP60.md. Its original synthetic session and committed transcript still contain VERDICT P06 NOT-SUPPORTED.

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
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:session-files=0', 'SupportB60:X2/sees:session-files=0', 'SupportC60:X2/sees:session-files=0', 'SupportD60:X2/sees:session-files=0', 'SupportE60:X2/sees:session-files=0', 'SupportF60:X2/sees:session-files=0', 'SupportG60:X2/sees:session-files=0', 'SupportH60:X2/sees:session-files=0', 'SupportI60:X2/sees:session-files=0', 'SupportJ60:X2/sees:session-files=0', 'SupportK60:X2/sees:session-files=0', 'SupportL60:X2/sees:session-files=0', 'SupportM60:X2/sees:session-files=0', 'SupportN60:X2/sees:session-files=0', 'SupportO60:X2/sees:session-files=0', 'SupportP60:missing', 'SupportQ60:X2/sees:session-files=0', 'SupportR60:X2/sees:session-files=0', 'SupportS60:X2/sees:session-files=0', 'SupportT60:X2/sees:session-files=0', 'SupportU60:X2/sees:session-files=0', 'SupportV60:X2/sees:session-files=0', 'SupportW60:X2/sees:session-files=0', 'SupportX60:X2/sees:session-files=0']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

#### probe

Command: `timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/accept-d-probe.py`.

Full stdout:
```text
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S648:NOT/SupportP60'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:missing', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
```
Captured exit: 1.

Full stderr: empty.

## Artifacts, reproduction and boundaries

- Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/`, observed 178 MiB (below 200 MB). No delegation or background jobs.
- `residual-controls.py` prepares and scores the synthetic fixtures; the copied original wave-1 builders are reference material and were never edited or run against their original location. The new runner reuses their snapshot/restore and mutation patterns, adding the committed claim-D entry, valid EVIDENCE, curl-shaped calls and (g).
- To rerun this exact stored assignment, use `timeout 18 env PYTHONDONTWRITEBYTECODE=1 python3 -B residual-controls.py <case-name>` from this sandbox. `baseline.zip` preserves this randomly assigned positive. `results.json` contains every changed-file hash and exact stdout/stderr/exit; `outputs/` holds the separate raw streams; `evidence-audit.json` holds all page-only spans. The runner restores its baseline after each case; no extra post-restoration counter run was performed.
- Runner SHA-256: `dce8ef561446b381fab674fc232d3a7d9f8990ab9c23cccb02d981a3d1b6a627`.
- Results SHA-256: `f32cbc7a8428682c11b65b1decf0872ddf825a77c6172870badaaf833e4b8d25`.
- Baseline archive SHA-256: `c442d9cb3d840d301b711cfafab467dd54baef67e3026486c36e16be02343f53`.
- Each new fixture/result file is bounded to 8 MiB by the runner; captured stdout/stderr are bounded. The locator’s temporary PDF and dependency cache stay in the sandbox. The copied extraction adapter only adds offline mode, Python -B and a deadline to the exact pinned-pypdf invocation; locator/extraction source was not modified.
- Tool installs/updates: **none**. Reused the copied existing offline pypdf==5.4.0 cache and unchanged uv extraction adapter. No pacman transaction, dependency download, host service change, lane git/jj write command, support dispatch, canonical judgment, admission, integration, or shipping.
- The only lane write is this assigned report, made with the write tool at `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-60/resid-a3/RescoreNarrowA3.md`.

## Selected mutation manifests

Hashes below are from the scored changes relative to the appropriate positive/dissent seed, not a later rebuilt fixture. Every case’s full manifest is retained in `results.json`.

### d-rewrite-landed-report

```json
{
  ".ufo/waves/round-60/support/SupportP60.md": {
    "before": "4b3d6b26008bd009bdd1a2acc65aa7d91ca63c8bfba5dd5df459c34e6554aa81",
    "after": "0866d648bb33962bb9a3496e6068a83a6840bfd46e1c27988f2c221969101540"
  }
}
```

### e-drop-dissenting-member

```json
{
  ".ufo/waves/round-60/support/registry.json": {
    "before": "c1efad39bbb1141eee61a0f0c78d6a3d296b19a67cd5db5db2317131b65627e4",
    "after": "909bb3f445a078b83823cdc304c8bdc0f7e803fc8dd250378678511a9278359a"
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
    "after": "4b3d6b26008bd009bdd1a2acc65aa7d91ca63c8bfba5dd5df459c34e6554aa81"
  },
  ".ufo/waves/round-60/support/packet-AdditionalReviewer60.md": {
    "before": null,
    "after": "5f26bca196afcb82765435f4cac46ea858a6da8dfdd29b4fffc9df273a83eaaa"
  },
  ".ufo/waves/round-60/support/planted-key.json": {
    "before": "c1a9571ee5f4b6b2398ffff19e7536f14b73cd770ad008fb80f5984b2a90d02f",
    "after": "ad2819400d02b724317a69224db65f4a07836a675743f5ae1cc2346b6ffe3e5b"
  },
  ".ufo/waves/round-60/support/registry.json": {
    "before": "c1efad39bbb1141eee61a0f0c78d6a3d296b19a67cd5db5db2317131b65627e4",
    "after": "281e37f53c0e98a333fa59dc0e06c263e0d26243e872bc9e2575618b3905fcaa"
  },
  ".ufo/waves/round-60/support/transcripts/KotodamaR60A3.AdditionalReviewer60.jsonl": {
    "before": null,
    "after": "9cb50e8044ec2ec7a6acd97c83ce5d018394b86844216bc656d7f02f7dba571e"
  },
  "reports/round-60/planted-key.sha256": {
    "before": "406049dcc124449bb5bf02b8d9be41e74f66a5ec26f5c48861e31a2b87d0b635",
    "after": "cf31798a252d006e633d138cb9c279f35b5afe48bcea2186879cca35f194ec19"
  }
}
```

### g-delete-dissenting-report

```json
{
  ".ufo/waves/round-60/support/SupportP60.md": {
    "before": "4b3d6b26008bd009bdd1a2acc65aa7d91ca63c8bfba5dd5df459c34e6554aa81",
    "after": null
  }
}
```
