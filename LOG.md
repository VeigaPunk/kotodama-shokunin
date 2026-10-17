# kotodama-shokunin — iteration log (append-only)

## 2026-10-17 — mint (round 0)

Minted under explicit operator directive (2026-10-17): "mint a new
shokunin, a linguistic shokunin; he will connect languages, cultures, and
be related to the lore and world bible, relating cultures, their myths,
symbolisms and eras to their linguistics and costumes", followed by an
operator dispatch of four 16-agent corpus-seeding swarms. Evidence:
`MINT.md`; roster scan `.ufo/scopes/kotodama-mint-20261017/mint-roster-scan.json`
(main repo); fleet `MANIFEST.json` `rounds[]` mint entry 2026-10-17.

Seed kit written: SKILL.md, PROVINCE.md, SHONEN.md (canonical),
AGENTS.md, SCORECARD.md, MINT.md; corpus skeleton
`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis}/`.

Next iterations (claimed, falsifiable):
- Corpus seeding: 64 knowledge entries from four swarms (3×16 zai-flash,
  1×16 sol-max); counting command `find corpus/knowledge -name '*.md' | wc -l`.
- corpus/README.md index written and committed after swarm landing.

## 2026-10-17 — mint corpus seeding, waves 1–3 (operator-dispatched swarms)

Operator dispatch 2026-10-17: three 16-agent swarms on zai-5.3-flash
seeded the three reference partitions. Measured at entry time:
`find corpus/knowledge -name '*.md' | wc -l` = 48 — linguistics/ 16,
myth-symbol/ 16, culture-material/ 16. Every entry carries cited sources
with `(to-verify)` flags where uncertain and a calibration section where
frameworks are contested (per lane AGENTS.md). Swarm agents were assigned
single files and did not append LOG entries; this entry records the batch.

Remaining per the same operator dispatch: a 128-agent gpt-6.1-sol-max
wave to finish the mint — the synthesis niche (coupling craft), the
verification/provenance partition, and civilizational bases covering all
earlier-civilization traditions. GitHub remote created and first push
same day.

## 2026-10-17 — mint corpus finishing wave (128 sol-max) + remote

Operator dispatch 2026-10-17: one 128-agent swarm on gpt-6.1-sol landed
the remaining partitions. Measured: `find corpus/knowledge -name '*.md'
| wc -l` = 176 total — synthesis/ 24, verification/ 12, civilizations/ 92
(plus the 48 from waves 1–3). Counting command re-runnable; measured in
worktree at commit time. `grep -rc 'to-verify' corpus/knowledge
--include='*.md' | awk -F: '{s+=$2} END {print s}'` = 1258 provenance
flags. corpus/README.md (index) and corpus/QUALITY.md (admission bar)
written; SKILL.md corpus map updated; SCORECARD re-measured.

Remote: github.com/VeigaPunk/kotodama-shokunin (public, matching the
2026-10 `shokunin-<domain>`/sibling convention). First push carried the
seed kit + 48 wave-1–3 entries; this commit carries the finishing wave.
Fleet README index row added (main-repo commit `bc889c5`).

Probation standing: >=3 verified rounds still required before a roster
row; probation recorded in fleet MANIFEST.json rounds[] (type "mint",
2026-10-17).

## 2026-10-17 — round-1 TRIAGE batch L3 (language-contact, linguistic-anthropology)

Round-1 triage worker (TRIAGE batch L3) processed the two assigned files
`corpus/knowledge/linguistics/language-contact.md` and
`corpus/knowledge/linguistics/linguistic-anthropology.md` (resolved by
`ls corpus/knowledge/linguistics/*.md | sort | sed -n '5,6p'`), web-verifying
every `to-verify` flag against real scholarship before touching it. No
source was invented.

