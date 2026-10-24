# RevCounterCa — attack on `reports/round-65/accept-ca.py` keying (round-64 HIGH-1/HIGH-2 class)

Seat: independent leaf, read-only on the lane. Attacked instrument: `reports/round-65/accept-ca.py`
(186 lines, untracked at HEAD), its frozen predicate `ACCEPT-CA-65`, and the claim-Ca statement in
`reports/round-65/claims.json:59-82`.

**Verdict: the Ca instrument does not close the class it dispositions.** R1 (the HIGH) is reduced to
four substring tests over a file no leg ever compares to git; 8 of 9 legs are satisfiable by appending
literal tokens; the instrument's own PASS names no revision and reads uncommitted bytes, which is the
defect R1 routed. Two crafted patches below: the token-only patch is killed by exactly one leg (R1);
the fabricated-restamp patch is killed by none (demonstrated PASS, exit 0).

## Method

- Lane state: `git -C lane rev-parse HEAD` = `17c32302c6845c8f164b985a8cb312d3181c8788` (= BASE).
  `git ls-files --error-unmatch reports/round-65/accept-ca.py` → untracked. So the counter that
  licenses claim Ca is itself uncommitted and every leg reads uncommitted bytes.
- Baseline run in the lane (read-only, no mutation): exit 1, 9/9 FAIL — matches
  `reports/round-65/telemetry/dry-run-ca.txt` byte for byte, including the QUOTES detail
  `out=['GATE_QUOTES: 0 findings']` on a **failing** leg.
- Attack harness: `/tmp/ca-h` = `git clone --no-checkout` of the lane (hardlinked objects, `.git` at
  BASE) + `rsync -a --exclude .git` of the lane worktree. No lane file, index, or jj state touched.
  Every patch below was applied **only** inside `/tmp/ca-h` and re-run with
  `python3 -B reports/round-65/accept-ca.py --root .` from `/tmp/ca-h`.
- Tooling: no installs; host `git`/`python3`/`rsync` only. The `lsp` device is not in this seat's
  toolset, so caller/definition checks could not be run through a language server; the whole
  instrument (186 lines) was read directly, so no result here rests on grep absence.

## Exact keying, leg by leg

Line numbers are `accept-ca.py`. `read()` (83-86) is a plain filesystem read of the **worktree**
(`open(os.path.join(root, path))`); only R2's baseline (125) and R1's tree lookup (106) call git.

| Leg | Line | Exact bytes it keys on | Base-state truth |
|---|---|---|---|
| R1 | 108-112 | `f"measured revision: {TRUE_REV}" in receipt` **and** `re.search(rf"^tree: {re.escape(tree)}$", receipt, re.M)` **and** `"re-stamped" in receipt` **and** `"measured revision: 95c9194e…" in receipt.split("original receipt bytes")[-1]` | all four absent (receipt is BASE:CA64 verbatim, 784 B) |
| R1 repeats | 113-118 | `"Correction (round 65, R1)" in` LOG.md, SCORECARD.md, `.ufo/waves/round-64/w2/LessonFinal.md` | absent |
| R2 | 126-127 | `base_rev == rev_text[:len(base_rev)]` + `rev_text.startswith(base_rev.rstrip("\n"))` against `git show BASE:revisions.txt`; **and** `"Correction (round 65, R2)" in rev_text and "final-measures-c.txt" in rev_text` | `original_intact=True`; marker absent; **`final-measures-c.txt` already occurs twice at BASE** → the second conjunct degenerates to one appended marker line |
| R3 | 132-134 | `"w1/ReviewerCa.md" in LOG` and `"w2/ReviewerCa.md" in LOG` and `"Correction (round 65, R3)" in SCORECARD` | absent. Note asymmetry: paths checked in LOG, marker checked in SCORECARD; the wrong string is *already* the uncorrected text, so only the correct path must be added |
| R4 | 139-142 | `"statement_correction" in claims` and `"at least their pinned leg" in claims` and `"ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints PASS." in claims.replace("\\","")` | first two absent; **the predicate already occurs exactly once at BASE** → the "unchanged predicate" clause is pre-satisfied and never diffed against BASE |
| R5 | 147-151 | `"c27a9fef" in control-o.txt and "b7d22703" in control-o.txt and "revision 3" in control-o.txt`; **and** `"Control-O binding" in LOG or "control-o binding" in LOG.lower()` | `in_control=True` **already** at BASE (`control-o.txt:1-2`); the whole live work is one literal string in LOG |
| R6 | 155 | `"Correction (round 65, R6)" in round-64.md and "R64-M12" in round-64.md` | marker absent; `R64-M12` pre-exists as the corrected text → one appended marker line |
| R7 | 159-164 | first `^- verified-at:.*$` match in the entry, and `not re.search("skeleton|await L1", line, I)` | currently the stale line → fix = delete the clause; **no content requirement** |
| CRITERION | 168-169 | `re.search(r"^1[7-9]\.\s", QUALITY, re.M)` and `re.search(r"tree hash", QUALITY)` | both absent |
| QUOTES | 172-181 | subprocess `tools/check-gate-quotes.py <root>/corpus/lessons/round-65.md` with `cwd=root`; `returncode == 0 and "0 finding" in stdout` | lesson absent → tool exit **2**; tool prints `GATE_QUOTES: 0 findings` anyway |

