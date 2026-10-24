# MutCounterO — FULL / MUTEX / FRAG mutant probe (claim O, round 65)

Seat: `kotodama-r65.MutCounterO`. Scope: mutate only the round-65 FULL/MUTEX/FRAG
additions of `reports/round-65/accept-o.py` in staged copies, run one bounded
behavioral detector on pristine / mutated / restored bytes, report killed-by.
No lane file, jj state, or Git index was written; no tools installed.

## Target and revision drift (the lane instrument moved during the probe)

| observed | sha256 | docstring rev | bytes | mtime | action |
|---|---|---|---|---|---|
| R1 | `70f582623964b9196d67773cd69692747d012bcc5660d795d08013d88a61e363` | revision 1 | 66810 | 01:51 | first target; mutants built, baseline run |
| R2 | `2a03a2feeec98a88adef99e08cf2230bfeeea81e5f636489b4dd9dab544a54c2` | revision 2 | 68252 | 01:52:59 | re-targeted; 5/5 killed (results identical to final) |
| R2b | `30065f000c80626965c6a27922d5d2445718e8b13d6aad2bba7649caf132b40e` | still "revision 2" | 68904 | 01:55:02 | re-targeted; 5/5 killed |
| **R3** | **`20d06dd6381201be1acff6e7c187b7355b1f103e8a32d43eb8e6759b15935f94`** | revision 3 | 69897 | 01:55:32 | **final target; table below** |

The five mutation points are byte-stable across R1→R3 (the R3 changes were the
digit-aware regexes and the expected filtered verdict, both outside them). The
lane tip hash was still `20d06dd…` when this report was written; any later
revision needs re-targeting (the generator asserts each needle occurs exactly
once, so it fails loudly rather than mutating the wrong text).

Final pristine/restored bytes in stage: `20d06dd…` (byte-identical to the lane
file). Stage artifacts:

```
stage/mut-o/accept-o.pristine.py                         20d06dd6381201be1acff6e7c187b7355b1f103e8a32d43eb8e6759b15935f94
stage/mut-o/accept-o.restored.py                         20d06dd6381201be1acff6e7c187b7355b1f103e8a32d43eb8e6759b15935f94
stage/mut-o/accept-o.m1_full_only_gains_frag.py          1a9058874a83ebcb3da2f10917dbadeea6763f4c55ed6018c022fdf88a4af0fd
stage/mut-o/accept-o.m2_suffix_marker_removed.py         420dc2f8bac95af6981dd273f940aa0746ae2866345a82d913303ebcc122ab70
stage/mut-o/accept-o.m3_mutex_m1_extras_emptied.py       ee1be415ce4915219f068a83305dd33383a1e8d0a2ed2e0a824cd7cec110f78e
stage/mut-o/accept-o.m4_frag_selftest_requirement_dropped.py 4fbe2d4814b41d6432ad24a2c8c70adf18f19781f30d50837564654ed1b0b440
stage/mut-o/accept-o.m5_frag_scan_check_weakened.py      33b729aa05a43cee30dbb36af0898891d8d6695e01010fb4c3f637e5f90ed679
stage/mut-o/detect.py                                    ebed9ceca43c3da27d16663ebcaccab48c79cc4c15e42ac3d30e177e21031139
stage/mut-o/gen_mutants.py                               70b0e7baffbe46b5d4c0928465af7228353d3e511764db6d6f854e3edd742d5a
```

## Detector (one bounded probe suite, same bytes for pristine/mutant/restored)

`detect.py` runs five probes per candidate (~4–5 s total, loopback only):

* **F (FULL bandwidth)** — `--only FULL` on a scratch root whose
  `tools/reopen-row.py` is a no-op executable. The inner 23-leg battery returns
  in 2 s; the parent's FULL detail exposes the leg universe and SKIP set:
  `FULL FAIL exit=1 pass=2/23 skip=3 unexpected_skip=[] fail=21`.
  This pins that FULL re-runs exactly CORE 13 + EDGE 7 + TOOL,DRIP,MUT and
  tolerates exactly the three self-SKIPs.
* **S (filtered marker)** — `--only TOOL`; the ACCEPT line must be
  `ACCEPT-O-65: PASS [filtered: 1/26 legs]`.
