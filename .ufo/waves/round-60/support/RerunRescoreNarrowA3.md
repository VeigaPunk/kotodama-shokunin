BREAKS: the stored revision-7 receipts of RescoreNarrowA3 do not reproduce under the frozen counter (47f27bd0cb0bea219f21cd731c2eb0fe71f7f626, sha256 cf068177…): the honest-shaped positive's SESSIONS-only probe flips PASS→FAIL (revision-8 EVIDENCE novelty rule kills S632/S644/S650), and the frozen legs are no longer cleanly re-runnable because real data-seat session files now exist and feed the revision-6 dissent scan.

# RerunRescoreNarrowA3 — independent re-measure of pre-data control receipts under the frozen counter

Falsify seat. Re-ran the stored RescoreNarrowA3 fixtures (the exact receipt bytes) with their own runner commands, under the FROZEN counter. Sandbox: `/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreNarrowA3/work/`. Leaf seat: no delegation, no background jobs. Time box respected. No tool installed (no pacman/uv/cargo/npm action; nothing to record).

## 1. Counter identity and earlier-counter note (assignment item)

- The receipts in `.ufo/waves/round-60/resid-a3/RescoreNarrowA3.md` name `counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19` — that is the **revision-7 counter** at the claim-D build commit `1cd9db7c` (verified: `git show 1cd9db7c:reports/round-60/accept-d.py | sha256sum` → `45ce3ef4…`).
- The frozen declaration is `reports/round-60/claims.json` at `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (commit message: "FREEZE … packet-key hash … revision-9 residual re-score receipts (NONE-MET)"). At that commit `accept-d.py` has sha256 **`cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d`** — identical to the revision-9 counter introduced at `a56b04fc`. claims.json at 47f27bd (`freeze_note`) itself states: "the counter is revision 9 (introduced at a56b04fc, sha256 cf068177…), the judged object is the entry at claim-D build 1cd9db7c (sha256 36bd628b…)". So the assignment's label "revision 8 at 47f27bd" is one step off the repo's own labels: commit 47f27bd **carries the revision-9 counter bytes** (revision 8 = `09be1e1`, r7 = `1cd9db7c`). I re-score against the bytes actually frozen at 47f27bd, i.e. cf068177. The receipts' 45ce3ef4 is an earlier counter — stated, as required.

Diff of the counter the receipts used (45ce3ef4, r7) → frozen (cf068177) — the full delta (revision 8 + revision 9), from `git diff 1cd9db7c 47f27bd -- reports/round-60/accept-d.py`:
1. Docstring/predicate extension (revision 8): EVIDENCE span must "locate in no other pinned page text", and ">= 5 distinct words absent from the packet block".
2. `EVIDENCE_SPAN` regex removed; added `MIN_NOVEL_WORDS = 5`, `QUOTE_CHARS`, `norm_forms` (plain + de-hyphenated, space-padded); `evidenced()` rewritten: any text between two double-quote marks (straight/curly, nested-quote parsing) is a candidate span; requires >=10 locator-normalised words, >=5 distinct words absent from the packet block, span in the row's pinned page (either form), not in the packet block (either form), not in any other pinned page.
3. `main()` builds `norms` for all pinned pages and calls `evidenced(evidence, sid, norms, raw_blocks, locator)`.
4. Revision 9: `CONFINE_DENY` additionally denies the token `\/` (backslash-escaped slash; RescoreConfineA3).

Adaptations made for the re-measure (only what the frozen counter requires, each named):
- (a) Copied the runner `residual-controls.py`, baseline.zip, results.json, fake-sessions, uv-cache, bin and the clone into my sandbox; changed only the constants `HOME` → my sandbox and `FROZEN_SHA` → cf068177 (the runner asserts the counter file's sha equals this constant). The clone's `accept-d.py` was already cf068177 (the original workspace's clone was updated by the later r9 activity; the runner's own assert now matches).
- (b) Regenerated the probe from the frozen counter by the **single-line SESSIONS substitution** the original `prepare()` performs (byte-for-byte replace of the frozen SESSIONS string with the sandbox fake-sessions path; assert count==1). Verified by unified diff: the regenerated probe differs from the frozen counter in exactly that one line. New probe sha256 `416211e4313850ae1887478cb9be5517bbe23edbe0b3b71ae0aaa2e882117d96` (the stored root probe `9abbe01b…` is the *r7* probe, i.e. stale relative to the frozen counter — the original workspace as left cannot rerun its own receipts: the runner's FROZEN_SHA assert fails against the current clone counter, and its probe is an r7 build).
- (c) No other edits: fixtures, mutations, scorer and baseline bytes untouched (baseline.zip sha `c442d9cb…` matches the recorded value; post-run restore verified 0 mismatches against the zip).

## 2. Environment drift discovered while re-running (affects every frozen leg)

`provenance()` globs `/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A3/KotodamaR60A3.{seat}.jsonl`. At receipt time (04:24 local) no such files existed → every seat reason was `session-files=0` and the revision-6 dissent scan found nothing, so frozen unsupported lists contained only `good=0` entries. **Now 24 real data-seat session files exist** (first written 04:53:03 local, i.e. during my rerun window; e.g. `KotodamaR60A3.SupportA60.jsonl` 209,356 B, `SupportB60.jsonl` 308,067 B, `SupportC60.jsonl` 238,882 B …). Consequences, demonstrated:
- Frozen-runs reason strings are now `transcript-not-session-copy` (sessions exist, differ from synthetic transcripts).
- The revision-6 dissent scan reads the **last write to the report path in the real session file** and injects the real data verdicts into `given`; e.g. debugging the r7 counter on the baseline state, `DEBUG-DISSENT SupportA60 P03 NOT-SUPPORTED S644 |given= [('P01','SUPPORTED'), …, ('P03','SUPPORTED'), …, ('P05','NOT-SUPPORTED'), ('P06','NOT-SUPPORTED'), ('P07','SUPPORTED'), ('P01','SUPPORTED'), ('P02','SUPPORTED'), ('P03','NOT-SUPPORTED'), ('P04','SUPPORTED'), ('P05','NOT-SUPPORTED'), ('P06','SUPPORTED'), ('P07','SUPPORTED')]` — the second block is the real session's last-write report (P03 NOT), not the synthetic fixture.
- Hence frozen-mode outputs now contain `Sxxx:NOT/<Seat>` entries even for the honest positive, and are functions of live data-seat state. **They are not re-runnable as isolated fixture measurements without modifying/unlinking real session files, which is forbidden** (never write under /home/vgpnk/.omp). I state this rather than pretending the frozen leg is clean. The probe legs are isolated (fake-sessions only) and are the meaningful re-measure.

## 3. Receipt-by-receipt re-measure (probe = isolated; frozen = contaminated as above)

Commands used for each case (identical shape to the original runner): `cd /fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreNarrowA3/work && timeout 180 env PYTHONDONTWRITEBYTECODE=1 python3 -B residual-controls.py <case>`. Full captured outputs are preserved byte-for-byte in `/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreNarrowA3/work/logs/<case>.stdout|stderr` (stderr empty for every run). The normalized diff against the original stored `outputs/<case>.<kind>.stdout` (stripping only the runner headers `cwd=/command=`/`exit=`/`stderr=`) gives the per-kind deltas below. RECEIPT lines in the original receipts (`rev=1cd9db7c`, counter 45ce3ef4) vs my rerun (counter cf068177):

| Case | Original (r7 counter) | My rerun (frozen counter cf068177) | Verdict |
|---|---|---|---|
| honest-shaped | frozen FAIL/1; probe PASS/0 | frozen FAIL/1 (contaminated; extra NOT entries, reasons transcript-not-session-copy); probe **FAIL/1** | **DIFFERENT** (probe PASS→FAIL; frozen not cleanly re-runnable) |
| dissent-seed | frozen FAIL/1; probe FAIL/1 [`S648:NOT/SupportP60`] | frozen FAIL/1 (contaminated); probe FAIL/1 [`S648:NOT/SupportP60`, `S632:good=0`, `S644:good=0`, `S650:good=0`] | same FAIL outcome; probe detail extended |
| a-delete-line-and-row | FAIL/FAIL | FAIL/FAIL | **SAME** body (SET,LINES,ROWS,PINNED,JUDGED,SUPPORT all fail, exit 1, byte-identical stdout) |
| b-reword-line | FAIL/FAIL | FAIL/FAIL | **SAME** body (JUDGED entry-hash mismatch + SUPPORT, exit 1) |
| c-rekey-edited-entry | FAIL/FAIL | FAIL/FAIL | same outcome; SUPPORT list differs because the fixture's own `build-packets.py` re-randomizes label↔sid assignment on each rebuild (both runs: 21 seats `bash-url-not-in-packet` — CONFINED mechanism reproduced) |
| c2-stable-rekey | FAIL/FAIL | FAIL/FAIL | **SAME** body (all 24 seats `packet-not-in-dispatched-task` = BOUND isolated; exit 1) |
| d-rewrite-landed-report | FAIL/FAIL | frozen FAIL/1 (contaminated); probe FAIL/1 [`S648:NOT/SupportP60` + 3 good=0] | same FAIL; `SupportP60:X2/sees:report-not-its-own-write` reproduced |
| e-drop-dissenting-member | FAIL/FAIL | frozen FAIL/1 (contaminated); probe FAIL/1 [`S648:NOT/SupportP60`, `roster` + 3 good=0] | same FAIL; `roster-not-the-frozen-24` reproduced |
| f-add-25th-member | FAIL/FAIL | frozen FAIL/1 (contaminated); probe FAIL/1 [`roster` + 3 good=0] | same FAIL; roster-only reason reproduced |
| f2-add-25th-dissenter | FAIL/FAIL | frozen FAIL/1 (contaminated); probe FAIL/1 [`roster` + 3 good=0] | same FAIL; roster-only reason reproduced |
| g-delete-dissenting-report | FAIL/FAIL | frozen FAIL/1 (contaminated); probe FAIL/1 [`S648:NOT/SupportP60` + 3 good=0] | same FAIL; `SupportP60:missing` reproduced, original session verdict still read |

Pasted receipt pairs (original vs mine) for every line:

honest-shaped
```
RECEIPT RescoreNarrowA3/honest-shaped counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=PASS stopped-by=frozen:SUPPORT;probe:none probe-exit=0
RECEIPT RescoreNarrowA3/honest-shaped counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
dissent-seed
```
RECEIPT RescoreNarrowA3/dissent-seed counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/dissent-seed counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
a-delete-line-and-row
```
RECEIPT RescoreNarrowA3/a-delete-line-and-row counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT;probe:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/a-delete-line-and-row counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT;probe:SET,LINES,ROWS,PINNED,JUDGED,SUPPORT probe-exit=1
```
b-reword-line
```
RECEIPT RescoreNarrowA3/b-reword-line counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:JUDGED,SUPPORT;probe:JUDGED,SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/b-reword-line counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:JUDGED,SUPPORT;probe:JUDGED,SUPPORT probe-exit=1
```
c-rekey-edited-entry
```
RECEIPT RescoreNarrowA3/c-rekey-edited-entry counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/c-rekey-edited-entry counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
c2-stable-rekey
```
RECEIPT RescoreNarrowA3/c2-stable-rekey counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/c2-stable-rekey counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
d-rewrite-landed-report
```
RECEIPT RescoreNarrowA3/d-rewrite-landed-report counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/d-rewrite-landed-report counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
e-drop-dissenting-member
```
RECEIPT RescoreNarrowA3/e-drop-dissenting-member counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/e-drop-dissenting-member counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
f-add-25th-member
```
RECEIPT RescoreNarrowA3/f-add-25th-member counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/f-add-25th-member counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
f2-add-25th-dissenter
```
RECEIPT RescoreNarrowA3/f2-add-25th-dissenter counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/f2-add-25th-dissenter counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```
g-delete-dissenting-report
```
RECEIPT RescoreNarrowA3/g-delete-dissenting-report counter-sha256=45ce3ef43d11686a41a36ab752541a99f561a665cfd209633ceeb7cf88137d59 rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
RECEIPT RescoreNarrowA3/g-delete-dissenting-report counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```

