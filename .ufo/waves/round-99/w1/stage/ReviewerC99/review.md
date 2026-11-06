# ReviewerC99 — independent non-author review of claim C (round 99, attempt 1)

Lane: kotodama. Base 527df3fee305b3454446946e6779ece45456307e. Entry: corpus/knowledge/linguistics/praise-poetry-panegyric.md (44922 B, 13 h2, topic line byte-equal). Edits by this seat: only `.ufo/waves/round-99/w1/stage/ReviewerC99/` (reopen.json, counter.txt, review.md, DONE). Scratch `/fast/scratch/hyaku/kotodama-r99/ReviewerC99/` deleted before yield. Tools installed: none. Host/pacman/sysctls untouched.

## 0. Dependencies

Bounded loop (`for i in $(seq 1 180); do [ -f DONE1 ] && [ -f DONE2 ] && break; sleep 60; done`): ScribeEntry99/DONE present early; ExecRegistry99/DONE landed while the loop ran (loop rc 0). Peer message from KotodamaR99 let me start the re-opens as soon as the registry rows + manifest were on disk; reopen.json was written before the whole-counter run, as counter leg C9 reads it.

## 1. Frozen counter (read-only, after reopen.json landed)

Command: `python3 -B reports/round-99/predispatch.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin --work /fast/scratch/hyaku/kotodama-r99/ReviewerC99/counter --base-rev 527df3fee305b3454446946e6779ece45456307e` — rc=0. Saved: stage/ReviewerC99/counter.txt (16 LEG lines + summary; wall 1046 s).

```
LEG O0 PASS tool-sha256 717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2 (must differ from v10 d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7)
LEG O1 PASS 175/175 floor=168 rc=0
LEG O2 PASS survivors=0 unnamed=0 refused=37 traceback=0 clean=9 not-clean=0 required=0/0/37/0/9/0 rc=0 pin=receipt=driver
LEG O3 PASS 34 baseline REG lines, 34 byte-identical in battery99 output
LEG O4 PASS tally=CRITIC-O98 survivors=24 unnamed=0 refused=1 traceback=0 overrefusal=0 rc=0 clean-not-rc0=[] unexpected-clean=[] plainmove-refused=True survivor-max=24
LEG O5 PASS tally=CRITIC-O97 survivors=3 unnamed=0 refused=22 traceback=0 rc=0 not-refused-named=[] benign-not-rc0=[]
LEG O6 PASS 136/136 killed, 0 survived, 0 broken-pattern (floor total 132) rc=0
LEG C1 PASS bytes=44922 h2=13 table=10x3 phrases=6/6 topic-line=equal
LEG C2 PASS rows=941 highest=S1017 new=11 qualifying=11
LEG C3 PASS added=11 removed=0 in-place-status/recheck/used-by=0 illegal=0 []
LEG C4 PASS census rc=0
LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=271 rows=271 findings=0
LEG C6 PASS qualifying ids cited in entry: 11/11 uncited=[]
LEG C7 PASS qualifying ids bound: 11/11 captures-verified=20 failures=[]
LEG C8 PASS files scanned=271 other owners=0 []
LEG C9 PASS qualifying ids re-opened with count 1: 11 (min 3) [S1007..S1017]
PREDISPATCH-99: PASS legs=16/16
```

- **Claim C legs C1–C9: 9/9 PASS** at my measurement; first failing leg for claim C: **none**.
- Claim O legs O0–O6 also PASS in this run (not judged by this seat; see ReviewerO99). Unlike round 98, no O leg was pending at review time.
- I re-derived C1 and C2 independently before the counter: bytes=44922, h2=13, best table 10x3, phrases 6/6 in h2, topic byte-equal (python, rc 0); rows=941, highest=S1017, new=11, qualifying=11 (python, rc 0). Both match the counter.

## 2. Re-open of the 11 qualifying rows (plain curl, default UA, -L, --max-time 30)

