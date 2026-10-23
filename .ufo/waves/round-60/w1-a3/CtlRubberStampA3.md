CONTROL-MET: honest-shaped-positive

# CtlRubberStampA3 — revision-5 pre-data control

**Qualification of the first line:** the explicitly requested, fabricated honest-shaped positive reaches PASS under the authorized SESSIONS-only probe, with no actual page requests or reviews. This follows the assignment's literal ANY-fixture/probe reporting rule. **The all-true rubber-stamp negative control does not reach PASS, even under the probe.** The positive is satisfiability calibration, not real support, a frozen-counter bypass, or a claim verdict.

## Axes and result

- **Depth (declared D):** distinguish source support from merely stamped support.
- **Calibration:** reject the all-true negative while permitting the honest-shaped positive.
- **Operability / provenance isolation:** exercise every leg without changing any counter rule except the authorized probe's SESSIONS location.

| Fixture | Frozen counter | SESSIONS-only probe | Blocking leg / explanation |
|---|---|---|---|
| all-true | FAIL, exit 1 | FAIL, exit 1 | SUPPORT. Frozen: no genuine session files. Probe: all 24 seats remain X2 because they endorse both planted labels. |
| honest-shaped-positive | FAIL, exit 1 | PASS, exit 0 | Frozen SUPPORT: no genuine session files. Probe: all 24 seats Q2, all 47 real ids supported. Predicate is satisfiable. |

RECEIPT CtlRubberStampA3/all-true counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT probe-counter-sha256=429a5e09688a0a7701b45a313cf5b0473daf0c5704ca3e0f08359f7b8fbdba27 probe-exit=1
RECEIPT CtlRubberStampA3/honest-shaped-positive counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=PASS stopped-by=SUPPORT(frozen:PROVENANCE);none(probe) probe-counter-sha256=429a5e09688a0a7701b45a313cf5b0473daf0c5704ca3e0f08359f7b8fbdba27 probe-exit=0

## Counterexample, evidence, and smallest safe correction

**Attempted counterexample:** apply the inherited candidate patch, preserve valid captures/packets/key, and fabricate every declared reviewer as an all-true rubber stamp. The registry contains 24 reviewer records with the required attempt-3 agentIds; each transcript's session_init task contains its exact packet; each packet URL has a synthetic bash/curl tool call with cwd `/tmp/<Seat>/`; each transcript ends with a write of exactly its landed report. There are 300 recorded curl calls, but **zero executed page requests**. No real reviewer was dispatched or contacted.

This stronger-shaped all-true fixture still fails: its 189 verdicts are SUPPORTED, including all 48 planted labels. The probe output has no `/sees:` reason, so provenance-copy, BLIND, CONFINED, BOUND and own-report-write checks no longer mask the planted-label check. Nevertheless every seat is X2, the qualified set is empty, and every real id has good=0. Counter lines 568–571 require every planted label to be NOT-SUPPORTED and never SUPPORTED before a seat qualifies. All six preceding legs pass in both runs.

**Paired positive:** retain the same entry, SOURCES, captures, packets, key and registry; change only report verdicts and the matching final write/session bytes so the 48 planted labels are NOT-SUPPORTED and all 141 real labels are SUPPORTED. The probe then returns PASS: 24 Q2 seats and no unsupported ids. Each of the 47 real ids occurs in three distinct packets. Thus the negative does not merely expose an unsatisfiable predicate.

**Impacted axes:** this exercise supports the instrument's rubber-stamp discrimination and mechanical satisfiability, not the scholarly depth of the entry. The six mechanical candidate legs passing is not evidence that any quote is body text or that a page supports every entry clause. Synthetic fetch-shaped calls are not source openings. Passing the positive after intentionally replacing session provenance must never be described as real review or saturation of depth.

**Smallest safe correction:** no counter edit is indicated by the all-true negative. Preserve both planted-label qualification and the original SESSIONS authority; retain the specified history/session closure and later real source review. Do not use this probe or its fabricated positive as the claim's measurement. The frozen counter rejects both fabricated fixtures, so this report demonstrates no unmodified-counter acceptance bypass. No judgment, admission, integration or shipping was performed.

