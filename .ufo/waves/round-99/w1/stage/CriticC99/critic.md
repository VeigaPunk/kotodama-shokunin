# CriticC99 — claim C falsification attempt (round 99, w1)

- Seat: CriticC99 (leaf critic, read-only on the lane; wrote only this stage dir and `/fast/scratch/hyaku/kotodama-r99/CriticC99/`).
- Lane base `527df3fee305b3454446946e6779ece45456307e`; claims frozen at `b1b80562edfc8f6082aec74bbbf0f25e152708a8`.
- Dependencies waited for and found: `stage/ScribeEntry99/DONE` (sha256 `1011940ebe51…`, 44922 B) and `stage/ExecRegistry99/DONE`. Bound loop `for i in $(seq 1 240); do …; sleep 15; done` — returned `DEPS-READY iter=58` (rc 0).
- Nothing in the lane was edited. `claims.json`, `predispatch.py`, `battery99.*`, control receipts and `reports/round-99/controls/` were read only.

## Verdict

**Claim C survives its frozen predicate: no leg C1–C9 is falsified.** The frozen counter's C legs are 9/9 PASS on the landed tree (measured twice: a byte-for-byte replica of the frozen C-leg code, rc 0, and the frozen counter itself, whose O6 mutation leg was still running when this report was written — see §0).

**Content quality is a different question, and it is not clean.** I found two defects the predicate cannot see and one boundary gap:

1. `corpus/knowledge/linguistics/praise-poetry-panegyric.md:179` — the §7 Yoruba *limit* cell states a recorded-practice claim that **no capture contains**: "titles are public property, so any drummer who knows them can assemble the praise". `public property` = 0 hits in S1007 (Finnegan) and 0 in S1009 (Barber); `any drummer` = 0; `knows them` = 0. The table's own caption (`:174`) says the cells are "filled from the recorded cases this entry cites", so this is an unsourced claim presented as a report, violating the entry's own grading convention (`:42`: "A clause about a recorded practice carries the registry id of the row that states it; where the entry reads past what the row says, the clause is tagged *inference*").
2. `:154` — "At a contemporary Xhosa **rally** the *imbongi* greets the assembled crowd, praises, turns to exhortation, and closes on a further praise (S1008)". S1008's performance is **not a rally**: it is Manisi declaiming in a university lecture hall at a conference (S1008: "Manisi then stood up in the university lecture hall"; "He then greets the audience of academics before him (lines 6-9)"; "Manisi turns next to exhortation (lines 36-41)"; "Then in conclusion he praises some pioneering missionaries"). `rally` in S1008 has **1** bare hit and it is the substring inside "o**rally**" (`t[2579:2584]`); the word-bounded count `\brall(y|ies)\b` is **0** — no rally. The *sequence* is supported; the *setting word* is not. (Rallies are S1011's material: "mass rally that was held in Umtata on April 22, 1990".)
3. Boundary gap — two base owners of the same case material are **never cited**: `civilizations/yoruba.md:78-92` (§"Oríkì: praise, memory, and an economy of recognition", with a 4-row relation table on patronage, gifts and reciprocal expectation) and `civilizations/germanic-norse.md:72-90` (§"Eddic/skaldic verse economy"). The entry nonetheless carries a Yoruba row (`:179`) and a Norse skaldic row (`:184`) restating both cases. By contrast the Mande case *is* deferred (`:86` cites `mali-songhai.md:53`) and the Parthian design checklist *is* deferred (`:89` cites `parthia.md:183`). The asymmetry is the defect, not the rows themselves.

Smallest safe corrections are in §5. None of them touches a frozen file, a leg, or another seat's output.

## 0. Commands and rc

