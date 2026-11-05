# kotodama round 94 — lesson

Round: kotodama round 94, attempt 1. Base `e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2`; freeze `d4ff93c8844e6db33a6e9d85fc7f0848e9f66ca7` (claims O, C, A, predispatch receipts and wave-1 spec). Claims O (operability), C (coverage) and A (adjacency) are exactly as frozen in `reports/round-94/claims.json`; the frozen bytes are not amended here.

Freshness remains paused by the open L0 questions kotodama round-11 and round-89 ("Freshness axis-move claims are paused until ruled"; `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` lines 47 and 303, both still carrying no L0 ANSWER). The lowest-axis obligation is neither met nor waived this round, and no freshness claim is declared.

## Gate

Claim C's registry rows. Five new rows, S965–S969, all opened by ordinary means on 2026-11-05 (plain `curl`, default user agent, `-L` follow-redirects, `--max-time 30`; no browser, no challenge passed, no verification disabled). Every quote below was re-verified by this seat against the committed capture bytes: each is an exact substring occurring exactly once (`bytes.count(quote) == 1`) and each is 25 words or fewer. The capture sha256 values are re-measured here and match the scout's table.

| row | URL | access date | HTTP status | located quote (≤25 words, exact substring of the capture) | capture sha256 |
|---|---|---|---|---|---|
| S965 | https://journals.openedition.org/tipa/2987 | 2026-11-05 | 200 | "Les premières berceuses qui sont adressées aux nouveau-nés sont constituées de sons vocaux rythmiques" (14 words) | `10a716133b7f95dea02718946fac92e5b5cd4cbce6c7a6909187bacc5a295757` (S965.html) |
| S966 | https://open.journals.ed.ac.uk/ScottishStudies/article/download/593/619 | 2026-11-05 | 200 | "function of nonsense vocables is strongly indicated by a story which Donald Archie" (13 words) | `901b0f9236170dfd4a03c8f320f3a089f97233e948c16b0d94ee6209ff11e17b` (S966.pdf); text rendering `5e810ad6bfcabb1fef5f3d04bcbef4600dbcc133f315429a81949bd63c74d201` (S966.txt) |
| S967 | https://www.folklore.ee/tagused/nr90/nurijeva.pdf | 2026-11-05 | 200 | "intonations that are meant to soothe or put the child to sleep" (12 words) | `f566dd70905e8be9c6d4964024bc655af1ff7c81e7ce9b5cc3a6eef0848919e6` (S967.pdf); text rendering `72082b74ee639ef614c1bdd40cf817f8af7b0f81cbaf5f5817cbf0fdf9ba635d` (S967.txt) |
| S968 | https://journals.openedition.org/ced/4965 | 2026-11-05 | 200 | "une version lente chantée de la comptine ainsi que des enregistrements des trois vers en version parlée" (17 words) | `232a3e466441d16b73a61a97d2d0d42b548ff18859de2df8bf2f100f4c10914f` (S968.html) |
| S969 | https://content.scirp.org/pdf/adr_2021052514072571.pdf | 2026-11-05 | 200 | "the refrain stands out as the leading sound modulator in the song." (12 words) | `d7147c8dcf9b374a02e514e01e73a1911bde31157169620a65d0038e1c6fee86` (S969.pdf); text rendering `f37239cf1946ee66386f14d2674f8750fa0a1e1b8f786d6762124d9385e119cc` (S969.txt) |

All five rows are tier A, status `mined`, opened 2026-11-05, recheck `180d`, used-by `corpus/knowledge/linguistics/lullaby-child-song-formulae.md` — the 11-cell census grammar of `corpus/SOURCES.md` (header row at line 28). The claim requires at least three new rows from S965 up; five are proposed.

Further located spans the entry author may draw on, all in the same captures, all ≤25 words, each re-verified here as an exact single occurrence:

- S965 (S965.html): "En langues kanak, les locuteurs distinguent linguistiquement, l’acte de “parler”" (10); "Ainsi, les berceuses sont-elles fortement marquées par la répétition syllabique" (10); "archives orales en ligne sur les langues kanak" (8).
- S966 (S966.txt): "in Irish the vocables which occur almost invariably in the lullaby chorus find no place in" (16); "repetitive, incantatory, unintelligible formula (Combarieu 1909: 13). He attached" (9); "vocables—except for the words mo leanbh (‘my child’) and, perhaps significantly, the" (12); "trick of folk aetiology, of justifying the continuation of a pre-Christian practice by" (13).
- S967 (S967.txt): "one, similar to many Finno-Ugric peoples, includes improvised songs - the most archaic" (13); "Udmurt lullabies are divided into two different musical and stylistic groups. The first" (13); "second group. That lullaby has been recorded throughout Udmurtia, almost supplanting" (11).
- S968 (S968.html): "Les élèves s’en servent lorsqu’ils jouent, pour chanter aux poupées au moment du réveil, ou bien pour les bercer." (19); "L’interprétation de cette comptine traditionnelle s’accompagne de gestes qui évoquent la course du soleil dans le ciel et l’arrivée de la nuit." (22).
- S969 (S969.txt): "An apostrophe is an address to someone who is not physically present at the" (14); "aesthetic devices such as repetition/refrain, rhetorical question device, and use of" (11).

Rejected and unreachable candidates, one line each with its exact response. None of these is a registry row.

- Berbel 2026, "Kinderlieder in Translation", `https://linguistische-treffen.pl/articles/29/03_berbel.pdf` — OPENED, not a row: HTTP 200, 814173 bytes, application/pdf; a translation study of German children's songs with finger-play gestures, offering no located quote about nonsense-syllable refrains, archaic retention in lullaby text, or the lullaby as archive.
- Aubinet 2026, *The Lullaby's Outline* (Routledge), preview PDF `https://api.taylorfrancis.com/content/books/mono/download?identifierName=doi&identifierValue=10.4324/9781003667513&type=googlepdf` — OPENED, not a row: HTTP 200, 1346887 bytes, application/pdf, publisher preview (front matter, table of contents and blurb only, no chapter body); a publisher description is tier B for substantive claims and carries no body argument about the six topic facets.
- Humanus 16(1) 2017 "Meaning and Form in Nursery Rhymes Translation", `https://ejournal.unp.ac.id/index.php/humanus/article/view/6655/pdf` — OPENED, not a row: HTTP 200 but 23120 bytes of text/html (the OJS viewer page, not the PDF), so no article body was served to a plain request.
- MDPI *Languages* "Modulation of Maximum Pitch in the Speech of Caregivers Addressing Their 18- to 24-Month-Old Children", `https://www.mdpi.com/2226-471X/10/10/257` — UNREACHABLE: HTTP 403, 399 bytes, text/html access-denied notice; not passed, not retried with any bypass.
- MDPI *Languages* "Language Attitudes Regarding Communication with Young Children and the Use of Diminutives", `https://www.mdpi.com/2226-471X/10/9/229` — UNREACHABLE: HTTP 403, 400 bytes, text/html access-denied notice.
- *Textes & Contextes* "Ninna nanna che tu crepi", `http://preo.u-bourgogne.fr/textesetcontextes/index.php?id=4110` — UNREACHABLE: HTTP 403, 2747 bytes, text/html, after redirect to `http://preo.ube.fr/textesetcontextes/index.php?id=4110`.
- *Intercultural Studies* "Don't Believe It, O Dove", `https://immi.se/index.php/intercultural/article/download/10.36923.jicc.v26i4.1632/1305` — UNREACHABLE: HTTP 406, 413 bytes, text/html.
- University of North Texas dissertation on the lullaby, `https://digital.library.unt.edu/ark:/67531/metadc1752327/m2/1/high_res_d/ESTWICK-DISSERTATION-2020.pdf` — UNREACHABLE: connection timed out after 30 s with 0 bytes received (curl exit 28); one attempt only, no retry, because a read timeout is not in the declared one-retry-on-transient-5xx/429 class.
- Traditional Ballad Index, `https://www.ballad-index.org/` — UNREACHABLE: curl exit 6, "Could not resolve host".
- Jentera "Local Wisdom and Didactic Values in Lullaby Kawih Mepende Murangkalih", `https://ojs.badanbahasa.kemdikbud.go.id/jurnal/index.php/jentera/article/view/4945` — UNREACHABLE: curl exit 6, "Could not resolve host".
- Europe PMC search `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=lullaby...` — UNREACHABLE: HTTP 502, 150 bytes.
- gutendex book search `https://gutendex.com/books/?search=lullaby...` — UNREACHABLE: first attempt HTTP 503 (curl exit 28 after 30 s on the second variant); the API did not serve results.

