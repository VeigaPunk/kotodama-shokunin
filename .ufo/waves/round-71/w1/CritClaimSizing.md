# CritClaimSizing — round 71 wave 1 (leaf, read-only)

Scope: attack the declared sizes of claims C / Ca / D in
`reports/round-71/claims.json` (frozen at base `b94a543c`). All evidence below was
produced read-only on an extracted copy of the base tree (`git archive b94a543c |
tar -x -C /tmp/critbase71`) plus the committed control receipts. Tooling: none
installed (pacman paused; nothing needed).

---

## 0. Verdict summary

| Claim | Sizing verdict | Primary defect |
|---|---|---|
| C (coverage) | **Underdetermined** | The gap-sweep that is supposed to prove the void register prints a hit at base ("dance" inside "avoidance" in `funerary-material-culture.md`), so the claimed "before" is false; the entry's `- gap filled:` attestation would be self-falsifying. The remaining legs (entry exists, 35→36, 242→243, ≥12 new rows) are real work — not vacuous. |
| Ca (calibration) | **Underdetermined** | Four of six counter legs are word-presence greps / row counts that cannot verify the claimed substance; the V70-3 leg is **already true at base** (check-gate-quotes exits 0 on the unfixed 27-word quote), and the "original bytes below a marker" requirement has no counter leg at all. |
| D (depth) | **Underdetermined as written** | The no-git leg archives a fixed historical commit (`453676a2`) that cannot contain the new counter, so the declared counting command can never observe `SELFTEST: COULD-NOT-EVALUATE`; the target is mechanically unreachable under its own command. |

Do-nothing controls: all three fail to reach their targets (verified by rerunning on base), so no after-state is reachable by a pure do-nothing control — **except** Ca's V70-3 Gate-quote leg, which is already satisfied at base.

Causal entanglement: **C and Ca write the same files** — `corpus/SOURCES.md`, `corpus/lessons/round-71.md`, `SCORECARD.md` — and Ca also rewrites the telemetry receipt files (`reports/round-71/telemetry/controls-{c,d}.txt`) that serve as C's and D's committed control receipts. C's NOHARM exact-diff predicate is incompatible with Ca's co-writes (see §3).

---

## 1. Claim C (coverage) — underdetermined

### 1.1 Base facts (verified at b94a543c)
- `find corpus/knowledge/culture-material -maxdepth 1 -type f | wc -l` = **35** ✓
- inventory `totals.files` = **242** ✓ (so 243 after +1 is consistent)
- registry `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` = **784** ✓
- no `*danc*` file ✓; entry absent ✓

### 1.2 The gap sweep does NOT print nothing at base — the "before" is false
Run the claim's own sweep on base:

```
grep -rniE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md
→ corpus/knowledge/culture-material/funerary-material-culture.md:4:- topic: … (the death register: avoi[dance] terms, …
```

The single hit is the word **"avoidance"** in the funerary topic line — the substring pattern `danc` matches inside `avoidance`. So:

- The declared before ("`grep … prints nothing`") is **false at base** (exactly one line prints).
- The surface language claims "0 **word-bounded** … topic-line owners", but the implemented sweep is *not* word-bounded. A word-bounded pattern (`\b(danc|choreograph|…)\b`) would produce zero hits — i.e., the sweep as written does not implement the surface promise.
- The after-state requires the entry's `- gap filled:` line to name "the sweep that showed the gap". That attestation would be false: the sweep shows no gap (it shows one hit, which is not a dance/performance/movement owner).

Counterexample: land the entry with a `- gap filled:` line naming the declared sweep, cite 12 new rows, count 36/243/796 — the predicate passes while the claim's own premise ("prints nothing") is contradicted by base evidence.

**Smallest safe correction**: word-bound the sweep regex (or exclude `avoidance`), record the corrected sweep output in the control receipt (it currently omits the sweep leg entirely — the stored receipt is a hand-summary of 4 lines, not the command output), and require the `- gap filled:` line to reproduce the corrected sweep's zero-owner output.

### 1.3 Do-nothing control
Fails correctly: entry absent, 35/242/784. However the committed receipt `reports/round-71/telemetry/controls-c.txt` ends with a 4-line hand-summary (`culture-material: 35 / corpus: 242 / registry: 784 / entry-absent: absent`) — it is not the raw command output (the commands print JSON + counts + sweep output), and it suppresses the sweep leg which would have shown the false-positive hit. This violates the declared green/do-nothing contract ("output is committed as the receipt").

### 1.4 Vacuity
The two count legs alone (36 files, corpus 243) are trivially reachable by adding any one file to the partition, but they are not the binding constraints; the entry-exists, ≥12-new-rows, check-cited-lines and NOHARM legs are substantive. Sizing is acceptable apart from §1.2.

---

## 2. Claim Ca (calibration) — underdetermined