Measured: before = 2 + 8 flags (`git show HEAD:<file> | grep -o to-verify |
wc -l`); after = 0 + 0 (`grep -o to-verify <file> | wc -l`). Decisions:
9 CONFIRM, 1 DOWNGRADE (Balaibalan authorship stays contested), 0 EXCISE.
New verified sources added to both `- sources:` blocks: Lindstedt 2000
(Rodopi, SSGL 28); Matisoff 1991 (Annual Review of Anthropology 20),
Enfield 2005 (same journal 34), Post 2011 (Mon-Khmer Studies Special
Issue 3) for the Sinosphere; Hale 1982 venue (Oceania Linguistic
Monographs 24), Hale & Nash 1997 (Pacific Linguistics C-136), Fleming
2017 (Language & Communication 56), Bausani 1954 (East and West 4),
Encyclopaedia Iranica "Bālaybalan Language", Chiang 1995 (University
Press of America), Hidalgo 1609 (Barcelona).

Ledger: `corpus/lessons/round-1-triage/L3.md` — one row per flag
(file | flag | decision | basis). Only the two assigned files plus the
new ledger were touched; no commits made.

## 2026-10-17 — round-1 GATE: myth-consistency-gate

Round-1 gate worker implemented the executable kernel for
`corpus/knowledge/verification/myth-consistency-gate.md` (§3 P pantheon
role coverage, §4 M motif coherence, §6 S symbol-domain uniqueness),
calibrated against `myth-symbol/symbolism-synthesis-method.md`,
`comparative-frameworks.md`, `pantheon-archetypes.md`, and
`motif-index-usage.md`. New files, and the only files touched:
`tools/gates/myth-consistency-gate.py` (stdlib only — no PyYAML in this
environment, so the packet parser is a documented YAML subset),
`tools/gates/fixtures/myth-consistency-gate.yml`,
`tools/gates/fixtures/myth-consistency-gate.expected`. No commits made.

Interface: `gate.py <culture-packet.yml>` prints `FINDING <id>: <message>`;
exit 0 clean / 1 findings / 2 could-not-evaluate. Spec IDs are emitted only
for spec conditions (MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02);
kernel-extension HOLD IDs MC-P00/M00/S00 and the exit-2 G-DATA code are
declared in the header docstring. Era alignment (§5 E) stays with the manual
review the spec describes.

Measured: `python3 tools/gates/myth-consistency-gate.py --selftest` →
"selftest: OK — fixture exit 1; planted IDs present: MC-P01, MC-P02, MC-M01,
MC-M02, MC-S01, MC-S02; clean control exit 0 (0 findings)". Both fixture
bytes are idempotent under rerun (`md5sum -c` passes) and selftest is
cwd-independent. Edge runs: base-schema-only packet → HOLD findings, exit 1;
`pantheon: NOT-APPLICABLE` → roster check skipped; malformed `name`/YAML and
unreadable path → exit 2 with G-DATA. The fixture is synthetic and labeled
non-canon; it asserts no world fact.

## 2026-10-17 — round-1 TRIAGE: batch S4

Operator dispatch: TRIAGE batch S4 over
`ls corpus/knowledge/synthesis/*.md | sort | sed -n '13,16p'` →
migration-founder-effects.md, multi-culture-creole-workshop.md,
myth-to-language-derivation.md, naming-canon-workflow.md. Web-verified every
`to-verify` occurrence before touching it; no source was invented.

Measured: before = 9 + 3 + 4 + 4 = 20 occurrences (`grep -o to-verify <file> |
wc -l` at HEAD); after = 8 (convention references only: 2 + 2 + 1 + 3).
Decisions: 10 CONFIRM (8 distinct claims: Icelandic runic distribution;
Trendgården/Foss cross-hammer readings; founding-era costume reconstruction;
Icelandic founder-population composition; Ladino script shift and term scope;
Sephardic surname attestation; Allen's Afroasiatic classification, 3 marks;
LGPN gender asymmetry), 2 DOWNGRADE (creole-workshop §12 thin-knowledge
boundary; migration §10 thin-areas), 0 EXCISE.