Search method (screening only; every row above was then opened by a direct request to the article page or PDF): the DOAJ open-access article API `https://doaj.org/api/search/articles/<query>?pageSize=25` over `lullaby`, `child-directed speech`, `nursery rhyme`, `comptines`, `berceuse`, `hällilaul`, `cuna canción`; the Crossref works API `https://api.crossref.org/works?query.bibliographic=...`; the OpenAlex works API `https://api.openalex.org/works?search=...`; and a plain `gutendex.com` probe (unreachable, recorded above). No bot challenge was met and none was passed.

Census before and after, as `reports/round-94/predispatch.py` computes it. The commands and exit codes below are the frozen counter's own lines; the base values are the frozen receipt `reports/round-94/predispatch-base.txt`.

- Claim A1 dangling-greeting-pointers, command `python3 -B reports/round-94/predispatch.py --root <lane-root>`, rc 0. Before: `A1 dangling-greeting-pointers 2 :: corpus/knowledge/culture-material/adornment-body-codes.md:5 corpus/knowledge/culture-material/costume-semiotics.md:143` (frozen receipt line 1; re-measured here at the lane root, rc 0, same string). After the repoint patch applied in scratch: the frozen counter still prints the identical line with the count 2 — not because the pointers still dangle but because of the counter's own filter defect, recorded as M3 below. With that one filter removed from a scratch copy of the counter, the same command prints `A1 dangling-greeting-pointers 0 ::` (rc 0).
- Claim C2 registry rows and highest id, same command and rc 0. Before: `C2 registry-rows 888 highest-id S964` (frozen receipt line 3). After, measured in scratch on a mirror of `corpus/` with the five new rows appended before `## Paths`: `C2 registry-rows 893 highest-id S969`.
- Census, command `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama`, rc 0 at base (frozen receipt line 5, last line `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`; re-measured here, rc 0, same last line). After, measured on the mirrored registry with the five new rows appended and the new entry present: `sources-census.sh validate --file <scratch>/tree/corpus/SOURCES.md`, rc 0, and the finding set is byte-identical to the base run's finding set apart from the file path in the `ok` line (35 pre-existing W-findings, zero E-findings; the new rows raise no finding). The projected registry counts are 888 → 893 rows, tier A 526 → 531, mined 781 → 786, mined-and-tier-A 470 → 475.
- Index, command `python3 -B tools/check-corpus-index.py --root .`, rc 0 at base (frozen receipt line 6, `CORPUS-INDEX: OK files=265 rows=265 findings=0`; re-measured here, rc 0, same line).
- Tool sha256 at base, same counter, rc 0: `O0 tool-sha256 9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` (frozen receipt line 4). The v4 selftest re-measured in scratch from the base bytes: `SELFTEST PASS 114/114`, rc 0, exactly 114 `  ok ` lines — the N = 114 base that claim O's SELFTEST predicate names as its floor plus six.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R94-M1 | verifier defect classes accepted by the grader | `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/CriticClaims93.md` (the ten-counterfeit attack record) and `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-93.md` section "## Routed to round 94" (the MutationTesterV4 and CriticClaims93 bullets) | none — no v4 pin or leg named any of these classes | grader v5, with a red-before on the v4 base: `.ufo/waves/round-94/w1/stage/ExecBattery94/red-before-v4.txt` (`BATTERY-SUMMARY survivors=4 unnamed=3 refused=0`: A1, B1, G1, K1 survive rc 0 on 9/9 legs; H1 and I1 die with Python tracebacks and no named diagnostic; J1 is refused on APPENDONLY but with the wrong verdict direction) and `.ufo/waves/round-94/w1/stage/ExecMutants94/red-before-v4.txt` (`MUTATION-SCORE: 0/5 killed, 5 survived, 0 broken-pattern`: script-strip-off, comment-strip-off, unescape-off, dispo-any-casei and baserows-drop-cell8 each SURVIVED with `selftest_rc=0`) |
| R94-M2 | report table label mismatch (tier-A-any-status values filed under the label "mined A rows") | `/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-93-verifier-spotcheck.md` section 2, the Claim C defect paragraph ("the report's before→after table row 'mined A rows 522 → 526' carries tier-A-any-status values") | none — no tool read the report table's label against its own command cell | an append-only erratum in the round-94 report; the filed round-93 bytes are not rewritten. The filed text stands as filed at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-93/kotodama.md` line 70, `| mined A rows | 522 | 526 | awk on column 5 and column 8 of the registry table |` (file sha256 `ceec3f4d2f5c6ffcdcc73563ea7f5cd3fccc8e2c1a7b345a9f46a44a51f2c22a`), and at `corpus/lessons/round-93.md` (sha256 `912bb2610f3f82fc801061a9bb46be9d8b526ff6c53ea9d76cb745e8dd87769e`). Measured here, read-only, at the two revisions the spot-check names: tier-A-any-status 522 → 526, mined-any-tier 777 → 781, mined-and-tier-A 466 → 470. The label is wrong; the delta +4 is right |

