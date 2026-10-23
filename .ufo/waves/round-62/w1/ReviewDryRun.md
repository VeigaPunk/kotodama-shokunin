# ReviewDryRun — declaration review, QUALITY criteria 9 + 11 (round 62, wave 1)

Seat: KotodamaR62.ReviewDryRun (reviewer, leaf, no dispatch). Date: 2026-10-23.
Objects: `reports/round-62/telemetry/declaration-dry-run.txt` (33 lines) vs `reports/round-62/claims.json` (111 lines), `reports/round-62/separability-manifest.json`, counters `reports/round-62/accept-d.py` / `accept-o.py`. Criteria text: `corpus/QUALITY.md:35` (criterion 9), `:39` (criterion 11). No tool installed; nothing written outside this report. Findings are recommendations, not admissions.

## Verdict summary

- Criterion 9 two-way **command coverage: MET**, verified mechanically, not by eye: `missing_from_receipt=[]`, `undeclared_in_receipt=[]`. All three declared commands appear verbatim, each exactly once (receipt lines 2, 19, 31); the manifest's two acceptance argvs equal the counting commands.
- Criterion 9 **expected-result naming: NOT MET** (F1) — the receipt names no expectation anywhere (its only `#` line is the header, line 1).
- Criterion 11 **clause→leg mapping: complete at the legs** (no clause of either statement is unchecked; maps below), but the declaration itself carries no clause list (F2), and three D clauses + one O clause have no red control named (F3). One leg checks less than its clause says (F4).

## Criterion 9 — receipt ↔ declaration, both ways

Mechanical check run this session (python over the two files):

- Declared: `claims.json:18` `python3 -B reports/round-62/accept-d.py`; `:56` `python3 -B reports/round-62/accept-o.py`; `:9` `python3 -B tools/check-claim-separability.py reports/round-62/separability-manifest.json`. Manifest acceptance argvs (`separability-manifest.json`, D and O units) are the same two argvs; the REC record unit carries none (correctly out of scope).
- Receipt `$ ` commands: lines 2, 19, 31 — exact string match to the three declarations; no fourth command.
- Instrument identity: sha256 of the on-disk counters equals the assignment's frozen values — accept-d `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`, accept-o `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`. Receipt header (line 1) "revision 0 (uncommitted at run time; lane main d42ffb89)" matches `claims.json:6` round_base and manifest `base` (all `d42ffb89…`).
- Receipt is internally consistent with a pre-landing tree: accept-d shows the unchanged base (`:3` `differ=[]`, `:10` `cited=[] registry=[]`, `:11` `inserted_rows=[]`, `:14` `located=0 cited=0`), accept-o shows the absent-tool path its code takes (`:20` `TOOL FAIL … exists=False`, `:21-28` every later leg `no tool`, `:30` exit=1 — matches `accept-o.py:227-235`), and separability stops at the absent land `tools/reopen-row.py` with exit=2 (`:31-33`) — the criterion's named absent-land form. Last-line/exit agreement holds everywhere (`:17-18`, `:29-30`, `:32-33`), and the printed labels match the declared predicates (`claims.json:19`, `:57`).
- Manifest ↔ claims agreement: lands, exports (`\bS69[3-9]\b` / none) and acceptance match `claims.json:43-47`, `:74-78`; `needs_git: true` on D is honest (SET/APPEND read BASE via `git show`, `accept-d.py:146-151`).

### F1 — Major (criterion 9): expected pre-landing results are not named in the receipt

`QUALITY.md:35`: "Expected pre-landing results are named in the receipt: an absent land (exit 2, the land named), or an after-value comparison failing with the before value printed. A checker that stops at its first absent land leaves its later legs unevaluated, and the receipt says so." The round-62 receipt contains **zero annotation lines** (only line 1 starts with `#`): no expected-result naming for any of the three commands, and no disclosure that the separability checker stopped at its first absent land leaving later units/legs unevaluated. The immediate predecessor shows the required shape: `reports/round-61/telemetry/declaration-dry-run.txt` line 2 (`# expected pre-landing: C FAIL (…); O FAIL (tool absent: …); separability: …`) and its final `# note:` line disclosing the first-absent-land stop. Charitable reading: the separability command's own output is in the named form (land named, exit 2, `:32-33`), and the counter outputs print before-values (`:3` `differ=[]`, `:14` `located=0 cited=0`); but nothing distinguishes "expected" from "observed", and O's absent land is reported at exit 1, not the named exit 2. Smallest fix: re-issue the receipt with one `# expected pre-landing:` line (round-61 shape) and the separability stop note. No counter change is needed, so the frozen-predicate rule is not touched.