New verified sources: Raschellà 2016 (NOWELE 69:2, DOI
10.1075/nowele.69.2.03ras); Plomp et al. 2021 (PLoS ONE, PMC7870008);
Schwarzwald (Jewish Languages Project, judeo-spanish-judezmo-ladino);
Beider (IIJG, "Perspectives of Jewish Onomastics"); National Museum of
Denmark C24451 (Nara to Norwich record) + Viking Archaeology wolf-cross
record; Lester-Makin & Owen-Crocker eds. 2024 (Boydell & Brewer); Allen 2014
§1.1 (Cambridge Core chapter summary); LGPN I statistics.

Ledger: `corpus/lessons/round-1-triage/S4.md` — one row per flag
(file | flag | decision | basis). Only the four assigned files, the new
ledger, and this LOG were touched; no commits made.

## 2026-10-17 — round-1 TRIAGE batch C3 (craft-artisan-lexicon, cuisine-food-lexicon)

Round-1 triage worker (TRIAGE batch C3) processed the two assigned files
`corpus/knowledge/culture-material/craft-artisan-lexicon.md` and
`corpus/knowledge/culture-material/cuisine-food-lexicon.md` (resolved by
`ls corpus/knowledge/culture-material/*.md | sort | sed -n '5,6p'`),
web-verifying every uncertainty flag against real, checkable sources before
touching it. No source was invented and no claim was laundered.

Measured: cuisine `to-verify` occurrences 11 → 1 (`grep -o 'to-verify'`; the
one remainder is the §11 policy sentence "flag every to-verify item before it
approaches the bible", not a claim). Craft had 0 literal `to-verify` marks;
its 3 inline "flag"/"verify" markers (fuller etymology, Dunstan row,
tsukumogami 99-year pair) were processed as equivalents. Decisions across the
13 ledger rows: 13 CONFIRM (3 with corrected content — the FAO "~42%" figure,
the West "English translation" citation, the 99-vs-100 tsukumogami rule),
0 DOWNGRADE, 0 EXCISE.

Sources added to the `- sources:` blocks: FAO 2026 *State of Agricultural
Commodity Markets* (wheat/maize/rice ≈40% of globally available calories,
FAOSTAT Food Balances 2023); Flandrin *Arranging the Meal* (trans. Johnson)
for the à la française→à la russe transition; Herrin *Women in Purple* +
Peter Damian *Institutio monialis* (Byzantine fork anecdote); Adamson *Food
in Medieval Times* (water vs ale/beer); Madrid press record 2 Jan 1894
(*El Imparcial* "Las uvas bienhechoras"; BNE Hemeroteca; via National
Geographic España 2024); OED + American Heritage s.v. *fuller*; Golden
Legend "Life of S. Dunstan" (CCEL text inspected); Foster *The Book of
Yokai* on the *Tsukumogami-ki*. Also corrected the Dongjing meng hua lu
citation (West's translations are selections in Mair et al. 2005, 405–22;
the "72 正店" figure is verbatim from juan 2) and the Liang emperor Wu
edict dating (511 CE in the Buddhist record vs 513 CE in Liang shu/Nan shi).

Ledger: `corpus/lessons/round-1-triage/C3.md` — one row per flag
(file | flag | decision | basis). Only the two assigned files plus the new
ledger were touched; no commits made.

## 2026-10-17 — round-1 GATE: costume-era-consistency-gate

Round-1 gate worker implemented the executable kernel for
`corpus/knowledge/verification/costume-era-consistency-gate.md`, calibrated
against the two corpus tables the spec cites:
`culture-material/dress-through-eras.md` (silhouette/material/wearer-rule
grammar, enforcement mechanisms) and `culture-material/textile-technology.md`
(fiber/dye/loom/finish gates, the dated process anchors). Checks: material
availability vs claimed costume (MAT-01..07, EAR-01), rank-rule conflicts
(R-01..R-07, spec §6 authority × interval × wearer × property × occasion),
the anachronism sweep over dated processes (E-01, EAR-04, G-ERA, spec §7),
and textile-tech bounds (T-01..T-03, spec §5: seamless-panel width, fit
mechanism, the "silk is never spun" invalid-rejection guard).

New files, and the only files touched:
`tools/gates/costume-era-consistency-gate.py` (stdlib only — document parser
is a YAML subset, JSON packets also accepted),
`tools/gates/fixtures/costume-era-consistency-gate.yml` (fictional packet
"Kedrun Delta", 20 costume rows, two clean controls, planted violations for
every expected ID), `tools/gates/fixtures/costume-era-consistency-gate.expected`
(21 IDs, one per line). No commits made.

Interface: `gate.py <culture-packet.yml>` prints `FINDING <id>: <severity>
<message>`; exit 0 clean / 1 findings / 2 could-not-evaluate (also covers a
packet missing `costumes`/`eras`; unforeseen packet shapes route to a G-DATA
line, not a traceback). Severity tokens `[reject]/[hold]/[note]` carry the
spec's verdict vocabulary; mapping to READY/REJECT/HOLD and all canon
decisions stay with the caller and lore-shokunin.

Measured: `python3 tools/gates/costume-era-consistency-gate.py --selftest` →
"self-test: 10/10 checks passed; fixture exit 1 with 21 planted finding IDs"
(parser invariants, expected-ID set equality, worked-example severities,
clean control exit 0, JSON control exit 0, malformed inputs exit 2, mauve-hue
false-positive guard). Fixture run → 25 finding lines, exit 1, including the
spec's worked examples (mauveine before 1856 → E-01 reject; 1.4 m seamless
panel vs 0.6 m loom → T-01 reject; 800 vs 750 m2 → MAT-05 reject). Fixture
and expected bytes are idempotent under rerun (`sha256sum`: 36d92113...,
4b0724f9...) and the selftest is cwd-independent (run from /tmp: exit 0).
The fixture is synthetic and labeled non-canon; it asserts no world fact and
adds no source claims beyond the spec's own keys ([S] mauveine 1856/1857,
[M] spun silk, `textile-technology.md` §2–4 anchors).
## 2026-10-17 — round-1 TRIAGE batch Z05 (byzantium, carthage, celts, chimu)

