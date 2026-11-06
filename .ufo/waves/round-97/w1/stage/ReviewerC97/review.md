# ReviewerC97 — independent non-author review of claim C (round 97, attempt 1)

Lane: kotodama. Base 1ffc5a83d2c70e3bc581594efbcf32c562ba2569. Entry: corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md (37387 B, 13 h2). Edits: none by this seat.

## 1. Frozen counter (read-only run, final)

Command: `python3 -B reports/round-97/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --work /fast/scratch/hyaku/kotodama-r97/ReviewerC97/counter --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569` — rc=1. Saved: stage/ReviewerC97/counter.txt.

```
LEG O0 PASS tool-sha256 1021dc9db778042d8049920292d96930f31481e77bce2b36f577ea2d88b5717b (must differ from v8 f29ab013...)
LEG O1 PASS 155/155 floor=154 rc=0
LEG O2 PASS survivors=0 unnamed=0 refused=31 required=0/0/31 traceback-free=True rc=0 pin=receipt=driver
LEG O3 FAIL sha pin missing or malformed: reports/round-97/controls/mutants97.sha256
LEG O4 PASS 34 baseline REG lines, 34 byte-identical in battery97 output
LEG C1 PASS bytes=37387 h2=13 table=7x6 phrases=6/6 topic-line=equal
LEG C2 PASS rows=917 highest=S993 new=9 qualifying=8 (min rows 911, highest >= S987, qualifying >= 3)
LEG C3 PASS added=9 removed=0 (removed must be 0)
LEG C4 PASS census rc=0
LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=269 rows=269 findings=0
LEG C6 PASS qualifying ids cited in entry: 8/8 uncited=[]
LEG C7 PASS qualifying ids with capture: 8/8 missing=[]
LEG C8 PASS files scanned=269 other owners=0 []
PREDISPATCH-97: FAIL legs=12/13
```

- Claim C legs C1–C8: **8/8 PASS**. The only failing leg is O3 (mutants97 pin not yet landed; MutationTester97 still running). Claim O is not judged here.
- Pre-dependency run (same command, before ScribeEntry97/ExecRegistry97 DONE): rc=1, `PREDISPATCH-97: FAIL legs=4/13`, identical to `reports/round-97/predispatch-base.txt`. The counter reproduces its control.
- Note: the frozen counter checks presence, counts and pins. It does not test whether a cited sentence is supported by its source. Section 4 is the only support check in this review.

## 2. Re-open of admitted sources (plain curl, -L, --max-time 30, curl's default user-agent string `curl/8`, retries per criterion 38)

Every fetch returned on attempt 1 (http 200, rc 0). Attempts logged in scratch `attempts.log` (removed at exit); summary here.

| id | url | http/rc/attempts | fresh bytes | fresh sha256 | pinned (manifest / lane capture) | quote count on fresh bytes |
|---|---|---|---|---|---|---|
| S975 (r96) | books.openedition.org/editionsehess/2703?lang=en | 200/0/1 | 239229 | 33c896a6…a8f2 | raw_sha256 33c896a6…a8f2 — **match** | text=1, raw=1 (19 words) |
| S984 (r96) | thetorah.com/article/yhwhs-covenant-… | 200/0/1 | 1157112 | f008c784…5538 | raw 4c62ddf7…e815, raw_bytes 1157108 — **drift** (+4 B, sha differs) | text=1; raw HTML=10 (markup duplicates the sentence) |
| S989 | repo.ignatianum.edu.pl/pl/file_records/866/download | 200/0/1 | 130290 | 8a59f531…4292 | lane S989.pdf sha 8a59f531d9e6… — **match** | pdftotext: ws-normalised=1 |
| S992 | gutenberg.org/files/37985/37985-0.txt | 200/0/1 | 1203657 | e356cd7d…3066 | lane S992.txt sha e356cd7d2e57… — **match** | ws-normalised=1 |
| S993 (Threnoi row source) | journal.oraltradition.org/…/23ii/07_23.2.pdf | 200/0/1 | 302080 | 1e53dabf…5599 | lane S993.pdf sha 1e53dabf8805… — **match**; S993.txt (pdftotext) sha 9c1a33a2… matches manifest captures[] | ws-normalised=1 |

Commands: `curl -L --max-time 30 -A curl/8 -o <file> -w '%{http_code}' <url>` (rc recorded per attempt). Quote counts: python `str.count` on raw bytes and whitespace-normalised text, with HTML tags stripped for html captures.

