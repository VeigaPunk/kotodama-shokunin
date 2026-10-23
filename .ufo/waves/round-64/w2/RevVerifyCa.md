# RevVerifyCa — claim Ca counter verification (final pin `7319ff4b…`)

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (jj-colocated, read-only).
Base: `ff30a205c8d23b35f1ac533740121a955a9fda96`. Declaration: `097c21d`.
Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w2/RevVerifyCa/` (shared clone `lane/`; pinned copies `accept-ca-rev2.py`, `accept-ca-new.py`; receipts `new-*.txt`, `rev2-*.txt`, `diff-*.txt`).

Axes named: calibration (primary), operability (controls, error paths), coverage (only gate-input state; no row/entry review). Reviewer only: I edited no lane file, row, counter or record; no commit; no claim judgment. No tools installed or updated. No `lsp` device is mounted on this seat (`read xd://lsp` → `No such tool: xd://lsp`), so caller/definition checks are text-grep plus executed runs; the counter has no code callers (only `claims.json:55`, spec/taskcall JSON, and its own docstring name it).

## Instrument history observed by hash

| version | sha256 | observed |
|---|---|---|
| rev1 | `f222648e…81d678` | 02:45Z, 02:52:28Z (byte-identical to CriticCa's fingerprint) |
| rev2a | `a8088092…f9060c` | 02:53:35Z – 02:56:52Z |
| rev2b (final pin) | `7319ff4b9c7eb2cd23f866eb4db62d469a539b8dd99b8326fb6bae8f1cb0d4c5` | 03:01:08Z onward; live sha re-checked after every scratch run, stable |

All results below were executed against the pinned copy `accept-ca-new.py` (sha `7319ff4b…`), not a moving file. Rev2b's diff vs rev2a is confined to the docstring revision history and the NITS leg; CANONLOG/PTRS/REVNAMES rev1 edits and HISTOGRAM/DISPO/R63SEP are unchanged.

## Checklist result (rev2b)

| item | requirement | result |
|---|---|---|
| 1 | working-tree full run, all 7 legs PASS | **PASS** (exit 0, pasted below) |
| 2 | CriticCa records-only mutation (without and with bare tokens) FAILs rev2 NITS | **PASS** — both fail; additionally the stronger wrong-substance and vacuous-phrase variants fail (table below) |
| 3 | base tree fails all 7 legs | **PASS** (7/7 FAIL, exit 1) |
| 4 | predicate sentence byte-identical vs `claims.json` | **PASS for claims.json** (byte-stable); in-script copy differs by one LF; no receipt carries it |

## Item 1 — full run on the working tree (rev2b)

```text
$ python3 -B reports/round-64/accept-ca.py --root .
CANONLOG PASS r64_at=272051 stray_has_r63=True points_at_stray=True prior_rounds=56
PTRS PASS score_dead=False stray_dead=False o_fixed=True c_fixed=True
HISTOGRAM PASS tiers={'A': 13, 'B': 11} correction_present=True
DISPO PASS items5_7=True s687_flip=True s693_kind=True
REVNAMES PASS missing=[]
NITS PASS correction_record=True seat_reports_nit=True duplicate_url_nit=True fail_legs_nit=True
R63SEP PASS result_cited=True dep_class_named=True
ACCEPT-CA-64: PASS
exit=0
```

Caveats (LOW-6): the run reads uncommitted `LOG.md`/`SCORECARD.md`/`corpus/LOG.md` and an **untracked** `reports/round-63/telemetry/revisions.txt`; the docstring says the legs verify "committed bytes"; no `final-measures-ca.txt` receipt exists yet (only the base `dry-run-ca.txt`).

## Item 2 — records-only controls against rev2b NITS

All fixtures: base files from `git show ff30a205:{LOG.md,SCORECARD.md,corpus/LOG.md}`, no `revisions.txt`, plus appended prose inside a `## Round 64` block.

| fixture | NITS | detail |
|---|---|---|
| `base` | FAIL | `correction_record=False seat_reports_nit=False duplicate_url_nit=False fail_legs_nit=False` |
| CriticCa exact append (records-only, `W04` token only) | **FAIL** | all False |
| same prose with bare 45/47/W04/27 | **FAIL** | all False |
| wrong-substance denial ("47 … is merely a filing example; round 63 still had 45 … No measured correction is made.") | **FAIL** | all False |
| vacuous phrase list ("Reviewed: 47 seat reports; 27 duplicate-URL rows; W04 noted; 9 FAIL legs.") | **FAIL** | all False |
| generic token note (DISPO/HISTOGRAM/R63SEP tokens) | **FAIL** | all False |

Rev2b requires a line in the canonical Round-64 block labelled `Round-63 numeric corrections:` that carries three exact affirmative old→new phrases: `47 seat reports landed, not 45`; `W04 covers 27 duplicate-URL rows, not just S650/S651`; `ACCEPT-O-63 dry run had 9 FAIL legs … not 6`. This rejects the whole records-only class the assignment names, including the wrong-substance control that falsified rev2a.

**Residual mention-vs-assertion holes (executed, both PASS):**

- Same-line quotation + denial: a labelled line containing all three exact phrases followed by `— quoting a false proposal; no measured correction was made.` → `NITS PASS correction_record=True seat_reports_nit=True duplicate_url_nit=True fail_legs_nit=True` (`new-mut-quoted-denial.txt`).
- Cross-round attribution: labelled line `a hypothetical round would say 47 seat reports landed, not 45; … None of this is claimed for round 63.` → `NITS PASS` all True (`new-mut-attributed.txt`).

Both reproduce CriticRevCa's "assertion/mention and attribution" hazard at the new, narrower boundary: the leg can verify that the exact correction sentences appear under the expected label, not that the record is not quoting or attributing them elsewhere. A records-only forger must reproduce the correction sentences verbatim to pass, so this is a semantic limit rather than the earlier token loophole; it should be disclosed rather than advertised as arbitrary natural-language verification.

## Item 3 — base tree fails all 7 legs (rev2b)

```text
CANONLOG FAIL r64_at=-1 stray_has_r63=True points_at_stray=False prior_rounds=0
PTRS FAIL score_dead=True stray_dead=True o_fixed=False c_fixed=False
HISTOGRAM FAIL tiers={'A': 13, 'B': 11} correction_present=False
DISPO FAIL items5_7=False s687_flip=False s693_kind=True
REVNAMES FAIL missing=['8d2041fa', '38ec1316', '0c892ce', '80ff34c', 'final-measures-c.txt', 'final-measures-o.txt', 'rev-separability.txt', 'census-end.txt']
NITS FAIL correction_record=False seat_reports_nit=False duplicate_url_nit=False fail_legs_nit=False
R63SEP FAIL result_cited=False dep_class_named=False
ACCEPT-CA-64: FAIL
exit=1
```

HISTOGRAM's registry half already computes `A=13 B=11` at base, so its base failure is only `correction_present=False`.

## Item 4 — predicate sentence vs claims.json

- `reports/round-64/claims.json` is byte-stable: declaration `git show 097c21d:reports/round-64/claims.json` and worktree both sha256 `e970aaceafa377230c91775f5b1b34e69aeb176faa52404715653d911a09bd3a`; `git diff 097c21d -- reports/round-64/claims.json` is empty. Predicate bytes: `ACCEPT-CA-64: every leg of reports/round-64/accept-ca.py prints PASS.` (69 chars).
- The copy in the counter docstring is **not** byte-identical: it wraps as `...accept-ca.py\nprints PASS.` — one LF where the predicate has a space (`p in normalize(doc)` True, `p in raw_doc` False).
- The docstring still asserts the sentence is "in every receipt"; it is not. No telemetry receipt carries the sentence; `reports/round-64/telemetry/dry-run-ca.txt:8` carries only `ACCEPT-CA-64: FAIL`. `claims.json` is byte-identical to its own declaration; nothing else is byte-identical to `claims.json`.

## Findings by severity

**HIGH-1 — two legs remain global token-presence checks; a generic records-only append flips them under rev2b (calibration).**
Executed against the pinned rev2b, base files plus generic prose containing only tokens (`Items 5, 6 and 7 … S687 is queued … SEPARABILITY: 2 findings, exit=1 … record dependency … REC … 13 / 11 … 45, 47, W04 and 27`):

```text
HISTOGRAM PASS tiers={'A': 13, 'B': 11} correction_present=True
DISPO FAIL items5_7=False s687_flip=True s693_kind=True
NITS FAIL correction_record=False seat_reports_nit=False duplicate_url_nit=False fail_legs_nit=False
R63SEP PASS result_cited=True dep_class_named=True
```

HISTOGRAM's `correction_present` accepts bare `13 / 11` anywhere in SCORECARD; R63SEP's `dep_class` accepts the three-letter substring `REC` plus `record dependency` anywhere in the 276 KB log; DISPO's `s687_flip` is the token pair `S687`+`queued`, and `items5_7` is literal `"item 5"`/`"item 6"`/`"item 7"` (my `Items 5, 6 and 7` failed only on case). `claims.json`'s Ca control sentence is narrowly worded ("without the named values still fails PTRS/HISTOGRAM/REVNAMES") so it is not itself falsified, but the predicate does not establish the discrimination the axis needs. A rev3 scoping of these legs (as NITS received) would still be a pre-data revision and is permitted — no acceptance datum exists.

**MEDIUM-2 — NITS passes same-line quotation-denial and cross-round attribution (calibration).**
Witnesses in item 2. Rev2b rejects all records-only controls that lack the exact correction sentences, so the assignment's item 2 is met; the remaining hole is semantic (mention vs assertion, attribution) and should be disclosed in the receipts rather than treated as full semantic verification.

**MEDIUM-3 — the docstring's "revision 2" now identifies two different byte states, and its forcing list was expanded post-hoc (calibration/provenance).**
`a8088092` (02:53Z) and `7319ff4b` (03:01Z) are both labelled "revision 2"; the second rewrote the first's NITS logic and added `.ufo/waves/round-64/w2/CriticRevCa.md` and `.ufo/waves/round-64/w2/RevVerifyCa.md` to the forcing controls. Nothing is committed and no Ca receipt exists yet, so L1 can regularise this by stamping the committed bytes as a distinct revision (rev3) with these receipts, or by confirming rev2 was never published; otherwise any future citation of "rev2" is ambiguous. Lane rule: every counter change is a stamped pre-data revision committed with its forcing-control receipt.

**MEDIUM-4 — PTRS passes only by rewriting filed historical bytes; the log declares append-only (calibration, contract conflict).**
`LOG.md:1` is `# kotodama-shokunin — iteration log (append-only)`, and the Round-64 entry context says "Prior rounds stand as filed." Yet `git diff 097c21d -- corpus/LOG.md` rewrites three filed Round-63 lines (O receipt `final-measures.txt`→`final-measures-o.txt`; C receipt →`final-measures-c.txt`; the routed-records sentence), and `SCORECARD.md`'s filed row 1210 replaces `reports/round-63/telemetry/final-measures.txt` with `final-measures-o.txt` in place. `accept-ca.py:97-102` requires the dead filename to be absent from the round-63 block and the stray log, so an append-only erratum can never pass PTRS. CriticCa §D raised this; it remains live and needs a canonical-judge decision on the instrument or an explicit preservation rule.

**LOW-5 — documented `exit 2 on unreadable input` remains partially implemented (operability).**
`read(SCORE)` sits outside the guarded block. Missing `LOG.md` → `ACCEPT_CA_INPUT_ERROR …`, exit 2 (correct). Missing `SCORECARD.md` → uncaught `FileNotFoundError` traceback, exit 1 (contradicts the docstring's exit-2 contract).

**LOW-6 — predicate copy/receipt claim inaccurate; PASS not bound to committed bytes (calibration evidence) — and the PASS reads a new untracked file.**
See items 1 and 4: one-LF docstring difference, false "in every receipt" assertion, uncommitted landed files, untracked `reports/round-63/telemetry/revisions.txt` (`git ls-files --error-unmatch` fails; `git check-ignore` exits 1, i.e. not ignored), no `final-measures-ca.txt`. Until L1 commits and names the revision, the 7/7 PASS has no committed-tree anchor; it should be re-run post-commit and filed as a receipt naming that revision.

**RESOLVED by rev2b (recorded for the forcing trail).**
- Rev2a's wrong-substance/vacuous-phrase NITS passes (reported by this seat as HIGH-2 and by CriticRevCa) now FAIL; the leg requires the labelled affirmative Round-63 record with exact old→new phrases.
- The `^## ` extractor's `###` truncation hazard is fixed by `^## (?!#)` in rev2b.
- Minor docstring mismatch remains: the NITS description names "the SCORECARD round-63 correction row", but the leg reads only the canonical `LOG.md` block. No current failure; note it if the docstring is revised again.

## Residual risk and verification gaps

- The counter moved twice during verification (rev1 → rev2a → rev2b). I verified the pinned final `7319ff4b…`; if RevCounters edits again, L1 must re-run the four checks against the committed bytes and stamp a distinct revision. Nothing here weakens a leg; this report changes no counter and no record.
- No language server was available; caller analysis is text-only (the script has no code callers), and there are no type/definition diagnostics to consult.
- Historical values 47 seat reports, 27 W04 rows, 9 dry-run legs and the S687 `queued` flip were checked only at receipt/worktree level (CriticCa and the diffs above); I did not re-derive them from `.ufo/waves/round-63/w1` or the census.
- Executed probes: base, CriticCa exact, bare-token, wrong-substance, vacuous-phrase, generic-token, quoted-denial, attribution — eight fixtures per pinned revision (rev2a and rev2b), not an exhaustive mutation battery over the seven legs. Of CriticRevCa's rev2 fixtures I reran the wrong-substance one on rev2a; their negated-phrase and out-of-scope fixtures were not rerun on rev2b (their word order does not match rev2b's required phrases).
- Base-tree tests used a shared clone's working directory and `git show`; the lane repo, its index and jj state were not mutated.

Report: .ufo/waves/round-64/w2/RevVerifyCa.md
