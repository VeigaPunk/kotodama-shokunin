# Round-90 discipline audit — ReviewerDiscipline

Audited at wave-in-flight, 2026-11-04 ~20:10-03, lane HEAD `c0c628d8`, freeze `d0b6f2a7f9cc36272682749a9b047b739406f0c8`, base `6b0b86e45ae902331aca75863db380f2991458c4`. Every finding below carries the command run and its observed output. **No blocking finding.** Two minor findings, three info notes, six pass records.

## Findings (by severity)

### MINOR-1 — committed at-freeze control receipts embed scratch paths (item 3)

```
$ python3 -B tools/check-cited-records.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
CITED-RECORDS: 0 empty / 12 scratch        (rc=1)
SCRATCH /fast/scratch/hyaku/kotodama-r90/atfreeze/... 9 hits in reports/round-90/controls/at-freeze-{C-base,C-freeze,O-base,O-freeze}.txt
SCRATCH /tmp/base84, /tmp/r88v-work                     3 hits in corpus/lessons/round-84-verifier-spotcheck.md, round-88-verifier-spotcheck.md
```

The 9 round-90 hits are `--work /fast/scratch/hyaku/kotodama-r90/atfreeze/...` echoes in recorded command lines, `observed=` strings on MATERIALIZE legs, and one `FileNotFoundError` path in O-base's MUTATION observed. They are command/observation echoes, not source citations, and the dirs they name are scheduled for deletion. Mitigation evidence — the rc is not newly caused by round-90:

```
$ git clone --no-hardlinks <lane> $S/baseclone && git -C $S/baseclone checkout 6b0b86e4
$ python3 -B $S/baseclone/tools/check-cited-records.py --root $S/baseclone
CITED-RECORDS: 0 empty / 3 scratch        (BASE_RC=1)   # same 3 /tmp hits, unchanged since base
$ git diff 6b0b86e4 --stat -- corpus/lessons/round-84-verifier-spotcheck.md corpus/lessons/round-88-verifier-spotcheck.md
(empty output — both files byte-identical to base)
```

So: rc=1 pre-exists at base (inherited, freshness-paused files, out of round-90 write scope); round-90 added 9 echoed scratch paths without flipping the verdict. No source citation in any round-90 artifact points into /tmp, /var/tmp or /fast/scratch.

### MINOR-2 — STUB leg is substring-presence, unpinned, and the frozen claim text misdescribes the stub's failure mode (item 1, O leg strength)

```
# reports/round-90/measure90.py (worktree, = rev5) STUB leg:
ok = ('SELFTEST' in text and 'FAIL' in text and 'MUTATION' in text and 'broken-pattern' in text)
# text = lands copy of cfg['O']['stub_receipt'] — no sha comparison (TOOL and MUTATION legs do pin bytes)
```

Two consequences, neither currently exploited:

- A lands revision could alter `reports/round-90/controls/stub-tool.txt` and still pass STUB as long as the four substrings remain. Current bytes are unchanged since freeze (stub-tool.txt absent from the `git diff d0b6f2a7 → worktree` stat, which lists only at-freeze-*.txt, counter-revisions.md, measure90.py). Residual risk at landing time.
- `claims.json` O.after_target says the stub control records "the stub failing SELFTEST and MUTATION". The actual committed receipt records the stub **passing** SELFTEST and failing REFUSALS + MUTATION:

```
# reports/round-90/controls/stub-tool.txt:
# rc=0 stdout='SELFTEST PASS 67/67'
# refusal cases printed ok by the stub: 0/13 -> REFUSALS leg FAIL
# rc=1 MUTATION-SCORE: 0/43 killed, 0 survived, 43 broken-pattern
```

The genuine control value (a fake `SELFTEST PASS 67/67` line is caught by REFUSALS, and the stub scores 0/43 with all broken-pattern) is stronger than the claim text implies, but the frozen description is inaccurate to the recorded bytes. claims.json is frozen; no seat may amend — recording the discrepancy here.

