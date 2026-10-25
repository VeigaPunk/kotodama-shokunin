# CritMistakeFix — attack on the round-73 mined-mistake plan (R2: verdict asserted against a FAIL receipt)

seat: CritMistakeFix (critic, leaf) · round 73 (hyaku run 7) · date 2026-10-25
lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` · base `8841ad3b896a0227674fa0725b818c999118046f`
attacked text: `reports/round-73/claims.json` (DRAFT-v0, claim **Ca**, legs `LEDGER`..`STAMP` at `:40-47`, `after` `:38`, `kill_rule` `:49`) — read only, never edited
write scope: this file. No lane write, no fleet write, no `claims.json` edit, no counter built, no tool installed, no network fetch (no User-Agent recorded because nothing was fetched live).
fixture provenance: all fixtures under `/tmp/CritMistakeFix/` (seat evidence only — **not** closure-resolvable per PROTOCOL §Evidence standard; the committable red-before is the base-commit run in §5).

---

## 1. Class

**Class name: `verdict-asserted-against-receipt` — a records file states a gate verdict token that the receipt it cites does not carry, and the run that would have produced the asserted verdict is never committed.**

The shape is exact and mechanical: the records row and the receipt disagree on **one word**, and the receipt's own terminal line is `ACCEPT-<id>: FAIL legs=<n>/<n>` — so the numeric token beside the verdict word (`legs=12/12`) is identical in the PASS and FAIL case and cannot contradict the copy.

Three instances on disk, one per ~6 rounds, each caught by a non-author's prose, never by a leg:

| # | round | records row | asserted | cited receipt (committed) | receipt says | introduced → settled |
|---|---|---|---|---|---|---|
| 1 | 59 | `SCORECARD.md:1134` (coverage axes row) | PASS | `reports/round-59/telemetry/as-reviewed-c.txt:18` | `ACCEPT-C-59: FAIL` | `7d19bd1` → corrected `47f27bd` (`SCORECARD.md:1147`) |
| 2 | 66 | fleet report `.ufo/reports/round-66/kotodama.md` | PASS | `reports/round-66/telemetry/final-measures-ca.txt` | `D2 FAIL` | corrected `SCORECARD.md:1293` |
| 3 | **72** | `SCORECARD.md:1401` (calibration axes row) | `ACCEPT-CA-72 PASS legs=12/12` | `reports/round-72/telemetry/measures-ca.txt:29` | `ACCEPT-CA-72: FAIL legs=12/12` | `b47033a` → **still open at base** (`corpus/lessons/round-72-verifier-spotcheck.md:31`, `:66`) |

Instance 3 is the round's primary mistake. Its mechanism is visible in the counter itself: `reports/round-72/accept-ca.py:231` prints

```python
print("ACCEPT-CA-72: %s legs=12/12" % ("PASS" if ok else "FAIL"))
```

— the leg tally is **hardcoded**, so `legs=12/12` appears on a FAIL receipt. The SCORECARD row's `PASS legs=12/12` is one word away from the committed receipt, and the number it quotes was copied from that FAIL receipt. Any leg that reads the tally instead of the verdict word is blind by construction.

## 2. Captured-by verdict: **named by a criterion, not captured by any leg**

Which rule should have caught it, read in order of specificity:

| rule | location | verdict |
|---|---|---|
| QUALITY 17, second sentence: "stamping a revision whose bytes fail the receipt's own legs" | `corpus/QUALITY.md:55` (landed r65, `3b1b5a6`) | **this is the exact rule** — the SCORECARD row stamps a PASS onto bytes whose own legs print FAIL. But 17's stated *Check* is narrower than its rule: "the accept-ca RECEIPTS leg of each round re-derives the lands revision and rejects receipts whose stamp, tree or counter sha do not match" — stamp/tree/sha only, **never the verdict word against a records row**. The rule existed for seven rounds and both later instances (66, 72) recurred under it. |
| QUALITY 9 / 11 | `corpus/QUALITY.md:35`, `:39` | meta-rules that should have forced the leg: every declared clause needs a command that can fail, and every receipt command must match a declaration. The SCORECARD verdict was a declared clause with no command. |
| QUALITY 19 | `corpus/QUALITY.md:59` (landed r67, `c5f0992`) | governs *where* a receipt runs and states explicitly that carrier-parentage "cannot be a lands-time leg … it is post-records evidence, graded after the records commit". Its "a receipt that does not exist at the lands revision is a FAIL (`unreadable`), never a skip" does **not** fire: the cited receipt exists at lands — it is the *rerun* that does not. 19 therefore cannot force a post-report rerun to be committed. |
| PROTOCOL §Evidence standard, "Claimed ≠ re-executed": "A command offered as evidence is a re-run performed at write time with its observed output" | `PROTOCOL.md:374` | the row quotes a run nobody performed; the rule is exactly on point, but it assigns no checker. |
| PROTOCOL §Gate standard: "A tool that cannot fail is a probe, and is registered as one" | `PROTOCOL.md:391-392` | the round-72 Ca counter is a gate for 12 legs and a **probe** for the SCORECARD surface (it never reads it). Registering the surface as "ungraded" was never done. |
| PROTOCOL snapshot clause: "Round prompts are snapshots: where a prompt … conflicts with the current `PROTOCOL.md` or `CORPUS.md`, the repo files win" | `PROTOCOL.md:90` | the prompt's claim text said `12/12 PASS`; the repo file (receipt) said FAIL; repo files win — so the row is a conformance defect under this clause too, again with no checker attached. |

Mechanical check that nothing reads the surface: no counter in rounds 66–72 opens `SCORECARD.md` (`grep -rn SCORECARD reports/round-*/accept-*.py` → only `round-64/accept-ca.py:60,99` and `round-65/accept-ca.py:94,103`). The capability existed at r64 (`PTRS` leg reads the round-63 SCORECARD block) and at r65, and **lapsed from r66 onward**; even when present it checked pointer filenames (`final-measures-o.txt`), never a verdict word.

**Verdict: `captured-by = QUALITY 17 (in words), none (mechanically)`.** The round's ledger entry R2 is correct as an instance; the *class* has no owner.

## 3. Recurrence test against claim Ca **as drafted**: no leg turns red

Constructed recurrence (fixture B below): a round-73 SCORECARD axes row asserts `ACCEPT-CA-73 PASS legs=12/12` while the committed `reports/round-73/telemetry/measures-ca.txt` prints `ACCEPT-CA-73: FAIL legs=12/12`. Leg-by-leg:

| Ca leg (`claims.json:40-47`) | surface it reads | red on the recurrence? |
|---|---|---|
| `LEDGER` | `reports/round-73/ledger.json` (fixed at freeze) | **no** — the row is written during the round, after the freeze; it is not a pair |
| `BASEMISMATCH` | the counter at base | no — base has no round-73 row |
| `REPAIR` | each REPAIR pair's receipt, searched for a PASS stamp | **no** — and it is satisfiable *while the disagreement stands*: fixture E commits a PASS rerun at a new path and the row still cites the FAIL receipt → `REPAIR` green, class intact |
| `ANNOTATE` | correction rows, per ledger pair | no — scoped to pairs |
| `APPENDONLY` | `git diff --numstat` removed lines | no — a false row **adds** lines |
| `NOSTUB` | shape of correction rows | no — the recurrence is an axes row, not a correction row |
| `SEPARABLE` / `STAMP` | Ca paths / the claim's own receipt | no — the claim's receipt can be perfect while a records row lies |

Ca is **instance-scoped by construction** (`before` at `claims.json:37` fixes the universe to the wave-1 sweep's pairs; the title's "self-assessment vs repo-state ledger" is really "vs the ledger"). It repairs R2 and cannot see R2's next occurrence. That is the defect I route.

Second, independent defect in the same claim text: the after-state token at `claims.json:38`, `PASS legs=<n>/<n> (n fixed at freeze)` inherits the hardcoded tally. A future row can quote `legs=12/12` from a FAIL receipt verbatim; the tally is never evidence of a verdict.

## 4. The smallest fix that makes the next recurrence red

One leg, added to Ca's `legs` array before freeze (no new gate, no new registry row, no new authority — it restores the SCORECARD-reading pattern `round-64/accept-ca.py:99` already used, with verdict semantics):

> **`VERDICTAGREE`**: every `SCORECARD.md` row **added in `base..<lands>`** under `## Axes — round <N>` that asserts a gate verdict token `ACCEPT-<ID>-<N>:? (PASS|FAIL)` (an `→ PASS`/`→ FAIL` inherits the last id) **and cites** `reports/round-*/telemetry/*.txt` carries, for that gate id, the **last** asserted word equal to the **last** `ACCEPT-<ID>: (PASS|FAIL)` line of the cited receipt read with `git show <lands>:<path>` — unless a correction row names the id and carries **both** words with its last word equal to the receipt's (stated→observed); the same check runs over every row named by a ledger pair; base `SCORECARD.md` must be a line-prefix of lands (else `COULD-NOT-EVALUATE`, exit 2).

