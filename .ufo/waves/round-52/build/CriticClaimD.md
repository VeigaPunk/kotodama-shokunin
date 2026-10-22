# CriticClaimD — round 52, attempt 1: attack on claim D (depth, landed `dea5ece`)

Seat: KotodamaR52.CriticClaimD (critic, leaf). Axis judged: depth. Lane HEAD `dea5ece63ca4372c41766ab242df1e26c2e6898a`; the worktree copy of the entry equals HEAD (`git diff --stat HEAD -- <entry>` is empty). Advice to the author lane, not admission. No tools installed.

## Verdict

The count holds and the change is a repair, not a deletion. All five former S094 lines are still present, and every detail is now either re-cited to S096 or S097 (both re-opened by plain `curl`, HTTP 200), marked `(to-verify)`, or cut. **One fixable depth defect:** on line 87, D dropped the page's "Type-3" qualifier. As a result the entry now says something S097's own page contradicts. Strictly read, that meets the third clause of D's falsifier for one line. A four-word edit repairs it. There is also one low-severity over-attribution on line 93. Neither is a tradeoff the judge has to reject; both are wording slips with a direct correction below.

## 1. Commands run at the lane root

Counting command:

```
$ awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md
0
```

D's acceptance argv from `reports/round-52/separability-manifest.json`, run through `subprocess.run(argv)`:

```
argv ['sh', '-c', 'n=$(awk \'/S094/{n++} END{print n+0}\' corpus/knowledge/linguistics/sign-languages-manual-modality.md); echo S094_lines=$n; test "$n" -eq 0 && ! grep -qE \'\\bS(13[4-9]|1[4-9][0-9]|[2-9][0-9][0-9])\\b\' corpus/knowledge/linguistics/sign-languages-manual-modality.md']
stdout 'S094_lines=0\n'
stderr ''
rc 0
```

Access checker: `python3 -B tools/check-source-access.py` printed `ACCESS: 2 flagged rows, 0 findings` and exited 0.

Mutation check of the acceptance argv. Each case ran on a copy of the entry under `/tmp/ccd/mut`; the lane was not touched.

| Injected line | rc | Expected |
|---|---|---|
| none (control) | 0 | 0 |
| `(S094)` | 1 | 1 |
| `(S134)` | 1 | 1 |
| `(S200)` | 1 | 1 |
| `(S999)` | 1 | 1 |
| `(S133)` | 0 | 0 |
| `S1340` (not an id) | 0 | 0 |
| `Battison 1974 counts six passive shapes` | 0 | not covered by the command |
| `speech-surrogates-whistled-drummed.md` | 0 | not covered by the command |
| `corpus/lessons/round-52.md` | 0 | not covered by the command |

The acceptance command enforces the counter and the S134+ ban. It does not enforce the two path bans in `must_not_cite`, and it does not catch reliance on Battison 1974 by author and year. I checked those by hand in item 4.

## 2. Repair or deletion: every detail that lost S094

Base lines come from `git show 147cfde:<entry>`; current lines are from the lane worktree. The page evidence comes from my own plain-`curl` re-open on 2026-10-22: S096 is `http://www.cslds.org/apsl-consortium/sign-linguistics/6-phonetics-and-phonology-minimal-pairs/` and S097 is `http://www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition/`, both HTTP 200 with no challenge.

