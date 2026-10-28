# RevCaRows — W2 falsification, round 76 kotodama (seat report)

Scope: the 19 `SCORECARD.md` `## Corrections — round 76` rows and the `SKILL.md` repair, checked
against the frozen `reports/round-76/ledger.json`, the exact `stated_at` lines at the base blob,
and `reports/round-76/telemetry/measures-ca.txt`. No edits; no builds/tests/linters; the counter
was NOT executed — every leg verdict below is reconciled from the committed receipt, the counter
source, and independent byte checks.

Revisions used (all read via `git show <rev>:<path>`, never the worktree):
base `98c486bdb4650ba5b8e651d332910e8ee60ad121`; freeze/config `df0f0309d61e5485bb17035d3f8791b1e6a11d40`;
Ca landing `a43ed807ea38b5fc5a7875a839d576cea73aba7c` (SCORECARD.md +28, SKILL.md 1 line);
C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a`; measured-outcome commit `af67443` ("record
measured claim outcomes") is the only committed home of `measures-ca.txt` and carries both landings
(`git merge-base --is-ancestor` checked for both).

## Independent re-verification performed

1. **All 20 ledger pairs are red at base and truthfully observed.** For every pair I took the
   `stated_at` blob line at base, captured the stated token with the pair's own `stated_parse`,
   ran the pair's `observe_cmd` argv (read-only git, cwd = lane) at base, parsed with the pair's
   `parse`, and compared: stated token present at the stated line for 20/20 pairs (exception:
   L76-19, see F2); observed == `expected_after` == `observed_at_base` for 20/20; stated ≠ observed
   (red) for 20/20. This confirms LEG PASS BASEMISMATCH ("red=20, min=10") is honest.
2. **stated_at lines verified byte-wise** (`git show 98c486b:<path>` line N). 19/20 exact; L76-19's
   `stated_text` spans a wrap (F2). L76-13's text IS on its line 8 — its defect is the surface class (F1).
3. **SCORECARD table vs ledger**: 19 table rows at `a43ed807:SCORECARD.md:1514-1532`; id set ==
   the 19 ledger ANNOTATE ids exactly (no L76-09 — documented dedup, `df0f0309:reports/round-76/claims.json`
   `pre_data_corrections[Ca-P1]`; no L76-16 — correctly excluded as REPAIR). Every old/new token cell
   matches the base stated token / `expected_after`. Exactly 3 command cells differ from the frozen
   ledger `rederive` strings: L76-19, L76-20, L76-21 (F3/F4).
4. **SKILL.md:707 (L76-16)**: base line carries `Measured 2026-10-27 at counter sha256 `fa5060b91bdb…``;
   the landed line carries `committed counter `reports/round-75/accept-c.py` sha256 `315c5f3f27fd…`;
   the receipt header's `fa5060b91bdb…` is the pre-freeze byte hash`. `fa5060b91bdb` no longer
   mis-attributes the selftest; base `stated_text` absent from the landed file. F5 for the grammar mismatch.
5. **STAMP honesty**: `measures-ca.txt` header pins counter sha256 `c1fc755e926f8d25e622469ec018bc9ad6c22b2f99ba83447fa95baab4a9695b`;
   recomputed `git show df0f0309:reports/round-76/accept-ca.py | sha256sum` → identical.
6. **COMBINED's cited line**: base `corpus/README.md:410` = `## culture-material/ (40)`;
   at C-lands = `## culture-material/ (41)`. Verified in both trees.
7. **R1EXEMPT inventory**: fixtures `r1exempt-green.json` / `r1exempt-red.json` / `r1exempt-mixed.json`
   ARE committed at the freeze under `reports/round-76/fixtures/`; the receipts
   `r1exempt-green.txt` / `r1exempt-red.txt` exist at NO revision (`git log --all -- <paths>` empty)
   and are absent from telemetry at both the freeze and Ca-lands.

## Findings (by severity)

### F1 — frozen-invalid pair: L76-13 filed on a forbidden surface (LEDGER + SEPARABLE red)
`df0f0309:reports/round-76/ledger.json` L76-13 `stated_at` =
`corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:8`. The frozen ANNOTATE leg allows
only {LOG.md, SCORECARD.md, corpus/lessons/round-75.md, corpus/QUALITY.md}; the frozen SEPARABLE leg
forbids `corpus/knowledge/**` outright. Counter check: `accept-ca.py:1499-1504` (inside `leg_ledger`).
The pair's facts are true (stated 111487 B vs evidence `bytes: 109588`, re-verified), but the knowledge
file is neither append-only nor a frozen mutable repair surface ({SHONEN.md, SKILL.md, corpus/README.md}),
so no disposition could ever close it. Frozen before data → fails as declared. measures-ca.txt:4,11 say
exactly this. Valid annotation? **No — frozen invalid (uncorrectable surface), factually true.**

