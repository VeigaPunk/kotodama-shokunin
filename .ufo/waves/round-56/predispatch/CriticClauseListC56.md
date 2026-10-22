# Round 56 pre-dispatch check, claim C (coverage): CriticClauseListC56

Non-author seat, QUALITY criterion 11 (`corpus/QUALITY.md:39`). Claim base `052f145`; draft `reports/round-56/claims.json` and `separability-manifest.json` read from the worktree (uncommitted).

Scratch: `/fast/scratch/hyaku/kotodama-r56/CriticClauseListC56/repo` = `git archive 052f145` plus the two worktree json files, `git init` there (scratch commit `501f365`), with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset. No installs. Nothing in the lane was written except this file.

## What holds (evidence)

- **The builder runs as declared.** `cd repo && python3 -B reports/round-56/criterion11-controls.py <scratch>/repo HEAD` exits 0 with `CONTROLS 15/15 as expected`. GREEN exits 0. Each RED fails exactly its declared leg; RED-COUNT is the one declared two-leg control (SET and SWEEP). The instrument sha256s match the files at 052f145 (`accept-c.py 465d0d51…`, `criterion11-controls.py b1bcffca…`).
- **The base run equals the declared `before`.** `python3 -B reports/round-56/accept-c.py` exits 1 with `SET FAIL count=231 … added=[] removed=[]`, `SWEEP FAIL exit=0 rows 231 files 231 missing_from_index 0 []`, `FLOOR FAIL cited=0` and `RANGE/STATUS/USEDBY PASS` (vacuous). It also prints `ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings`.
- **Words to clauses.** Every mechanical phrase of the statement (`claims.json:19`) maps to a clause and a leg:
  - "231 to 232": C-count (SET and SWEEP), with the 231 pinned by the base-list length check at `accept-c.py:60`.
  - "the one file added … no file is removed" and "of any extension": C-one-new-file (SET), with RED-SET and RED-SET-EXT.
  - "rows 232 files 232 and missing_from_index 0" and the sweep exit: C-index (SWEEP). RED-SWEEP drives `missing_from_index 1`, RED-SWEEP-EXIT drives exit 1, and RED-COUNT moves rows to 233.
  - "at least 20 distinct": C-floor (FLOOR).
  - "S359-S418", "exactly one row" and "no S-id range": C-range (RANGE).
  - "mined": C-status (STATUS). "names the entry in its used-by cell": C-usedby (USEDBY). "check-source-access exits 0": C-access (ACCESS).
  - "seven legs passing": the builder's `len(legs) == 7` (`criterion11-controls.py:205`).
- **No leg passes vacuously at landing.** STATUS and USEDBY are vacuous only when nothing is cited, and FLOOR at 20 or more forbids that. RANGE's upper bound is new this round, and the LAST_SID=419 mutant (below) shows RED-RANGE-HIGH kills it.
- **Review-only items have no weaker stand-in.** `accept-c.py` has no topic or `- topic:` predicate. The topic, the page-carries-sentence check, opened-by-ordinary-means, calibration, one-way pointers, handoff and gap substance stay as review only. The gap evidence reproduces: the base has 0 filename owners matching `kongo`, and `grep -ril kongo corpus/knowledge` returns only `linguistics/language-contact.md`.
- **The export regex is exact.** Looping `\bS(359|3[6-9][0-9]|40[0-9]|41[0-8])\b` over S000..S999 gives `matches 60 359 418 True` (exactly S359..S418). Boundary probes (`S3590`, `S0359`, `xS359`, `S359a`, `S359_`, `S358`, `S419`, `S4180`) give no match.
- **Export novelty holds.** In the base copies of C's lands, the block-id count is `corpus/README.md: 0` and `corpus/SOURCES.md: 0`, and the entry is absent at base. O's land `tools/check-gate-quotes.py` has 0 block matches; its only S-id is `S187` at line 88. A staged separability run (GREEN stand-in landing, stub `corpus/lessons/round-56.md`, `--lane <lane> --root <staged>`) gives no input error and no C finding. The only finding is `O-><base>`, which is expected because O is not landed. Appending `# fixture id S360` to O's land yields `SEPARABILITY_DEPENDENCY O->C via export … matched tools/check-gate-quotes.py:431`, so the export binds O's lines.

