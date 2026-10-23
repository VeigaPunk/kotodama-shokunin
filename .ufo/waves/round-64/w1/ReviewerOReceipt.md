# ReviewerOReceipt — claim O evidence freshness/completeness

Scope: verify the O evidence set (receipt freshness, mutant telemetry, tool byte-identity, MUT-leg kill list) for round-64 claim O. Evidence commands and outputs pasted; samples 2026-10-23 22:58–23:15 local.

## Check 1 — `reports/round-64/telemetry/final-measures-o.txt`: FAIL (stale partial)

- File exists (1818 bytes, mtime `2026-10-23 22:49:21`), but it is a **truncated, unsigned run**, not a final receipt:
  - **22 leg lines, all `PASS`** (TOOL, INDEP, GEN, ORDER, BOUND, EXIT, PRIV, DEFAULT, ERR, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT, EDGE_SCHEMEREL, EDGE_USERINFO, EDGE_HTTPS, EDGE_MALTARG, EDGE_SLASHLESS, EDGE_308, EDGE_5TH200, DRIP) — the file then **ends mid-run: no `MUT` leg, no `ACCEPT-O-64:` verdict line, no `exit=` trailer**. The counter prints all 23 legs then `ACCEPT-O-64: PASS|FAIL`; a completed run cannot end at line 22.
  - **No 'measured revision' line, no 'counter sha256' line** anywhere in the file (lines 1–22 read verbatim: leg lines only). The round-61 convention (`reports/round-61/telemetry/final-measures.txt:1-2`) *does* carry `# final measures, measured revision <sha>` + `# counters: ... sha256 <sha>` headers; this receipt has neither, so it cannot be bound to a revision or to counter rev3.
  - `sha256sum reports/round-64/accept-o.py` → `c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18`. The file records no sha, so there is **nothing to compare** — neither match nor mismatch is provable from the receipt.
- Provenance: the 22:49 file predates ExecCounterO's live run, whose scratch dir was created 22:58 and which captures to `~/.cache/hyaku/kotodama-r64-w1/ExecCounterO/run-o.txt`, **not** to the telemetry path. So the on-disk file is an orphaned partial from an earlier, apparently killed run (it cannot be ExecCounterO's run: different destination and earlier mtime).
- **Fresh run COMPLETED** (`python3 -B reports/round-64/accept-o.py --root .`, pid 121692, 22:58→~23:12): `run-o.txt` holds all 23 legs printing PASS, ending `MUT PASS bad=[] mutants=10 kill_evidence=[…]` / `ACCEPT-O-64: PASS` / `exit=0`. At last sample the executor had not yet copied it into `telemetry/final-measures-o.txt` — the stale 22:49 partial still occupies the path.
- Verdict: **the receipt on disk is stale-partial and must be overwritten** by the completed run's output. The run itself passes cleanly; measured revision should name the working copy (`jj @` = `b7d22703`, parent `097c21d0`), and the counter sha `c27a9fef…` binds it to rev3 — but only if the executor prepends the header (see Defect 3).

- `reports/round-64/telemetry/` contains only: `census-start.txt`, `census-wave1.txt`, `dry-run-c.txt`, `dry-run-ca.txt`, `dry-run-o.txt`, `dry-run-o-baseline-copy.txt`, `final-measures-o.txt`. None of `mut-o.txt`, `edge-o.txt`, `control-o.txt` exists anywhere in the lane tree (glob `**/{mut,edge,control}-o*.txt` → no hits).
- `claims.json` O `lands` lists all three plus `final-measures-o.txt`; `controls.O` names `telemetry/control-o.txt` as the control receipt (round-63 counter cannot score the new legs; docstring-only patch leaves GEN green while m1..mread still fail their pinned legs). The w1-spec seat `ExecOCounter` (attempt-1) was tasked to write all four receipts; the nw1 `ExecCounterO` prompt **only requires `final-measures-o.txt`** — no seat in the re-run wave is assigned `mut-o.txt`/`edge-o.txt`/`control-o.txt`. **Declared lands are unowned in the live wave plan** → likely to stay missing.
- Verdict: **incomplete evidence**; the claim's own `lands` will not exist at close unless a seat produces them (or claims.json is corrected).

## Check 3 — `tools/reopen-row.py` byte-identity: PASS

- `sha256sum tools/reopen-row.py` → `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0`.
- Round-63 capability record `reports/round-63/telemetry/freeze-sha256.txt` records `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0  tools/reopen-row.py` — **match**.
- `git show ff30a205c8d23b35f1ac533740121a955a9fda96:tools/reopen-row.py | sha256sum` → same `c0f10a84…`; the file is also absent from `jj st` modifications — unchanged at the base and unchanged in the working copy.
- Verdict: **byte-identical to the round-63 record and to the declared base** — the "unchanged tool" premise holds.

## Check 4 — MUT leg lists ten mutants `m1..mread` with `pinned_fail=True`: on-disk FAIL (absent); fresh run satisfies it modulo format

