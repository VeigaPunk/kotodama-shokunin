# RevCounterPredicates — round-71 frozen-claim adversarial review

Seat: L1Kotodama71.RevCounterPredicates (leaf, read-only on claims.json).
Frozen source: `reports/round-71/claims.json` (claims C, Ca, D). Base tree materialized in scratch from `base_revision` b94a543c70f40dba7e49fff96d05bfb8bbd8c678 (git archive → /tmp/revcounter); all declared counting commands were run verbatim there (and in-repo where .git is required).
No tools installed (nothing needed).

---

## Claim C (coverage) — verdict: **defect-with-fix-suggestion** (numeric predicate frozen; two clauses unenumerated, one label missing)

1. Pasteable / runs on base — PASS. Verified on base tree:
   - `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → exit 0, JSON `totals.files=242`. NOTE: with `--json --summary` the human summary (`culture-material: 35` etc.) is **not** printed; the summary lines in `telemetry/controls-c.txt:3910-3913` were appended outside the declared command. `culture-material` count is not printed by any leg either (only derivable by counting the JSON `files` array / `find|wc`).
   - `find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l` → 35.
   - `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 784 (matches registry baseline).
   - `python3 -B tools/check-cited-lines.py ...dance-performance-movement-codes.md` → `CITED_LINES_ERROR no such file or directory`, exit 2.
2. Target concrete / re-derivable — PASS: 36 (find/wc), 243 (JSON totals.files), ≥796 S-rows (grep), exit 0.
3. Do-nothing control fails to reach target — PASS (verified): 35≠36, 242≠243, 784<796, entry absent → check-cited exit 2.
4. Universal clauses:
   - "each cited row's quote is opened and quoted in the round lesson Gate" — universal over cited rows; **no leg enumerates the citations or verifies the quotes in the lesson Gate** (unenumerated in command; relies on manual sweep).
   - "every row's used-by path exists" — **no leg verifies used-by existence**. `tools/check-cited-lines.py` only lints MULTI-ID/TABLE-ID lines (see source: it returns findings for multi-source-id lines / table rows and fails on missing input; it does not check SOURCES rows or used-by paths). This kill-rule clause is unsupported by the declared command.
   - "NOHARM sweep diff = exactly …" — not produced by the command (appended manually).