Command: `curl -sS -L --max-time 30 -o <scratch>/fetch/<id>-1.bin -w '%{http_code}' <url>` (URL copied verbatim from each row's source cell). Criterion-38 retries armed (≤3 attempts, 20 s backoff on rc 28 / conn error / 429 / 5xx): **every row answered http 200 on attempt 1** (11 fetches, 11 × rc 0, 0 retries). Per-row values below are the observed values written to stage/ReviewerC99/reopen.json.

| id | url (fetched, = source cell) | http/attempts | fresh bytes | fresh sha256 (16) | vs manifest capture sha | quote_count on fresh bytes |
|---|---|---|---|---|---|---|
| S1007 | archive.org/download/80204dff-c8a9-4155-a539-7ee980102875/…_djvu.txt | 200/1 | 1431723 | 73df25c214bd03c2 | match | 1 |
| S1008 | journal.oraltradition.org/wp-content/uploads/files/articles/3iii/6_opland.pdf | 200/1 | 122076 | 82e20d080362ec83 | match | 1 |
| S1009 | journal.oraltradition.org/wp-content/uploads/files/articles/20ii/Barber.pdf | 200/1 | 895589 | 679330595ed9cb63 | match | 1 |
| S1010 | journal.oraltradition.org/wp-content/uploads/files/articles/16i/Groenewald.pdf | 200/1 | 941966 | c04fa91bbf02bc86 | match | 1 |
| S1011 | www.journal.oraltradition.org/wp-content/uploads/files/articles/10i/8_kaschula.pdf | 200/1 | 678241 | 680667fd0ab57c26 | match | 1 |
| S1012 | www.gutenberg.org/cache/epub/10717/pg10717.txt | 200/1 | 320993 | d8823d133ebb5905 | match | 1 |
| S1013 | www.gutenberg.org/files/9842/9842-h/9842-h.htm | 200/1 | 412673 | 1c058141482623a8 | match | 1 |
| S1014 | archive.org/stream/book-3-purananuru/BOOK3-Purananuru_djvu.txt | 200/1 | 184857 | 727001ebfadb2929 | **drift** (data, not failure) | 1 |
| S1015 | journals.uni-goettingen.de/wom/article/download/2303/1986/5234 | 200/1 | 121791 | 3ae6a0816757bc04 | match | 1 |
| S1016 | www.asnc.cam.ac.uk/resources/mpvp/wp-content/uploads/2013/02/Introduction-to-Skaldic-Poetry_Debbie-Potts.pdf | 200/1 | 294812 | 9d5bc8134936916f | match | 1 |
| S1017 | mural.maynoothuniversity.ie/id/eprint/19500/1/Kavanagh%20Emer%20Signs%20and%20Wonders.pdf | 200/1 | 1897884 | 73809ae35594fdb1 | match | 1 |

(16-char prefixes shown; the 64-hex values are in reopen.json.) Conversion as the captures were: pdftotext for the 7 PDFs (S1008/S1009/S1010/S1011/S1015/S1016/S1017), tag-strip for HTML (S1013, S1014's HTML wrapper), plain text otherwise; whitespace-collapsed `str.count` of the manifest quote. 10/11 fresh byte-strings are sha256-identical to a manifest capture.

**S1014 drift:** the archive.org `/stream/…_djvu.txt` URL serves a dynamic "Full text of…" HTML wrapper (fresh fetch from `data-node="www21.us.archive.org"`, 184857 B; lane raw capture 191267 B from another node; the lane also stores the converted S1014.txt, 44945 B). The manifest quote "The main themes found in Purananuuru are praise of the ruler, patronage, heroism in battles" counts 1 on both fresh-tag-stripped and capture text (python `count`, rc 0). Same benign class as round-98's S1003. C9 is satisfied 11/11, not merely the required 3.

## 3. Support sweep — every cited sentence (70 lines carry a registry id)

Method: mechanical longest common n-gram per cited line against its named capture (10→4-word windows, ws-collapsed, python rc 0), then manual capture reads for every line below 6 words. Scale: **S** = supported by the captured passage; **W** = weak; **U** = unsupported or contradicted.

| group | lines | verdict | capture evidence |
|---|---|---|---|
| verbatim-grade (≥6-word exact run in capture) | 47 lines: 46–49, 51, 67, 71–72, 74–85, 100, 102–107, 123–128, 146–153, 200–204, 206–210 | S | e.g. 46: "form panegyric is the type of court poetry"; 75: "wander through the streets or attend festivals on their own"; 128: "poems about earlier chiefs were handed down and probably known"; 210: "the fili depended on the wealth of his patron for" |
| near-paraphrase, confirmed by targeted read | 48 ("divining implements or even a train or bicycle are also praised"), 50 ("In return the ruler acknowledges their praise by gifts or money which are often given publicly" — the anchor quote), 52/53 ("a performance of something… pre-existed the moment of utterance"; "praises of Dingaan… particular occasion"), 73 ("a District Head's maroka… team normally contained several drummers… two or more pipers, and sometimes a horn-blower"), 83 ("stay in one patron's house for many days… counsellors and ambassadors too"), 101 ("molo (three-stringed guitar) goes 'Molo, the drum of intrigue…'… association between the molo and immorality"), 156 ("introduced in that particular performance from his knowledge of the stock language and imagery"), 170 (audience shouts + gifts passages), 205 ("praise yields to criticism… descendants of nineteenth-century imperialists… turns next to exhortation"), 209/212 ("chosen to live his own life, and not to be the property of another"; "praise is overtaken of distaste… from covetous men… darken the good man's noble deeds") | S | all in S1007/S1008/S1009/S1012/S1014 captures as quoted |
| manual (0-gram) | 82 ("It will not be my part To speak of thee reproachfully, A more choice act of mine will be To celebrate thy praise in song"), 154 ("In the traditional role of the Xhosa oral poet (imbongi), Manisi turns next to exhortation… in conclusion he praises"), 211 ("encode discreet criticisms of royal and dynastic power… flaunt the existence, while guarding the content, of secrets"), 188–194 (the seven §7 row-attribution lines; each named row's claims verified in the bullets above; tier labels in the README's "A 6, B 5" also check out) | S | S1013, S1008, S1009 captures |

Tally (70 cited lines): **68 supported, 2 weak, 0 unsupported**.

- **W — line 155 (S1008):** "it is the *imbongi*'s duty to greet **a lord** with a royal praise name". The capture says "it is his duty to greet **Lord** with a royal praise name" — Lord is Albert Lord, the folklorist being praised at the rally, not a rank. The general duty reading is Opland's own ("as an imbongi…", "a traditional Xhosa audience should by repeating the praise name after him" — both verbatim), and the registry teaches cell generalizes the same way ("greet the chief"), but the entry's lowercase "a lord" silently converts the proper name. One-word-class fix; nothing else in §3/§6 depends on it.
- **W — line 189 → §7 Greek row cells:** "victory, myth and moral counsel, praise of house and city". Capture supports victory ("triumphal odes for victories"), myth ("some different legendary matter") and the moral dimension ("interest, poetical, historical, and moral"); "moral counsel" and "praise of house and city" are compressions not stated in those words (Pindar "does all honour to Athens, 'bulwark of Hellas'"; victor's family/kin enumeration). Design-variable cell carrying no per-cell id by the §7 preamble's own rule, and row-attributed via line 189 — defensible, but the two nouns outrun the capture slightly.

## 4. Other checks

- **Phrase hits natural (6/6, each owning its topical h2):** "praise poetry" §2 (l.44), "praise singer" §3 (69), "praise epithet" §4 (98), "genealogical recitation" §5 (121), "praise performance" §6 (144), "panegyric" §8 (198). Whole-entry counts 3–7 per phrase (grep -o, rc 0); no prose stuffing; §1/§7 table mentions are content cells.
- **C8 sweep confirmed empty by me too:** no other knowledge file's topic line or heading carries a frozen phrase; orality-formulaic-language.md §3 heading is "Epithets and praise-names: the formula lexicon" — no frozen-phrase owner, and the entry defers to it twice (couples line 19; §1 boundary table row citing `:56-62` and the `:60` bullet as prior art; §4 routing paragraph). No restatement of orality §3's formula-lexicon content (the entry's oríkì material is Finnegan S1007 detail not present in orality §3).
- **NON-CANON / PROVINCE:** 2 × NON-CANON (label rule §1 l.40; worked example §9); canon + PROVINCE.md deferral at l.40; §12 handoff paragraph. Inference ledger (§13) lists 9 readings and the preamble's "carries *inference* or *design, not sourced* where it appears in the body" holds — 11 body `(inference)` tags + 18 `(design, not sourced)` tags cover all nine (grep -c, rc 0). Round-98's ledger-mismatch defect class is absent.
- **README edit (git diff 527df3fe… -- corpus/README.md, rc 0):** +37/−1: revision 2.25 block prepended; row added in filename order between `politeness-taboo-euphemism.md` and `proverbs-riddles-attestation-solutions.md` with the `- topic:` text verbatim; `## linguistics/` 43 → **44**; totals 270 → **271**; footer updated "(total 271 files; directory totals 44/36/43/29/24/95)", checked 2026-11-06; Round 99 section states tier A 6 / B 5 (matches the rows) and "no row is superseded this round" (verified below).
- **Registry diff (git diff 527df3fe… -- corpus/SOURCES.md, rc 0):** exactly 11 insertions, 0 deletions — pure append; C3 illegal=0. No new row's `teaches` opens "supersedes" (python scan, rc 0), and no base row was touched, so **no row was added and superseded in the same round**.
- **Manifest/captures:** 20 capture files sha-verify (counter C7); manifest quotes count 1 in their named quote_capture for all 11 rows (counter C7 + my fresh recount).

## 5. Findings by severity

1. **Low — line 155 (S1008): "a lord" vs the source's Albert Lord.** Proper noun silently genericized. One-clause fix ("greet the praised — in this case the visiting scholar Lord — with a royal praise name") or keep and accept the registry-consistent reading; no leg is affected.
2. **Low — §7 Greek row cells outrun the Myers introduction slightly** ("moral counsel", "praise of house and city"). Tighten to the capture's own terms or leave; the §7 preamble already says the table is design-variable, filled from cited cases, with row-level attribution lines.
3. **Observation — S1014 fresh drift:** archive.org dynamic node wrapper; quote intact on fresh bytes; lane stores both raw and converted captures, so C7 stays byte-verifiable.
4. **Observation — counter scope:** C1–C9 measure presence, counts, pins and fresh re-opens; sentence support is this seat's reading, reported in §3. The two W items pass every frozen leg — the gap is the counter's design, not an edit target for this seat.

## 6. Verdict

- **Frozen counter, claim C: legs C1–C9 PASS (9/9)** at my measurement; C9 satisfied 11/11 (http 200, quote_count 1 on fresh bytes, observed values only; 10/11 byte-identical to lane captures, 1 dynamic-page drift with quote intact). First failing leg: **none**.
- **Reviewer verdict on claim C as sourced coverage: PASS.** All 70 cited sentences are supported (68 S, 2 W, 0 U); the two W items are wording-grade, flagged for the L1's optional repair pass, and no frozen leg or acceptance criterion fails on them. The whole counter reports PASS 16/16 over the landed tree.
- Lowest-axis note: no claim this round moves freshness; the obligation is neither met nor waived (claims.json `lowest_axis_note`) — recorded here, outside this seat's judgment.
- This seat edited nothing outside its stage.

## 7. Verification gaps

- Claim O is not judged here (ReviewerO99's assignment); my counter run shows O0–O6 PASS over the same tree at the same moment, which is evidence, not judgment.
- Support judgments (§3) are this seat's reading of the captured passages; the table cites the capture text for each group.
- The counter does not fetch the network; C9's evidence is this seat's reopen.json, validated by the counter against the landed registry (url ∈ source cell, sha format, counts).