- The on-disk receipt has **no MUT line at all** (ends at DRIP). The completed fresh run does satisfy the intent: `MUT PASS bad=[] mutants=10 kill_evidence=[...]` with each of `m1->EDGE_SCHEMEREL FAIL`, `m10->EDGE_USERINFO FAIL`, `m2->EDGE_USERINFO FAIL`, `m3->EDGE_HTTPS FAIL`, `m9->EDGE_MALTARG FAIL`, `m5->EDGE_SLASHLESS FAIL`, `m6->EDGE_308 FAIL`, `m7->EDGE_5TH200 FAIL`, `m8->(GEN/BOUND) FAIL`, `mread->DRIP FAIL` present — all ten names verified via grep on `run-o.txt`.
- Format caveat for whoever reviews the fresh receipt: the counter never prints `pinned_fail=True` for a passing mutant. In `accept-o.py:1087-1100`, `pinned_fail` appears only inside the `bad=[...]` list on failure; a PASS line reads `MUT PASS bad=[] mutants=10 kill_evidence=[m1->EDGE_SCHEMEREL FAIL; ...]`. The correct passing signature is `mutants=10` + `bad=[]` + `kill_evidence` naming all ten mutants (m1, m10, m2, m3, m9, m5, m6, m7, m8, mread) each with its pinned leg(s) printing FAIL. Demand that full kill_evidence list in the fresh receipt — `mutants=10` alone does not prove all ten were exercised.
- Cross-leg caveat corroborating CriticO's note: I rebuilt m5 (slashless-Location → server-root patch) in scratch and ran the counter against it with `--only EDGE_SCHEMEREL,EDGE_SLASHLESS`: **both legs FAIL** (`EDGE_SCHEMEREL FAIL rows=[('S2770','UNREACHABLE',2)]`, `EDGE_SLASHLESS FAIL rows=[('S2338','UNREACHABLE',2)]`). The claim wording "each fail **exactly** their pinned leg" is therefore literally false as a property statement — the counter only *runs* each mutant's pinned legs, so it cannot and does not verify exclusivity. This is claim-text overstatement, not a leg defect: do not weaken the leg; record it as an open finding (a true exclusivity leg would run each mutant over all 23 legs and require exactly the pin set to fail).
- `reports/round-64/mutants/` exists but is **empty** (mtime 17:13, from attempt-1); the current counter builds mutants under its own tempdir (`work/mroot-<name>`), not there — the dir is dead weight unless ExecCounterO fills it per its step (5).

## Defects (ranked)

1. **HIGH — declared evidence unowned/absent**: `mut-o.txt`, `edge-o.txt`, `control-o.txt` are in `claims.json` O.lands and `controls.O` names `control-o.txt`, but no live wave-1 seat is tasked to write them; none exist. O's control is currently unevidenced.
2. **HIGH — on-disk `final-measures-o.txt` is a stale partial**: 22/23 legs, no MUT, no verdict, no exit, no header; left by an earlier killed run at 22:49. Risk: a reader could miscount it as the final receipt. The completed fresh run must overwrite it.
3. **MEDIUM — receipt header requirement dropped in the nw1 prompt**: ExecCounterO's instructions ask only for raw stdout + `exit=<code>`; neither its prompt nor the counter emits measured-revision/counter-sha256 lines, so even the fresh receipt will be unbound to `c27a9fef…`/measured revision unless the executor adds the r61-style header. The counter's own docstring (accept-o.py:95-97) describes receipts that name both. Recommend the executor prepend `# measured revision <jj commit>` + `# counter sha256 c27a9fef…` to the installed copy.
4. **MEDIUM — claim wording overstates kill exclusivity**: "each fail exactly their pinned leg" — m5 demonstrably also fails EDGE_SCHEMEREL (verified above); the counter pins by *selection*, not exclusivity. Open finding; propose claim-text revision (pre-data, forcing control: this m5 cross-leg run), not a leg change.
5. **LOW — spec wording drift**: ExecCounterO's prompt asks to "verify the MUT leg lists all ten mutants m1..mread with pinned_fail=True each", a form the counter cannot print on PASS; reviewers should check `bad=[]` + complete `kill_evidence` instead (see Check 4).

## Verification gaps / residual risk

- Fresh run observed complete and green (`ACCEPT-O-64: PASS`, `exit=0`, all ten mutants in kill_evidence), but at last sample it lived only in `~/.cache/hyaku/kotodama-r64-w1/ExecCounterO/run-o.txt`; receipt installation is the executor's remaining step. CriticO is independently running `GEN,MUT` on a snapshot — its control receipts may cover part of the mut-o evidence under a different filename/path.
- m5's EDGE_SCHEMEREL cross-failure was observed only for m5; other mutants' cross-leg behavior was not exhaustively probed (the counter doesn't either).
- No tools installed (none needed; pacman guard respected — no pacman transactions attempted).
