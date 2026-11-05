# kotodama round 96 — lesson

Round: kotodama round 96, attempt 1 (L1 KotodamaR96). Base `0539276c0e329743200b60e98bf289c540f78864`.
Freeze `deca7e6fff988061f01bfc501a91e18fca892822` (claims.json, predispatch.py, control receipt
`reports/round-96/predispatch-base.txt`: FAIL legs=3/12). Correction before any seat ran:
`063f70c9ab9aed5297741773292ded6d713d537a` (claim-O before-prediction changed from survivors=10 to
survivors=9, refused=15; the predicate and counter were not changed). Wave `w1`: 12 seats, dispatched
17:42:59 -03 after a disk-pressure defer (`reports/round-96/`… see `.ufo/l0-questions.md` round-96 line).

Claims (frozen in `reports/round-96/claims.json`):

- **O — operability (grader v6 → v7 → v8).** Close the nine CriticO95 fresh survivors (NB1, VT1, FF1, LS1,
  NEL1, ANSI1, CYR1, BR1, DASH1) and add the F1 battery class. Frozen predicate: battery96
  `survivors=0 unnamed=0 refused=24`, selftest ≥144, mutation96 killed==total ≥95 with 0 survived and 0
  broken-pattern, REG lines of reg-v5 byte-identical in battery96 output.
- **C — coverage (frontier → core).** New entry `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`
  on a surface with no owned knowledge file at base, plus ≥3 new tier A|B registry rows opened 2026-11-05.

## Measured before → after (frozen counter `reports/round-96/predispatch.py`)

| leg | base `0539276c` (control) | landed tree (`f29ab013…`, tool v8) |
|---|---|---|
| O0 tool sha ≠ v6 `f7981ba2…` | FAIL (sha = v6) | PASS |
| O1 selftest | FAIL 134/134 < 144 | PASS 147/147 |
| O2 battery96 | FAIL driver missing (control run by ExecBattery96 over v6: survivors=9 refused=15) | PASS survivors=0 unnamed=0 refused=24 |
| O3 mutation96 | FAIL driver missing (v6 red-before: 95/112 killed, 17 broken-pattern) | PASS 111/111 killed, 0 survived |
| O4 REG | FAIL no battery output | PASS 34/34 identical |
| C1 entry | FAIL absent | PASS 30143 B, 11 h2, table 19×5, 6/6 phrases, topic equal |
| C2 registry | FAIL 898 rows, highest S974, 0 qualifying | PASS 908 rows, highest S984, 10 qualifying |
| C3 append-only | PASS (guard) | PASS added=10 removed=0 |
| C4 census | PASS (guard) | PASS rc 0 (`.ufo/waves/round-96/census/census-end.txt`) |
| C5 index | PASS (guard, 267 files) | PASS 268/268/0 |
| C6 ids cited | FAIL | PASS 10/10 |
| C7 captures | FAIL | PASS 10/10 |

Counting command for every leg: `python3 -B reports/round-96/predispatch.py --root . --work <scratch> --base-rev 0539276c0e329743200b60e98bf289c540f78864`
(landed-tree run output: `reports/round-96/predispatch-lands.txt`).

## Honest account of claim O (read this before the verdict)