| # | command (cwd = lane root unless stated) | result | rc |
|---|---|---|---|
| 1 | `git grep -n -i -E 'praise poe\|panegyr\|praise.singer\|izibongo\|oriki\|oríkì\|griot\|imbongi' 527df3fe… -- corpus/knowledge` | 30 lines, 12 files | 0 |
| 2 | per-phrase `grep -r -i -o` over the extracted base tree | praise poetry 5 occ/4 files; praise singer 0/0; panegyric 4/2; genealogical recitation 1/1; praise epithet 1/1; praise performance 2/2 | 0 |
| 3 | frozen-counter `sweep_owners(tree_knowledge(base), PHRASES)` (module imported, base tree extracted with `git archive`) | files 270, owners **0** | 0 |
| 4 | same sweep on the landed tree | files 271, owners **0** | 0 |
| 5 | `git show 527df3fe:corpus/SOURCES.md \| grep -c '^ {0,3}\| S…'` | 930 rows, highest S1006 | 0 |
| 6 | `grep -c '^ {0,3}\| S…' corpus/SOURCES.md` | 941 rows, highest S1017 | 0 |
| 7 | `python3 overlap.py <entry> <19 owners>` (8-word, case-folded, word-level) | see §2 | 0 |
| 8 | `python3 audit.py .` (manifest recount + anchor + id match) | 11/11 count 1, 11/11 in anchor, 20 captures sha-verified, ids equal | 0 |
| 9 | `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` | last line `file ok …/corpus/SOURCES.md`; only W04 (S928, pre-existing) | 0 |
| 10 | `python3 -B tools/check-cited-lines.py <entry>` | `CITED-LINES: 0 finding(s) in 1 file(s)` | 0 |
| 11 | `python3 -B tools/check-corpus-index.py --root .` | `CORPUS-INDEX: OK files=271 rows=271 findings=0` | 0 |
| 12 | `python3 clegs.py . 527df3fe…` (C1–C9 copied verbatim from `predispatch.py`) | `C-REPLICA: PASS legs=9/9` | 0 |
| 13 | `python3 -B reports/round-99/predispatch.py --root . --work <scratch> --base-rev 527df3fe…` | O0–O5 PASS; O6 still running at write time (mutation99) | — |
| 14 | `git diff --stat corpus/SOURCES.md corpus/README.md` | SOURCES +11/−0; README +37/−1 (the −1 is `## linguistics/ (43)` → `(44)`) | 0 |

## 1. Is the surface unowned at base by content?

**No, not by content — only by the six frozen phrases.** The claim's "before" sentence is literally true for the frozen phrases and misleading about the institution.

The counter's C8 is a *narrow* predicate: `sweep_owners` (`predispatch.py:56`, used at `:581-587`) scans only `- topic:` lines and `^#{1,6} ` headings for the six phrases, case-folded with punctuation stripped. It returns 0 at base (270 files) and 0 at land (271 files) — I re-ran it both times with the counter's own functions (commands 3 and 4). That is a real, reproducible result, and it is what C8 means.

But the base corpus already teaches praise poetry as an institution in **five h2 sections and one numbered item**, none of which carries a frozen phrase in its heading:

| base file:line | heading / line | what it already owns |
|---|---|---|
| `linguistics/orality-formulaic-language.md:56` | `## 3. Epithets and praise-names: the formula lexicon` | the formula lexicon |
| `linguistics/orality-formulaic-language.md:60` | "Praise poetry as social formula: Yoruba oríkì (Barber 1991) and Nguni izibongo (Opland 1983). A person's praise-name is compressed genealogy + history + political claim — **the epithet system promoted to a social institution**; praise verses are edited and contested as circumstances change." | **the institution thesis itself**, in one bullet |
| `civilizations/yoruba.md:78` | `## Oríkì: praise, memory, and an economy of recognition` (+ relation table `:86-90`, flattery limit `:83`, economy caveat `:84`) | the Yoruba praise economy, patronage, gifts, reciprocal expectation, "praise is not necessarily bland flattery" |
| `civilizations/mali-songhai.md:50` | `## Jeli oral archives: registers, rights, and interested memory` (+ 6-row register table `:59-64`) | the jeli office: genealogy, praise, mediation, patronage, admonitory court performance |
| `civilizations/parthia.md:165` | `## Gōsān: calibrate the evidence before designing a bardic institution` (+ design move `:183`) | bardic-institution design: "specify repertoire ownership, payment, permissible mockery, commemorative duty, and audience competence" |
| `civilizations/zimbabwe-shona.md:87` | `## Mutupo: clan emblems, taboo animals, and praise address` | praise address as clan designation |
| `myth-symbol/sacred-kingship-mythic-charter.md:150` | `5. **Praise-recitation as performed pedigree.** … with the reciter as an office` | praise-recitation as royal legitimation, the reciter as an office |

So the claim's phrase "praise poetry is mentioned only in prose of 12 files" understates the base: it is mentioned in prose of 12 files **and** taught as an h2 section in five of them, with three tables and two design moves. The claim names only `orality-formulaic-language.md` §3 as a boundary. That is the claim's weakest sentence, not its legs.

**Expansion or duplicate authority?** On the written evidence, **expansion** — with two exceptions (§5 items 2–3).

