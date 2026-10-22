# Round 57 pre-dispatch critic — claim O clause list and shortcut hunt (CriticClauseListO57)

**Instrument revision measured:** lane `main` at declaration commit `51726fa6` (scratch clone `/fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/lane`, checked out detached at `51726fa6`). `git diff 6f08c494 51726fa6 -- reports/round-57/accept-o.py reports/round-57/controls-o.py tools/check-gate-quotes.py` is empty, so the claim base and the declaration carry the same instruments.

| file | sha256 |
|---|---|
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/accept-o.py` | `906c7f08932167dd60c9c9f3a65718f7bc22b20828b9a4512ee6139f36c31672` |
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-gate-quotes.py` (base) | `3a13ab9cb93e211bd8c79bd2dfe78e6fb6cd76df0a87efebb315e68688bf6b67` |
| `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/base-gate-keep.txt` | `817b000849fb7c8d7b16c836a8103ac3267ea22b07d76c4944a5b94dce7ad120` (matches PINS) |

All scratch artefacts are under `/fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/`: the builder `build.py`, the variants in `tools/*.py`, the full instrument outputs in `out-*.txt`, and `oracle.py` and `realrow.py`. No installs. Nothing in the lane was written except this report.

## Verdict

**The frozen ACCEPT-O-57 counter can be met without the claimed work. That is two blocking defects (B1 and B2), plus one blocking gap in the criterion-11 receipt (B3).** Honest work does meet all six legs (section 4), and GEN's oracle is right for every template (section 3). The fixes below are all small changes to the instrument and controls.

- **B1 (GEN):** GEN can be passed with **no grammar change at all**.
  - `cheat-replay-identity.py` replays the generator, because the seed is the temp directory's name.
  - `cheat-seatgen-identity.py` turns on bare-numeric detection only on rows ending `Seat: Gen.`.
  - Both print `ACCEPT-O-57: PASS` with exit 0, yet on a real-shaped lesson both report `GATE_QUOTES: 0 findings`, exit 0, for two bare numeric references.
  - The second cheat is the fixture-text-keyed shortcut that the declaration's `two_claim_note` says cannot pass.
- **B2 (MUTANTS):** a 6-line identity snapshot in `selftest()` kills all three in-process mutants and tests no behaviour.
  - Its selftest passes an on-disk double-decode mutant: `SELFTEST: 38/38 pass`, exit 0.
  - This is cheaper than the honest kill set, so it is "the cheapest shortcut" under QUALITY criterion 11 and addendum §9. It is disclosed as a residual, but no control scores it.
- **B3 (criterion 11):** the committed receipt `reports/round-57/telemetry/controls-o.txt` has **no green control** (all 7 controls exit 1).
  - Only one control (hashpin, for O-mutants) isolates its clause. The other five clauses have no red control that fails their leg alone; criterion 11 calls such a clause "unverified, not passing".
  - Isolating near-miss controls do exist; I built them (section 4).

## 1. Clause list check

The O statement in `claims.json` line 50 reads: "reports a numeric character reference written without its closing `;` (decimal or hexadecimal) as html-entity, and its --selftest fails under each of the three round-56 survivor mutants; ACCEPT-O-57 holds (see predicate)."

| clause | words match statement/predicate? | leg that can fail | red control cited | isolated per criterion 11? (receipt line) |
|---|---|---|---|---|
| O-gen | Yes, it is the statement's "numeric reference without `;` … as html-entity" plus predicate GEN. | GEN | base, sidcheat, shortlist, anyamp | **No.** Base "does not count as a control" (criterion 11). sidcheat fails GEN+MULTI+MUTANTS (receipt l.12), shortlist fails GEN+MUTANTS (l.22), anyamp fails GEN+MUTANTS+SELFTEST (l.32). |
| O-multi | Yes, predicate MULTI ("the valid lesson's own findings still print"). | MULTI | sidcheat | **No.** sidcheat also fails GEN and MUTANTS (l.12). |
| O-mutants | Yes, the statement's "--selftest fails under each of the three … mutants". | MUTANTS | base, hashpin | **Yes, via hashpin:** GEN, MULTI, KEEP, FORMAT, SELFTEST PASS and MUTANTS FAIL (l.42-51). |
| O-keep | Yes, predicate KEEP. | KEEP | keepbreak | **No.** keepbreak fails all six legs (l.52). |
| O-format | Partly. The predicate says only "FORMAT" and never defines it; the definition lives in the accept-o docstring. | FORMAT | keepbreak, stderrnoise | **No.** stderrnoise fails FORMAT+GEN+MULTI+MUTANTS+SELFTEST (l.62). |
| O-selftest | Yes, predicate SELFTEST. | SELFTEST | anyamp | **No.** anyamp fails GEN+MUTANTS+SELFTEST (l.32). |