Three properties, each measured below:

1. **Scoped, not full-file.** Universe = new rows ∪ ledger-pair rows. Full-file scope is a permanent-red trap: any historical uncorrected row makes every future round's Ca red forever (measured: at `8841ad3`, full-file scope = 17 rows graded, 1 finding; scoped with no pairs = 0 graded, PASS).
2. **Settles by the two repairs Ca already permits** — the sanctioned re-stamp below a marker in the cited receipt (QUALITY 17's preserved-bytes rule) and an appended correction row. It never asks for a rewrite of frozen bytes.
3. **Reads only committed bytes**, so it is a lands-time leg (QUALITY 19) and adds nothing to the post-records set.

Recommended companion edits (same claim, no scope growth):
- `after`: print `PASS legs=<passed>/<total>` (never a constant), so the tally differs between verdicts. Round-72's counter printed `legs=12/12` on both (`accept-ca.py:231`) and its FAIL receipt proves the token is quotable from a failure (`measures-ca.txt:29`).
- `REPAIR` R2: bind the accepted rerun to **the receipt path the SCORECARD row cites** ("a committed receipt carrying a PASS stamp" is satisfiable at a new path while the row still cites the FAIL receipt — fixture E). With `VERDICTAGREE` in place this is redundant but it removes the false assurance from the leg's own wording.
- `kill_rule`: add "or any axes row's asserted verdict disagrees with the receipt it cites and no correction row settles it".

## 5. Red-before demonstration (minimal, CORPUS kaika rule)

`CORPUS.md:169` — "Ship a red-before state where the same command exits non-clean for the named reason and the fix is the only delta." The class is already on disk, so **no fixture needs committing**:

- **Red (committable, pre-data):** run the leg at base `8841ad3` naming the ledger pair → observed
  `ROW SCORECARD.md:1401 ACCEPT-CA-72 asserted=PASS receipt=reports/round-72/telemetry/measures-ca.txt verdict=FAIL DISAGREE` / `VERDICT-AGREE: FAIL graded=1 findings=1` / exit 1.
- **Green (committable, at `<lands>`):** the same command after R2's repair → `VERDICT-AGREE: PASS graded=1 findings=0` / exit 0 (measured on fixture A, which is the lane's bytes plus the R2 correction row: the fix is the only delta).
- **Stub control (must stay red):** a correction row naming only the id does not settle (fixture D) — this is the round-69 stub-row class, and it is the control that keeps the settlement clause honest.

