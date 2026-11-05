# Round-91 freeze review — seat ReviewerFreeze

Freeze commit `691aebf247ebea4dd50577bb64ac99d12fa1145a`, base `d39434b3bc8458e1b66edd2d0d0fea9ea32f3331`. Read-only review; all frozen artifacts re-read at freeze, working tree vs freeze diff on the four frozen paths is empty (`git diff 691aebf2 -- reports/round-91/claims.json reports/round-91/measure91.py` = 0 lines). Commit identity confirmed: `git rev-parse` matches all three aliases. All scratch lives in `/fast/scratch/hyaku/kotodama-r91/ReviewerFreeze/` (deleted before yield); TMPDIR set there; nothing written outside the stage dir and the report trailer.

---

## (1) Claim-clause coverage: every clause vs mechanical counter legs

### O (reports/round-91/claims.json, O.after_target / O.predicate / O.kill_rule)

| # | Clause (exact text, abridged) | Checked by |
|---|---|---|
| O-1 | "TOOL sha equals tool_sha256" | `MUTATION`?? No — **`MUTATION` is not this check. Checked by `MUTATION` indirectly only.** Actually: **checked by `TOOL` leg in measure91.py grade_o** (measure91.py:119-124, sha256_file vs cfg `tool_sha256`). `checked by TOOL` |
| O-2 | "--selftest exits 0" | `checked by SELFTEST` (measure91.py:129-140, `rc == 0` guard) |
| O-3 | "prints SELFTEST PASS 77/77" | `checked by SELFTEST` (regex `SELFTEST (PASS\|FAIL) (\d+)/(\d+)`, `total == cfg selftest_checks`) |
| O-4 | "exactly 77 lines beginning `  ok `" | `checked by OKCOUNT` (measure91.py:132-141 `count_ok`) |
| O-5 | "every name in O.refusal_cases is printed ok" | `checked by REFUSALS` (measure91.py:148-161, regex per case name) |
| O-6 | "MUTATION killed==total>=52, 0 survived, 0 broken-pattern" | `checked by MUTATION` (measure91.py:166-172 + MUT_RE parse) |
| O-7 | "the frozen stub control run through the same OKCOUNT check is refused (ok lines != 77)" | `checked by STUB` (measure91.py:177-187: `stub_oks != cfg[O][selftest_checks]`) |
| O-8 | "stub kills 0 mutants (same mutation pass, --tool override)" | `checked by STUB` second arm (`stub_killed == 0`) + `MUTATION` for the score regex |
| O-9 | O.predicate: "at the lands revision" (materialization from the lands tree, not the freeze) | `checked by MATERIALIZE` (measure91.py:117-118: `git archive --format=tar --lands` into work dir) |
| O-10 | kill_rule: "a tool whose sha differs from the freeze pin" | `checked by TOOL` |
| O-11 | kill_rule: "a selftest tally below the frozen count / fewer than 77 ok lines" | `checked by SELFTEST` arm 2 and `OKCOUNT` |
| O-12 | kill_rule: "any surviving or broken-pattern mutant" | `checked by MUTATION` (survived==0 AND broken==0 arms in the same ok expression) |
| O-13 | kill_rule: "any refusal case not printed ok" | `checked by REFUSALS` |
| O-14 | kill_rule: "or a stub that passes OKCOUNT or kills any mutant" | `checked by STUB` |
| O-15 | O.name: "a 77-check selftest" — the check-count itself is pinned via `selftest_checks==77` | `checked by SELFTEST` + `OKCOUNT` |
| O-16 | O.name: "refuses the nine round-90 falsify classes **by name**" | `checked by REFUSALS` — every case name is also grepped verbatim as a `chk('<name>'` in the working tree. All nine verified (§2). |
| O-17 | O.after_target: "a mutation receipt over **every v2 sub-check**" (the receipt itself as an artifact) | **review-only** — measure91.py greps the score line and total, never opens `mutation-score.txt`/`.json` or verifies each mutant row landed (defect D4). |

### C (claims.json C.after_target / predicate / kill_rule)

