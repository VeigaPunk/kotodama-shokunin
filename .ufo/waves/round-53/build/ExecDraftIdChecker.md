# ExecDraftIdChecker — round 53

**Seat:** `KotodamaR53.ExecDraftIdChecker` (executor, leaf).
**Assigned item:** build the mistake-fix tool — a draft-id fragment checker — as
`tools/check-draft-ids.py`, stdlib only, in the style of
`tools/check-source-access.py` (module docstring with usage and exit codes).
**Round:** 53, attempt 1 (hyaku phase 3, 2026-10-22).
**Lane repo:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
**Sandbox clone:** `/fast/scratch/hyaku/kotodama-r53/ExecDraftIdChecker`
(`git clone -q --shared` of the lane), checked out at the declaration
`60f1d2a3d832b926e37f82b11c67496d131a1431`.

**File locations.** The tool is in the sandbox clone at
`/fast/scratch/hyaku/kotodama-r53/ExecDraftIdChecker/tools/check-draft-ids.py`
**and** in the lane at `tools/check-draft-ids.py` (the L1 copied the first
version in during this seat's run; this seat then updated the lane copy with
the path-resolution fix, section 6). sha256 of both, after the fix:

```
423a37b1b0ce232d2eb853c91c252cae4845795539217847bc6040b3811d6a60  tools/check-draft-ids.py   (superseded, before the docstring sync)
f49679b6a4174714b38a471084c91a6b9a949650d66c4fd7590469abba683fb4  tools/check-draft-ids.py   (final)
f49679b6a4174714b38a471084c91a6b9a949650d66c4fd7590469abba683fb4  <sandbox>/tools/check-draft-ids.py
```

The lane copy is **untracked**; the L1 owns committing it and its receipt.

---

## 1. What the tool is for (the mined mistake)

