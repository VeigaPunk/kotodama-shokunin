# Round 54 pre-dispatch — criterion 11 controls replay (seat CriticControlsReplay)

Verdict: CONTROLS DEFECTIVE F1 (non-.md add passes), F2 (duplicate row passes), F3 (C-count has no red that falsifies it)

## Findings
F1 — fix before dispatch. The statement is wider than SET. claims.json:18 says "the one file added under corpus/knowledge is ...masks-masquerade.md".
  accept-c.py:56-57 counts only `*.md` files, and sweep.py:102 does the same. Mutants m1 and m1b (below) add `masks-masquerade.notes.txt` or
  `masks-glossary.MD` next to the entry: exit 0, all seven legs PASS, and the statement is false. This is the round-53 class again
  (lessons/round-53-verifier-spotcheck.md:67-90). Base has 0 non-.md files under corpus/knowledge (`git ls-tree -r 4b2299b`).
  Smallest correction: SET walks every regular file (drop the `.md` filter), so the base list stays exact. Add a RED with a second non-.md file.
F2 — fix before dispatch. Duplicate S-id rows are invisible. accept-c.py:75-78 builds `table` as a dict, so the last row with an id wins.
  check-source-access.py does not check for duplicates either. In mutant m2, S258 appears twice: first `queued` with used-by `—`, then
  `mined`. Result: exit 0, all PASS. "Every cited row is mined" and "names the entry in its used-by cell" are false for one S258 row.
  Smallest correction: RANGE marks any cited id with more than one `^| Sddd ` row as bad. Add a RED with a duplicate row.
F3 — fix before dispatch. C-count has no control that makes it false. claims.json:20 calls RED-SET "the nearest near-miss for the count and the set together".
  But RED-SET keeps the count at 230 (receipt:19, `count=230`), so in that copy "229 to 230" is true; RED-SET only falsifies C-one-new-file.
  An isolated red for the count does not exist: mutant m6 (count 231, README row, header, totals and footer all moved) fails SET and SWEEP,
  because SWEEP also pins 230 (accept-c.py:67). Criterion 11 (QUALITY.md:39) says "a clause with no control is unverified".
  Smallest correction: map C-count to legs SET+SWEEP in the clause list, and add RED-COUNT (m6) with exactly those two legs expected to fail.
  The control script's `failing == [expect_leg]` check (criterion11-controls.py:142) has to accept a declared list of legs. The judge must
  rule whether a two-leg red meets "every other leg as passing".
N1 — note. RED-RANGE passes the other legs by masking, and it changes two clauses at once. S238's used-by does not name the entry, yet
  USEDBY prints PASS: accept-c.py:86 drops range-bad ids before STATUS and USEDBY. A nearer near-miss is m5 (S238 cited and the entry
  appended to S238's used-by), which fails RANGE alone. RANGE's second half ("is a SOURCES.md row") has no control; m3 (S259, no row)
  shows it fails correctly.
N2 — note. RED-FLOOR drops a whole line. A nearer near-miss for "distinct" is m4 ((S258)→(S257): 20 tokens, 19 distinct); FLOOR fails alone.
N3 — note. RED-ACCESS uses the most literal marker, `headless` (check-source-access.py:33). Mutant m10 records an automation bypass in a
  paraphrase ("Cloudflare check cleared by an automated Chromium session"): ACCESS PASS. The clause says only "exits 0", so it stays true.
  The ordinary-means judgment is correctly review-only (claims.json:32), and the review seat must not lean on ACCESS for it.
N4 — note. Instruments are not pinned at acceptance time. Mutant m8 is RED-SET plus a one-line edit to base-knowledge-files.txt: exit 0.
  These files are outside the lands (claims.json:39-42,59), so the closure must diff reports/round-54/ and compare the receipt's sha256 lines.
N5 — note. Exit status: no pipe, `$(…)` or `|| true` exists. accept-c.py reads both sub-tool return codes directly (:66, :94), and the
  control script uses check=True for git and tar. One gap: an undecodable entry raises UnicodeDecodeError, which is not caught (:73-82).
  Result: a traceback and exit 1, not the documented exit 2 (m9). This is still non-zero, so nothing is hidden.
N6 — note. The controls run `sys.executable` (criterion11-controls.py:38), not the literal `python3`. On this host that is /usr/bin/python3,
  so the effect is the same, but it is not the declared argv verbatim. claims.json:44 "ACCESS PASS (exit 1)" reads as the ACCESS tool's exit;
  the dry run shows ACCESS exit=0 and accept-c exit 1 (declaration-dry-run.txt:9-10).

## Replay
Run from a scratch archive of 1ec84db: `python3 -B reports/round-54/criterion11-controls.py <lane> 1ec84db` → exit 0, `CONTROLS 8/8 as expected`.
Against the receipt it differs only in line 1 (`tree 1ec84db…` vs `tree 4b2299b…`); all five sha256 lines are identical. The run at 4b2299b is
byte-identical to the receipt (diff exit 0); 4b2299b..1ec84db touches no instrument. The base list equals the 229 .md paths at 4b2299b.

## Mutants (scratch /fast/scratch/hyaku/kotodama-r54/CriticControlsReplay/mutants.py: GREEN from the script's own green(), then the change; argv `python3 -B reports/round-54/accept-c.py`)
m1_non_md exit 0 | m1b_upper_md exit 0 | m2_dup_row exit 0 | m8_instrument_edit exit 0 | m10_access_phrasing exit 0 — each prints:
  SET PASS count=230 required=230 added=['corpus/knowledge/culture-material/masks-masquerade.md'] removed=[]
  SWEEP PASS exit=0 rows 230 files 230 missing_from_index 0 [] / FLOOR PASS cited=20 floor=20 / RANGE PASS bad=[] / STATUS PASS bad=[]
  USEDBY PASS bad=[] / ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
m3_unregistered exit 1: RANGE FAIL bad=['S259'], other six PASS.   m4_floor_distinct exit 1: FLOOR FAIL cited=19 floor=20, other six PASS.
m5_range_nearest exit 1: RANGE FAIL bad=['S238'], other six PASS.
m6_count_231 exit 1: SET FAIL count=231 required=230 added=[…-notes.md, …masks-masquerade.md] removed=[]; SWEEP FAIL exit=0 rows 231 files 231; other five PASS.
m9_bad_utf8 exit 1: no legs printed; stderr `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 835`.
Full output: /fast/scratch/hyaku/kotodama-r54/CriticControlsReplay/mutants-output.txt. No tools installed. The lane was not modified except for this file.