* **M (MUTEX exactness)** — imports the candidate, replaces only `run_tool`
  with pinned per-mutant measured failing sets (the ten real MUTANTS needles
  are still checked, the real comparison statements execute), and runs
  `--only MUTEX`. The receipt is deliberately **stale**, which isolates the
  exactness comparison from the fresh-receipt branch (see finding N1) and is
  baseline-stable: pristine `bad=['exactness-sweep-o65.txt:stale_or_mismatch']`,
  table `m1:EDGE_HTTPS+EDGE_SCHEMEREL+EDGE_USERINFO … m6:EDGE_308,
  m7:EDGE_5TH200 …`.
* **G1 (FRAG selftest)** — fake checker: `--selftest` exits 1, scan prints
  `FRAG: 0 finding(s) in 26 file(s)` exit 0. Frozen leg must FAIL.
* **G2 (FRAG scan)** — fake checker: selftest passes, scan prints
  `FRAG: 2 finding(s) in 26 file(s)` exit 0. Frozen leg must FAIL
  (verdict must not accept a findings report just because it contains "finding").

Baseline: `DETECTOR pristine: CLEAN deviations=[]` on all five probes.
Restored: same bytes, `CLEAN` again. The byte-identity is the restoration
evidence (lane file never touched: mtime 01:55:32 unchanged before/after).

## Mutants — all five killed (5/5, 0 survived)

| # | mutant (one literal replacement, count=1) | pristine observation | mutated observation | killed-by |
|---|---|---|---|---|
| m1 | FULL `run_legs_all` gains `"FRAG"` (line 1135) | `FULL FAIL exit=1 pass=2/23 skip=3 unexpected_skip=[]` | `FULL FAIL exit=1 pass=2/24 skip=2 unexpected_skip=[]` | R2 pin `set(skip_lines) == self_skips` (line 1158): the inner run no longer SKIPs FRAG; also `len(pass_lines) == len(run_legs_all)` (line 1157) because the expected universe grew to 24. The trace is self-inclusive: FULL would execute FRAG, which itself spawns the durable checker. |
| m2 | `suffix = ""` (line 1285) | `ACCEPT-O-65: PASS [filtered: 1/26 legs]` | `ACCEPT-O-65: PASS` | Filtered-run receipt marker (S probe): a 1/26-leg run presents as the unfiltered verdict, the exact round-64 residual. At R3 additionally caught by FULL's `verdict_line == [expected_verdict]` (line 1159), where `expected_verdict` bakes in `[filtered: 23/26 legs]`. |
| m3 | `"m1": {"EDGE_SCHEMEREL", "EDGE_USERINFO", "EDGE_HTTPS"}` → `{"EDGE_SCHEMEREL"}` (line 1170) | `MUTEX FAIL bad=['exactness-sweep-o65.txt:stale_or_mismatch']` (no m1 exactness deviation) | `MUTEX FAIL bad=["m1:measured=['EDGE_HTTPS', 'EDGE_SCHEMEREL', 'EDGE_USERINFO']!=expect=['EDGE_SCHEMEREL']", 'exactness-sweep-o65.txt:stale_or_mismatch']` | Exactness equality `set(failed) != expect` (line ~1223): the disclosed m1 extras (USERINFO, HTTPS) are precisely what the emptied list would hide. Differential kill on identical pinned measurements; see baseline caveat below. |
| m4 | `frag_ok = (st.returncode == 0 and sc.returncode == 0 …` → drop `st.returncode == 0` (line 1263) | `FRAG FAIL selftest=exit1 scan=exit0 files=26/26` | `FRAG PASS selftest=exit1 scan=exit0 files=26/26` | Selftest exit-code conjunct: a checker whose own mutant battery is red still stamps FRAG green. |
| m5 | `"0 finding"` → `"finding"` (line 1264) | `FRAG FAIL selftest=exit0 scan=exit0 files=26/26 scan_out=['FRAG: 2 finding(s) in 26 file(s)']` | `FRAG PASS selftest=exit0 scan=exit0 files=26/26` | Literal zero-finding requirement: exit 0 plus the word "finding" is satisfied by a scan reporting two findings. |

