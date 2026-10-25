# CritGaming1 — round 71 wave 2: gaming ACCEPT-C-71

Seat: `L1Kotodama71.CritGaming1` (critic, leaf). Read-only on the lane; every mutation ran in a scratch copy under `/tmp/cg1-*`, made with `git archive HEAD | tar -x` at `14c88d9`, then `cp -a` once per mutation.
Counter under test: `reports/round-71/accept-c.py`. Its sha256 was `1df995c2…5db4` when I started and `80b4ca09…0ed8` after `edd7895` (see F7).
Tooling: nothing installed or updated.

## Verdict

**FAIL (the instrument can be gamed). The landed data holds.** Asks (a) and (c) were both gamed: a 12-line stub passes all 7 legs, and the sweep leg passes with extra owners present. For ask (b), all 13 rows really were opened: every Gate quote is located verbatim in the source. But nothing in the counter checks the Gate. Deleting the Gate table, or the whole lesson, still gives PASS.

The live entry is genuine. Its 13 Gate quotes are verbatim, its body claims are grounded in the fetched pages, and the base-tree gap claim survives even a stemmed sweep. These are defects in the instrument and the predicate, not in the data. They are fixable, but under the freeze rule the fix belongs in a new counter (round 72) or a declared correction. It must not be an edit to the frozen file.

## Baseline (PASS as reported)

```
cd kotodama-shokunin && python3 -B reports/round-71/accept-c.py --root .   # 7/7 LEG PASS, ACCEPT-C-71: PASS, exit 0
```

Do-nothing control: I copied `accept-c.py` into `git archive b94a543`, the base commit. The run dies with `FileNotFoundError` (traceback, exit 1). It does not print a `LEG FAIL` line or exit 2, although the docstring says "2 input error". The base counts are 35 / 242 / 784, which match `controls-c.txt`.

## (a) Could a stub entry pass? — YES (FAIL)

Scratch mutations, each followed by `python3 -B reports/round-71/accept-c.py --root .`:

| id | mutation of `dance-performance-movement-codes.md` | result |
|---|---|---|
| A1 | `head -24` (all `##` body sections deleted) | **PASS exit 0** |
| A2 | `head -14` (only the 13 `- source:` lines; no gap-filled/topic/body) | **PASS exit 0** |
| A3 | `printf 'S%s\n' 861 … 872` (12 bare ids, nothing else) | **PASS exit 0** |
| A4 | 12 ids inside an HTML comment + `lorem` | **PASS exit 0** |
| A5 | everything after the first `## ` deleted | **PASS exit 0** |
| A6 | empty file | FAIL (CITED) |
| A7 | 12 **old** mined rows (S001…S035), with the entry path appended to their used-by cells | **PASS exit 0** |

The frozen shell `counting_command` in `claims.json` also reaches its declared target on the A3 stub: `36`, `243`, `797` (≥ 796), `CITED-LINES: 0 finding(s)` with exit 0, and `test -f` returning 0.

Why it passes:
- The CITED leg is `set(TOKEN_RE.findall(text))` over the whole file. It has no notion of a body, a section, prose or the header keys. One id per line also keeps `check-cited-lines` clean.
- The counter never reads the `opened` cell (`cells[9]`) and never compares an id against base. A7 shows that "new rows opened this round" goes unenforced. MutC point 3 reports the same gap; A7 shows it is exploitable end-to-end.
- The registry-exactness kill rule ("increases by exactly the number of new rows opened for the claim") has no leg. A8 appended a junk, uncited `S874` row and the counter still gave **PASS exit 0**.
- Live observation: `S873` was cited only in the header block, with no body sentence. An uncommitted working-tree edit now adds `(S873)` to the Calibration shelf. That confirms header-only citations satisfy the counter today.

## (b) Could a row be mined without opening? — the data was opened; the counter can't tell (FAIL on the instrument)

The predicate says "each cited row's quote is opened and quoted in the round lesson Gate". The counter has no leg that reads `corpus/lessons/round-71.md`.