Class note: the round-64 routed HIGH-1 was "two legs remain global token-presence checks; a generic
records-only append flips them" (`.ufo/waves/round-64/w2/RevVerifyCa.md:91`; HIGH-2 the denial-prose
bypass, `:119`). Claim O's own statement (`claims.json:34`) records that this revision "keyed legs"
were meant to end exactly this.

## Patch A — global-token-only, `8bab271c` everywhere, receipt never re-stamped

Applied in `/tmp/ca-h` (no git writes): appended `Correction (round 65, R1)` to LOG.md, SCORECARD.md,
`w2/LessonFinal.md`; one LOG line carrying both `w2/ReviewerCa.md` and `w1/ReviewerCa.md` plus
`Control-O binding`; `Correction (round 65, R3)` to SCORECARD; `Correction (round 65, R2): final-measures-c.txt.`
to revisions.txt; `statement_correction: … at least their pinned leg.` appended to
`reports/round-64/claims.json`; `Correction (round 65, R6) applies to R64-M12.` to `round-64.md`;
`- verified-at: 2026-10-24` substituted for the stale line; `17. A receipt must pin the tree hash of its
read inputs.` appended to QUALITY.md; a one-row `## Gate` lesson at `corpus/lessons/round-65.md`.
`8bab271c` was pasted into prose only; `final-measures-ca.txt` left byte-identical to BASE.

Result (real output):

```
R1 FAIL restamp=False tree=0ec0e50ea828ca6d8e20298f72af49414692e9e4 repeats_log_score_lessonfinal=True
R2 PASS  R3 PASS  R4 PASS  R5 PASS  R6 PASS  R7 PASS  CRITERION PASS  QUOTES PASS
ACCEPT-CA-65: FAIL    (exit 1)
```

**Exactly one leg kills Patch A: R1**, and only because none of its four receipt tokens is present.
No leg checks that `8bab271c` names the revision the *records* bytes belong to, that the receipt's
title still says FINAL, or that the three "correction" lines say anything. 8/9 legs are global-token
satisfiable — the same shape as the round-64 HIGH-1 legs this revision claims to have replaced.

## Patch B — "re-stamp" by fabrication (original bytes destroyed)

Wrote `final-measures-ca.txt` as 5 lines: a re-worded title with `re-stamped`, `measured revision:
8bab271c…`, `tree: 0ec0e50ea828ca6d8e20298f72af49414692e9e4` (the real tree of 8bab271c, obtainable by
`git rev-parse` — the docstring hands the reader the revision), a marker line
`--- original receipt bytes (as superseded) ---`, and one fabricated line
`measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2`. The genuine 19-line receipt
(counter sha, command, date, 7 PASS lines) is **deleted**; the receipt no longer preserves a single
original byte, and no leg notices.

Result: **`ACCEPT-CA-65: PASS`, exit 0, 9/9 legs**, with the three token corrections of Patch A still in
place. **No leg kills Patch B.** Statically confirmed: `CA64` appears only at :66 (constant) and :105
(`read`); there is no `git show BASE:CA64`, no hash of the preserved region, no length/content check.
R1's fourth clause needs only that the string `measured revision: 95c9194e…` appear **after the last**
occurrence of the literal `original receipt bytes` — one fabricated line satisfies it. The receipt's own
`counter sha256: d0787979…` claim is likewise never re-verified (no leg hashes accept-ca.py, and
`sha256`/`hashlib`/`__file__` occur in the docstring only).

This is round-64 HIGH-1's substance — a receipt whose bytes cannot be attributed — re-created by the
instrument that dispositions HIGH-1. Claim Ca's text ("the original bytes preserved") is unfalsifiable
by its counter.

## Patch B′ — empty tree pin when `git rev-parse` fails (escape hatch)

`tree_code` is computed at :106 but **not gated** in `r1_ok` (:108-112); `re.escape("") == ""`, so when
the revision is unresolvable `tree = ""` and the pattern `^tree: $` matches a receipt line `tree: `
(trailing space). With a `PATH` shim whose `git` exits 128 only for `rev-parse` and delegates otherwise
(what a shallow/`git archive`/exported verification checkout produces for an absent sha), receipt line
`tree: ` gives:

```
R1 PASS restamp=True tree=unresolvable repeats_log_score_lessonfinal=True
… ACCEPT-CA-65: PASS    (exit 0)
```

`tree=unresolvable` is printed in the detail string only; nothing fails on it. In any environment that
does not carry `8bab271c`, R1 binds **no hash at all** and still prints PASS. Because `.git` here
carries the sha, the live lane is not currently in that state — the defect is latent, not hypothetical:
it is exactly how a CI/export verification run would evaluate this instrument.

## Cross-cutting HIGH: "committed bytes" is false, and PASS names no revision

