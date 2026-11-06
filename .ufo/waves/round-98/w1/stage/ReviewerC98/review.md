# ReviewerC98 — independent non-author review of claim C (round 98, attempt 1)

Lane: kotodama. Base bcf664aa089ddbd1fac85772ed22a38d1b454d23. Entry: corpus/knowledge/linguistics/toast-drinking-speech-formulae.md (47370 B, 13 h2, topic line byte-equal). Edits by this seat: only `.ufo/waves/round-98/w1/stage/ReviewerC98/` (reopen.json, counter.txt, review.md, DONE). Scratch `/fast/scratch/hyaku/kotodama-r98/ReviewerC98/` removed before yield.

## 0. Dependencies

Bounded wait (`for i in $(seq 1 180); do [ -f DONE ] && ...; sleep 60; done`): stage/ScribeEntry98/DONE and stage/ExecRegistry98/DONE both present at iteration 30 (rc 0).

## 1. Frozen counter (read-only run, after reopen.json landed)

Command: `python3 -B reports/round-98/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --work /fast/scratch/hyaku/kotodama-r98/ReviewerC98/counter --base-rev bcf664aa089ddbd1fac85772ed22a38d1b454d23` — rc=1. Saved: stage/ReviewerC98/counter.txt.

```
LEG O0 PASS tool-sha256 d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7 (must differ from v9)
LEG O1 PASS 161/161 floor=160 rc=0
LEG O2 PASS survivors=0 unnamed=0 refused=36 traceback=0 clean=3 not-clean=0 rc=0 pin=receipt=driver
LEG O3 FAIL sha pin missing or malformed: reports/round-98/controls/mutants98.sha256
LEG O4 PASS 34 baseline REG lines, 34 byte-identical in battery98 output
LEG O5 PASS tally=CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0 rc=0 not-refused-named=[] benign-not-rc0=[]
LEG C1 PASS bytes=47370 h2=13 table=7x5 phrases=6/6 topic-line=equal
LEG C2 PASS rows=929 highest=S1005 new=12 qualifying=11
LEG C3 PASS added=13 removed=1 in-place-status/recheck/used-by=1 illegal=0 []
LEG C4 PASS census rc=0
LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=270 rows=270 findings=0
LEG C6 PASS qualifying ids cited in entry: 11/11 uncited=[]
LEG C7 PASS qualifying ids bound: 11/11 captures-verified=17 failures=[]
LEG C8 PASS files scanned=270 other owners=0 []
LEG C9 PASS qualifying ids re-opened with count 1: 11 (min 3) [S994..S1004]
PREDISPATCH-98: FAIL legs=14/15
```

- **Claim C legs C1–C9: 9/9 PASS** at my measurement. No C leg fails; the first failing leg for claim C is **none**.
- The only failing leg is O3 (mutants98 pin not yet landed; MutationTester98 still running at review time). Claim O is not judged here. O5 already shows the five named forgeries refused and the three benign controls rc 0.

## 2. Re-open of the 11 qualifying rows (plain curl, default user agent, -L, --max-time 30)

Command: `curl -sS -L --max-time 30 -o <scratch>/fetch/<id>-1.bin -w '%{http_code}' <url>` (one URL per row, copied verbatim from the registry source cell). Criterion 38 retries armed (≤3 attempts, 20 s backoff on rc 28 / conn error / 429 / 5xx): **every row answered http 200 on attempt 1** (11 attempts total, 11 × rc 0). Full fetch log kept in scratch (removed at exit); per-row numbers below are the observed values written to stage/ReviewerC98/reopen.json.