Round-1 triage worker (TRIAGE batch Z05) processed the four assigned files
`corpus/knowledge/civilizations/{byzantium,carthage,celts,chimu}.md`
(resolved by `ls corpus/knowledge/civilizations/*.md | sort | sed -n '17,20p'`),
web-verifying every `(to-verify)` occurrence against real scholarship before
touching it. No source was invented; no sibling or fleet file touched.

Measured: before = 5 + 8 + 3 + 8 = 24 `(to-verify)` occurrences
(`git show HEAD:<file> | grep -o to-verify | wc -l`); after = 0 + 0 + 0 + 1
(`grep -o to-verify <file> | wc -l`). The single remaining hit is chimu.md's
status-key legend that defines the mark (not a claim). Of 22 claim flags:
14 CONFIRM, 8 DOWNGRADE, 0 EXCISE; two non-claim occurrences handled
(one definition retained, one stale meta-instruction in carthage.md §12
rewritten to match the resolved gates).

Notable: Augustine's `Chanani` line was DOWNGRADED rather than confirmed —
Quinn, McLynn, Kerr & Hadas 2014 (PBSR 82: 175–197) re-examined the
manuscripts and find the archetype read *quid sit*, not *quid sint*, so the
line "cannot be used as positive evidence". The naval-lexicon flag was
resolved from Krahmalkov's own cited scan (`brrm` cargo ships, `ḥbl`
sailor; no warship-class or rank lexeme). Hurst & Stager 1978's publisher DOI
carries a stale 1973 year — entries note the correct 1978, 9(3) citation.