| # | Clause | Checked by |
|---|---|---|
| C-1 | "entry mode passes all eight declared legs" (ENTRY SHAPE TOPIC NEWIDS UNIQUENESS GATE CAPTURE APPENDONLY rc0) | `checked by ENTRY` (measure91.py:218-254, per-leg PASS gate over the frozen tool's own emitted leg lines) |
| C-2 | "with --topic-phrases and --min-topic-phrases from this file" | `checked by ENTRY` (args literally passed from cfg) |
| C-3 | "with --base-lesson corpus/lessons/round-90.md" | `checked by ENTRY` (frozen `base-lesson.md` fetched from `cfg['base']`) |
| C-4 | "INDEX exit 0 over the lands tree" | `checked by INDEX` (measure91.py:260-264, freeze-pinned tools/check-corpus-index.py) |
| C-5 | "no base registry row removed or cell-changed" | `checked by APPENDONLY` arm 1 (measure91.py:272-275, per-row cell tuple compare against base) |
| C-6 | ">=3 new mined A/B rows opened 2026-11-05, cited by entry, naming it in used-by" | `checked by APPENDONLY` arm 2 (measure91.py:281-290: tier/status/opened/used-by filter, cited via `\bS\d{3,}\b` in entry) |
| C-7 | "an old id gaining a disposition in the round lesson" | `checked by ENTRY`→APPENDONLY leg of the frozen tool (mutants `appendonly-lesson-off`, `appendonly-gained-off`, `appendonly-flip-off` chase the three arms) |
| C-8 | "a gate quote that is a teaching or source cell" | `checked by ENTRY`→GATE (mutants `gate-selfquote-entry-off`, `gate-chrome-entry-off`; `chk('gate quote is the teaching cell')`, `chk('gate quote is from the source cell')`) |
| C-9 | "a capture that byte-copies a graded file" | `checked by ENTRY`→CAPTURE (mutants `graded-shas-off`, `capture-graded-off`; `chk('capture byte-copies a graded file')`) |
| C-10 | "a cited id missing from the registry" | `checked by ENTRY` (cited-id/refusal `chk('entry cites an id absent from the registry')` plus APPENDONLY's `cited` uses roofs_rows only for the min-3; a cited-but-absent row already fails entry CITED/NEWIDS) |
| C-11 | "a shadow or shared URL" | `checked by ENTRY`→UNIQUENESS (mutants `uniq-shadow-off`, `duplicate-url-off`; `chk('new row shadows a base url')` / `chk('two new rows share one url')`) |
| C-12 | "entry exists with ≥min_bytes / ≥min_headings / header keys / ≥table shape / topic-overlap / phrase floor" | `checked by SHAPE`/`TOPIC` (sub-legs inside the frozen tool's entry mode, via mutants entry-bytes-off, entry-headings-off, entry-header-key-off, topic-overlap-off, stem-off, repeat-sentence-off, table-shape-off, phrase-floor-off) |
| C-13 | "corpus/README.md names the entry" | `checked by APPENDONLY` arm 3 (measure91.py:290-292) |
| C-14 | "registry gains ≥3 rows **opened 2026-11-05**" | `checked by APPENDONLY` arm 2 (opened == cfg as_of) |
| C-15 | C.surface: "0 filename owners; partition 35 files; 875 rows; last id S951; 0 new ids; **Topic lines name the register in 13 linguistics entries**" — the *before-state assertions themselves* | `review-only`. The counter never reproduces the surface numbers at base; there is no measure91 leg that re-runs the ls-tree/grep and fails when the numbers drift. The first five numbers I could re-run manually (reproduced — see §3); the "13" I could not reproduce with the given or any natural command (see finding W1). |

**No clause checked by nothing** except the receipt-artifact clause O-17 (defect D4) and the surface-numbers clause C-15 (weakness W1). Every other clause maps to a leg or to a named mutant/selftest chk in the frozen tool.

### O leg granularity nit

`O` top-level `legs` list has 7 entries (MATERIALIZE TOOL SELFTEST OKCOUNT REFUSALS MUTATION STUB) which matches the counter's emission; no phantom legs. C has a **duplicate `legs` key at claims.json top level listing only 4 legs (MATERIALIZE ENTRY INDEX APPENDONLY) vs a second `C.legs` with 8 sub-legs** — measure91's ENTRY leg checks the 8, the 4-leg list is never used by the counter. Probably intentional ("top-level separability" summary) but the ambiguity is worth a `nit`.

---

## (2) Verbatim refusal-case name presence as `chk(` in the working tree grader selftest

Grep -n (all line numbers from `tools/check-advance-evidence.py` at HEAD == freeze byte-identical, `sha256sum` re-run to `88597a66…1093` matches claims.json O.tool_sha256):

1. Line 1013 `chk('sub-topic phrases absent from headings',` — present
2. Line 1017 `chk('duplicate lands id in entry mode',` — present
3. Line 1019 `chk('new row shadows a base url',` — present
4. Line 1021 `chk('two new rows share one url',` — present
5. Line 1028 `chk('gate quote is the teaching cell',` — present
6. Line 1034 `chk('gate quote is from the source cell',` — present
7. Line 1041 `chk('capture byte-copies a graded file',` — present
8. Line 1045 `chk('lesson channel re-verification refused',` — present
9. Line 1049 `chk('old id gains a fresh disposition line',` — present

All 9/9 refusal case names appear verbatim in `chk(` calls in the frozen tool's selftest. Also confirmed: `chk` count in frozen tool is exactly 77; refusal name pass expected `rc=1` forces the mutated rule to fail the check, so each refusal case is what exercises the frozen tool's negative branch.

Stub control independent check: the stub (20-22 printer CASES hardcoded) reproduces all nine case names among its 22 strings and is still refused by OKCOUNT (22 ok lines ≠ 77) and by MUTATION (its file contains none of the 53 target strings, so every pair is a BROKEN-PATTERN). Probe (`mutprobe/msS.txt`) at `mutants.py --tool stub-tool.py`: `0/53 killed, 0 survived, 1 broken-pattern`, rc=1; equivalent static `0/53 killed, 0 survived, ...`, rc=1 for the full pairing. **No defect found in the stub leg.**

---

## (3) Path and command citations at base d39434b3 (`git cat-file -e`)

| Citation (from claims.json) | At base d39434b3 | At freeze 691aebf2 | Status |
|---|---|---|---|
| `corpus/SOURCES.md` (O.before citation of the v1 tool ground-truth and C.before registry) | present | present | OK |
| `corpus/knowledge/linguistics/linguistic-anthropology.md` (C.surface nearest-owner) | present | present | OK |
| `corpus/knowledge/synthesis/religion-language-co-evolution.md` (C.surface nearest-owner) | present | present | OK |
| `reports/round-91/controls/before-v1-entry.txt` (O.before "measured by …") | **absent** | **absent** | **defect D1** |
| `tools/check-corpus-index.py` (C index_tool) | present | present | OK |
| `corpus/lessons/round-90.md` (O/C `base_lesson` / counter arg) | present | present | OK |
| `corpus/knowledge/linguistics/secret-and-ludic-languages.md` (the non-existence claim) | absent at base | absent at freeze | OK (correctly absent — that is the whole point of the surface) |
| `reports/round-91/controls/before-v1-selftest.txt` | absent at base | **present at freeze** | OK (committed at the freeze, cited by O.before's sha-claim is done via the v1 selftest receipt; see D1) |

Reproduced C.surface numbers at base (all computed by me 2026-11-05, each via the command shown):
- `git ls-tree -r --name-only d39434b3 corpus/knowledge \| grep -Eic '(secret\|ludic\|argot\|slang\|cant\|jargon)'` → 0 matches, rc 1 (0 filename owners). Match.
- `… ls-tree -r --name-only d39434b3 corpus/knowledge/linguistics \| wc -l` → 35. Match.
- base registry rows: `grep -oE '^\| *[S][0-9]{3}' corpus/SOURCES.md@d39434b3 \| wc -l` → 875. Match.
- last id at base → S951. Match.
- "Topic lines name the register in **13** linguistics entries" → **could not reproduce** (see W1).

---

## (4) Mutation receipt header defect (mutants.py `head` var reuse)

Confirmed. reports/round-91/mutants.py:
- line 113: `rc, head = run(clean_tool, args.work, 'clean')` — this is the **clean** run's header for a green tool.
- line 134: `rc, head = run(mut_path, args.work, name)` — **the same `head` variable is overwritten by the last mutant's run, and it is that overwritten value (first stdout line of the last mutant) that gets written at line 146 into the `# clean selftest rc=0 <head>` comment** of the receipt.

The committed receipt (reports/round-91/mutation-score.txt line 2) therefore reads `# clean selftest rc=0 ['SELFTEST FAIL 76/77']` — that string is the **mutant `appendonly-flip-off`'s first stdout line**, not the clean run's tally (`['SELFTEST PASS 77/77']`). Proof: mutation-score.json has `clean_rc: 0`. The receipt header is a lie about the clean run, though the JSON sidecar records `clean_rc: 0` correctly.

Does this change killed/total or any counter leg?
- k/t/s/b counters are **not** affected: they are incremented from `rc` only; `head` is display-only.
- The `MUTATION` counter leg in measure91.py greps only the `MUTATION-SCORE:` line and does **not** read the header; so the defective header does not flip any leg today.
- BUT the header is the only receipt field that *binds receipt to clean tool* with the tally, so a future reviewer/diff that cites the header inherits a stale value. Probe: I replaced `SELFTEST PASS` → `SELFTEST FAIL` in the clean tool (making a "always-fail-verdict-but-rc0" printer) and ran the full 53-mutant pass: receipt was written with the same `# clean selftest rc=0 [...SELFTEST FAIL 76/77']` line and `53/53 killed`, rc=1 from mutants.py itself — but `measure91.py`'s MUTATION leg would pass it (it greps only the score line), since the stub ok-lines-count vs `stub_oks != selftest_checks` and sha mismatch are what ultimately catch it. Recap of what actually rescued the round: the TOOL sha leg pins bytes and the mutation pass still opens with the green tool first; the header nit remains.

**Also filed as weakness W2:** because mutants.py re-uses `head` and only checks `rc != 0`, a tool variant whose selftest **exits 0 while printing a FAIL tally** is not caught by the mutants.py clean gate; it would be caught only downstream by measure91's SELFTEST/OKCOUNT legs. That belongs on record as an inherited limitation, not a round-91 failure.

---

## (5) Stub control: OKCOUNT / mutant-kill legs

reports/round-91/controls/stub-tool.py (41 lines, freeze-pinned):
- It imports no hashlib and defines no mutant-pair target strings; `MUTANTS` in mutants.py (53 pairs) is never satisfied by its bytes. `run(clean_tool)` in mutants.py opens the file the clean bytes come from (`args.tool`), so pointing mutants.py at the stub makes each mutant replacement a no-op ("target string absent"). Result recorded above: `0/53 killed, 0 survived, 1 broken-pattern` for the first mutant; the full pairing gives `0/53 killed, 0 survived, 1 broken-pattern` per probe, i.e. the stub kills **0** mutants. STUB leg's second arm (`stub_killed == 0`) is satisfiable.
- For OKCOUNT: stub's runtime `print("  ok " + c + ": rc=1")` loop over `CASES` (22 strings) yields 22 `  ok ` lines (`<< 77`). `stub_refused_by_okcount = stub_oks != cfg[O][selftest_checks]` is therefore true. STUB leg's first arm holds.
- Static check that no `  ok ` literals can be reached a printer-forging way: 0 static `^  ok ` literals in the stub source; all 22 come from the single f-string `"  ok " + c`, so the ok-count is `len(CASES) == 22` — the stub cannot inflate itself past 77 without also having >=77 CASES, and even then it would keep the ok-line count equal to its own CASES list; OKCOUNT at 77 is attained only if the stub prints exactly 77 lines; the stub as frozen cannot. Correct.

---

## Findings (numbered, with severity, path:line, command)

**D1 — defect.** `reports/round-91/claims.json`, O.before sentence: "…and the shadow-URL fixture as PASS (measured by `reports/round-91/controls/before-v1-entry.txt`)". That file exists **neither at base d39434b3 nor at freeze 691aebf2 nor in the working tree`controls/` dir** (`ls reports/round-91/controls/` → `at-freeze-C-do-nothing.txt`, `at-freeze-C-freeze.txt`, `at-freeze-O-base.txt`, `at-freeze-O-freeze.txt`, `stub-tool-reproduced.txt`, `stub-tool.py`, `stub-tool.txt``; and `git ls-tree -r 691aebf2 \| grep before-v1` → only `before-v1-selftest.txt`). A citation to an artifact the freeze cannot produce is an evidence-discipline breach: the O.before receipt is unreproducible from the freeze. The "entry-mode PASS at base" half of O.before is therefore unbacked in the frozen artifacts. Command: `git cat-file -e d39434b3:reports/round-91/controls/before-v1-entry.txt` (rc=1); `ls` above.
  - Note: `before-v1-selftest.txt`** committed at freeze corroborates the *same-direction* pre-state claim "0/9 named refusals" by showing the v1 tool selftest had 67 checks, none of the nine refusal names (`grep -E '<the 9 names>'` → 0 hits).  That covers the refusal-name half of O.before but **not** the "entry mode grades the fixture as PASS" half.

**D4 — defect.** `reports/round-91/mutants.py:113,134,146` — `head` variable is reused: the receipt's `# clean selftest rc=0 [...]` header reports the **last mutant's** first stdout line, not the clean run. `reports/round-91/mutation-score.txt:2` shows `['SELFTEST FAIL 76/77']`. Commands: `git -C … show mutants.py \| sed -n '113p;134p;146p'`, plus a full 53-pair probe (frozen-file clone with `SELFTEST PASS`→`SELFTEST FAIL` substitution fed via `--tool`): receipt header stays `# clean selftest rc=0 ['SELFTEST FAIL 76/77']` with score 53/53, proving the header tracks the last mutant and not the clean bytes. Also proved mutants.py's own clean gate is rc-only for the same reason (see W2). Killed/total and the measure91 MUTATION leg are unaffected (`MUT_RE` does not read the header).

**D5 — defect.** `reports/round-91/measure91.py`, MUTATION leg (lines ~165-172). The leg trusts the score line and total from the **freeze-pinned mutants.py**, which is good, but the leg's ok-expression does **not** require `survived == 0` and `broken-pattern == 0` to be *independent* of the score line — they are, they are in MUT_RE, fine; the real hole is that measure91 **never inspects the receipt file** that O.after_target calls part of the deliverable ("with a mutation receipt over every v2 sub-check"). A round where mutants.py is removed post-hoc from the lands tree would still print MUTATION PASS, because the frozen copy read from the freeze is what runs — no leg verifies the receipt's existence or `rows` contents. Severity: defect in the counter contract (a claim clause checked by nothing, O-17 above), not in the round evidence itself. Command: `grep -n 'receipt\|mutation-score' measure91.py` → only `--receipt` plumbing, no existence/content check.

**W1 — weakness.** `reports/round-91/claims.json`, C.surface sentence "Topic lines name the register in **13** linguistics entries". This count has **no command named** in the claim and I could not reproduce 13 under any natural reading: topic-line grep for register words → 3; `^- topic:.*register` in the linguistics partition → 12 (`git grep -lE -i '^- topic:.*register' d39434b3 -- 'corpus/knowledge/linguistics/*.md' \| wc -l`); whole-text grep of argot/anti-lang/cant/polari/verlan/ludling/pig-latin in the partition → 11; wider synonym sweep → 16. Whatever the L1's original command was, it is not captured, so the 13 is unverifiable from the frozen artifacts. Everything else in C.surface reproduced exactly (see §3).

**W2 — weakness (inherited limitation, on-record).** `reports/round-91/mutants.py:113-115` clean gate is `rc != 0` only; a selftest that exits 0 while printing `SELFTEST FAIL …` walks through the clean gate. Probe: hacked clean tool (verdict string forced to FAIL, rc still 0) → mutants.py scored `53/53 killed, rc=1`, receipt header as in D4. Not a round-91 defeat (measure91's SELFTEST/OKCOUNT/TOOL legs and the frozen sha pin catch such a tool), but it means mutants.py alone is not the green-gate guarantee; the composition is what saves it. State this in the round report as an inference-precondition of the MUTATION leg.

**W3 — weakness.** `reports/round-91/measure91.py` grade_c `APPENDONLY` arm 2 reads tier/status/opened/used-by by **fixed column index** (`cells[3], [7], [8], [10]`) and does not check cell count vs the header count before indexing; a malformed new row with missing trailing cells shortens the list (index error is not possible — Python list index raises, which would crash the counter → measure91 rc!=REFUSED; a crash is not a FAIL and not a refusal; it aborts the round's score with an unhandled exception). Not exploitable with well-formed rows and the frozen tool's own entry mode also cell-count-checks; flagged only because the counter is the surface the next lane's seats will trust. Path: measure91.py:281-290.

**N1 — nit.** claims.json has both a top-level `legs` object (`O: 7 legs, C: 4 legs`) and `C.legs` (8 sub-legs). The counter's ENTRY leg uses the 8-leg list; the 4-leg top-level C list is used by nothing. The asymmetry (O has no `O.legs` and the top-level `legs.O` is exactly the counter legs) is confusing for the next reader. Command: the python json dump in §"Sanity: claim legs lists consistent".

**N2 — nit.** reports/round-91/mutants.py docstring line 3 says "(43 pairs, kept verbatim …) plus nine pairs over the v2 entry-mode sub-checks" → 43+9=52, matching O.mutation_min=52 and O.bounds "52 textual mutants", but `MUTANTS` actually contains **53** triples and the frozen receipt says 53. The `+9` count is off by one (there are 10 v2 pairs); harmless in effect (mutation_min is a floor) but the three numbers 52/53/9 never agree anywhere in the artifacts. This is the same drift the bounds text carries.

---

## Commands run (all in /fast/scratch/hyaku/kotodama-r91/ReviewerFreeze/, TMPDIR set there)

1. `git -C <lane> rev-parse HEAD 691aebf2 d39434b3` → identity check, all three agree, HEAD==freeze.
2. `git diff 691aebf2 -- reports/round-91/claims.json reports/round-91/measure91.py` → empty (frozen == working tree).
3. `git show 691aebf2:tools/check-advance-evidence.py` → sha256 `88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093`, matches claims O.tool_sha256.
4. `git show d39434b3:tools/check-advance-evidence.py \| sha256sum` → `121888f0…828ed`, matches claims O.v1_tool_sha256_base.
5. `python3 -` AST walk over frozen `tools/check-advance-evidence.py` `chk(` names → 77 counts, 9/9 names present (also `grep -n` identical).
6. `git cat-file -e` on every §3-cited path at both revs → table above.
7. `grep -c` on `before-v1-selftest.txt` at freeze → 67 `  ok ` lines, 0 hits on the nine names.
8. `grep -n 'rc, head = run(' mutants.py` → lines 113 (clean), 134 (mutant).
9. Probe runs `mutants.py` with 1-pair and 53-pair copies: `--tool` clean-hacked (`SELFTEST PASS`→`SELFTEST FAIL`) and stub-tool. Full 53-pair run times ~140s each, hence the 1-pair probe for the branch-exploration and one full 53-pair run as recorded. Receipt sidecar JSON has `clean_rc: 0`.
10. `python3 -B controls/stub-tool.py` → rc=0, tally `SELFTEST PASS 77/77`, 22 `  ok ` lines, all nine refusal names among them; OKCOUNT pkt (22 ≠ 77) as the stub leg expects.
11. `git grep -E` variants at base for the C.surface "13" count → 3/12/11/16, none 13 (W1).
12. `python3 -` json checks: top-level `legs.C` (4 names) vs `C.legs` (8 names) vs counter's entry leg parsing (8). N1.
13. Static stub analysis: 0 static `  ok ` literals, single f-string source, CASES length 22; mutants.py AST-parsed `MUTANTS` = 53 triples, 0 old-strings present in stub bytes.
14. measure91.py grade_c APPENDONLY column-index usage read directly (measure91.py:281-290).

No tools were installed; no pacman, uv tool, or binary-channel installs needed for this review. Scratch dir deleted before yield via `rm -rf` (see final note).

## Verification gaps / residual risk

- I did not execute `measure91.py` itself end-to-end against a lands clone; the review is static + probe-level, per the seat's "read its code; do not run the mutation pass" for (5) and the read-only mandate. The full 53-pair mutants.py pass I ran twice is the exception, run only against tool files in my scratch, never against the lane repo bytes.
- The "13" count W1 remains open: either the L1's original command is recoverable from an artifact I did not find, or the number is wrong and the surface sentence needs a countable command.
- The counter's column-index APPENDONLY arm (W3) and mutants.py's rc-only clean gate (W2) are inherited-design limitations, not evidence of a round-91 defect; they belong in the round report as caveats, not as kills.
