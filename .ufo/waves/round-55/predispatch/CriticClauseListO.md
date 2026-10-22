# CriticClauseListO — QUALITY criterion 11 non-author check of claim O (round 55, pre-dispatch)

Seat: `KotodamaR55.CriticClauseListO`. I authored none of the files checked. I checked the declaration at `662239d2`, with claim base `d44309a1`. All runs were in a scratch clone (`/fast/scratch/hyaku/kotodama-r55/CriticClauseListO/lane`) and a `git archive` copy (`…/tcopy`). I wrote nothing in the lane except this file. Installs: none.

## Verdict: DEFECTS

The S-id sets are right. The four copies (the statement, `accept-o.py`, the control builder, and the closure §5 items 1–2) agree exactly, and I re-derived them from `corpus/lessons/round-54.md`. The receipt replays byte-identically: 8/8, the same instrument sha256s, only the `tree` line differs.

The legs and controls are not able to fail on several of the statement's words:

- five weakened `accept-o.py` legs still pass all 8 controls;
- five tool stand-ins that break the statement's meaning make `accept-o.py` exit 0;
- one tool exit status is never read;
- the `kind` text and the first sentence carry two provenance mismatches.

## Re-derivation (criterion 11 item 2)

**Truncated grounds.** The closure's rule `grep -cE '[a-z,;] ?\. Seat:'`, run over the `## Gate` lines (46 rows), gives exactly the 17 rows in `TRUNC_WANT`. An independent reading, "Grounds text has no terminal period", gives the same 17. Every one of the other 29 rows ends its Grounds with `.`, so those rows read `.. Seat:`.

Two stricter readings disagree with the closure:

| reading | rows it gives | disagrees on |
|---|---|---|
| closure prose "end their Grounds **mid-word**" (`round-54-verifier-spotcheck.md:77`) | 9: S242 `mater`, S244 `depe`, S250 `li`, S251 `ensembl`, S253 `st`, S259 `bus`, S263 `personi`, S277 `collec`, S278 `d` | 8 rows cut after a whole word: S241 `and a`, S248 `carries the`, S255 `and the`, S264 `a public`, S265 `societies, a`, S275 `wearable ␠`, S276 `named ␠`, S279 `idiom ␠`. The closure's own example, S241, is not mid-word. |
| length cap (Grounds = 220 chars) | 15 | S263 and S279 are 218 chars (218 bytes), so a cap rule misses them |

The leg follows the closure's regex, and the statement does not say "mid-word", so the leg is consistent. The wording of the routing source is looser than its rule.

**Doubled locator.** Three faithful readings give exactly the 13 rows in `DOUBLED_WANT`:

- a `'X'` span repeated as `"X"`;
- the first `"…"` text occurring earlier in the locator;
- the first span inside the pre-quote locator.

The naive reading, "≥2 straight spans before `Grounds:`", gives 14, adding **S273** (`round-54.md:63`). S273 is not doubled: its escaped `\"mask of Agamemnon\"` splits one quote into two spans.

A strict "section name" reading disagrees on **S259** and **S262**. In those two rows the repeated span is a paragraph incipit (`paragraph beginning 'I did not know of firam'`, `paragraph 2 (beginning 'My focus on the carved headpiece')`), not a section name. The closure's list includes both, and so does the leg.

## Findings

### 1. `accept-o.py` never reads the round-53 run's exit status (criterion 11: "reads the exit status of every tool it runs")

Evidence: `accept-o.py:73` runs `r53`. Only `r53.stdout` is used, at `:82`. `r54` and `adv` are read at `:89` and `st` at `:92`. The docstring at `:27` says "Every tool's exit status is read directly".

Counterexample (stand-in `r53-exit2` in `tcopy`): the round-53 run prints the same 12 `words=` lines, then a `GATE_QUOTES_ERROR`, and exits 2. All seven legs PASS and `accept-o.py` exits 0.

Fix: KEEP53 becomes `kept == base53 and r53.returncode == 1`, with the detail `exit={r53.returncode}`. Statement wording: "KEEP53 (the round-53 run exits 1 and its words=<n> finding lines equal reports/round-55/base-gate-r53.txt)". Add the control RED-KEEP53-EXIT: same stdout, exit 2.

### 2. EXIT cannot tell "findings" from a crash, and lines the checker cannot parse pass NOFALSE and ESCAPE without being checked