### 2.1 Base facts (verified at b94a543c)
- `grep -c 'acc2d614' corpus/SOURCES.md` = **0**; S860 row names `6cb51a4` (1 hit) ✓
- `grep -c 'trend' SCORECARD.md` = **0** ✓
- `reports/round-71/telemetry/` does not exist at base (the six files the counter greps are absent → the raw command errors, it does not print 0s)
- round-70 telemetry exists: `measures-o.txt` header `# after-state receipt O — measured at lane 6cb51a4+landed edits, …`; `controls-ca.txt` header `# pre-data control Ca (do-nothing) - measured at base 21e6a7f …` — single-line headers, no 17/19 block ✓ (V70-1 before confirmed for round-70 files)

### 2.2 Target-file ambiguity: the counter checks round-71 files, the before describes round-70 files
The predicate/counting-command grep `reports/round-71/telemetry/{measures,controls}-{o,ca,d}.txt` (created this round), while the "before" describes the **round-70** receipts (`reports/round-70/telemetry/…`), which are the files V70-1 flags. Two materially different implementations satisfy the prose:
- (i) edit the **round-70** receipts in place — violates the freeze rule ("no frozen byte of any filed round is rewritten") and the non-goal on filed round-70 bytes; the counter would see nothing change in round-71 files → fail;
- (ii) create **round-71 copies** with the header — passes the counter, but the round-70 originals remain headerless, so the V70-1 defect is not actually repaired.
The claim does not say which; the counter cannot distinguish. **Underdetermined.**

### 2.3 V70-3 leg is already true at base (premature saturation)
The round-70 lesson Gate still contains the 27-word quoted span (line 13 of `corpus/lessons/round-70.md`: the S860 quote `"A row whose used-by names a path …"` = 27 words, whitespace-split). The claim's own checker, run on base:

```
python3 -B tools/check-gate-quotes.py corpus/lessons/round-70.md
→ GATE_QUOTES: 0 findings; exit 0
```

The tool merges quoted spans separated by prose into separate runs, so the 27-word quote passes its run-merge word count. Consequently:
- The after-leg "check-gate-quotes exits 0 with 0 findings" is **already satisfied at base** — a do-nothing control reaches it.
- The counter cannot detect the V70-3 defect it is meant to verify. Concrete counterexample: land a clean round-71 lesson, leave the round-70 27-word quote untouched → counter passes, V70-3 unrepaired.
- The claim's gloss "(whitespace split, checked by tools/check-gate-quotes.py)" conflates raw whitespace-split word counting with the tool's run-merge semantics — the tool is not the whitespace-split check the phrasing promises.

### 2.4 Unenforced after-state: "original bytes preserved below a marker"
The after-state requires the six receipts to carry the header "with original bytes preserved below a marker". Neither the counting command nor the kill rule checks this: the counter only greps for six `# …` header lines (36 matches). A claim could overwrite the six files with header-only content and pass every counted leg. **Underdetermined.**

### 2.5 Word-presence greps pass vacuously
- `grep -c 'trend' SCORECARD.md` ≥1 — satisfied by *any* occurrence of the word "trend" anywhere in the scorecard, not by a specific round-70 trend-*correction* row (e.g., a "trend: none" note would pass).
- `grep -cE '^(reject|rejected)' corpus/lessons/round-71.md` ≥1 — satisfied by any line starting with "reject", anywhere in the lesson, not necessarily a Gate reject-sweep statement; a line like "rejected alternative: …" passes.
- Verdict table: `awk -F'|' 'NR>1 {print $1}' | wc -l` counts every line after row 1 — including markdown separator rows (`|---|---|`) and rows with empty verdict labels. The "21 nonempty rows" target can pass with 20 verdicts + 1 separator/blank line. The kill rule says "21 nonempty", but the counter does not enforce nonemptiness.

### 2.6 Control receipt fidelity
`controls-ca.txt` is a hand-written 5-line summary, not the raw command output (the raw command errors on the three missing `measures-*` files; it cannot print "0" for them). Also note the target "36 matches" assumes exactly six header lines per file; the kill rule is "missing any of the six header lines" — duplicated header lines over-count and are unguarded.

**Smallest safe corrections**: (1) fix the target path set: either state plainly that round-71 copies are created (and stop describing round-70 files as the fixed objects), or — if round-70 files are in scope — get an explicit freeze exemption; (2) add a counter leg that asserts the marker line and verifies the bytes below the marker equal the original receipt's bytes (e.g., sha256 of tail); (3) replace `grep -c 'trend'` with an anchored row pattern (e.g., line containing both `round-70` and `correction`); (4) anchor the reject-sweep check to the `## Gate` section; (5) count verdict rows as `awk -F'|' 'NR>1 && $1 ~ /[^[:space:]]/'` excluding separator lines; (6) for V70-3, check the round-70 lesson with a plain whitespace-split word count of each quoted span (≤25), not the run-merge tool.

---

## 3. Causal entanglement: C ↔ Ca (same files)