The `/tmp` fixtures below prove the leg catches a **future** recurrence and that its settlement routes are exactly the two legal repairs; they are seat evidence, not closure evidence.

## 6. Measured controls (all runs: committed bytes via `git show`, exit codes as shown)

Fixture repo: `D=$(mktemp -d /tmp/CritMistakeFix/fx.XXXXXX)`, `git -C "$D" init -q`, base = `git archive 8841ad3 SCORECARD.md reports` (all git calls name `-C "$D"`; local throwaway identity set only inside `$D`).

| point | construction | command | observed | verdict |
|---|---|---|---|---|
| lane @ base, full-file scope | lane bytes, no correction row | `verdict-agree-probe3.py . 8841ad3` | 17 pairs, 1 finding: `SCORECARD.md:1401 … DISAGREE`; exit 1 | **red** — the class is caught on committed history, no fixture |
| lane @ base, scoped, no pairs | `--base 8841ad3` | `verdict-agree-probe4.py . 8841ad3 --base 8841ad3` | `PASS graded=0 findings=0`; exit 0 | no historical bleed |
| lane @ base, scoped, pair `ACCEPT-CA-72` | as above + `--pair ACCEPT-CA-72` | probe4 | `:1401 … DISAGREE`, `FAIL graded=1 findings=1`; exit 1 | R2 red-before |
| **A** settle R2 | lane + `## Corrections — round 73` row (stated PASS / observed FAIL) | probe3 `0d84971` | `PASS pairs=17 findings=0`; exit 0 | **green**, fix = only delta |
| **B** recurrence | A + round-73 axes row `ACCEPT-CA-73 PASS legs=12/12` + receipt `ACCEPT-CA-73: FAIL legs=12/12` | probe4 `e5e9dd2 --base 0d84971` | `:1419 … DISAGREE`, `FAIL graded=1 findings=1`; exit 1 | **the recurrence is red** |
| **C** settle recurrence | B + correction row (stated PASS / observed FAIL) | probe4 `831982d --base 0d84971` | `:1419 … SETTLED`, `PASS graded=1 findings=0`; exit 0 | green |
| **D** stub control | B + correction row naming only `ACCEPT-CA-73` | probe4 `8b4c4df --base 0d84971` | `:1419 … DISAGREE`, `FAIL graded=1 findings=1`; exit 1 | stub does **not** settle |
| **E** Ca's REPAIR wording | B + PASS rerun receipt at a **new** path, row unchanged | probe4 `37a2ec9 --base 0d84971` | `:1419 … DISAGREE`; exit 1 | `REPAIR`-as-drafted would pass while the row still lies |
| **F** sanctioned re-stamp | B + PASS block appended below a marker in the **cited** receipt | probe4 `f9f9a34 --base 0d84971` | `:1419 … AGREE`, `PASS graded=1 findings=0`; exit 0 | the legal repair path works |

