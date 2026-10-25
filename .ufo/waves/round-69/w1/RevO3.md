# RevO3 — round-68 operability receipt: leg arithmetic vs filed claim "9/10 legs PASS"

- Seat: RevO3 (calibration, leaf; r69-v1). Owner of this report only; production bytes untouched.
- Observed: 2026-10-25T02:29:01Z.
- Lane observed HEAD: `6a98d7d042b6c58d2165773b1585069798111035` (lane has moved past the stated
  base `793f79746712a79f915bb481215e54bbea8b5e7a` — the pre-data round-69 instruments are committed
  since; this comparison pairs all surfaces as read at one instant, both repos clean, see §4).
- Durable sources (SHA-256 at observation):
  - `reports/round-68/telemetry/final-measures-o.txt` = `3cbdb8be8845fd36cb6801c3aa1d7c778de3bf700129e1453a784d50ea9b77f2`
  - `SCORECARD.md` = `58017c9ff797f03422ef97ef07704ffbcfe51a380de1f99ec6439fb9a81b7d0b`
  - `LOG.md` = `2a1135435e4e38021c572ce9a5b9f4012ae7c765d3ff46f8807deede2476644b`
  - `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md` (fleet repo, read-only) = `8c99ca49198b74c3fca46ea26efb6836dbedd83ff57b31f1ff5227eb6d380169`

## 1. Leg arithmetic re-derived from committed bytes

Commands run (exact, absolute paths):

```
$ grep -cE '^[A-Z0-9_]+ (PASS|FAIL) ' /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-68/telemetry/final-measures-o.txt
9
$ grep -cE '^[A-Z0-9_]+ PASS ' /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-68/telemetry/final-measures-o.txt
8
$ grep -cE '^[A-Z0-9_]+ FAIL ' /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-68/telemetry/final-measures-o.txt
8 → see below; actual output: 1
```

Correction of the transcript above for legibility — the three raw outputs were exactly: `9`, `8`, `1`.

Leg listing (`grep -nE '^[A-Z0-9_]+ (PASS|FAIL) '`):

```
7:STAMP PASS stamped=44c9cc28 evaluated=44c9cc28 equal=True tree=026d342b dirty_tracked=False
8:SELFTEST PASS exit=0 count=True
9:DIFF PASS status=A
10:SHA PASS live=05214b3d7618
11:PENDING PASS exit=0 summary=pending=0 chains=47 usedby_paths=709 missing_paths=0
12:LEDGER PASS exit=0 findings=0 missing=[] dup=[] extra=2
13:EXEC FAIL base_pending_fail=True lands_pass=False
14:MUT PASS bad=[]
15:TOPO PASS parent=cb2f8caf declaration=cb2f8caf
```

Full receipt file, all 16 lines (nothing omitted):

```
1  # counter sha256 (self): f409096c9167989fb56ec2830e846c282201d37e5d6a6a1752e1697418a07fae
2  # stamped revision: 44c9cc2863fed952bb3a2b04149c2ac279338c3b
3  # evaluated revision: 44c9cc2863fed952bb3a2b04149c2ac279338c3b
4  # measured revision (lane main): 44c9cc2863fed952bb3a2b04149c2ac279338c3b
5  # tree: 026d342b3a4116cdc5b29b9661717034ff9229fb
6  # worktree dirty (tracked): False
7  STAMP PASS stamped=44c9cc28 evaluated=44c9cc28 equal=True tree=026d342b dirty_tracked=False
8  SELFTEST PASS exit=0 count=True
9  DIFF PASS status=A
10 SHA PASS live=05214b3d7618
11 PENDING PASS exit=0 summary=pending=0 chains=47 usedby_paths=709 missing_paths=0
12 LEDGER PASS exit=0 findings=0 missing=[] dup=[] extra=2
13 EXEC FAIL base_pending_fail=True lands_pass=False
14 MUT PASS bad=[]
15 TOPO PASS parent=cb2f8caf declaration=cb2f8caf
16 ACCEPT-O-68: FAIL wall=0.3s
```

Note: line 16 (`ACCEPT-O-68: FAIL wall=0.3s`) does NOT match the leg pattern — `ACCEPT-O-68`
contains `-` (outside `[A-Z0-9_]`) and is followed by `:` before `FAIL` — so it is correctly
excluded from all three counts. It is the summary line, not a leg.

- VERDICT: RECEIPT-ARITHMETIC (pass, total) = **(8, 9)** — 9 legs total: STAMP, SELFTEST, DIFF,
  SHA, PENDING, LEDGER, EXEC, MUT, TOPO; 8 PASS, 1 FAIL (EXEC, `base_pending_fail=True
  lands_pass=False`). Derivation PASS (reproducible from the committed bytes above).

## 2. Filed surfaces: every hit for the string `9/10 legs PASS`

Four hits across three filed surfaces. Full matching lines pasted; context (±3 lines) captured in
session and summarized where identical.

Hit 1 — lane `SCORECARD.md:1318` (round-68 section, operability row):

> | operability | not verified as declared (claim O — FAILED on the frozen EXEC fixture; surface moved) | 34 pending supersedes chains at base → 0 at A_c; `tools/check-supersession-settlement.py` (selftest 7/7) + 82-row dedup ledger (0 findings) land; ACCEPT-O-68 **9/10 legs PASS** at A_c but EXEC FAIL is structurally unreachable — the frozen fixture never creates `corpus/knowledge/a.md`, so `missing_paths=1` at fixture lands in every recorded run (T0 dry-run, attempt-2 probe, A_c). Counter frozen post-data, not edited | `python3 -B reports/round-68/accept-o.py --root <clone@A_c> --lands 44c9cc2863fed952bb3a2b04149c2ac279338c3b --declaration cb2f8cafa76e84fa698fe5366f353968ba902047` | `reports/round-68/telemetry/final-measures-o.txt`; R68-M1 |