### F2 — frozen-invalid pair: L76-19 stated_text wraps the stated line (LEDGER red)
Base `corpus/lessons/round-75.md`: line 47 ends `...S888's window (`chars=4097 before=10`) and S892's`;
line 48 is `   (`chars=4097 before=284`) both start at the document head...`. The ledger's
`stated_text` = "S892's window (`chars=4097 before=284`)" is not contained in line 48 (or any single
line, ±2 checked), while the token `284` IS anchored there and the observation (`before=2020` in
`reports/round-75/evidence/S892.txt`) is true. Counter requires `stated_text` inside the single
`stated_at` line (`leg_ledger`, accept-ca.py:1550-1560 branch). measures-ca.txt:4 clause 2 is accurate.
Valid annotation? **No — frozen invalid (line-pointing), underlying defect real.**

### F3 — frozen-corrupt rederive strings for L76-19/20/21 (ANNOTATE + NOSTUB red; root cause)
The ledger's own `rederive` fields for these three ids lost their shell quoting:
`git grep -h -E ^window: chars= <base> -- reports/round-75/evidence/S892.txt` (L76-19),
`git grep -h -o -E ^sha256: [0-9a-f]{8} <base> -- .../S885.txt` (L76-20), `.../S887.txt` (L76-21) —
compare L76-08's correctly quoted `'^window: chars=[0-9]+ ...'` in the same file. `rederive_argv`
shlex-splits the raw string (accept-ca.py:1377-1382), so `chars=` / the base revision land in the
pathspec role of `_git_grep_problem` (accept-ca.py:1039-1089) → "path operand ... does not exist in
the clone" → rederive not executable → three rows machine-unannotated (`leg_annotate`,
accept-ca.py:1786-1877) and three `rederive-cmd` stubs (`leg_nostub` requires the row to CONTAIN the
ledger's raw `cmd`; accept-ca.py:2074-2135). measures-ca.txt:7-8 match. **Frozen invalid (all three);
their observe_cmd argv arrays are fine, so the pairs are observable — only the machine-replayed
command field is corrupt.**

### F4 — SCORECARD wording defect: "verbatim projection" is false for 3/19 rows and the disclosure under-reports
`a43ed807:SCORECARD.md:1535` claims the table is "a verbatim projection of the 19 ANNOTATE pairs" and
names only L76-13 and L76-19 as defective. Byte comparison shows the command cells for L76-19/20/21
(`:1531-1532` and L76-20's row) carry the quoted, executable forms — NOT the frozen ledger bytes —
and the receipt shows five rows touched by failures (13, 16, 19, 20, 21), not two. The disclaimer
("not an assertion that the frozen Ca counter accepts them") prevents dishonesty and every token cell
is correct, but "verbatim" is factually wrong and the two-defect naming invites the reading that the
other 17 rows are machine-clean when three more are not. **Wording/citation weakness only; no data error.**

### F5 — L76-16 REPAIR red by frozen grammar, substantively correct
Frozen `statement_after.parse` = `^\| accept-c-75 \|.*?committed counter sha256 `([0-9a-f]{12})``
(`statement_after()`, accept-ca.py:1390-1421, "no-match" message at :1413). The landed SKILL.md:707
inserts the path between the required trigram words: "committed counter **`reports/round-75/accept-c.py`**
sha256 `315c5f3f27fd…`" — the literal `committed counter sha256` occurs 0 times in the landed file,
so REPAIR fails as declared (measures-ca.txt:6). The repair itself is complete and honest: new digest
present, pre-freeze digest explicitly re-attributed to the receipt, base stated_text gone, target file
is in the frozen mutable set {SHONEN.md, SKILL.md, corpus/README.md}. **Frozen invalid mechanically;
substantively valid repair.**

### F6 — R1EXEMPT red: fixtures committed, run receipts never committed
Leg text (claims.json, Ca `R1EXEMPT`) and code (accept-ca.py:2507-2521) require
`reports/round-76/telemetry/r1exempt-green.txt` and `r1exempt-red.txt` committed at Ca-lands carrying
`LEG PASS/FAIL APPENDONLY` + exit codes. The three fixture JSONs are committed at the freeze
(`df0f0309:reports/round-76/fixtures/`), but neither receipt exists at `a43ed807` — nor at any commit
in the lane. The exemption logic itself ran green inside the counter (fixtures built and graded);
the failure is the missing committed evidence. measures-ca.txt:10 accurate. **Execution gap, honestly measured.**

### F7 — COMBINED red: C and Ca frozen with incompatible exemption grammars
`leg_combined` re-runs APPENDONLY at the `--combined` tree with `combined_exemptions=True`
(accept-ca.py:2568-2575), which reads claim C's `owned_inplace` expecting an integer `base_line` and
verifies `base_lines[n-1] == base_text` / `lands_lines[n-1] == after_text` (accept-ca.py:1913-1930).
C's frozen `owned_inplace` (claims.json, claim C) carries only {path: corpus/README.md, base_text:
"## culture-material/ (40)", after_text: "## culture-material/ (41)"} — **no `base_line`** →
"claim-C owned-inplace line has invalid line number" → the C-owned README heading edit at base line
410 (verified in both trees) is a changed line outside every allowed set → combined APPENDONLY red →
COMBINED red. Both claims were frozen in the same commit with one side's exemption format unreadable
by the other's counter; neither bytes can change. measures-ca.txt:13's "no valid line number" matches
the code path exactly. **Genuine cross-claim freeze defect, honestly measured.**

### Passing legs independently supported
- BASEMISMATCH (red=20): re-verified pair by pair (see item 1).
- APPENDONLY at Ca-lands: the landing's full diff is SCORECARD.md (+28 appended) and SKILL.md (1 line
  replaced at the L76-16 `stated_at` line) — exactly inside the frozen exemption sets; green is honest.
