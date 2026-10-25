# CritGaming2 — falsify seat, claim Ca (ACCEPT-CA-71), round 71 wave 2

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only; findings only).
Scratch: `/tmp/ca71/` — pristine copy of the 12 graded inputs, one mutation per case, counter pinned by sha256.
No tooling installed; no lane bytes written; no subagents.

## 0. Pinned state (the lane landed six commits under this review)

| item | value |
|---|---|
| HEAD at final pin | `e1d0d44` (matrix re-confirmed identical after `57e0a72` → `e1d0d44`; the counter and the six receipts are unchanged since `57e0a72`) |
| counter attacked | `reports/round-71/accept-ca.py`, sha256 `1ce25fb9ade45c263ba8ddec32f4fb73492ee5f0e82ef2e501bfa975fdcd2517` |
| frozen claim | `reports/round-71/claims.json` @ `65ff151` (unchanged since the pre-data re-freeze) |
| verdict table | `reports/round-71/telemetry/quarantine-verdicts.md`, 21 rows, 10 PRESENT · 7 REFUSED · 4 UNVERIFIABLE |

The matrix was re-run against **three** counter versions while the lane moved: `f706aacd` (committed at `7179d6d`), `f32a4075` (uncommitted intermediate), `1ce25fb9` (landed at `57e0a72`). The eight surviving holes are identical in all three; the numbers below are the `1ce25fb9` run. Everything the lane fixed mid-review is credited in §4, not reported as live.

Reproduce: `python3 /tmp/ca71/harness.py` — rebuilds the pristine copy from the lane, applies one mutation, runs the counter with `--root <scratch>`.

## 1. The four assigned mutations — all four behave as required

Baseline (unmutated scratch, `1ce25fb9`): `ACCEPT-CA-71: PASS`, exit 0.

| # | mutation | counter | exit | leg that fired |
|---|---|---|---|---|
| a | delete `# original bytes preserved below` from `reports/round-70/telemetry/measures-d.txt` | **FAIL** | 1 | `V70-1` |
| b | 26-word quote in the round-70 Gate S860 row (append ` extra`) | **FAIL** | 1 | `V70-3` (`words=26`) |
| c | drop verdict row `S835` | **FAIL** | 1 | `QUARANTINE` (`rows=20`) |
| d | duplicate verdict id `S776` (append a copy of its row) | **FAIL** | 1 | `QUARANTINE` (`rows=22 unique=21`) |

Control `e1` (60-word quote, no line shift) also fails `V70-3`, so (b) fails on the word count and not on incidental parse damage.

**These four sensitivities are real. They are not the problem.** Eight mutations violate the claim as written and leave the counter at `PASS`.

## 2. Blocking defects (all three reproduce at `57e0a72`)

### B1 — the frozen counting command cannot reach its own target

`reports/round-71/claims.json` → `claims.Ca.counting_command`, last leg, run verbatim from the lane root:

```
awk -F'|' '$1 ~ /S[0-9]+/ && $2 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/ {n++} END{print n+0}' \
  reports/round-71/telemetry/quarantine-verdicts.md
→ 0
```

With `-F'|'` on rows shaped `| S776 | PRESENT | … |` the fields are `$1=""`, `$2=" S776 "`, `$3=" PRESENT "` — the predicate addresses id and verdict one field early and can never count a row. Declared `target`: *"21 verdict rows with nonempty verdict labels"*; declared `kill_rule`: *"…or the verdict table not carrying 21 nonempty rows"*.

`accept-ca.py` uses the correct indices (`cells[1]`, `cells[2]`) and prints 21, so the claim carries **two instruments that disagree**, and the frozen one reads 0 on correct data. Every other leg of the same command hits its target: `6 6` (six files × six header lines), `acc2d614`→1, `NR==13`→25 words, trend→1, sweep→1, verdict→**0**.

### B2 — the `# counter sha256 (self)` field left its contract, and the lane's checker silently skips it

`corpus/QUALITY.md` criterion 17 requires the receipt to name *"the counter's sha256"*; `tools/check-receipt-seq.py:60` encodes exactly that (`SHA_RE`, `check_counter_sha` → `sha256(counter)`); the round-71 Ca receipt follows it. The six round-70 receipts instead record a third meaning:

```
# counter sha256 (self): e391f886…bd945  (round-70 claim Ca counting_command sha)
sha256(exact JSON string of reports/round-70/claims.json Ca.counting_command) = e391f886…bd945   MATCH
```

The value is reproducible, so it is not fabricated — but three defects remain:

1. **Contract drift.** One field means `sha256(counter script)` on round-71 receipts and `sha256(counting-command string)` on round-70 receipts; QUALITY 17 and the lane's parser still say the former. `check-receipt-seq.py receipt:counter` will compare the wrong object the moment the parenthetical stops breaking the regex.
2. **The check is skipped, not failed.** The trailing parenthetical violates `SHA_RE = ^# counter sha256 \(self\): ([0-9a-f]{64})\s*$`:
   ```
   parse_header(reports/round-70/telemetry/measures-ca.txt)['counter_sha'] = None
   python3 -B tools/check-receipt-seq.py --root . reports/round-70/telemetry/measures-ca.txt:reports/round-71/accept-ca.py
   → SEQ PASS / TREE PASS / RECEIPT-SEQ: PASS, exit 0      (no SHA leg printed)
   ```
   The tool's own docstring: *"A receipt missing a header line is a FAIL, not a skipped check."* A malformed line degrades to a skip, so the provenance tool now certifies receipts it never checked.