New verified sources added to the `- sources:` blocks: byzantium [S] Parani
2003, [T] Haldon 2006, [U] Buckton 1994; carthage Quinn et al. 2014,
McCarty 2019, Hurst & Stager 1978, Bénichou-Safar 1982 and 2004,
Lancellotti 2010; celts Carr 2005, Grömer 2016; chimu Urban 2017,
Herrera Calderón et al. 2019, Moseley & Deeds 1982.

Ledger: `corpus/lessons/round-1-triage/Z05.md` — one row per flag
(file | flag | decision | basis). Touched only the four assigned files, the
new ledger, and this log entry; no commits made.## 2026-10-17 — round-1 TRIAGE batch Z17 (mongol, muisca, nazca, newar-nepal)

Round-1 triage worker (TRIAGE batch Z17) processed the four assigned files
`corpus/knowledge/civilizations/{mongol,muisca,nazca,newar-nepal}.md`
(resolved by `ls corpus/knowledge/civilizations/*.md | sort | sed -n '65,68p'`),
web-verifying every `(to-verify)` occurrence against inspected sources before
touching it. No source was invented; no sibling or fleet file touched.

Measured: before = 12 + 8 + 3 + 8 = 31 occurrences
(`git show HEAD:<file> | grep -o "(to-verify)" | wc -l`); after = 10 + 6 + 3 + 6
= 25 (`grep -c "(to-verify)" <file>`). Six marks removed; decisions overall:
10 CONFIRM (including 4 non-claim legend/policy lines retained by design),
21 DOWNGRADE, 0 EXCISE. Of the 21 downgrades, 6 were reworded to calibrated
uncertainty and 15 were re-read and kept unchanged as already-stated evidence
gaps.

Notable edits: the UNESCO deel record's own metadata gives 2010-11-20 (mark
removed); Unicode L2/19-016 p. 2 calls the Tata-tonga adoption story a "popular
narrative"; Unicode ch. 14 §14.4 confirms 'Phags-pa's separate Tibetan line
(devised 1235–1280, promulgated 1269); Starostin–Dybo–Mudrak 2003, entry *ŭdu,
gives Middle Mongol female-shaman forms; [I09, §3.3.6] shows "Acrotom" is
Duquesne's designation, not an attested Muysca word; the [M21] raft account
contains no dive, recurrence, quantities or formula; Knudson et al. 2009
sampled 16 of 18 trophy heads with a local-origin conclusion (per-individual
data still open); Hutt 1994 anchors the Mañjuśrī lake myth to the Svayambhū
Purāṇa (earliest known copy 1558); Cleveland 1991.1081 re-inspected — the
record's "1600s" date vs its Gurkha-period description left unresolved.

New sources added to `- sources:` blocks: mongol — Pandey 2019 (Unicode
L2/19-016), Starostin–Dybo–Mudrak 2003, Unicode ch. 14 §14.4; newar-nepal —
Hutt 1994, *The Rising Nepal* 2026 (modern usage record only).

Open lead reported for follow-up, not edited here (unflagged): muisca.md's
acrotom-cycle row states "12 + 12 + 13 months" while [I09, §3.3.9] prints
"12 + 12 + 12 + 1" for the same 37-moon span.

Ledger: `corpus/lessons/round-1-triage/Z17.md` — one row per flag
(file | flag | decision | basis). Touched only the four assigned files, the
new ledger, and this log entry; no commits made.## 2026-10-17 — round-1 TRIAGE batch Z08 (etruria, finnic-sami, fon-dahomey, germanic-norse)

Round-1 triage worker (TRIAGE batch Z08) processed the four assigned files
`corpus/knowledge/civilizations/{etruria,finnic-sami,fon-dahomey,germanic-norse}.md`
(resolved by `ls corpus/knowledge/civilizations/*.md | sort | sed -n '29,32p'`),
web-verifying each `(to-verify)` flag against inspected sources before touching
it. No source was invented; no sibling or fleet file touched; edits kept
surgical (flagged sentences + the corresponding `- sources:` entries only).