## 4. The different outcome, isolated: honest-shaped probe PASS → FAIL

Full rerun output (frozen + probe), honest-shaped (fresh restore from the same baseline bytes):

```
=== honest-shaped / frozen ===
cwd=/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreNarrowA3/work/clone
command=timeout 45 python3 -B reports/round-60/accept-d.py
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S644:NOT/SupportA60', 'S635:NOT/SupportC60', 'S644:NOT/SupportC60', 'S624:NOT/SupportE60', 'S645:NOT/SupportF60', 'S619:NOT/SupportF60', 'S647:NOT/SupportG60', 'S634:NOT/SupportH60', 'S600:NOT/SupportL60', 'S649:NOT/SupportM60', 'S605:NOT/SupportM60', 'S647:NOT/SupportN60', 'S621:NOT/SupportN60', 'S638:NOT/SupportN60', 'S603:NOT/SupportN60', 'S633:NOT/SupportO60', 'S607:NOT/SupportO60', 'S613:NOT/SupportQ60', 'S648:NOT/SupportQ60', 'S629:NOT/SupportS60', 'S601:NOT/SupportS60', 'S636:NOT/SupportT60', 'S600:NOT/SupportT60', 'S625:NOT/SupportV60', 'S607:NOT/SupportV60', 'S626:NOT/SupportW60', 'S651:NOT/SupportW60', 'S617:NOT/SupportW60', 'S642:NOT/SupportW60', 'S600:good=0', 'S601:good=0', 'S603:good=0', 'S604:good=0', 'S605:good=0', 'S607:good=0', 'S608:good=0', 'S609:good=0', 'S610:good=0', 'S611:good=0', 'S612:good=0', 'S613:good=0', 'S614:good=0', 'S615:good=0', 'S617:good=0', 'S618:good=0', 'S619:good=0', 'S620:good=0', 'S621:good=0', 'S622:good=0', 'S624:good=0', 'S625:good=0', 'S626:good=0', 'S627:good=0', 'S628:good=0', 'S629:good=0', 'S630:good=0', 'S631:good=0', 'S632:good=0', 'S633:good=0', 'S634:good=0', 'S635:good=0', 'S636:good=0', 'S637:good=0', 'S638:good=0', 'S639:good=0', 'S640:good=0', 'S641:good=0', 'S642:good=0', 'S644:good=0', 'S645:good=0', 'S646:good=0', 'S647:good=0', 'S648:good=0', 'S649:good=0', 'S650:good=0', 'S651:good=0'] qualified=[] seats=['SupportA60:X2/sees:transcript-not-session-copy', 'SupportB60:X2/sees:transcript-not-session-copy', 'SupportC60:X2/sees:transcript-not-session-copy', 'SupportD60:X2/sees:transcript-not-session-copy', 'SupportE60:X2/sees:transcript-not-session-copy', 'SupportF60:X2/sees:transcript-not-session-copy', 'SupportG60:X2/sees:transcript-not-session-copy', 'SupportH60:X2/sees:transcript-not-session-copy', 'SupportI60:X2/sees:transcript-not-session-copy', 'SupportJ60:X2/sees:transcript-not-session-copy', 'SupportK60:X2/sees:transcript-not-session-copy', 'SupportL60:X2/sees:transcript-not-session-copy', 'SupportM60:X2/sees:transcript-not-session-copy', 'SupportN60:X2/sees:transcript-not-session-copy', 'SupportO60:X2/sees:transcript-not-session-copy', 'SupportP60:X2/sees:transcript-not-session-copy', 'SupportQ60:X2/sees:transcript-not-session-copy', 'SupportR60:X2/sees:transcript-not-session-copy', 'SupportS60:X2/sees:transcript-not-session-copy', 'SupportT60:X2/sees:transcript-not-session-copy', 'SupportU60:X2/sees:transcript-not-session-copy', 'SupportV60:X2/sees:transcript-not-session-copy', 'SupportW60:X2/sees:transcript-not-session-copy', 'SupportX60:X2/sees:transcript-not-session-copy']
ACCEPT-D-60: FAIL
exit=1
stderr=''
=== honest-shaped / probe ===
cwd=/fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreNarrowA3/work/clone
command=timeout 45 python3 -B /fast/scratch/hyaku/kotodama-r60a3/KotodamaR60A3.RerunRescoreNarrowA3/work/accept-d-probe.py
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL unsupported=['S632:good=0', 'S644:good=0', 'S650:good=0'] qualified=['SupportA60', 'SupportB60', 'SupportC60', 'SupportD60', 'SupportE60', 'SupportF60', 'SupportG60', 'SupportH60', 'SupportI60', 'SupportJ60', 'SupportK60', 'SupportL60', 'SupportM60', 'SupportN60', 'SupportO60', 'SupportP60', 'SupportQ60', 'SupportR60', 'SupportS60', 'SupportT60', 'SupportU60', 'SupportV60', 'SupportW60', 'SupportX60'] seats=['SupportA60:Q2', 'SupportB60:Q2', 'SupportC60:Q2', 'SupportD60:Q2', 'SupportE60:Q2', 'SupportF60:Q2', 'SupportG60:Q2', 'SupportH60:Q2', 'SupportI60:Q2', 'SupportJ60:Q2', 'SupportK60:Q2', 'SupportL60:Q2', 'SupportM60:Q2', 'SupportN60:Q2', 'SupportO60:Q2', 'SupportP60:Q2', 'SupportQ60:Q2', 'SupportR60:Q2', 'SupportS60:Q2', 'SupportT60:Q2', 'SupportU60:Q2', 'SupportV60:Q2', 'SupportW60:Q2', 'SupportX60:Q2']
ACCEPT-D-60: FAIL
exit=1
stderr=''
REECEIPT RescoreNarrowA3/honest-shaped counter-sha256=cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d rev=1cd9db7cdc83fd41f5d04cd620af879555442f19 frozen=FAIL exit=1 probe=FAIL stopped-by=frozen:SUPPORT;probe:SUPPORT probe-exit=1
```