- The entry cites `orality-formulaic-language.md:60` as prior art **in the boundary table** (`:29`) and adds only office/patronage/reward/order/audience/rivalry. It does not re-derive the slot behaviour.
- It defers the Mande case (`:86` → `mali-songhai.md:53`), the Parthian design checklist (`:89` → `parthia.md:183`), the royal register (`:129` → `sacred-kingship-mythic-charter.md:150`), the Polynesian precision rules (`:133` → `polynesia-navigation.md:146`), the genealogy critique (`:133` → `kinship-terminology.md:153`), the rival-versions point (`:135` → `inca.md:151`), the bard/druid/diviner split (`:214` → `celts.md:50`) and the Tamil "praise is interested speech" (`:54` → `india-tamil-sangam.md:57`). I checked all sixteen line references in the entry's boundary table and body; **every one lands on the stated content** (command below).
- It does **not** cite `yoruba.md` or `germanic-norse.md`, and its §7 table restates both cases.

Line-reference check (all 16, one command, rc 0):

`for ref in …; do sed -n "${l}p" corpus/knowledge/$f; done` — `orality:56` → §3 heading; `funerary:56` → §3 keeners; `duelling:110` → §6 boast formula; `toast:122` → §5 toastmaster; `deity-name:69` → §4 epithet systems; `sacred-kingship:150` → item 5 performed pedigree; `heraldry:35` → §3 bearer unit; `naming:44` → §2 anthroponymy; `polynesia:142` → oral genealogy; `kinship:153` → collected genealogies critique; `parthia:183` → design move; `inca:151` → rival histories; `celts:50` → Diodorus 5.31; `tamil-sangam:57` → "Praise is interested speech"; `oath:20` → §1 scope; `mali:53` → jeli work includes genealogy. All correct.

## 2. Overlap: shared 8-word sequences

Method: word-level, case-folded (`[a-z0-9']+`), 8-word shingles, entry vs each of the 19 adjacent owners named in `ConnectorOverlap99/overlap.md` §2–§3. Entry: 7,380 words, 7,373 shingles, 7,345 unique.

| owner | shared 8-grams | what the shared spans are |
|---|---|---|
| `linguistics/verbal-duelling-ritual-insult.md` | **9** | boilerplate only — `source corpus sources md the registry rows below`, `… one id per line` |
| `linguistics/toast-drinking-speech-formulae.md` | **7** | path references only — `linguistics verbal duelling ritual insult md the boast taunt and` |
| `civilizations/polynesia-navigation.md` | **3** | one substantive sentence: `a shorter performance is not automatically a corrupted longer one` |
| `myth-symbol/heraldry-emblems-identity-marks.md` | **2** | table header — `neighbour anchor what it owns this entry s boundary` |
| `linguistics/orality-formulaic-language.md` | **1** | `the epithet system promoted to a social institution` |
| `linguistics/funerary-lament-dirge-formulae.md` | **1** | boilerplate — `registry rows below one id per line sources` |
| the other 13 owners (`naming-systems`, `linguistic-anthropology`, `sacred-kingship-mythic-charter`, `hero-journey-variants`, `sacred-registers-liturgical-language`, `dance-performance-movement-codes`, `yoruba`, `mali-songhai`, `parthia`, `germanic-norse`, `zimbabwe-shona`, `hawaii`, `maori`) | **0** each | — |

Top three spans, in full:

1. `source corpus sources md the registry rows below` (9 shingles, verbal-duelling) — the house metadata line every entry carries (`- source: corpus/SOURCES.md (the registry rows below, one id per line)`). Not prose.
2. `linguistics verbal duelling ritual insult md the boast taunt and` (7 shingles, toast) — a cross-reference path in the entry's `- couples:` line. Not prose.
3. `a shorter performance is not automatically a corrupted longer one` (3 shingles, polynesia) — **substantive, and attributed at the point of use**: entry `:133` reads "…a shorter performance is not automatically a corrupted longer one (`civilizations/polynesia-navigation.md:146`)", and `polynesia-navigation.md:146` reads "A recitation may select an appropriate line without claiming to enumerate every descendant; a shorter performance is not automatically a corrupted longer one." This is a cited quotation with a line locator, not a silent copy.

The one orality shingle (`the epithet system promoted to a social institution`) appears at entry `:29` inside the boundary table's description of what orality owns — again attributed, with `:60` named.

**Conclusion for §2:** no silent duplication at the 8-word level. The two substantive overlaps are both attributed quotations. This does **not** clear the case-level restatement of Yoruba and Norse (§5 items 2–3), which is paraphrase-level and invisible to shingle counting.

