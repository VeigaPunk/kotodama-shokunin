# Round 79 — kotodama (run 12 landed the claims at 80c6352/82b822a/7fdf355; run 14 completed the round records on the Windows host)

## Gate

Candidates considered and dispositioned (pre-freeze draft:
`.ufo/waves/round-79/CLAIMS-DRAFT.md`, base `44f76d456c1b326a71ffdb381590af825cbf11be`):

- **ADMITTED — claim O (operability, capability acquisition; the round's one
  declared claim).** `tools/ledger-token-guard.py` lands at `80c6352`
  (sha256 `504c51c6fa73c0b5418c1b1ad734be926f43ed355832d5796a298af040dd7964`,
  17822 bytes): red fixture 11/11 pair failures, green fixture 11/11 PASS,
  selftest 9/9, 16/16 refusal fixtures, fresh-nonce oracle separates the real
  tool from an echo stub. Frozen counter:
  `ACCEPT-O-79: PASS legs=10/10` at lands `7fdf355`, freeze `82b822a`.
  Re-derived on this host (run 14): `reports/round-79/telemetry/lands-rerun-o-run14.txt`
  (exit 0, counter sha `3ad26c10…` matching the fleet graded receipt), plus a
  direct invocation `reports/round-79/telemetry/guard-direct-red-run14.txt`
  (`LEDGER-TOKEN-GUARD: FAIL pairs=11 failed=11 mismatched=10 vacuous=1`, exit 1).
- **EXECUTED AS UNCLAIMED REPAIR — candidate Ca (calibration).** The round-78
  census receipt drift (S884 `used-by=…amend-2026-10-24-r13.md` at
  `reports/round-78/telemetry/census-end.txt:33` vs `…amend-2026-10-23.md` in
  the registry at the receipt's measured revision `4b255745`) is bound by the
  append-only correction `reports/round-79/corrections/ca79-r78-s884.md`
  (landed `0439764`; receipt not rewritten). Frozen counter:
  `ACCEPT-CA-79: PASS legs=7/7` at lands `82b822a`; re-derived on this host:
  `reports/round-79/telemetry/lands-rerun-ca-run14.txt` (exit 0). Per the
  pre-freeze scope disposition, census-receipt repair is not the calibration
  sizing target (SCORECARD/SHONEN self-assessment mismatches), so no axis
  delta is taken (QUALITY 20: record repairs are calibration work, not a score).
- **REJECTED before freeze (coverage): dining/tableware knowledge entry.**
  Ground already held: `corpus/knowledge/culture-material/cuisine-food-lexicon.md`
  §6 "Etiquette: the table as grammar" (lines 90–93: table manners history,
  chopstick taboo grammar) and `furniture-interior-lexicon.md` naming dining.
- **REJECTED (carried from rounds 77/78): naming-systems candidate** — went
  through a complete source/content review in round 77 and was not admitted;
  round 78's Gate upheld the rejection.
- **Freshness (historically the lowest non-retired axis): paused.** The
  axis-move remains paused by the unresolved round-11 L0 question — operator
  ruling, same disposition as rounds 77/78. The SCORECARD carries no
  saturation line/window, so the stagnation nudge is NOT invoked; the pause,
  not the nudge, is the recorded reason the round worked operability.

New SOURCES row this round: **S897** (own-work, tier A for its scope, status
`mined`, opened 2026-10-30). Gate record per CORPUS rule 1: source path
`tools/ledger-token-guard.py`; command
`python -B tools/ledger-token-guard.py --selftest --work <scratch>` (and the
frozen-counter demonstration in `reports/round-79/claims.json` claim O);
access date 2026-10-30; located quote (file body, docstring lines 8–9):
"This guard re-runs every observation against the immutable committed bytes
named by the pair's `observe` object" (20 words), grounding `teaches`.

Spot-check: no non-author reviewer was available inside this single-session
run; no decision this run opened an external source or admitted a knowledge
entry. The round's gate decisions (O admit, Ca correction, counter revision 2)
stand author-side with their re-runnable receipts committed; the closure
judge samples from the counting commands in `SCORECARD.md`, each of which
re-derives its verdict from committed bytes on any host with git + python.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R79-M1 | landing — the run-12 wrap-up committed the graded counter receipts to the fleet repo but left both counters' selftest receipts uncommitted and the falsify wave unlaunched, so QUALITY 23's "verdict line, exit code and counter sha256 committed under the round's telemetry" had no round-79 receipt until this run | `reports/round-79/telemetry/` before run 14 held only `baseline-census-mismatch.json`, `census-start-meta.json`, `census-start.txt`; QUALITY 23 (binds from round 74) | fix: both counters' selftest receipts committed this run (`selftest-o-run14.txt`, `selftest-ca-redbefore-run14.txt`, `selftest-ca-fixed-run14.txt`); the W2-class mutation pass over the landed tool stays routed to round 80 (the ~20 adopted-but-unlanded W1 hardening findings under `.ufo/waves/round-79/w1/` would change frozen tool bytes mid-closure; they land through a future QUALITY 23 counter revision with red-befores) |
| R79-M2 | provider — `accept-ca.py`'s selftest fixture wrote files in text mode: on Windows this lands CRLF in fixture blobs and the `$`-anchored used-by parser then fails every DERIVE leg (`SELFTEST: 4/12`, exit 1), and the strict `shutil.rmtree` raised `PermissionError` on Windows read-only git object files after `SELFTEST` printed | `reports/round-79/telemetry/selftest-ca-redbefore-run14.txt` (counter sha `63444388…` in the receipt); `reports/round-79/counter-revisions.md` revision 2 | fix: counter revision `94b66ea5…` — fixture writes pin LF (`newline="\n"`), cleanup uses `ignore_errors=True` (the shape `accept-o.py` has used since its freeze); post-fix selftest `12/12` exit 0 (`selftest-ca-fixed-run14.txt`); graded lands verdict byte-identical pre/post (`lands-rerun-ca-run14.txt`, `lands-rerun-ca-postfix-run14.txt`); no predicate moved |
| R79-M3 | provider — two committed wave-stage paths carry `>` in their filenames (`.ufo/waves/round-68/stage/mut-o/runs/f3_keep-split_on_non_split_S126>S105.txt`, `.ufo/waves/round-68/stage/mut-o/runs/f3_keep-successor_on_unclosed_S044>S034.txt`): legal on the old Linux host, uncheckoutable on Windows NTFS; a third file (`.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/aux/S894-wayback.txt`) is absent on disk after the host move. The inherited working tree therefore shows three staged deletions that are host artifacts, not lane-authored work; the blobs are intact in `HEAD` (`git cat-file -e HEAD:<path>` passes) | `git ls-tree -r HEAD --name-only | grep -E '[<>"\|?*]'` prints the two `>` paths; `git diff HEAD --stat` = exactly those 3 deletions | captured-by: none — no lane rule required Windows-portable characters in committed paths; fix: recorded here; the deletions are left unstaged and untouched (index is not lane-managed on this host; commits go through the plumbing helper only). Routing note for the operator/integrator: prefer NTFS-safe names in future wave-stage paths; the files stay recoverable on any POSIX checkout |

## Sources & frontier

Registry rows 820 → 821 (S897 own-work added this round, status `mined`).
Counting: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
= 821 (at the round-79 records commit; 820 at base `44f76d4`). Census
receipts: `reports/round-79/telemetry/census-start-run14.txt` and
`census-end-run14.txt` (validate exit 0 both). No status/recheck/used-by
changes to prior rows this run.