Lane capture checks (`reports/round-97/evidence/`):
- Manifest top-level `sha256` pins the text capture for S985–S992 (all match, verified by `hashlib.sha256` on each `S98x.txt`/`S99x.txt`). S987 pins its .html; S993 pins its .pdf and S993.txt via captures[].
- **Defect (manifest):** `manifest.json` `captures[].file` names for S985–S992 (e.g. `pagliai_2009.txt`, `hoebel_1954_capture.txt`, `lokasenna_bellows.html`, `ruszkiewicz_2020.txt`) do not exist; the files are `S98x.*`. Counter C7 passes only because it matches by id prefix. Recorded as a manifest defect.
- **Defect (quote):** `judgement` (S986 sentence, line 97) is not a substring of S986.txt (count 0, `str.count`, rc 0). The capture reads `judg- M … mcnt` (OCR hyphenation) and the source spelling is "judgment".

## 3. Quote recount on the lane captures (all 25 quoted fragments in cited sentences)

Command: python, for each `"…"` fragment in the 16 cited sentences and the funerary S993 sentence, `count` on the capture named by the cited id (`.txt`, or `.html` after tag stripping). Result: **24 fragments count == 1** (raw and ws-normalised); **1 fragment ("judgement", S986) count == 0** (see defect above). Word counts are ≤20 per fragment.

## 4. Support table — cited sentences in the new entry (16), plus the funerary S993 sentence

Scale: **S** = supported by the captured passage; **W** = weak (partly supported, or a clause outruns the source); **U** = unsupported or contradicted by the captured passage.