## 3. Row and quote recount

- Registry: 941 rows, highest `S1017`; 11 new rows `S1007`–`S1017`, all tier A/B, all `mined`, all `opened 2026-11-06`, all `used-by` exactly `corpus/knowledge/linguistics/praise-poetry-panegyric.md` (command 6 + `audit.py`).
- Manifest: 11 entries, ids exactly equal to the entry-cited ids (`entry-not-manifest=[]`, `manifest-not-entry=[]`).
- Every quote: `count == 1` in its named `quote_capture`, `1..25` words, and `ws(quote) in ws(anchor cell)` — **11/11**, 20 capture files sha-verified against the manifest (`audit.py`, rc 0).
- `rows.md` ids == entry-cited ids == manifest ids (`S1007`…`S1017`).
- Census `validate` rc 0 (read-only). Index rc 0, `files=271 rows=271 findings=0`.
- Registry diff is append-only: `+11 / −0` lines in `corpus/SOURCES.md`.

Minor documentation inconsistency (not a claim-C failure): `stage/ExecRegistry99/rows.md`'s `bytes` column pairs each row's **raw source** byte count with the **extracted `.txt`** sha256 (e.g. S1008: sha `112fdd45…` = `S1008.txt`, bytes `122076` = `S1008.pdf`). The manifest itself is correct (`S1008.pdf` = `82e20d08…`, 122076 B; `S1008.txt` = `112fdd45…`, 49051 B), and `ReviewerC99/reopen.json`'s fresh shas match the **raw** files, so nothing false reaches the counter. It could mislead a re-checker who compares the rows.md pair against one file.

## 4. Citation audit

I checked **32** cited sentences against their captures (longest-common-word-run search over all 61 cited bullets, then a manual read of the capture window for every bullet whose longest shared run was short). All 32 are tabulated; **30 are supported verbatim or near-verbatim**, and the two defects in the Verdict are the exceptions. Spans are exact substrings of the named capture (whitespace collapsed).

| entry line | id | supporting capture span |
|---|---|---|
| `:46` panegyric is court poetry | S1007 | "In its specialized form panegyric is the typ…" |
| `:47` praise names nearly universal | S1007 | "praises … also occur among non-centralized peoples … the use of 'praise names' is nearly universal" |
| `:48` divining set, bicycle, train | S1007 | "inanimate things like divining implements or even a train or bicycle are also praised" |
| `:49` status validated three ways | S1007 | "It can validate status by the content of the praise, by the number and quality of the performers, and by the public nature of the recitation." |
| `:50` gifts given publicly | S1007 | "In return the ruler acknowledges their praise by gifts or money which are often given publicly." |
| `:51` withholding / derogatory allusions | S1007 | "up to a point praisers can withhold praise or include implicit or explicit derogatory allusions as a kind of negative sanction on the ruler's acts" |
| `:52` praise pre-exists the performance | S1009 | "detached from the immediate context and re embodied in a future performance" |
| `:53` re-embodied in a later performance | S1009 | same passage; the entry's next sentence restates it |
| `:71` every Zulu king had specialists | S1007 | "every Zulu king had one or more specialists who both recited the praises of previous rulers and composed new ones" |
| `:73` Hausa *maroka* team | S1007 | "The king's musicians and maroka form an organized group containing one or more titular series and effective authority hierarchies." |
| `:74` wooden gongs may not praise below a level | S1007 | "wooden gongs, for instance, may not be used to praise anyone below a certain level" |
| `:75` freelance Mandingo singers | S1007 | "expert Mandingo singers … to wander through the streets or attend festivals on their own initiative" |
| `:76` gifts from enthusiasm as well as fear | S1007 | "gifts are showered on the praise poets from enthusiasm as w…" |
| `:77` Xhosa *imbongi* decries/praises | S1011 | "directed at the Chief, decrying what was unworthy, praising what was worthy" |
| `:78` still an important part | S1011 | "still forms an important part of contemporary Xhosa oral traditions" |
| `:79` improvisation vs memorial | S1008 | "the tendency in Xhosa poetry toward improvisation, as distinct from Zulu poetry, which is apparently primarily memorial" |
| `:80` five of the longest odes | S1012 | "Pindar wrote five of the longest of his extant odes" |
| `:81` not the property of another | S1012 | "he had chosen to live his own life, and not to be the property of another" |
| `:82` not my part to speak reproachfully | S1013 | "It will not be my part To speak of thee reproachfully, A more choice act of mine will be To celebrate thy praise in song" |
| `:83` bards as counsellors and ambassadors | S1014 | "These people used to go from place to place, stay in one patron's house for many days … They were good friends, counsellors and ambassadors too." |
| `:84` praise-singing most audible | S1015 | "the praise-singing function is by far the most obvious and audible manifestation" |
| `:85` money in poetry; skalds compete | S1016 | "There certainly was money in poetry for the skald; court poets would receive generous rewards and renown…" + "skalds would compete for the favour of their patron by crafting the most elaborate of praise poems" |
| `:105` renew formulae, coin metaphors | S1010 | "the ability of praise poets to constantly renew well-known formulaic expressions by linguistic adaptation and … the coinage of new metaphors" |
| `:148` audience shouts encouragement | S1007 | "The audience too play their part and often shout out encouragingly in support of what the praiser is saying or to cheer him on" |
| `:201` Ngoni ludicrous praise | S1007 | "sometimes sarcastic or even insulting remarks are included which, among the Ngoni at least, are said to represent a high kind of praise—such comments are so ludicrous that they could not possibly be true" |
| `:202` praise exerts control on a ruler | S1007 | "praise poetry could also have the implicit result of exerting control on a ruler as well as the obvious one of upholding his position" |
| `:205` praise yields to criticism | S1008 | "praise yields to criticism, for they are descendants of nineteenth-century imperialists" |
| `:206` recovered as anything but a curiosity | S1010 | "questions persist as to whether the ancient panegyric should, or can, be recovered as anything but a curiosity" |
| `:207` bedroom to political meeting; toddlers | S1010 | "Praise poems in Southern Africa can be found anywhere from the private bedroom to the public political meeting … on subjects from toddlers to recently deceased elders" |
| `:208` Tswana composer's property | S1007 | "these original praise poems are the property of the composer in the sense that until his death no one may recite them in public (Schapera 1965: 6, on Tswana)" |
| `:211` ruling group withholds meaning | S1009 | "it could be used by the ruling group to flaunt the…" |
| `:212` distaste from covetous men | S1012 | "is fain to babble against and darken the good man's noble deeds" |