Wording points (minor):

- **"drawn from the whole table" (predicate GEN) is not true.** The draw is the 571 letter-valued names out of 2125 `;`-terminated html5 names (`realrow.py` output: `html5 table: 2125 names ending ';', 571 letter-valued (GEN's draw)`). The accept-o docstring says this correctly; the predicate overstates it.
- **The statement's "its --selftest fails" is not what MUTANTS runs.** MUTANTS calls `module.selftest()` in-process; only SELFTEST runs the `--selftest` CLI, and only unmutated. The words should say "its selftest() returns non-zero".
- **GEN observes reporting, not decoding, of bare numeric references.** A tool that flags `&#233w` but leaves it undecoded passes GEN, because no template's other findings depend on that decode. The statement claims only reporting, so this is consistent. The review-only docstring item covers the policy statement.

## 2. Shortcut hunt (commands run from the scratch clone root at `51726fa6`)

Builder: `python3 -B /fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/build.py`, which applies anchored swaps to the base tool, as `controls-o.py` does.

### 2a. GEN keyed on generator artefacts: both cheats PASS

`cheat-replay-identity.py` (base grammar **unchanged**, sha256 `503eba17…`) is 26 diff lines. In `check()`, when a path matches `/kotodama-r57-accept-o-[^/]+/(\d+)/lessons/` it does three things:

1. It reads the seed from the directory name; `accept-o.py:294` uses `os.path.join(tmp, str(seed))`.
2. It loads `reports/round-57/accept-o.py` from its cwd; `run()` uses `cwd=root`.
3. It calls `generate()` and emits the expected multiset.

It also carries the B2 identity snapshot.

```
$ python3 -B reports/round-57/accept-o.py --tool /fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/tools/cheat-replay-identity.py
# tool ../tools/cheat-replay-identity.py sha256 503eba1787d197a35273e469dd986295ab177d2bb1e2d6c8707c9038e0739404
# seeds [1826312549, 1826312550, 1826312551, 1826312552, 1826312553]
GEN PASS lessons=5 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 38/38 pass
ACCEPT-O-57: PASS
exit=0
```

`cheat-seatgen-identity.py` (sha256 `370bdfeb…`) is 8 diff lines: the base grammar plus `if "Seat: Gen." in line and re.search(r"&#(?:[0-9]+|[xX][0-9A-Fa-f]+)(?![0-9A-Fa-f;])", line): has_html_entity = True`, plus the identity snapshot.

```
$ python3 -B reports/round-57/accept-o.py --tool /fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/tools/cheat-seatgen-identity.py
# seeds [3430422806, 3430422807, 3430422808, 3430422809, 3430422810]
GEN PASS lessons=5 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 38/38 pass
ACCEPT-O-57: PASS
exit=0
```

Both cheats also PASS with `--seed 5700` (exit 0; `out-*-5700.txt`). Neither does the claimed work. The lesson below has two real-shaped rows, `"the caf&#233 society"` and `"the &#8220w quoted word"`, with real hosts and `Seat: Scout.`/`Seat: Scribe.`:

```
$ python3 -B realrow.py      (exit=0)
  base                    GATE_QUOTES: 0 findings  exit=0
  honest                  …:5 S900 html-entity / …:6 S901 html-entity / GATE_QUOTES: 2 findings  exit=1
  cheat-replay-identity   GATE_QUOTES: 0 findings  exit=0
  cheat-seatgen-identity  GATE_QUOTES: 0 findings  exit=0
```

Other constant artefacts that a one-line key would work on equally well:

- the URL host `https://example.invalid/`;
- the Grounds prefix `A generated row on`;
- the date `accessed 2026-10-22`;
- the title `# Generated lesson`;
- the registry header `# Generated registry` and `generated — ` source cells;
- the temp prefix `kotodama-r57-accept-o-`;
- the 14-syllable lowercase alphabet;
- exactly 13 rows, one per template.

On cost: the honest grammar fix is two characters (`;?` twice), so these keys are not cheaper than the honest GEN fix. The replay cheat, though, is a complete PASS with zero grammar work. Together with the seatgen cheat, it shows the predicate does not entail the statement, which is the round-56 defect class (`corpus/lessons/round-56-verifier-spotcheck.md` §5 item 1).

### 2b. MUTANTS without behavioural tests: PASS

`cheat-identity.py` (sha256 `f83bc96f…`) is the honest `;?` grammar plus `_PRISTINE = (decode_html_references, check, run)` at module end. `selftest()` opens with `if (decode_html_references, check, run) != _PRISTINE: return 1`. It adds no new test case.