Both fixes can fail where they claim to, and the red-before receipts are named above.

R94-M1 is shown able to fail by the two v4 red-before receipts, not by assertion. `red-before-v4.txt` (ExecBattery94) is the proof that the v4 tool does not already refuse the classes: with `TOOL sha256=9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` pinned in its own header, four of the seven classes pass rc 0 on all nine legs and two die with a traceback and no named diagnostic, so a v5 that "refuses all seven" is a change of behaviour, not a re-reading. `red-before-v4.txt` (ExecMutants94) is the proof that the five routed mutants are live pin gaps: each patch matches the v4 bytes exactly once (`script-strip-off` 1, `comment-strip-off` 1, `unescape-off` 1, `dispo-any-casei` 1, `baserows-drop-cell8` 1), each mutant prints `SURVIVED selftest_rc=0`, and the score line reads `0/5 killed, 5 survived, 0 broken-pattern` — so `killed == total` at v5 is a real measurement rather than a vacuous pass. The frozen counter cannot mask either: the stub control `reports/round-92/controls/stub-tool.py` re-measured here prints `SELFTEST PASS 89/89` with rc 0 and 34 `  ok ` lines against its own 89-tally, which is the printed-tally attack the claim's do-nothing control names.

R94-M2 is shown able to fail by the measurement that exposes the label: the report's own command cell says "awk on column 5 and column 8 of the registry table", and that awk run against `corpus/SOURCES.md` at `8b2ce60a7bbf015f42a6c9e5c45e994e4c2f7742` and at `95e7a5cff1687b21d982607ab0bfd8e381c3036c` returns tier-A-any-status 522 and 526 — the numbers the table prints under the label "mined A rows" — while mined-and-tier-A at the same two revisions is 466 and 470. The erratum is therefore checkable and can be falsified: if the appended round-94 erratum named 466 → 470 as the tier-A-any-status values, the awk command would contradict it. The append-only form is what keeps the check honest: the filed round-93 bytes are hashed above and are not to be edited, so the erratum in the round-94 report is the only place the correction may live.

