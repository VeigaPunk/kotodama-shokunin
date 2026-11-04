# ReviewerCounter — round 89 w1: surgical review of the frozen instrument

Seat: ReviewerCounter (reviewer). Reviewed: `reports/round-89/{measure89.py, claims.json, controls89.py}` and the receipts `controls/controls.txt`, `counter-selftest.txt` (+`.json`), `selftest-redbefore.txt` and `quality-oneliners.txt`, all at freeze `1cbd0efc56edaa9394e3532fc5d8ef924f122f01` (base `42816d25…`). Every reproduction ran in a `git clone --shared` scratch at `/fast/scratch/hyaku/kotodama-r89/ReviewerCounter/lane` (toplevel asserted before each commit) and used the frozen counter bytes (self sha256 `6bc14bcd…cdf040`). Scratch has been removed. No lane file was edited. This is a recommendation, not an admission.

Receipts are in `.ufo/waves/round-89/w1/stage/ReviewerCounter/`:
- `probe89.py`, `probe89b.py`: the junk-landing and refusal drivers.
- `probe89-run.txt`, `probe89b-run.txt`, `probe89-results.json`: the console output, plus raw counter stdout/stderr/rc for every scenario.
- `unit-probes.txt`: helper-function probes.
- `selftest-rerun.txt(.json)` and `controls-rerun.txt`: my reproductions.
- `capture-sha256.txt`: the sha256 of each live capture I took at 2026-11-04T19:10:48-03:00. Every URL returned HTTP 200 with no challenge. I kept the hashes but not the bytes.

## Baseline reproduction (no defect)
- `python3 -B measure89.py --selftest --work st --receipt selftest-rerun.txt` returned rc=0 with `SELFTEST: PASS 21/21`. The result matches the committed receipt.
- `python3 -B controls89.py --lane lane --work ctl --out ctl-out` returned rc=0. Its 9 rows are identical to the committed `controls.txt`: same verdicts and same two known survivors.
- The sha256 values of claims.json, measure89.py and controls89.py at the freeze equal the values bound in `controls.txt`.

## Findings by severity

The counter in every row below is the frozen one: `measure89.py --root lane --freeze 1cbd0efc… --lands <probe> --claim F|C --work <scratch>`. Each landing sits on top of the freeze and is built by `probe89.py` / `probe89b.py`.

### HIGH

**H1. Shadow duplicate rows pass F, but the registry does not move.** Scenario `F-shadow-duplicate-rows-in-comment`: rc=0, `ACCEPT-F-89: PASS legs=5/5`.
- The landing leaves the 13 real population rows at `90d`. It appends bumped copies of those rows inside a `<!-- … ``` … ``` -->` block at the end of SOURCES.md.
- `rows()` keys rows by id and the last row wins, so ADVANCED, BACKED and OTHERCELLS all read the shadow copy.
- On the same lands the freeze-era auditor `tools/check-sources-recheck.py --as-of 2026-11-04 --window 90` returns rc=0 with `RECHECK-QUEUE: 0 due / 20 upcoming / 16 on-release / 872 rows`. The queue is unchanged and the first S009 row still reads `90d`.
- The counter gives a freshness PASS while the lane's own queue shows zero re-verification.
- Duplicate ids are not detected anywhere. Unit probe: `rows()` with a duplicate id → last wins (`z`).

**H2. Genuine captures with boilerplate quotes pass F: an undeclared survivor.** Scenario `F-boilerplate-quote-genuine-capture`: rc=0, PASS 5/5.
- The 13 population URLs were really fetched on 2026-11-04 (HTTP 200). Each quote is site chrome, not the row's teaching:
  - `Computer Science > Computation and Language` (arXiv)
  - `Best Practices in Research Reporting` (PLOS)
  - `International Day of the Intangible Cultural Heritage` (UNESCO)
  - the JSON key `child_language_count` for the glottolog `.json` rows: one token, 20 normalised chars, so `quote_ok` accepts it.
- `claims.json` F bounds say re-verification means "the row's teaching is still locatable". The only declared survivor is a forged capture, but nothing in the counter ties the quote to the row's `teaches` cell or to non-chrome text.
- This landing is honest about fetching and still passes without showing any teaching.

**H3. The Wayback suffix rule takes any timestamp and any wrapping host. F passes on a 1999 snapshot.**
- `url_ok` only checks `startswith('https://web.archive.org/web/') and endswith(row_url)`.
- Scenario `F-wayback-1999-timestamp` (manifest url `https://web.archive.org/web/19990101000000/<row url>`): rc=0, PASS 5/5.
- Scenario `F-wayback-suffix-foreign-host` (`https://web.archive.org/web/2026/https://evil.invalid/?u=<row url>`): rc=0, PASS 5/5.
- Unit probe: `url_ok('https://web.archive.org/web/https://example.org/a', …)` → True, so no timestamp segment is required at all.
- For a freshness claim, an archive snapshot from any year is not a 2026-11-04 surface. The predicate wording "a web.archive.org capture of one" is looser than the claim's meaning, and the code is looser still: the foreign-host form is not "a capture of" the row URL.