Round 52's integration left **unresolved draft-id fragments** in
`corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`: the
seat draft ids were never mapped to registry rows, so the text kept bare
`-N` fragments such as `(S159, -6)`. The fragments read like citations but
name no source, so the entry cites nothing on that claim, and every gate that
counts cited rows is blind to the gap. The round-52 closure routed the repair
(`corpus/lessons/round-52-verifier-spotcheck.md:130-136`: "Replace all 11 `, -N`
draft-id fragments with S-ids, and teach the provenance gate to flag them").

This tool is the "teach the gate to flag them" half. It scans Markdown corpus
entries for the three fragment shapes and prints one finding per token.

## 2. Detection rules and why each predicate is what it is

Three disjoint forms are reported:

| Rule | Shape | Where it may appear |
|---|---|---|
| **F1** | `NEW-<SeatName>-<n>` | anywhere in the file |
| **F2** | `, -N` or `; -N` | inside a *citation parenthesis* — a parenthesis whose text contains at least one standalone registry id `S###` |
| **F3** | `-N` glued to a registry id, no separator (`(S157-2)`) | inside a parenthesis |

F2 and F3 are disjoint by construction: a fragment preceded by a comma or
semicolon is F2; a fragment glued to the id is F3.

Three predicates keep the tool from firing on text that only looks like a
fragment. Each is a control in the selftest.

1. **A registry id is one that stands alone.** `S0718-68942020000100013` is a
   SciELO article pid; `S0271-5309` is a DOI stem. An id glued to a URL
   character (`=`, `/`, `.`) or a DOI stem (`-`) is not a registry id and does
   not make its parenthesis a citation parenthesis. F3 additionally requires a
   short fragment (at most three digits), which a DOI stem never has.
   *Without this predicate the first corpus run reported 6 false positives*
   (4 civilization files and one synthesis file); with it, 0.
2. **A fragment must be a list element of the citation.** After it comes `,`,
   `;`, `)`, `]`, `}` or end of line. `-40 °C` inside a citation parenthesis is
   a temperature, not a draft id.
3. **A non-registry id does not open a citation parenthesis.**
   `(KTD-AR-S-0005, -0006, -0007)` is a dated-record id series, and
   `DR-FUR-01, -02, -06 and -08` is not parenthesised at all. Both are
   reported by a naive "any `, -N`" rule and neither is a draft-id fragment.
   These two near-misses were measured by `KotodamaR53.ScribeMistake` on
   2026-10-22 and are covered as negatives here.

## 3. Interface

```
python3 -B tools/check-draft-ids.py [--root LANE_ROOT] [PATH ...]
python3 -B tools/check-draft-ids.py --selftest
```

With no `PATH` the tool scans every `*.md` under `<root>/corpus/knowledge/`.
A `PATH` may be a Markdown file or a directory (scanned recursively). **A
relative `PATH` is resolved against `--root`**, not against the process working
directory (see section 6 — this was a bug in the first version).

Output: one line per finding, then the total.

```
DRAFT_ID <path>:<line> '<token>'
DRAFT_IDS: <n> findings
```

The token is the matched text as it appears in the file: `, -6` for an F2
fragment, `-2` for an F3 fragment, `NEW-Seat-1` for an F1 token.

Exit codes: **0** no findings; **1** findings; **2** could not evaluate
(stderr `DRAFT_ID_INPUT_ERROR`). Read-only, stdlib only (`argparse`, `os`,
`re`, `sys`, `tempfile`).

## 4. Selftest — 25 text controls + 5 filesystem controls, all pass

`python3 -B tools/check-draft-ids.py --selftest`

```
PASS clean want=0 got=0 []
PASS F1-new-token want=1 got=1 [1:NEW-ExecDraftIdChecker-1]
PASS F1-new-token-in-paren want=1 got=1 [1:NEW-ScribeSec08-12]
PASS F1-hyphenated-seat-name want=1 got=1 [1:NEW-KotodamaR53-Scribe-3]
PASS F2-comma-fragment want=1 got=1 [1:, -6]
PASS F2-semicolon-fragment want=1 got=1 [1:; -2]
PASS F2-three-fragments want=3 got=3 [1:, -5, 1:, -6, 1:, -7]
PASS F3-adjacent-fragment want=1 got=1 [1:-2]
PASS spec-example-S157 want=1 got=1 [1:, -2]
PASS spec-example-S179 want=2 got=2 [1:, -5, 1:, -6]
PASS neg-page-range want=0 got=0 []
PASS neg-id-range want=0 got=0 []
PASS neg-id-range-ascii want=0 got=0 []
PASS neg-negative-number want=0 got=0 []
PASS neg-negative-number-in-citation want=0 got=0 []
PASS neg-line-range want=0 got=0 []
PASS neg-table-separator want=0 got=0 []
PASS neg-hyphenated-word want=0 got=0 []
PASS neg-non-registry-paren want=0 got=0 []
PASS neg-non-registry-prose want=0 got=0 []
PASS neg-to-verify want=0 got=0 []
PASS neg-scielo-pid want=0 got=0 []
PASS neg-doi-stem want=0 got=0 []
PASS neg-doi-in-parens want=0 got=0 []
PASS mixed want=1 got=1 [1:, -6]
SELFTEST: 25/25 pass
PASS root-relative-path findings=1
PASS absolute-path findings=1
DRAFT_ID_INPUT_ERROR no such file or directory: /tmp/tmpXXXX/no/such/dir
PASS missing-path exit=2
DRAFT_IDS: 0 findings
PASS clean-tree exit=0
DRAFT_ID corpus/knowledge/p/e.md:1 ', -6'
DRAFT_IDS: 1 findings
PASS defect-tree exit=1
SELFTEST: filesystem controls PASS
```

Exit code 0. The `spec-example-S157` and `spec-example-S179` controls are the
two example shapes named in the assignment (`(S157, -2)` and `(S179, -5, -6)`)
pinned as explicit assertions. The five filesystem controls exercise the
path resolution and all three exit codes against a real temporary tree.

## 5. It can fail — run A, the round-52 tip entry

The tip export was produced exactly as the assignment specifies:

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show \
  6524184e9c55665b84884a25ec240c695cacb64e:corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md \
  > /fast/scratch/hyaku/kotodama-r53/ExecDraftIdChecker/scratch-round52-tip.md
```

Run (from `/tmp`, deliberately outside the tree being scanned, so the path
resolution is exercised rather than assumed):

```
$ cd /tmp
$ python3 -B <sandbox>/tools/check-draft-ids.py --root <sandbox> scratch-round52-tip.md
DRAFT_ID scratch-round52-tip.md:104 ', -2'
DRAFT_ID scratch-round52-tip.md:106 ', -6'
DRAFT_ID scratch-round52-tip.md:107 ', -6'
DRAFT_ID scratch-round52-tip.md:113 ', -4'
DRAFT_ID scratch-round52-tip.md:174 ', -5'
DRAFT_ID scratch-round52-tip.md:177 ', -5'
DRAFT_ID scratch-round52-tip.md:177 ', -6'
DRAFT_ID scratch-round52-tip.md:177 ', -7'
DRAFT_ID scratch-round52-tip.md:179 ', -12'
DRAFT_ID scratch-round52-tip.md:181 ', -2'
DRAFT_ID scratch-round52-tip.md:181 ', -12'
DRAFT_IDS: 11 findings
exit=1
```

**11 findings, as expected.** The 11 tokens sit on 8 lines (104, 106, 107,
113, 174, 177 ×3, 179, 181) — exactly the line set the round-52 closure
recorded at `corpus/lessons/round-52-verifier-spotcheck.md:130-136`.

Cross-check by the counter's own regex on the same file:
`grep -oE ', -[0-9]+\b' scratch-round52-tip.md | wc -l` → **11**. The tool
agrees with the counter's fragment count on this file.

## 6. Bug found and fixed in this seat's own tool — path resolution

The first version resolved a relative `PATH` against the **process working
directory** instead of `--root`. The bug surfaced when the L1 copied the tool
into the lane and the run against the base tree was issued from the lane
directory: the tool scanned the lane's `corpus/knowledge` (whose working copy
already carries the repair) while the operator asked for the base tree, and
printed `DRAFT_IDS: 0 findings` for a tree that provably still holds the
defect.

**Fix:** a new `resolve(root, target)` joins a relative path onto `--root`;
absolute paths are used as given. `display_path` now also tolerates a root on
a different drive or an unresolvable relpath. Five filesystem controls were
added to the selftest to pin the behaviour (`root-relative-path`,
`absolute-path`, `missing-path`, `clean-tree`, `defect-tree`).

**Every count in this report was re-measured after the fix**, from a working
directory outside the tree under test. The counts are unchanged: 11, 10, 10, 0.

This is worth flagging to the L1 as a general lesson rather than a tool detail:
a tool that takes `--root` and a relative path must resolve the path against
`--root`, or it silently scans the wrong tree. The reference tool
`tools/check-source-access.py` has no path argument, so it never had to
decide this; `--sources` there is likewise resolved against `--root`
(`sources = args.sources or os.path.join(args.root, "corpus/SOURCES.md")`),
which is the convention this tool now follows.

## 7. Run B and run C — the base tree and the declaration tree

Both trees were extracted read-only so the run is against committed content,
not a working copy:

```
git -C <lane> archive a9cf95fe47a82b516f6c2487cb76b89c3a71c493 corpus/knowledge | tar -x -C /tmp/base-tree
git -C <lane> archive 60f1d2a3d832b926e37f82b11c67496d131a1431 corpus/knowledge | tar -x -C /tmp/decl-tree
```

228 Markdown files in each. Runs from `/tmp`:

```
$ python3 -B <sandbox>/tools/check-draft-ids.py --root /tmp/base-tree corpus/knowledge
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:106 ', -6'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:107 ', -6'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:113 ', -4'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:174 ', -5'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:177 ', -5'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:177 ', -6'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:177 ', -7'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:179 ', -12'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:181 ', -2'
DRAFT_ID corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:181 ', -12'
DRAFT_IDS: 10 findings
exit=1
```

The declaration tree `60f1d2a` prints **the same 10 findings** — and
`diff -r /tmp/base-tree/corpus/knowledge /tmp/decl-tree/corpus/knowledge` is
empty, so the two trees agree in `corpus/knowledge`, as expected.

**All 10 findings are in the speech-surrogates entry. No other file in
`corpus/knowledge` produces a finding.** The 10th token is the one the
round-53 prerequisite already repaired: the tip's line 104 `(S157, -2)` was
re-cited to S184 by commit `9ae5af9`, so the base and declaration trees have
10, not 11.

Two runs in the same tree, same file:

```
$ diff <(git show 6524184e:corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md) \
       corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
104c104
< | Mountain, ravine and dense-forest terrain | Silbo Gomero, La Gomera (inscribed 2009): a range of "up to five kilometres" with hamlets in the ravines (S157, -2); ...
---
> | Mountain, ravine and dense-forest terrain | Silbo Gomero, La Gomera (inscribed 2009): messages carried "over a distance of up to five kilometres" on an island cut by "a network of very deep ravines" ...
```

The single changed line is exactly the line the prerequisite repaired, and it
is exactly the difference between 11 and 10 findings.

**Other corpus-tree forms, measured (all 0 findings):** zero `NEW-` tokens
anywhere under `corpus/knowledge`; the two near-misses at
`corpus/knowledge/culture-material/furniture-interior-lexicon.md:137` and
`corpus/knowledge/verification/append-only-record-verification.md:73` are not
flagged.

## 8. The lane copy, and the current lane worktree

The lane copy at `tools/check-draft-ids.py` (sha256
`f49679b6a4174714b38a471084c91a6b9a949650d66c4fd7590469abba683fb4`) was run
directly in the lane:

```
$ cd <lane>
$ python3 -B tools/check-draft-ids.py --selftest
... SELFTEST: 25/25 pass ... SELFTEST: filesystem controls PASS
exit=0

$ python3 -B tools/check-draft-ids.py --root /tmp/base-tree corpus/knowledge
DRAFT_ID ... DRAFT_IDS: 10 findings
exit=1

$ python3 -B tools/check-draft-ids.py --root /tmp /tmp/receipt-tip.md
DRAFT_ID ... DRAFT_IDS: 11 findings
exit=1

$ python3 -B tools/check-draft-ids.py
DRAFT_IDS: 0 findings
exit=0
```

The last run is against the lane working copy, whose entry already has the
fragments replaced (another seat's D-repair draft; `git diff` on that file
shows 8 insertions / 8 deletions, and line 106 now reads `(S159); ... (S162)`).
The tool agrees with that repair.

**Decoy-CWD check (the shape that used to be wrong).** A clean decoy tree was
planted at `/tmp/decoy/corpus/knowledge/decoy.md` containing only `(S159)`, and
the tool was invoked with the working directory set to that decoy:

```
$ cd /tmp/decoy
$ python3 -B tools/check-draft-ids.py --root /tmp/base-tree corpus/knowledge
DRAFT_ID ... DRAFT_IDS: 10 findings
exit=1                      # the base tree, not the decoy

$ python3 -B tools/check-draft-ids.py --root .
DRAFT_IDS: 0 findings
exit=0                      # the decoy, correctly clean
```

`--root` now governs which tree is scanned, whatever the working directory is.
Before the fix, the first of these two commands would have scanned the decoy
and printed a false green.

**The failing receipt now exists**, which was the open item in the
`ScribeMistake` report: the lane's own copy of the tool exits 1 with 11
findings on the round-52 tip export and 10 findings on the base tree. The
L1 owns committing the tool and that receipt. The receipt must be run from a
directory that is not the tree under test, so the run cannot certify the
wrong tree by accident.

## 9. The tool can also fail on its own inputs

```
$ python3 -B tools/check-draft-ids.py --root . /nonexistent/path.md
DRAFT_ID_INPUT_ERROR no such file or directory: /nonexistent/path.md
exit=2

$ python3 -B tools/check-draft-ids.py --root /tmp/empty-nonexistent-root
DRAFT_ID_INPUT_ERROR no such file or directory: /tmp/empty-nonexistent-root/corpus/knowledge
exit=2
```

## 10. Files changed

| Path | Change |
|---|---|
| `/fast/scratch/hyaku/kotodama-r53/ExecDraftIdChecker/tools/check-draft-ids.py` | **new**, the tool (sandbox clone) |
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-draft-ids.py` | the tool, copied in by the L1 mid-run and then **updated by this seat** with the path-resolution fix (section 6); still untracked |
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-53/build/ExecDraftIdChecker.md` | **new**, this report |

No other file in the lane, a sibling lane, or the fleet repo was created,
edited or deleted. The entry `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`
was **not** touched by this seat — its working-copy modification belongs to
another seat's D-repair draft. No `jj` command was run at the fleet root; no
commit, push, fetch or index operation was performed in the lane.

## 11. Evidence index

| Fact | Evidence |
|---|---|
| Rounds-52 routed defect: 11 bare `, -N` fragments, "teach the provenance gate to flag them" | `corpus/lessons/round-52-verifier-spotcheck.md:130-136` |
| Tip entry has 11 fragments on lines 104, 106, 107, 113, 174, 177, 179, 181 | `git show 6524184e:.../speech-surrogates-whistled-drummed.md` + `grep -oE ', -[0-9]+\b' \| wc -l` → 11 |
| Base and declaration trees hold 10 fragments (line 104 repaired by the prerequisite) | tool runs B and C; `diff -r` of the two trees is empty; `git show 9ae5af9` diff |
| Prerequisite re-cited line 104 to S184 | `corpus/lessons/round-52-verifier-spotcheck.md:130-136`; diff in section 7 |
| Counter's own fragment regex agrees | `reports/round-53/d-count.py` `FRAG = re.compile(r", -[0-9]+\b")` |
| Near-miss forms to not flag | `corpus/knowledge/culture-material/furniture-interior-lexicon.md:137`; `corpus/knowledge/verification/append-only-record-verification.md:73` |
| Zero `NEW-` tokens under `corpus/knowledge` | tool runs B and C (F1 never fires) |
| Lane worktree already repaired | `git diff --stat -- corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` → 8 insertions, 8 deletions |
| Path-resolution bug and fix | section 6; `root-relative-path` filesystem control |

## 12. Risks and limits

- **F3 has a three-digit ceiling** (`(-\d{1,3})`). A draft id of four or more
  digits glued to an id would not be caught. The observed fragments are `-2`,
  `-4`, `-5`, `-6`, `-7`, `-12`, so the ceiling is not binding today; it is
  what keeps DOI stems out. Raise it if the seat draft-id format grows.
- **F2 needs a standalone registry id in the same parenthesis.** A fragment in
  a parenthesis that cites no registry row (`(, -6)` on its own) is not
  reported. That is the intended reading of "citation parenthesis", but it
  means the tool is a citation-scoped check, not a raw token grep.
- **F1 masks its own span** before the other two rules run, so a
  `NEW-Seat-3` inside a citation parenthesis yields one finding, not two.
- The tool is **text-shaped**, not semantic. It cannot tell whether a
  registered `S159` actually supports the claim next to it; that remains the
  review question the round-52 closure already assigned.
- The tool does **not** read `corpus/SOURCES.md`. It reports unresolved draft
  ids, not unresolved or unregistered rows; `reports/round-53/d-count.py`'s
  `SID_BAD` leg and `tools/check-source-access.py` cover those.
- The lane's current working copy already has the fragments replaced, so a
  post-repair run of this tool in the lane prints 0 findings and exits 0.
  That is the repair confirmed, not the tool failing to see anything.
- **`--root` must point at the tree you mean.** With the section 6 fix, a
  relative path is root-relative and an absolute path is honoured as given,
  but a wrong `--root` still scans the wrong tree. The failing receipt in
  section 8 is the pattern to copy: name the tree explicitly and show the
  exit code.

## 13. Unrun checks

- **Not run against the round-51 or earlier trees.** Only the round-52 tip
  entry, the base tree and the declaration tree were scanned.
- **No build, lint, test or formatter was run** in the lane — the editing wave
  is in flight and the parent owns post-integration gate execution. The only
  execution was `python3 -m py_compile` on the sandbox copy (passes) and the
  tool's own runs.
- **The lane copy is untracked and uncommitted.** No committed receipt of the
  tool failing on the defect exists yet; the L1 owns that commit.

## 14. Tooling

No packages were installed or upgraded. Python 3 standard library only
(`argparse`, `os`, `re`, `sys`, `tempfile`); no third-party dependency, no
network access.

---

## Final file content

Path: `tools/check-draft-ids.py` (in the lane and in the sandbox clone,
byte-identical, sha256 `f49679b6a4174714b38a471084c91a6b9a949650d66c4fd7590469abba683fb4`).

```python
#!/usr/bin/env python3
"""Draft-id fragment check for corpus entries (round 53, mined mistake repair).

A corpus entry must cite sources by their registered `corpus/SOURCES.md` id
(`S001`, `S002`, ...). Round 52's integration left unresolved draft-id
fragments in the speech-surrogates entry: the seat draft ids were never mapped
to registry rows, so the text kept bare `-N` fragments such as `(S159, -6)`.
The fragments read like citations but name no source, so the entry cites
nothing on that claim and every gate that counts cited rows is blind to it.

This tool reports every unresolved draft id it can see in Markdown text:

  F1  a `NEW-<SeatName>-<n>` token anywhere in the file;
  F2  a `, -N` (or `; -N`) fragment inside a *citation parenthesis* — a
      parenthesis whose text contains at least one registry id `S###`;
  F3  a `-N` fragment written directly after a registry id inside a
      parenthesis, with no separator (`(S157-2)`).

F2 and F3 are disjoint by construction: a fragment preceded by a comma or
semicolon is F2, a fragment glued to the registry id is F3.

Two predicates keep the tool from firing on text that only looks like a
fragment:

  * A registry id is one that stands alone. `S0718-68942020000100013` is a
    SciELO article pid and `S0271-5309` a DOI stem, so an id glued to a URL
    (`=`, `/`, `.`) or a DOI stem (`-`) is not a registry id and is not a
    citation parenthesis. F3 therefore also requires a short fragment (at
    most three digits), which a DOI stem never has.
  * A fragment must be a list element of the citation: after it comes `,`,
    `;`, `)` or the end of the line. `-40 °C` inside a citation parenthesis
    is a temperature, not a draft id.

A bare `, -N` that follows a non-registry id (`(KTD-AR-S-0005, -0006,
-0007)`) or that is not parenthesised at all (`DR-FUR-01, -02, -06 and -08`)
is a different numbering convention, not a draft-id fragment, and is not
reported.

Usage:
  python3 -B tools/check-draft-ids.py [--root LANE_ROOT] [PATH ...]
  python3 -B tools/check-draft-ids.py --selftest

With no PATH the tool scans every `*.md` file under `<root>/corpus/knowledge/`.
A PATH may be a Markdown file or a directory (scanned recursively). A
relative PATH is resolved against `--root`, not against the process working
directory.

Output: one line per finding, then `DRAFT_IDS: <n> findings`.
  DRAFT_ID <path>:<line> '<token>'
The token is the matched text as it appears in the file: `, -6` for an F2
fragment, `-2` for an F3 fragment, `NEW-Seat-1` for an F1 token.
Exit codes: 0 no findings; 1 findings; 2 could not evaluate (stderr
DRAFT_ID_INPUT_ERROR). Read-only, stdlib only.
"""
import argparse
import os
import re
import sys
import tempfile

# A registry id that stands alone: not glued to a URL, a DOI stem or a word.
SID = re.compile(r"(?<![\w/=.&#?%:-])S\d{3,}(?![\w-])")
# A draft token: NEW-<SeatName>-<n>.
NEW_ID = re.compile(r"\bNEW-[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*-\d+\b")
# A separated fragment: `, -N` or `; -N`.
SEP_FRAG = re.compile(r"[,;][ \t]*-\d+\b")
# A glued fragment: `S###-N` with no separator.
ADJ_FRAG = re.compile(r"(?<![\w/=.&#?%:-])S\d{3,}[ \t]*(-\d{1,3})(?![\w-])")
# What may follow a fragment for it to be a list element of the citation.
TAIL = re.compile(r"[ \t]*(?:[,;)\]}]|$)")


def paren_groups(line):
    """Balanced parenthesis spans of one line as {start, end, parent} dicts.

    `start` is the index of the opening bracket, `end` the index just past the
    closing bracket, `parent` the start index of the enclosing group (or
    None). Groups are returned in closing order; use `find_group` to pick the
    innermost group containing a position.
    """
    stack = []
    groups = []
    for index, char in enumerate(line):
        if char == "(":
            stack.append((index, stack[-1][0] if stack else None))
        elif char == ")" and stack:
            start, parent = stack.pop()
            groups.append({"start": start, "end": index + 1, "parent": parent})
    return groups


def find_group(groups, position):
    """Innermost parenthesis group containing `position`, or None."""
    best = None
    for group in groups:
        if group["start"] < position < group["end"] - 1:
            if best is None or group["start"] > best["start"]:
                best = group
    return best


def group_chain(groups, group):
    """The group and its ancestors, innermost first."""
    chain = []
    by_start = {g["start"]: g for g in groups}
    current = group
    while current is not None:
        chain.append(current)
        current = by_start.get(current["parent"])
    return chain


def is_list_element(line, end):
    """True when a fragment ending at `end` closes a citation list element."""
    return TAIL.match(line, end) is not None


def scan_line(line, number):
    """Findings on one line as (line_number, column, token) tuples."""
    findings = []
    masked = list(line)
    for match in NEW_ID.finditer(line):
        findings.append((number, match.start(), match.group(0)))
        for index in range(match.start(), match.end()):
            masked[index] = " "
    masked = "".join(masked)
    groups = paren_groups(masked)
    citation = {}
    for group in groups:
        inner = masked[group["start"] + 1:group["end"] - 1]
        citation[group["start"]] = bool(SID.search(inner))
    for match in SEP_FRAG.finditer(masked):
        if not is_list_element(masked, match.end()):
            continue
        group = find_group(groups, match.start())
        if group is None:
            continue
        if not any(citation[g["start"]] for g in group_chain(groups, group)):
            continue
        findings.append((number, match.start(), match.group(0)))
    for match in ADJ_FRAG.finditer(masked):
        token = match.group(1)
        column = match.start(1)
        if not is_list_element(masked, match.end()):
            continue
        group = find_group(groups, column)
        if group is None:
            continue
        findings.append((number, column, token))
    findings.sort(key=lambda item: (item[1], item[2]))
    return findings


def scan_text(text):
    """Findings in a whole document as (line_number, column, token) tuples."""
    findings = []
    for number, line in enumerate(text.splitlines(), 1):
        findings.extend(scan_line(line, number))
    return findings


def resolve(root, target):
    """Resolve a CLI path against `--root`, so a relative path is root-relative."""
    return target if os.path.isabs(target) else os.path.join(root, target)


def markdown_files(root, paths):
    """Resolve CLI paths to a sorted list of Markdown files."""
    targets = list(paths) if paths else ["corpus/knowledge"]
    files = []
    for target in targets:
        target = resolve(root, target)
        if os.path.isdir(target):
            for folder, _dirs, names in os.walk(target):
                for name in sorted(names):
                    if name.endswith(".md"):
                        files.append(os.path.join(folder, name))
        elif os.path.isfile(target):
            files.append(target)
        else:
            raise ValueError(f"no such file or directory: {target}")
    return sorted(set(files))


def display_path(path, root):
    """Path as printed in a finding: root-relative when it lies under the root."""
    try:
        relative = os.path.relpath(path, root)
    except ValueError:
        return path
    return relative if not relative.startswith("..") else path


def check(root, paths):
    files = markdown_files(root, paths)
    findings = []
    for path in files:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        for number, _column, token in scan_text(text):
            findings.append(f"DRAFT_ID {display_path(path, root)}:{number} '{token}'")
    return files, findings


def run(root, paths):
    try:
        files, findings = check(root, paths)
    except (OSError, ValueError, UnicodeDecodeError) as error:
        print(f"DRAFT_ID_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    for line in findings:
        print(line)
    print(f"DRAFT_IDS: {len(findings)} findings")
    return 1 if findings else 0


def selftest():
    cases = [
        # name, text, expected findings
        ("clean", "the entry cites (S159) and S160 in prose.\n", 0),
        ("F1-new-token", "the row is NEW-ExecDraftIdChecker-1 in this draft.\n", 1),
        ("F1-new-token-in-paren", "cited (NEW-ScribeSec08-12) in passing.\n", 1),
        ("F1-hyphenated-seat-name", "the row is NEW-KotodamaR53-Scribe-3 here.\n", 1),
        ("F2-comma-fragment", "the drums reach people \"working their farms\" (S159, -6).\n", 1),
        ("F2-semicolon-fragment", "the range is \"up to five kilometres\" (S157; -2).\n", 1),
        ("F2-three-fragments", "the drum is a lossless code (S179, -5, -6, -7).\n", 3),
        ("F3-adjacent-fragment", "the quote sits in (S157-2) of the nomination.\n", 1),
        ("spec-example-S157", "the range is quoted in (S157, -2) of the form.\n", 1),
        ("spec-example-S179", "the drum is documented in (S179, -5, -6) here.\n", 2),
        ("neg-page-range", "the report prints (S145, pp. 2131-2134) for the row.\n", 0),
        ("neg-id-range", "the rows S134–S183 were opened this round.\n", 0),
        ("neg-id-range-ascii", "the rows S134-S183 were opened this round.\n", 0),
        ("neg-negative-number", "the sensor fails below -40 °C in winter.\n", 0),
        ("neg-negative-number-in-citation", "the row gives (S001, -40 °C) for the drum.\n", 0),
        ("neg-line-range", "the anchor is `phonetics-phonology.md:197-199`.\n", 0),
        ("neg-table-separator", "| channel | what it carries |\n|---|---|\n", 0),
        ("neg-hyphenated-word", "the co-speech channel and a well-known pair.\n", 0),
        ("neg-non-registry-paren", "preserved as the dated record it was (KTD-AR-S-0005, -0006, -0007).\n", 0),
        ("neg-non-registry-prose", "every consequence above was derived from DR-FUR-01, -02, -06 and -08.\n", 0),
        ("neg-to-verify", "the distance figure is (to-verify) for this instrument.\n", 0),
        ("neg-scielo-pid", "full text (https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-68942020000100013).\n", 0),
        ("neg-doi-stem", "the DOI (10.1016/S0271-5309(03)00012-0) ends the entry.\n", 0),
        ("neg-doi-in-parens", "the article (https://doi.org/10.4067/S0717-73562014000300003) is open.\n", 0),
        ("mixed", "(S159, -6) is a fragment; (S145, pp. 2131-2134) and -40 °C are not.\n", 1),
    ]
    failures = 0
    for name, body, want in cases:
        found = scan_text(body)
        ok = len(found) == want
        failures += not ok
        detail = ", ".join(f"{number}:{token}" for number, _column, token in found)
        print(f"{'PASS' if ok else 'FAIL'} {name} want={want} got={len(found)} [{detail}]")
    total = len(cases)
    print(f"SELFTEST: {total - failures}/{total} pass")
    failures += filesystem_controls()
    print("SELFTEST: filesystem controls", "PASS" if failures == 0 else "FAIL")
    return 1 if failures else 0


def filesystem_controls():
    """Controls that exercise the path resolution and the exit codes."""
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        knowledge = os.path.join(tmp, "corpus", "knowledge", "p")
        os.makedirs(knowledge)
        with open(os.path.join(knowledge, "e.md"), "w", encoding="utf-8") as handle:
            handle.write("the quote sits in (S159, -6) here.\n")
        # A relative path is resolved against --root, not the process CWD.
        _files, findings = check(tmp, ["corpus/knowledge"])
        ok = len(findings) == 1 and findings[0].startswith(
            "DRAFT_ID corpus/knowledge/p/e.md:1 ")
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} root-relative-path findings={len(findings)}")
        # An absolute path is accepted too.
        _files, findings = check(tmp, [knowledge])
        ok = len(findings) == 1
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} absolute-path findings={len(findings)}")
        # A missing path is an input error, exit 2.
        got = run(tmp, ["no/such/dir"])
        ok = got == 2
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} missing-path exit={got}")
        # A clean tree exits 0.
        with open(os.path.join(knowledge, "e.md"), "w", encoding="utf-8") as handle:
            handle.write("the quote sits in (S159) here.\n")
        got = run(tmp, ["corpus/knowledge"])
        ok = got == 0
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} clean-tree exit={got}")
        # A tree with a fragment exits 1.
        with open(os.path.join(knowledge, "e.md"), "w", encoding="utf-8") as handle:
            handle.write("the quote sits in (S159, -6) here.\n")
        got = run(tmp, ["corpus/knowledge"])
        ok = got == 1
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'} defect-tree exit={got}")
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=".")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    return run(args.root, args.paths)


if __name__ == "__main__":
    sys.exit(main())
```