Why: all 24 seats still qualify under the probe (the fixture is genuinely page-reading), but under the frozen counter's revision-8 EVIDENCE rule three rows — S632, S644, S650 — fall below 2 counted SUPPORTED seats (`good=0`). Running the frozen counter's `evidenced` (with the same `norms`/`QUOTE_CHARS` logic) over all 141 recorded evidence spans: 9 spans fail, all on these three rows (3 seats each), all for the **novelty** condition (`len(set(words)-block_words) < 5`): e.g. `SupportE60/P01` on S632 ("while others can only be activated by reading the text writt…"), `SupportA60/P03` on S644 ("the definition of charm is very similar anything worn about …"), `SupportO60/P02` on S650 ("and that they were connected to notions of good luck and hop…"). The spans are genuinely in the pinned page text (r7-valid), but they are built from packet words (the quote/teaches/entry fields restate them), so the frozen counter rejects them. This is precisely the leak revision 8 closed; the stored r7-era positive was not rebuilt for it. Net: the stored "honest-shaped probe PASS" receipt is false under the frozen counter.

Counter-check on the seed dependence: the directory `/fast/scratch/hyaku/kotodama-r60a3/RescoreNarrowA3/r9/` contains a later "revision-9" rerun of these controls whose baseline.zip differs in 74 of 79 files (packets, planted-key.json, key sha, all reports, all transcripts; target seat/label changed from SupportP60/P06 to SupportJ60/P04) — i.e. it re-*built* the fixtures with a new random seed rather than re-running the stored receipt bytes, and its honest-shaped probe PASSes. So passing under the frozen counter is seed-dependent for this generator; the exact stored fixtures fail.