A third defect is mine to record and is not in the frozen claim set, so it is stated here and routed below rather than folded into either row.

R94-M3 · counter defect · `reports/round-94/predispatch.py` line 33, `targets = [t for t in LINK.findall(text) if "greet" not in t]` · captured by this seat's own read-only reproduction and, independently, by the ExecAdjacency94 seat (`stage/ExecAdjacency94/before-after.txt` records the same cause and the same 0 under a scratch-only diagnostic copy) · fix: none applied — the counter is frozen and claims.json is frozen. The filter drops every link target whose path contains "greet", so the one target claim A's repoint is supposed to use, `linguistics/greeting-leave-taking-formulae.md`, can never be counted as resolving; the counter therefore reports 2 dangling after a correct repoint. Measured in scratch here: with the repoint patch applied to a clone at base, the frozen counter prints `A1 dangling-greeting-pointers 2 :: corpus/knowledge/culture-material/adornment-body-codes.md:5 corpus/knowledge/culture-material/costume-semiotics.md:143` (rc 0), and the same pointer lines resolve to `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md` under a direct probe of the counter's own three candidate paths (both lines resolve; the target file exists and mentions greeting and leave-taking). With only that filter removed from a scratch copy, the counter prints `A1 dangling-greeting-pointers 0 ::` (rc 0). This is a decision for the L1, and it is the reason claim A's after-target cannot be reported as met this round.

## Routed-to-95 candidates

- The L0 overlap question on the ideophones entries is still open and unanswered: `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` line 356 (kotodama | round-92) asks whether `corpus/knowledge/linguistics/ideophones-mimetics.md` (landed `1473606b`) may keep restating `corpus/knowledge/linguistics/sound-symbolism.md` §6 (lines 99–111), and the line carries no L0 ANSWER. It is also carried forward in `corpus/lessons/round-93-verifier-spotcheck.md` §6 item 5. Nothing in round 94 touched either file; the question is unchanged and is routed again.
- The freshness pause is unchanged: `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` line 47 (kotodama | round-11, "Freshness axis-move claims are paused until ruled") and line 303 (kotodama | round-89, whether live source re-verification falls inside that pause). Neither carries an L0 ANSWER; the round-94 claim set declares no freshness claim, so the obligation is neither met nor waived. Route: unchanged, awaiting the ruling.
- The title-only exclusions are still open, and the criterion that was supposed to close them does not close them. `corpus/lessons/round-92-verifier-spotcheck.md` §4 and §5 item 1 record the sixteen round-92 search-log exclusions that were decided on DOAJ metadata with no per-candidate reason, plus three named re-decisions (Awetí 2015, Zulu Lexikos 2011, Turkish Signifiances 2020) whose captures were re-opened and found disagreeing with the gate. QUALITY criterion 37 landed in `corpus/QUALITY.md` (line 365) and its own sweep passes on the round-93 lesson (`awk '/^## Gate/{g=1;next} /^## /{g=0} g' corpus/lessons/round-93.md | grep -E '^- ' | grep -vE '^- S[0-9]+ admit' | grep -viE 'reason|because|off-topic|on-topic|not on topic|not opened|unassessed|marginal|restricted|access|403|404|429|500|TLS|unreachable|fail|could not|not re-openable|does not|never|same|title-only|no reason|not fetched|cannot'` → 0 of 31 bullets), but criterion 37 constrains what a round's own Gate writes; it cannot retro-fit a reason onto the round-92 bullets, and no round-93 or round-94 lesson re-decides the sixteen or the three named sources. Evidence pointer: `corpus/lessons/round-93-verifier-spotcheck.md` §6 item 5. Route: unchanged, still open.
- The frozen A1 counter's line-33 filter defect (R94-M3 above) is not closed this round and no seat may amend `reports/round-94/predispatch.py`. Evidence pointer: `reports/round-94/predispatch.py` line 33, measured above, and `stage/ExecAdjacency94/before-after.txt`. Route: the L1 either amends the frozen counter's filter (a claims-side change the seats cannot make) or accepts claim A with A1 = 2 and this cause recorded.
- The round-94 battery's naming rule for J1 is a judgment that the L1 must ratify, not a settled fact. `stage/ExecBattery94/red-before-v4.txt` records J1 as `rc=1 traceback=no named=none outcome=UNNAMED` with the detail `LEG FAIL APPENDONLY`, and the seat's own report discloses that a literal leg-name-only reading would count J1 as REFUSED on v4. The round-93 critic recorded the same class as a wrong-direction refusal. Route: the L1 states which rule governs, because the choice changes whether J1 is a survivor of v4 or a refusal.
- The F1 class named in the round-93 routed list — content-free numbered h2 headings that pass ENTRY and are refused only on TOPIC — is not among the seven classes claim O's battery names, and the round-94 battery manifest carries no F1 entry. It therefore remains uncovered by this round's predicate. Evidence pointer: `corpus/lessons/round-93.md` "## Routed to round 94", the CriticClaims93 bullet, and `.ufo/waves/round-94/w1/stage/ExecBattery94/manifest.json`, which lists A1, B1, G1, H1, I1, J1, K1 only. Route: unchanged.
- Six round-93 mutant patterns match the v4 bytes more than once (`self-quote-check-off` ×2, `source-quote-check-off` ×2, `duplicate-id-off` ×2, `duplicate-url-off` ×3, `cellcount-off` ×2, `gap-cap-slash-capture-error-off` ×2), so the exactly-once patch rule the five routed mutants are held to cannot be applied to them without marking the frozen 83-entry set broken-pattern. The round-93 score was taken under replace-all semantics, so the frozen 83 are unchanged. Evidence pointer: `.ufo/waves/round-94/w1/ExecMutants94.md`, "Noted for MutationTester94". Route: the L1's mutation run must keep the replace-all semantics for the round-93 entries and the exactly-once rule for the five routed ones, and must say which applies where.