**H4. An off-topic filler entry with genuine captures passes C 8/8.** Scenario `C-offtopic-filler-genuine-captures`: rc=0, `ACCEPT-C-89: PASS legs=8/8`.
- The entry is titled "Sourdough starter care". Six sections repeat one sentence 25×.
- Its table is `| a | b | c |` / `|---|` / `|0|`…`|4|`.
- It has three new rows (S936–S938, self-declared tier A) pointing at example.com, example.net and example.org. They are backed by real fetched captures and the real quote "This domain is for use in documentation examples without needing permission."
- Nothing checks that the entry is about evidentiality. Nothing checks that its text is non-repetitive, or that the self-asserted tier is plausible.
- The declared C survivor is only "forged capture". This one uses no forgery.

### MEDIUM

**M1. The capture path is unconstrained, so a capture can be the graded file that contains the quote.**
- `capture_check` accepts any committed path at lands.
- Scenario `F-capture-is-SOURCES.md`: the capture is `corpus/SOURCES.md` and each quote is the first 12 words of the row's teaches cell. Result: rc=0, PASS 5/5, with no file under `reports/round-89/rechecks/` except the manifest.
- Scenario `C-capture-is-lesson-file`: the capture is `corpus/lessons/round-89.md`, which holds the quote by construction. Result: rc=0, PASS 8/8.
- This is the forged-capture class taken to zero effort. A re-fetch reviewer who scans `rechecks/` or `evidence/` sees no capture files to re-open.
- It also makes the `separability` text false. That text says F reads only `reports/round-89/rechecks/` and C reads `reports/round-89/evidence/`. In this landing, F's authority is SOURCES.md itself (a QUALITY-28-style self-judging read).

**M2. The kill rule "a NOT-LOCATED row is never advanced" is stated but not coded (QUALITY 26, one text).**
- Scenario `F-located-and-not-located-same-id`: every advanced id also has a `- Sxxx NOT-LOCATED: page gone` line. Result: rc=0, PASS 5/5.
- Scenario `F-NOT_LOCATED-underscore-and-NOT-LOCATED-space`: lines written `NOT LOCATED` or `NOT_LOCATED` count as LOCATED. Result: rc=0, PASS 5/5.
- Unit probes:
  - `LOCATED_RE` matches `S009 NOT LOCATED` and `S009 NOT_LOCATED`, and `NOTLOC_RE` matches neither.
  - Lowercase `not-located` is not a disposition at all.

**M3. Graded-tree `.gitattributes` steers what the freeze-pinned index tool sees (QUALITY 28 adjacent).**
- `git archive <lands> corpus` honours `export-ignore` from the lands tree.
- Scenario `C-export-ignore-hides-unindexed-file`: the H4 landing plus an unindexed `corpus/knowledge/linguistics/hidden-unindexed.md` and `corpus/.gitattributes` marking that file `export-ignore`. Result: INDEX passes, rc=0, PASS 8/8.
- The same frozen tool over the real checkout returns rc=1 with `CORPUS-INDEX: FINDINGS files=262 rows=261 findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT`.
- The tool bytes are pinned, but its input view is chosen by the graded tree.

**M4. The `fetched_at` check is only a prefix match.**
- `str(fetched_at).startswith('2026-11-04')`. Scenario `F-fetched_at-prefix-junk` with `"2026-11-04 (not actually fetched)"`: rc=0, PASS 5/5.
- The contract's local-ISO-with-offset form is not enforced.
- An honest fetch recorded in UTC after 21:00 -03:00 (`2026-11-05T01:00:00Z`) is rejected (unit probe: False).

### LOW

