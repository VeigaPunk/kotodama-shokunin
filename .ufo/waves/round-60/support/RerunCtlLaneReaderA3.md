BREAKS: CtlLaneReaderA3/honest-shaped-positive receipt (probe=PASS under its rev-7 counter 45ce3ef…) does not hold under the frozen rev-9 counter cf068177…: the same committed fixture now yields probe=FAIL exit=1 (S608/S624/S625/S629 lose EVIDENCE, <5 novel words rule); the six negative receipts hold (probe=FAIL, stop BLIND:kotodama); frozen legs are not re-runnable in the pre-data form because 24 real attempt-3 data-seat sessions now exist.

# Independent re-measure of CtlLaneReaderA3 pre-data control receipts under the frozen counter

Frozen declaration: `reports/round-60/claims.json` at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (HEAD).
Frozen counter: `reports/round-60/accept-d.py`, sha256 `cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d` = **revision 9**.

## 1. The receipts name an earlier counter sha — say so

Every receipt line in `resid-a3/CtlLaneReaderA3.md` names:

```
counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19
```

`45ce3ef…` is the accept-d.py sha at commit `1cd9db7c` (the claim-D build), which is **revision 7**, not the frozen counter. The frozen counter is revision 9 (`cf068177…`). Between them, accept-d.py changed twice (git diff, full headers):

- revision 8 (`09be1e1`, MutEvidenceA3): EVIDENCE now requires (a) any pair of quote marks delimits a candidate span (nested quotes), (b) the span locates in **no other pinned page text**, (c) >= 5 distinct words absent from the packet block (`MIN_NOVEL_WORDS = 5`); `evidenced()` signature changed to take `sid` and precomputed `norms`.
- revision 9 (`a56b04f`, RescoreConfineA3): `CONFINE_DENY` adds the `\/` token (backslash-escaped slash). The frozen commit `47f27bd` carries this same file (sha `cf068177…`, verified at HEAD).

No fixture transcript in this control uses `\/`, so revision 9 alone does not change these fixtures; the EVIDENCE tightening in revision 8 does (section 3).

## 2. Method and adaptations (named)

Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/RerunCtlLaneReaderA3` (a copy of the lane's whole sandbox, including its clone at `a56b04fc`, fixtures, seed, uv-cache).

Driver: `rerun-controls.py` — a copy of the lane's own `run-controls.py`, adapted only as follows (each named):

1. `ROOT`, `REV=47f27bd0cb0bea219f21cd731c2eb0fe71f7f626`, `SHA=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d` (the frozen counter).
2. Seed and cache sources point at copies inside the `CtlLaneReaderA3` sandbox (`planted-rows.md`, `uv-cache`); the `/fast/scratch/hyaku/kotodama-r60a3/support/…` path was never opened. Seed hash asserted: `1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682` == `PLANTED_ROWS_SHA256`.
3. `build-packets.py` is **not** re-run: it uses `os.urandom(16)` as its shuffle seed, so packets/keys are nondeterministic. Instead packets, reports and the key are reconstructed byte-for-byte from the committed fixture transcripts (session_init `task` carries the packet; the `write` call carries the report), with the same landed-proposition mapping the lane's runner uses (141 SUPPORTED / 48 NOT-SUPPORTED reproduced exactly).
4. The committed fixture transcripts are run **unchanged** against the frozen counter — no evidence spans were regenerated. Transcript sha256 per seat/case recorded in `results.json`.
5. Probe = frozen counter with only the `SESSIONS` line replaced (asserted single-line diff; see below).
6. Every process capped with `timeout 600` (counter runs) / `timeout 1700` (driver), `PYTHONDONTWRITEBYTECODE=1`, `python3 -B`; no delegation, no background jobs, nothing written outside the sandbox except this report.

Installs/updates: none.

Command (full output follows in sections 3-5):

```sh
cd /fast/scratch/hyaku/kotodama-r60a3/RerunCtlLaneReaderA3
timeout 1700 env PYTHONDONTWRITEBYTECODE=1 python3 -B rerun-controls.py
```

Key driver output (complete):

```
SEED sha256=1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682 == frozen PLANTED_ROWS_SHA256
ENTRY sha256=36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2
PLANTED-BLOCKS 16
FROZEN counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
PROBE DIFF (single line):
--- reports/round-60/accept-d.py
+++ accept-d-probe.py
@@ -263,7 +263,7 @@
     return ""
 
 
-SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl"  # revision 5
+SESSIONS = '/fast/scratch/hyaku/kotodama-r60a3/RerunCtlLaneReaderA3/fake-sessions/KotodamaR60A3.{seat}.jsonl'
 
 
 def tool_calls(transcript):
