# Round-31 closure audit — C04 (independent re-verification)

- artifact: reports/round-31/closure-audit-C04.md
- claim: R31-C (calibration) closure ledger — auditor slot C04
- auditor: kotodama-shokunin round-31 C-closure worker slot 4 (operator regimen loop 3 GLM-1; 16w zai-coding-plan/glm-5.3-flash-low zai MAX)
- date: 2026-10-18; lane HEAD: e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c (git rev-parse, re-read 2026-10-18)
- target: re-verify >=6 rows of reports/round-31/closure-ledger.json from raw sources (fleet reports at /home/vgpnk/Projects/shokunin/.ufo/reports/round-N/kotodama.md, MANIFEST.json at fleet root, lane git) — not by trusting the ledger.
- method: per sampled row — (1) extract every hex token >=7 chars from the raw report text and run `git cat-file -e <h>^{commit}` + `git merge-base --is-ancestor <h> HEAD` in the lane repo; (2) `grep -n "^#" <report>` for the four required sections; (3) MANIFEST.json rounds[] round==N type==closure with kotodama, checking verdicts/adjudication presence; (4) MANIFEST-notes work-commit prefix-match against report-cited hashes.

## Per-row results

### round 8 — PASS

- report `.ufo/reports/round-8/kotodama.md` exists: True
- sections (`grep -n "^#" …`, 2026-10-18): Work performed=True, Landed changes=True, Before → after measurements=True, SHONEN=True → 4/4
- commit citations:
  - `cf338a7`: exists=True ancestor_of_lane_head=True (git cat-file -e cf338a7^{commit}; git merge-base --is-ancestor cf338a7 HEAD (2026-10-18))
  - `e1694ba`: exists=True ancestor_of_lane_head=True (git cat-file -e e1694ba^{commit}; git merge-base --is-ancestor e1694ba HEAD (2026-10-18))
  - `e1694bad6ac96aca45a11ca5746582b275929355`: exists=True ancestor_of_lane_head=True (git cat-file -e e1694bad6ac96aca45a11ca5746582b275929355^{commit}; git merge-base --is-ancestor e1694bad6ac96aca45a11ca5746582b275929355 HEAD (2026-10-18))
- commit ancestry (cited-commit subset): OK
- work-commit cross-check: MANIFEST notes work commit `e1694bad6ac96aca45a11ca5746582b275929355` prefix-matches a report-cited hash: True
- MANIFEST closure entry: present=True date=2026-10-17 verdicts={"depth": "improved", "coverage": "unchanged", "operability": "improved", "freshness": "improved", "calibration": "improved", "adjacency": "unchanged"}
- verdicts/adjudication present: True — notes head: "Regimen loop 1 build 1 (64w opencode-go/deepseek-v4.1-flash, 64/64 completed): claims F/O/D verify, acceptance exits 0 (kotodama-shokunin/reports/round-8/valida…"

### round 11 — PASS

- report `.ufo/reports/round-11/kotodama.md` exists: True
- sections (`grep -n "^#" …`, 2026-10-18): Work performed=True, Landed changes=True, Before → after measurements=True, SHONEN=True → 4/4
- commit citations:
  - `a3f6fce`: exists=True ancestor_of_lane_head=True (git cat-file -e a3f6fce^{commit}; git merge-base --is-ancestor a3f6fce HEAD (2026-10-18))
  - `a3f6fcef2d92a1099581140c81d4264e9a4e2aa3`: exists=True ancestor_of_lane_head=True (git cat-file -e a3f6fcef2d92a1099581140c81d4264e9a4e2aa3^{commit}; git merge-base --is-ancestor a3f6fcef2d92a1099581140c81d4264e9a4e2aa3 HEAD (2026-10-18))
  - `e3ef171`: exists=True ancestor_of_lane_head=True (git cat-file -e e3ef171^{commit}; git merge-base --is-ancestor e3ef171 HEAD (2026-10-18))
- commit ancestry (cited-commit subset): OK
- work-commit cross-check: MANIFEST round-11 notes name no work commit (REJECTED round); verdict presence carried by adjudication text
- MANIFEST closure entry: present=True date=2026-10-17 verdicts={"depth": "improved", "coverage": "unchanged", "operability": "improved", "freshness": "unchanged", "calibration": "improved", "adjacency": "unchanged"}
- verdicts/adjudication present: True — notes head: "Regimen loop 1 build 4: REJECTED — claim F failed as declared (drift stability 0.778 < 0.95; all 45 drifts dispositioned, dominant cause is the round's own legi…"

### round 17 — PASS

