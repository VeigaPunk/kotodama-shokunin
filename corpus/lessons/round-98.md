# kotodama round 98 — lesson

Round: kotodama round 98, attempt 2 (L1 KotodamaR98a2; attempt 1 L1 KotodamaR98 ended mid-work,
`.ufo/watchdog.log` `lane-dead-no-report kotodama round=98` 23:31:14). Base `bcf664aa089ddbd1fac85772ed22a38d1b454d23`.
Freeze `db88f107606aae90efe01344551c7e1ea71cd419` (attempt 1, before any seat ran): `reports/round-98/claims.json`,
counter `reports/round-98/predispatch.py`, do-nothing control `reports/round-98/predispatch-base.txt`
(`PREDISPATCH-98: FAIL legs=5/15`), forgery and positive controls `reports/round-98/controls/forgery-summary.txt`,
battery98 + pin + v9 control receipt (`reports/round-98/controls/battery98{.py,.sha256,-control-v9.txt}`).
Waves: `w1` (13 seats, attempt 1; 3 died with the orchestrator session without a report) and residual `w2`
(3 seats, attempt 2) replacing the three dead attack/mutation seats.

Claims (frozen, unchanged by attempt 2):

- **O — operability (grader v9 → v10).** Close the five CriticO97 forgeries that pass v9 unnamed: DEL1 (U+007F in
  the verdict token), ENC1 (U+20DD, category Me), ROMAN1, SUP1, FWPER1 (non-ASCII numbering tokens / full stop in
  h2 heads). Legs O0–O5.
- **C — coverage (frontier → core).** New entry `corpus/knowledge/linguistics/toast-drinking-speech-formulae.md`
  on a surface with no topic-line or heading owner at base (C8 owners=0) plus ≥4 new tier A|B rows. Legs C1–C9.

## Inherited from attempt 1 (re-verified by attempt 2)

Reused after re-verification: the freeze commit; seat outputs of ExecGraderV10 (v10 bytes
`d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7`), ExecRegistry98 (S994–S1005), ScribeEntry98 (entry,
README row), ReviewerC98 (`reopen.json`, C9), CriticC98, ReviewerOath98, ScoutSurface98, ScoutSources98,
ConnectorOverlap98, ExecGateCaps98 (`tools/check-gate-captures.py`); attempt-1 L1 integration repairs (entry lines
142/248/§8/§13, S1006 supersede of S994, S1005 supersede of S992, eight oath-entry sentence repairs, criterion 40).
Each repair was re-checked by attempt 2: every new quoted fragment counts 1 in its capture (`grep -c -F`), and the
frozen counter was re-run (below). Discarded: the unpinned draft `mutants98.py` and `attacks_critic98.py` of the dead
seats count as no evidence; the w2 seats re-derived them.

## Measured before → after (frozen counter `reports/round-98/predispatch.py`)

Counting command: `python3 -B reports/round-98/predispatch.py --root . --work <scratch> --base-rev bcf664aa089ddbd1fac85772ed22a38d1b454d23`.

| leg | base `bcf664aa` (do-nothing control `predispatch-base.txt`) | landed tree (tool v10 `d35b13c9…`) |
|---|---|---|
| O0 tool sha ≠ v9 | FAIL (sha = v9) | PASS |
| O1 selftest ≥160 | FAIL 155/155 | PASS 161/161 |
| O2 battery98 | FAIL survivors=5 unnamed=0 refused=31 | PASS 0/0/36/0/3/0, driver = pin = v9 receipt (all in freeze commit) |
| O3 mutation98 | FAIL driver missing (red-before over v9: 117/128, 11 broken-pattern) | PASS 128/128 killed, 0 survived, 0 broken, driver `dd88caec…` = pin = first receipt |
| O4 REG | PASS (guard) 34/34 | PASS 34/34 |
| O5 critic97 replay | FAIL survivors=8, DEL1 ENC1 ROMAN1 SUP1 FWPER1 not refused | PASS survivors=3 (benign CYRH1/ZWSH1/BELH1 rc 0) refused=22 |
| C1 entry | FAIL absent | PASS 47760 B, 13 h2, table 7×5, 6/6 phrases, topic equal |
| C2 registry | FAIL 917 rows, highest S993, 0 qualifying | PASS 930 rows, highest S1006, 11 qualifying |
| C3 append-only | PASS (guard) | PASS added=14 removed=1 in-place=1 (S992 status/used-by) illegal=0 |
| C4 census | PASS (guard) | PASS rc 0 |
| C5 index | PASS (guard, 269) | PASS 270/270/0 |
| C6 ids cited | FAIL | PASS 11/11 |
| C7 captures | FAIL | PASS 11/11, 17 captures verified |
| C8 content sweep | PASS (guard, owners 0) | PASS owners 0 of 270 |
| C9 non-author re-open | FAIL | PASS 10 ids (ReviewerC98 `reopen.json`) |