| # | line | cited | claim (abridged) | verdict | evidence in capture |
|---|---|---|---|---|---|
| 1 | 37 | S985 | duel = argumentative genre, two parties, challenge, performative display, audience | S | S985.txt @8231 & @8337: "a genre of argumentative language that entails exchanges between two persons, parties, or characters that challenge each other to a performative display of verbal skillfulness in front of an audience" |
| 2 | 44 | S985 | duels vary in form; may be sung or spoken, improvised or memorized | S | S985.txt @10644: "they can be improvised or memorized, or even written down; sung or spoken" |
| 3 | 48 | S985 | catharsis reading is a common view that scholarship criticises | S | S985.txt @145: "A common view of verbal duels posits that they are a cathartic expression of aggression" (the article's opening frame) |
| 4 | 64 | S988 | flyting = verbal competition, heaping abuse; a literary game | S (hedge dropped) | S988.txt @145/@233; source: "It was presumably, at least in part, a literary game." Entry drops "presumably" |
| 5 | 66 | S989 | Scottish flyting's main purpose: to humiliate the opponent | S | S989.txt @1497: "the Scottish genre of flyting, whose main purpose was to humiliate the opponent" |
| 6 | 68a | S987 | "The exchange or contest of insults was dear to the Norse heart" | S | S987.html @8955 (introductory note) |
| 7 | 68b | S987 | Lokasenna frame: guest "not invited", "demands a place and is given one", Loki's entry | W | S987.html @12266 has the entry and silence; Loki asks "At your feast a place and a seat prepare me" and Bragi answers "A place and a seat will…" (so "demands a place … is given one" is supported). "not invited" does not occur in the capture (grep `invit`: 0; `uninvit`: 0); it is an inference from "Or bid me forth to fare". |
| 8 | 70 | S992 | Arabic naqāʾid: recited everywhere; each poet had thousands of partisans | S | S992.txt @457796 (re-opened fresh, ws=1): "Soon these 'Flytings' (_Naqá’iḍ_) were recited everywhere, and each poet had thousands of enthusiastic partisans…" The entry calls Nicholson's history "the survey of the form" — a 1907 literary history; wording acceptable. |
| 9 | 85 | S985 | avoid conflating verbal duels with ritual insults (substantially different) | S | S985.txt @7668: "it is important to avoid conflating verbal duels with ritual insults, since these are substantially different, albeit overlapping, genres." |
| 10 | 95a | S986 | song duels are juridical instruments; settle disputes; restore relations | S | S986.txt @222572: "The song duels are juridical instruments insofar as they do serve to settle disputes and restore normal relations…" |
| 11 | 95b | S986 | song-duel complex "all down the west coast"; "reported together with its use among the Polar Eskimos" | **U** | The quote (west coast of Alaska and Aleutians) is supported. The Polar Eskimo mention in S986 is not about song duels: "Rasmussen noted a similar case among the Polar Eskimos" (a stabbing/execution passage, S986.txt @~ 'Polar'). The entry's "its use among the Polar Eskimos" misattributes it. The sentence's untagged clause "festive occasions … sporting performance … stealth and ambush excluded" IS supported (S986: "the contests are announced and occur on festive occasions… Stealth, cunning, and ambush are not part of such contests") but is not cited and is labelled "design, not sourced". |
| 12 | 97 | S986 | East Greenlanders song duels "may be carried on for **days** at a time"; decision by a **named office**; "judgement"; "judge is a named role inside the contest" | **U (contradicted)** | S986.txt @214147: "Among the East Greenlanders song duels may be carried on for **years**, just for the fun of it." The entry's "days at a time" contradicts the source. "named office": no office is named in the song-duel passage. "judge is a named role": the source says "He who is most heartily applauded is 'winner'" (audience applause decides), no named judge. "judgement" in quotes: source is "judg- ment" (OCR) — the quoted string is not in the capture (count 0). |
| 13 | 116 | S985 | one sung form: poets exchange stanzas on an audience-proposed theme | S | S985.txt @ 'propos' hit: "The poets duel by exchanging octets, stanzas of eight verses in hendecasyllables… on a theme usually proposed by the audience." "sung": the same passage belongs to the contrasto, "a genre of sung, improvised verbal duel" |
| 14 | 128 | S985 | audience decides what is an insult; performance between poets and audience is the key | S | S985.txt @37696: "Furthermore, in verbal duels, the audience is fundamental in deciding what is or is not an insult, …" and "…the performance between poets and audience is therefore the key." (exact substring, count 1) |
| 15 | 135 | S990 | Consistory → first championship, with rules, judges' panel, prizes; verdict public — "…choosing Xalbador to participate in the **next round**" | **W (misquote)** | S990.txt @20594: "…with its rules, judges' panel, and prizes" — supported. S990.txt @63231: "…choosing Xalbador to participate in the **final round** alongside the reigning champion Uztapide." The entry writes "next round"; source says "final round". The entry's "public verdict" clause is supported. |
| 16 | 137 | S991 | balagtasan: indigenous competitive debate poetry; joust with overseeing judge or emcee-adjudicator; the lakandiwa | S | S991.txt @1204 and @1317: "Balagtasan is an indigenous form of competitive Filipino debate poetry in the Tagalog language. It is a literary joust between two poets with an overseeing judge or emcee-adjudicator…"; "the lakandiwa or judge" (S991, author note) |
| F | funerary L (new paragraph, not in the new entry) | S993 | "A Greek case supplies the same office [professional mourner] under another name: in the Maniat lament of **Epirus** the dirge has a professional leader …" | **U (contradicted)** | S993.txt @~53957: the koriféa is "a single female lamenter … emerges from among the collective mourners … as a leader who improvises a solo lament." The source states the modern Maniat thrínos "holds no association with professional mourners" (p.124). "Epirus": the source places Maniat laments in Inner Mani (Peloponnese); Epiros is a separate comparison ("modern rural Epiros, Crete, and Inner Mani"). The funerary sentence therefore contradicts its source on both the office and the region. |

Tally (16 new-entry sentences): **12 supported** (rows 1, 2, 3, 4, 5, 6, 8, 9, 10, 13, 14, 16), **2 weak** (rows 7, 15), **2 unsupported** (rows 11, 12; row 12 contradicted). Total 16. The funerary S993 sentence (row F) is **1 unsupported (contradicted)**.

### Table §8 (seven data rows: six traditions and the ritual insult) — cell-level

The table's own preamble says "each row is grounded in the registry row named beside it". Cell check:

- Scottish flyting — adjudicator "the assembled company or a judge": not stated in S988/S989 captures. **U (unverified)**.
- Norse senna — contestants "a guest and a host, or two guests"; stakes "reputation, standing, and who yields": not stated in S987. **U (unverified)**.
- Inuit song duel — adjudicator "a judge inside the contest": the captured passage says the winner is the most applauded singer (audience). **U (contradicted)**.
- Arabic naqāʾid — "the crowd's partisanship": supported by S992 (partisans). **S**.
- Basque bertsolaritza — "a judges' panel", "rules and prizes": supported by S990. **S**.
- Filipino balagtasan — "a named moderator (lakandiwa)": supported by S991. **S**.
- Ritual insult row ("sung or spoken, one-directional"; "no opponent; the ritual carries the liability"; source "Pagliai 2009"): S985 says ritual insults are different from duels; it does not describe their structure. **U**.

Grounding list (§8, lines 163–170): the S985 ritual-insult line quotes the cathartic sentence, which is about verbal duels, not ritual insults. It does not ground the ritual row. **W**.

## 5. Other checks

- **Phrase hits natural (6/6 in headings):** "verbal duel" in `## 2. The verbal duel: …`; "ritual insult" in `## 4. Ritual insult across traditions`; "flyting" in `## 3. Flyting and senna: …`; "song duel" in `## 5. Song duels: …`; "boast formula" in `## 6. The boast formula: …`; "audience adjudication" in `## 7. Audience adjudication: …`. The H1 also carries "verbal duelling". No stuffing in prose.
- **Topic line:** byte-equal to the frozen topic (C1 `topic-line=equal`).
- **Table shape:** 6 columns × 7 data rows (header + separator outside the count). C1 counter reset per table: counted correctly.
- **Non-canon:** the entry marks invented material "NON-CANON" (2 occurrences, including the micro-example at §11). Canon is deferred in §1 (line 27: "What is true in any world is lore-shokunin's") and §12 (lines 253–255, handoff to the lore world bible). The entry does not cite lore-shokunin/PROVINCE.md, which sibling entries (kongo-kingdom.md:151, footwear-codes-terminology.md:10) do. Not a frozen leg; an observation for the L1. **Non-blocking.**
- **README edit (corpus/README.md):** `## linguistics/ (41)` → `(42)`; row `verbal-duelling-ritual-insult.md` inserted in filename order (after translation-protocol-fidelity.md, before writing-systems.md); footer section "Round 97 verbal duelling entry" added; 268 → 269. Directory totals 42+36+43+29+24+95 = 269. Consistent with C5 (`files=269 rows=269`). Diff: 1 deletion, 20 insertions (`git diff 1ffc5a83… -- corpus/README.md`). Correct.
- **Funerary edit:** `git diff 1ffc5a83d2c70e3bc581594efbcf32c562ba2569 -- corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`, rc=0: exactly one added paragraph (2 added lines, one blank plus one sentence) after the Irish gendered-office paragraph. No other change to that file. The sentence itself is row F (**contradicted**).
- **Registry rows S985–S992:** all `tier` A/B, `status` mined, date 2026-11-05, `used-by` the entry path; each exact locator counts 1 (table in §3). Row S993 (Threnoi) is used-by the funerary file, outside claim-C counts; its "what it supports" text says the article "names the professional dirge leader (koriféa)" — the capture does not support "professional" (see row F). **Defect in the S993 row description.**
- **Uncommitted lane state (not claim C, noted):** `corpus/QUALITY.md` shows a 6-line working-tree modification (`git status`). Not reviewed; not part of claim C.

## 6. Findings by severity

1. **High — row 12 (line 97): contradicted quote.** The entry says East Greenlanders' song duels "may be carried on for days at a time"; the source (S986) says "for years, just for the fun of it". The sentence also asserts a "named office" and a "named judge" that the captured passage does not contain, and quotes "judgement" which is not in the capture.
2. **High — funerary sentence (new paragraph, funerary-lament-dirge-formulae.md): contradicted by S993.** S993 says the Maniat thrínos "holds no association with professional mourners"; the entry's "same office … professional leader" conflicts with that. "Maniat lament of Epirus" misplaces Maniat (Inner Mani, Peloponnese).
3. **Medium — row 11 (line 95): misattribution.** "its use among the Polar Eskimos" is Rasmussen's murder-case aside, not song-duel use.
4. **Medium — row 15 (line 135): misquote.** "next round" should be "final round" (S990).
5. **Medium — §8 table cells:** Inuit song duel "a judge inside the contest" is contradicted (applause decides); Norse senna cells, Scottish flyting adjudicator, and the ritual-insult row (Pagliai 2009) are not supported by their named sources. The table preamble overclaims grounding.
6. **Low — row 7 (line 68):** "not invited" is an inference; the capture supports "a place and a seat" only.
7. **Low — row 4 (line 64):** "presumably" dropped from the S988 literary-game hedge.
8. **Low — manifest:** `captures[].file` names for S985–S992 point to nonexistent files; C7 passes by id prefix only.
9. **Low — registry S993 row:** "professional dirge leader" contradicts its own source.
10. **Low — S984 (round-96 admitted source) drift:** raw bytes +4 (1157108→1157112), sha256 changed; text quote still count 1; raw-HTML count 10. The pinned text capture is unaffected. Recorded only.
11. **Observation — counter scope:** C1–C8 measure presence and counts, not support. Findings 1–5 pass every frozen leg; claim C is mechanically PASS while its cited content is not faithful. This gap is the counter's design, not an edit target for this seat.

## 7. Verdict

- **Frozen counter, claim C:** legs C1–C8 **PASS (8/8)**. No C leg fails. Under the frozen kill rule, the claim-C predicate is met on the current tree.
- **Reviewer verdict on claim C as sourced coverage: FAIL.** First failing item: **line 97 (row 12)**, the "days at a time" misstatement that contradicts S986. The first failing *leg* is **none**; the counter does not test support. Before the L1 accepts claim C as sourced coverage, rows 11, 12, 15, the §8 table cells, the funerary S993 sentence, the "judgement" quote, and the S993 registry description need correction. Those are lane content edits for the L1; this seat edited nothing.

## 8. Verification gaps

- O3 pending (mutants97.sha256 not landed). Claim O not judged here.
- Entry text was judged against captured text only. Live pages were not re-fetched for S985–S992; the pinned captures were used, plus fresh re-opens of S989, S992, S993 (sha identical) and S975/S984 (round-96).
- Support judgments are this seat's reading of the captured passages; the table in §4 gives each judgment's evidence line.