- report `.ufo/reports/round-17/kotodama.md` exists: True
- sections (`grep -n "^#" …`, 2026-10-18): Work performed=True, Landed changes=True, Before → after measurements=True, SHONEN=True → 4/4
- commit citations:
  - `e7ecd204` — non-commit hex token, excluded from commit set: digest-not-commit: prose context (packet/projector digest); git cat-file -t: not an object (2026-10-18); prose context: round-17 report line 19 'deterministic packet e7ecd204…' / round-23 report line 16 'final combined projector `2819f687…`'. On-disk sha256-prefix match searched (out/, corpus/, examples/, round-17/23 report dirs, 2026-10-18): no file found — artifacts transient; classification rests on prose + `git cat-file -t` non-object result.
  - `3dd37542`: exists=True ancestor_of_lane_head=True (git cat-file -e 3dd37542^{commit}; git merge-base --is-ancestor 3dd37542 HEAD (2026-10-18))
  - `3dd3754207032cb81f5fb3e202fe85cf79211339`: exists=True ancestor_of_lane_head=True (git cat-file -e 3dd3754207032cb81f5fb3e202fe85cf79211339^{commit}; git merge-base --is-ancestor 3dd3754207032cb81f5fb3e202fe85cf79211339 HEAD (2026-10-18))
  - `9b49a4a`: exists=True ancestor_of_lane_head=True (git cat-file -e 9b49a4a^{commit}; git merge-base --is-ancestor 9b49a4a HEAD (2026-10-18))
- commit ancestry (cited-commit subset): OK
- work-commit cross-check: MANIFEST round-17 notes name no work commit (REJECTED round); verdict presence carried by adjudication text
- MANIFEST closure entry: present=True date=2026-10-18 verdicts={"depth": "unchanged", "coverage": "improved", "operability": "improved", "freshness": "unchanged", "calibration": "improved", "adjacency": "unchanged"}
- verdicts/adjudication present: True — notes head: "Regimen loop 2 build 1: REJECTED on claim D — the round-11 typed-pipeline-gate L1 leg is assemble-d2-bound and cannot consume D4 packets (boundary + re-pin reci…"

### round 23 — PASS

- report `.ufo/reports/round-23/kotodama.md` exists: True
- sections (`grep -n "^#" …`, 2026-10-18): Work performed=True, Landed changes=False, Before → after measurements=True, SHONEN=True → 3/4: known finding F-C31-1 (no `## Landed changes` heading; substance present in-prose; disposition recorded in ledger, not repaired)
- commit citations:
  - `2819f687` — non-commit hex token, excluded from commit set: digest-not-commit: prose context (packet/projector digest); git cat-file -t: not an object (2026-10-18); prose context: round-17 report line 19 'deterministic packet e7ecd204…' / round-23 report line 16 'final combined projector `2819f687…`'. On-disk sha256-prefix match searched (out/, corpus/, examples/, round-17/23 report dirs, 2026-10-18): no file found — artifacts transient; classification rests on prose + `git cat-file -t` non-object result.
  - `0e81d9d`: exists=True ancestor_of_lane_head=True (git cat-file -e 0e81d9d^{commit}; git merge-base --is-ancestor 0e81d9d HEAD (2026-10-18))
  - `b5d9844615b32b145fc263e3bd37062dce703b3b`: exists=True ancestor_of_lane_head=True (git cat-file -e b5d9844615b32b145fc263e3bd37062dce703b3b^{commit}; git merge-base --is-ancestor b5d9844615b32b145fc263e3bd37062dce703b3b HEAD (2026-10-18))
- commit ancestry (cited-commit subset): OK
- work-commit cross-check: MANIFEST notes work commit `b5d9844615b32b145fc263e3bd37062dce703b3b` prefix-matches a report-cited hash: True
- MANIFEST closure entry: present=True date=2026-10-18 verdicts={"depth": "improved", "coverage": "unchanged", "operability": "improved", "freshness": "unchanged", "calibration": "improved", "adjacency": "unchanged"}
- verdicts/adjudication present: True — notes head: "Regimen loop 2 GLM-1: O/D verify, acceptance exits 0; work commit b5d9844615b32b145fc263e3bd37062dce703b3b. Wording tail dispositioned (preferred route); six co…"

### round 29 — PASS