### F6 — Low: no mechanical two-way checker for this round's receipt

Rounds 52-53 committed `reports/round-N/dry-run.py check`; rounds 59-61 and 62 declare none, so the both-ways property rests on manual/closure review (this report performed it). Convention-consistent, but the round-62 receipt currently has no committed instrument that would catch a future omission (the exact R51-M5 class). Informational.

## Criterion 11 — every claim clause mapped

### Claim D (`claims.json:16`) → legs (`accept-d.py:3-50` docstring; implementations `:152-287`)

| # | Clause (statement words) | Leg | Leg vs clause |
|---|---|---|---|
| 1 | differs from d42ffb89 in exactly lines 63, 74, 75, 93 | SET (`:157-160`) | exact: equal line count + differ == [63,74,75,93] (all other lines byte-identical) |
| 2 | each is a bullet with one S-id | ONEID (`:162-164`) | exact (`^\s*- ` + exactly one distinct id) — **no red control** (F3) |
| 3 | and no defect mark | NOMARK (`:166-167`) | exact (7 mark tokens, casefolded) |
| 4 | line 63 (S692) keeps the open country list | OPEN (`:169-172`) | operationalized as `belgium,?\s+(etc\|and elsewhere\|and other\|among other)` and bans `france, and belgium` — **stricter** than the clause (F5) |
| 5 | line 75 (S666) keeps the source's hedge or attribution | HEDGE (`:173-176`) | operationalized as `we have\|bbc\|the article/programme names/cites/gives/reports`; "or attribution" covered only by the BBC/programme patterns (F5) |
| 6 | line 74 cites S665 and names the caption, or cites a new row | CAPTION (`:177-180`) | exact: (`{S665}` + `\bcaption\b`) or single new-block id |
| 7 | line 93 cites one new tier A/B row S693-S699 whose quote names talaria or Hermes | SOLE (`:184-194`) | exact: single new id, 13 cells, tier cell in {A,B}, normalised quote matches `\b(talaria\|hermes)\b` |
| 8 | new rows are exactly the ids the entry cites from that block | ROWS (`:196-229`) | exact: cited_new == reg_new, non-empty, whole entry scanned |
| 9 | mined, opened 2026-10-23, used-by the entry | ROWS (`:218-224`) | exact (status cell, opened cell, ENTRY in used-by split) |
| 10 | each listing a live URL and a Wayback capture | ROWS (`:211-217,225-226`) | **"live" checked as shape only** — an http(s) non-Wayback URL listed before the first `web.archive.org/web/` URL; liveness is not proven (LOCATE can pass via the capture with a dead live URL) (F4) |
| 11 | each located by the base locator within three passes | LOCATE (`:264-277`) | exact: PASSES=3, GAP=60, locator unchanged |
| 12 | corpus/SOURCES.md keeps every base line (S687 only its used-by cell) | APPEND (`:231-243`) | exact: greedy in-order subsequence over **all** base lines (row and non-row — a deleted/edited header stalls the cursor and fails); S687 exempted in the used-by cell only; every inserted row a new-block row |
| 13 | the four lines restate their quotes (LINK) | LINK (`:245-261`) | exact: ≥5 content words, ≥3 shared, LCS ≥ max(4, ceil(0.4·content)) — matches the round's entry rules |
| 14 | without copying more than 12 consecutive words (COPY) | COPY (`:262-263`) | exact: longest run ≤ 12, S-id masked before the run count |
| 15 | check-source-access and check-cited-lines exit 0 | ACCESS (`:278-279`), LINT (`:280-283`) | both read `returncode` directly, no pipes — **no red control for either** (F3) |

`review_only` (`claims.json:38-42`) names three items and matches the counter's review-only paragraph (`accept-d.py:46-49`) plus the lore handoff; nothing from the statement hides there unlisted. Every D clause lands on a leg; every leg maps to ≥1 clause.