Measured: before = 3 + 10 + 9 + 3 = 25 exact `(to-verify)` occurrences plus one
annotated variant (`(to-verify: competing analyses …)` in germanic-norse), 26
flags; after = 1 + 7 + 8 + 1 = 17. Nine marks removed; decisions overall:
10 CONFIRM, 16 DOWNGRADE, 0 EXCISE. The 16 downgrades are scope guardrails,
standing definitions, or gaps no source in reach could close (Fon naming
corpora, palace honorific grammar, exact garment regulations, Sámi drum layout
corpus, marital-status trim meanings, Finnic costume ensembles, Sámi name
order, Gaski page-level lyric readings) — each re-read and left as calibrated
uncertainty; fourteen of them stand byte-identical by design, and two were
narrowed in wording.

Notable verifications: the Etruscan `netśvis` "haruspex" equation is the Pesaro
bilingual — Latin `L. CAFATIUS … HARUSPEX FULGURIATOR` beside Etruscan
`CAFATES … NETŚVIS TRVTNUT FRONTAC`, cited in de Grummond & Simon as TLE 697 =
ET Um 1.7 (new [PES] source entry; the row now states the equation instead of
treating the term as an unchecked research lead). Kelemen 2022: 76's attribution
of an Indo-European-loan view of Dierpmis to Aikio is a misattribution: Aikio
2012: 84 prints `dierpmis 'thunder god'` inside his Palaeo-Laplandic substrate
word list — the file's caution is now a checked finding rather than a flag.
Kelemen 2022: 73 gives the jumala/Ipmil route (Finno-Volgaic *juma, "possibly
adopted from Finnish to Saami with Swedish mediation", UEW 638 / SSA 1:247).
The Getty handbook p. 26 does gloss dokunnon (master and possessor of all
riches), simido (master of the world), ainon (eminent master of the earth);
Capo Chichi 2023, *African Arts* 56(2): 10–19, documents that a récade
authenticated a royal messenger's message and separates Fon `wensagunkpo` from
the thunder-priest's `sokpo`. On the Norse side, Solheim et al. 2025, *Antiquity*
99(404): 422–439 puts the Svingerud/Hole fragments at 50 BC–AD 275; the Vanir
question is documented on both sides (Simek 2010, *RMN Newsletter* 1: 10–19 vs
Frog & Roper 2011, *RMN Newsletter* 2: 29–37); the "seiðr from the Sámi" theory
is a standing controversy (von Schnurbein 2003, *History of Religions* 43(2):
116–138). "Gun-gun" as a Fon talking-drum term could not be verified anywhere in
the Fon/Gbe drum literature — flag retained.

New sources added to `- sources:` blocks: etruria — [PES] Pesaro bilingual
(CIL I² 2127 = CIL XI 6363 / TLE 697 = ET Um 1.7); finnic-sami — Renzi 2025
dissertation (regional joik genre names), Aikio 2012 source line annotated with
the p. 84 re-check; fon-dahomey — Capo Chichi 2023, Smithsonian NMAfA récade
record; germanic-norse — Solheim et al. 2025, Simek 2010, Frog & Roper 2011,
von Schnurbein 2003.

Ledger: `corpus/lessons/round-1-triage/Z08.md` — one row per flag
(file | flag | decision | basis). Touched only the four assigned files, the
new ledger, and this log entry; no commits made.

## 2026-10-17 — round-1 TRIAGE batch C4 (dress-through-eras, era-periodization-models)

Round-1 triage worker (TRIAGE batch C4) processed the two assigned
culture-material files, resolved by `ls corpus/knowledge/culture-material/*.md
| sort | sed -n '7,8p'`: `dress-through-eras.md` (5 flags) and
`era-periodization-models.md` (1 claim flag + 1 §12 meta-sentence). Every flag
was web-verified against inspected scholarship, primary texts, or statutes
before touching it; no source was invented; no sibling or fleet file touched.

Measured before/after (`git show HEAD:<file> | grep -o '(to-verify)' | wc -l`
→ `grep -o '(to-verify)' <file> | wc -l`): dress 5 → 1, era 2 → 0. Decisions:
5 CONFIRM, 1 DOWNGRADE, 0 EXCISE; the one remaining occurrence is the narrowed
(to-verify) on the sideless surcoat's primary sermon locus.

Notable: the "ten obey, ten not obey" (十从十不从) rhyme is verified as folk
tradition (徐珂《清稗类钞》 1916 records it as "国初，人民相传…"; 蔡元培
1903 had "自幼习闻" it), while the 金之俊/Dorgon negotiation story is a 1904
revolutionary-press invention (陈去病《清秘史》 → 天嘏《满清外史》 1912) that
夏晓虹's study judges apocryphal — the sentence now carries that provenance.
衣冠禽兽's badge etymology is a folk etymology with no lexicographic support
(earliest book citation, 明·陈汝元《金莲记》第七出, is already an insult per
漢典/《成語典》). gauze←Gaza and the Arabic/Persian silk derivations are
evidence-free conjectures (Etymonline / Century Dictionary). The Mesopotamian
hem is CAD's *sissiktu*, normalized *sissiqtu* by Gaspa (2017, Textile
Terminologies, 81), documented sealing legal documents — claim narrowed from
"ritual and oath" to "legal transactions", Malul (1986, BiOr 43) added.
South Korea's Dangun calendar (1948–1961) is confirmed against 「연호에 관한
법률」 법률 제4호 (1948) and 법률 제775호 (1961, 서력기원 from 1962). The
sideless-surcoat "gates of hell" flag was the only DOWNGRADE: the sobriquet is
French "porte/fenêtre d'enfer", attributed to churchmen by costume history
(Racinet 1888; Anderlini 2019), with no primary sermon text located.

