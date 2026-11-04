# SentinelGrammar — adversarial probe report (Kotodama r82, hyaku run 15, milestone r82-v1)

**Seat:** SentinelGrammar (leaf, read-only probe; no delegation, no background mutation).
**Hypothesis under test (falsifiable):** every `recheck` cell in `corpus/SOURCES.md` at lane base revision `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` is machine-parseable under the declared grammar (`on-release` | `NNd` | ISO date), and every `opened` cell is an ISO date.
**Verdict: hypothesis HOLDS.** Parse-failure list is empty over the full table. One operability trap found that the O seat must respect (blank-line table split, §3).

## 0. Input and integrity

- Registry bytes read at base rev (command): `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/SOURCES.md`
- 991457 bytes — python `len(blob)`; sha256 `2f60171c8879f99e690f15403985c240a0b80def31b003e4862272b92f108263` — `sha256` of the same blob; 960 lines — `blob.count(b'\n')`.
- Base commit: `c285b2afb19d4b64320e18df1f55e426bf2d0b0c 2026-11-01 17:44:19 +0000 round-81 verifier spot-check (integrator, hyaku): non-author admit/reject` — `git log -1 --format='%H %ci %s' <rev>`.
- Parser: independent, written for this probe in scratch (`stage/SentinelGrammar/probe_parser.py`, sha256 `15c52faff7b0a26f6ae34158613715437c7113f1edb3f3b03d42ad238810d93e`); NOT the round's tool. Runtime: Python 3.14.8 — `python3 --version`. No tools were installed (nothing to record under the tooling authorization).
- The probe did NOT execute the draft `tools/check-sources-recheck.py` (sentinel bound: no invoking another runtime). Draft-tool behavior claims in §7 are ExecEvidence's, relayed with that provenance.

## 1. Parse-failure list and value histograms (expect-empty met)

- Parse failures: 0 — `probe_parser.py --registry <blob> --as-of 2026-11-04 --window 90` → `== PARSE FAILURES (0) ==` (raw output: `stage/SentinelGrammar/receipt.asof-2026-11-04.txt`).
- Data rows: 827 — same run, `data rows=827 — lines 30..859`. Cell-count histogram `{11: 827}`; malformed pipe lines 0; ids 827 distinct, all `^S\d{3}$`, no duplicates.
- recheck forms: `{Nd: 659, ISO: 154, on-release: 14}` — same run. Distinct recheck values exactly 6: `180d` 249, `365d` 392, `90d` 18, `on-release` 14, `2027-10-22` 42, `2027-10-23` 112. Nd cadence set exactly `{90, 180, 365}`, min 90, max 365.
- opened: all 827 valid ISO; 10 distinct dates, min `2026-10-19`, max `2026-11-01`; all in 2026.
- status context: `{mined: 732, queued: 58, rejected: 37}` — rejected rows are registry rows and are included in `rows` (contract: rows = rows parsed; it does not exclude rejected).
- Independent cross-check, different mechanism, agrees exactly: `grep -c '| on-release |'` → 14; `grep -c '| 90d |'` → 18; `| 180d |` → 249; `| 365d |` → 392; `grep -cE '\| 2027-10-2[23] \|'` → 154; opened-cell greps `| 2026-10-19 | (…)` → 47 and `| 2026-11-01 | (…)` → 3 — all against the staged blob.
- Case-variant sweep for `on-release` (On-Release / ON-RELEASE / on_release): covered by the parser's exact-value histogram (6 distinct values, 0 failures ⇒ no other spelling exists in the file). Negative claim, sweep = the exact-value histogram in the raw receipts.

## 2. Queue the tool will print (base-rev data)

- as-of 2026-11-04, window 90 (horizon 2027-02-02) — `probe_parser.py … --as-of 2026-11-04 --window 90`:
  `RECHECK-QUEUE: 0 due / 18 upcoming / 14 on-release / 827 rows`
  The 18 upcoming are the `90d` rows (due 2027-01-17 ×7, 2027-01-20 ×7, 2027-01-22, 2027-01-23 ×2); full `UPCOMING` list in the receipt.
- as-of 2027-11-01, window 90 (horizon 2028-01-30) — `probe_parser.py … --as-of 2027-11-01 --window 90`:
  `RECHECK-QUEUE: 813 due / 0 upcoming / 14 on-release / 827 rows`
  827 − 14 on-release = 813; max due date is 2027-10-24 < as-of. The tool will print 813 `DUE` lines — volume is per contract. Full list in `receipt.asof-2027-11-01.txt`.
- Post-base observation (not in the numbers above): S904–S906 (planned opens 2026-11-04) do not exist at the base rev (max id S903; max opened 2026-11-01). With the contract's inclusive horizon, a row opened on as-of 2026-11-04 with `90d` gets due_date 2027-02-02 = horizon exactly → counted `upcoming`, not `due`. Derivation from the stated contract, flagged for the O seat's fixtures.