### INFO-1 — counter revisions: endpoints verified, intermediates unrecoverable (item 1)

`counter-revisions.md` (added post-freeze in `9fb2c58f`) explains revs 1–5; none changes a leg, threshold, predicate or constant:

```
$ sha256sum reports/round-90/measure90.py
80a07a579be80376d2ba6227011a7231bff47e75ad92c6e4a6e415676aad835a   == table rev 5
$ git show d0b6f2a7:reports/round-90/measure90.py | sha256sum
4091cda9e0b5af399e99e85898f3040b9070d4225cf11584a601fe4c19caf0ce   == table rev 1
$ git diff d0b6f2a7 -- reports/round-90/measure90.py   # full net diff rev1→rev5:
  (a) git archive via subprocess binary + tar on stdin        (table rev 4)
  (b) absent-tool branch: SELFTEST records 'tool absent at lands' instead of FileNotFoundError (rev 2)
  (c) absent-entry branch: ENTRY leg FAIL 'entry absent at lands' instead of rc2 REFUSED (rev 5)
  (d) APPENDONLY reads entry from materialized tree instead of git_show (rev 5)
  (e) args.root = os.path.abspath(args.root)                  (rev 3)
```

No leg name, threshold (`cfg['O']['selftest_checks']`, `cfg['O']['mutation_min']`), predicate or constant appears in the diff. Constants are structurally pinned: `measure90.py` loads cfg from the **freeze revision** (`raw = git_show(root, freeze, 'reports/round-90/claims.json')`, line 105), and the worktree claims.json is byte-identical to the freeze copy (`sha256` `9c161eeecae4…` for both). Verification gap: rev 2–4 blobs are not in the object store (sha256 values only in the table), so their per-step diffs are unverifiable; the verified rev1→rev5 net diff is clean, so no persistent change exists. Note: at-freeze base-control receipts are stamped 19:56 (pre-rev5 counter) while freeze-control receipts are 19:59 (rev5); the recorded behaviors are consistent with the described revision history (O-base's MUTATION observed carries the FileNotFoundError text rev2 was written to fix).

### INFO-2 — claim C landing not yet materialized; capture-hygiene and source-conduct items not yet observable

At audit time: `corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, `reports/round-90/evidence/` and `manifest.json` are absent from the worktree (`ls` → No such file or directory); `.ufo/waves/round-90/w1/lands/` is empty; worktree `corpus/SOURCES.md` == base (no new rows landed yet — the ≥3 new S942–S948 rows are still due). Items requiring landing artifacts (every cited capture committed and non-empty; every capture http status 2xx; no CAPTCHA/login/paywall body as evidence) could only be checked against the freeze-era committed artifacts, which show no violations (at-freeze receipts record no challenge pages). These must be re-checked at WAVE-DONE against the materialized lands.

### INFO-3 — scratch inventory snapshot for the WAVE-DONE check (item 6)

```
$ ls /fast/scratch/hyaku/kotodama-r90/
ExecIndepRefetch  L1  ReviewerDiscipline  ReviewerEntry  ScoutRecon  ScribeEntry
atfreeze  godspeed-bytes.txt  l1-probe  mut.json  mut.txt  mut2  plan-err.txt
plan-err2.txt  plan-out.json  plan-tasks.json  run-err.txt  stub
```

WAVE-DONE has not occurred; this is the comparison baseline. Seat-named dirs present: ExecIndepRefetch, ReviewerEntry, ScribeEntry, ScoutRecon, ReviewerDiscipline (mine — removed before this report's yield). The `L1`, `atfreeze`, `l1-probe`, `stub`, `mut`, `mut2`, `plan-*`, `godspeed-bytes.txt` entries are L1-owned; per contract L1 clears its scratch at wave close. Any seat-named dir surviving WAVE-DONE is a finding to raise then.

## Pass records

1. **Frozen-byte drift (item 1):** `sha256sum tools/check-advance-evidence.py` → `121888f08a81ad87675863cf972dd4d32f0a6764b9911dab6b4c8fc4bfe828ed` == claims.json O.tool_sha256; `git show HEAD:tools/check-advance-evidence.py | sha256sum` → same (worktree not dirty). Counter legs/thresholds/constants match claims.json by construction and by audit: O legs MATERIALIZE/TOOL/SELFTEST/REFUSALS/MUTATION/STUB, C counter legs MATERIALIZE/ENTRY/INDEX/APPENDONLY, inner entry legs from frozen `cfg['C']['legs']` (ENTRY SHAPE TOPIC NEWIDS GATE CAPTURE), new-row qualifier `tier in ('A','B') and status=='mined' and opened==cfg['as_of']` (2026-11-04). claims.json byte-identical to freeze commit. Revisions explained per INFO-1.
2. **Registry append-only legality (item 2):** `git diff 6b0b86e4 -- corpus/SOURCES.md` → empty; full `git diff --stat 6b0b86e4..HEAD` → 18 files, 2408 insertions, **0 deletions**, all new files under `.ufo/waves/round-90/` and `reports/round-90/` plus `tools/check-advance-evidence.py`; zero files under `corpus/`. No existing row removed, no cell changed, freshness pause respected at both worktree and HEAD.
3. **Evidence hygiene (item 3):** checker rc=1 analyzed in MINOR-1 — no round-90 citation points into /tmp, /var/tmp or /fast/scratch; the only scratch references are control-receipt command echoes and base-inherited round-84/88 lesson lines.
4. **Scope (item 4):** lane `git log` → all commits authored `kotodama-shokunin <kotodama@shokunin.local>` (L1); `git reflog` → only `export from jj` entries; no seat commits, no resets. Fleet-root `git status --porcelain` → no round-90/kotodama-named leftovers (nearest: `closure-kotodama-r83-entry.json`, mtime 10:15, round 83, pre-wave; `after` stray dated 2026-11-03 20:05, pre-round; `.ufo/reports/round-78/chousa.md` 20:01 and `.scratch/run15-state.json` 20:04 belong to chousa/orchestrator activity outside this wave's dispatch at 20:05–20:06; `.ufo/reports/round-84/kama.md` modified 12:28, kama lane, pre-wave). shokuknow: 1919 pre-existing dirty files, newest kotodama mtime 2026-10-24 — no round-90 write. `~/.local/bin` newest entry 2026-11-02 — untouched; no tool installs by this seat.
5. **Source conduct (item 5):** no captures exist yet (INFO-2); committed freeze-era artifacts (claims.json, controls, mutation-score.txt, stub-tool.txt) contain no CAPTCHA/bot-challenge, login-wall or paywall evidence; mutation-score.txt header pins the tool sha `121888f0…` == freeze pin and reports `MUTATION-SCORE: 43/43 killed, 0 survived, 0 broken-pattern` (≥ frozen min 42).
6. **Reserved ids:** no registry rows exist yet outside base; nothing observed contradicting the S942–S949 reservation. To re-verify against the lands at WAVE-DONE.

## Residual risk and verification gaps

- MINOR-2's unpinned STUB leg and the substring check are structural; only a WAVE-DONE re-diff of `reports/round-90/controls/stub-tool.txt` against the freeze blob closes it for this round.
- Capture-level hygiene, source conduct and new-row qualification (S942+, lesson gate lines, used-by citations, opened==2026-11-04) are unverifiable until the claim-C landing materializes; re-run at WAVE-DONE: the checker above, `git diff 6b0b86e4 -- corpus/SOURCES.md` (expect appends only, new ids within S942–S948 + existing), and per-capture http-status/quote review.
- Counter rev 2–4 intermediate bytes unverifiable (sha256 table entries only); net effect proven clean.