| id | url (fetched, = source cell) | http/attempts | fresh bytes | fresh sha256 (16) | vs manifest capture sha | quote_count on fresh bytes |
|---|---|---|---|---|---|---|
| S994 | gutenberg.org/cache/epub/598/pg598.txt | 200/1 | 1748859 | 1c3850032b20ce15 | **match** | 1 |
| S995 | is.wikisource.org/wiki/Heimskringla/Ynglinga_saga/36 | 200/1 | 49860 | f1836735b006fc25 | **match** | 1 |
| S996 | gutenberg.org/files/1600/1600.txt | 200/1 | 200852 | 5beae4c6964d6a2c | **match** | 1 |
| S997 | gutenberg.org/files/1181/1181-0.txt | 200/1 | 132565 | d6da26aa8776d726 | **match** | 1 |
| S998 | gutenberg.org/cache/epub/66508/pg66508-images.html | 200/1 | 1433504 | da8df856ac4f42d3 | **match** | 1 |
| S999 | mapageweb.umontreal.ca/tuitekj/publications/Tuite-supra.pdf | 200/1 | 561533 | ac34ddfda0286622 | **match** | 1 |
| S1000 | gutenberg.org/cache/epub/981/pg981.txt | 200/1 | 170898 | 112fe18ee0690a88 | **match** | 1 |
| S1001 | anthroencyclopedia.com/entry/feasting | 200/1 | 84274 | a120b05abe3c0b70 | **match** | 1 |
| S1002 | melocki.org.uk/monmouth/History.html | 200/1 | 483734 | beb208d1cc546192 | **match** | 1 |
| S1003 | archive.org/stream/…28_djvu.txt | 200/1 | 1012349 | 84b14a3d9b041… | **drift** (data, not failure) | 1 |
| S1004 | hal.science/hal-01974763/document | 200/1 | 329909 | e78507faf87f17a2 | **match** | 1 |

Conversion as the captures were: pdftotext for S999/S1004 PDFs; tag-strip for S995/S998/S1001/S1002/S1003 HTML; plain text otherwise; whitespace-collapsed `str.count` of the manifest quote. 10/11 fresh byte-strings are sha256-identical to the lane capture. S1003 drift: the archive.org djvu text is served as an HTML "Full text of…" page; lane capture 1006079 B from `data-node=www20`, fresh fetch 1012349 B from `data-node=www12` (+6270 B of node/dynamic bytes); the quote "they bow when the cup is received, and when it is presented (in return)" counts 1 on both. C9 is satisfied 11/11, not merely the required 3.

## 3. Quote recount on lane captures (grounding list, §8)

Command: python, for each `"…"` fragment in the 12 grounding-list lines, ws-collapsed `count` against `quote_capture` (tag-stripped/pdftotext as above). Result: **23 of 24 fragments count == 1**; the 24th is S1001's `"Feasting"` (the page title, count 6) — the load-bearing fragments for that row ("Toasting, which links two uses of the mouth…", "before everyone simultaneously drinks") count 1. No fragment counts 0 or >1 except the title.

## 4. Support sweep — cited sentences (28 lines carry a registry id)

Scale: **S** = supported by the captured passage; **W** = weak; **U** = unsupported or contradicted.