Evidence: Python exits 1 on an uncaught exception. `FINDING` (`:47`) silently drops any line whose detail is not one token, or whose line field is not one integer (for example `adversarial.md:5-6`, which is the hard-wrap row's natural locator). Nothing checks the summary line or stderr.

Counterexamples, all `accept-o.py` exit 0:

- `crash`: the round-54 findings print, then a traceback. EXIT PASS `round54=1`.
- `s903-unparsed`: the fixture run also prints `adversarial.md:8 S903 words=28 hyphen-split`. ESCAPE PASS, although the statement says S903 stays unreported.
- `stray-unparsed`: the round-54 run also prints `round-54.md:63 S273 doubled-locator spans=2`. NOFALSE PASS.

Fix: one helper, used by every non-selftest run:

```python
def parsed(result):
    lines = result.stdout.splitlines()
    rows = [FINDING.match(l) for l in lines[:-1]]
    ok = (not result.stderr and bool(lines) and all(rows)
          and lines[-1] == f"GATE_QUOTES: {len(rows)} findings")
    return ok, [m.groups() for m in rows if m]
```

EXIT then also requires `ok` for the round-54, fixture and round-53 runs. Statement wording: "EXIT (the round-54, adversarial-fixture and round-53 runs each exit 1, write nothing to stderr, and print only finding lines and a matching `GATE_QUOTES: <n> findings` summary)". Add the controls RED-EXIT-CRASH (findings, then a traceback) and RED-EXIT-SHAPE (one two-token detail).

### 3. Each "exactly" leg has a red control in only one direction, so a weakened leg survives all 8 controls

Criterion 11 asks for "a red per mechanical clause … nearest near-miss". "Exactly [list]" can fail two ways: a row missing or a row extra. Each red tests only one of them.

Evidence: I committed each mutant in the scratch clone and ran the unchanged builder. Every one reports `CONTROLS 8/8 as expected`:

| mutant of `accept-o.py` | direction no control tests |
|---|---|
| DOUBLED `DOUBLED_WANT <= doubled` | extra row inside the union (for example S264, truncated-only, gaining `doubled-locator`; NOFALSE cannot see it) |
| TRUNC `trunc <= TRUNC_WANT` | missing row |
| ESCAPE `"S903" not in esc` | missing escape shape |
| EXIT `r54.returncode == 1` | the adversarial-run half of "each exit 1" |
| KEEP53 `len(kept) == len(base53)` | a changed line at the same count |

Fix: replace or add controls in `criterion11-controls-o.py`. Each changes one clause alone, and every other leg passes.

- **RED-DOUBLED-MISS**: drop **S262**, not S277. S262's `"…"): "…"` form is the hardest of the 13 shapes for a rule.
- **RED-DOUBLED-EXTRA**: **S264**, a truncated-only row, gains `doubled-locator`.
- **RED-TRUNC-MISS**: drop **S279**. It has 218 chars and a space before the period, the hardest of the 17. Keep the existing RED-TRUNC (S239 extra) as RED-TRUNC-EXTRA. S239's `owed..` ending is a good near-miss.
- **RED-ESCAPE-MISS**: S904 unreported. Its spans already join into one 22-word run, and only the new inter-span ellipsis rule flags it. Keep RED-ESCAPE (S903 extra) as RED-ESCAPE-EXTRA.
- **RED-EXIT-ADV**: the fixture run exits 0 with the same findings.
- **RED-KEEP53**: replace the count-changing drop (an easy break of the kind criterion 11 rules out) with a count-preserving one. S236 `words=29` becomes `words=30`, still 12 lines. Change the KEEP53 detail to print the first differing line, so the receipt shows why the leg fails.
- **RED-NOFALSE** (better near-miss, optional): use **S273** gaining a `words=` finding instead of S245. S273 is the only clean row whose straight quotes parse as two spans, so a widened quote regex would plausibly produce exactly this finding.

The builder's `len(legs) == 7` must follow any leg change.

### 4. ESCAPE checks "an S-id has some finding", not "the escape shape is reported"

Evidence: `accept-o.py:81` collects S-ids of any class. The statement's first sentence claims the tool "reports … four of the five carried escape shapes". Counterexample `s904-wrong-class`: S904 is reported only as `doubled-locator`, as a naive two-span doubled rule would report it, and the inter-span ellipsis escape is not handled. ESCAPE PASS, exit 0.

Fix: pin the finding detail per row. The documented whitespace word rule determines it: S901 26, S902 26, S904 8+14 = 22, S905 26.

```python
ESCAPE_WANT = {("S901", "words=26"), ("S902", "words=26"), ("S904", "words=22"), ("S905", "words=26")}
esc = {(s, d) for _, _, s, d in findings(adv)}
```

Statement wording: "ESCAPE (on reports/round-55/fixtures/adversarial.md the findings are exactly S901 words=26, S902 words=26, S904 words=22, S905 words=26)". The new RED-ESCAPE-MISS control covers it.

### 5. False provenance in the `kind` field and the first sentence

Evidence:

- **Escape count.** `claims.json` O `kind` says "repairs … the five carried escape classes". The statement says "four of the five", and ESCAPE requires S903 unreported.
- **Who routed what.** The first sentence says the checker reports "the two Gate-line shapes the round-54 closure **routed**". The closure routed defect 1's fix as errata ("File full grounds as errata", `round-54-verifier-spotcheck.md:77`). Only defect 2 was routed to the checker ("Add it as an escape class, or make the checker fail on it", `:78`).

Fix:

- `kind`: "…; turns the round-54 closure's routed defects 1 and 2 into checks (defect 1's errata filing stays a records item) and repairs four of the five carried escape classes".
- First sentence: "…reports the two Gate-line shapes the round-54 closure named in routed defects 1 and 2…".

### 6. The S905 shape is described differently from the fixture bytes (wording only)

Evidence: `fixtures/adversarial.md:10` is `- * S905 — …`. That sha matches the round-54 original `/fast/scratch/hyaku/kotodama-r54-a2/ReviewGateQuoteTool/adversarial.md`, so "copied unchanged" holds. But `accept-o.py:21` calls it a "`* ` bullet". The round-54 review's suggested fix, `^[-*+]\s+`, does **not** match `- * S905`, so an implementer who follows that fix fails ESCAPE.

Fix (docstring and lesson wording; keep the fixture as it is): "S905 (a `- ` row whose first token is `*`, fixture line 10; `^[-*+]\s+` alone does not reach it)". Also, the `accept-o.py` docstring's review-only list (`:28-30`) leaves out the claims.json item "the selftest carries a red and a green case for each new class". Add it so the two lists agree.

### 7. Inputs not pinned at acceptance time (low priority)

Evidence: `records_not_claims` allows edits to "reports/round-55/* other than lands", which covers the fixture, `base-gate-r53.txt` and `accept-o.py` itself. KEEP53 and ESCAPE depend on those bytes. Only the receipt's sha256 lines (`criterion11-controls-o.txt:2-6`) pin them, and only a closure that compares them will notice a change.

Fix: `accept-o.py` checks the sha256 of FIX (`e31e602f…`) and BASE53 (`77fd00fb…`) and exits 2 on a mismatch.

## Items checked that hold

- **Clause list (criterion 11 item 1).** Each of the seven parenthesised leg phrases maps to one clause and one leg. "exits 0, with its seven legs passing" is the counting command itself. The three review-only items are honestly unmechanical. The only phrases without a faithful leg are the first sentence's "reports … shapes" (findings 4–5) and the halves listed in finding 3.
- **Controls (criterion 11 item 3).** Every red in the receipt fails its own leg alone, and every other leg passes (`criterion11-controls-o.txt:27-88`).
- **GREEN stand-in honesty (criterion 11 item 4).** The stand-in exists only in a copy, carries a "never landed" header, and keeps the base tool beside it as `check-gate-quotes-base.py`. It hands the round-53 run and `--selftest` to the real base tool, so KEEP53 and SELFTEST in GREEN are real base runs. The stand-in's `:1` line numbers and its S904 `words=26` are cosmetic: no leg reads them.
- **Vacuity at the landed tip.** KEEP53 does not pass vacuously if the `words=` format changes: `base53` holds 12 lines, so `kept=[]` FAILs. Its hole is the exit status (finding 1). ESCAPE does not pass vacuously if S903 starts being counted with hyphen splitting: S903 becomes reported and ESCAPE FAILs, as the statement intends. Its holes are the class (finding 4) and lines it cannot parse (finding 2).
- **No conflict with base findings.** I checked mechanically that the round-53 and round-54 Gate sections contain none of the four escape shapes: no guillemets, no `*`/`+` row markers, no continuation lines, no ellipsis between spans, and no odd counts of straight quotes. So the escape fixes cannot add findings that would trip KEEP53 or NOFALSE.

## Unrun checks

- I did not run the builder with my proposed controls, or `accept-o.py` with my proposed helpers. The code above is untested.
- I did not test the `words=` findings rule on rounds 51–52 (KEEP53 covers round 53 only, as the statement does).
- I did not open any web source (out of scope).
- I did not compare against the declaration dry-run receipt beyond confirming that its O lines (`declaration-dry-run.txt:22,31-32,41`) name the declared argv.
