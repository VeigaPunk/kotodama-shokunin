# kotodama round 98 — non-author verifier spot-check

author: hyaku closure (non-author integrator, @m_zfl)

Closed 2026-11-06. Base `bcf664aa089ddbd1fac85772ed22a38d1b454d23`, freeze `db88f107606aae90efe01344551c7e1ea71cd419`, after `7ff35e6ce6a8027fd04ba4a6bccce179b7286ca3`.
Report: fleet `.ufo/reports/round-98/kotodama.md`. Prompt: fleet `.ufo/prompts/kotodama-round-98.md`.

Driver digest (copied from the mutable `.ufo/watchdog.log`):

```
2026-11-05T22:16:28-03:00 launch kotodama round=98 pgid=3621976 driver=hyaku-inline attempt=1
2026-11-05T23:31:14-03:00 lane-dead-no-report kotodama round=98; retry same round (hyaku-inline attempt=1: L1 ended without a landed report: FAIL report_of (missing, unchanged, no SHONEN heading, or < 400B): .ufo/reports/round-98/kotodama.md)
2026-11-05T23:31:17-03:00 launch kotodama round=98 pgid=2173056 driver=hyaku-inline attempt=2
2026-11-06T00:51:30-03:00 complete kotodama round=98; hyaku-inline attempt=2
```

## 1. Step-1 conformance — pass

- `git log --format='%an %H' -- .ufo/reports/round-98/kotodama.md` (fleet repo) → `kotodama-shokunin 97b6ec0ad800868b31ced7464eaf87bb174bd93e` (2026-11-06 00:51:09 -0300). The report was committed by the lane identity.
- `## SHONEN` heading is present with 4 `[~]` lines, matching the 4 boxes in `SHONEN.md` (`grep -c '^- \[' SHONEN.md` → 4). No box is `[x]`.
- The cited commits are `bcf664aa…`, `db88f107…` and `7ff35e6c…`. For each, `git cat-file -t` → `commit` and `git merge-base --is-ancestor <hash> main` → ok.
- `git log bcf664aa..7ff35e6c` shows two commits, both authored by `kotodama-shokunin <kotodama@shokunin.local>`.
- `scripts/hyaku/jj-lane.sh state …` → `branch=main local=7ff35e6c… remote=7ff35e6c… ahead=0 behind=0 head=detached tracked=0 untracked=0`.
- `git status --porcelain` → 0 lines. `git ls-remote origin refs/heads/main` → `7ff35e6c…`.
- The prompt carries the template contract: §§1–5 of `templates/round-prompt.md` plus hyaku addendum §6 (`grep -n '^## '` on the prompt).
- Attempt 1 died with no report. Attempt 2 reused its outputs after re-verifying them, and the report says so (§Routing). This is not a defect.

## 2. Claims

The frozen counter is `reports/round-98/predispatch.py`. The control `predispatch-base.txt` → `PREDISPATCH-98: FAIL legs=5/15`, and the landed run `predispatch-lands.txt` → `PASS legs=15/15`. Both are committed evidence, verified by reading.

### Claim O (operability, grader v9 → v10)

The frozen predicate is met. The harm is measured.

Re-measured by me:

- `git show bcf664aa:tools/check-advance-evidence.py | sha256sum` → `1021dc9d…717b`.
- `git show 7ff35e6c:tools/check-advance-evidence.py | sha256sum` → `d35b13c9…16af7`.
- O0 agrees: the two hashes differ.
- `sha256sum reports/round-98/controls/battery98.py` → `cdb77c4b…968b`, which equals `battery98.sha256`. The battery is in freeze commit `db88f107` (`git show --stat db88f107`).
- `sha256sum .ufo/waves/round-98/w1/stage/MutationTester98/mutants98.py` → `dd88caec…efb0f`, which equals `mutants98.sha256`.
- `git diff bcf664aa 7ff35e6c -- tools/check-advance-evidence.py` shows the heading check changed from `unicodedata.category(_c) in ('Mn','Me')` to `unicodedata.category(_c)[0] == 'M'` (line 742). The v10 comment above it still says "Mn/Me", so the docstring has drifted from the code.
- The same diff shows `_nonascii_number` contains a dead disjunct, `any(... for p in [])`. This confirms ReviewerO98b F2.
- Lane exposure: a Python census over `git show 7ff35e6c:` of the 270 `corpus/knowledge/**/*.md` files → `h2 3010 Mc 0 nonascii-numeral-only 0`. This matches the report's 0/3010.