| # | line | cited | claim (abridged) | verdict | evidence in capture |
|---|---|---|---|---|---|
| 1 | 54 | S1001 | toast joins the mouth's two uses; accord in mind, communion in body | S | S1001.txt: "Toasting, which links two uses of the mouth (communication and consumption) is a concrete expression of accord in mind and communion in body." |
| 2 | 56 | S1001 | standing, around a table, glasses touched or lifted, eye contact or gaze, simultaneous drink | S | same passage verbatim |
| 3 | 58 | S1002 | king told the lady "offered to drink your health" | S | S1002.txt: "She called you 'Royal lord'", said the interpreter, "and offered to drink your health." |
| 4 | 60 | S1002 | interpreter fixes the answer as a formula | S | "Your answer to her must be 'Drinc heil'"; custom line "he who drinks to any one says 'Wacht heil'! and he that pledges him, answers 'Drinc heil'!" |
| 5 | 89 | S1002 | formula shows its two halves | S | same passage |
| 6 | 91 | S1003 | host washes hands, rinses cup, raises it | S | "(The host) washes his hands, rinses the cup, and raises it,—to give the highest idea of purity." |
| 7 | 93 | S1003 | bows on receipt and on presentation in return | S | "they bow when the cup is received, and when it is presented (in return)" |
| 8 | 105 | S996 | supped, then libations and hymn, then drinking | S | "Socrates took his place on the couch, and supped with the rest; and then libations were offered, and after a hymn had been sung to the god…" |
| 9 | 107 | S998 | law: after solid food removed, taste of unmixed wine as sample of the Good Deity's power; rest mixed | S | Philochorus quote verbatim in S998.txt |
| 10 | 109 | S998 | cup-carrying linked to table removal, via a tyrant story | S | "when the pledge-cup to the Good Deity was handed round, it was customary to remove the tables, is made plain by the wicked action of Dionysius the tyrant of Sicily" |
| 11 | 111 | S1003 | vessel of liquor between room and door, host and guests sharing | S | "The chief of the district… had the vessel of liquor placed between the room (on the east), and the door…, host and guests sharing it between them." |
| 12 | 142 | S999 | office "not a modern invention in the record"; tamada selected even when two men; ideal holder qualities | **U (frame contradicted)** | The factual half is verbatim (S999.txt: "at every occasion where wine is to be consumed, even if only two men are present, one of them is selected to be tamada… knowledgeable, witty, and articulate, but also a good drinker"). But the frame inverts the source: Tuite argues the institution "may not be as ancient as many think", is "conspicuously absent" from courtly literature and early accounts, and "tamada and t'olumbaši… are not attested before the 19th century". |
| 13 | 144 | S999 | each round opens with a themed toast by the toastmaster, only he drinks | S | verbatim |
| 14 | 146 | S999 | guests reply one after the other on the same theme, then drink | S | verbatim |
| 15 | 148 | S999 | opening-phase order rigid; many rounds | S | "follows a quite rigid sequence… Anywhere from three… to three dozen or more rounds" |
| 16 | 150 | S999 | all wine in one draught ideally; in practice only the tamada obliged | S | verbatim |
| 17 | 152 | S1000 | queen hands cup first to heir and warden, then younger and older, then a named guest who answers | S | "handed the cup first to the East-Danes' heir and warden… to younger and older everywhere carried the cup, till… to Beowulf bore the beaker… The cup he took… and answer uttered" |
| 18 | 154 | S994 | order: victory/power → peace/good season → oath-named goblet → memory goblet | S | "first Odin's goblet was emptied for victory and power to his king; thereafter, Niord's and Freyja's goblets for peace and a good season. Then it was the custom of many to empty the brage-goblet (1); and then… the remembrance goblet" |
| 19 | 187 | S995 | feast-maker and heir stands against the bragafull, swears, drinks, then led to father's high seat | S | "Skyldi sá þá standa upp í móti bragafulli og strengja heit, drekka af fullið síðan. Síðan skyldi hann leiða í hásæti það sem átti faðir hans." ("strengthens the oath" is a literal gloss of *strengja heit*) |
| 20 | 189 | S994 | edition note: goblet over which vows were made; emptied after victory/peace | S | endnote "(1) The brage-goblet, over which vows were made.—L." + order above |
| 21 | 191 | S994 | memory turn, not promise | S | "a goblet to the memory of departed friends, called the remembrance goblet" |
| 22 | 193 | S997 | guests pledging one another; "Quite right (said Callias), and we will pledge you" | S | verbatim (Callias answering Socrates) |
| 23 | 195 | S997 | cup-bearers push cups round, quickening each circuit | S | "The cup-bearers should imitate good charioteers, and push the cups round, quickening the pace each circuit." |
| 24 | 210 | S994 | memory-cup vs oath-cup pairing | S (as tagged inference) | both S994 facts verified above; pairing flagged "(inference)" in body and §13 |
| 25 | 242 | S1004 | toastmaster must down a glass after every toast; refusing = breach; charge on the runner, not the decliner | S | "the toastmaster had to down a glass at one go after every toast (refusing to do so was a breach of etiquette)" |
| 26 | 244 | S1004 | toasts taken seriously; principles, denominational/national/local identity | S | "Toasts were taken seriously. They expressed a man's deeply-held principles, and his deeplyfelt denominational, national, and/or local identity." |
| 27 | 246 | S1004 | no man must drink against his principles; refusing = manliness, independence | S | "no man must drink a toast if it went against his principles. Refusing a toast was a mark of manliness and independence of mind." (entry drops the wry "It was a truth universally acknowleged" frame; see findings) |
| 28 | 248 | S996 | each drinks as he pleases, no compulsion | S | "that they were all to drink only so much as they pleased… there is to be no compulsion" |