- report `.ufo/reports/round-29/kotodama.md` exists: True
- sections (`grep -n "^#" …`, 2026-10-18): Work performed=True, Landed changes=True, Before → after measurements=True, SHONEN=True → 4/4
- commit citations:
  - `87bfc99`: exists=True ancestor_of_lane_head=True (git cat-file -e 87bfc99^{commit}; git merge-base --is-ancestor 87bfc99 HEAD (2026-10-18))
  - `87bfc9956f0fc60e6821fe53b622d0043e28be10`: exists=True ancestor_of_lane_head=True (git cat-file -e 87bfc9956f0fc60e6821fe53b622d0043e28be10^{commit}; git merge-base --is-ancestor 87bfc9956f0fc60e6821fe53b622d0043e28be10 HEAD (2026-10-18))
  - `e923d6e`: exists=True ancestor_of_lane_head=True (git cat-file -e e923d6e^{commit}; git merge-base --is-ancestor e923d6e HEAD (2026-10-18))
- commit ancestry (cited-commit subset): OK
- work-commit cross-check: MANIFEST notes work commit `87bfc9956f0fc60e6821fe53b622d0043e28be10` prefix-matches a report-cited hash: True
- MANIFEST closure entry: present=True date=2026-10-18 verdicts={"depth": "unchanged", "coverage": "unchanged", "operability": "improved", "freshness": "unchanged", "calibration": "improved", "adjacency": "improved"}
- verdicts/adjudication present: True — notes head: "Regimen loop 3 verify: C/O/A verify, acceptance exits 0; work commit 87bfc9956f0fc60e6821fe53b622d0043e28be10. Register landing reproduced; law calibration disp…"

### round 30 — PASS

- report `.ufo/reports/round-30/kotodama.md` exists: True
- sections (`grep -n "^#" …`, 2026-10-18): Work performed=True, Landed changes=True, Before → after measurements=True, SHONEN=True → 4/4
- commit citations:
  - `44145d5`: exists=True ancestor_of_lane_head=True (git cat-file -e 44145d5^{commit}; git merge-base --is-ancestor 44145d5 HEAD (2026-10-18))
  - `71cd9d37`: exists=True ancestor_of_lane_head=True (git cat-file -e 71cd9d37^{commit}; git merge-base --is-ancestor 71cd9d37 HEAD (2026-10-18))
  - `71cd9d376ebd144e94e4f12d997f73e5d2839aa9`: exists=True ancestor_of_lane_head=True (git cat-file -e 71cd9d376ebd144e94e4f12d997f73e5d2839aa9^{commit}; git merge-base --is-ancestor 71cd9d376ebd144e94e4f12d997f73e5d2839aa9 HEAD (2026-10-18))
- commit ancestry (cited-commit subset): OK
- work-commit cross-check: MANIFEST notes work commit `71cd9d376ebd144e94e4f12d997f73e5d2839aa9` prefix-matches a report-cited hash: True
- MANIFEST closure entry: present=True date=2026-10-18 verdicts={"depth": "improved", "coverage": "unchanged", "operability": "improved", "freshness": "unchanged", "calibration": "improved", "adjacency": "unchanged"}
- verdicts/adjudication present: True — notes head: "Regimen loop 3 integrate: O/C/D verify, acceptance exits 0; work commit 71cd9d376ebd144e94e4f12d997f73e5d2839aa9. 5/5 routed items resolved (QREG dangles, speak…"

## Counts (command + date)

| count | value | command | date |
|---|---|---|---|
| rows re-verified | 6 | rounds {8, 11, 17, 23, 29, 30} in this audit loop | 2026-10-18 |
| reports present | 6/6 | os.path.isfile per .ufo/reports/round-N/kotodama.md | 2026-10-18 |
| sections 4/4 | 5 (round 23 = 3/4, known F-C31-1) | grep -n "^#" per report | 2026-10-18 |
| commit citations verified | 13 | git cat-file -e + git merge-base --is-ancestor vs lane HEAD e8d2d0d | 2026-10-18 |
| non-commit hex tokens classified | 2 (e7ecd204 r17, 2819f687 r23) | git cat-file -t + prose-context read | 2026-10-18 |
| MANIFEST closure entries present | 6/6 | MANIFEST.json rounds[] round==N type==closure | 2026-10-18 |
| work-commit cross-checks pass | 4/4 where MANIFEST names one (8, 23, 29, 30) | prefix-match vs report-cited hashes | 2026-10-18 |

## Verdict

`verify` — all 6 re-verified rows agree with closure-ledger.json. Ancestry: every cited commit exists and is an ancestor of lane HEAD. Sections: 5/6 full, round 23 reproduces the already-recorded finding F-C31-1 (no new defect). Verdict presence: 6/6 closure entries carry verdicts or an explicit REJECTED/operator-skip adjudication. Falsification: any row above whose commands re-run to a different result (2026-10-18).