| Line | Detail at base (S094) | Now | On the page? |
|---|---|---|---|
| 83 | three Stokoe parameters (S071, S094) | S071, S096 | yes. S096: "Stokoe argued that the handshapes, locations and movements in his model are all phonemes". Tab, dez and sig come from S071. |
| 83 | palm orientation as a parameter (S094) | "which Battison (1978) proposed as a fourth parameter (S096)" | yes. S096: "Battison (1978) proposed that palm orientation should be added as the fourth phonological parameter in ASL" |
| 83 | minimal pairs differ in one parameter (S096, S094) | S096 only | yes. S096: "In a minimal pair, the two words are basically identical, except for one difference." |
| 87 | "about 45 handshape primes in ASL, not all of them contrastive (S094)" | "the CSLDS module, reporting Battison 1978, counts 45 possible handshapes in ASL, of which only 7 can serve as the passive hand (S097)" | **only in part, see the defect below.** "not all of them contrastive" was cut. |
| 90 | "Battison treats it as a fourth aspect (S094)" | "Battison (1978) adds it as a fourth parameter, with the ASL pair CHAIR/NAME (S096)" | yes. S096: "the examples given by him were CHAIR and NAME" |
| 92 | "six shapes in Battison 1974 (S094)" | seven shapes (A, S, B, 5, G, C, O), 1978 (S097), plus "an earlier, smaller 1974 set is not checked here (to-verify)" | the seven shapes are on the page: "A, S, B, 5, G (i.e., 1), C and O" (Battison 1978, p.206). The 1974 remnant carries an inline `(to-verify)`, which D's method allows. |
| 93 | APPLE/ONION, CAR/WHICH, OFFER/MAYBE, SHORT/TRAIN (S094) | APPLE/ONION, CAR/WHICH, NAME/SHORT, CHAIR/NAME, "after Battison 1978 (S096)" | the pairs are on the page. OFFER/MAYBE and SHORT/TRAIN were cut, and each of the four parameters still has one ASL pair. **Over-attribution, see below.** |

Result: it is a repair. Every cell still carries its point, two details were cut (the "not all contrastive" clause and the 1974 pairs), and no cell was emptied. The round-52 lesson's gate quotes (`corpus/lessons/round-52.md:34-35`) match what I found on the pages.

## 3. Does the statement match the counter's predicate exactly?

The statement says "0 lines that cite S094". The predicate counts lines that contain the substring `S094`. The two differ in two ways:

- A line could mention S094 without citing it (for example "S094 was rejected"). The counter would count it. For a target of 0 this makes the counter stricter than the statement, which is the safe direction.
- A line could rely on Battison 1974 by author and year or by the Gallaudet URL. The counter would not count it, and my mutation row confirms that. I checked the tree for this: `rg -n 'Battison|1974|gallaudet|Phonological Deletion|S0?94\b'` returns only lines 83, 87, 90, 92 and 93. Every Battison mention is to 1978, sourced through S096 or S097, except the 1974 remnant on line 92, which is explicitly marked `(to-verify)` rather than cited.

So the statement and the predicate agree at this tree. The words "lines that cite" and "lines containing the substring" differ only in the strict direction. This is consistent with `corpus/lessons/round-52.md:17`.

## 4. Did D cite S134 or above, the speech-surrogate entry, or `corpus/lessons/round-52.md`?

No. `rg -n 'speech-surrogate|round-52|S1(3[4-9]|[4-9][0-9])' <entry>` matches nothing (rc 1), and the acceptance grep for S134 and above passes. The commit changes only the entry: `git show --stat dea5ece` shows 1 file, 5 insertions and 5 deletions.

## 5. Did D harm depth anywhere?

**Defect, fixable (falsifier clause 3 in letter, line 87).** D replaced the S094 detail with a statement drawn from S097 but dropped the page's scope. S097 says:

> "Out of the 45 possible handshapes in ASL, only 7 can appear as the passive hand of a Type-3 two-handed sign." (unheaded paragraph after the Type 1–3 list, same paragraph as `corpus/SOURCES.md` S133's anchor)

The entry says "of which only 7 can serve as the passive hand", with no qualifier. The same page gives the counterexample:

> "In Type 2 signs, the two hands have the same handshape, but only one hand is moving." (section Type 2; the example listed is NAME (ASL))

In a Type-2 sign the passive hand copies the active handshape, so it is not limited to the seven. The entry's own minimal-pair sign NAME (line 93) is the page's Type-2 example. [INFERENCE] NAME is usually described with H handshapes, which are outside A, S, B, 5, G, C, O; I did not check this against a source this session. The lesson's gate quote (`corpus/lessons/round-52.md:35`) keeps "of a Type-3 two-handed sign", so the qualifier was lost between the quote and the entry. Impacted axis: depth (a true, scoped detail became an overgeneralized one). The counter result is not affected.

**Low: over-attribution (line 93).** "the ASL pairs the CSLDS module lists, after Battison 1978 (S096)" credits all four pairs to Battison 1978. The page tags CAR, WHICH, NAME and SHORT with "(Battison, 1978)", and the orientation pair to Battison (1978) in prose. It lists "ONION – ASL" and "APPLE – ASL" without any attribution.

**Low: unsourced attribution (line 87).** "reporting Battison 1978" is attached to the 45-handshape count. The page's sentence with 45 has no citation of its own; the 1978 attribution is inferred from the sentence before it ("(1978, p.207)"). "The CSLDS module counts 45" is fully supported.

**Not harm, but noted:**
- The cut clause "not all of them contrastive" rested only on S094, so cutting it is allowed by D's method. The fact that replaced it (the passive-hand limit) supports the dominance condition, which line 92 already covers, rather than the row's own point about contrastive inventory. The row's point now rests on S071 (dez) alone. This is a mild loss of relevance, not of truth.
- OFFER/MAYBE and SHORT/TRAIN were cut and replaced by pairs the page carries, so the one-pair-per-parameter coverage is unchanged.
- Line 92's `(to-verify)` has no backticks, while the entry's other 12 marks do. `tools/gates/provenance-audit.py:79` matches `to-verify` either way, and 77 knowledge files use the plain form. This is cosmetic.
- The entry still cites S097, whose anchor names a section the page does not have. S133 supersedes that locator. This is a separately routed defect (`corpus/lessons/round-52.md:19`), not D's; the content S097 is cited for is on the page.
- `rg` finds no restatement of the removed details (OFFER/MAYBE, SHORT/TRAIN, "handshape primes", "fourth aspect", the six-shape set) anywhere in `corpus/knowledge` or `corpus/README.md`.

## Falsifier results

| Falsifier clause | Result |
|---|---|
| any value other than 0 | not met (0) |
| entry cites an S-id from S134 upward | not met (acceptance grep passes; mutations show the grep works) |
| a detail that lost S094 rests on a row whose re-opened page does not carry it, with no `(to-verify)` | **met in letter for line 87** (the passive-hand limit without the Type-3 scope, which S097's page contradicts). Lines 83, 90, 92 and 93 are not met, apart from the minor over-attribution on line 93. |
| must_not_cite: speech-surrogate entry, round-52 lesson | not met (checked by hand; the acceptance command does not cover these) |

## Smallest safe correction (text to paste, author lane)

Line 87, replace

`of which only 7 can serve as the passive hand (S097)`

with

`of which only 7 can serve as the passive hand of a two-handed sign whose hands differ in handshape (S097)`

Line 93, replace

`— the ASL pairs the CSLDS module lists, after Battison 1978 (S096)`

with

`— the ASL pairs the CSLDS module lists, all but APPLE/ONION credited to Battison 1978 (S096)`

Optional, line 87: change "the CSLDS module, reporting Battison 1978, counts" to "the CSLDS module counts". Optional, line 92: write the mark as `` `(to-verify)` ``.

Neither correction adds an S-id or a path, so after the edit D's counter stays at 0 and the acceptance command still exits 0.

## Unrun checks

- `reports/round-52/dry-run.py --check`, `tools/check-claim-separability.py`, `reports/round-52/claims-agree.py`: not run. That is the L1's job and outside a critic's scope.
- I did not check NAME's handshape against a source this session (marked [INFERENCE] above). The Type-2 counterexample does not depend on it.
- Battison 1974 itself is still unopened by ordinary means (S132: HTTP 403). The 1974 remnant on line 92 stays `(to-verify)`.