### Claim O (`claims.json:54`) → legs (`accept-o.py:2-67` docstring; implementations `:227-330`)

| # | Clause (statement words) | Leg | Leg vs clause |
|---|---|---|---|
| 1 | tools/reopen-row.py exists | TOOL (`:227-230`) | exact |
| 2 | names none of reports/, accept-o, round-62 | INDEP (`:236-239`) | exact substring check |
| 3 | run as a copy outside the lane | INDEP (`:241-243`) | exact: all runs use a tempdir copy, cwd there |
| 4 | against a run-time random local fixture | GEN (`:245-273`) | exact: `random.SystemRandom`, random ids/paths/vocab/quotes, 18 classes × 2 shuffled + one closed-port row |
| 5 | prints for every row the contract's verdict and attempt count | GEN (`:262-273`) | exact per-row (verdict, attempts) vs class expectation, plus the summary line (checks more than the clause) |
| 6 | in argument order | ORDER (`:274-275`) | exact: printed id list equals argument list (duplicates/misorder fail) |
| 7 | makes exactly the contract's number of requests per URL | BOUND (`:276-284`) | server-side per-path hit counts vs expectation; skips NOROW and the closed-port row — for that row the attempt count is only self-reported (`attempts=9`), anchored server-side solely by DEFAULT's DEAD row (`:306-311`, hits==9) (F7 note) |
| 8 | exits 1 on the mixed fixture and 0 on an all-body fixture | EXIT (`:286-292`) | exact |
| 9 | refuses private hosts without --allow-private | PRIV (`:294-304`) | loopback (127.0.0.1) only: REFUSED attempts=0, zero server hits, exit 1 — the contract's other refusal classes (RFC1918, link-local, reserved, non-resolving host) have no fixture row (F7) |
| 10 | runs three passes 60 s apart by default | DEFAULT (`:306-311`) | exact: UNREACHABLE attempts=9, wall ∈ [100,600] s, 9 server hits |
| 11 | exits 2 with REOPEN_ERROR and no traceback on five bad inputs | ERR (`:313-330`) | exact: the five cases (no id, missing registry, invalid UTF-8, `--passes 0`, `--gap x`), each exit 2 + REOPEN_ERROR + no `Traceback` |

`review_only` (`claims.json:70-73`) matches the docstring (`accept-o.py:64-66`): live-page behaviour and later-round use stay outside the legs. Every O clause lands on a leg. Criterion 11's transport rule is met: neither counter pipes a status (`subprocess.run` + `returncode` only; LOCATE calls the locator in-process).

### F2 — Major (criterion 11): the declaration lists no clause list, and no control artifacts are committed

`QUALITY.md:39`: "The declaration lists each claim's clauses … a non-author seat checks the list against the statement's words before dispatch … Check from committed bytes, before dispatch: the clause list in the declaration, the control script that builds each copy, its receipt in a file criterion 9's two-way check does not read (no `$ ` prefix), and the sha256 of each instrument it ran." Round 62's declaration carries `legs` name arrays (`claims.json:20-35, 58-68`), `review_only` and control lists, but **no clause→leg list** — rounds 54-58 had explicit `"clauses"` arrays (e.g. `reports/round-54/claims.json:19-22`), round 61 embedded per-leg clause parentheticals in its statement; round 62's D statement names only LINK and COPY inline (`:16`) and O names none (`:54`). The mapping lives only in the counters' docstrings, which `claims.json` does not reference for D at all (O has `contract` → docstring, `:55`; D has no such field). Likewise, as of the dry-run state there is no committed control script, no non-`$ ` control receipt, and no instrument sha256s — and the receipt itself is the base run, which criterion 11 says "does not count as a control". This report supplies the non-author clause check; smallest fix: add the clause map (or a D `contract` pointer) as a declaration revision note and land the wave-1 control receipts + hashes as committed non-`$ ` telemetry, as the criterion's check names.

### F3 — Medium (criterion 11): mechanical clauses with no named red control; D's green control undeclared

`controls_required_before_data` (`claims.json:82-94` D, `:96-107` O) does not cover:

- D, clause 2 (bullet / one S-id, ONEID): no control isolates it — the id-only bullet `- (S692)` mutation (w1-spec CtlDDeleteMove) keeps ONEID green by design; a two-S-id line or a non-bullet line would.
- D, clause 15 (ACCESS): no control makes `tools/check-source-access.py` exit non-zero.
- D, clause 15 (LINT): no control produces a MULTI-ID/TABLE-ID finding.
- O, clause 9 (PRIV): no control is a tool that fetches despite no `--allow-private`.
- Green controls: O's list has one ("an honest independent implementation", `:107`); **D's list has none**, although the wave dispatches `CtlDHonest` (`.ufo/waves/round-62/w1-spec.json:101-104`) — the declaration under-lists what the wave runs. Criterion 11 explicitly requires the green control ("a copy where every clause holds, and there the command exits 0").

Smallest fix: add the five red controls and D's green control to the declared lists (declaration text, not counters — no predicate impact).

### F4 — Medium: ROWS checks less than its clause says ("live URL")

Clause: "each listing a live URL and a Wayback capture" (`claims.json:16`). Implementation (`accept-d.py:211-217`): any http(s) URL not containing `web.archive.org/` counts; nothing requests it. LOCATE can pass entirely via the capture while the live URL is dead (the locator tries URLs in order and stops at the first body match). So "live" is enforced as "a non-archive URL is listed first", not liveness — and the clause is not named review-only, which criterion 11 requires for clauses no command checks mechanically. Smallest fix: either name the liveness clause review-only, or have LOCATE's success detail record which URL located (its failure detail already names reasons).

### F5 — Low: OPEN/HEDGE are stricter than their clauses (fails safe)

"Keeps the open country list" / "keeps the source's hedge or attribution" are operationalized as fixed regexes (`accept-d.py:69-70`): an honest rewording without `Belgium` or without `we have`/BBC/programme-attribution phrasing fails a true claim. Stricter-than-clause is safe (junk-token controls target exactly this gaming), and HEDGE's "or attribution" is covered only by the BBC/programme patterns. Informational; wording could name the tokens.

### F7 — Low: O legs narrower than the contract at two points

PRIV exercises only the loopback class of the contract's refusal set (loopback, private, link-local, reserved, unspecified, non-resolving); no fixture row for a non-resolving host, which would be cheap (`http://<random>.invalid/`, expect REFUSED attempts=0). BOUND skips the closed-port row, so "exactly the contract's number of requests" for the connection-error class rests on the tool's self-reported `attempts=` in GEN, anchored server-side only by DEFAULT's DEAD row. Both are statement-compatible ("private hosts" covers loopback) but below the docstring's contract.

## Positive verifications (exercised this session)

- Two-way command coverage mechanically clean (missing/undeclared both `[]`).
- Counter sha256s equal the frozen assignment values; receipt ran revision 0 of both.
- Receipt outputs re-derived against counter code leg by leg: every printed line is what the code produces on the base tree; no leg result is inconsistent with a pre-landing tree.
- Separability absent-land exit 2 with the land named (`:32-33`) — the one receipt line already in criterion 9's named form.
- No clause of either statement is left to an unlisted weaker stand-in predicate; both `review_only` lists match their counters' docstrings.

## Residual risk and verification gaps

- The receipt is uncommitted-at-run-time by its own header; I could not verify from git that the declared bytes, counters and receipt will land together (criterion 8's commit-together rule) — closure must check that from committed bytes.
- I did not run either counter or the separability checker myself (receipts are the evidence; leaf reviewer); the pre-landing outputs are judged against code, not re-executed.
- F1/F2/F3 are declaration/receipt-shape fixes; the wave's control seats are mid-flight, so whether the criterion-11 control receipts and hashes land committed is open at review time.
- Round-62 control lists vs wave items: `CtlDInputs` (robustness: shallow clone, no .git, invalid UTF-8, missing locator) is dispatched but declared nowhere in `claims.json` — beyond clause controls, harmless, but it will leave a receipt with no declaration anchor.

## Sources opened

`reports/round-62/{claims.json, separability-manifest.json, accept-d.py, accept-o.py, telemetry/declaration-dry-run.txt, telemetry/census-start.txt}`; `corpus/QUALITY.md:25-50`; `reports/round-61/{claims.json, telemetry/declaration-dry-run.txt}`; `reports/round-54/claims.json` (clause-list convention); `reports/round-59..61` directory listings; `.ufo/waves/round-62/w1-spec.json`. No installs. No lane writes except this report.