Landed-tree receipt: `reports/round-98/predispatch-lands.txt` (L1 run). Independent runs: ReviewerO98b
`PREDISPATCH-98: PASS legs=15/15` rc 0 (`.ufo/waves/round-98/w2/ReviewerO98b.md` §1); ReviewerC98 C1–C9 PASS.

**Harm findings outside the frozen predicate (non-author, claim O).** ReviewerO98b F4 and CriticO98b
over-refusal 1: v10 widens the heading combining-mark check from Mn/Me to all M, so a valid h2 heading with a
spacing mark (Mc, e.g. Devanagari visarga U+0903) is CLEAN on v9 and `FAIL TOPIC` (`HEADING-COMBINING`) on v10.
ReviewerO98b F1: the `HEADING-NUMBER` loop refuses a bare non-ASCII-numeral heading (`## Ⅳ.`) that cannot anchor,
so it protects nothing and refuses a valid entry. Measured lane exposure: 0 of 3010 h2 headings in
`corpus/knowledge` carry an Mc mark, 0 are non-ASCII-numeral-only (L1 python sweep, rc 0). These are two
false-refusal surfaces new in v10. The grader was not changed after the mutation first measurement (the pin binds
those bytes); the fix is routed to round 99. Claim O therefore meets its frozen predicate with two recorded
over-refusal regressions; the admission ruling ("no axis harmed") is the closure's.


## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R98-M1 | Gate-table hash names no capture file (round-97 closure routed defect 3: S993's hash is the PDF while its quote is counted in the `.txt`) | `corpus/lessons/round-97-verifier-spotcheck.md` §5 item 3; `corpus/lessons/round-97.md` Gate table (no `capture file` column) | none (no tool read the Gate table) | new `tools/check-gate-captures.py` (ExecGateCaps98) + this lesson's Gate table carries a `capture file` column with full 64-hex hashes. Shown able to fail: `python3 -B tools/check-gate-captures.py corpus/lessons/round-97.md reports/round-97/evidence` → rc 1, `GATE-CAPTURES: 9 finding(s) in 9 row(s)`; selftest case S993 pdf-vs-txt → SHA-MISMATCH (`SELFTEST PASS 13/13`, `.ufo/waves/round-98/w1/stage/ExecGateCaps98/`); this lesson → see §Gate check |
| R98-M2 | entry sentence contradicts its cited source (R97-M2 class recurs) | ReviewerC98 §support: entry line 142 "The office is not a modern invention in the record" vs S999 "conspicuously absent" / "not attested before the 19th century"; CriticC98 F2 "as much as" vs capture "so much as" (S996) | the frozen counter measures presence and binding, not sentence support; caught by ReviewerC98/CriticC98 | L1 repair before landing: line 142 rewritten on the two S999 quotes (each count 1 in `reports/round-98/evidence/S999.txt`); §8 grounding line quotes "so much as" (count 1 in S996.txt); §8 table preamble marks every unquoted cell as design; §13 ledger preamble corrected |
| R98-M3 | registry teaches cell carries a word no capture grounds | CriticC98 F1: S994 teaches "Oceanic …"; `grep -r -l Oceanic reports/round-98/evidence` → none | none (C7 binds the quote, not the teaches cell) | S1006 supersedes S994 (CORPUS rule 2; S994 status mined → queued, used-by → —); entry citations re-pointed to S1006; manifest entry S1006 bound to `S1006.txt` (sha equal to S994.txt) |
| R98-M4 | oath entry (round 96) sentences not supported by their captures | ReviewerOath98 `stage/ReviewerOath98/support.md`: 22 sentences, 11 supported, 3 weak, 5 unsupported, 3 contradicted | none at round 96 (R97-M2 class; the round-97 sweep routed it here) | 8 defective lines repaired (L47, L82, L92, L96, L118, L120 + L122 merged, L126) with new quotes each count 1 in `reports/round-96/evidence/S976/S978/S984.txt`; the 3 weak lines (L49, L51, L53) are routed to round 99 |
| R98-M5 | seats lost with the orchestrator session, no report | `.ufo/waves/round-98/w1-results.json` (output null for all 13); no `MutationTester98.md`, `CriticO98.md`, `ReviewerO98.md` | none | residual wave `w2` (3 seats) re-ran the mutation, critic and non-author review items; the dead seats' drafts were not counted |

## Gate

