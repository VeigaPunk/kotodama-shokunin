# CriticClaimSizingC — round 52 claim sizing (C, with D)

Seat: `KotodamaR52.CriticClaimSizingC` (critic, leaf). Author-lane advice, not admission.
Read at lane `main` = `dea5ece` (claims declared at `d9f73c8`, base `147cfde`), 2026-10-22.
Nothing in the lane was written except this report. No installs, no network.

## Result

- **C's statement is wider than its acceptance command in four clauses.** Those clauses are "one new entry", the topic clause, "indexed in corpus/README.md", and the cited-set when ranges or draft ids are used.
- **A hollow C passes the declared acceptance.** The hollow version is a one-line entry carrying one S-id, plus one skeletal SOURCES row, with `corpus/README.md` untouched.
- **The `grep -q '"total": 228'` leg checks nothing beyond the file count.** It matches the sweep's `footer_live` line, which is computed from the files on disk. The `|` pipe also throws away the sweep's own exit code, which is the only part that reads the index.
- **D's statement is sized correctly, in the safe direction.** It re-derives from committed bytes: 0 lines contain `S094` at `dea5ece`. Its counter would also read 0 on an emptied file. That case is excluded by D's falsifier review clause, not by the command.
- **The draft lesson's claim about round 52 is false for C.** `corpus/lessons/round-52.md:17` says C's statement "lists only clauses its acceptance command checks". That is the round-51 defect (`round-51-verifier-spotcheck.md:44-49`, `:123`) recurring. Replacement wording is below.