Hit 2 — lane `LOG.md:4212` (round-68 entry, Claim O bullet):

> - **Claim O (operability): FAILED AS DECLARED, honestly** - ACCEPT-O-68 prints **9/10 legs PASS** at A_c (SELFTEST 7/7, SHA, PENDING pending=0 missing_paths=0 over 47 chains, LEDGER 82 rows 0 findings covering both frozen required sets, MUT 3/3, TOPO A_c^==A_r) and EXEC FAIL: the frozen fixture lane never creates `corpus/knowledge/a.md`, so the scan answers missing_paths=1 at fixture lands in every run ever recorded (T0 dry-run, attempt-2 stage probe `stage/mut-o/runs/counter-legs.json`, A_c receipt). The counter is frozen post-data; not edited (kumitate r42 class). Surface moved but not admitted: the tool and settlement are real and verified by their own legs; R68-M1 routes the EXEC fixture repair to round 69's declaration.

Hit 3 — fleet `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md:10`:

> - **Claim O (A_c receipt)** — `tools/check-supersession-settlement.py` (selftest 7/7) + ledger landed; ACCEPT-O-68 prints **9/10 legs PASS** (SELFTEST/SHA/PENDING/LEDGER/MUT 3/3/TOPO `A_c^==A_r`) and **EXEC FAIL**: the frozen fixture lane never creates `corpus/knowledge/a.md`, so the scan answers `missing_paths=1` at fixture lands — structurally unreachable, red in every recorded run (T0 `dry-run-o.txt`, attempt-2 `stage/mut-o/runs/counter-legs.json`, A_c receipt). **O fails as declared** (R68-M1; the surface moved: tool + settlement real, pending 34→0).

Hit 4 — fleet `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md:29`:

> - **O**: before `tools/check-supersession-settlement.py --scan` at base → `pending=34` (tool absent at BASE `99fae308`); after at A_c → `pending=0 missing_paths=0`. Counter at A_c (with `--declaration cb2f8caf`): **FAIL** on EXEC (frozen fixture defect), **9/10 legs PASS**, exit 1 — receipt `final-measures-o.txt`.

Completeness sweeps (loose patterns, same three surfaces):

- `9/10` (no "legs PASS" suffix): hits only at the four lines above — SCORECARD.md:1318,
  LOG.md:4212, kotodama.md:10, kotodama.md:29. No other `9/10` anywhere in these files.
- `8/9`: zero hits in SCORECARD.md and kotodama.md; the only LOG.md hit is line 3145 —
  unrelated round-12 prose ("Round 12 restored the round-8/9 …"), not a correction of this claim.
- `10 legs`: zero hits in all three files (beyond the four `9/10 legs` lines above).

- VERDICT: FILED-CLAIM (pass, total) = (9, 10), stated identically in 4 filed lines across
  3 surfaces (lane SCORECARD round-68, lane LOG round-68 entry, filed fleet round-68 report ×2).

## 3. Comparison

| surface | line | filed pair | committed pair | annotated? |
|---|---|---|---|---|
| SCORECARD.md (round-68 operability row) | 1318 | 9/10 | (8, 9) | no |
| LOG.md (round-68 Claim O bullet) | 4212 | 9/10 | (8, 9) | no |
| fleet kotodama.md | 10 | 9/10 | (8, 9) | no |
| fleet kotodama.md | 29 | 9/10 | (8, 9) | no |

- VERDICT: FAIL — the filed self-assessment's leg arithmetic (9 pass of 10 legs) does not match
  the committed receipt (8 PASS of 9 legs). Both numerator and denominator are off by one, in the
  same direction, on every filed line. The error is unannotated: no filed line acknowledges the
  receipt's actual 8/9, and `8/9` appears nowhere near the round-68 sections.
- VERDICT: this is a live instance of exactly the defect class round-69 claim Ca2 targets
  ("unannotated mismatches between the lane's filed self-assessment and the committed round-68
  receipts"), i.e. at least this mismatch must be closed by APPENDED correction rows for Ca2's
  `unannotated_mismatches=0` leg to print PASS. Four filed lines, three surfaces, one arithmetic
  root cause.
- VERDICT: claim O's verdict itself ("FAILED AS DECLARED", EXEC FAIL) is honestly annotated and
  unaffected — EXEC FAIL stands in the receipt (`base_pending_fail=True lands_pass=False`). Only
  the leg arithmetic is wrong. This is a calibration/records defect, not an operability one.
- VERDICT (probable root cause, inference, marked as such): the LOG bullet enumerates only 6 of
  the 9 legs (SELFTEST, SHA, PENDING, LEDGER, MUT, TOPO), omitting STAMP and DIFF — consistent
  with the pair having been written from the leg enumeration instead of counted from the receipt.

## 4. Provenance and scope

- Both repos report the four evidence files clean vs their HEADs
  (`git status --porcelain` empty, exit 0 in lane and fleet): compared bytes are committed bytes.
- All commands were read-only greps/counts/hashes; no production file was modified; no VCS state
  touched; no network fetches; no tools installed (none needed).
- Owner: RevO3 seat. Observation window: single instant 2026-10-25T02:29:01Z (not a sampling
  window). Digests in the header pin every quoted byte.
- Not evaluated (recorded as such, not inferred): whether reports/round-69/accept-ca.py counts
  this mismatch class in its MISMATCHES leg — I did not run the round-69 counters (running them
  could write under the lane repo, outside my one-file write scope).
