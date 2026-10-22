# CriticCClaimSizing — round 53 falsify, claim C statement against its commands

Seat: `KotodamaR53.CriticCClaimSizing` (critic, leaf, non-author of C). Item attacked: claim C's `statement` in `reports/round-53/claims.json`, measured at C's landing commit `47ec825f11543b5ba457e21772d587b3f529e756` against claim base `a9cf95fe47a82b516f6c2487cb76b89c3a71c493`.

Method: `git archive` exports of the base (`base/`), D's landing `374ae5a` (`d/`) and C's landing (`land/`) in the private sandbox `/fast/scratch/hyaku/kotodama-r53/falsify/CriticCClaimSizing`. `reports/round-53/clauses.py` is not in any commit, so it was copied from the lane worktree (sha256 `3d373e41f59a7cfb816f1faa3fed2b2678f30a394a8326504124d4e5a8687042`) and run from the sandbox. Three mutants were built in the sandbox from `land/` by one throwaway script (`mut.py`, sandbox only). The only file written in the lane is this report. Tool installs: none.

## 0. Result

- At `47ec825`, every clause of C's statement is true. Each one re-derives with one plain command over committed bytes (section 2).
- **The declared commands are still narrower than the statement.** The counting command (`find corpus/knowledge -name '*.md' | wc -l`) and `accept-c.py` together check five of the seven clauses. They do not check "one new entry" or the topic clause. A scratch tree where either clause is false still gives `accept-c.py` exit 0 (mutants `swap` and `topic-off`).
- `clauses.py` closes "one new entry" (C1). It closes the topic clause only in part: C2 tests the words `gesture` and `pointing` and nothing else, so the `topic-thin` mutant passes C2. It is also not a committed or declared command.
- **Drift guard:** yes. Round 53's C statement is wider than its counting command, and also wider than counting plus acceptance. This is the same class as round 51 (D) and round 52 (C), so it is the third consecutive round. `corpus/lessons/round-52-verifier-spotcheck.md:57` says "A third trips the drift sentinel."

## 1. Clause map: which command checks each clause