3. **Nothing recomputes it.** Mutation `n` — change a measured value below the marker (`unique_ids=10` → `unique_ids=99`) — leaves `ACCEPT-CA-71: PASS`, exit 0. V70-1's "original bytes preserved" is structural only.

The object the six receipts now pin is the **broken** round-70 counting command — the same string whose verdict leg prints 0 (B1). The stamp is honest about an instrument that cannot reproduce its claim.

### B3 — the class-admissibility rule was relaxed in the counter to admit a row the register classes forbid

`57e0a72` added a `class_ok` leg, then weakened it one commit later. Landed form:

```python
# payload-absent rows may be PRESENT/REFUSED (quote checked) or
# UNVERIFIABLE (source unfetchable/truncated, e.g. S791)
UNREACHABLE = {"S807","S812","S835"}
class_ok = all(r[1] == "UNVERIFIABLE" for r in rows if r[0] in UNREACHABLE)
```

The leg is now **one-sided**: it can only catch an unreachable-class row verdicted `PRESENT`/`REFUSED`; it can never catch a `payload-absent` row verdicted `UNVERIFIABLE`. The intermediate version (`f32a4075`) enforced both sides and failed on the live table (`class-ok=False`); the response was to relax the predicate, not to reconcile the record.

The record is still unreconciled:

- table header: *"21 data rows: 18 `payload-absent` + 3 unreachable-class"*;
- table contents: **4** `UNVERIFIABLE` rows — `S791, S807, S812, S835`;
- register: `S791` is `payload-absent` (`absent-defect-register.md:123`), and that class means *"cited source, companion URLs and local artifacts were all checked; the quote is in none of them"*;
- `S791`'s note: *"registry URL truncated, exact document unfetchable"* — which contradicts its own class, and is the sole justification the code comment now cites.

One of the two sentences must change: either `S791` is re-classed (and the header says 16 + 5, or 17 + 4), or it is re-verdicted `REFUSED` with the fetched-cleanly note. Carrying the exception in a code comment is not a reconciliation — and mutation `p` (three `PRESENT`→`REFUSED` flips, tally now wrong) passes, so the leg no longer discriminates.

## 3. Sensitivity holes that survive the landed counter (`1ce25fb9`)

Each row is a scratch mutation that violates the claim as written but leaves `ACCEPT-CA-71: PASS` (exit 0).

| # | mutation | why it survives | smallest fix |
|---|---|---|---|
| H1 | `e2`: quote inflated to 60 words **and one line inserted above the Gate table** | `V70-3` reads the hard-coded `r70[12]` (frozen command: `NR==13`); a line insertion makes it measure the `\|---\|` separator (`words=1`) | locate the row by content (`ROW_RE` + `"S860" in cells[1]`), then count `cells[3]` |
| H2 | `i`: `# tree:` header line deleted from the block, re-added as body prose | `has_all = all(line in data …)` is a whole-file substring test, not a header-position test | require the six lines as the first six lines (or the block immediately above the marker) with exact `# <field>:` prefixes |
| H3 | `j`: reject sweep hollowed to `rejected this round: none.`, the word `flip` left in an unrelated Mistakes row | `candidate_ok = re.search("flip", lt)` over the whole lesson file | require ≥1 line after the sweep carrying both a reason and a flip; reject `rejected this round: none` when a sweep is claimed |
| H4 | `k`: `acc2d614` moved out of S860's verify-at cell into the `teaches` cell | `"acc2d614" in s860[0]` — any cell | assert `"acc2d614" in cells[6]` (verify-at) |
| H5 | `l`: the whole `### Round-70 trend-correction row` block deleted, the phrase left inside a `D10` table row | substring test on `SCORECARD.md`; no row exists today — the record is a heading plus prose | require a table row whose first cell matches `round-70 trend-correction`, or rename the claim to "correction record" |
| H6 | `n`: a measured value below the marker changed | the digest is never recomputed (B2.3) | recompute the named digest and compare |
| H7 | `p`: three labels flipped `PRESENT`→`REFUSED`; the tally still reads 10/7/4 while rows read 7/10/4 | only row labels are read; the tally line is never parsed, and `class_ok` is one-sided (B3) | parse the tally, compare with row counts, restore the two-sided class test |
| H8 | `q`: a second S860 row written `\|S860\|…` carrying the stale `6cb51a4` | the duplicate filter is `line.startswith("\| S860 ")`, so a loosely-spaced duplicate is invisible to `len(s860) == 1` | match `ROW_RE` only (drop the `startswith`), then require exactly one match |

## 4. Verified correct, and credit for the mid-review fixes