- Docstring :7 and claim Ca (`claims.json:61`) say "one counting leg over **committed bytes**". R2's
  baseline (`git show BASE:…`) is the only git read of content; every other leg is `open()` on the
  worktree. Patch A/B passed with HEAD still at BASE and every edited file uncommitted: a staged or
  dirty patch and a committed one are indistinguishable to this instrument.
- The counter emits no revision, no tree, no worktree-status line, and no self-hash: its output is nine
  leg lines plus `ACCEPT-CA-65: PASS`. So a PASS is attributable to **no revision**. The round-64
  routed defect states the rule the instrument now violates: "a verdict names the revision it was
  measured against" (`round-64-verifier-spotcheck.md:47-53`), and CRITERION (:168-169) mints that rule
  for receipts while accept-ca.py itself violates it. Self-application gap.
- `git status` is never consulted; the round-64 HIGH-1 failure mode (receipt over a dirty worktree) has
  no detector inside the Ca counter.

## MEDIUM — negation-blind / empty-value legs (empirically PASS)

- CRITERION is presence-only: replacing the new criterion with
  `17. A receipt must NOT pin a tree hash; pin only the counter sha.` still prints
  `CRITERION PASS criterion_with_tree_hash=True`. The criterion's content (pin measured revision **and**
  tree hash, never only the counter sha) is unverified; any line `1[7-9]. ` plus any `tree hash` token
  anywhere in the file passes. (`corpus/QUALITY.md` is 53 lines with criteria 1-16, so the number
  conjunct does require new text — the content conjunct does not.)
- R7 accepts an empty value: `- verified-at:` with nothing after the colon → `R7 PASS line='- verified-at:'`.
  It also only inspects the **first** `^- verified-at:` line; the stale clause surviving on a
  continuation line, in another field of the same entry, or on a second `verified-at` would not be seen.
- R4 reads `reports/round-64/claims.json` as text, never parses it: appending
  `statement_correction: …` after the closing brace (invalid JSON) passes; the predicate clause can be
  satisfied by the pre-existing occurrence while the actual predicate sentence is moved or edited
  elsewhere, because there is no `git show BASE:` diff for this file (contrast R2, which does diff).
  The "byte-unchanged" promise in the docstring (:44-45) is unimplemented.

## LOW — QUOTES delegation and its receipt hazard

- The leg's `"0 finding" in q_out` conjunct is worthless: the tool prints `GATE_QUOTES: 0 findings` on
  every exit path including exit 2 (observed at baseline and recorded in `dry-run-ca.txt:8`). Only the
  exit code gates. Consequence for records: a receipt that pastes the stdout tail reads "0 findings"
  for a **failing** leg — the round-64 HIGH-2 receipt class.
- Coverage: `check-gate-quotes.py` skips `truncated-grounds` for S-ids absent from the registry and
  cannot fire `over-cap` on rows with no quoted spans (tool docstring :15-63). A `## Gate` section with
  rows carrying no/one-word quotes therefore yields exit 0 with the claim-C quotation discipline
  unchecked. My single-row `## Gate` file passed QUOTES.
- The leg is bound to `corpus/lessons/round-65.md` only; any other round-65 Gate rows are unread.

## LOW — documented exit contract unimplemented

Docstring :18 promises "2 on unreadable input"; there is no `return 2`/`sys.exit(2)`, and `read()`
swallows `OSError` to `""`. A missing `git` binary raises `FileNotFoundError` → traceback, exit 1.
Exit 2 is never produced.

## Dependency finding

`reports/round-65/telemetry/controls-ca.txt` does not exist (telemetry holds only `census-start.txt`,
`controls-c.txt`, `dry-run-c.txt`, `dry-run-ca.txt`, `dry-run-o.txt`). `claims.json:88` requires
"controls-ca.txt … meet the frozen counters' prior revision (the round-64 form) and fail the round-65
form" **before data**. The pre-data control for Ca is therefore unverifiable from disk; `dry-run-ca.txt`
is a base-state FAIL run, not a prior-form control.

## Residual risk and verification gaps

- Patches were executed in `/tmp/ca-h` (clone at BASE + rsync worktree). All legs are path-based, so
  behavior is identical to the lane; R2's baseline bytes are identical (same `.git` object).
  No lane file, index, or jj state was written; no git/jj write was run.
- Not attempted: accept-c.py / accept-o.py attacks (other seats), registry/tier inflation for claim C,
  and the round-65 entries' substance. Claims Ca's *substance* (that the R1-R7 repairs are truthfully
  stated) is a separate question: this report shows the instrument cannot distinguish a true repair
  from a fabricated one.
- Fix shape implied by the evidence (not applied): compare the preserved region to `git show BASE:CA64`
  byte-for-byte and require it to equal the base bytes; fail when `tree_code != 0`; gate on
  `git rev-parse HEAD`/worktree-vs-tree equality; emit the measured revision + counter sha; diff
  `reports/round-64/claims.json` against BASE and parse it; require the CRITERION text to contain the
  affirmative pair (measured revision **and** tree hash) rather than a negation-blind token; require a
  non-empty value on the `verified-at` line. Recommendation only — I do not edit integration.

Report: .ufo/waves/round-65/w1/RevCounterCa.md