| # | clause of C's statement | declared command that checks it | other check | at `47ec825` |
|---|---|---|---|---|
| 1 | "Knowledge files go from 228" | counting command at base (receipt `reports/round-53/telemetry/declaration-dry-run.txt`: `find corpus/knowledge -name '*.md' \| wc -l` → `228`) | — | 228 ✔ |
| 2 | "to 229" / "the count is 229" | counting command, and `accept-c.py` COUNT (`os.walk`, `.md`) | — | 229 ✔ |
| 3 | "one new entry, corpus/knowledge/linguistics/gesture-co-speech-pointing.md" | **none.** ENTRY only checks that the path exists, and COUNT only checks the total. | `clauses.py` C1 (uncommitted record) | ✔ |
| 4 | "on co-speech gesture, pointing and quotable gestures as conlang and worldbuilding method" | **none** | `clauses.py` C2 checks only `gesture` and `pointing` in the `- topic:` line | ✔ |
| 5 | "reports/round-53/accept-c.py exits 0" | `accept-c.py` | — | exit 0 ✔ |
| 6 | "the README sweep run on its own exits 0 with rows 229 files 229 and missing_from_index 0" | `accept-c.py` SWEEP (reads the sweep's own return code, line-anchored regexes) | — | ✔ |
| 7 | "every S-id the entry cites is S187 or above and is a mined corpus/SOURCES.md row whose used-by cell names the entry" | `accept-c.py` SIDS | — | cited 52, bad [] ✔ |

### Outputs at the landing commit

```
$ (cd land && find corpus/knowledge -name '*.md' | wc -l)        # base/ gives 228, d/ gives 228
229
$ (cd land && python3 -B reports/round-53/accept-c.py); echo exit=$?
COUNT PASS knowledge_files=229 required=229
ENTRY PASS corpus/knowledge/linguistics/gesture-co-speech-pointing.md
SWEEP PASS exit=0 rows 229 files 229 missing_from_index 0 []
SIDS PASS cited=52 bad=[]
exit=0
$ (cd land && python3 -B reports/round-28/readme/sweep.py); echo exit=$?
rows 229 files 229
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
totals_line 229 totals_ok True
footer_findings [] footer_ok True
exit=0                                   # (parts/footer/sha lines omitted)
$ (cd land && python3 -B ../clauses.py --base-tree ../base); echo exit=$?
C1 PASS added=['corpus/knowledge/linguistics/gesture-co-speech-pointing.md'] removed=[]
C2 PASS topic_chars=375
C3 PASS draft_tokens=[]
D1 PASS lines=196 base=196
D2 PASS lost=[]
exit=0
```

`accept-c.py` run in the lane worktree prints the same four PASS lines and exits 0. The sweep resolves its lane from its own `__file__` (`reports/round-28/readme/sweep.py:44-45`), so the sandbox runs measured the export, not the lane.

## 2. Can the closure re-derive the unchecked clauses with one plain command over committed bytes? Yes

```
$ git diff --name-status --no-renames --diff-filter=AD a9cf95f 47ec825 -- corpus/knowledge
A	corpus/knowledge/linguistics/gesture-co-speech-pointing.md
$ git show 47ec825:corpus/knowledge/linguistics/gesture-co-speech-pointing.md | grep -c '^- topic: co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method'
1
$ for c in a9cf95f 47ec825; do git ls-tree -r --name-only $c -- corpus/knowledge | grep -c '\.md$'; done
228
229
```

- Clause 3: there is exactly one added path, the named entry, and no deleted knowledge file. Without `--diff-filter` the diff also lists `M speech-surrogates-whistled-drummed.md`, which is D's repair and not a new entry.
- Clause 4: the topic line opens with the statement's phrase word for word. The only difference is the article "a" ("as a conlang and worldbuilding method").
- Clause 1 also re-derives from committed bytes without the receipt.

I also checked clause 7 against the holes the build-wave critic found (`.ufo/waves/round-53/build/CriticClaimSizingC.md` §2) at `git show 47ec825:corpus/SOURCES.md`:

- There are 52 rows from S187 to S238. No S-id has two rows, so the "last row wins" dictionary hole cannot hide anything here.
- Every one of the 52 rows is `mined`, and its used-by cell holds the entry path as an exact comma-separated item, not just a substring.
- No row below S187 names the entry.
- The entry cites exactly the 52 unique ids S187 to S238.
- The entry contains no zero-padded, short or range-form S tokens (`\bS\d{1,2}\b|\bS\d{4,}\b|S\d{3}[–-]S?\d{3}` gives 0 matches).

So none of SIDS's known holes is used at the landing commit.

## 3. Findings

### F1 — high (a gate that passes a false claim): the declared commands pass trees where clauses 3 or 4 are false

Counterexample, run on scratch copies of `land/`:

| mutant | change | `accept-c.py` | `clauses.py` | plain command (section 2) |
|---|---|---|---|---|
| `swap` | `linguistics/numerals-and-measures.md` renamed to `linguistics/zz-numerals.md`, with its README row renamed to match (so two new knowledge paths, one removed) | **exit 0**, all four PASS | `C1 FAIL added=[...gesture-co-speech-pointing.md, ...zz-numerals.md] removed=[...numerals-and-measures.md]`, exit 1 | set diff shows `> zz-numerals.md`, `< numerals-and-measures.md` |
| `topic-off` | entry topic and its README row topic both set to `hand-made pottery` | **exit 0**, all four PASS | `C2 FAIL topic_chars=26`, exit 1 | topic grep → 0 |

In both trees the statement is false, but the declared counting and acceptance commands pass. The landed bytes are not affected (section 2): this is a sizing defect in the declaration, not a false landed claim.

- Impacted axes: coverage (C's admission evidence), and operability of the drift guard.
- `reports/round-53/final-measures.py` controls C-red-4 and C-red-5 (lines 147-156) run only `clauses.py`. Both leave the README untouched, so `accept-c.py` would fail them on SWEEP anyway. They do not show what `swap` shows: a tree that passes every declared command while one clause is false.
- Smallest safe correction: the declaration is frozen and must not be narrowed. The closure should rule clauses 3 and 4 from the two plain commands in section 2, and record that the declared commands check neither clause. Paste-ready text for the closure or the lesson:

  > C's declared commands check five of the statement's seven clauses. "One new entry" and the topic clause are checked by no declared command: a scratch tree with a second added file and one removed (README rows matching), or with the topic set to an unrelated phrase in both the entry and the README, still gives `accept-c.py` exit 0. Both clauses re-derive at `47ec825` with `git diff --name-status --no-renames --diff-filter=AD a9cf95f 47ec825 -- corpus/knowledge` (one line, `A` the entry) and `git show 47ec825:corpus/knowledge/linguistics/gesture-co-speech-pointing.md | grep -c '^- topic: co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method'` (1).

### F2 — medium (mis-cited check): `clauses.py` is neither committed nor declared

- `git ls-files --error-unmatch reports/round-53/clauses.py` gives `did not match any file(s) known to git`.
- `git ls-tree -r --name-only 47ec825 -- reports/round-53/` lists `accept-c.py`, `claims-agree.py`, `claims.json`, `d-count.py`, `dry-run.py`, `separability-manifest.json` and two telemetry files. It does not list `clauses.py` or `final-measures.py`.
- `clauses.py` is not in `claims.json` and not in the dry-run receipt.

Even so, `corpus/lessons/round-53.md:20` (uncommitted) says "`reports/round-53/clauses.py` checks them and the final receipt shows each can fail". As things stand, a closure working "over committed bytes" cannot run it.

Fix: land `clauses.py` (and `final-measures.py`) as records, under `records_not_claims` "reports/round-53/* other than lands", in the records commit before the closure. Cite it by commit hash, and keep the section 2 plain commands as the closure's primary re-derivation.

### F3 — medium (imprecise check): C2 is narrower than clause 4

Counterexample: mutant `topic-thin` sets the topic, in both the entry and its README row, to `gesture pointing`.

```
accept-c.py: COUNT PASS / ENTRY PASS / SWEEP PASS / SIDS PASS, exit 0
clauses.py:  C1 PASS ... C2 PASS topic_chars=25 ... exit 0
topic grep:  0, exit 1
```

C2 passes a topic that drops "quotable gestures" and "conlang and worldbuilding method". So the lesson's "checks them" (line 20) overstates C2.

Fix (paste-ready, `reports/round-53/clauses.py`, C2 leg):

```python
        phrase = "- topic: co-speech gesture, pointing and quotable gestures as a conlang and worldbuilding method"
        legs.append(("C2", topic.startswith(phrase), f"topic_chars={len(topic)}"))
```

Also change the docstring's C2 line to: `C2  "on co-speech gesture, pointing and quotable gestures as conlang and worldbuilding method": the entry's '- topic:' line opens with that phrase`.

C-red-5 (`hand-made pottery`) still fails under this fix, so no test is weakened. Whether the body actually carries that topic remains a review question for the section reviewers.

### F4 — high per the drift guard: the claim-sizing class appears for the third consecutive round

The class is "a statement wider than its own measure":

- Round 51: D's `path:line` clause was checked by a counter that accepts a directory token (`corpus/lessons/round-51-verifier-spotcheck.md:44-49`).
- Round 52: C's "indexed in corpus/README.md" clause was checked by a piped `grep` that could not fail (R52-M3, `corpus/lessons/round-52-verifier-spotcheck.md:53-57`). Round 52's C statement also carried the same unchecked "one new entry ... on speech surrogates" clauses (`reports/round-52/claims.json`).
- Round 53: C's statement is wider than its counting command, and still wider than counting plus acceptance, by clauses 3 and 4 (F1).

Round 53 did close the R52-M3 hole. `accept-c.py` reads the sweep's own exit code, and the build critic's README-row-removed mutant fails SWEEP. But the class itself has recurred. The `red_before_rule` guard only proves that each declared command can go red on a falsified copy. It cannot detect a clause that no declared command reads.

- Is the C statement wider than its counting command? **Yes, exactly by clauses 1 and 3 to 7.** The counting command prints a single number.
- Is it wider than its declared commands combined? **Yes, by clauses 3 and 4 only.**

This is a fixable sizing defect that the closure can re-derive (section 2), not a false landed claim. It matches the condition `round-52-verifier-spotcheck.md:57` names for tripping the drift sentinel. The closure must record the trip and not rule it a non-recurrence.

Fix: in the closure and the SCORECARD, state "claim-sizing class, third consecutive round (51 D, 52 C, 53 C); drift sentinel tripped". Uncommitted QUALITY criterion 11 already asks that "Every clause names the command that checks it". From round 54, the dry-run receipt should list each statement clause next to its declared command, so that a clause mapped to no command fails at declaration and is not found after landing.

### F5 — low (wording, outside sizing, for the head reviewer): leftover seat-draft wording in the entry head

`corpus/knowledge/linguistics/gesture-co-speech-pointing.md` (at `47ec825`):

- The sources field says "the integrator assigns the row ids at integration and every id the entry then cites is at or above the round-53 floor."
- The verified-at field says "Not claimed: … the assigned `S###` ids, and any gate run against the landed entry are not claimed here — this seat measured only the pre-entry state".

Both describe the build seat's draft, not the landed entry, which cites 52 assigned ids and passes `accept-c.py`. No gate reads these fields, so they do not change any clause above.

Fix: replace the first sentence with "the rows are S187-S238, each registered in `corpus/SOURCES.md` with the entry in its used-by cell". Replace the Not-claimed sentence with "post-entry: `find corpus/knowledge -name '*.md' | wc -l` → 229; `python3 -B reports/round-53/accept-c.py` exit 0 at `47ec825`". Route to `KotodamaR53.ReviewCHead`.

## 4. No defect found (checked)

- COUNT (`os.walk`) and the declared `find | wc -l` agree at base (228), at D's landing (228) and at C's landing (229).
- SWEEP reads the sweep's own exit code. At `47ec825`, `topic_mismatch`, `orphan_rows` and `footer_findings` are empty.
- SIDS: all of the section 2 hole checks are clean at `47ec825`.
- Clause 1 (228 at base) is in the committed receipt and re-derives with `git ls-tree`.