Rows written this round (`corpus/SOURCES.md`, appended after S993; opened 2026-11-05 by plain curl `-L --max-time 30`,
default user agent; quote counts on the named capture file; `reports/round-98/evidence/manifest.json`):

| id | URL | access | HTTP | tier | status | located quote (≤25 words) | capture file | capture sha256 | attempts |
|---|---|---|---|---|---|---|---|---|---|
| S994 | https://www.gutenberg.org/cache/epub/598/pg598.txt | 2026-11-05 | 200 | A | queued | “Then it was the custom of many to empty the brage-goblet” (11 words; count 1) | S994.txt | `1c3850032b20ce159eba4b8dba4b8b5a2647561aede41842f67bd1eaf123af2d` | 1 |
| S995 | https://is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/36 | 2026-11-05 | 200 | B | mined | “strengdi hann þá heit að hann skyldi auka ríki sitt hálfu í hverja höfuðátt eða deyja ella” (17 words; count 1) | S995.txt | `f18df855dad84f3dc9fe31f615a73491b20dcef009d9d308f9f867d410c21b86` | 1 |
| S996 | https://www.gutenberg.org/files/1600/1600.txt | 2026-11-05 | 200 | A | mined | “libations were offered, and after a hymn had been sung to the god,” (13 words; count 1) | S996.txt | `5beae4c6964d6a2c955544c376f14c9f39a8d84774a21c49d630365fa041e922` | 1 |
| S997 | https://www.gutenberg.org/files/1181/1181-0.txt | 2026-11-05 | 200 | A | mined | “Quite right (said Callias), and we will pledge you.” (9 words; count 1) | S997.txt | `d6da26aa8776d7269f37d0bf4e170d1113f1ce4340443f7b9ffdc89acae8f519` | 1 |
| S998 | https://www.gutenberg.org/cache/epub/66508/pg66508-images.html | 2026-11-05 | 200 | A | mined | “the pledge-cup to the Good Deity” (6 words; count 1) | S998.txt | `75aae7dab036feffb743daa4242241a3d44b9abb06b805d50d6fd50d398681b4` | 1 |
| S999 | https://www.mapageweb.umontreal.ca/tuitekj/publications/Tuite-supra.pdf | 2026-11-05 | 200 | B | mined | “The order of toasts, especially in the opening phase of” (10 words; count 1) | S999.txt | `35f309b24b671f73a424dcd9f6541fe5b4604e0148e1cc5b47bd674a5dbca4aa` | 1 |
| S1000 | https://www.gutenberg.org/cache/epub/981/pg981.txt | 2026-11-05 | 200 | A | mined | “and the high-born lady handed the cup first to the East-Danes' heir and warden,” (14 words; count 1) | S1000.txt | `112fe18ee0690a88451c928b0c4382adf5a2be828d8d8a12d638f53650d07b40` | 1 |
| S1001 | https://www.anthroencyclopedia.com/entry/feasting | 2026-11-05 | 200 | B | mined | “Toasting, which links two uses of the mouth (communication and consumption) is a concrete expression of accord in mind and communion in body.” (23 words; count 1) | S1001.txt | `97806a7fbe9211630f5e7945ba708d1206b03278fd2f5a0215e374da0de05779` | 1 |
| S1002 | https://www.melocki.org.uk/monmouth/History.html | 2026-11-05 | 200 | B | mined | “Your answer to her must be 'Drinc heil'” (8 words; count 1) | S1002.txt | `281f021b03773cc7aac5f61441b8204a688e082832155985f91235fdad34afac` | 1 |
| S1003 | https://archive.org/stream/mlbd.sacredbooksofeas0000fmax.vol.28/mlbd.sacredbooksofeas0000fmax.vol.28_djvu.txt | 2026-11-05 | 200 | A | mined | “they bow when the cup is received, and when it is presented (in return)” (14 words; count 1) | S1003.txt | `ce54f01d59c11043399ac79de6011f54fb5ab059af535482745f39611597ccb7` | 1 |
| S1004 | https://hal.science/hal-01974763/document | 2026-11-05 | 200 | B | mined | “the toastmaster had to down a glass at one go after every toast (refusing to do so was a breach” (20 words; count 1) | S1004.txt | `41484c9fdc467a9200fa71f91b74c93098cbad8227ea57d535f7973d456f3d41` | 1 |
| S1005 | https://www.gutenberg.org/files/37985/37985-0.txt | 2026-11-05 | 200 | B | mined | “Soon these 'Flytings' (_Naqá’iḍ_) were recited everywhere, and each poet had thousands of enthusiastic partisans who maintained that he was superior to his rival.” (24 words; count 1) | S1005.txt | `e356cd7d2e57677d48413768956fa9b517ed8f28d9ff8ff63b3651cfa0893066` | 1 |
| S1006 | https://www.gutenberg.org/cache/epub/598/pg598.txt | 2026-11-05 | 200 | A | mined | “Then it was the custom of many to empty the brage-goblet” (11 words; count 1) | S1006.txt | `1c3850032b20ce159eba4b8dba4b8b5a2647561aede41842f67bd1eaf123af2d` | 1 |