Both claims write:
- `corpus/SOURCES.md` — C appends ≥12 new rows; Ca repoints S860's verify-at cell (edit of an existing row);
- `corpus/lessons/round-71.md` — C appends the lesson (NOHARM allows "lesson appends"); Ca writes the Gate reject-sweep statement + candidate;
- `SCORECARD.md` — C appends (NOHARM allows "scorecard appends"); Ca adds the trend-correction row.

Additionally, Ca's header fix targets `reports/round-71/telemetry/{measures,controls}-{o,ca,d}.txt`, which includes `controls-c.txt` and `controls-d.txt` — the committed **control receipts of claims C and D**. Ca rewrites those files (adding the six-line header above the original bytes), i.e., Ca mutates the evidence artifacts other claims' green controls describe.

Concrete failure mode: C's predicate requires "NOHARM sweep diff = exactly the new entry + the new rows + README/lesson/scorecard/log appends". If Ca's S860 edit, lesson Gate text, scorecard row, or receipt-header rewrites are present in the same diff (or land before C's NOHARM snapshot), C's exact-diff equality breaks and **C cannot pass** regardless of C's own work. Ca has no NOHARM leg, so the entanglement is asymmetric: the two claims cannot both pass as declared unless the NOHARM baseline explicitly excludes Ca's files/cells, or the claims land as one integrated commit with a reconciled NOHARM allowance. The claims.json freeze does not specify any such reconciliation.

**Smallest safe correction**: define the NOHARM diff algebra over per-claim ownership (document which files each claim may touch, e.g., Ca owns `SOURCES.md` S860 cell only), or scope C's NOHARM to corpus-paths plus strictly-append-only tops, and sequence Ca after C (or jointly commit) with the receipt-header rewrite treated as owned by Ca.

D writes only `reports/round-71/accept-d.py` (+ its control receipt) — no shared file with C/Ca, except that Ca's header rewrite touches `controls-d.txt`.

---

## 4. Claim D (depth) — mechanically unreachable no-git leg

### 4.1 Verified
- `git rev-parse --verify 453676a2363c97e158cb112c9588906564d95a21` succeeds; `git ls-tree -r 453676a2` contains `reports/round-69/accept-d.py` and **no** `reports/round-71/` path.
- The declared counting command's no-git leg: `git archive 453676a2 | tar -x -C $T; cd $T; python3 -B reports/round-71/accept-d.py --selftest; echo EXIT=$?` — inside `$T` the file `reports/round-71/accept-d.py` does not exist, so python exits 2 with `can't open file …` and prints **no** `SELFTEST: COULD-NOT-EVALUATE (no git)` line.
- The target requires both exit 2 **and** the SPEC string. The leg can therefore never pass, and equally never fail on the intended ground: the counter cannot measure the new counter's no-git behavior at all. (Note the exit-code coincidence: missing-file python also exits 2, so a grader keying only on `EXIT=$?` would be fooled into a pass — the string leg is the only discriminator and it is unreachable.)
- The in-repo leg and the frozen data-predicate leg are well-formed and substantive; the D control receipt is verbatim and reproduces the frozen false red (`SELFTEST: 1/2`, REAL_EXIT=1) correctly.

### 4.2 Correction
The no-git scratch must be produced from the **landed** tree, not a fixed historical commit: e.g., `git archive HEAD` (or `git archive $(git rev-parse HEAD)`) after landing, or `cp -a` of the working tree minus `.git`. Keep `453676a2` only for the frozen-counter reproduction portion (the control leg that shows the false red). The counter module itself (current draft in the worktree) implements the no-git guard correctly (`_has_git_dir()` → SPEC + exit 2); only the harness wiring is broken.

---

## 5. Do-nothing control summary

| Claim | Base rerun matches declared control? | Reaches after-state? |
|---|---|---|
| C | Counts yes (35/242/784, entry absent); sweep leg omitted from receipt and, when run, prints one false-positive hit | No |
| Ca | acc2d614 0, trend 0, lesson/verdict absent — yes; but raw command errors on missing files rather than printing 0, and V70-3 leg already passes at base | No (but V70-3 leg already true) |
| D | New counter absent; frozen false red reproduced (1/2, exit 1) | No |

---

## 6. Impacted axes

- **coverage (C)**: before-truth / gap provenance — the sweep is not word-bounded and hits `avoidance`; the entry's gap-filled attestation is falsifiable at base.
- **calibration (Ca)**: counter-predicate fidelity — V70-3 leg saturated at base; original-bytes preservation unmeasured; word-presence greps pass vacuously; target-path ambiguity vs freeze rule.
- **depth (D)**: counter harness reachability — no-git leg cannot execute the new counter as written.
- **entanglement (C↔Ca)**: shared writes to `SOURCES.md`, round-71 lesson, `SCORECARD.md`, and telemetry receipt files; C's NOHARM exact-diff cannot coexist with Ca's writes as declared.