## Findings

### 1. RANGE's lower edge S359 is never tested at its nearest near-miss (S358). Severity: blocks dispatch

- **Words:** "every cited S-id lies in C's reserved block **S359**-S418" (`claims.json:19`, clause C-range).
- **Code:** `accept-c.py:94` uses `not FIRST_SID <= int(s[1:]) <= LAST_SID`. RED-RANGE cites **S357** (`criterion11-controls.py:130-138`; `claims.json:65`).
- **Why it matters:** criterion 11 asks for "the nearest near-miss". S358 is nearer, and the round-55 shape used exactly `FIRST_SID-1` (S284). S358 is `queued` with used-by `—` at base, which is presumably why it was avoided. But STATUS and USEDBY skip rows that fail RANGE (`accept-c.py:96`), so S358 can be cited with only RANGE failing.
- **Demonstration:** a mutant `accept-c.py` with `FIRST_SID = 358`, committed in scratch `mut358`, then run through the unmodified builder:

  ```
  python3 -B reports/round-56/criterion11-controls.py <scratch>/mut358 HEAD
  ## RED-RANGE: exit 1 (expected 1); failing legs ['RANGE']; AS EXPECTED
  CONTROLS 15/15 as expected          (builder exit 0)
  ```

  The off-by-one survives every control, so the S359 edge is "unverified, not passing". For comparison, the `LAST_SID = 419` mutant gives `RED-RANGE-HIGH: exit 0 … NOT AS EXPECTED`, `CONTROLS 14/15` and builder exit 1, so the upper edge is properly tested.
- **Minimal fix:** in `red_range`, cite `(S358)` and append the entry to S358's used-by. Update `claims.json:65` to "RED-RANGE (S358 cited, with the entry in S358's used-by)". I verified this in scratch (`fix`, `fixmut`):
  - Real instrument: `RANGE FAIL bad=['S358']`, `STATUS PASS`, `USEDBY PASS`, `CONTROLS 15/15`, exit 0.
  - FIRST_SID=358 mutant: `RED-RANGE … failing legs ['STATUS']; NOT AS EXPECTED`, `CONTROLS 14/15`, exit 1. The mutant is now killed.
  - This changes a committed instrument, so the claim base moves.

### 2. "exactly one corpus/SOURCES.md row" is weaker than the lane's own row grammar. Severity: should fix

- **Words:** "has exactly one corpus/SOURCES.md row" (C-range).
- **Code:** `accept-c.py:86` counts only lines matching `^\| S\d{3} ` (exactly one space). The lane's access checker treats `^\|\s*(S\d{3,})\s*\|` as a row (`tools/check-source-access.py:31`) and also parses these looser lines.
- **Demonstration:** `python3 -B probe.py` in scratch, on the GREEN copy plus a second, queued S378 row:
  - `DUP-ROW-2SPACE ('|  S378 |'): exit 0; failing []` with `RANGE PASS bad=[]`
  - `DUP-ROW-NOSPACE ('|S378 |'): exit 0; failing []`
- **Minimal fix:** count rows with `^\|\s*(S\d{3,})\s*\|`, the same grammar as the access checker, and key `table` by the captured id. At base both grammars count the same rows (strict 378, loose 378 on the staged copy), so nothing changes at base. Add a RED-RANGE-DUP variant using `|S378 |`.

### 3. "the entry writes no S-id range" misses common range notations. Severity: should fix