5. Predicate sentence vs receipt label — counts label-match, but "check-cited-lines exit 0" has **no printed label**: the command never echoes `$?`, so the receipt text cannot contain the exit-0 fact (only the last leg's shell status carries it).

Fix suggestion: add an enumeration leg, e.g.
`grep -oE 'S[0-9]{3,}' corpus/knowledge/culture-material/dance-performance-movement-codes.md | sort -u` and for each id assert the row exists in `corpus/SOURCES.md` with `status=mined` and `used-by` containing the entry, and that every used-by path exists (e.g. reuse `tools/check-supersession-settlement.py` semantics or a small loop); append `; echo CC_EXIT=$?` to the command to emit the exit label.

---

## Claim Ca (calibration) — verdict: **defect-with-fix-suggestion** (three concrete gaps)

1. Pasteable / runs on base — PASS (Bash brace expansion; all six legs execute). Base values: leg1 grep → 0 matches, exit 2 (six round-71 files absent); leg2 `acc2d614` → 0; leg3 gate-quotes → `GATE_QUOTES_ERROR … unreadable` + `GATE_QUOTES: 0 findings`, exit 2; leg4 `trend` → 0; leg5 `^(reject|rejected)` → 0 (lesson absent); leg6 awk → fatal open error, wc 0.
2. Target concrete — PASS: 36 matches; S860 acc2d614 ≥1; gate-quotes exit 0 + 0 findings; trend ≥1; reject ≥1; 21 verdict rows.
3. Do-nothing control fails — PASS (verified): all six legs below target.
4. Universal clauses:
   - "all six receipts have the six-line header … and the original bytes below the marker" — leg1 aggregates counts across the six files (`grep -cE … f1..f6`): a state with all 36 matches inside one file and the other five stripped **passes the 36 target** while violating the predicate. Per-file distribution is not asserted. Fix: `for f in reports/round-71/telemetry/{measures,controls}-{o,ca,d}.txt; do grep -cE '^# (counter sha256|stamped revision|evaluated revision|measured revision|tree|worktree dirty)' "$f"; done` and require 6 each.
   - "and the original bytes below the marker" — **no leg detects deletion of the preserved bytes** (the strip-bytes mutant passes). Fix: require the marker line plus a byte-preservation check (e.g. size floor or diff against the base blobs).
   - "the 21-row verdict table … with every row having a verdict label" — `awk -F'|' 'NR>1 {print $1}' | wc -l` counts rows regardless of whether the first cell is empty; an empty-label row still counts. Fix: `awk -F'|' 'NR>1 && length($1)>0 {n++} END {print n+0}'` = 21.
   - "SCORECARD.md carries a round-70 trend-correction row" — `grep -c 'trend'` only proves ≥1 occurrence of "trend", not that it is a round-70 correction row (weak, note).
   - "lesson Gate … carries >=1 candidate with reason+flip" — `grep -cE '^(reject|rejected)'` does not check the candidate/rip clause (note).
5. Predicate vs receipt labels — leg3 prints `GATE_QUOTES: 0 findings` matching the sentence; remaining counts label-match once the fixes above are in.

---

## Claim D (depth) — verdict: **defect-with-fix-suggestion** (declared counting command cannot reach its own target)

1. Pasteable / runs — the command parses, and counter logic is sound, but leg2 as declared is broken:
   - Leg2 archives the hardcoded old revision `453676a2363c97e158cb112c9588906564d95a21` (round-70 records commit). Verified: `git archive 453676a2 | tar -t` contains `reports/round-69/accept-d.py` but **no `reports/round-71/` at all**. Running the declared command in-repo produced `python3: can't open file …/reports/round-71/accept-d.py`, `EXIT=2`, and **no `SELFTEST: COULD-NOT-EVALUATE (no git)` line**. The no-git target sentence is unreachable via the declared command (the exit-2 comes from file-not-found, not from the guard; the kill rule "no COULD-NOT-EVALUATE line" would fail).
   - The new counter itself is correct: in a true .git-less copy of the current tree it prints `SELFTEST: COULD-NOT-EVALUATE (no git)` and exits 2 (verified); in-repo leg1 prints `SELFTEST: 2/2` exit 0 (verified); leg3 frozen prints `ACCEPT-D-69: PASS legs=8/8` exit 0 (verified).
2. Target — "no-git exit 2 + COULD-NOT-EVALUATE" is **not attainable** from the declared command (see above); the other two legs are concrete and met today.
3. Do-nothing control — fails to reach target (PASS): at base the round-71 counter is absent (legs 1–2 file-not-found; leg3 frozen still 8/8 PASS). **Fidelity defect**: committed `telemetry/controls-d.txt` does not run the declared counting command — it substitutes `python3 -B reports/round-69/accept-d.py --selftest` in the no-git copy (frozen counter), so the recorded control evidence is not the declared command's output.
4. Universal clauses — none problematic (all references are singular / enumerated).
5. Predicate vs receipt labels — leg1 prints `SELFTEST: 2/2` ✓; leg3 prints `ACCEPT-D-69: PASS legs=8/8` ✓; leg2 cannot print `COULD-NOT-EVALUATE` ✗. (Note: no leg emits the `ACCEPT-D-71:` label itself; same situation as round-70, whose receipts also carried no ACCEPT line — convention note, not graded as defect.)

Fix suggestion: replace `git archive 453676a2363c97e158cb112c9588906564d95a21` with `git archive HEAD` (or `git archive $(git rev-parse HEAD)`) so the extracted tree contains `reports/round-71/accept-d.py`; keep `echo EXIT=$?`; and regenerate `controls-d.txt` from the actual declared command.

---

## Residual risk / verification gaps
- After-state receipts do not exist yet (pre-data); point 5 was checked against the declared commands and the round-69/70 receipt conventions. The control receipts are curated summaries, not raw transcripts of the declared commands (e.g. `controls-c.txt` summary lines and `controls-d.txt`'s substituted leg), so "the label the receipt prints" was interpreted as the declared command's observable output.
- Round-70 used identical freeze-rule wording ("predicate sentence in the plan is the same sentence the receipt prints") while its receipts contained no ACCEPT label; I treated exact-label emission as convention, not defect.
- `reports/round-71/accept-ca.py` appeared in the working tree during this review (draft executor artifact); claims.json untouched (verified read-only).