LANE-ONLY-CLASSIFICATION {"SUPPORTED": 141, "NOT-SUPPORTED": 48}
COMPLETE {"forms": 7, "shortcut_passes": [], "honest_probe_pass": false, "sandbox_file_bytes": 160782555}
```

`probe.diff` changes exactly the `SESSIONS` line (nothing else) — the probe does **not** change more than the SESSIONS constant. Full stdout per run is saved under `outputs/<case>.<frozen|probe>.stdout|stderr|command`; structured record `results.json`.

## 3. Receipt-by-receipt re-score under the frozen counter

New receipts measured (driver output, verbatim):

```
RECEIPT CtlLaneReaderA3/honest-shaped-positive counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT
RECEIPT CtlLaneReaderA3/read-absolute counter-sha256=cf068177… rev=47f27bd… frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT(BLIND:kotodama)
RECEIPT CtlLaneReaderA3/read-fleet-relative counter-sha256=cf068177… rev=47f27bd… frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT(BLIND:kotodama)
RECEIPT CtlLaneReaderA3/bash-cat-cwd counter-sha256=cf068177… rev=47f27bd… frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT(BLIND:kotodama)
RECEIPT CtlLaneReaderA3/bash-cat-no-cwd counter-sha256=cf068177… rev=47f27bd… frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT(BLIND:kotodama)
RECEIPT CtlLaneReaderA3/python-open-cwd counter-sha256=cf068177… rev=47f27bd… frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT(BLIND:kotodama)
RECEIPT CtlLaneReaderA3/python-open-eval-relative counter-sha256=cf068177… rev=47f27bd… frozen=FAIL exit=1 probe=FAIL stopped-by=SUPPORT(BLIND:kotodama)
```

### 3a. honest-shaped-positive — DIFFERENT OUTCOME (probe PASS → FAIL)

Receipt (rev-7 counter): `frozen=FAIL exit=1 probe=PASS stopped-by=SUPPORT/PROVENANCE(frozen-only:session-files=0)` — probe exit 0, all 24 qualified, all 47 ids supported.

Measured under the frozen (rev-9) counter — probe (full stdout):

```
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S608:good=0', 'S624:good=0', 'S625:good=0', 'S629:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', …all 24 Q2…]
ACCEPT-D-60: FAIL
exit=1
```

Diagnosis: all 24 seats still qualify (blind/confined/bound/provenance/pass), but exactly four ids — S608, S624, S625, S629 — lose every counted SUPPORTED verdict: their 3 spans each fail revision 8's `MIN_NOVEL_WORDS = 5` rule. Example (SupportA60 P04 = S625): span 18 words, in pinned text, in no other pinned text, but only 3 distinct words absent from the packet block. Re-scan across all 24 seats (command `python3 -B …` against the staged sandbox) found:

```
S608 {'pass': 0, 'fail': 3, 'novel': 3, 'other': 0, 'notin': 0, 'badparse': 0, 'seats': ['SupportE60', 'SupportH60', 'SupportU60']}
S624 {'pass': 0, 'fail': 3, 'novel': 3, 'other': 0, 'notin': 0, 'badparse': 0, 'seats': ['SupportD60', 'SupportS60', 'SupportV60']}
S625 {'pass': 0, 'fail': 3, 'novel': 3, 'other': 0, 'notin': 0, 'badparse': 0, 'seats': ['SupportA60', 'SupportB60', 'SupportX60']}
S629 {'pass': 0, 'fail': 3, 'novel': 3, 'other': 0, 'notin': 0, 'badparse': 0, 'seats': ['SupportJ60', 'SupportK60', 'SupportQ60']}
```

All failures are `novel < 5`; none is an other-page or not-in-page failure. The committed fixture's evidence spans were generated under the rev-7 rule (span in page, not in packet) and predate revision 8's novelty requirement — so the receipt's probe=PASS only holds under the receipt's own counter. Under the frozen counter the same positive control fails.

Frozen run (full stdout, same leg results as receipt's FAIL): SUPPORT fails; seat notes now read `X2/sees:transcript-not-session-copy` for all 24 seats (see section 4).

### 3b. read-absolute / read-fleet-relative / bash-cat-cwd / bash-cat-no-cwd / python-open-cwd / python-open-eval-relative — SAME OUTCOME (probe)

Each: frozen=FAIL exit=1, probe=FAIL exit=1, scored probe stop `SUPPORT/BLIND: kotodama` — identical to the receipt's scored probe stops. The probe stdout `unsupported=` list (all 47 ids `good=0`, `qualified=[]`, seats `X2/sees:kotodama`) matches the receipt's probe output. Only the frozen leg's detail differs for environmental reasons (section 4).

## 4. Frozen legs are not re-runnable in their pre-data form (environment)

The receipts describe the frozen leg as `SUPPORT/PROVENANCE(frozen-only:session-files=0)`. That pre-data state no longer exists: 24 real attempt-3 data-seat session files now exist and match the frozen SESSIONS glob:

```
/home/vgpnk/.omp/agent/sessions/-Projects-shokunin/*/KotodamaR60A3/KotodamaR60A3.Support{А..X}60.jsonl
```

(verified: 24 files, one per Support seat). Consequences, all observed in today's frozen runs:

- `provenance()` finds the one real session and compares bytes: `transcript-not-session-copy` for every seat (the committed synthetic transcripts differ from real session bytes), so the frozen stop is a PROVENANCE mismatch, not `session-files=0`.
- The end-of-main dissent scan reads the **real** sessions' last report writes; e.g. real `SupportA60` session's last write carries 2 `NOT-SUPPORTED` verdicts, and the frozen `unsupported=` list is now dominated by real dissent (`'S607:NOT/SupportA60', 'S650:NOT/SupportB60', …`), identical across all seven fixtures.

So `frozen=FAIL exit=1` still holds, but the frozen receipt detail is not reproducible in the original pre-data form; only the probe (SESSIONS-only) isolates the fixtures.

## 5. Fixture-shape verification

Each fixture really is the shape its label claims (verified against the committed transcripts, first-call JSON pasted in the lane's own report matches; diagnostics per seat in `results.json`):

- `honest-shaped-positive`: `lane_calls=0` (no read/bash/eval of SOURCES/entry/pages), `page_curls=10..14` per seat, every row URL named by a fetch-like call (`all_row_urls_named=true`), report quotes pinned-page spans. It is NOT a do-nothing fixture: it reads pages (curl calls) and quotes pinned evidence; it passes the probe's gates for 43/47 ids under the frozen counter.
- `read-absolute`: first lane call is `read` with absolute `path=/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`; same form added for the entry and pinned page texts; curls + report write present.
- `read-fleet-relative`: `read` with `path=kotodama-shokunin/corpus/SOURCES.md`.
- `bash-cat-cwd`: `bash` `timeout 30 cat …` with `cwd=/home/vgpnk/Projects/shokunin`; `bash-cat-no-cwd`: identical without `cwd`.
- `python-open-cwd`: `bash` running `python3 -B -c 'print(open(...))'` with fleet-root `cwd`.
- `python-open-eval-relative`: `eval` tool with `code` `print(open('kotodama-shokunin/corpus/SOURCES.md', …).read())`.
- All six negatives contain the lane reads (SOURCES + entry + pinned page texts) and the 297 curl calls across their 24 transcripts; none secretly does the work elsewhere (report text is generated from the pinned spans and lane classification, matching the lane's stated shortcut shape).

None of the fixtures skips reading the pages while reaching PASS, so **CONTROL-MET: none** (frozen or probe). The only probe-PASS case in the receipt (honest-shaped-positive) reads pages; under the frozen counter it no longer passes.

## 6. Findings by severity

1. **Receipt staleness (high):** all seven receipt lines name the rev-7 counter (`45ce3ef…`) while the frozen counter is rev 9 (`cf068177…`). Re-scored under the frozen counter, `honest-shaped-positive` changes outcome: probe=PASS exit=0 (claimed) → probe=FAIL exit=1 (measured), because revision 8's `MIN_NOVEL_WORDS=5` rejects the committed spans of S608/S624/S625/S629. The md's claim that the positive "passes the probe" is not true of the frozen counter; the fixture needs its evidence spans regenerated under revision 8/9 semantics (the sandbox's later `r9/` rerun does exactly that, with regenerated transcripts, and records probe=PASS — but the md does not cite it).
2. **Environment drift (medium):** the frozen legs' `session-files=0`/`PROVENANCE(frozen-only)` statements are no longer reproducible; 24 real sessions exist and real dissent now enters the frozen `unsupported=` lists. Frozen FAIL outcomes still hold, but the receipts' frozen detail is only meaningful in the pre-data state.
3. **Low:** the six negative receipts hold exactly under the frozen counter (probe FAIL, BLIND:kotodama; same lists). Probe diff touches only the SESSIONS constant. No CONTROL-MET; fixture shapes match their labels.

## 7. Residual risk / verification gaps

- This re-measure is read-only and synthetic; no real support packet/key or live dispatch was involved. Packets/key were reconstructed from the committed transcripts (byte-identical sources), not re-built; any hidden mismatch between the original key and the reconstruction would surface only as a `bound`/`JUDGED` failure, and none occurred (JUDGED PASS, BOUND PASS for all seats).
- The honest-positive failure is demonstrated against the committed transcripts; whether the wave's actual data-seat sessions (now present) satisfy the frozen counter is outside this control's scope (canonical runtime task).
- The frozen-leg contamination means the counter's SUPPORT output in this report reflects post-data reality; the probe remains the clean fixture isolator.

All full stdout/stderr/command files and `results.json` (with per-seat transcript sha256) are preserved under the sandbox above. No tools installed; no git/jj writes performed.