- **Code:** `accept-c.py:84` uses `\bS\d{3}\s*(?:[–—-]|to)\s*S?\d{3}\b`. This gap is inherited from round 55.
- **Demonstration:** on GREEN with `(S378)` replaced:

  | Notation | Exit | RANGE result |
  |---|---|---|
  | `(S377 through S378)` | 0 | PASS, `range_notation=[]` |
  | `(S377…S378)` | 0 | PASS, `range_notation=[]` |
  | `(S377−S378)` (U+2212) | 0 | PASS, `range_notation=[]` |
  | `(S377‒S378)` (U+2012) | 0 | PASS, `range_notation=[]` |
  | `(S377–78)` (two-digit tail) | 1 | PASS, `range_notation=[]` |

  The two-digit tail fails only through FLOOR, because it drops the distinct count to 19. In an entry citing 21 ids it would pass.
- **Minimal fix:** use `\bS\d{3}\s*(?:[-‐‑‒–—―−~…]|\.{2,3}|to|through|thru)\s*S?\d{2,3}\b`.
  - It catches all seven probe notations and none of `(S359, S360)`, `(S359; S360)` or `S359 and S360`.
  - Over all 231 base entries it finds the same 10 hits as the current regex, so it adds no false positives.
  - Add a RED-RANGE-SPAN variant using `(S377 through S378)`.

### 4. "names the entry in its used-by cell" is a substring test. Severity: should fix

- **Code:** `accept-c.py:99` uses `ENTRY not in table[s][11]`.
- **Demonstration:** setting S378's used-by to `corpus/knowledge/civilizations/kongo-kingdom.md.bak` gives `USEDBY-SUBSTR: exit 0; failing []`.
- **Minimal fix:** `ENTRY not in [u.strip() for u in table[s][11].split(",")]`. Base convention allows this: all 313 used-by cells that name an entry use full comma-separated paths, and none uses a short form.

### 5. SET does not see a symlinked directory under corpus/knowledge. Severity: note

- **Words:** "every file under corpus/knowledge, of any extension".
- **Code:** `accept-c.py:63-64` calls `os.walk` without `followlinks`, so a symlink to a directory lands in `dirs` and is never listed. Git would track it as a file.
- **Demonstration:** GREEN plus `corpus/knowledge/civilizations/linked-dir -> ../../../outside` (which contains `hidden.md`) gives `SYMDIR exit 0`, `SET PASS count=232`. A symlinked *file* is caught (`SET FAIL count=233 added=[…kongo-alias, …]`).
- **Minimal fix:** in the walk, also add every `d` in `dirs` for which `os.path.islink` is true to `live`.

### 6. False provenance in the instrument docstring. Severity: note

- **Code:** `accept-c.py:2` reads "adapted from **reports/round-56/accept-c.py**", which is itself; the real source is `reports/round-55/accept-c.py` (`diff` confirms). Also, the docstring's review-only list (`accept-c.py:24-27`) omits two items that `claims.json` lists: calibration under criterion 2 including the cosmogram reading, and the lore handoff section.
- **Minimal fix:** at the next instrument commit, change the docstring to "adapted from reports/round-55/accept-c.py" and point the review-only line at `claims.json` only. This does not affect acceptance.

### 7. The export rule and the record scope are not enforced by the manifest. Severity: note

- **Export rule** (`claims.json:12`): "no other claim **or record** writes an id in that block this round". The separability tool never scans records ("Records are never scanned as dependers", `tools/check-claim-separability.py:20`). The record half of the rule therefore has no mechanical check. In addition, the lesson `corpus/lessons/round-56.md` is a record and will plausibly mention C's ids.
- **Record scope** (`claims.json:225`): "routed registry fixes in corpus/SOURCES.md rows below S359" are declared records. But `corpus/SOURCES.md` appears only in C's manifest lands (`separability-manifest.json:8-12`), so those bytes are attributed to C's landed bytes. A record edit to a base row can also flip C's whole-registry ACCESS leg. That gives two authorities for one path.
- **Minimal fix:** narrow the export rule's wording to "no other claim assigns an id in that block", or add a record-side check. In `claims.json:225`, state that registry fixes land under C's path and are attributed to C by the manifest.

VERDICT: defects found (7)