## L1 integration record (added at landing, 2026-11-05; the seat text above is verbatim)

This section supersedes the stale items in the seat draft where they disagree with what
happened at integration. Nothing above is rewritten.

1. **R94-M3 is closed.** The L1 amended the frozen counter before any claim was scored:
   `reports/round-94/predispatch.py` rev2 (commit `314ad1247ed5fec1195d8228da5c6bc37a51ea30`,
   documented in `reports/round-94/counter-revisions.md`) removes the line-33 greet-name
   exclusion; the base receipt was re-stamped from a `git archive` of the base and prints the
   same values (A1 still 2 at base). ReviewerC94's claim-A blocking finding was measured
   against rev1 bytes in a base clone and is resolved by rev2: on the assembled lands tree
   rev2 prints `A1 dangling-greeting-pointers 0`. The route in the draft's Routed-to-95 list
   is withdrawn.
2. **Battery instrument amendment (pre-scoring).** The battery manifest and the driver's
   class table guessed diagnostic token names that differ from the v5 grader's actual named
   tokens; the lists were amended (originals kept) before the graded battery ran, documented
   in `reports/round-94/counter-revisions.md`. Graded result at the candidate bytes
   (`7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff`):
   `BATTERY-SUMMARY survivors=0 unnamed=0 refused=7`, per-class named tokens
   (`VERDICT-NONASCII`, `VERDICT-SOFTHYPHEN`, `TOPIC`, `MANIFEST-ROW-TYPE`, `NEWIDS`,
   `gained a NOT-LOCATED line`, `VERDICT-LOWERCASE`), no traceback anywhere, and the 34 REG
   lines byte-identical to the v4 run (`diff` empty). Receipts:
   `reports/round-94/controls/` (battery-v5.txt, reg-v4.txt, reg-v5.txt, selftest-v5-run1.txt,
   stub receipts, instrument-shas.txt).