The first measurement of the landed v7 bytes (`2e28a289…`) failed O3: `MUTATION-SCORE: 109/112 killed, 3 survived`.
Survivors `fs-u001d-off` and `fs-u001e-off` were real test gaps (U+001D/U+001E were in the refusal tuple but
had no selftest pin); `id-lookalike-refuse-off` survived because the ID1 branch at v7 line 335-345 is a
duplicate of the earlier `_refuse_verdict_channel` ID-NONASCII check and no probe distinguishes them.
Repair, landed as the same claim's v8 bytes (`f29ab013…`): (a) pins FS2 (U+001D) and FS3 (U+001E) added to the
round-96 pin block; (b) the shadowed duplicate branch deleted (CUT 335–345) per the engineering rule to delete
dead weight; battery96, selftest and REG all re-ran green after the deletion. (c) The mutant entry whose
target was deleted (`id-lookalike-refuse-off`) was retired from `stage/MutationTester96/mutants96.py` (kept as
`mutants96.py.pre-retire` in the stage, sha recorded in the Report) — mutation total 112 → 111. The v7
measurement (109/112, O3 FAIL) is kept as the record; the predicate (killed==total, 0 survived, total ≥95) was not
changed. A non-author verifier should rule whether the v8 repair counts as the claim's landing; the report
carries both measurements and does not hide the first failure.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R96-M1 | transient-timeout misread as unreachable (the round-95 Thrênoi reject) | `corpus/lessons/round-95.md` line 26 (curl exit 28, max-time 30, no retry) vs `.ufo/waves/round-96/w1/stage/ReviewerThrenoi96/decision.md` §1 (both URLs HTTP 200 on attempt 1, 302080 B PDF) and §3(a) "access reason DID NOT HOLD" | none — QUALITY.md criterion 37 accepts a single-attempt access reason; the bounded re-opener's transient retry rule (`tools/reopen-row.py`, 3 attempts, lines 84–92 and 488–566) was not applied to this reject | QUALITY.md criterion 38 (below): a reject whose reason is access must have passed three transient-retry attempts through the re-opener rule; a single-attempt timeout is recorded `not-opened-transient`, not `UNREACHABLE`. Able to fail: the round-95 Thrênoi line fails the criterion's sweep (`grep -n 'UNREACHABLE' corpus/lessons/round-95.md` returns the line with `curl exit 28` and no retry count) and the re-open above shows the reason did not hold. |
| R96-M2 | grader test gap: U+001D/U+001E claimed refused, unpinned | `.ufo/waves/round-96/w1/stage/MutationTester96/mutation-score-v7.txt` lines 104–105 (`fs-u001d-off`, `fs-u001e-off` SURVIVED on v7) | the round-95 selftest carried no pin for the U+001C–U+001E family (only FS1 round-95 class); round-95 mutation receipt did not cover the family | v8 pins FS2 and FS3 (selftest 147/147); mutation re-run kills both (`reports/round-96/predispatch-lands.txt`, leg O3). |
| R96-M3 | dead duplicate check (shadowed branch) | `tools/check-advance-evidence.py` v7 lines 335–345 vs `_refuse_verdict_channel` lines 290–300; `id-lookalike-refuse-off` SURVIVED | CriticO95 and ExecGraderV7 both missed it: no equivalence check existed for grader branches | branch deleted in v8; mutant retired with disclosure (above). Evidence that the deletion is safe: selftest 147/147, battery96 24/24, REG 34/34 green after deletion. |
| R96-M4 | derived-before-landed ids in a draft | `.ufo/waves/round-96/w1/ScribeEntry96.md` (first message: entry cited S975–S985 from the scout's candidate order, C4 included) | the scribe's dependency wait was bounded and the scribe continued on a derived mapping when the registry seat had not landed | the entry was re-keyed to the landed `rows.md` ids (S975–S984), C4-grounded paragraphs removed; counter legs C2/C6/C7 would have failed the earlier draft. Caught by ExecRegistry96's dropped.md, not by the L1. |
| R96-M5 | claim before-prediction wrong before any seat ran | `reports/round-96/claims.json` (first draft: survivors=10 refused=14 — counted ZWNJ1 control and assumed F1 unrefused) | none — the prediction was written without running the v6 battery | correction commit `063f70c9` before any seat ran; the control receipt measured survivors=9 refused=15 (ExecBattery96 `control-v6.txt`), as corrected. |

Sweep for R96-M1 class (captured-by check run this round):
`grep -n 'UNREACHABLE' corpus/lessons/round-9[0-5].md | grep -v 'retry' | head` — rows whose access reason has no
retry count are listed for re-open in round 97 (not re-decided here; route-only).

## Gate

Rows admitted this round (`corpus/SOURCES.md` lines 932–941; opened 2026-11-05 by plain curl, `-L`,
`--max-time 30`, default user agent; each quote re-counted by the registry seat and by CriticC96 with
bytes.count == 1 on the capture; HTTP 200 for all ten):

| id | URL | access | HTTP | located quote (≤25 words) | capture sha256 |
|---|---|---|---|---|---|
| S975 | https://books.openedition.org/editionsehess/2703?lang=en | 2026-11-05 | 200 | “the ultimate goal of all these self-curses is, of course, to strike fear into those who swear the oath” (19 words; count 1) | `3124ab40600a2b60…` |
| S976 | https://hcmc.uvic.ca/~scancan/pdf/nygaard_1_28.pdf | 2026-11-05 | 200 | “at ek vinn eið at bauga, lögeið” (7 words; count 1) | `770a34d847a5696e…` |
| S977 | https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0133:book=19:card=258 | 2026-11-05 | 200 | “ἴστω νῦν Ζεὺς πρῶτα θεῶν ὕπατος καὶ ἄριστος” (8 words; count 1) | `5572d82e7fcbff8c…` |
| S978 | https://journal.fi/scf/article/download/7032/20487/61412 | 2026-11-05 | 200 | “curse-enhanced oaths or vows lie behind the notion of the geis” (11 words; count 1) | `42b907c3ad71293a…` |
| S979 | https://mural.maynoothuniversity.ie/id/eprint/1333/1/Satirical_Narrative_in_Early_Irish_Literature.pdf | 2026-11-05 | 200 | “the seven requirements which compose any satire (cach n-aír) are” (10 words; count 1) | `1160f5ccdae8f369…` |
| S980 | https://ora.ox.ac.uk/objects/uuid:36e9551e-5a3b-4aac-98c1-0e12614110f9/files/dhq37vp39v | 2026-11-05 | 200 | “a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra” (10 words; count 1) | `4e7f3189db1fc11e…` |
| S981 | https://d-museum.kokugakuin.ac.jp/eos/detail/?id=8565 | 2026-11-05 | 200 | “divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections” (15 words; count 1) | `08431da0a5430c7c…` |
| S982 | https://ojs.unm.ac.id/englishperformance/article/download/89987/37848 | 2026-11-05 | 200 | “to witness their truthfulness and punish them if they lied” (10 words; count 1) | `a8e1ce4a84abf2bf…` |
| S983 | https://en.wikisource.org/wiki/Shinto:_The_Way_of_the_Gods/Chapter_12 | 2026-11-05 | 200 | “the recital of a norito or formula—not a prayer, as it is sometimes called” (14 words; count 1) | `ae7cf21185c0a2e2…` |
| S984 | https://www.thetorah.com/article/yhwhs-covenant-why-moses-calls-heaven-and-earth-as-witnesses | 2026-11-05 | 200 | “Moses in Deuteronomy draws on formulations found in ancient Near Eastern treaties” (12 words; count 1) | `6b6f435681c9880d…` |

Rows not admitted (scout `candidates.md` §3 and registry `dropped.md`): the scout rejected R11 Iliad 1 (scope), R15 novel
(scope), R17/R24 Jewish Encyclopedia pages (wrong article: the person BARAK), R20 Butler Iliad (no formula wording
in capture), R26 Sefaria (app shell, 578 B), R27 Manusmriti 8.109 (registry duplicate of S838), R28 TheTorah topic
landing (index, superseded by C11), R30 livius.org (404), R31 soas.ac.uk (landing, no body). C4 (Ó Murchú asseveration)
was admitted by the scout, then dropped by the registry seat: fresh HTTP 404, quote count 0 — "no fallback to the
scout's old capture". Wayback fetches timed out on this host (curl rc 28); availability-API pointers recorded, not
captures.

**Nominated, not admitted:** the Thrênoi to Moirológia PDF (Oral Tradition 23/2, 2008; `ReviewerThrenoi96` §5),
tier A, for the professional-mourner facet of the lament entry. The access reason did not hold; the content decision is
ADMIT-AS-CANDIDATE. No row was written: the registry seat (the only writer of `corpus/SOURCES.md`) had finished, and the
L1 does not write rows. Routed to round 97 with its flip condition. The round-95 reject is therefore *withdrawn in
substance* but the registry still has no row for the source.

## Assimilation

`Assimilation: none`. `considerthese/` does not exist in this lane (verified: `ls considerthese` → no such file). The
shokuknow package `merge/kotodama/` exists at `/home/vgpnk/Projects/shokuknow/merge/kotodama/`; this round's frontier
item was the sourced claim C, and the quarantine-first slice (kotodama 21 rows at 2026-10-24, re-derived count not
re-run this round) was not hand-checked. Nothing was adopted from the package; nothing was written there.

## Routed to round 97

- CriticO96 (attack seat, `stage/CriticO96/attacks.md`): against v7, seven classes survive that battery96 does not
  carry: CR1 (lone CR U+000D in verdict), US1 (U+001F), OGH1 (U+1680 space), IS1, NUL1, CM1, CMW2. Their tally is
  `CRITIC-O96 survivors=7 unnamed=0 refused=12`. They are not claim-O failures (the predicate is battery96), but they
  are the next claim-O surface. v8 has not been re-attacked; the v7 measurement is the one reported.
- CriticO96 and MutationTester96 on v8: not re-run after the v8 edit except the frozen counter (O2, O3 PASS).
- Shadowed-branch class: a grader equivalence check (a branch whose removal leaves every battery and selftest result
  unchanged) is a candidate QUALITY criterion; not added this round.
- Duplicate-authority risk for claim C: CriticC96 §2 measured 14 of 4891 distinct 8-grams shared with
  `myth-symbol/binding-speech-complex.md` (0.29%, deferral prose). The new entry defers the enforcement side to that
  file; a future round may tighten the boundary. Not a verdict change.
- ReviewerC96 (reviewer seat) ended without a DONE marker and without a verdict (its last text: "Still blocked on the
  DONE markers — continuing the wait"). Dead seat, no verdict. The L1 ran the frozen counter on the landed tree
  (`reports/round-96/predispatch-lands.txt`) and CriticC96 recounted quotes and ids; the reviewer's check is not
  substituted.
- Thrênoi nomination (above).
- Freshness axis: still paused by open L0 questions kotodama round-11 (`.ufo/l0-questions.md` line 47) and round-89
  (line 303). No ANSWER line. The lowest-axis obligation is neither met nor waived this round.
- Ideophones overlap (round-92 L0 question, line 356): still open.
- Dispatch was held by host disk pressure on `/fast` (100% at 17:28 -03; L0 line appended this round). The seats ran
  after space returned (49% at 17:52). Routing to the operator.

## QUALITY.md criterion 38 (new, this round)

Criterion 38 is added to `corpus/QUALITY.md`: a reject or exclusion whose recorded reason is access (UNREACHABLE,
timeout, TLS, connection error) must show the retry rule of the bounded row re-opener (three attempts per URL on a
transient result, then a further pass) on the record. A single attempt is recorded as `not-opened-transient`, not
`UNREACHABLE`. Able to fail: applied to the round-95 Thrênoi line it fails (one attempt, `curl exit 28`, no retry
count) and the re-open shows the reason did not hold.

## Sources census

- Start: `.ufo/waves/round-96/census/census-start.txt`: `sources-census.sh validate --root <fleet> kotodama` rc 0.
- End: `.ufo/waves/round-96/census/census-end.txt`: rc 0 (`kotodama ok`). Registry 898 → 908 rows, +10 (S975–S984), 0 removed.
