NONE-MET

# CtlDoNothingA3 — revision-5 pre-data do-nothing controls

## Axes and result

- **Depth:** no proposition, source row or capture is repaired by any fixture.
- **Calibration:** test whether unchanged bytes, bookkeeping assertions or an empty support directory can masquerade as measured work.
- **Observed:** all three fixtures print `ACCEPT-D-60: FAIL`, exit 1, under both the frozen counter and the SESSIONS-only probe. Each fails **SET, LINES, ROWS, PINNED, JUDGED, SUPPORT**; OLDWORD passes.
- This is evidence only about these controls, not an admission, a claim-wide verdict, or evidence that the inherited candidate is source-supported.

```text
RECEIPT CtlDoNothingA3/a-base counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SET,LINES,ROWS,PINNED,JUDGED,SUPPORT
RECEIPT CtlDoNothingA3/b-records-only counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SET,LINES,ROWS,PINNED,JUDGED,SUPPORT
RECEIPT CtlDoNothingA3/c-empty-support counter-sha256=b6389454bbdf1115d36c35486ba2628f7f8072127562f7ffc26df5078b450cdc rev=14e6413820d482913f723432b62d566967ccd1a6 frozen=FAIL exit=1 probe=FAIL stopped-by=SET,LINES,ROWS,PINNED,JUDGED,SUPPORT
```

Probe counter sha256: `2e5d6c0924cc263ef7179178bfde5af17dd0092ccefc25f7c203a7894122965b`. All three probe exits are 1. Frozen hash was asserted before every invocation.

## Counterexample construction and evidence

The strongest assigned attempt is **(c)**: start with the unchanged claim base, add a SCORECARD row claiming PASS plus an explanatory LOG entry and lesson, then create an apparently available support directory whose sole file is a valid, empty registry (`{"members": []}`). It produces neither the claimed depth repair nor any review evidence. It does **not** fool revision 5.

One private clone was checked out at `14e6413820d482913f723432b62d566967ccd1a6`. Cases were measured sequentially, with complete file-content inventories asserting the exact changes between cases:

| Case | Changes relative to previous case | Frozen | Probe | Failing legs |
|---|---|---|---|---|
| (a) `a-base` | None; clone at revision 5, entry at base | FAIL / 1 | FAIL / 1 | SET, LINES, ROWS, PINNED, JUDGED, SUPPORT |
| (b) `b-records-only` | Append one SCORECARD row, one LOG entry; add one lesson file | FAIL / 1 | FAIL / 1 | Same six |
| (c) `c-empty-support` | Add only `.ufo/waves/round-60/support/registry.json`, with empty members | FAIL / 1 | FAIL / 1 | Same six |

Case (b)'s changed paths are exactly `SCORECARD.md`, `LOG.md`, `corpus/lessons/round-60-records-only-control.md`. The SCORECARD addition is:

```text
| depth | CONTROL ONLY: records-only assertion, not a measured verdict | Round 60 ACCEPT-D-60 claimed PASS without any entry or source edits | python3 -B reports/round-60/accept-d.py | corpus/lessons/round-60-records-only-control.md |
```

The LOG and lesson explicitly identify this as a negative-control assertion, not real completed work. Their full additions are retained in `records-only-additions.json` in this seat's sandbox. No packet, report, transcript, key, planted row, capture or source row was added. Case (c)'s support directory contains only the empty registry; no material was borrowed from a real review wave.

Entry sha256 before and after all cases: `4e1bef48db9cbab07bb218f3b586ff2cc2e5f3b9e923f5ccb603c0afcc9e9d3d`.
SOURCES sha256 before and after: `35627babb0e3182f8d548cdd0ca71a461eceeadaaeff81511465b325555cc64b`.

The failures have distinct, observed causes:

- **SET:** entry still cites 43 ids; all four new ids are absent.
- **LINES:** no line cites any new id.
- **ROWS:** all four superseding rows are absent.
- **PINNED:** manifest absent and no row/manifest for any new id.
- **JUDGED:** missing key/hash material prevents judged-object binding.
- **SUPPORT:** zero qualified seats and zero counted support for each of the 43 currently cited ids. Creating the empty registry only removes the `no-registry:FileNotFoundError` diagnostic; it does not create support.
- **OLDWORD PASS** means only that the base does not contain the frozen over-reach phrases; it is not evidence of restored depth.