Baseline caveat for m3 (per role: a baseline failure is inconclusive): on R1/R2
the MUTEX leg was already red for an independent defect (digit-blind regex,
finding N2), so the M probe is differential — it requires the pristine run to
show the m6/m7 deviations and *no* `m1:measured=`, and attributes m3 only for
the added m1 deviation. After R3 fixed the regex, pristine MUTEX measures
`m6:EDGE_308`, `m7:EDGE_5TH200` correctly and the comparison path is clean
apart from the deliberate stale receipt; the m3 delta is unchanged.

## Instrument findings observed while probing (not mutants)

* **N1 — NEW BLOCKING at R3 `20d06dd…`: fresh-receipt MUTEX crash, `NameError:
  hashlib`.** `accept-o.py:1235` calls `hashlib.sha256(tool_blob)` in the
  receipt else-branch, but the module-level import is `import hashlib as _hl`
  inside `main()` (line 449); there is no bare `hashlib` binding. Reproduced
  in-process with a fresh matching sweep receipt: `CRASH NameError name
  'hashlib' is not defined`, last output `['MUT SKIP', 'FULL SKIP']`, no ACCEPT
  line. This branch is reached exactly when the sweep receipt is fresh — the
  intended post-sweep state — so `python3 -B reports/round-65/accept-o.py
  --root .` would traceback and ACCEPT-O-65 can never PASS. Fix: use `_hl` or
  add a top-level `import hashlib`. (My M probe therefore keeps the receipt
  stale to exercise exactness; it does not mask this defect.)
* **N2 — fixed at R3, was blocking R1–R2b:** MUTEX/FULL failed-line regex
  `^[A-Z_]+ FAIL` cannot match `EDGE_308` or `EDGE_5TH200` (digits), so m6/m7
  measured `NONE` and MUTEX was unpassable. Evidence: regex probe
  (`re.match(... 'EDGE_308 FAIL') is None`), `dry-run-o.txt` table
  `m6:NONE, m7:NONE`, `controls-o.txt` control 3, and `.ufo/.../w1/RevCounterO.md`
  per the R3 revision note. R3's `[A-Z0-9_]+` (lines 1147, 1207) repairs it;
  my pristine M probe now measures both legs correctly.
* **N3 — fixed at R3, was blocking R1–R2b:** FULL required
  `verdict_line == ["ACCEPT-O-65: PASS"]` while its inner run always carries
  the mandatory filtered suffix (inner invocation observed:
  `ACCEPT-O-65: FAIL [filtered: 23/26 legs]`; dry-run receipt
  `FULL FAIL exit=0 pass=21/23 skip=3`). R3's `expected_verdict` (line 1154)
  now matches the inner string. Mutant m2 would have satisfied the old equality
  by destroying the suffix — the two pins were contradictory.
* **N4 — fixed at R2:** FRAG passed vacuously over 0 row fragments
  (`FRAG PASS … 0 finding(s) in 0 file(s)`, `dry-run-o.txt`). R2's `files == 26`
  (line 1265) is active in both G probes (`files=26/26`).
* **N5 — R2b receipt tool-sha check is unreachable while rows are stale**
  (`elif` before the sha branch) and crashes when they are fresh (N1); net
  negative as shipped.
* `controls-o.txt` was absent at 01:52 and appeared at 01:53; read and used,
  no longer a dependency.

## Reproduction

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-65/stage/mut-o
python3 -B gen_mutants.py                 # asserts every needle count == 1
python3 -B detect.py accept-o.pristine.py pristine
python3 -B detect.py accept-o.m1_full_only_gains_frag.py m1_full_only_gains_frag
...                                       # m2…m5, then
python3 -B detect.py accept-o.restored.py restored
```

## Verdict

Five mutants attempted, five killed, none survived. Restoration verified by
sha256 (`20d06dd…` pristine = restored = lane tip at write time), detector
CLEAN on restored bytes. The mutant outcomes are a coverage finding about the
FULL/MUTEX/FRAG pins as they existed at R3 — they do not resolve N1, which is a
pre-data blocker in the same revision and is reported to the L1 for repair
before any scoring run.