S994–S1004 are the claim-C candidates (S994 superseded by S1006 before landing, see R98-M3). S1005 supersedes the
round-97 row S992 (tier A → B, round-97 closure routed defect 1); S992 in place: status `mined` → `queued`, used-by
`corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` → `—` (`.ufo/waves/round-98/w1/stage/ExecRegistry98/s992.md`).
S994 in place (row added this round): status `mined` → `queued`, used-by entry → `—`.

Rejected or not admitted (`.ufo/waves/round-98/w1/stage/ScoutSources98/candidates.md`, 26 opened, 11 admitted,
15 rejected), each with reason and flip:
- C2, C4–C8 (Ynglinga saga ch. 35, 37–41, Wikisource, HTTP 200): no toast, cup or oath text (grep `bragaf` 0); flip: none (wrong chapter).
- C14 (Gutenberg 981-0.txt): HTTP 404; the same translation is admitted at cache/epub/981 (S1000).
- C17 SAGE Encyclopedia of Alcohol "Toasting": 403 + SSO; flip: a plain 200 copy.
- C18 Pace Law Review: 403; flip: an open copy.
- C19 Leaves (doi 10.21412/LEAVES_1003): 4 attempts timed out (rc 28); flip: a successful fetch.
- C20/C21 Kyoto repository: JS landing shell only; flip: a served PDF.
- C22 ctext.org Liji: bot-challenge page, no bypass; C23/C24 sacred-texts Li Ki: 403 — the same Legge translation is admitted via archive.org (S1003).

Counting command for the manifest fields (round-97 closure routed defect 4):
`python3 -c "import json;m=json.load(open('reports/round-98/evidence/manifest.json'));print(len(m),sum(len(e['captures']) for e in m),sum(1 for e in m if e.get('quote_capture')))"`
→ `13 19 13` (13 entries, 19 `captures[].file` fields, 13 `quote_capture` fields), rc 0.

Gate check (R98-M1): `python3 -B tools/check-gate-captures.py corpus/lessons/round-98.md reports/round-98/evidence` → rc 0, `GATE-CAPTURES: 0 finding(s) in 13 row(s)` (receipt `reports/round-98/gate-captures-lands.txt`).

Assimilation: none (`considerthese/` does not exist in this lane; shokuknow `merge/kotodama/` not adopted this round).

## Routed defects of round 97 (`corpus/lessons/round-97-verifier-spotcheck.md` §5)

1. S992 tier — S1005 supersedes (above).
2. Pin timing — battery98, its pin and its v9 receipt are in the freeze commit `db88f107` (QUALITY criterion 40).
3. Gate-table capture file — R98-M1.
4. Manifest counting command — stated above.
5. CriticO97 survivors — claim O; the oath-entry support sweep — R98-M4.

## Routed to round 99

1. v10 over-refusals: restore Mn/Me on the heading combining check (`tools/check-advance-evidence.py:742`,
   ReviewerO98b F4; fix the docstring) and drop or narrow the `HEADING-NUMBER` loop (`:757-766`, F1); pin both with
   benign selftest twins (Mc heading, bare numeral heading) so the regression can fail.
2. CriticO98b survivors (24 classes, same on v9 and v10, `.ufo/waves/round-98/w2/stage/CriticO98b/attacks.md`): verdict
   window whitelist (`LØCATED`, `ŁOCATED`, `LOCAÐTED`; Po/So/Sk/Lm/Co/Cn; mid-token TAB/space) and generic list-mark
   stripping in heading tokens (letters, `§`, `№`, `#`, `1.1.1`, circled letters).
3. ReviewerO98b F2 (dead `_dispo_match` Me branch), F3 (unpinned NFKD Me branch `L⃝OCATED`), F5 (generic TOPIC name for
   ROMAN1/SUP1/FWPER1).
4. Oath entry weak lines L49, L51, L53 (ReviewerOath98 `support.md` R-items).
5. Freshness remains paused until L0 answers (round-11, round-89).


## Sources census

- Start: `.ufo/waves/round-98/census/census-start.txt`, rc 0.
- End: `.ufo/waves/round-98/census/census-end.txt` (written at landing).