Tally (28 cited sentences): **27 supported, 0 weak, 1 unsupported (line 142, frame contradicted)**. Minor hedges noted inline (12: "In principle" dropped; 27: ironic frame dropped).

## 5. §8 table — cell-level against the captures

The preamble says "Cells tagged *(design)* are proposals of this entry; the remaining cells rest on the source named in the grounding list underneath." Only 3 cells carry *(design)*. Checking untagged cells against the named captures (mechanical fragment search across all 11 captures, rc 0):

- **Supported (untagged):** "any guest, called in turn" and "the reply that quotes the theme" (S999 verbatim); "the full cup, drunk to the end" (S994 "empty"/S999 single-draught); "the memory-turn" (S994); "the first pour goes out and is not drunk" (S996 libations; S998 pledge-cup "as little as possible drunk out of it").
- **Not in any capture, presented as source-resting (untagged):** "drinking on the theme's last word" (official round; 'last word' occurs in S994/S998 only as "King Olaf's last words"/"these last words"); "speaking over the toast is not [possible]"; "a sip and a return of the wish" (personal round); "a late arrival is not a refuser; the opening may not be declined" (opening; S1003's arrival hits are the guest-arrival bow and an unrelated mourning note); "refusal here asserts enmity and is the most expensive turn" (memory/boast); the penalty-cup stage's three untagged cells ("the wronged party, or a standing office", "the named fault and the pre-declared tariff" — 'tariff' in S1004 is wine trade tariffs; "drunk in one, with no reply"); "the shortest toast of the sequence" (close; §5 tags the same content design, §8 does not).

## 6. Other checks

- **Phrase hits natural (6/6 in h2 headings):** "toast formula" §2 (line 39), "health-drinking" §3 (68), "libation" §4 (97), "toastmaster"/"toast sequence" §5 (122), "drinking oath" §6 (172; also 6.1 at 176), "toast sequence" §8 (252). 'toastmaster' also appears in §8 table cells as ordinary content ("the host, or the toastmaster"). No stuffing in prose.
- **Table shape:** 7 data rows × 5 cols; C1 counted table=7x5. Topic line byte-equal (C1 `topic-line=equal`; re-derived, True).
- **NON-CANON:** 2 occurrences (grep -c, rc 0), including the §9 worked micro-example. Canon deferral in §1 (line 33: "lore-shokunin records what is true inside a world; chousa owns the procedure…") and §12 (line 377, "The package lore-shokunin receives… The world bible supplies the people, the rite, the cup…"). The entry does not cite `lore-shokunin/PROVINCE.md` (grep PROVINCE in entry: 0) which some sibling entries do — same observation class as round 97; not a frozen leg.
- **Inference ledger mismatch (low):** §13 claims "Each is tagged *inference* in the body as well as here" and lists 7 items; the body carries only 1 `(inference)` tag (line 210) — the other six readings appear in the body tagged *design, not sourced* instead (grep -c '(inference)' = 8: 1 body + 7 ledger).
- **README edit (corpus/README.md):** `git diff bcf664aa… -- corpus/README.md` = 22 insertions, 1 deletion (rc 0): `## linguistics/ (42)` → `(43)`; new row in filename order with the `- topic:` text verbatim; "Round 98" section added; totals 269 → **270** with the counting command stated. Consistent with C5 (`files=270 rows=270`).
- **S992 correction:** `git diff bcf664aa… -- corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` (rc 0) changes exactly 3 lines, each the token S992 → S1005 (sources list, the quoted sentence, the grounding row); no other bytes. Registry: the S992 row's cells diff as exactly `status: mined→queued` and `used-by: …verbal-duelling…→—` (cell-level diff, rc 0); all fixed cells byte-identical (counter C3: removed=1, allowed=1, illegal=0). New row S1005 (tier B, mined, 2026-11-05, used-by the duelling entry) opens `supersedes S992 —` per the registry header's correction rule. Correct.
- **Working-tree state outside claim C (observation, not judged):** `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` (7 insertions, 9 deletions — reworded cited sentences/quotes) and `corpus/QUALITY.md` (+6 lines) are modified vs base. The oath edit matches routed defect 5 (ReviewerOath98's sentence-support sweep, outside claim counts); QUALITY.md matches the round-97 precedent of a pending working-tree edit. Flagged for the L1's commit hygiene.

## 7. Findings by severity

1. **High — line 142 (S999): contradicted frame.** "The office is not a modern invention in the record." The cited source's argument is the opposite: the supra-with-tamada "may not be as ancient as many think", the institution is "conspicuously absent" from older literature, and the words tamada/t'olumbaši "are not attested before the 19th century". The sentence's factual half is verbatim-supported; the frame misrepresents the source's central claim. One-clause fix (e.g., "attested in the record, though the source dates its words to the 19th century or later"); the design apparatus does not depend on the antiquity claim.
2. **Medium — §8 preamble overclaims grounding.** ~10 untagged cells ("drinking on the theme's last word", "a sip and a return of the wish", "the opening may not be declined", "refusal here asserts enmity", the penalty-cup stage's cells, "the shortest toast of the sequence") have no support in the named captures yet fall under a preamble that says untagged cells "rest on the source named in the grounding list". The same cells are tagged *(design, not sourced)* where they appear in §5/§7. Fix: add *(design)* tags or a design column marker.
3. **Low — §13 ledger self-description.** 7 ledger items, 1 body `(inference)` tag; six readings are body-tagged *design, not sourced*. Fix the ledger intro or move the tags.
4. **Low — dropped hedges.** Line 142 drops Tuite's "In principle"; line 246 drops Duthille's ironic "It was a truth universally acknowleged" framing. Both change tone, not facts.
5. **Observation — no `lore-shokunin/PROVINCE.md` pointer**, unlike some sibling entries. Not a frozen leg.
6. **Observation — counter scope:** C1–C9 measure presence, counts, pins and fresh re-opens; they do not test sentence support. Findings 1–3 pass every frozen leg. This gap is the counter's design, not an edit target for this seat.

## 8. Verdict

- **Frozen counter, claim C:** legs C1–C9 **PASS (9/9)** at my measurement; C9 satisfied by 11/11 qualifying ids (http 200, quote_count 1 on fresh bytes, observed values only). No C leg fails; first failing leg: **none**.
- **Reviewer verdict on claim C as sourced coverage: PASS, with one High content defect.** Unlike round 97, no cited sentence is misquoted or contradicted in its factual content, and every quote fragment recounts cleanly (23/24 count 1; the 24th is a page title). The single unsupported element is the framing clause at line 142 (finding 1), which the L1 should correct before dispatch; findings 2–3 are labeling defects worth fixing in the same pass. This seat edited nothing outside its stage.

## 9. Verification gaps

- O3 pending at review time (mutants98 pin/driver not landed). Claim O not judged here; O0/O1/O2/O4/O5 already pass on the landed grader.
- Support judgments are this seat's reading of the captured passages; §4 and §5 cite the capture evidence for each judgment. Fresh fetches agreed with the captures on all 11 rows (10 sha-identical, S1003 dynamic-page drift with quote intact).
- The counter does not fetch the network; C9's evidence is this seat's reopen.json, validated independently by the counter against the landed registry.