3. **Claim O FAILED AS DECLARED on its frozen MUTATION leg.** MutationTester94 ran the full
   88-mutant set against the candidate: `86 killed, 1 survived (head-qualify-off),
   1 broken-pattern (dispo-fallback-off)`. The frozen leg requires killed == total with
   0 survived and 0 broken-pattern, so the leg fails and the claim's kill rule fires; the
   five routed mutant classes are all killed (their sub-requirement holds), but the leg as
   frozen is unmet. No amendment is made after scoring. Receipts:
   `.ufo/waves/round-94/w1/stage/MutationTester94/mutation-score.txt` (sha256
   `786c9eb1431213160237cf7a912bfc7a08b35f92c1ecf518d7361a9408e3a211`), survivors named in
   `survivors.md`; a lands-stamped re-run is recorded at `reports/round-94/mutation-score-lands.txt`.
4. **SELFTEST, BATTERY and REGRESSION legs pass** on the candidate bytes: selftest
   `SELFTEST PASS 126/126`, 126 `  ok ` lines, rc 0, four concurrent runs (floor was >= 120
   with six new named checks; the tool adds 12: seven round-94 class checks plus five mutant
   pins). The stub control fails SELFTEST (prints `SELFTEST PASS 89/89` with only 34 ok
   lines), fails BATTERY (`survivors=7 refused=0`) and fails MUTATION (`0/88 killed,
   88 broken-pattern`).
5. **ReviewerO94's verdict is void by timing, not by content.** The seat's 45-minute
   dependency bound expired before the grader seat wrote its stage; the candidate landed
   later. The selftest/diff/regression review the seat prepared for was executed by the L1
   (item 2 and item 4 above); CriticO94's independent attack (13 new counterfeit classes
   against the candidate, plus the G0 control clean) and MutationTester94's run stand as the
   outside checks.
6. **Claim C landed with two reviewer framing fixes applied before landing** (ReviewerC94
   notes C6/C7): the entry's "That single exception is the whole design point" sentence now
   reads "The real-word exceptions are the whole design point", "the strongest available
   evidence that the shift is a *lexicalized* distinction" now reads "direct evidence that
   the speak/sing split is a *lexicalized* distinction", and "gives singing its own verb"
   now reads "lexicalizes the speak/sing split" (design line). Entry landed bytes sha256
   `9bcbf64d03a65d65223c255b110f063bedcd57dd2e90220dd6999dfcd139e7d9`, 43409 bytes. The
   round-93 erratum owed by R94-M2 is filed in the round-94 report's Errata section.
7. **Census after values are the lands measurements** (assembled tree identical to the
   landed bytes): `A1 dangling-greeting-pointers 0`, `C1 entry-present 1`,
   `C2 registry-rows 893 highest-id S969`, `O0 tool-sha256 7957945d…`, census rc 0 with
   0 E-findings on S965-S969, index `CORPUS-INDEX: OK files=266 rows=266 findings=0`.
8. **J1 ratification (draft's Routed-to-95 item):** the L1 ratifies the battery's J1 naming:
   the class counts as REFUSED when the grader prints the message
   `gained a NOT-LOCATED line` (a named diagnostic), which v5 does; v4's misfire is recorded
   in the red-before. The F1 gap and the multi-match round-93 mutant patterns stay routed.
9. **Wave shape:** one v1 wave of 13 seats (5 executor, 1 scout, 1 connector, 2 scribe,
   2 reviewer, 1 critic, 1 mutation-tester; attack 4/13 = 31 percent), no residual call, no
   replacement seat, no dead seat; every seat's scratch was removed before yield except
   L1-owned scratch (`/fast/scratch/hyaku/kotodama-r94/L1-*`), which the L1 removed after
   landing.