## 3. Operability trap found by this probe: the registry table is not contiguous

- The table is split by 3 blank lines into 4 blocks: lines 30–704, 706–786, 788–852, 854–859 — parser output `contiguous table blocks` / `block gaps [(704, 706), (786, 788), (852, 854)]`; `grep -c '^|'` → 829 (header + separator + 827 rows).
- Exploit path: a row-walk that stops at the first non-pipe line (the blank at line 705) silently parses only 675 of 827 rows and prints a confident wrong queue (`0 due / 15 upcoming / 14 on-release / 675 rows` — this probe's own first run did exactly that before being fixed to scan all pipe lines).
- Smallest remediation: `tools/check-sources-recheck.py` must scan every pipe-starting line in the file (or skip blank lines inside the table) rather than break at the first blank. The draft tool already survives it (its queue receipts agree with mine at 827 rows — ExecEvidence, §7).

## 4. Degenerate cases the grammar hides (honest answers; no rule invented)

- `0d` cadence: does not exist — sweep is the Nd cadence histogram over all 659 Nd rows (`{90: 18, 180: 249, 365: 392}`, min 90). If it existed, the contract already determines it: `0d` → due = opened + 0 = opened → due at any as-of ≥ opened. Deterministic; no special case needed; untested by real data (optional fixture).
- `3650d` cadence: does not exist (max N is 365 — same histogram). Would parse (`\d+d`) and land outside any window; counts only toward `rows`. Deterministic; untested by real data.
- `opened` after an absolute `recheck` date: does not exist — sweep is the degenerate scan over all 154 ISO-recheck rows (`ISO-recheck rows with recheck date BEFORE opened: 0`). If it existed, the contract still decides deterministically: due = the ISO date, so the row is due from before it was opened. The honest answer: the grammar/contract leaves nothing undefined here; these cases are simply unexercised by real data, so any specific desired behavior is a policy choice that belongs in fixtures, not in invented tool logic.

## 5. Leading spaces (census grammar's 0–3 tolerance)

- Leading-space histogram over all 829 pipe lines: `{0: 829}`; rows with 1–3 leading spaces: 0; rows with >3: 0; rows with a leading TAB: 0 — parser `== TABLE SCAN ==` block (raw receipts).
- Therefore the 1–3-leading-space branch of the O contract ("parses the 11-cell Registry rows (0-3 leading spaces)") is **untested by real data** — every real row is flush-left. Recommended fixture for `--selftest`: a registry whose row is indented by exactly 2 spaces must parse identically to the flush-left row (same counts, same due classification); and, recommended, a 4-space-indented row is a CommonMark code block and must NOT be parsed as a row.

## 6. Consistency observation (not a parse defect)

Rows opened 2026-10-22/23 express the same one-year recheck in two spellings: 154 absolute ISO cells (`2027-10-22` ×42 = 2026-10-22+365, `2027-10-23` ×112 = 2026-10-23+365) alongside `365d` cadence rows from the same cohorts. The grammar handles both; nothing for the tool to do. Recorded so nobody "normalizes" one into the other by accident.

## 7. Cross-seat coordination (read-only)

- ExecEvidence's independent probes reproduce my queue numbers exactly at both as-of dates (`0/18/14/827` and `813/0/14/827`) — three-way agreement (their probes, my parser, the draft tool). Their full receipts: `.ufo/waves/round-82/w1/ExecEvidence.md`.
- Their reported selftest fixture bug describes an older snapshot: draft line 253 currently reads `row("S911", "2026-01-01", "30d")[:-1] + "| extra |"`, which already contains the fix they prescribed and splices into 12 cells (string arithmetic against `row()` at lines 169–172, which ends `" - |"`). Relay of their unrun-by-me draft-tool claims: 12-cell, 10-cell, and `fortnight` cadence all exit 2 with `RECHECK-ERROR`, no traceback — consistent with the contract, verified by them, not re-run by me.

## 8. Files written by this seat (all absolute)

1. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/SentinelGrammar/probe.md` — parser inline + both raw outputs verbatim (37705 bytes).
2. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/SentinelGrammar/probe_parser.py` — the independent parser (receipt copy).
3. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/SentinelGrammar/receipt.asof-2026-11-04.txt` — raw output, exit 0.
4. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/SentinelGrammar/receipt.asof-2027-11-01.txt` — raw output, exit 0.
5. `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/SentinelGrammar.md` — this report.

## 9. Checks not run

The draft tool itself was never executed by this seat (bound), so draft-side selftest status is reported as relayed (§7), not re-verified. All other claims above carry the command that produced them.