| id | mutation | result |
|---|---|---|
| B1 | delete all 13 `\| S86x — / \| S87x —` Gate rows from the lesson | **PASS exit 0** |
| B2 | `rm corpus/lessons/round-71.md` | **PASS exit 0** |

Data check: I fetched each source and searched its HTML for the quote after unescaping, stripping tags, applying NFC and collapsing whitespace (`/tmp/cg1-q.py`).

- Live `ich.unesco.org` answered 200 for S861–S867.
- Wayback refused port 443 from this host, so I used `http://web.archive.org/...` for S869. The live RAD page returns 403.
- Every quote was **FOUND verbatim**: S861 (15 words), S862 (12), S863 (8), S864 (10), S865 (8), S866 (10), S867 (7), S868 (10), S869 (11, capture `20260907171642`), S870 (6), S871 (10), S872 (8), S873 (6).
- `python3 -B tools/check-gate-quotes.py corpus/lessons/round-71.md` prints `GATE_QUOTES: 0 findings`, rc 0.
- Body-claim spot check: grounded in the same pages. S864 "twenty hours", S863 "village housewives", S865 male/female technique and "dynasties"/"clubs", S867 onnagata/mie, S870 "originated by Rudolf Laban", S866 "humorously … social issues", S871 mātṛkā.

## (c) Could the sweep leg pass with extra owners? — YES (FAIL)

| id | mutation | result |
|---|---|---|
| C1 | rename entry → `dance-codes.md` | FAIL (ENTRY, then a traceback at `open(ENTRY)`, exit 1) |
| C2 | rename entry → `movement-codes.md` | FAIL (same traceback) |
| C3 | `masks-masquerade.md` topic → `- topic: dance, dancing and choreography codes; …` | **PASS exit 0** |
| C4 | add `choreography-systems.md` (topic `choreography and dance notation systems`) **and delete** `funerary-material-culture.md` | **PASS exit 0** |
| C5 | `linguistics/gesture-co-speech-pointing.md` topic → `dance and performance movement codes` | **PASS exit 0** |
| C6 | `dress-through-eras.md` topic → `Dances, choreographies and dancing bodies` | **PASS exit 0** |
| C7 | `dress-through-eras.md` topic → `performance codes` | FAIL (SWEEP) — caught |
| C8 | `-  topic: performance codes` (two spaces after `-`) | **PASS exit 0** |
| C9 | add `dance-notes.txt` | FAIL (SWEEP) — caught |

Why:
- **`\b(danc|choreograph)\b` only ever matches the literal tokens `danc` and `choreograph`.** Demo: `printf -- '- topic: dance\n- topic: danc\n- topic: choreography\n- topic: Dancing\n' | grep -niE '^- topic:.*\b(danc|choreograph|movement culture|performance)\b'` matches only `- topic: danc`. The live entry is caught only because its topic line contains the word "performance". In practice, the word-bounding added in the pre-data correction leaves the sweep blind to "dance" and "choreography".
- The topic sweep is anchored to `^- topic:` exactly (C8 bypasses it) and scoped to `culture-material/*.md` (C5 bypasses it).
- The filename sweep is `*danc*` only. `choreograph*`, `performance*` and `movement*` filenames are never swept (C4).
- There is no NOHARM leg, although the predicate requires "NOHARM sweep diff = exactly the new entry + the new rows + README/lesson/scorecard/log appends". C4 deletes an unrelated entry and still passes, because the 36/243 count is preserved.

The base-tree gap claim holds anyway. At `b94a543`, `grep -rnioE '^- topic:.*\b(danc\w*|choreograph\w*)' corpus/knowledge/culture-material/*.md` prints nothing. Outside the partition, the stem sweep hits only topic lines in 5 civilization entries: `amazigh-berber`, `java-majapahit`, `lakota-plains`, `siam-thai` and `taino`. Those are tradition-scoped mentions, so the out-of-partition scope is a tradeoff to declare, not a false gap.

## Additional findings

