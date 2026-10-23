# Round 61 W1 — ScribeMistakes

## Scope and evidence status

Read first: `reports/round-61/claims.json`; then `corpus/QUALITY.md` criteria 1–14, lessons and verifier spot-checks for rounds 58–60, the filed round-60 report, and its committed `reports/round-60/telemetry/final-measure.txt` receipt. The report below is a text-only intake for round 61's `## Mistakes`; it does not edit the lesson or QUALITY.md.

At inspection, `corpus/lessons/round-61.md` and `tools/check-cited-lines.py` were absent. The O contract is documented in `reports/round-61/accept-o.py:7-16,30-32`, but its tool has not been run here. W5 below is an inline diagnostic, not output from that tool. No acceptance/build/lint gate or counter was run, no tool was installed, and no product or lesson file was changed. The five timeout-capped commands below are read-only witnesses requested for these proposed fixes.

## Proposed `## Mistakes` rows

| id | class | evidence pointer (path:line) | captured-by (criterion/rule or none) | fix (and how it is shown able to fail) |
|---|---|---|---|---|
| R61-M1 | report arithmetic and status not reconciled to committed evidence | `.ufo/reports/round-60/kotodama.md:14,46,61`; `corpus/lessons/round-60-verifier-spotcheck.md:38-40`; recurrent report-count defects: `corpus/lessons/round-58.md:117`, `corpus/lessons/round-59.md:117-118` | none in QUALITY 1–14 or an identified mechanical report check; the round-60 spot-check caught these after filing | Before filing, derive report figures and seat/control classifications from committed receipts and assert them instead of transcribing them; W2–W4 fail on the round-60 report and receipt. |
| R61-M2 | report structure omission | `.ufo/reports/round-60/kotodama.md:48-59`; `corpus/lessons/round-60-verifier-spotcheck.md:37,144` | none in QUALITY 1–14 or an identified tool | Add a closeout assertion requiring the `## Gate` heading in its required location; W1 counts zero such headings in the filed round-60 report and exits 1. |
| R61-M3 | cited clauses cross-contaminated by other ids and table cells | `corpus/lessons/round-60.md:56`; `corpus/lessons/round-60-verifier-spotcheck.md:117,145`; `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:49-55,95` | none in QUALITY 1–14 or a tool present at inspection; intended round-61 tool not yet present | Enforce one distinct S-id per cited knowledge line and no S-id in a table row with `tools/check-cited-lines.py`; W5 finds the S612/S613 line and seven cited table rows in the round-60 entry, exiting 1. |

## Draft QUALITY criterion 15 (not applied)

15. **Cited lines are clause-scoped** — each cited knowledge line carries exactly one distinct S-id, and no table row carries an S-id; check with `python3 -B tools/check-cited-lines.py corpus/knowledge` once the tool lands. Grounded in R60-M6 (`corpus/lessons/round-60.md:56`; verifier confirmation at `corpus/lessons/round-60-verifier-spotcheck.md:117,145`); W5 is a local failing witness, not a run of the tool.

## Failing witnesses

All were run from `/home/vgpnk/Projects/shokunin` under `timeout 300`; the displayed `exit=` is the Python check's status (a shell suffix captured and printed it). Each is a deliberately failing assertion on round-60 filed bytes.

### W1 — missing `## Gate`

Command:

```sh
timeout 300 python3 -B -c 'from pathlib import Path; import sys; p=Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotodama.md"); n=sum(1 for line in p.read_text().splitlines() if line == "## Gate"); print(f"Gate heading count={n}; expected=1"); sys.exit(0 if n == 1 else 1)'
```

Output:

```text
Gate heading count=0; expected=1
exit=1
```

### W2 — void categories versus committed final-measure receipt

Command:

```sh
timeout 300 python3 -B -c 'from pathlib import Path; import re,sys; report=Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotodama.md").read_text(); receipt=Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/telemetry/final-measure.txt").read_text(); seats=re.search(r"seats=\[(.*?)\]\n", receipt).group(1); chr_n=seats.count("X2/sees:deny:chr("); cwd_n=seats.count("X2/sees:bash-cwd-outside-sandbox"); blind_n=seats.count("X2/sees:kotodama"); bare_n=seats.count("\x27SupportU60:X2\x27"); report_chr=int(re.search(r"(\d+) `deny:chr\(`", report).group(1)); report_void=int(re.search(r"(\d+) voided by CONFINED", report).group(1)); derived_confined=chr_n+cwd_n; ok=(report_chr==chr_n and report_void==derived_confined); print("receipt: deny:chr(=%d, bash-cwd-outside-sandbox=%d, kotodama=%d, bare-X2=%d; CONFINED=%d, total-unqualified=%d" % (chr_n,cwd_n,blind_n,bare_n,derived_confined,chr_n+cwd_n+blind_n+bare_n)); print("report: deny:chr(=%d, voided-by-CONFINED=%d" % (report_chr,report_void)); print("void-breakdown check: %s" % ("PASS" if ok else "FAIL")); sys.exit(0 if ok else 1)'
```

Output:

```text
receipt: deny:chr(=4, bash-cwd-outside-sandbox=5, kotodama=1, bare-X2=1; CONFINED=9, total-unqualified=11
report: deny:chr(=5, voided-by-CONFINED=11
void-breakdown check: FAIL
exit=1
```

### W3 — SupportX60 is qualified in the receipt, but called void in the report

Command:

```sh
timeout 300 python3 -B -c 'from pathlib import Path; import re,sys; report=Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotodama.md").read_text(); receipt=Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-60/telemetry/final-measure.txt").read_text(); qualified=[item.strip(" '\''\"") for item in re.search(r"qualified=\[(.*?)\]", receipt).group(1).split(",")]; report_line=next(line for line in report.splitlines() if "SupportX60" in line and "voided by the counter" in line); is_qualified="SupportX60" in qualified; is_reported_void="SupportX60" in report_line; ok=not(is_qualified and is_reported_void); print("SupportX60: receipt-qualified=%s; report-says-voided=%s; %s" % (is_qualified,is_reported_void,"PASS" if ok else "FAIL")); sys.exit(0 if ok else 1)'
```

Output:

```text
SupportX60: receipt-qualified=True; report-says-voided=True; FAIL
exit=1
```

### W4 — “five” control wins and revision-5 attribution

Command:

```sh
timeout 300 python3 -B -c 'from pathlib import Path; import sys; report=Path("/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotodama.md").read_text().splitlines(); spot=Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-60-verifier-spotcheck.md").read_text().splitlines(); r=next(line for line in report if "five pre-data controls met earlier counters" in line); s=next(line for line in spot if "Stale discernment line" in line); five="five pre-data controls" in r; three="three controls" in s; fourth="fourth seat\u0027s evasion" in s; review="Revision 5 was not forced by a control receipt" in s; ok=not(five and three and fourth and review); print("report line 46 says five controls=%s; verifier says three control-MET plus fourth evasion=%s; revision 5 was L1 review=%s" % (five,three and fourth,review)); print("control-summary check: %s" % ("PASS" if ok else "FAIL")); sys.exit(0 if ok else 1)'
```

Output:

```text
report line 46 says five controls=True; verifier says three control-MET plus fourth evasion=True; revision 5 was L1 review=True
control-summary check: FAIL
exit=1
```

### W5 — inline round-60 cited-line witness (not the absent round-61 tool)

This targeted diagnostic checks the documented R60-M6 line and the cited table rows only; it does not assert a corpus-wide result.

Command:

```sh
timeout 300 python3 -B -c 'from pathlib import Path
import re,sys
p=Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md")
lines=p.read_text().splitlines()
ids=list(dict.fromkeys(re.findall(r"\bS\d+\b", lines[94])))
table=[]
for n,line in enumerate(lines,1):
    rowids=list(dict.fromkeys(re.findall(r"\bS\d+\b", line)))
    if 49 <= n <= 55 and line.startswith("|") and rowids: table.append((n,rowids))
print("MULTI-ID %s:95 %s" % (p,",".join(ids)))
for n,rowids in table: print("TABLE-ID %s:%d %s" % (p,n,",".join(rowids)))
print("CITED-LINES: %d finding(s) in 1 file(s)" % (1+len(table)))
sys.exit(1 if len(ids)>1 and table else 0)'
```

Output:

```text
MULTI-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:95 S612,S613
TABLE-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:49 S603
TABLE-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:50 S641
TABLE-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:51 S640
TABLE-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:52 S605
TABLE-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:53 S626
TABLE-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:54 S638
TABLE-ID /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:55 S628
CITED-LINES: 8 finding(s) in 1 file(s)
exit=1

## Sweep notes and bounds

The selected report row covers the recurring report arithmetic defects recorded as R58-M2 and R59-M2 and the control-summary ambiguity in R59-M3. Capture already present among the reviewed items: R58-M1 is now QUALITY 12; the R58 kind-enum defect has the sources census E05 check; R60-M1 is QUALITY 14. R60-M6 is the uncaptured line-scoping defect addressed by proposed R61-M3 and draft criterion 15.

No report or lesson content was changed except this report. No installs, build, test, formatter, source fetch, git, or jj command was run. The round-61 acceptance counters were not executed; W1–W5 are diagnostics for the mistakes described above, not claim acceptance evidence.

## Artifact path

`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-61/w1/ScribeMistakes.md`