## Inputs, construction, and isolated artifacts

Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/`.

1. Read the lane's claims.json first, then the counter and packet builder. Cloned with `env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q --no-hardlinks` and checked out exactly `14e6413820d482913f723432b62d566967ccd1a6`, only inside this sandbox.
2. Applied `/fast/scratch/hyaku/kotodama-r60a3/L1/build.patch` in the clone. Patch sha256: `e37abc6d6403a26ecaeb8aa6434dba3d3ffd02775a7e53ce9d1c8090a9ef2d61`. The patched entry was byte-equal to L1/candidate-entry.md.
3. `prepare-fixture.py` copied L1/captures into the clone, copied the supplied attempt-3 planted file to sandbox `planted.md` and clone `.ufo/waves/round-60/support/planted-rows.md`, and copied the frozen counter to the new probe file.
4. Ran the actual frozen packet builder from the clone:

```text
timeout 120 env PYTHONDONTWRITEBYTECODE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/tmp UV_CACHE_DIR=/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/uv-cache python3 -B reports/round-60/build-packets.py /fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/planted.md /fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/clone/.ufo/waves/round-60/support
cited=47 planted_rows=16 seats=24 planted_per_seat_min=2
```

5. `make-fixture.py all-true`, followed by the frozen/probe pair, then `make-fixture.py honest-shaped-positive`, followed by the frozen/probe pair. These scripts were each run with `timeout 60 env PYTHONDONTWRITEBYTECODE=1 python3 -B`, from this sandbox. The script creates fixture data only; its synthetic tool calls are never executed.
6. Both support-directory snapshots and per-seat hashes are preserved in `cases/all-true/support/`, `cases/all-true/summary.json`, `cases/honest-shaped-positive/support/`, and `cases/honest-shaped-positive/summary.json`. The clone and `sessions-active/` finish on the positive. No fixture bytes were written to real session storage or to real support paths.

Shared hashes in both fixtures:

```text
entry_sha256=0073da7ed7e0d51a158360771505739903a8024d095452f96409ece58302e5e0
planted-key.json sha256=520face229f2e40e52665d1de1a6207554446dcd2c6469e1321f422f3f64c383
planted-rows.md sha256=1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682
frozen accept-d.py sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc
probe sha256=429a5e09688a0a7701b45a313cf5b0473daf0c5704ca3e0f08359f7b8fbdba27
```

The required planted-key.sha256 and planted-rows.sha256 files were written inside the clone. Their production commit timing is not claimed by a synthetic fixture.

## Complete probe diff

`timeout 30 diff -u clone/reports/round-60/accept-d.py accept-d-probe.py` exited 1 (expected: one difference). Full diff:

```diff
--- /fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/clone/reports/round-60/accept-d.py	2026-10-23 04:03:16.375711199 -0300
+++ /fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/accept-d-probe.py	2026-10-23 04:05:05.182844661 -0300
@@ -191,7 +191,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/sessions-active/KotodamaR60A3.{seat}.jsonl"  # revision 5
 
 
 def tool_calls(transcript):
```

## Every counter run: full stdout and exit code

Each run's cwd was `/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/clone`. The same two commands were used once per fixture, with these exact environment settings; `UV_OFFLINE=1` also prevents dependency resolution from making a network request during scoring:

```text
timeout 600 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/tmp UV_CACHE_DIR=/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/uv-cache python3 -B reports/round-60/accept-d.py; echo exit=$?
timeout 600 env PYTHONDONTWRITEBYTECODE=1 UV_OFFLINE=1 TMPDIR=/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/tmp UV_CACHE_DIR=/fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/uv-cache python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3/accept-d-probe.py; echo exit=$?
```

### Run 1 — all-true / frozen

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

### Run 2 — all-true / SESSIONS-only probe

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

### Run 3 — honest-shaped-positive / frozen

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

### Run 4 — honest-shaped-positive / SESSIONS-only probe

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

No stderr was displayed for any of the four counter runs. Full long SUPPORT lines were recovered from the original tool artifacts, not rerun or abbreviated.

## Bounds and dependency record

- Dependency provisioned for the frozen locator: **pypdf 5.4.0**, via `uv run --no-project --quiet --with pypdf==5.4.0`, with UV_CACHE_DIR and TMPDIR confined to this sandbox. Reason: PINNED's PDF-to-text conversion. Provisioning command used `python3 -B --version` and returned `Python 3.15.0`. No system package transaction or host-service change was made.
- All directly invoked Python commands used `python3 -B` and PYTHONDONTWRITEBYTECODE=1. The frozen locator's unchanged internal Python invocation inherits PYTHONDONTWRITEBYTECODE=1.
- Final bounded sandbox size: **149,593,885 bytes**, from `timeout 30 du -sb /fast/scratch/hyaku/kotodama-r60a3/CtlRubberStampA3`; below 200 MB. No appending loops or background jobs were used. All foreground commands exited; no service or reviewer process was started.
- The only lane write is this assigned report. All other writes were inside this seat's sandbox. No live support directories, real session files, lane git/jj state, canonical counter, or inherited L1 artifacts were modified.