- **F7 — the counter's bytes changed after scoring.** `measures-c.txt` stamps `# counter sha256 (self): 1df995c2…5db4` at `8c203bd`. `edd7895` ("docstring accuracy (Filler37 nit)") then edited `accept-c.py`, which now hashes to `80b4ca09…0ed8`. The change is docstring-only and behaviour-neutral, but it contradicts the freeze rule ("not edited after any seat scores them"), and the receipt's self-hash no longer matches the live counter. Also, `measures-c.txt` was untracked at `14c88d9`, while the entry's `- recheck:` line names it as the commit receipt.
- **F8 — the counter was born with the data.** `git log --diff-filter=A -- reports/round-71/accept-c.py` shows it first appears in `498db73`, the data-landing commit; it is not present at freeze commit `65ff151`. The lesson already records this (instrument-provenance row). It matters here because this post-hoc counter carries the gameable legs above, and the frozen shell command, re-verified as authoritative, is gameable too (A3).
- **F9 — `controls-c.txt` has 0 of the six 17/19 header lines.** Measured with `grep -cE '^# (counter sha256|stamped revision|…)'`. This is the same defect class Ca repaired for round 70. `controls-ca.txt` also has 0.

## Impacted axes

coverage (claim C's frozen predicate can be met by a stub); calibration (the receipt/counter identity diverged; the Gate and NOHARM legs promised in the predicate are absent); depth (none).

## Smallest safe correction (new counter or declared correction; do not edit the frozen file)

1. **BODY:** each counted id must appear in at least one line that is not a `- source:` line and sits under a `## ` heading. Also require the header keys `- gap filled:`, `- topic:`, `- scope:` and `- refuses:`.
2. **NEW:** each counted row must have `cells[9] == "2026-10-25"` and an id above S860, the base maximum. Add a leg checking that registry rows at lands minus registry rows at base equals the number of new ids.
3. **GATE:** parse the `## Gate` table in `corpus/lessons/round-71.md`. Require one row per counted id with a non-empty quote, and require `check-gate-quotes.py` to exit 0.
4. **SWEEP:**
   - Use stems `\b(danc\w*|choreograph\w*|movement culture|performance)\b`.
   - Match topic lines with `^\s*[-*]\s+topic\s*:`.
   - Sweep filenames for `*danc*`, `*choreograph*` and `*performance*`.
   - Extend to `corpus/knowledge/**`, with a declared allowlist of the 5 civilization files.
5. **NOHARM:** check `git diff --name-status <base>..<lands>`. Any `D` or `R` under `corpus/knowledge/`, or any path outside {entry, `corpus/SOURCES.md`, README, lesson, SCORECARD, log, `reports/round-71/**`, `.ufo/**`}, fails.
6. **F7:** either revert `edd7895`, or re-stamp `measures-c.txt` with the current counter hash and log the change as a correction.
7. **Error path:** fail cleanly (`LEG FAIL ENTRY`, exit 2) instead of a traceback when the entry is absent.

## Commands (re-runnable)

- Scratch: `S=$(mktemp -d); git archive HEAD | tar -x -C $S`, then per mutation `T=$(mktemp -d); cp -a $S/. $T/; cd $T; <mutation>; python3 -B reports/round-71/accept-c.py --root .; echo EXIT=$?`
- A3 stub: `printf 'S%s\n' 861 862 863 864 865 866 867 868 869 870 871 872 > corpus/knowledge/culture-material/dance-performance-movement-codes.md`
- A7: `/tmp/cg1-oldrows.py` (appends the entry to 12 old mined rows' used-by and writes those ids as the entry)
- B1: `sed -i '/^| S86[1-9] —/d;/^| S87[0-3] —/d' corpus/lessons/round-71.md`
- C3: `sed -i '0,/^- topic:/s//- topic: dance, dancing and choreography codes;/' corpus/knowledge/culture-material/masks-masquerade.md`
- Quote check: `/tmp/cg1-q.py` over the fetched pages in `/tmp/cg1-src/`
- F7: `sha256sum reports/round-71/accept-c.py; git show 498db73:reports/round-71/accept-c.py | sha256sum; head -1 reports/round-71/telemetry/measures-c.txt`
