# reports/round-79 — counter revisions (QUALITY 23)

Round-79 counters were frozen at `82b822a7971d236928aac7792be0964cd7ee1059`
(freeze #1 `98b0e53` superseded). Recorded revisions after the freeze:

| # | when / commit | counter | old sha256 | new sha256 | what moved | predicate moved? |
|---|---|---|---|---|---|---|
| 1 | run 12 (2026-10-30), commit `7fdf355` | `reports/round-79/accept-ca.py` | `adfadbec65e15a763c9db6c6745a5d4f0e3ad5f7c658be3d9256f1da4d181620` (bytes at freeze `82b822a`) | `63444388788fefdcde49ac77e4e209e6423bec22b1a1884801f9bc5fa2b95c5c` | corrections derive from `base..lands` adds; `freeze..lands` stays the separable window (documented in the run-12 report and `LOG.md`; the fleet graded receipt `.ufo/reports/round-79/kotodama-accept-ca-lands.txt` names counter sha `63444388…`, i.e. it was produced by the new bytes) | leg set unchanged (7); window arithmetic only |
| 2 | run 14 (2026-10-31), this round's records commit | `reports/round-79/accept-ca.py` | `63444388788fefdcde49ac77e4e209e6423bec22b1a1884801f9bc5fa2b95c5c` | `94b66ea5fea5432c9207d0c7b1fd90c0525a159f1032ef5a9ea5c36b19ff0456` | SELFTEST fixture host-portability only: fixture file writes pin LF (`open(..., newline="\n")` — text-mode writes on Windows produced CRLF fixture blobs and the `$`-anchored used-by parser then reported `unparsed used-by line` on every DERIVE leg); cleanup uses `shutil.rmtree(..., ignore_errors=True)` (Windows read-only git object files raised `PermissionError` after `SELFTEST` printed) | no — grading paths untouched; the graded lands verdict is byte-identical before and after the fix |

Revision 2's red-before (same selftest, only the fix removed):
`telemetry/selftest-ca-redbefore-run14.txt` — `SELFTEST: 4/12`, exit 1; the
receipt's `# counter sha256 (self):` line reads `63444388…`, pinning exactly
which bytes failed. All eight red scenarios stayed red as wanted; the two
clean scenarios were falsely red on CRLF, and the run died in cleanup after
printing. After the fix: `telemetry/selftest-ca-fixed-run14.txt` —
`SELFTEST: 12/12`, exit 0, sha `94b66ea5…`.

Graded verdict unchanged: `telemetry/lands-rerun-ca-run14.txt` (pre-fix
bytes, `ACCEPT-CA-79: PASS legs=7/7`, exit 0) and
`telemetry/lands-rerun-ca-postfix-run14.txt` (post-fix bytes,
`ACCEPT-CA-79: PASS legs=7/7`, exit 0), both run at
`--lands 82b822a7971d236928aac7792be0964cd7ee1059 --freeze
82b822a7971d236928aac7792be0964cd7ee1059` against the lane repo. The two
receipts differ only in the working-counter context, not in any leg line.

`accept-o.py` needed no revision: its selftest passes on this host as
shipped (`telemetry/selftest-o-run14.txt`, `SELFTEST-O79: PASS`, exit 0;
counter sha `3ad26c10c168749d0126b26fe973ffcfce2cbef8d4db36910d58fef29173adc0`,
unchanged from the fleet graded receipt), and its graded lands run
reproduces byte-identical (`telemetry/lands-rerun-o-run14.txt`,
`ACCEPT-O-79: PASS legs=10/10`, exit 0).

Both receipts required by QUALITY 23 (verdict line, exit code, counter
sha256, committed under the round's telemetry) now exist for both counters;
run 12 landed the graded receipts in the fleet repo but committed no
selftest receipts (lesson `corpus/lessons/round-79.md` R79-M1).
