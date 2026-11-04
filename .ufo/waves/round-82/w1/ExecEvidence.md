# ExecEvidence — Kotodama r82 w1 receipts (claims O + D)

Seat: ExecEvidence (leaf, receipts). Date: 2026-11-04. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base revision: `c285b2afb19d4b64320e18df1f55e426bf2d0b0c`. No tool installs were made (nothing added to any PATH dir). No network fetches were made (UA-record discipline N/A for this seat). Scratch dir `/fast/scratch/hyaku/kotodama-r82/ExecEvidence/` removed before yield; all receipts survive in stage.

## 0. Verdict summary

- Queue receipts AGREE with the independent tally at both dates — four numbers and all 813 DUE lines identical, against the frozen base blob. Claim O's core computation is corroborated by a from-contract reimplementation.
- `--selftest` now PASSES: `SELFTEST: PASS (13 checks)`, exit 0 (revision `95e67c16…`). My first pass against the earlier in-wave revision `0bbf942a…` caught a real selftest-fixture defect ("12-cell row" check returned rc=0); the tool itself was contract-correct throughout (my probes), the owner (ExecTool) fixed the fixture line same wave, and all receipts were re-taken against the fixed bytes. No blocker remains.
- Entry-draft lint pre-check passes: `CITED-LINES: 0 finding(s) in 1 file(s)`.
- Context so the L1 does not misread 827 vs 832: my receipts are pinned to the base blob per assignment; the live registry grew to 832 rows during the wave (S904–S908, all 365d). The two views reconcile exactly (§6).

## 1. Frozen registry blob

- `991457` bytes — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md > /fast/scratch/hyaku/kotodama-r82/ExecEvidence/SOURCES-frozen.md` (stderr empty).
- sha256 `2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263` — `sha256sum` of that file.
- Structure observed: single `## Registry` heading at line 26; header `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` (11 columns); recheck cell values include `on-release`, `90d`, `180d`, `365d`. S904–S906 are absent from the blob, as expected for rows opened this round.

## 2. Receipt 1 — queue receipts (draft tool over frozen blob)

Tool: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/tools/check-sources-recheck.py`. Revision history during my seat: `0bbf942aeab362daf2f5e68f2c48ac1f4c46dbbd7ae98d8e740667030aebe087` (14258 B, first pass) → `95e67c16f466c0f1b2e34faf9681063b4af68024feb3a3ec4d0efd3b740ba219` (14259 B, fixture fix at line 253, re-take). The staged files carry the re-take (fixed revision); the audit outputs were byte-identical at both revisions because the fix touches only the selftest fixture.

- `queue-as-of-2026-11-04.txt`: `RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows`, 0 DUE lines, exit 0, stderr empty.
- `queue-projection-2027-11-01.txt`: `RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows`, `813` DUE lines, exit 0, stderr empty.
- Files carry header lines: command, registry revision, tool path, tool sha256, registry blob sha256, exit code, then full stdout.

## 3. Receipt 2 — independent tally + comparison

`/fast/scratch/hyaku/kotodama-r82/ExecEvidence/tally.py` (staged copy: `.ufo/waves/round-82/w1/stage/ExecEvidence/independent-tally.py`) implemented from the round contract only, before reading the tool's parsing code. Command per date: `python3 -B tally.py SOURCES-frozen.md <as-of> 90`.

- as-of 2026-11-04, exit 0: `RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows`
- as-of 2027-11-01, exit 0: `RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows` + 813 `DUE <id> <iso-date>` lines.

Comparison (programmatic, both dates, at both tool revisions): tool `(0, 18, 14, 827)` vs tally `(0, 18, 14, 827)` — match; tool `(813, 0, 14, 827)` vs tally `(813, 0, 14, 827)` — match; sorted DUE line sets equal (`813` vs `813` lines). `OVERALL AGREEMENT: True`. No disagreement to flag on the numbers.

## 4. Receipt 3 — selftest (caught a fixture defect; now PASS)

**First pass** against revision `0bbf942a…`: `python3 -B <draft tool> --selftest`, exit code `1`:

```
SELFTEST: FAIL 12-cell row: rc=0 stdout='DUE S911 2026-01-31
RECHECK-QUEUE: 1 due / 0 upcoming / 0 on-release / 1 rows
'
SELFTEST: FAIL (1 of 13 checks failed)
```

Mechanism (source read, selftest check 4): the fixture was built as `row("S911", "2026-01-01", "30d")[:-1] + " extra |"` — `[:-1]` removes the closing pipe, so the appended text GLUED `extra` onto cell 11 (`- extra`) instead of adding a 12th cell; `parse_row` correctly split 11 cells, computed 2026-01-01+30d = 2026-01-31, exited 0, and the check (expecting exit 2) failed. The tool's row-parsing contract was intact: my independent probes (fixtures staged under `probes/`, receipt `malformed-row-probe.txt`, re-taken against the fixed revision) all exit 2 with a single `RECHECK-ERROR` line and no traceback:

- 12-cell row → `RECHECK-ERROR line 5: row has 12 cells, expected 11`
- 10-cell row → `RECHECK-ERROR line 5: row has 10 cells, expected 11`
- cadence `fortnight` → `RECHECK-ERROR row S999: unparseable recheck cadence 'fortnight'`

**Re-take** against revision `95e67c16…` (line 253 now `row("S911", "2026-01-01", "30d")[:-1] + "| extra |"` — the exact one-character repair; owner ExecTool applied it independently), `python3 -B <draft tool> --selftest`, exit code `0`:

```
SELFTEST: PASS (13 checks)
```

`13` checks run — `13` ≥ 8, count clause met; format matches the contract string. Staged: `tool-selftest.txt` (carries the PASS re-take; the FAIL first pass is quoted here).

## 5. Receipt 4 — entry-draft cited-lines pre-check

Draft present: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` (`28994` bytes — `os.stat`, mtime 2026-11-04 ~08:24 local). Command: `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-cited-lines.py <draft>`, exit `0`:

```
CITED-LINES: 0 finding(s) in 1 file(s)
```

That is exactly the claim-D gate target. Staged: `cited-lines-precheck.txt`.

## 6. Base (827) vs live (832) reconciliation

ExecTool reports the live registry grew 827→832 rows during the wave (S904–S908, all recheck `365d`, opened 2026-11-04 → due 2027-11-04). My receipts are pinned to the base blob per assignment. Arithmetic check of the delta: at as-of 2026-11-04 (horizon 2027-02-02) the five new due dates fall outside → `0 due / 18 upcoming / … / 832 rows` (matches ExecTool's live line); at as-of 2027-11-01 (horizon 2027-12-30) they fall inside the window → `813 due / 5 upcoming / … / 832 rows` (matches). ScribeRows-6 independently confirms 827 = base census, 832 = post-landing census. No disagreement.

## 7. Files written (absolute paths)

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ExecEvidence.md` (this report)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecEvidence/queue-as-of-2026-11-04.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecEvidence/queue-projection-2027-11-01.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecEvidence/tool-selftest.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecEvidence/cited-lines-precheck.txt`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecEvidence/independent-tally.py`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ExecEvidence/probes/{12-cell-row.md,10-cell-row.md,unparseable-cadence.md}`

## 8. Risks / handoff to L1

- No blocker remains for claim O: selftest passes at the fixed revision; queue numbers corroborated independently; error clauses probed green.
- My receipts intentionally reflect the BASE blob (c285b2a, 827 rows) per assignment; any gate run against the live registry should expect 832 rows (§6).
- S907 reject candidate and source fetches were out of my seat scope; not checked here (unrun).