## 5. Fixture shape claims (assignment item)

Verified by reading the runner (`residual-controls.py`) mutation paths and the recorded `changes_from_seed` hashes; no fixture is do-nothing and none secretly does the work it claims not to do:
- honest-shaped: genuine page-reading positive (EVIDENCE spans located in pinned pages; 141 SUPPORTED, 48 planted NOT-SUPPORTED; 300 synthetic curl calls) — but, as above, not conformant to revision-8 evidence.
- dissent-seed: flips SupportP60/P06 (S648) to NOT-SUPPORTED in BOTH the committed report and the last-write session event (`dissent()` replaces the report line and events[-1] content).
- a: deletes exactly the one S648 entry line and the one `| S648 |` SOURCES row (asserts count==1 each); packets/sessions untouched.
- b: replaces exactly the one phrase "The IDD article describes Pazuzu" → "… explicitly describes …" (assert count==1).
- c: b + reruns the official `build-packets.py` and refreshes planted-key.sha256 (random reassignment → CONFINED `bash-url-not-in-packet` on 21 seats).
- c2: b + rewrites `entry_sha256` in key and packet headers/entry text only; label→URL mapping untouched (isolates BOUND; all 24 `packet-not-in-dispatched-task`).
- d: only SupportP60.md's P06 line restored to SUPPORTED; session write stays NOT (reproduces `report-not-its-own-write`).
- e: only registry.json drops the dissenting member (24→23) — report/session/transcript/packet/key intact (`roster-not-the-frozen-24`).
- f: registry.json appends AdditionalReviewer60 (24→25) on the passing positive; nothing else (`roster` only).
- f2: f + full packet/key mapping/report/adapted synthetic session for the extra seat; key sha refreshed; original 24 stay positive (`roster` only).
- g: unlinks only SupportP60.md; session and transcript retain the NOT verdict (probe shows `SupportP60:missing` while `S648:NOT/SupportP60` persists).
- Probe-vs-frozen: for BOTH the stored pair (45ce3ef4 vs 9abbe01b) and my regenerated pair (cf068177 vs 416211e4…), the probe differs from its counter in exactly one byte line — the SESSIONS constant. No probe changed more than the SESSIONS constant.

## 6. CONTROL-MET

NONE. No fixture that skips reading the pages reaches PASS under the frozen counter or the SESSIONS-only probe. The only probe PASS in the stored receipts (honest-shaped) is not a page-skipper, and it no longer passes under the frozen counter. All other probes fail as before. (`NONE-MET` headline of the source report remains correct, but for a different reason than its stored runs show.)

## 7. Residual risk / verification gaps

- Frozen legs of ALL receipts are no longer independently re-measurable in isolation (live data-seat sessions contaminate the dissent scan; cannot be moved or read as data without touching /home/vgpnk/.omp, which is forbidden). Receipt-time frozen values (session-files=0, no NOT entries) are therefore not reproducible as-is; only the probe legs are isolated.
- The `c` case is not byte-reproducible by design (random rebuild). Its receipt's *mechanism* (CONFINED, 21 seats) reproduced.
- Judgment on whether the honest-shaped failure is a defect of the counter or of the fixture: the frozen counter implements exactly its declared revision-8 predicate; the stored positive's evidence was generated under revision 7's weaker rule. The fixture generator is the part that did not keep pace; the stored receipt is stale.
- No claim judgment is made; this is a falsify/measure report only.