Two sentences are **not** supported as written:

- `:154` — the sequence is supported, the word "rally" is not (see Verdict item 2).
- `:179` (Yoruba limit cell) — no capture contains the claim (see Verdict item 1).

Design and inference material is correctly tagged: §9–§11 and §13 carry `design, not sourced` / `inference`, and the inference ledger (`:320-332`) lists nine readings. I found no hedge reported as fact outside the two above.

## 5. Smallest safe corrections (for the L1 / ScribeEntry99, not applied by me)

1. **`:154` — drop one word.** Replace "At a contemporary Xhosa rally" with "At a contemporary Xhosa conference performance" (or "public academic occasion"). The rest of the sentence and `(S1008)` stand. If the rally setting is wanted, it is S1011's Umtata 1990 material, but then the *sequence* claim needs re-sourcing.
2. **`:179` — replace the Yoruba limit cell with a sourced limit and add the missing cross-ref.** Suggested cell: "praise may recall danger or contested reputation rather than flattery (`civilizations/yoruba.md:83`); titles are recited by drummers who know them". The first clause is verbatim-supported by `yoruba.md:83`; the second is supported by S1007 ("given to them by friends or, most often, by the drummers"). This removes the unsourced "public property … any drummer … assemble" claim and closes the Yoruba boundary gap in one edit.
3. **`:184` / §1 table — add the Norse cross-ref.** The skaldic economy is `germanic-norse.md:72-90`; add it to the §1 boundary table as `civilizations/germanic-norse.md:72-90` (§Eddic/skaldic verse economy) with the boundary "meter and the economy of praise stay there; this entry cites the patron relation as one institution case". No content change needed.
4. **Optional, claim text only (no leg):** the "before" sentence "praise poetry is mentioned only in prose of 12 files" should say "…in prose of 12 files, five of which carry an h2 section on a praise institution". C8 is unchanged either way; the sentence is what a later reader will over-trust.

If the L1 wants a single repair that buys the most: **item 2** — it is the only unsourced factual claim in the entry and it also fixes the largest boundary gap.

## 6. Tooling

None installed or upgraded. Used only `git`, `grep`, `sed`, `awk`, `sha256sum`, `pdftotext` (poppler, already present), `python3`, and the lane's own read-only tools.

## 7. Scratch

`/fast/scratch/hyaku/kotodama-r99/CriticC99/` removed before yield (`rm -rf`, rc 0).