```
$ python3 -B reports/round-57/accept-o.py --tool /fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/tools/cheat-identity.py
# seeds [2370785799, 2370785800, 2370785801, 2370785802, 2370785803]
GEN PASS lessons=5 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 38/38 pass
ACCEPT-O-57: PASS
exit=0
```

Its selftest does not test behaviour. The same double-decode applied **on disk** survives:

```
$ python3 -B tools/cheat-identity-ondisk-double-decode.py --selftest   ->  SELFTEST: 38/38 pass  exit=0
$ python3 -B tools/honest-ondisk-double-decode.py --selftest           ->  SELFTEST: 42/43 pass  exit=1
```

Compiling the patches "under the tool's own file name" (`claims.json` review_only, accept-o `MUTANT_RUNNER`) does not stop this, because the snapshot compares function identity, not `co_filename`. Equivalent described variants:

- `__code__` or `co_firstlineno` comparison;
- `any(k.startswith("_orig_") for k in globals())`, which keys on the mutant text: all three patches bind `_orig_*`.

## 3. GEN oracle correctness (attack c)

`oracle.py` re-generates lessons with accept-o's own `generate()` and compares each row's expected `html-entity` with an independent reading of the declared policy. That reading is: numeric `&#[0-9]+` or `&#[xX][0-9A-Fa-f]+` bind with or without `;`; named references bind only as an exact `name;` in `html.entities.html5`. The script also runs the honest tool on each lesson.

```
$ python3 -B oracle.py 1000 /fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/tools/honest.py
seeds=1000 oracle_vs_independent_mismatches=0 []
seeds=1000 tool_mismatches=0 []
rows where html.unescape changes text but oracle expects none: {'&copy ': 503, '&reg ': 497}
exit=0
```

Per template, the expectations are right under the declared policy:

- **named-1 and named-2:** letter-valued `name;` gives html-entity.
- **numeric-bare:** `&#233 ` and `&#233w` decode in WHATWG and in `html.unescape`.
- **hex-bare:** the tail is drawn from `ghkmnprstvz`, so a greedy hex match cannot absorb it.
- **invalid-codepoint:** `&#0;`, `&#xD800;` and `&#1114112;` all become U+FFFD.
- **double-encoded:** `&amp;#8230;` decodes once to a literal `&#8230;`, which gives html-entity only. Under double-decode it gives an extra `words=` ellipsis-joined finding.
- **truncated-encoded:** gives html-entity plus truncated-grounds.
- **overcap-numeric:** gives html-entity plus `words=n`.
- **bare-ampersand:** `&#;`, `&#x;`, `&#xg`, `?a=1&b=2` and a non-html5 `&XY;` give none.
- **named-no-semicolon:** gives none.

The only divergence from HTML5/`html.unescape` is `&copy `/`&reg ` without `;`, where WHATWG decodes legacy names. That is the tool's stated policy ("names bind only with `;`"), so it is not a defect. The docstring should say it departs from HTML5 there (minor, review-only).

## 4. Meetability by honest work and isolating controls (attack d)

`honest.py` (sha256 `4d660fbc…`) is 29 diff lines on the base:

- the `;?` grammar on both numeric alternatives;
- three class cases: `html-entity-decimal-bare-red` (`"caf&#233 two"`), `html-entity-hex-bare-red` (`"caf&#xE9w two"`) and `double-encoded-decoded-once-green` (`"one &amp;hellip; two"`, expected only html-entity);
- two `run()` cases on an [invalid, valid-with-`&copy;`] pair: `continue-past-bad-file-red` (exit 2 and the exact finding plus `GATE_QUOTES: 1 findings`) and `cli-label-html-entity-red` (the exact stdout line ending ` html-entity`).

```
$ python3 -B reports/round-57/accept-o.py --tool /fast/scratch/hyaku/kotodama-r57/CriticClauseListO57/tools/honest.py
# seeds [3062718144, 3062718145, 3062718146, 3062718147, 3062718148]
GEN PASS lessons=5 failing=0 []
MULTI PASS runs=10 failing=[]
MUTANTS PASS unmutated_selftest_exit=0 survivors=[] unpatched=[] exits={'none': 0, 'double-decode': 1, 'stop-at-first-bad-file': 1, 'label-rename': 1}
KEEP PASS changed=[]
FORMAT PASS malformed_runs=[]
SELFTEST PASS exit=0 SELFTEST: 43/43 pass
ACCEPT-O-57: PASS
exit=0
```

The same result holds with `--seed 5700` (exit 0). KEEP is safe for honest work: a grep of `corpus/lessons` for bare numeric references finds only the prose mention at `round-56-verifier-spotcheck.md:161`, and no Gate row in lessons 49-56.