Axes: coverage (C), depth (D), calibration (the lesson's self-description). Everything here is a fixable defect, not a tradeoff that requires rejection. The declaration is frozen. The fix is for the closure to re-derive the unchecked clauses with the commands listed below, and for the lesson to describe the gap honestly. If C lands with substance, it can still verify. If it lands hollow, only the falsifier's review clause and these closure commands will catch it.

## 1. The sweep leg: `python3 -B reports/round-28/readme/sweep.py | grep -q '"total": 228'`

The sweep prints two lines that both contain `"total": N`:

- `footer`: the README's own counts-footer, as declared and parsed from the README (`sweep.py:107-117`).
- `footer_live`: the live value, `{"total": total_files, ...}` (`sweep.py:207-208`, rendered at `:230`). Here `total_files` is the number of `*.md` files on disk under each README-sectioned partition (`sweep.py:126-158`).

So `grep -q` succeeds as soon as `footer_live` reads 228, and that happens whenever the disk holds 228 top-level files in the six sectioned partitions. That is the same fact `test "$n" -eq 228` has already checked. The sweep's real index predicate is `ok`: 0 missing rows, topic equality, footer equal to live, and totals line equal to live. That decides its exit code (`sweep.py:191-194`, `:427`). In POSIX `sh`, a pipeline's status is the status of its last command, `grep`, so the sweep's exit code is discarded.

I simulated this in memory: real README, a 228th linguistics file injected through a patched `disk_files`, nothing written.

| README state | sweep `ok` / exit | `missing_from_index` | lines matching `"total": 228` | leg result |
|---|---|---|---|---|
| untouched (no row, footer 227) | False / 1 | `['linguistics/speech-surrogates-whistled-drummed.md']` | `footer_live` | **pass** |
| only the footer edited to 228 | False / 1 | same | `footer`, `footer_live` | **pass** |

**Is this as intended?** The statement says "indexed in corpus/README.md (sweep footer total 228)". Two readings are possible, and both fail:

- If "sweep footer" means the README's `footer` line, the grep is mis-aimed, because `footer_live` satisfies it first.
- If it means `footer_live`, the leg restates the file count.

Neither reading checks a README row. The only extra thing the leg adds is that every counted file sits top-level in a sectioned partition.

**Smallest correction** (for future declarations): drop the pipe and test the sweep's exit code, `python3 -B reports/round-28/readme/sweep.py >/dev/null`. Exit 0 already implies 0 missing rows, an exact topic match, the README footer equal to live, and the totals line equal to live.

## 2. A hollow entry passes

I ran the declared python leg (`separability-manifest.json`, C `acceptance[3]`) in memory, with `open()` patched to serve a fake entry and the real `corpus/SOURCES.md` plus the appended rows. Nothing was written.

| case | output | exit |
|---|---|---|
| H1: entry `S134`; row `\| S134 \| x \| … \| <entry path> \|` | `C_SID_BAD 0 [] cited 1` | **0** |
| H2: entry cites `NEW-ScoutGapSurrogate-1`, `-2` and `S134` | `C_SID_BAD 0 [] cited 1` | **0** |
| H3: entry `(S134–S139)`; only rows S134 and S139 exist | `C_SID_BAD 0 [] cited 2` | **0** |
| H4: row with tier C, status `queued`, opened `2026-01-01`, source `Wikipedia` | `C_SID_BAD 0 [] cited 1` | **0** |
| H5: entry with author-year only, no S-id | `C_SID_BAD 0 [] cited 0` | 1 (the `not ids` guard works) |

Put together, the three legs pass with:

- a one-line file at the named path, so `find` reads 228;
- `corpus/README.md` untouched, which passes per §1;
- one skeletal SOURCES row whose `used-by` cell contains the path.

Each leg was observed passing separately. The end-to-end chain is `[INFERENCE]` from `&&` composition; I did not run it on disk because writing files is outside my bounds.

H3 matters in practice. Both model entries write their shelf as a range in the head block: `sign-languages-manual-modality.md:7` and `:9` (`S071–S122`), and `pastoralism-animal-husbandry.md` (`S048–S069`). A C entry that copies the model will write `S134–S1xx`. The regex sees only the two endpoints, so middle rows are never checked for existence or for the entry in `used-by`. A range that spans all round-52 rows would also "cite" rows C does not use, such as a mined-mistake row.

What the leg does check correctly: every 3-digit `S\d{3}` token. This is stricter than "cites" because it also catches mentions. Each token must be at least S134, be a SOURCES row, and have the full path as a substring of field 11 (`used-by`). Field 11 is the right column: all 133 rows split into 13 fields, no row contains an escaped `\|`, and the 93 non-`—` `used-by` cells use the full `corpus/knowledge/...` path form.

## 3. Clause-by-clause: is each statement worded to its command's predicate?

Against the round-51 ruling (`round-51-verifier-spotcheck.md:44-49`: "the counter's `resolved` test … checks a weaker predicate", "the statement was wider than its own measure from the moment it was declared"), the routed item (`:123`: "word future statements to the counter's actual predicate"), and the prompt rule (`.ufo/prompts/kotodama-round-52.md:342-350`):

| claim clause | what the declared command actually checks | exact? |
|---|---|---|
| D "has 0 lines that cite S094" | lines containing the byte string `S094`, which includes mentions as well as citations | **Safe-wide.** The counter's set contains every citing line, so 0 rules out any citing line. |
| D (implicit: the entry still exists with its rows) | nothing; `/dev/null` substituted for the path gives `S094_lines=0`, exit **0**; a missing file fails safe (awk fatal, `test: integer expected`, exit 2) | **No.** An emptied entry passes. Excluded only by the falsifier's review clause. |
| D falsifier "citing an S-id from S134 upward" | the acceptance's `! grep -qE '\bS(13[4-9]\|…)\b'` | exact |
| D (method) re-cite only to rows that carry the detail; no rejected row | nothing. S132 (the rejected Battison 1974 row) is below 134, so citing it passes D's acceptance. Only `tools/check-source-access.py` flags it (S132 is one of its 2 flagged rows), and that tool is not in D's acceptance. | **No.** Closure-only. |
| C "Knowledge files go from 227 to 228" | `find corpus/knowledge -name '*.md' \| wc -l` = 228 | exact |
| C "one new entry, `<path>`" | the count is 228 and the named path opens | **No.** A net count of 228 is also reached by adding two files and removing one. The separability dynamic leg overlays only the lands onto base, so it does not see this either. |
| C "on speech surrogates … as conlang and worldbuilding method" | nothing | **No.** Review only. Not declared as such. |
| C "indexed in corpus/README.md (sweep footer total 228)" | `footer_live` 228, which equals the disk count (§1) | **No.** No README row and no README footer is checked. |
| C "every S-id it cites is S134 or above" | every 3-digit `\bS\d{3}\b` token | Exact for literal tokens. **Wider** for range notation (H3). Draft `NEW-…` ids are invisible (H2). |
| C "… and is a corpus/SOURCES.md row" | `^\| S\d{3} ` row key; duplicate ids collapse to the last row | Exact, provided ids are unique (unique at base: 133 rows) |
| C "… whose used-by cell names the entry" | full path is a substring of field 11 | exact |
| C falsifier: criterion 10 | not in the acceptance; `tools/check-source-access.py` exists (currently `ACCESS: 2 flagged rows, 0 findings`, exit 0) | **No.** Closure-only. The checker only sees self-disclosed bypass notes (its `BYPASS` regex runs over the source, anchor and teaches cells). |
| C must-not-cite "sign-languages … lines changed by D" | nothing. That file exists at base, so the separability land-path leg ignores it, and D exports `[]` | **No.** Closure-only. |
| C and D must-not-cite `corpus/lessons/round-52.md` | the separability static leg. The `y` loop includes record units (`check-claim-separability.py:621-633`), and the path is absent at base | exact |
| entry contract: at most 250 lines, eight-field head, H2s ending Recheck then Scope, zero H3, `DR-SRG-`, NON-CANON | not in the statement and not in any command | Out of the claim, so it is not a sizing defect. But nothing gates it. |

Against §9's first bullet ("one concrete value … one command over committed bytes"): D meets it once the command is pointed at committed bytes. C's after-value, "228, with the acceptance command exiting 0", is one value plus a compound gate, and the gate certifies less than the statement says. Against the second bullet (no universal clause unless the command enumerates the full set): C's "every S-id it cites" is enumerated in full only when no ranges or draft ids are present.

## 4. Re-deriving each clause from committed bytes (closure)

The declared argv runs against `WORKTREE` with paths relative to cwd. The sweep finds its lane from `__file__` (`sweep.py:44-47`). So export first, then run everything inside the export: `git archive <head> | tar -x -C X && cd X`.

**D** (observed now at `dea5ece` with `git show`):

- `git show dea5ece:corpus/knowledge/linguistics/sign-languages-manual-modality.md | awk '/S094/{n++} END{print n+0}'` gives **0**.
- The same file piped to `grep -cE '\bS(13[4-9]|1[4-9][0-9]|[2-9][0-9][0-9])\b'` gives **0**.
- Piped to `grep -cE '\bS13[23]\b'` gives **0**.
- `wc -l`: 224 at `147cfde` and 224 at `dea5ece`, so the entry was not emptied. The diff is 5 lines changed in place (lines 83, 87, 90, 92, 93).
- `python3 -B tools/check-source-access.py` gives exit 0, 2 flagged rows, 0 findings (worktree; D's file is unchanged since `dea5ece`).
- Still a review item: each re-cited detail is present on S096 or S097 when re-opened. The lesson Gate (`round-52.md:34-35`) quotes NAME/SHORT, CHAIR/NAME, "fourth phonological parameter" and "Out of the 45 possible handshapes". That is CriticClaimD's job.

**C** (to run at C's head):

1. Count: `find corpus/knowledge -name '*.md' | wc -l` gives 228.
2. One new entry: `git diff --name-status --diff-filter=ADR 147cfde <head> -- corpus/knowledge` prints exactly one line, `A corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`.
3. Indexed:
   - `python3 -B reports/round-28/readme/sweep.py; echo $?` exits **0** with `missing_from_index 0`, `topic_mismatch 0`, `totals_line 228`, and `footer {… "total": 228, "dir_totals": [27, 26, 28, 29, 24, 94]}`.
   - `grep -c '^- `speech-surrogates-whistled-drummed.md` — ' corpus/README.md` gives 1, under `## linguistics/ (27)`.
4. S-ids:
   - The declared python leg, then expand every range: `grep -oE 'S[0-9]{3}[[:space:]]*[–-][[:space:]]*S?[0-9]{3}' <entry>`. Every member must be a row with the entry in `used-by`.
   - `grep -cE 'NEW-[A-Za-z0-9]+-[0-9]+' <entry> corpus/SOURCES.md` gives 0 for both files.
   - `grep -oE '^\| S[0-9]{3} ' corpus/SOURCES.md | sort | uniq -d` prints nothing.
5. Row substance: no command declares this. For each cited row:
   - `status` is `mined`, `opened` is `2026-10-22`, and the source cell holds a URL.
   - The tier fits criterion 6, and a C-tier row is never the sole support.
   - The lesson Gate quote is at most 25 words, with its location.
   - `python3 -B tools/check-source-access.py` exits 0.
   - `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` prints `ok`.
6. Criterion 10 on undisclosed routes: re-open each cited URL by a plain request, `curl -sS -A 'Mozilla/5.0' -D- <url>`. Expect HTTP 200 with no `cf-mitigated` header, and the quote present.
7. Must-not-cite and one-way:
   - `grep -cE 'sign-languages-manual-modality\.md|round-52\.md' <entry>` gives 0.
   - The entry carries `phonetics-phonology.md:197`, `music-instrument-lexicon.md:98`, `orality-formulaic-language.md:114`, `:124` and `sound-symbolism.md:121`.
   - `git diff --quiet 147cfde <head> -- corpus/knowledge/linguistics/phonetics-phonology.md corpus/knowledge/culture-material/music-instrument-lexicon.md corpus/knowledge/linguistics/orality-formulaic-language.md corpus/knowledge/linguistics/sound-symbolism.md` exits 0.
8. Topic and contract (review, stated as review):
   - `wc -l` is at most 250.
   - `grep -c '^### '` gives 0.
   - The last two H2s are Recheck and then Scope.
   - The eight head fields are present.
   - `NON-CANON` and `DR-SRG-01` are present, and the handoff names lore-shokunin.
   - A reader confirms the subject is speech surrogates, including horns, reed pipes, xylophones, jaw harps and gongs, and the signal-code boundary.

## 5. Wording fixes for the lesson (the declaration stays frozen)

Replace the disposition cell of row "1. D statement wider than its counter" at `corpus/lessons/round-52.md:17` with:

> Not repaired in the pastoralism entry (its `civilizations/` row stays a directory row). Only D was worded to its command. D's statement ("0 lines that cite S094") is checked by a wider predicate, lines containing the string `S094`, so a 0 cannot hide a citing line; the same counter also reads 0 on an emptied file, which D's falsifier review clause excludes, not the command (`dea5ece` keeps all 224 lines). C was not: its statement is wider than its acceptance command in four clauses. "One new entry" is checked only as a file count of 228 plus the named file opening. The topic clause is checked by no command. "Indexed in corpus/README.md (sweep footer total 228)" is not checked: `grep -q '"total": 228'` matches the sweep's `footer_live` line, which the sweep computes from the files on disk, and the pipe drops the sweep's exit code, so an entry with no README row passes. "Every S-id it cites" is enumerated in full only for literal three-digit ids, not for ranges such as `S134–S140` or draft `NEW-…` ids. Those clauses are re-derived at closure by the commands under "Closure checks", not by the declared acceptance.

Candidate mined mistake (numbering is the L1's):

> **Round 52: a pipe hid a check.** The C acceptance ran `sweep.py | grep -q '"total": 228'`. The pattern matches the sweep's live disk count as well as the README's footer, and `sh` returns `grep`'s status, not the sweep's. The leg therefore only repeats the file count, and the "indexed" clause went unchecked. Rule: never pipe a checker into a pattern match for a pass/fail leg. Use the checker's own exit code (`sweep.py >/dev/null`), or parse its `--json` and assert the named field (`footer.total`, `missing_from_index`).

Rule addition for the next declaration (claim-sizing addendum, lane side):

> Before declaring, take each clause of the statement and name the command term that fails when only that clause is false. A clause with no such term is moved to the falsifier as a named review item, or cut. The receipt names one hollow control per claim (for example, a one-line entry with one row) and shows that the acceptance fails on it.

## 6. Falsifiers for wave 2

Any of these refutes "C verified" even when the declared acceptance exits 0:

1. `git diff --name-status --diff-filter=ADR 147cfde <head> -- corpus/knowledge` shows anything other than the single `A` line for the entry.
2. `python3 -B reports/round-28/readme/sweep.py` exits non-zero at C's head, or its `footer` (not `footer_live`) total is not 228.
3. The entry contains an S-id range with a member that is missing from SOURCES or lacks the entry in `used-by`, or it contains any `NEW-<Seat>-<n>` token.
4. A cited row is not `mined`, is not opened `2026-10-22`, or has no URL. Or `tools/check-source-access.py` exits non-zero. Or a cited URL returns a challenge (`cf-mitigated`) to a plain request.
5. The entry names `sign-languages-manual-modality.md` (any line D changed) or `round-52.md`. Or any of the four partial-owner files differs from base.
6. The entry exceeds 250 lines, or has an H3, or lacks the closing Recheck and Scope H2s, NON-CANON or `DR-SRG-01`.
7. The lesson still says C's statement "lists only clauses its acceptance command checks".

For D:

8. `git show <head>:…/sign-languages-manual-modality.md` has fewer lines than base (224) without a recorded cut.
9. The entry cites S132 (caught by `tools/check-source-access.py`, not by D's acceptance), or carries a bare "Battison 1974" without an inline `(to-verify)`.

## Unrun checks

- The C closure checks (§4) cannot run until C lands.
- No URL was re-opened; that belongs to the source seats and the closure.
- The end-to-end hollow-C chain was inferred from three legs observed separately, not run on disk.
- The separability checker and `dry-run.py` were not run.