The counter evaluates and prints every leg rather than short-circuiting on SET. No seat reaches PROVENANCE in these fixtures: none has a registered member, report, packet or transcript. Therefore the probe demonstrates continued rejection with the provenance location changed, **not** strength of the provenance, confinement or binding checks themselves.

## Smallest safe correction

No counter correction is indicated by these three controls. Retain their FAIL receipts and keep records-only assertions and directory presence non-authoritative. Do not infer saturation or candidate correctness from these expected failures. There is no observed depth/calibration tradeoff here requiring a different admission rule.

## Reproduction and probe diff

Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/CtlDoNothingA3/`.

Artifacts: `run-controls.py` (fixture construction and bounded invocations), `receipts.json` (every stdout/stderr/exit/hash), `summary.json` (inventory deltas and hashes), `records-only-additions.json`, `probe.diff`, `accept-d-probe.py`, private `clone/`. The fake-session directory is empty. No session file under the operator's home was written.

Setup executed successfully:

```sh
timeout 180 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r60a3/CtlDoNothingA3/clone
timeout 60 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotodama-r60a3/CtlDoNothingA3/clone checkout -q 14e6413820d482913f723432b62d566967ccd1a6
timeout 600 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlDoNothingA3/run-controls.py
```

Outer commands ran from this seat's sandbox. Each counter subprocess ran from its private `clone/`, with default root `.` and its own 600-second timeout. The runner performs (a), then creates (b), then creates (c); its final clone is case (c), so a fresh reproduction starts from a fresh private checkout.

The probe changes exactly one assignment:

```diff
--- frozen/reports/round-60/accept-d.py
+++ probe/accept-d.py
@@ -191,7 +191,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = "/fast/scratch/hyaku/kotodama-r60a3/CtlDoNothingA3/fake-sessions/KotodamaR60A3.{seat}.jsonl"  # probe only
 
 
 def tool_calls(transcript):
```

## Full counter outputs

No counter run is omitted below. All six stderr streams were empty. Frozen command for each case, cwd private `clone/`:

```sh
timeout 600 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlDoNothingA3/clone/reports/round-60/accept-d.py
```

Probe command for each case, same cwd:

```sh
timeout 600 env PYTHONDONTWRITEBYTECODE=1 python3 -B /fast/scratch/hyaku/kotodama-r60a3/CtlDoNothingA3/accept-d-probe.py
```

### (a) Frozen

```text
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

### (a) Probe

```text
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

### (b) Frozen

```text
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

### (b) Probe

```text
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-registry:FileNotFoundError no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

### (c) Frozen

```text
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

### (c) Probe

```text
SET FAIL cited=43 want=47 missing=['S648', 'S649', 'S650', 'S651'] extra=[] retired_cited=[]
LINES FAIL bad=['S648:lines=0 base_line=False', 'S649:lines=0 base_line=False', 'S650:lines=0 base_line=False', 'S651:lines=0 base_line=False']
OLDWORD PASS present=[]
ROWS FAIL bad=['S648:rows=0 registry=None', 'S649:rows=0 registry=None', 'S650:rows=0 registry=None', 'S651:rows=0 registry=None']
PINNED FAIL bad=['manifest:FileNotFoundError', 'S648:no-row-or-manifest', 'S649:no-row-or-manifest', 'S650:no-row-or-manifest', 'S651:no-row-or-manifest']
JUDGED FAIL no-key:FileNotFoundError
SUPPORT FAIL unsupported=['S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0'] qualified=[] seats=[] no-planted-rows:FileNotFoundError
ACCEPT-D-60: FAIL
exit=1
```

## Bounds

No tools installed or updated. No external pages fetched, no browser, no additional runtime, no delegation, no background jobs. All shell work was timeout-bounded in this seat's sandbox or its private clone; all Python runs used `PYTHONDONTWRITEBYTECODE=1` and `python3 -B`. Sandbox footprint measured 164 MiB (`du -sm`), below 200 MB. All started commands returned synchronously. The only lane file written by this seat is this report.