- RECEIPTS / STAMP / FROZENCFG: `accept-ca-75-at-lands.txt` present at the freeze; the measures header's
  counter sha256 equals the frozen `accept-ca.py` blob (recomputed); freeze is on the lands' first-parent
  chain; ledger/claims at lands are untouched by the 2-file landing.
- Leg arithmetic: 12 legs, 7 red (LEDGER, REPAIR, ANNOTATE, NOSTUB, R1EXEMPT, SEPARABLE, COMBINED) /
  5 green → `ACCEPT-CA-76: FAIL legs=5/12`, exit 1 (measures-ca.txt:16-17). Consistent.

## Per-row verdict (19 ANNOTATE rows + 1 REPAIR)

| id | row verdict | basis |
|---|---|---|
| L76-01…L76-08, L76-10, L76-11, L76-12, L76-14, L76-15, L76-17, L76-18 (16 rows) | **valid annotations** | append-only surface; stated_text on the stated line; old/new tokens byte-verified; command cell identical to the frozen ledger `rederive`; executable under the argv grammar |
| L76-13 | frozen-invalid (surface) | F1; facts true, file uncorrectable |
| L76-19 | frozen-invalid (line-point + corrupt rederive) | F2+F3; token and observation true |
| L76-20, L76-21 | frozen-invalid (corrupt rederive) | F3; tokens and observations true |
| L76-16 (REPAIR, SKILL.md:707) | mechanically frozen-invalid; substantively correct | F5 |

## Verdict

No false green and no fabricated measurement found: every red leg in `measures-ca.txt` traces to real
frozen bytes, and every green leg survived independent re-derivation. The frozen Ca configuration
carries four uncorrectable defect classes — L76-13's forbidden surface (F1), L76-19's wrapped
stated_text (F2), the quote-stripped rederive strings of L76-19/20/21 (F3), and the L76-16
statement_after trigram that the landing's (correct) wording does not satisfy (F5) — plus the missing
R1EXEMPT receipts (F6) and the C↔Ca owned_inplace grammar mismatch that makes COMBINED unreachable
(F7). `ACCEPT-CA-76: FAIL legs=5/12` is the correct, honest outcome and claim Ca fails as declared
per its kill rule ("any leg false at <Ca-lands> → fails as declared"); nothing here authorizes touching
frozen bytes. New wording defect to carry forward: SCORECARD.md:1535's "verbatim projection" claim and
two-defect disclosure (F4) under-report the machine-visible defect set.

## Residual risk and verification gaps

- The counter was not executed (prohibited): leg outputs are reconciled from the committed receipt,
  counter source, and my own byte/argv checks. The exact rejection strings for L76-20/21 ("base
  revision as a path operand") are code-derived (accept-ca.py:1039-1089), not captured from a live run.
- RECEIPTS/STAMP runtime behavior is taken from committed receipt headers + code reading; I did not
  re-run the round-75 counter inside a clone.
- SEPARABLE's "no byte names C's terms" scan over the full read set was spot-checked on ledger.json
  (zero hits for calendar-festival*/era-periodization*/S894-S898), not on every named telemetry receipt.

No tool installs or upgrades were made (none needed); pacman untouched. Scratch
`/fast/scratch/hyaku/kotodama-r76/RevCaRows` removed before yielding. No files outside the seat report
were created or modified.