Verified from committed evidence only. I did not run the gate (PROTOCOL §Gate standard, Closure consequence):

- O1: `SELFTEST PASS 161/161`, with absolute `--work` (`w1/ExecGraderV10.md` line 12; `predispatch-lands.txt` O1).
- O2: battery98 `0/0/36/0/3/0`, against v9 `survivors=5 refused=31` (`controls/battery98-control-v9.txt`).
- O3: `MUTATION-SCORE: 128/128 killed, 0 survived, 0 broken-pattern` (`controls/mutation98-first.txt`).
- O4: REG 34/34.
- O5: critic97 replay `survivors=8` → `3`, with all five named forgeries refused (`controls/critic97-on-v9.txt`; `predispatch-lands.txt`).

Harm finding:

- Two non-author seats measured the same regression independently: ReviewerO98b F4 (`w2/ReviewerO98b.md`) and CriticO98b OK-MCWORD (`w2/stage/CriticO98b/attacks.md:104,151`). An h2 heading carrying a Mc spacing mark (U+0903) is CLEAN on v9 and is refused `HEADING-COMBINING` on v10.
- The code diff above confirms the mechanism. Mc covers ordinary Indic vowel signs, for example U+093E. A heading such as `## राम …` contains only Mc marks and no Mn mark, so v9 accepts it and v10 refuses it. For a linguistics lane, that is a real input class.
- F1 adds a second new false-refusal branch (`HEADING-NUMBER` on a bare `## Ⅳ.`). That heading protects nothing.
- Current exposure in the corpus is 0. The harm is still a new false-refusal surface on valid input, and it is not netted against the five closed forgeries. This follows AXES.md ("a trade anywhere is not an improvement") and the precedent of the chousa r27 and r47 closures.
- **Operability: harmed.**

### Claim C (coverage, toast and drinking-speech formulae entry)

The claim verifies. All of the following were re-measured:

- `git show 7ff35e6c:corpus/knowledge/linguistics/toast-drinking-speech-formulae.md | wc -c` → 47760. `grep -c '^## '` → 13. At base `bcf664aa` the path is absent (`fatal: … not in 'bcf664aa'`).
- `grep -c -E '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 917 at base and 930 at after. The highest id went from S993 to S1006.
- The SOURCES.md diff shows one in-place line (S992) and 14 added rows, S994–S1006, with S992 re-added in its new form.
- Citation counts in the entry (`grep -o 'S…' | uniq -c`) are S995 3, S996 4, S997 4, S998 4, S999 8, S1000 3, S1001 4, S1002 5, S1003 5, S1004 5 and S1006 7. All 11 qualifying ids are cited. S994 is no longer cited, because S1006 superseded it.
- `grep -c toast-drinking-speech-formulae corpus/README.md` → 2.
- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok … corpus/SOURCES.md`, rc 0. Every W01/W04 warning is on a pre-existing row, S127–S928; none is on S994–S1006.
- Repair sample (the report asked closure to sample line 142 and §8):
  - I re-opened S999 (Tuite PDF, HTTP 200, 6 pages) and ran `pdftotext`.
  - Each of these phrases has `grep -o -F` count 1 in the flattened text: "conspicuously absent", "are not attested before the 19th century", "even if only two men are present", and "after which he". Line 142 is supported.
  - The §8 preamble tags proposal cells *(design)* and restricts untagged cells to grounded lines. The marking is honest.
  - `grep -n -i oceanic` on the entry → no hit. The CriticC98 F1 fix is present: the word survives only in the superseded S994 row.
- Oath-repair sample: the S978 quote "sharing characteristics with curses of the conditional type" has `grep -c -F` count 1 in `reports/round-96/evidence/S978.txt`.
- **Coverage: improved.**

### Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| operability | harmed | Frozen O0–O5 are met. v10 adds two new false-refusal surfaces on valid input, Mc headings (F4) and bare non-ASCII-numeral headings (F1); this is a trade, not netted |
| coverage | improved | Claim C was re-measured as above |
| depth | unchanged | The oath repairs are not a claim (observation only) |
| freshness | unchanged | Paused by L0 (round-11, round-89). Not met and not waived |
| calibration | unchanged | Gate-capture checker and QUALITY criterion 40 (observation, not a claim) |
| adjacency | unchanged | No move. ConnectorOverlap98 found 0 sibling claims |

## 3. Discernment spot-check

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S1001 Open Encyclopedia of Anthropology, Feasting | admit (B) | `curl -sL https://www.anthroencyclopedia.com/entry/feasting` → 200, 84274 B | agree | The quote head "Toasting, which links two uses of the mouth" is present. This is a scholarly reference entry, and tier B fits |
| S999 Tuite, Autocrat of the Banquet Table | admit (B) | `curl -sL …/Tuite-supra.pdf` → 200, PDF of 6 pages | agree | The Gate quote "The order of toasts, especially in the opening phase of" has count 1, and the line-142 quotes have count 1 each |
| S1002 Geoffrey of Monmouth, Giles transcription (SOURCES.md row) | admit (B) | `curl -sL https://www.melocki.org.uk/monmouth/History.html` → 200 | agree | The ≤25-word quote "Your answer to her must be 'Drinc heil'" (8 words) is present verbatim. This is an amateur-hosted transcription of a public-domain translation, and tier B fits |
| C18 Pace Law Review | reject (403) | `curl -sL 'https://digitalcommons.pace.edu/cgi/viewcontent.cgi?article=1326&context=pilr'` → 403, 5610 B | agree | Still walled. The flip ("an open copy") is right |
| C14 Gutenberg 981-0.txt | reject (404) | `curl -sL https://www.gutenberg.org/files/981/981-0.txt` → 404 | agree | Still 404. The same text is admitted at cache/epub/981 (S1000) |
| C2 Ynglinga saga ch. 41 | reject (wrong chapter) | candidates.md row C2 → `…/Ynglinga_saga/41`. I re-opened sibling C4, ch. 35 → 200, `grep -c -i -E 'bragaf|bragarf'` 0, `heit` 0 | agree | No toast, cup or oath text, so the reject is sound |

The spot-check agrees with the gate on all 3 admits and all 3 rejects.

## 4. Trend verdicts

- **expansion: improved.** A ground with no owner at base (C8 owners 0 of 269) now has an admitted entry. Its citations are 11 `mined` tier A/B rows, and census rc is 0.
- **quality: improved.** The S992 tier error is superseded by S1005. Eight unsupported or contradicted sentences in the oath entry now rest on located quotes; I re-verified a sample (S978, count 1). The 3 weak lines that remain (L49/L51/L53) are marked and routed, not left unmarked.
- **discernment: improved.** The non-author spot-check agrees with the gate on admits and rejects (LEARNING.md row). The author's own verdict was `unchanged`, but the grader over-refusals it cited are graded under operability, not under gate discernment.

## 5. Ruling

The status is ok. The claims verify on their frozen predicates, but operability is harmed. **Admitted: false (`rejected-harmed`).**

## 6. Routed defects (lane fixes next round)

1. F4: restore the v9 `Mn/Me` heading check, or add a benign selftest twin with a Mc heading (U+093E/U+0903) that must stay CLEAN. Fix the docstring at `:735-741`, which says "Mn/Me" while the code checks all M.
2. F1: remove the `HEADING-NUMBER` loop, or pin a benign twin (`## Ⅳ.` paired with a real heading). Also remove F2, the dead `for p in []` disjunct in `_nonascii_number`.
3. F3: pin the load-bearing but unpinned branches that ReviewerO98b identified with selftest cases.
4. CriticO98b's 24 survivors (verdict-window whitelist, list-mark stripping) stay open.
5. Oath entry weak lines L49/L51/L53.
6. SOURCES.md: S994 was added and superseded in the same round, which left a dead `queued` row. Prefer correcting before landing, without a self-superseded row.