New sources added to the entries' `- sources:` blocks: dress-through-eras.md —
陈去病《清秘史》, 天嘏《满清外史》, 徐珂《清稗类钞》, 夏晓虹 "历史记忆的重构：
晚清'男降女不降'释义", 明·陈汝元《金莲记》第七出 (六十种曲本), 漢典/教育部
《成語典》, Etymonline (Century Dictionary), CAD S 323a, Malul 1986 (BiOr 43),
Gaspa 2017, Racinet 1888, Anderlini 2019; era-periodization-models.md — Korea
bullet (연호에 관한 법률, 법률 제4호/제775호, 국가법령정보센터). Ledger:
`corpus/lessons/round-1-triage/C4.md` — one row per flag
(file | flag | decision | basis). Touched only the two assigned files, the new
ledger, and this log entry; no commits made.

## 2026-10-17 — round 1: gates + triage (admitted)

Claims (declared before dispatch, lowest axes first):
1. operability — implement >=4 verification specs as executable gates.
   Before `ls tools/gates/*.py | wc -l` = 0 → after = 6, all `--selftest`
   green (run recorded at close; fixtures pinned under tools/gates/fixtures/).
   VERDICT: improved, verified.
2. freshness — triage 300 of 1258 to-verify flags. Before grep-sum 1258 →
   after 795 (463 net; decision rows: 503 CONFIRM / 416 DOWNGRADE / 64
   EXCISE across 42 ledgers, `grep -h 'CONFIRM|DOWNGRADE|EXCISE'
   corpus/lessons/round-1-triage/*.md | wc -l` = 983). Target exceeded.
   VERDICT: improved, verified.
Other axes: calibration improved (983 basis-carrying decision rows vs 0);
depth, coverage, adjacency unchanged. No axis harmed. Round ADMITS.

Dispatch record: one AgentSwarm, 62 agents on
alibaba-token-plan/deepseek-v4.1-flash; 47 completed, 15 filter-killed
(resume-fatal), key-2 retry quota-blocked. Provider incident + carried
debt (batches L6 M2 M8 C6 C8 S2 V1 V2 Z03 Z10 Z13 Z18 Z19 Z21 Z22)
recorded in corpus/lessons/round-1-gates-and-triage.md; retried round 2
on key 3 or held for quota.