- The four assigned sensitivities (§1) and the `V70-1` marker requirement.
- **Quarantine ids match the register exactly.** `awk -F'|' -v l=kotodama '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {gsub(/[^S0-9]/,"",$4); print $4}' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md | sort` → `diff` against the table's ids → `IDS-MATCH-EXACT`; row counts equal the closing tally (10/7/4).
- **Receipt revision/tree legs verify.** Measures: `stamped == evaluated == measured == 453676a2…`, `# tree: 7153d0d1…` = `git rev-parse 453676a^{tree}`. Controls: all three revisions `21e6a7f3…`, `# tree: ece8c7cd…` = `git rev-parse 21e6a7f^{tree}` — the base-stamp correction is sound.
- **Fixed during this review (no stale claim made):** at `1d1b432` four further holes survived — all 21 ids replaced by `S001..S021`, one id swapped to `S999`, the original first line gutted to `# xx`, the marker hoisted above the header block. `7179d6d` (hard-coded `SLICE`, `# after-state receipt`/`# pre-data control` prefix) closes all four; re-run at `1ce25fb9` they FAIL `V70-1`/`QUARANTINE` as they should.
- **Also fixed:** the six round-70 self-digests. At `1d1b432`/`2eb0183` they read `(digest of the preserved original bytes below the marker)` with a value matching no reachable preimage — preserved block `6f40598b…` vs claimed `3722a4a6…`, no round-70 counter ever existed (`git rev-list --all --objects | grep 'round-70/.*\.py'` empty), a cross-file permutation test hit nothing, and a scan of all 5 719 historical blobs under `reports/`, `corpus/`, `tools/`, `SKILL.md`, `SCORECARD.md` returned `HITS: NONE`. `f5c845b` replaced them with the reproducible counting-command digest (credit `RevReceipts`); the parser break and the missing recompute survived (B2).

## 5. Axis impact

- **Calibration (Ca):** blocked by B1 (instrument), B2 (field contract + vacuous check), B3 (one-sided class leg + unreconciled slice description). V70-3's measurement is address-fragile (H1); V70-5's sweep is a token, not a structure (H3).
- **Operability:** B2.2 is the worse half — `tools/check-receipt-seq.py` reports `RECEIPT-SEQ: PASS` on receipts whose counter-sha leg it silently skipped. The lane's provenance tool has been narrowed by a documentation edit.
- **Depth:** none. The table is a records surface.
- **Evidence (wave accounting):** unaffected; `CritQuarantineDesign`'s wave-1 class-semantics warning is still live and is now the only place the rule is stated two-sided.

## 6. Smallest safe correction set (ordered, each one line)

1. `claims.json` freeze record: fix the verdict leg to `$2 ~ /S[0-9]+/ && $3 ~ /^(PRESENT|REFUSED|UNVERIFIABLE)$/` and re-record the measured value (the counter already prints 21; no data changes).
2. Six round-70 receipts: one meaning for `# counter sha256 (self)` stated without breaking `SHA_RE` — either `sha256(counter)` per QUALITY 17, or a new line `# counting-command sha256:` — then show a `SHA-…` leg in `check-receipt-seq.py` output.
3. Verdict table header + `S791`: pick one — re-class `S791` as unreachable (header becomes 17 + 4 / 16 + 5, matching the 4 UNVERIFIABLE rows) or re-verdict it `REFUSED` with the fetched-cleanly note. Restore the two-sided `class_ok` (`f32a4075` form) once the record agrees.
4. `accept-ca.py`: recompute the named digest (H6), require header position (H2), parse the tally (H7).
5. `accept-ca.py`: content-locate the round-70 Gate row (H1), anchor `acc2d614` to the verify-at cell (H4), require a reason+flip candidate line (H3), require a real trend-correction row or rename the claim (H5), drop the `startswith` duplicate filter (H8).

## 7. Residual uncertainty

- A digest could in principle hash a worktree state never committed; that does not rescue B2 — the field now names a reproducible string while the parser still cannot read the line.
- `--lands` is accepted by `accept-ca.py` and printed, never graded (dead argument); `SLICE_IDS = None` and `ORIGINAL_FIRST = "# after-state receipt"` are dead constants (`ORIGINAL_FIRST` still dead at `1ce25fb9`). Three abandoned rigor hooks in a 130-line counter.
- I did not attack claims C or D; `RevCounterC`/`RevCounterDM` hold those. This matrix touches only `accept-ca.py` and its 12 inputs.
- The lane was landing commits every few seconds during this review (`1d1b432` → `64da9e1` → `7179d6d` → `e7e7e26` → `2eb0183` → `f5c845b` → `57e0a72`). Findings are pinned to `57e0a72` / counter `1ce25fb9`; a later commit touching the counter, the six receipts or the table invalidates the pin, not the method.

**Verdict: FAIL.** ACCEPT-CA-71 must not be admitted on `e1d0d44` (counter `1ce25fb9`): its frozen counting command prints 0 against its own target (B1), its receipts' provenance field left its contract and the lane's checker silently skips the leg (B2), and the class-admissibility rule was relaxed in code while the table's slice description still says 18 + 3 against 4 `UNVERIFIABLE` rows (B3). The four assigned mutations do fail correctly; the claim's problem is what it lets through, not what it catches.