Probe sources: `/tmp/CritMistakeFix/verdict-agree-probe3.py` (full-file scope) and `verdict-agree-probe4.py` (scoped). Both stdlib-only, read-only, `git show` only.

## 7. Impacted axes and what this does not touch

- **calibration (Ca):** the claim gains one leg and a truthful tally token. Nothing else.
- **coverage (C):** untouched — `VERDICTAGREE` reads `SCORECARD.md` and `reports/**`, neither of which C lands, so Ca's `SEPARABLE` leg still holds (C lands `corpus/knowledge/**`, `corpus/SOURCES.md`, `corpus/lessons/round-73.md`).
- **quality / discernment:** untouched. This is a record repair (QUALITY 20: record repairs are calibration, never quality/discernment observables).
- **freshness:** untouched (paused under the open round-11 L0 ruling).
- **operability:** no new gate and no new `SKILL.md` registry row — the leg lives inside `accept-ca-73.py`, whose registry row is R3's work.

## 8. Residual limits of the proposed leg (stated, not hidden)

1. **Correction-row settlement is shape-based** (both words present, last word = observed). A row that appends `FAIL` to itself inside an `## Axes` section could settle itself; closing that needs a rule that settlement rows must not be the graded row's section — deferred, because the existing correction rows (`SCORECARD.md:1147`, `:1293`) live inside axes sections and would be excluded by the stricter rule.
2. **A row citing a PASS receipt that is not the lands run** is out of this leg's scope (that is QUALITY 19/`STAMP` territory). The leg prints `graded=<n>` so a shrinking denominator is visible.
3. **Rows whose cited receipt carries no terminal `ACCEPT-*` line** are skipped, not failed; the graded count exposes it.
4. **Historical rows outside the scope** (rows added before `base`) are graded only when a ledger pair names them. That is deliberate: the scoping measurement above shows full-file scope would freeze every future round red on `SCORECARD.md:1134`-class history.

## 9. What I did not do

No edit to `claims.json` or any lane file; no counter written into `reports/round-73/`; no `git` write in the lane (all lane access was `git show`/`grep`/`read`); no fleet write; no network fetch; no tool install; no subagent.