**Isolating near-miss red controls** (each on top of `honest.py`, `--seed 5700`; full output in `out-red-*.txt`). Every one exits 1 with `ACCEPT-O-57: FAIL`, and **only** its own leg fails:

| control | near-miss | failing legs | others |
|---|---|---|---|
| `red-gen.py` | hex keeps the required `;` (decimal-only fix; hex selftest case dropped) | GEN (`missing … 'S841', 'html-entity'`) | 5 PASS |
| `red-multi.py` | when the last path is unreadable, earlier findings are dropped (the selftest tests only invalid-first) | MULTI (`order=bad-last`) | 5 PASS |
| `red-keep.py` | ellipsis-joined prints its class name instead of `words=<n>` | KEEP (`round-52.md`, `round-53.md`) | 5 PASS |
| `red-format.py` | stderr note `large registry` when SOURCES.md has more than 50 lines | FORMAT (all 8 KEEP runs) | 5 PASS |
| `red-selftest.py` | `--selftest` returns `selftest() or run(args.paths)` (exit 2 with no paths) | SELFTEST (`exit=2 SELFTEST: 43/43 pass`) | 5 PASS |

So every clause can fail alone. The committed receipt simply does not show it (B3).

## 5. Findings

**B1 — blocking (O-gen; axes: operability, provenance of the PASS label).** GEN is met by checkers that implement no bare-numeric grammar on real lessons (2a). Fixes to `accept-o.py`, each small:

1. Name each per-seed directory with `tempfile.mkdtemp()` instead of `str(seed)`, and never put the seed in any path, argv or environment the tool sees. This closes the replay.
2. Randomize every constant artefact per seed: the URL host from a random label plus `.example`, the Seat label from the lane's real seat names, the Grounds prefix from random words, the accessed date, the lesson title, and the registry header and source cells.
3. Draw filler words from a word list taken at run time from corpus prose, not from a 14-syllable alphabet.
4. Add one real-row leg: inject a generated bare-numeric reference into a randomly chosen Gate row of a copy of `corpus/lessons/round-55.md` (with its real SOURCES.md copied beside it), and require exactly one extra `html-entity` triple on that row.
5. Commit `seatgen` and `replay` as controls in `controls-o.py`, expected to fail GEN.

**B2 — blocking (O-mutants; axes: operability, false provenance of "selftest kills").** An identity snapshot (6 lines, no behavioural case) meets MUTANTS (2b). Fixes:

1. In `MUTANT_RUNNER`, add three **neutral** patches that rebind each of `decode_html_references`, `check` and `run` to a behaviour-preserving wrapper. Each run of the runner must draw its wrapper's helper names at random, and the selftest must exit 0 under all three, or MUTANTS fails. I tested this scratch-side: the honest candidate gives `neutral-* selftest_exit=0` for all three, and `cheat-identity` gives `selftest_exit=1` for all three.
2. Give the real mutants random helper names instead of `_orig_*`, which defeats the name-keyed variant.
3. Commit `identity` as a control expected to fail MUTANTS.

This turns the review-only residual into a leg that can fail. A deeper cheat that fingerprints wrapper bytecode remains possible, but it costs more than the behavioural cases.

**B3 — blocking for criterion-11 compliance (all O clauses; axis: verifiability).** The receipt `reports/round-57/telemetry/controls-o.txt` has no green control (lines 2, 12, 22, 32, 42, 52 and 62 all show exit 1), and only hashpin (l.42-51) isolates its clause. Fixes:

1. Add a green stand-in control (the `honest.py` shape) that must exit 0.
2. Replace the multi-leg reds for O-gen, O-multi, O-keep, O-format and O-selftest with single-leg near-misses built on the green copy, like those in section 4.
3. Drop "base" from the `red_control` fields for O-gen and O-mutants, since criterion 11 says "the base run does not count as a control".
4. Re-commit the receipt with the instrument sha256s.

**M1 — minor (O-gen wording).** "random HTML5 named references drawn from the whole table" should read "drawn from the 571 letter-valued `name;` entries of the HTML5 table".

**M2 — minor (statement wording).** "its --selftest fails under each … mutant" should read "its selftest() returns non-zero in-process under each … mutant". MUTANTS never runs the CLI flag under a mutant.

**M3 — minor (predicate completeness).** The predicate names FORMAT without its condition. It should add "(the KEEP runs write nothing to stderr, every stdout line is a finding or the summary, and the summary count equals the finding lines)".

**M4 — minor (disclosure).** Named references without `;` are not bound, which departs from HTML5 legacy decoding (`&copy `). The review-only docstring item should require that this departure be stated.