**L1. Predicate vs code drift beyond M2 (QUALITY 26).** Each item below is coded but not stated, or stated more strictly than coded:
- The C quote must be double-quoted and ≥20 normalised chars. The C predicate says only "<=25-word quote".
- ENTRY header keys must appear as `- key` bullets in the first 80 lines. This is not stated.
- TABLE accepts data rows with 1 cell and ignores code fences. Scenario `C-headings-table-inside-code-fence-1cell-rows`: all `## ` headings and the table sit inside a ``` fence. Result: rc=0, PASS 8/8. Unit probe: `tables()` returns `[(3, 5)]` for 1-cell rows.
- "ISO date" accepts ISO basic and week forms: `fromisoformat('20270503')` and `('2027-W18-1')` both return 2027-05-03 on Python 3.14.8.
- A CJK quote is one whitespace "word", so a 300-char quote passes the ≤25-word cap (unit probe: True).

**L2. False negatives that could reject honest work.**
- **Arrow spacing:** `recheck 90d → 2027-05-03` (spaced), `recheck: 90d→…`, `=>` and `—>` all fail BACKED.
- **CJK quotes:** normalisation makes a CJK run one token, so a CJK quote matches only when it spans a whole punctuation-delimited run. A sub-clause of a Japanese sentence returns False. This is relevant to S875 (bunka.go.jp).
- **URL variants:** `urls()` strips a trailing `)` (`…/Foo_(bar)` becomes `…/Foo_(bar`). `url_ok` rejects a Wayback capture of the `http://` form and the live URL with a trailing slash.
- **S142:** the row URL is itself a 2025 Wayback snapshot, so only that exact URL matches. A fresh 2026 Wayback capture or the live historicbrass.org URL cannot back S142.

**L3. A malformed frozen claims.json is an rc=1 "error", not an rc=2 refusal.**
- Probe `malformed claims.json at freeze` → rc=1 `FAIL legs=0/5 (error: JSONDecodeError …)`.
- The docstring promises a refusal for an "unreadable frozen claims.json". The absent case is refused correctly (rc=2).
- It is never a PASS, so this is low.

**L4. The executing counter file is not bound.**
- FROZENCFG compares the lands blob with the freeze blob, not the running `__file__`.
- An edited copy run against the do-nothing lands (`--lands` = freeze) returned rc=0, `ACCEPT-F-89: PASS legs=5/5`. Only the header `counter sha256 (self): 66db38c9…` differs from `6bc14bcd…`.
- Readers must compare that header sha; the counter never asserts it.

**L5. Selftest coverage gaps.**
- QUALITY 35 is met in form. The selftest:
  - retains raw stdout, stderr and rc in `counter-selftest.txt.json` (21 records, all with stdout);
  - asserts the clean positives (rc 0, `PASS legs=n/n`, empty stderr);
  - asserts each negative's observed `LEG FAIL <NAME>`;
  - is shown red-before by `selftest-redbefore.txt` (BACKED forced → 18/21, exit 1).
- It has no case for:
  - non-2xx `http_status`, sha256 mismatch, a bad `fetched_at`, or the Wayback/foreign-host URL;
  - the ADVANCED window bounds (d = as_of+90, d > as_of+366);
  - a LOCATED+NOT-LOCATED conflict or duplicate rows;
  - a recheck change on a non-population row;
  - the off-chain-freeze and unreadable-claims refusals.
- It keeps `expect_leg` but not the parsed fail-leg list.

## Refusals: checked, no defect except L3
Each was run with the frozen counter:

| Probe | rc | Result |
|---|---|---|
| Uppercase 40-hex freeze | 2 | `not a 40-hex revision` |
| 12-char lands | 2 | `not a 40-hex revision` |
| Annotated tag object as freeze | 2 | `not a commit` |
| lands == base | 2 | `lands equals frozen base` |
| Freeze off first-parent (lands built from base) | 2 | refused |
| Freeze reachable only via a merge's second parent | 2 | refused |
| freeze = base (claims.json absent) | 2 | `frozen claims.json unreadable` |
| lands == freeze | 1 | `legs=2/8`, graded as the do-nothing control, as documented |

LEGCOUNT is covered by selftest `refuse-legcount` (rc=2).

## QUALITY 28 (graded-tree authority)
- The index tool is read with `git show <freeze>:tools/check-corpus-index.py` into `--work` and run over a `git archive` of lands, so the tool bytes are pinned.
- `quality-oneliners.txt` QUALITY28 prints nothing, exit 0.
- The residual graded-tree authority comes from three places:
  - the manifest's self-asserted `http_status`, `fetched_at`, `url` and `capture` path (M1, M4);
  - `export-ignore` (M3);
  - the self-asserted tier and status of new rows (H4).

## Residual risk and verification gaps
- H1–H4, M1 and M2 are survivors besides the two declared forged-capture controls. Per the contract the frozen instrument stays unamended, so these must be disclosed in the round's lesson and SCORECARD notes.
- Of these, the non-author re-fetch seat can catch H2, H3 and M1 only if it checks:
  - the quote against the row's `teaches` cell;
  - the Wayback timestamp;
  - that capture paths lie under `rechecks/` or `evidence/`.
- H1 is caught by running `check-sources-recheck.py` at lands, or by a duplicate-id census, next to the counter.
- I did not grade the actual round-89 landing; none existed when I reviewed.
- I did not run `separability89.py` because it is not in the freeze commit. The `separability` field names it as `reports/round-89/separability89.py`, but `git show --stat 1cbd0efc` lists no such file.
- Live captures cover 13 of 16 population URLs. I did not fetch S032 (doi.org), S142 (Wayback) or S875 (bunka.go.jp), because 13 were enough for ADVANCED ≥ 10.

## Commands observed (rc)
- `git clone -q --shared --no-checkout <lane> lane && git -C lane checkout -q --detach 1cbd0efc…` → 0. Toplevel = scratch/lane.
- `curl -sL -m 30 …` × 16 → all HTTP 200.
- `python3 -B probe89.py <scratch>` → 0. The first run's C rows failed INDEX on TOPIC_MISMATCH because of my entry topic. I fixed the probe, deleted the scratch-only branch `probe-side` and tag `probe-t` (toplevel asserted), and reran; the rerun results are recorded above.
- `python3 -B probe89b.py <scratch>` → 0.
- `python3 -B measure89.py --selftest …` → 0.
- `python3 -B controls89.py …` → 0.
- `rm -rf /fast/scratch/hyaku/kotodama-r89/ReviewerCounter` → done before yield.

Tools installed or updated: none.
