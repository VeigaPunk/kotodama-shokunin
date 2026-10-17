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
## 2026-10-17 — round 2: triage fragment M04 (1 flag, CONFIRM)

Target: `corpus/knowledge/myth-symbol/comparative-frameworks.md`
(sorted position 4 of `corpus/knowledge/myth-symbol/*.md`). One
`(to-verify)` flag found (`grep -n '(to-verify)'`), §3 Eliade
calibration: "The Enūma Eliš–akītu performance link itself is contested
in Assyriology". Web-verified the contestedness at source level and
CONFIRMed: mark removed, clause now names the two grounds (the sole
ritual program is a late Seleucid-era tablet, Thureau-Dangin *Rituels
accadiens* 1921: 127–154; the cosmogonic-renewal reading is challenged
from J. Z. Smith 1976 on), and five sources appended to the file's
`- sources:` block as a "triage round-2 additions" clause: Sommer
(JANES 27, 2000: 81–95 — the article PDF was read directly), J. Z. Smith
(HR 16, 1976 / *Map is Not Territory*, 1978), Thureau-Dangin (1921),
Ballentine (OUP 2015), Debourse (Brill 2022 / *Religion Compass* 18,
2024). §9's cross-reference updated to "sourced as contested in §3".
Post-edit check: `grep -c '(to-verify)'` = 0 on the file; header
(topic/sources/couples) preserved. Ledger:
`corpus/lessons/round-2-triage/M04.md`. Touched only the assigned file,
the new ledger, and this log entry; no commits made.

## 2026-10-17 — round 2: triage C11 (`music-instrument-lexicon.md`)

Assigned file: `corpus/knowledge/culture-material/music-instrument-lexicon.md`
(sorted position 11). Two `to-verify` flags, both in §7 Calibration.

- CONFIRM — "Raga therapy"/"healing frequency" claims under-evidenced. Basis:
  Babel, Baral & Srivastava (2023), *Cureus* (PMC10754644) — raga-EEG
  meta-analysis "was inconclusive" (5 studies, 71 participants); Stanhope &
  Weinstein (2020), *Complementary Therapies in Medicine* 51:102412 (PMID
  32507429) — 4 peer-reviewed singing-bowl studies, low-level designs, "we
  cannot recommend singing bowl therapies at this stage". Mark removed; both
  sources named inline and appended to the `- sources:` block.
- DOWNGRADE — Greek *kithara* ← Iranian "hypothesis". Basis: Beekes (2010),
  *Etymological Dictionary of Greek* I:694–5 — κιθάρα as Pre-Greek, possibly
  related to Proto-Hurro-Urartian *kinnar; the Persian story is popular-source
  (Klein; Online Etymology Dictionary) and fails on chronology (Homeric
  attestation) and phonology. Clause rewritten as a rejected etymology.

Evidence: `grep -c -i 'to-verify' corpus/knowledge/culture-material/music-instrument-lexicon.md`
before = 2, after = 0. Ledger: `corpus/lessons/round-2-triage/C11.md`.
Touched only the assigned file, the ledger, and this entry; no commits made.

## 2026-10-17 — round 2: triage fragment V05 (0 flags resolvable, 2 n/a)

Target: `corpus/knowledge/verification/lexicon-coverage-audit.md`
(sorted position 5 of `corpus/knowledge/verification/*.md`, resolved by
`ls corpus/knowledge/verification/*.md | sort | sed -n '5p'`). Enumeration
(`grep -o '(to-verify)'` = 2; bare `to-verify` = 2): lines 33 and 189 only.
Both tokens are the entry's own status-label vocabulary (§2's
`attested`/`reconstructed`/`contested`/`design-choice`/`(to-verify)` set) and a
§9 scope declaration with an instruction for future users — neither marks an
external claim, so the three resolution outcomes of
`to-verify-triage-protocol.md` §4 do not apply; decision `n/a — not a claim`
for both, marks retained (same class as round-1 batch V3's 30 vocabulary
tokens). Eliminating them would delete a label the entry's verdict contract
depends on.

Because no claim was flagged, the batch's verification effort went to the
entry's checkable scholarship (round-1 V3 precedent): all eight records in the
`- sources:` block re-verified as printed — Haspelmath & Sims 2010 (Hodder
Education, 2nd ed., ISBN link 200); List/Cysouw/Forkel 2016 LREC 2393–2400
(ACL L16-1379); Rzymski et al. 2020 Sci Data 7:13, doi
10.1038/s41597-019-0341-x (200); Haspelmath & Tadmor 2009 + Haspelmath 2009
chapter 35–54, doi 10.1515/9783110218442.35 (202); Gries 2008 IJCL 13(4):
403–437, doi 10.1075/ijcl.13.4.02gri — the §5 DP(w) = 0.5 × Σ|n_i(w)/n(w) −
N_i/N| formula matches Gries's Deviation of Proportions; Campbell 2013, 3rd
ed., EUP. All six §9 access points resolve (John Benjamins 403 = Cloudflare
bot block to this client, DOI resolved to the correct article path; nature.com
also bot-blocked, identity confirmed via DOI + citing works). All 16 `couples:`
paths exist under corpus/knowledge/{linguistics,myth-symbol,culture-material}/.
No correction warranted — **corpus file not edited**; ledger:
`corpus/lessons/round-2-triage/V05.md`. Touched only the new ledger and this
log entry; no commits made.
## 2026-10-17 — round-2 TRIAGE batch M16 (myth-symbol/trickster.md)

Round-2 triage worker (TRIAGE file 1/1, batch M16) processed
`corpus/knowledge/myth-symbol/trickster.md`, resolved by
`ls corpus/knowledge/myth-symbol/*.md | sort | sed -n '16p'`. Three
`(to-verify)` marks found (lines 34, 79, 82; no variant forms): 3 CONFIRM,
0 DOWNGRADE, 0 EXCISE; `grep -c 'to-verify'` 3 → 0. Every flag was
web-verified before editing; no source invented; no sibling or fleet file
touched.

Findings: (1) the Pueblo-clown flag asked for a dedicated survey and one
exists — Parsons & Beals (1934), "The Sacred Clowns of the Pueblo and
Mayo-Yaqui Indians," *American Anthropologist* 36(4):491–514, plus Hieb (1972,
in Ortiz ed., *New Perspectives on the Pueblos*) and Babcock (1984, in
MacAloon ed., *Rite, Drama, Festival, Spectacle*, 102–128). (2) The Loki cult
absence is the standard scholarly position: Lindow (2001), s.v. "Loki" ("no
cult of Loki, and place-names based on Loki are unknown") and von Schnurbein
(2000), *History of Religions* 40(2):109–124. (3) The gender flag confirmed
with scope narrowed: dedicated female-trickster surveys exist but are
literary/folkloristic — Smith (1997), Jurich (1998), Landay (1998), Tatar
(2015, *Cambridge Companion to Fairy Tales*, 39–59) — and Hyde (1998,
appendix) argues "all the standard tricksters are male"; the
mythological/ethnographic survey is the thin part, and the sentence now says
so.

Sources were appended to the file's `- sources:` block as a "triage round-2
additions (2026-10-17; web-verified)" clause. Ledger:
`corpus/lessons/round-2-triage/M16.md` — one row per flag
(file | flag | decision | basis). Diff is 4 changed lines (3 flags + sources);
no commits made.

## 2026-10-17 — round 2: triage Z10f (`arabia-pre-islamic.md`)

Assigned file: `corpus/knowledge/civilizations/arabia-pre-islamic.md`
(sorted position 10). Chunked `sed` reads; **0 live `(to-verify)` flags** —
`grep -i verify` and a Unicode-normalized scan both return nothing. The file's
four pre-round-1 flags were already resolved by round-1 batch Z03 (commit
`291c714`; Zakharia 2015 / Ghabin 2008 / Al-Muaikel 1995 added to `- sources:`
then).

Round-2 re-verification of the three factual resolutions against the cited
sources (all hold; no edit needed):
- ġūl row — Zakharia 2015 (HAL PDF read): "les deux poèmes dans lesquels
  Ṯābit Ibn Ǧābir Ibn Sufyān décrit sa rencontre avec la goule"; ʿAntara's
  Algol verse (Dīwān ed. al-Tibrizī p. 137); Imruʾ al-Qays's ghoul-teeth
  simile; the rarity statement.
- rifādah — Ghabin 2008:67: Quṣayy institutions "feeding the pilgrims
  (rifāda), providing water for them (siqāya) and establishing the council of
  the clans (dār al-nadwa)", fn. 45 = Watt, *Muhammad at Mecca*, p. 13.
- sūq chronology — Al-Muaikel 1995: ʿUkāẓ–Mijnah–Majāz sequence in
  Dhū l-Qaʿda–Dhū l-Ḥijja; "the architectural development of the Suq did not
  take place during the pre-Islamic period".

No file edit (minimal-edit rule; round-1 wording and sources already correct).
Post-check: `grep -c '(to-verify)'` = 0 on the file. Ledger:
`corpus/lessons/round-2-triage/Z10f.md`. Touched only the new ledger and this
entry; no commits made.
## 2026-10-17 — round-2 TRIAGE M15 (symbolism-synthesis-method)

Zero actionable `(to-verify)` flags: the file's only two "to-verify" strings
(§9 step-8 line, §10 package line) name the handoff "open to-verify list"
artifact, not claims — `grep -c '(to-verify)'` = 0 before and after; NFKC
re-scan and the seed commit `76c105b` agree. Swept attributable claims instead:
three verified, two wrong locators corrected (minimal edits; `- sources:`
otherwise intact): Brown (1983) was cited as *American Ethnologist* 10(2):
211–225, true record *Anthropological Linguistics* 25(2): 121–161 (JSTOR
30027665; Glottolog 1061); "Aveni (1997), Skywatchers" → Aveni (2001),
*Skywatchers: A Revised and Updated Version of Skywatchers of Ancient Mexico*,
U Texas Press, ISBN 9780292705029 (UTP catalogue, AbeBooks 8/15/2001; the 1997
Wiley book is *Stairways to the Stars*), body §4.4 citation re-keyed to 2001;
Man'yōshū 894 (Yamanoue no Okura, 言霊の幸はふ国) confirmed against the Nara
Prefecture Manyō Hyakka DB and the Senshū University text of 5:894–896, source
line added. Ledger `corpus/lessons/round-2-triage/M15.md`. Touched only the
assigned file, the ledger, and this log entry; no commits made.

## 2026-10-17 — round-2 TRIAGE C16 (warrior material culture)

`corpus/knowledge/culture-material/warrior-material-culture.md` (sorted
position 16) carried exactly 2 `(to-verify)` flags; both processed, file now at
`grep -c '(to-verify)'` = 0: 1 CONFIRM, 1 DOWNGRADE, 0 EXCISE.

CONFIRM — §7 Nagashino "three-rank volley fire". The hedge is correct and now
carries sources: 『信長公記』 has no rotating-volley passage (the account is
traced to the Edo-period 『甫庵信長記』 and canonized as fact by Meiji-era
textbooks), against 藤本正行「長篠の鉄砲戦術は虚構だ」『歴史と旅』1980年5月号 and
「長篠合戦における織田の銃隊の人数について」『甲冑武具研究』35 (1975); 名和弓雄
『長篠・設楽原合戦の真実』雄山閣 1998 (matchlock-replication: the drill was not
executable); 平山優『長篠合戦と武田勝頼』吉川弘文館 2014 (the 三段＝三か所
re-reading, reviewed by 磯田道史, 毎日新聞 2014-03-16, as overturning the 通説).
What remains disputed is the *degree* of coordination — 小和田哲男's field
summary (relayed at eishin.ac blog, 2023) calls the coordinated-volley image
絵空事 while noting three-man firing teams as the current mainstream alternative
— so the bullet keeps its hedge, loses the mark, and gains inline citations.

DOWNGRADE — §4 Voice row, the term "mondō". Unverifiable as the term for night
challenge-and-response passwords. 精選版 日本国語大辞典 s.v. 合言葉 (aikotoba),
sense ①: "a signal word fixed in advance to distinguish friend from foe in
darkness or when fighting in melee," first citation 『謙信家記』 (1580); 問答
denotes the question-and-answer *exchange form*, not the watchword (Weblio's
aikotoba entry: "言葉の問答による合図"). Cell rewritten to **aikotoba** 合言葉
with the form/term distinction stated in place.

Both sources appended as two bullets in the entry's `- sources:` block
(kotobank.jp/word/合言葉-421239 read 2026-10-17). Header preserved; edits
confined to the two flagged loci plus the sources block. Ledger:
`corpus/lessons/round-2-triage/C16.md`. Touched only the assigned file, the
ledger, and this log entry; no commits made.

## 2026-10-17 — round 2: triage fragment V07 (4 flags, all rule tokens retained)

Target: `corpus/knowledge/verification/naming-collision-gate.md` (sorted
position 7 of `corpus/knowledge/verification/*.md`). Round-1 batches V1/V2
died before triaging positions 1–8, so this file had no prior pass. All four
`(to-verify)` tokens (lines 48, 119, 151, 188) are the gate's own rule
vocabulary — instructions to mark *future* reviewed claims — not marks on
existing factual propositions, so no CONFIRM/DOWNGRADE/EXCISE subject existed
and the corpus file was left byte-identical (header intact). Independently
re-confirmed the entry's whole 8-source block on 2026-10-17: Crossref for
Hough (`10.1093/oxfordhb/9780199656431.001.0001`, editor Hough, OUP 2016),
IPA Handbook (`10.1017/9780511807954`, CUP 1999) and Wagner–Fischer
(`10.1145/321796.321811`, JACM 21(1):168–173); Open Library + live Routledge
page for Haspelmath & Sims 2010 (Hodder, 2nd ed., ISBN 9780340950012); live
fetches of WALS ch. 12 (Maddieson, content matches the entry's use), UAX #15
rev 58 (Unicode 18.0.0, 2026-08-12, Whistler, §§1.1–1.2), UTS #39 rev 34
(18.0.0, 2026-08-27, Hadley & Pournader, §4), and the UNESCO ethics page
(12 principles, 10.COM 15.a; principles 1, 4–5, 7–10 present). Rule rationales
checked against WALS ch. 141 (Comrie; script ≠ genealogy) and a peer-reviewed
chance-resemblance discussion (PMC10432883). No link rot, no wrong metadata.
Result: 0 CONFIRM / 0 DOWNGRADE / 0 EXCISE — 4 retained as rules. Ledger:
`corpus/lessons/round-2-triage/V07.md`. Touched only the ledger and this log
entry; no corpus file edited, no commits made.
## 2026-10-17 — round 2: triage fragment V01 (2 CONFIRM, 1 locator corrected)

Target: `corpus/knowledge/verification/calibration-registry.md` (sorted position 1
of `corpus/knowledge/verification/*.md`, resolved by
`ls corpus/knowledge/verification/*.md | sort | sed -n '1p'`). Enumeration
(`grep -o '(to-verify)'` = 9): lines 36, 39, 105, 176–180, 187. 7 of the 9 are the
entry's own status vocabulary (code T, §1 mark-survival rule), craft rules (§7
costume guard, §13 provenance caution) and standing per-case rules (§12 rows for
clan/crest/animacy, attestations/etymologies/edicts, sky-genealogies/deep families/
cognitive effects) — the three §4 outcomes do not apply, so those are recorded
`n/a — not a claim` and retained (round-1 V3 / round-2 V05 class).

The two checkable §12 open dependencies were web-verified and confirmed:

- **Smith "Dying and Rising Gods" — supplied placement in *Imagining Religion*
  (1982) is wrong.** The 1982 Chicago book is seven essays ("Fences and Neighbors",
  "In Comparison a Magic Dwells", "Sacred Persistence", "The Bare Facts of Ritual",
  "The Unknown God: Myth in History", "A Pearl of Great Price and a Cargo of Yams",
  "The Devil in Mr. Jones") per the publisher blurb and the archive.org contents
  listing; no such chapter. The essay is the entry in *The Encyclopedia of Religion*,
  ed. Eliade (Macmillan, 1987), **4:521–27** — Smith's own citation in *Drudgery
  Divine* (1990), Mettinger's bibliography (BMCR 2002.09.07), and the Encyclopedia
  index at archive.org. Row rewritten, mark lifted; the anti-*To Take Place*
  substitution warning kept; residual passage check noted.
- **Enūma Eliš / akītu.** Recitation before Marduk's statue on day 4 of Nisannu is
  stipulated in one Late Babylonian ritual tablet (Thureau-Dangin, *Rituels
  accadiens*, 1921: 127–154 = ANET 332); text ed. Talon, SAACT 4 (Helsinki, 2005);
  critical treatment Debourse, *Of Priests and Kings* (CHANE 127, Brill 2022, esp.
  9–35, doi:10.1163/9789084513837), which treats akītu as historically dynamic
  rather than monolithic; Richey (Chicago diss.) on the sequence being known
  essentially from one late text and on "unchanging festival" reconstructions as
  untenable simplifications. Row now C with the recitation/drama distinction and
  anti-extrapolation rule retained and the editions named.

Edits to the corpus file (3, minimal): one appended `- sources:` bullet
("Triage round-2 additions (2026-10-17; web-verified)") and the two §12 rows;
`- topic`/`- sources:`/`- couples` header preserved; marks 9 → 7.

**Dependency notice:** `myth-symbol/myth-ritual-theories.md` and
`myth-symbol/pantheon-archetypes.md` carry the same wrong 1982 placement for the
Dying-and-Rising-Gods argument; not this batch's files, so not edited — the §12
route column now names them for whoever owns them. Canon untouched. Ledger:
`corpus/lessons/round-2-triage/V01.md`. Touched only the assigned corpus file, the
new ledger and this log entry; no commits made.

## 2026-10-17 — round 2: triage S05 (`coupling-model.md`)

Assigned file: `corpus/knowledge/synthesis/coupling-model.md` (sorted
position 5 of `corpus/knowledge/synthesis/*.md`; 202 lines, read in ≤60-line
`sed -n` windows). Five `(to-verify)` tokens found (lines 25, 143, 196, 200,
201); `grep -i 'to-verify'` returns the same five, so no bare variant was
missed.

- CONFIRM — §Provenance line 196 (the Roach-Higgins & Eicher "access
  restrictions" note). Basis: Crossref record for doi:10.1177/0887302X9201000401
  (title, both authors, *Clothing and Textiles Research Journal* 10(4):1–8,
  June 1992) retrieved 2026-10-17; the deposit record hdl:11299/162438 is
  publicly readable and exposes the published abstract, whose framework matches
  the file's summary; the p. 1 dress definition is independently quoted in the
  PMC review PMC10559650. `curl` 403s on the UDC page while a browser-style
  fetch succeeds, which most likely produced the original note. Mark removed;
  residual restated in prose; UDC record added to `- sources:`.
- 4 tokens retained as non-claims (protocol §4 applies the three outcomes to
  claims; convention per round-2 batch V05): line 25 is the **A/H/D/V** status
  legend, line 143 a **D** recipe non-claim, lines 200/201 the entry's
  competence limit and its specimen-internal evidential gap.
- Source work on line 143's feasibility premise (the model's own **F** edge):
  "triage round-2 additions (2026-10-17; web-verified)" clause appended to the
  Barber line in `- sources:` — Bender Jørgensen & Walton (1986), *Journal of
  Danish Archaeology* 5:177–188, doi:10.1080/0108464x.1986.10589966 (Crossref
  record; madder/bedstraw determinations cited at p. 184 in Vanden Berghe et
  al.'s open-access paper), and Newman & Gates (2020), "The Matter of Madder in
  the Ancient World," in the Getty APPEAR volume *Mummy Portraits of Roman
  Egypt* (open-access chapter read directly; madder fixed to textile fibers with
  inorganic mordants). §5.3 now marks the dyed wool as externally documented;
  the recipe mark stays.

Evidence: `wc -l` = 202 (unchanged), `grep -c '(to-verify)'` before = 5,
after = 4, `git diff --stat` = 4 insertions / 4 deletions on the one file.
Header preserved. Ledger: `corpus/lessons/round-2-triage/S05.md`. Touched only
the assigned file, the new ledger, and this entry; no commits made.## 2026-10-17 — round-2 TRIAGE batch Z70 (olmec)

Round-2 triage worker processed `corpus/knowledge/civilizations/olmec.md`
(sorted position 70; ledger `corpus/lessons/round-2-triage/Z70.md`). File read
only in ≤61-line chunks. 4 `(to-verify)` flags processed: 3 CONFIRM, 1 DOWNGRADE,
0 EXCISE; `grep -c '(to-verify)'` before 4 → after 0.

CONFIRMs: (a) Epi-Olmec decipherment "disputed, not a secure translation base" —
inspected Robinson (2008) *Lost Languages* p. 263 via Wikipedia "Isthmian script"
("decidedly unproven"), Macri (2017) Glyph Dwellers Reports 51–53 (R53 fetched;
R52 reads sign MS20 as a phrase-ending mark, against Justeson–Kaufman), and
Mora-Marín's 2005/2007 review PDF (defense of the decipherment) — the dispute is
live on both sides; (b) Olmec garment/textile vocabulary "thinly evidenced" —
Follensbee (2008), *Ancient Mesoamerica* 19(1):87–110, abstract inspected via
Missouri State BearWorks ("only a few fragments of cordage and woven mats have
yet been recovered"); (c) provenance note that the cited debate is not an
exhaustive survey — later structural work (Macri 2017) located and inspected;
Vonk (2020, unpublished) recorded as an uninspected lead only.

DOWNGRADE: the §Provenance "page-specific quotation… (to-verify)" sentence was an
access-limit statement, not a cultural claim; recast as an explicit citation-level
note (protocol §3/§12); full-file inspection confirms no quotations, indigenous
words, or translated royal names are introduced.

Sources appended to the entry's `- sources:` block as "triage round-2 additions
(2026-10-17; web-verified)": Follensbee 2008; Robinson 2008; Macri 2017; Mora-Marín
2005/2007. Touched only the assigned file, the new ledger, and this log entry; no
commits made.

## 2026-10-17 — round-2 TRIAGE C15 (`trade-economy-lexicon.md`)

Target: `corpus/knowledge/culture-material/trade-economy-lexicon.md`
(sorted position 15 of `corpus/knowledge/culture-material/*.md`). Chunked
`sed -n` reads only (≤60 lines). Two `(to-verify)` flags, both in the
etymology tables; `grep -c 'to-verify'` 2 → 0. Ledger:
`corpus/lessons/round-2-triage/C15.md`.

- CONFIRM — §2 calibration, "troy weight" ← Troyes "plausible but debated".
  OED online s.v. *troy* n.² (fetched 2026-10-17, public preview; entry
  status "not yet fully revised") gives etymon "Probably from a proper
  name: Troyes", first evidence c. 1390–1 in *Earl Derby's Expeditions*;
  Britannica's *troy weight* entry agrees ("supposedly derives"). The rival
  derivation was read at source — C. M. Watson 1910: 82–83 (archive.org
  full text), with his single witness, Wright's *English Dialect
  Dictionary* vol. 6 s.v. **TROY** ("A steelyard; a pair of scales… Cf.
  trone"), checked directly. Zupko 1977 was unreachable in any copy and is
  therefore not cited for the rewritten sentence. Sources added: C. M.
  Watson (1910); Wright (1898); the header's OED entry now names the senses
  and their unrevised status.
- DOWNGRADE — §4B `stock` row, "retained stock half of Exchequer tallies".
  OED online s.v. *stock* n.¹ confirms "not yet been fully revised"; its
  text (read through two OED-derived witnesses: languagehat 2020 quoting
  sense A.42 and the A.52a note that shares-sense is only *partly* the
  tally sense; Etymonline s.v. *stock*) gives an obscure, blended origin,
  not a tally origin. The popular telling (Graeber 2011, ch. 3 — already a
  lane source) also mis-names the halves ("stock" vs "the stub… hence
  'ticket stub'"); the documented terms are stock/foil. Cell rewritten to
  keep the split-object image, etymology marked unproven.

Touched only the assigned file, the new ledger, and this log entry; no
commits made.

## 2026-10-17 — round 2 triage Z51: khmer-angkor.md

Resolved sorted position 51 (`ls corpus/knowledge/civilizations/*.md | sort |
sed -n '51p'`) → `corpus/knowledge/civilizations/khmer-angkor.md`. Both
`(to-verify)` flags sit in §11 and are now processed: 1 CONFIRM, 1 DOWNGRADE,
0 EXCISE.

- CONFIRM — K.235 dating calibration. DHARMA draft edition (ERC 809994,
  rev. 2025-05-07) titles the text "K. 235. Stela of Prasat Sdok Kak Thom,
  974 Śaka"; face D line D82 carries `974 śaka`, Sanskrit stanza 123 dates the
  same event by horoscope (no month/tithi), and the carried translation glosses
  974 Śaka = 1052 A.D.; Śaka 974 spans civil 1052–1053, so "1053" citations
  (8 February 1053 in modern reference literature) are day-level conversions.
  Source [CC25] added; hedge kept in sourced form.
- DOWNGRADE — §11 "Thin areas" scope hedge recast as calibrated uncertainty
  with reasons: post-Angkor epigraphy nearly disappears 13th–16th c. and the
  royal chronicles were compiled mainly 18th–19th c. (Kolnin 2022, *RUDN
  Journal of World History* 14(4):461–484, read 2026-10-17); *neak ta*-type
  practice rests chiefly on twentieth-century ethnography (Ang Choulean 1986,
  bibliographically verified, marked as not read in the file). Sources [KL22]
  and [AC86] added.

Edits confined to the two §11 bullets, the source-access-calibration bullet and
the `- sources:` block; `- topic:`/`- couples:` untouched. Ledger:
`corpus/lessons/round-2-triage/Z51.md`. `grep -ic to-verify` on the file = 0.
No commits made.## 2026-10-17 — round 2: triage fragment Z76 (9 flags: 7 CONFIRM, 2 DOWNGRADE)

Target: `corpus/knowledge/civilizations/polynesia-navigation.md` (sorted
position 76 of `corpus/knowledge/civilizations/*.md`). All nine `(to-verify)`
marks resolved against live sources: rongorongo (L25) → CONFIRM on Ferrara et
al. 2024, *Scientific Reports* 14:2794, doi:10.1038/s41598-024-53063-7 (script
still undeciphered) and Guy 1990, *Journal de la Société des Océanistes*
91(2):135–149 (Tablet Mamari lunar calendar = most-cited content reading, not a
navigation text), plus Valério 2024 (OUP, pp. 189–224). Regional-corpora gaps
(L80, L196), the item-dating caution (L100) and chiefly tattoo entitlements
(L131) → CONFIRM, now naming Gifford 1924 (Bishop Museum Bulletin 8, 207 pp.),
Handy 1923 (Bulletin 9, 358 pp.), Krämer 1902–03 / trans. Verhaaren 1995, von
den Steinen 1925–28 (Reimer, vol. I = Tatauierung) and Allen 2006 (*Tattoo
Traditions of Hawaiʻi*, Mutual Publishing, ISBN 1-56647-770-0). Mau Moko record
(L179) → CONFIRM: Te Awekotuku with Nikora, Rua, Karapu and Nunes (photographs),
Viking/Penguin 2007, ISBN 978-0-67-004561-7 (Royal Society Te Apārangi record).
Sāmoan matai titles (L162) → CONFIRM: Tapu 2020, *UCLA Asian Pacific American
Law Journal* 24(1):61–89, doi:10.5070/P3241048154 (titles bestowed by ʻāiga
consensus, held for the family, revocable), plus Krämer. kāpeʻa antiquity (L15)
→ DOWNGRADE: two Hawaiian names for the cross recorded (kāpeʻa in Pukui–Elbert;
Hānaiakamalama via Johnson & Mahelona 1975/2015, attributed in Hawaiian
star-line teaching material) but neither dated to prehistory. Whakapapa
teaching procedures (L147) → DOWNGRADE: Roberts et al. 2004 full text blocked
and Mahuika 2019 description-level only, so recast as an explicit non-claim. A
March 2026 self-published Zenodo "LLM rongorongo decipherment" claim was checked
and set aside as non-peer-reviewed. `grep -c to-verify` on the entry = 0; file
197 → 207 lines, header preserved, ten source records added. Ledger:
`corpus/lessons/round-2-triage/Z76.md`. Touched only the assigned file, the new
ledger, and this log entry; no commits made.## 2026-10-17 — round 2: triage fragment Z69 (4 flags: 4 CONFIRM, 0 DOWNGRADE, 0 EXCISE)

Target: `corpus/knowledge/civilizations/nubia-kush.md` (sorted position 69 of
92), read in three chunks (1–60, 61–120, 121–176) per the chunked-reading rule.
Four marked propositions, all resolved by CONFIRM with a checkable source
appended to the entry's `- sources:` key line and detail lines added to its
"Source key and calibration" section; a fifth `(to-verify)` token is the
entry's own rule vocabulary for future claims and was retained unchanged
(same handling as the V07 pass). Evidence: publisher/date/ISBN/collation of
Žabkar 1975 (Aris & Phillips; 0-85668-027-3 = 978-0-85668-027-4; 217 pp.,
33 pls.) confirmed in catalogue and review records, with the lion-temple hymn
separately edited (Hintze 1962:28, reproduced at Lohwasser, MittSAG 7
(1997):33 — fetched, p. 33 checked); Amanishakheto's Beg. N 6 findspot debate
documented from Labia 2018 (HAL halshs-03941996, pp. 517–518, quoting Ferlini
1837 and reporting Budge 1907 and Markowitz & Lacovara JARCE 1991);
`amani` = Amun in Meroitic royal names from Kuckertz, MittSAG 29 (2018):119ff.
(fetched). New source keys [Lo97], [K18], [L18]. One stale cross-reference
("confirmation where marked") updated. Header preserved; edits confined to the
four flagged loci, the source block, and that sweep. Ledger:
`corpus/lessons/round-2-triage/Z69.md`. Touched only the assigned file, the
ledger, and this log entry; no commits made.

## 2026-10-17 — round-2 TRIAGE Z72 (`pacific-northwest.md`)

Target: `corpus/knowledge/civilizations/pacific-northwest.md` (sorted
position 72 of `corpus/knowledge/civilizations/*.md`). Chunked `sed -n` reads
only (≤60-line windows). Eight `(to-verify)` flags processed
(`grep -n 'to-verify'` → lines 35, 49, 99, 132, 135, 140, 152, 179; no
variant forms): 6 CONFIRM (one with scope narrowed), 1 DOWNGRADE, 0 EXCISE;
`grep -c '(to-verify)'` 8 → 0. Ledger:
`corpus/lessons/round-2-triage/Z72.md`, one row per flag.

- CONFIRM — regional coverage note. Southern Wakashan coverage now rests on
  Arima and Dewhirst (1990), "Nootkans of Vancouver Island," *HNAI* 7,
  pp. 391–411; Renker and Gunther (1990), "Makah," same volume; McMillan
  (1999), *Since the Time of the Transformers* (UBC Press). Salish side:
  Gustafson (1980), *Salish Weaving*; Tepper, George, and Joseph (2017),
  *Salish Blankets* (Univ. of Nebraska Press), co-authored with Skwxwú7mesh
  weavers. Residual left in prose: no community-authored southern Wakashan or
  Salish ceremonial-register source is consulted.
- CONFIRM — Chilkat "structural yarn": Penn Museum NA1285 ("warp made from
  wool-wrapped cedar bark fibers and weft made from wool"); National Museum
  of Finland (2020) (bark warp covered with wool, wool weft); Canada's
  History; Samuel (1982), *The Chilkat Dancing Blanket* (standard technical
  monograph, record verified). Variation now stated: bark proportion differs
  by weaver and robe (KRBD 2019, Dorica Jackson); Emmons (1907) itself not
  inspected, and the source-key sentence that promised "fine construction
  claims remain flagged" was corrected.
- CONFIRM — Chilkat "equipment and sequencing": Handwoven (2020), Lily Hope
  profile — warp fastened only to the top of the upright frame, hanging
  free, twined in small vertical sections rather than side-to-side rows;
  Haines Sheldon Museum — single-bar frame, suspended warp, optional stone
  weights (variation noted); Burke Museum (2010) — painted pattern board and
  center-plus-two-side-panel layout.
- CONFIRM — Chilkat vs Ravenstail: Alaska State Museum exhibit coverage
  (Alaska DEED, n.d., curator Steve Henrikson) — Ravenstail older, geometric,
  extinct by the early 1800s; Chilkat later, curvature/formline, wool plus
  cedar bark warp, longer fringe; Samuel (1987), *The Raven's Tail: Northern
  Geometric Style Weaving* (UBC Press, ISBN 0-7748-0224-3).
- CONFIRM — Coast Salish row: Lin et al. (2023), *Science*
  382(6676):1303–1308, doi:10.1126/science.adi6549 (woolly-dog fleece as a
  distinct fiber economy) plus Gustafson (1980) and Tepper et al. (2017).
- CONFIRM — language-implementation and naming flags: both now name the same
  verified route, Grubb (1977), *A Practical Writing System and Short
  Dictionary of Kwakw'ala (Kwakiutl)*, Mercury Series, Canadian Ethnology
  Service Paper 34, with U'mista's published orthography; no form or
  translation was invented.
- DOWNGRADE — the "potlatch tense"/honorific-affix flag: no consulted source
  documents such forms, so it is now stated as negative evidence with the
  burden of proof on any design asserting them; the one documented
  special-speech strand found (Berman 1996 on Hunt's myth-recitation style,
  quoted at second hand and flagged as such in the file) was added as the
  positive pointer.

Touched only the assigned file, the new ledger, and this log entry; no
commits made.## 2026-10-17 — round 2: triage batch Z39 (india-classical-sanskrit)

File: `corpus/knowledge/civilizations/india-classical-sanskrit.md` (sorted
position 39 of 92 civilizations entries; appears in no round-1 ledger).
8 `(to-verify)` occurrences processed — 7 CONFIRM, 1 convention retained, 0
DOWNGRADE, 0 EXCISE (every flag was a guardrail, a gap note, or the stop-rule
convention; no wrong claim to excise). Ledger:
`corpus/lessons/round-2-triage/Z39.md` (one row per flag).

Basis: UC Press pages for P06 (Pollock 2006) and K86 (Kinsley 1986) and the
SUNY page for C91 (Coburn 1991) fetched and matched against the entry's
stated chapter loci; wisdomlib Manu 2.41 (J20) read for the student-dress
loci and its comparative notes (Vaśiṣṭha 11.49; Āpastamba 1.3.1–9 —
white/mañjiṣṭhā/haridrā by varṇa); Leland, *Rainbow Body* (Ibis, 2016;
*Quest* 105.2) and Leadbeater (1927) for the Western thread of the rainbow
chakra colours; Nardi, *Theory of Citrasūtras* (Routledge, 2006) for
text-dependent colour sets; Marshall, *Mohenjo-daro*, 1:32–33 (Gulati–Turner
laboratory analysis of the cotton on a silver vessel) for image-vs-object
evidence; Alkazi 1983, Boulanger 1997, Banerjee & Miller 2003 for the
antarīya/uttarīya reconstruction labels and drape variety; Bryant 2001,
Srinivasan 1975–76 and 1984, Jung 1932/1996 for the discredited-continuity
norm. All are appended to the entry's `- sources:` line as a "triage round-2
additions" clause.

Gate: `python3 tools/gates/provenance-audit.py
corpus/knowledge/civilizations/india-classical-sanskrit.md` → exit 0,
findings=0, 1 residual mark (the stop-rule bullet, which must name the
convention). Header (topic/sources/couples) preserved; 179 lines before and
after; edits confined to the seven flagged loci plus the sources line.
Touched only the assigned file, the ledger, and this log entry; no commits.

## 2026-10-17 — round 2: triage batch Z49 (japan-yayoi-kofun)

File: `corpus/knowledge/civilizations/japan-yayoi-kofun.md` (sorted position
49 of 92 civilizations entries). 6 `(to-verify)` occurrences processed — 6
CONFIRM, 0 DOWNGRADE, 0 EXCISE. Ledger: `corpus/lessons/round-2-triage/Z49.md`
(one row per flag).

Basis: Nishimura (2018) full-text copy (Project MUSE; *Asian Perspectives*
57(1):105–158) inspected — individual-ownership thesis, six-type typology of
157 provenienced beads, Late Jōmon household-to-grave shift, and the surveyed
shape theories (fetus/tooth/moon/soul as proposals; Jōmon meanings "not
clear"). Frellesvig (2010) Introduction p. 2 inspected ("Extensive attestation
of Japanese goes back to the eighth century"); §1.2 "Sources" and §4.1 "Ainu"
located in the ToC. The Ainu-etymology caution now names Frellesvig §4.1,
Vovin (2022), "Ainu elements in early Japonic," in Bugaeva, ed., *Handbook of
the Ainu Language* (De Gruyter Mouton), 185–208, and Nakagawa (2003),
「日本語とアイヌ語の史的関係」, in Vovin & Osada, eds., 『日本語系統論の現在』
(Nichibunken), 209–220 (genetic relation improbable; contact recent/limited).
Vovin and Nakagawa were appended to the entry's `- sources:` line as a "triage
round-2 additions" clause.

Gate: `python3 tools/gates/provenance-audit.py
corpus/knowledge/civilizations/japan-yayoi-kofun.md` → exit 0, marks=0,
findings=0. Header (topic/sources/couples) preserved; 196 lines before and
after; edits confined to the six flagged loci plus the sources line.
Touched only the assigned file, the ledger, and this log entry; no commits.## 2026-10-17 — round-2 TRIAGE S06 (`cultural-translation-protocol.md`)

Round-2 triage worker processed `corpus/knowledge/synthesis/cultural-translation-protocol.md`
(sorted position 6; ledger `corpus/lessons/round-2-triage/S06.md`). File read only in
≤60-line chunks. 5 `(to-verify)` occurrences: 2 claim flags, both CONFIRM, 0 DOWNGRADE,
0 EXCISE; 3 non-claim convention tokens retained (protocol §4 class, following round-2
V05/V01/S05). `grep -o '(to-verify)'` before 5 → after 3.

CONFIRMs (both guards on the same item): Appiah, "Thick Translation", *Callaloo* 16(4):
808–819 — Crossref `10.2307/2932211` and the JSTOR issue record (i347965, Autumn 1993)
confirm identity, issue, and pagination; the essay's definitional sentence at p. 817 was
verified through two inspected open-access scholarly intermediaries that quote it with
the page number — Cammarota, "Translating Medieval Texts", Edizioni Ca' Foscari 2018,
pp. 37–54, DOI 10.14277/6969-248-2/FMM-17-2 (fetched and read in full), and "Técnicas de
traducción", New Prairie Press / Kansas State University Libraries open textbook (fetched
and read in full). The entry's paraphrase also matches the Benjamins ETSB abstract.
Residual limit stated in the entry: the paywalled full text was not collated page by
page; reopen if a full text (Callaloo or the Venuti *Reader* reprint) is inspected.

Sources appended to the `- sources:` block: DOI/JSTOR locators on the Appiah line, plus a
"Page-level corroboration" bullet naming the two intermediaries. Coherence sweeps: the §1
provenance sentence and the §14 close-out sentence, whose "Appiah passage-level
verification … remain open" clause had gone stale. Retained tokens: §6 safeguard (L93),
§8 note-discipline rule (L134), §10 coverage-card rule (L158) — convention vocabulary,
left byte-identical. Header (`topic`/`sources`/`couples`) preserved; `git diff
--numstat` = 5 insertions / 4 deletions on the assigned file, 205 → 206 lines.

Touched only the assigned file, the ledger, and this log entry; no commits.

## 2026-10-17 — round 2 triage Z52: korea-joseon.md

Resolved sorted position 52 (`ls corpus/knowledge/civilizations/*.md | sort |
sed -n '52p'`) → `corpus/knowledge/civilizations/korea-joseon.md`. 14
`to-verify` strings: 13 real flags + 1 label definition (line 10, untouched).
All 13 processed: 13 CONFIRM, 0 DOWNGRADE, 0 EXCISE. File diff = 14 insertions
/ 14 deletions (the 13 flagged lines + an appended `triage round-2 additions`
clause in `- sources:`); `grep -c to-verify` on the file went 14 → 1 (the label
definition). Ledger: `corpus/lessons/round-2-triage/Z52.md`.

Evidence highlights (all web-verified 2026-10-17, Korean reference works):

- "yesa" (L56): 禮事 occurs only as a generic phrase for a ritual observance;
  the register terms are 제사 jesa, 예 ye (한국민족문화대백과사전, 예), 예서
  yeseo (우리역사넷, "예와 제사").
- *Gukjo oryeui* (L58): 1474 state ritual code, five rite classes + same-year
  국조오례의서례 (국가유산진흥원 English notice; 한국교회사연구소 record;
  Korea Heritage Service on Jongmyo Daeje as gillye).
- Verbatim Korean (L69): 중세국어 marked tone with 방점 until tone loss in the
  central dialect in the later 16th c.; three-way honorific layer unlike modern
  speech levels (한국민족문화대백과사전, 중세국어).
- Gwageo (L91): law allowed 양인 이상; excluded 장리 sons, sons of remarried
  women, 서얼 — relaxed 1553 / 1625 허통사목 / 1696; 『속대전』 barred 천인
  from 무과; 식년문과 초시 240 (후 243), 복시·전시 33인 (갑3·을7·병23)
  (한국민족문화대백과사전, 과거 §응시 자격; Wagner 1974 added).
- Regional spirit traditions (L101): 호남·동해안·제주 corpora named
  (한국민족문화대백과사전, 무가; 우리역사넷, 지역별 무당의 호칭); backdating
  limit retained.
- 오방색 / dress colour (L113): directional map documented (국립민속박물관
  한국민속대백과사전); garment colour policed by 복식금제 bans on
  황·백·홍·자·회·옥·녹색 with per-colour reasons (한국민족문화대백과사전,
  복식금제 §복색).
- Dragon claws (L114): rank grading 왕·왕비 오조룡 / 세자 사조룡 / 세손
  삼조룡 codified by 1892 and carried into 1897; the popular "kings had four
  claws" story is contradicted by 『세종실록』 31:9:2 (1449) — sillokwiki
  사조룡의; Korea Heritage Service 오조룡 왕비 보.
- 갓끈 / 망건 (L122–123): 『경국대전』 graded cord materials by rank, 1469
  bans reached 서인; capping ceremony 15–20, headband marked adult status
  "귀천 없이", practice folded into marriage, ended by the 1894–95 topknot
  order (한국연구재단 한국복식사전 s.v. 갓·망건; 한국민족문화대백과사전,
  관례; 정진영 2008, 이화여대).
- Black-gat entitlement (L132): dated law is material/weave/brim (1441–1651,
  1670/1688), not examination passers (한국민족문화대백과사전, 복식금제
  §입모).
- 항렬 / naming (L139, L144): each lineage fixes its own 항렬표 printed at the
  jokbo head; many slave records carry a bare name with no surname; 피휘 was
  reign-specific (안대회 2010, 『한국문화』 52).

Touched only the assigned file, the new ledger, and this log entry; no commits
made. Limits: sillok entries were read through sillokwiki citations, not
collated from the printed recension; no Korean-language monograph read in full.

## 2026-10-17 — round 2: triage fragment V04 (5 non-claim tokens retained, 8 sources verified)

Assigned file: `corpus/knowledge/verification/internal-consistency-audit.md`
(sorted position 4 of `corpus/knowledge/verification/*.md`; 186 lines, read in
≤60-line `sed -n` windows). `grep -o '(to-verify)' | wc -l` = 5 (lines 14, 34,
111, 154, 165); `grep -c -i 'to-verify'` = 5 and `grep -c -i 'to verify'` = 0, so
no bare variant was missed.

- **0 CONFIRM / 0 DOWNGRADE / 0 EXCISE — 5 `n/a — not a claim` (all retained).**
  All five tokens are this method entry's own use-mention vocabulary: the mark as
  an `evidence-status` value, as the state of an unresolved locator, and as the
  prescribed action in three audit rules. Deleting one would delete the controlled
  vocabulary the protocol runs on; the three outcomes in the triage protocol §4
  apply to claims. Convention followed from round-2 batches V05/S05.
- Verification therefore went to the method claims adjacent to the tokens, and all
  held: Fischer (1970) p. 47 on the negative proof (consulted as quoted verbatim in
  Vermette 2017, *aboriginal policy studies* 6(2):92, open access — Fischer's book
  itself not inspected); Williams (2023/24), *Notes and Queries*,
  doi:10.1093/notesj/gjad106 — OED3 revised earliest dates downward for 38–44% of
  revised entries, so first attestation is provisional; TEI P5 ch. 22 (release
  documentation read directly) separating graded `certainty`, `precision`, and
  per-element `respons`; Brill's TEI–EpiDoc documentation (read directly) for
  Leiden/EpiDoc character-level certainty (`cert="low"`) plus its caveat that
  "there is, it seems, not one Leiden system"; Greenberg (2009), *BMJ* 339:b2680
  (abstract and figure captions via PubMed 19622839) — citation bias,
  amplification, and "conversion of hypothesis to fact through citation alone"
  manufacture unfounded authority; Dowden, "Fallacies," *IEP* s.v. Appeal to
  Authority (entry read); Kausch (2023), *Journal of Universal Language* 24(2) and
  Honkasalo (2011), *TULIP* 31:67–77 (both read) defining the rebus as homophonic
  substitution, so a rebus is a claim about the period's phonology.

Edits to the corpus file (minimal: 11 insertions / 2 deletions; 186 → 195 lines;
`topic`/`sources`/`couples` header fields preserved): a "triage round-2 additions
(2026-10-17; web-verified)" clause on the `- sources:` line; eight new
bold-author + Basis bullets in `## Source basis and limits`, each naming what was
inspected and what was not (Fischer via Vermette; Walton 1997 not inspected); one
"Verification boundary (round-2 triage, 2026-10-17)" bullet recording that the
five tokens are use-mention definitions retained; and a one-line re-anchoring of
the limits bullet ("The knowledge-representation sources above are **not
ethnographic verification**, and neither are the round-2 verification-method
additions"), whose old "These are …" had been left referring past the new bullets
to its original antecedent. Marker count before = 5,
after = 5 — no mark removed and none added (a draft boundary bullet that
re-quoted the literal mark was reworded to keep the count stable). Ledger:
`corpus/lessons/round-2-triage/V04.md`.

Residual: the entry still surveys no tradition-specific evidence (its own limits
bullet says so), and the `evidence-status` vocabulary remains a local convention —
a later pass could scope-label it in §1 alongside the couples graph and severity
levels. Touched only the assigned file, the new ledger and this log entry; no
commits made.## 2026-10-17 — round 2 triage Z74: Achaemenid Persia entry

Assigned file `corpus/knowledge/civilizations/persia-achaemenid.md` (sorted
position 74) carried 5 `(to-verify)` occurrences; all five are now closed and the
literal count is 0 (`grep -c to-verify` before 5 → after 0). Decisions: 4 CONFIRM
/ 1 DOWNGRADE / 0 EXCISE. Ledger: `corpus/lessons/round-2-triage/Z74.md`.

Evidence behind the decisions: (1) Boyce, "Fravaši," EI X/2: 195–199 was
retrieved through an Internet Archive copy after the live Iranica page returned
HTTP 403 — it records no certain ancient plastic representation of the fravašis,
Moulton's fravaši identification of the winged symbol, and the later scholarly
case for xᵛarənah (cites Boyce II, p. 103 n. 82); (2) Stolper, "Persepolis
Fortification Archive Project," The Oriental Institute 2006–2007 Annual Report
(ISAC PDF) describes the ARTA 2007.001 tablet as an ordinary archive tablet in
Old Persian language and script, "the first 'practical' Old Persian text ever
found, anywhere" — the ARTA PDF itself was not retrievable, which the entry now
states as an access note; (3) the ring/feather row was downgraded after
inspecting a 2008 Zoroastrian community essay that reads the ring as a "ring of
covenant, loyalty and faithfulness" and the feathers as good/bad thoughts,
words, deeds ("some interpreters consider") — the older "marriage fidelity"
wording was found in no published source, so the cell now names these readings
as modern reception; (4) Ebbinghaus et al. (2023), "An Achaemenid God in Color,"
Heritage 7(1): 1–49 shows Persepolis pigments (Egyptian blue, malachite, yellow
ocher, cinnabar, hematite, calcite) and that colour reconstructions rest on
assumptions and get revised, so the dye/rank-colour cell now states what is and
is not established; (5) the closing stop-rule marker was a method directive, so
its required comparator dating was supplied in place (Shahnameh completed 1010
CE per Iranica "Šāh-nāma").

Sources added to the entry's `- sources:` block: Stolper (2007) annual report,
Ebbinghaus et al. (2023), Firdawsī's Šāh-nāma as a dated comparator, and the
modern devotional essay labeled as reception only. Header preserved; edits were
five in-place text changes plus the source additions. Touched only the assigned
file, the ledger, and this log entry; no commits.## 2026-10-17 — round 2: triage fragment Z37 (`igbo.md`)

Target: `corpus/knowledge/civilizations/igbo.md` (sorted position 37 of
`corpus/knowledge/civilizations/*.md`). 14 `(to-verify)` occurrences pre-edit
(`grep -c`), 11 processed (CONFIRM 1 / DOWNGRADE 10 / EXCISE 0) plus 3
no-decision legend/blanket lines (L22 legend, L25 and L184 thin-coverage).
Evidence inspected as full pages/PDFs, accessed 2026-10-17:

- CONFIRM (L29→L30): Ohiri-Aniche, “Reconstructing the Igbo Cluster,”
  LLACAN/CNRS PDF — Williamson (1989) keeps Igboid/Lower Niger as a
  coordinate branch of New Benue-Congo, Williamson & Blench (2000) place it
  under West Benue-Congo, and the label “Igboid” is criticised in favour of
  “Igbo cluster”. Mark removed; source appended.
- DOWNGRADE highlights: kola reception now carries the documented igọ ọjị
  structure (mmacha okwu / mkpoku / closing prayers with itu ogu;
  presentation to the eldest, circulation, breaking) with declared
  Christian/traditionalist variation — Oyeka, *NIU Journal of Humanities*
  11(1):77–89 PDF. Calendar rescoped to Onwuejeogwu 1981's Nri-centred
  13-month/28-day scheme, described in the record as “neither universal nor
  synchronized” (Wikipedia “Igbo calendar” + ZorBari-Nwitambu & Kalu 2018,
  *IJCA R* 5(1):36–47); the book itself not inspected. Masquerade cell tied
  to the UW Ethnomusicology Archives Ottenberg finding aid (documents
  occasions, not transcripts). Odinani usage divergence recorded
  (Wikipedia “Odinani” as near-synonym usage). Mgbeke/Mgborie pattern via
  Udeani 2007, 28–29, as recorded at Wikipedia. Chukwudi/Kenechukwu glosses
  corroborated by Ezeugwu & Chinweuba, *Philosophia* 21/2018:26–47.
- Kept-open fences (no text change): local tone rules; chant melody–tone
  negotiation (Ekwueme 1974 located as lead only, uninspected); detailed
  Nri/Onitsha/Aro institution dates (948 CE claim vs 12th-century influence
  estimate).
- Achebe/Chukwukere source line corrected: JSTOR 40460646 = Chukwukere
  1983, *Anthropos* 78(3–4):519–534 (AfricaBib record); the essay text
  itself still uninspected.

Post-edit `grep -c '(to-verify)'` = 13 (12 flags + the legend line);
`python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/igbo.md`
→ 0 findings, exit 0. Ledger: `corpus/lessons/round-2-triage/Z37.md`.
Touched only the assigned file, the new ledger, and this log entry; no
commits made. Limits: Achebe, Arinze/Kalu, Onwuejeogwu 1981, Udeani 2007 and
Ekwueme 1974 were not read in full (intermediaries are named inline); no
Igbo-language dictionary or speaker check performed.

## 2026-10-17 — round 2 triage, file 1/1 (`taino.md`)

TRIAGE assignment resolved by `ls corpus/knowledge/civilizations/*.md | sort |
sed -n '85p'` → `corpus/knowledge/civilizations/taino.md`. Twelve claim-level
`(to-verify)` flags processed; the tag's own legend row and the closing
verification-boundary sentence were left intact by design. Ledger:
`corpus/lessons/round-2-triage/Z85.md`.

- CONFIRM ×8 — Granberry–Vescelius attribution caution (Adelaar 2009, IJAL
  75(2): 275–278, doi:10.1086/598773: skeptical of *Quizquella* and the Tolan
  comparison); cassava route (Harper; Wiktionary s.v. cassava — parallel
  Spanish/French/Portuguese routes from Taíno *caçabi*); canoe route (Harper
  s.v. canoe — English 1550s direct from Spanish *canoa*; Wiktionary s.v.
  canoa); Yúcahu/Atabey epithet caution (Pané gives names without glosses);
  Guabancex (Wikisource Pané index: "CAPITULO XXIII: De otro cemí llamado
  Guabancex"); batey adjudication caution (Oliver 2009: ritual performance and
  heavy betting, "the rules of betting in these times are unknown"); stone
  collars (Oliver 2009 via Walker 1993: public display / curated heirlooms);
  cave-art thin area (Cooper et al. 2016 motifs only; ICOMOS 2006: the
  Caribbean corpus was long considered undatable, mostly attributed to the
  Ceramic Age).
- DOWNGRADE ×4 — hurricane "exact Indigenous phonemic form" (only a
  reconstruction, Wiktionary *\*hurakā*; Schwartz 2015 ch. 1 documents the
  unresolved Taíno/Maya etymology: "A great deal of confusion clouds the
  etymology of the word 'huracan'"); "Amona means X" (Cooper et al. 2016: 1055
  give the name without derivation; circulated glosses unsourced — a PR OECH
  survey saying the name's meaning is little known is an image-only PDF and
  was not used); *nagua* rank/island detail (Nin 2020 quoting Oviedo — waist to
  mid-leg, longer for principal women, nothing for virgins; Díaz del Castillo —
  thigh length in Cuba); pigment recipes / color-rank dictionaries (no
  Taíno-specific study found in targeted searches).
- EXCISE ×0 — no flag turned out factually wrong; every one was supportable in
  calibrated form.

Sources added to the file: Adelaar 2009; Schwartz 2015; ICOMOS 2006; Nin 2020;
Harper extended with *canoe*; Wiktionary extended with *cassava*.

Checks after editing: `grep -n "to-verify"` leaves only L19 (legend) and L178
(boundary); table pipe counts consistent (scripted check); headers intact;
`git diff` limited to `taino.md` plus the new ledger. No commits made.

## 2026-10-17 — round-2 TRIAGE Z50 (`java-majapahit.md`)

Target: `corpus/knowledge/civilizations/java-majapahit.md` (sorted position 50 of
`corpus/knowledge/civilizations/*.md`). Chunked `sed -n` reads only (≤60 lines).
Four `(to-verify)` flags, all in prose; `grep -c 'to-verify'` 4 → 0. Ledger:
`corpus/lessons/round-2-triage/Z50.md`.

- CONFIRM — Majapahit "last date" (L47 pre-edit). Noorduyn (1978), *BKI*
  134(2–3): 207–274, full text inspected: the 1486 Pëtak and Trailokyapuri
  charters and Tomé Pires (1513) show Hindu-Javanese kings continued after
  1478, which later Javanese tradition adopted as the fall — a date Noorduyn
  shows "cannot be based on historical fact"; the end came "some forty years
  later". Herho, Herho & Susanto (2023), *Geographica Pannonica* 27(3):
  199–210 (PDF inspected): "differences of opinion regarding exactly when
  the Majapahit collapsed"; 1478 = "beginning of the collapse", 1527 = last
  year before Demak's conquest. Bullet rewritten with both dates; sources
  added.
- CONFIRM — macapat origins/inventory (L75). Sahlan & Mulyono (2012),
  *el-Harakah* 14(1): 101–114 (full text inspected): origins "sulit
  dilacak" (Purbatjaraka — born with Middle Javanese verse; Pigeaud — early
  Islamic period; Saputra's ≥1541 estimate vs the 1279 tradition); stanza
  inventories 8/11/15 by authority. Row rewritten; source added.
- CONFIRM — keris meteoritic nickel (L131). UNESCO ICH "Indonesian Kris"
  fetched: blades made "in layers of different iron ores and meteorite
  nickel". Brandstätter et al. (2025), *Meteoritics & Planetary Science*
  (abstract, DOI 10.1111/maps.14340): 1 of 5 Ni-rich krises possibly made
  with Prambanan meteorite metal; Ni and Co content alone proves nothing.
  Line rewritten; source added.
- DOWNGRADE — thin-coverage blanket (L198): rewritten as a reasoned scope
  limit (archive courtly, monumental, later-collected), marker retired per
  protocol §2.8 (naked marker without a research question).

Kieven (2013) and the OAPEN/Brill copies were bot-blocked this pass, so those
statements were not counted as inspected. Touched only the assigned file, the
new ledger, and this log entry; no commits made.

## 2026-10-17 — round-2 TRIAGE V03 (`costume-era-consistency-gate.md`)

Target: `corpus/knowledge/verification/costume-era-consistency-gate.md`
(sorted position 3 of `corpus/knowledge/verification/*.md`; 203 lines before,
205 after). 8 `(to-verify)` occurrences (pre-edit lines 11, 15, 16, 76, 158,
168, 171, 201): **2 CONFIRM / 2 DOWNGRADE / 0 EXCISE — 4 retained as
non-claims** (protocol §4 restricts the three outcomes to claims; §4.7–8; §8).

- **[L] pagination → DOWNGRADE.** The printed vol. II is lending-restricted
  (archive.org `tudorroyalprocla0002paul`: `_djvu.txt` HTTP 403, no
  search-inside), so the text was not inspected; §3's rule was followed rather
  than claiming otherwise. Pagination located through inspected citing works:
  Bolland (2011, QMUL DPhil) cites the 1574 apparel preamble at Hughes &
  Larkin II.381; Cotter (2021, *Journal of Early Modern Studies* PDF) cites the
  gilt weapons/spurs clause, identical to the transcription, at II.384; Kirtio
  (2011, *Constellations* PDF) cites the Greenwich 15 June 1574 proclamation at
  II.386. Line now asserts the narrower claim and "no full page range is
  claimed"; entry number "no. 601" left unasserted (excerpt did not pin it).
- **[M] CAMEO access → CONFIRM.** Re-checked: HTTP 403 again, Wayback
  availability + CDX report no snapshot, so the revision date stays unknown and
  is recorded as an access fact. The used proposition (spun silk from
  discontinuous fibre/waste) is corroborated by an inspected accessible source,
  Encyclopaedia Britannica "Spun silk yarn" ("Spun silk is made from short
  lengths obtained from damaged cocoons or broken off during processing,
  twisted together to make yarn"), added as key **[B]** and to `- sources:`.
- **§10 badge imagery → CONFIRM.** The collated text settles it: the closing
  note exempts "a servant … wearing any cognizance of his master" alongside
  henchmen, heralds, pursuivants at arms and apparel given by the Queen, and
  prescribes no device imagery. Row now quotes the note.
- **§10 naming → DOWNGRADE.** Blanket marker replaced by a dated, sourced
  statement: Lampert (2019, University of Leicester PhD, full text read) quoting
  Hanks, Coates & McClure (2016) — hereditary surnames "varied in different
  parts of the country and between social classes", "by the mid-15th century
  almost every person in England had a hereditary surname"; §3.2.3 on
  occupational surnames formed at surname stabilisation. Added as key **[N]**.
  Lost warrant: no formula for persons outside the settled English population.
- **4 rule/scope tokens retained** (lines 16, 76, 158, 201): the §1 directive
  to flag future unsupported items, the §5 competence limit, the §9 seed-file
  scope rule, and the §12 scarce-chronicles caution — none is an atomized claim.

Evidence: `wc -l` = 205 (was 203); `grep -c '(to-verify)'` before = 8,
after = 4 (now lines 18, 78, 160, 203); `grep -c -i 'to-verify'` = 4 (no bare
variant); `git diff --stat` = 9 insertions / 7 deletions on the one file
(§5 "Reeled silk" guard now cites `[M]/[B]`).
Header preserved. Ledger: `corpus/lessons/round-2-triage/V03.md`. Touched only
the assigned file, the new ledger, and this entry; no commits made.

## 2026-10-17 — round 2: TRIAGE Z81 (`siam-thai.md`, file 1/1)

- File: `corpus/knowledge/civilizations/siam-thai.md` (resolved by
  `ls corpus/knowledge/civilizations/*.md | sort | sed -n '81p'`).
- Flags: 8 `(to-verify)` before → 0 after; decisions 8 CONFIRM (7 recalibrated
  in place, 1 placeholder cell replaced with the verified term), 0 DOWNGRADE,
  0 EXCISE. Ledger: `corpus/lessons/round-2-triage/Z81.md` (8 rows + limits).
- Verification (all fetched 2026-10-17): [S11] Burapha University Library
  rachasap reference (PDF downloaded; `pdftotext`): ประชวร = ป่วย/เจ็บ as royal
  verb; อาพาธ = เจ็บป่วย for monks; explicit prohibition of *ทรง* before
  ready-made royal verbs ("ทรงประชวร ทรงเสวย ทรงประทับ ไม่ได้ เป็นอันขาด");
  [S12] King Prajadhipok's Institute "ศักดินาสยาม": schedules in the
  พระไอยการตำแหน่งนาพลเรือน / นาทหารหัวเมือง sections of the Three Seals law,
  attributed to Borommatrailokkanat and ชำระ under Rama I, "rai" unit
  contested; [S13] Library of Congress Law Library (2025): 1913 Surname Act
  uniqueness requirement (sec.12(5)); Persons' Name Act B.E. 2505 (1962)
  sec. 8(3); Thai act name พระราชบัญญัติขนานนามสกุล B.E. 2456, promulgated
  22 Mar 1913, in force 1 Jul 1913 (Royal Privy Purse; STOU Library pages).
  S6 and S8 re-fetched: masking accounts differ verbatim ("all the characters"
  vs "all performers except … goddesses, female humans, and some female
  demons"). S2 read from the open ZORA PDF by local extraction: §4.3 p. 600,
  *soŋ* verbal prefix / *phráʔ-thîi-nâŋ* suffix, Table 12 kin→sawoei,
  puai→prachuan. S3 record verified (CUP 2017, ISBN 9781107190764 /
  9781316641132; library catalogue records).
- Gate: `python3 tools/gates/provenance-audit.py corpus/knowledge/civilizations/siam-thai.md`
  → exit 0, marks=0, findings=0. 183 → 186 lines; header preserved; edits
  confined to the eight flagged loci, the `- sources:` line, `verified-at`, and
  three added source-key bullets. Touched only the assigned file, the new
  ledger, and this log entry; no commits made.## 2026-10-17 — round-2 TRIAGE M03 (myth-symbol/color-symbolism.md)

17 `(to-verify)` flags on 14 distinct claims: 12 CONFIRM, 5 DOWNGRADE,
0 EXCISE; `grep -c '(to-verify)'` 17 → 0; `- topic/- sources/- couples`
header intact; 18 line-edits, one file. Load-bearing corrections:

- **The Tang "674" yellow edict was wrong**: 舊唐書 卷45 輿服志 (Wikisource,
  read) gives 668 (總章元年「始一切不許著黃」) for the yellow ban and 674
  (上元元年) for the rank ladder the file already cited — re-dated in place.
- Korea's "crowd-visibility" motive replaced by the sources' grounds (white
  resembling mourning dress; rank/frugality order), with the 백의금지령 list
  (Taejong yr 1 = 1401 onward; 續大典 청의) — 한림학보 2019, 글로벌경제신문
  2022; the 백의민족 image left flagged as contested (korea.net/Joinau 2021).
- shiromuku's "dyed in the husband's family's colour" re-classified as a
  modern bridal-trade gloss; the documentable element is the Muromachi-period
  warrior bridal white (国立国会図書館 kaleido 38).
- "White = good" questionnaires (Williams & Best lineage) and the Lüscher
  row downgraded to measure-specific statements (PRAM/CMT forced choice;
  Jonauskaite et al. 2019/2020a; Kawai et al. 2022 implicit null).

Confirmed with added sources: 《元典章》 禮部·服色 至元五年「娼妓之家，家長并
親屬男子裹青巾」 (blue-green headcloth; 七修類稿 owns the cuckold idiom);
土民仕置覚 (1643) barring farmers from purple/紅梅色, repeat cycle
1667/1683/1788/1842; taijitu swirl dating (Louis 2003, *HJAS* 63); Lüscher
validity studies (French & Alexander 1972; Braun & Bonta 1979; Holmes et al.
1984, record-level); obangsaek/saekdongot (한국민족문화대백과 s.v. 색동옷;
한국민속대백과 s.v. 색동저고리); kittel/tachrichin (Dosick; Chabad.org);
white elephants (Miksic & Goh 2017 ch., cakravartin attribute with contested
casus belli); Ireland (Cronin & Adair 2002 recorded as the standard
treatment); Himba/Maasai ochre (*Cosmetics* 10(3):71, 2023); red-ink name
taboo (左傳 襄公二十三年 丹書 + Gwangju News 2013); Meiji mourning reform
(浄土真宗本願寺派総合研究所 15: 1872 decree, 1886 women's black).

Ledger `corpus/lessons/round-2-triage/M03.md` carries the per-flag inspection
level and residuals — notably no scholarly folkloristics reference for the
red-ink taboo, and Cronin & Adair (2002) and 風見明 (2008) not page-read.
Touched only the assigned file, the new ledger, and this log entry; no
commits made.

## 2026-10-17 — round-2 ADJACENCY: handoff-packet-check gate

Round-2 adjacency worker implemented the checker gate for the handoff
envelope of `synthesis/worldbible-integration-contract.md` (§4 required
fields; §1 revision/digest pinning; §6, §8.7 and §11 checklist canon
standing) and for the glossary `etymology` profile of
`synthesis/glossary-registry-format.md` (§§2, 4). New files, and the only
files touched besides this entry and the SKILL.md registry row:
`tools/gates/handoff-packet-check.py` (stdlib only),
`tools/gates/fixtures/handoff-packet-check.md`,
`tools/gates/fixtures/handoff-packet-check.expected`. No commits made.
The contract plays the spec role; no separate verification spec was
written.

Interface: `handoff-packet-check.py <packet.md>` (or `-` for stdin)
prints `FINDING <id>: <LEVEL> — <message>` plus INFO lines; exit 0 clean /
1 findings / 2 could-not-evaluate (HO-DATA: not a Markdown document,
unreadable, non-UTF-8, usage error). Finding IDs: HO-DATA, HO-MISSING,
HO-EMPTY, HO-BASELINE, HO-CONTRACT-REF, HO-MANIFEST-DIGEST, HO-DEP-FLOAT,
HO-CANON-MARKER, HO-CANON-CLAIM, HO-GLOSS-ETYM. Fields count as supplied
when named as a section heading, a `- field: value` item, or a table-row
first cell; a `(to-verify)`-only or placeholder value is HO-EMPTY.

Measured: `python3 tools/gates/handoff-packet-check.py --selftest` →
"selftest: OK — fixture findings 11 across 9 ids (HO-BASELINE,
HO-CANON-CLAIM, HO-CANON-MARKER, HO-CONTRACT-REF, HO-DEP-FLOAT, HO-EMPTY,
HO-GLOSS-ETYM, HO-MANIFEST-DIGEST, HO-MISSING); clean control exit 0;
probes cover canon, baseline, dependency, contract_ref and glossary
vocabulary; malformed inputs exit 2; CLI verified from another cwd"
(exit 0). Fixture run: exit 1, 11 findings, `fields=13/16
glossary-entries=3`, one INFO glossary-external (A3). `/dev/null`, an
absent path and an argparse usage error exit 2; stdin run exits 1; the
fixture bytes are unchanged after the run (`md5sum -c` passes). Full loop
`for g in tools/gates/*.py; do python3 $g --selftest; done` → all 7 exit
0. The fixture is synthetic and labeled non-canon; it asserts no world
fact and no canon standing. SCORECARD operability re-measure (gates now
count 7) is the round closer's action.

## 2026-10-17 — round 2 triage Z73: parthia.md (14 claim flags cleared)

Resolved position 73 of `ls corpus/knowledge/civilizations/*.md | sort` →
`corpus/knowledge/civilizations/parthia.md`. Literal `(to-verify)` occurrences:
16 before = 14 claim flags + 2 method-grammar references (line 13 grammar rule;
line 211 process note, both left in place as method); 2 after. Decisions:
14 CONFIRM, 0 DOWNGRADE, 0 EXCISE. Ledger with one row per flag:
`corpus/lessons/round-2-triage/Z73.md`.

Verification highlights: Sellwood 71.1's `wl` read as a short Aramaic-script
form of the royal name (Hopkins's Vologases I page and inscriptions index —
fuller `wlgšy MLK'` on later Vologases IV issues; Nabel 2017 Cornell diss.,
"wl, an abbreviation"); Isidore *Parthian Stations* §6 (Schoff 1914) keeps the
Bazigraban custom house separate from the Ecbatana treasury/Anaitis temple, and
the edition's silk material sits only in Schoff's commentary and the appended
Chinese annal passages (Hirth); Polybius 10.27.12 attests the temple's stored
wealth (gilded pillars; silver tiles and bricks); Boyce's "Gōsān" entry read in
full via the Internet Archive copy (Manichaean Parthian `gwsʾn` 4th–5th c. CE;
Armenian `gōsān`; Mandaean `gwsānā`; 11th-c. *Vis o Rāmin*), with the
hereditary-household bard explicitly her probable inference; Boyce 1957
page/DOI metadata confirmed at the article page plus an independent
bibliography; Alram 1986 record via the Iranica bibliography (s.v. Hēraus) and
the IPNB series record; the Iran Chamber art excerpt identified as Edith
Porada, *The Art of Ancient Iran* (1965), ch. 14 "The Art of the Parthians"
(chapter title, volume series reference, Internet Archive contents list, and an
independent thesis citation agree); Curtis 2012 (Wick–Zehnder volume) for the
iconography cautions.

Sources added to the entry: Polybius, Porada, Curtis, Nabel, plus the trail
bullets rewritten for the Iranica access route. Touched only the assigned file,
the new ledger, and this log entry; no commits made.

## 2026-10-17 — round 2: triage fragment Z12 (austronesia-philippines-taiwan.md)

Resolved position 12 of `ls corpus/knowledge/civilizations/*.md | sort` →
`corpus/knowledge/civilizations/austronesia-philippines-taiwan.md`. Literal
`(to-verify)` occurrences: 1 before = 1 after — the calibration-label legend,
retained as method (no live claim flag). This file's round-1 batch (Z03) was
filter-killed after its edits were committed and logged as carried debt; its
10 claim rows were re-audited here, not re-decided: 19 CONFIRM, 0 DOWNGRADE,
0 EXCISE, plus 8 additional load-bearing claims checked. Ledger with one row
per flag: `corpus/lessons/round-2-triage/Z12.md`.

Verification highlights: Unicode 17.0 §17.1 read word-for-word for the Pallava/
Kavi route uncertainty; Findley et al. 2022 Table 1 ("Settlement Terrace —
Latangan/boble/kubu") plus the separate *Boble* section; UNESCO record 00015
("before the seventh century"; "Since the Ifugao's culture is matrilineal …"),
same text in the 2001 proclamation compendium; Brown 1919 page images (printed
p. 79 = *Hibiscus tiliaceus* cordage; p. 56 ff. = abacá section; index
"Hibiscus tiliaceus 8, 79, 81, 103"); Calapis et al. 2011 abstract (buntal
extracted from buri petioles, two fibre caps); Ochiai 2021 repository record
("Kumu Watan literally means 'Kumu, the child (daughter) of Watan'"); Taru's
*Pacific Arts* article (*K'gi*; *P'jit*, the girl who grew wings); National
Museum exhibition terms (*maamlag*, *moma*, *hapid*, *bayah*, *bulul*);
Cultural Survival's *gaga* gloss and tattoo reasons; *Philippine Mats* (1913)
on *Corypha elata*.

Correction: Plasencia's festival passage sits on printed p. 186 of Blair &
Robertson vol. VII, not p. 177 (scan running head "186" + BookReader leaf 190
→ pageNum 186; TOC relation start p. 173). Fixed in three places, and the
register line now links the 1903 scan. Touched only the assigned file, the new
ledger, and this log entry; no commits made.

## 2026-10-17 — round 2: triage carry-over + lore-handoff adjacency (REJECTED)

Claims (declared before dispatch):
1. freshness — resolve >=400 of the 795 carried/remaining to-verify flags
   (sum <= 395). Measured after dispatch: 795 → 587 (208 net; 43 new
   ledgers in corpus/lessons/round-2-triage/). Target missed by 192.
   VERDICT: improved in fact, claim falsified as declared.
2. adjacency — executable handoff path to lore: a non-canon sample packet +
   a contract-check gate + a passing run + L0 question. Measured: 0 →
   tools/gates/handoff-packet-check.py (selftest green) +
   examples/handoff-packet.sample.md passing with fields=16/16,
   glossary-entries=20, exit 0; L0 line appended (.ufo/l0-questions.md);
   lesson corpus/lessons/round-2-adjacency.md. VERDICT: improved, verified.

Admission: REJECTED — not every claim verified (freshness below target).
No axis harmed. Freshness progression carries to round 3, right-sized.

Dispatch record: token-plan key 3 quota-dead at launch (monthly quota,
resets 2026-10-28); key 2 also dead (resets 2026-10-23); relaunched on
key 1 (probe confirmed quota) — 46/49 completed, 7 filter-killed
(linguistics pos 11; synthesis pos 7; civilizations pos 71, 82, 83, 87,
88) — third filter strike on the same files; carried as debt, to be
finished by the lane directly or retried after quota reset.

Serialization correction (evidence rule): the round-2 YAML packet's
validation block claimed handoff-packet-check exit 0 / fields=16/16; the
committed Markdown-native checker re-runs exit 1 over the YAML
(field-recognition misses). Corrected pre-freeze inside the .yml (its own
edit discipline permits pre-freeze amendment), and the envelope was
re-serialized in the contract-default Markdown as
examples/handoff-packet.sample.md, which passes clean. Contract file digest
verified: sha256:50c4c2f2…8fb7268c1. L0 question to lore already asks lore
to confirm intake format; the Markdown serialization is kotodama's
producer-side default unless lore answers otherwise.
## 2026-10-17 — round 3 D2: component 14-kin-address written

Delivered `examples/culture-d2/components/14-kin-address.yml` (round-3
D2 design drill; marked `canon: not canonized (D2 design drill)`).
Omaha-type kinship on an Iroquois base for D2's segmentary
pasture-holding lineages (patrilineal, male-line pasture rights): MBD/MBS
skew, cross-cousin distinctness, partial affine-merging, 24 kin-lexicon
records K01-K24, a feature matrix, a five-column term table, twelve
address rules (pitch compass, wind-name licence, storm law, name closing,
stranger + salt-kin protocol, teknonymy, marriage-direction pitch, joking
licence, bystander rule, dry-word rule, seasonal address ecology,
refusal/repair), the `suwá` ("held-air") avoidance register with a
generative class-word substitution table and pitch flattening, four era
strata ES0-ES3, five metadiscourse artifacts, six stress-test scenes, nine
typed coupling edges written as CONTRACT FIELD paths, an import audit, and
a `follows:` list of 20 corpus-section citations.

Evidence (local, pre-freeze): lines=436 bytes=41526; K-records=24, all
unique; block ids=49, all unique; all 8 cited corpus paths exist; 0 tabs;
YAML validity unverified (PyYAML absent in this environment). Import grep
`grep -n -i -oE "river|water|flood|tie|rope|yoke"` → 6 hits, every one
inside the import-audit note itself or a substring false positive
("property"); the one binding-image gloss found in self-review (K13
'yoke-mate') was re-coined to 'the one across the fire' before freeze.
Frozen digest (final, after all pre-freeze amendments including a
path-typo fix in the R01 follows line; the component's validation block
records the check-time digest d8967e2b… and points here):
`sha256:4bfa35d08ae7345dea47852ebfc4734b469c671764bbefd2cc0f3a257330a6a6`
(435 lines, 41578 bytes). No sibling component or corpus
file was read or edited for content; cross-component needs are stated as
CONTRACT FIELD paths because the round-3 CONTRACT block was absent from
the writer's dispatch text — flag for the round closer. No commits made.## 2026-10-17 — round 3 D2: corpus gap-fill mesoamerica-primary-sources written

Delivered `corpus/knowledge/civilizations/mesoamerica-primary-sources.md`
(round-3 gap-fill; a real-world reference entry, not a D2 design component,
so the D2 shared-culture seed does not govern it and no `culture:`/`follows:`
header keys apply — the corpus house format is topic/sources/couples; the
equivalent decision-table list sits in §11 "Corpus couplings and handoff").
Content: surviving codex inventory with holdings (four Maya screenfolds,
incl. Códice Maya de México / ex-Grolier and its 2018 radiocarbon
authentication; Borgia Group; Mixtec group incl. the Selden palimpsest;
Nahua tribute/history books; lienzos), indigenous-language alphabetic
sources (Florentine Codex, Mendoza, Chilam Balam, Popol Vuh, Cantares,
Zapotec documents via Ticha, Relación de Michoacán), missionary grammars
(Córdova 1578, Molina, Motul tradition), modern epigraphy and archives
(CMHI, TWKM/Bonn, Wayeb, Glyph Dwellers, the Isthmian dispute, Cascajal
contested, AILLA/CARE), a ten-item provenance checklist, a four-date
source-criticism protocol with a minimum-source table, calibration
(B/C/R/H/T vocabulary), and a canon-boundary close.

Evidence (local, pre-freeze): lines=161 bytes=32633; predicate `python3
tools/gates/provenance-audit.py corpus/knowledge/civilizations/mesoamerica-primary-sources.md`
-> exit 0, findings=0, INFO to-verify-count 39 marks on 32 lines (inventory
only, per provenance-audit-ledger-format §5). All 18 corpus paths cited by
the entry resolve (`test -f` loop, all OK). Citations web-verified this pass
before writing: SLUB Dresden codices pages (Códice Maya de México chain:
Saenz 1965, Grolier Club 1971, Mexico 1974); Solís et al. 2018 / INAH
2018-08-30 authentication (La Jornada 2018-08-31); Snijders, Zaman & Howell
2016 doi:10.1016/j.jasrep.2016.07.019; Princeton Digital PUL Chumayel C0940
no. 4; Boone 2007 ISBN 978-0-292-71263-8; Miller & Brittenham 2013 ISBN
978-0-292-74436-3; Saturno, Stuart & Beltrán 2006 doi:10.1126/science.1121745;
Relación de Michoacán MS Escorial C-IV-5 (1539–1541); TWKM/classicmayan.org
(Univ. Bonn, from 2014, dir. Grube); CMHI Peabody series identity; AILLA
(UT Austin, DELAMAN, 2024 relaunch). Where only a bibliographic record was
inspected, the claim carries `(to-verify)`.

No sibling component or corpus file was read or edited for content; no
commits made. Flag for the round closer: gap-fill dispatches carry the D2
shared-culture-seed boilerplate although corpus reference entries are
seed-exempt by house format — cost is one wasted interpretation step.

## 2026-10-17 — round 3 D2: component 01-brief written

Delivered `examples/culture-d2/components/01-brief.yml` (round-3 D2 design
drill; `canon: not canonized (D2 design drill)`). Supplies the CONTRACT
block the round-3 dispatches were missing (flag raised by the
14-kin-address writer): design problem, seed restated SEED-01–08, spine
SP-01–03 (verticality + wind), aesthetic stance AS-01–05, D1 contrast
R-01–06, D1 no-import list D1B-01–09, coupling principles CP-01–13,
comparator register CMP-01–06 (each a corpus entry with its own cautions),
component registry C-01–C-10 + C-14 + C-ASM, contract (ID namespaces, era
tag space E0–E3 with an explicit alias rule, per-key record fields matching
the six executable gates, rules RG-01–08 incl. the knot-geometry rule
against the D1 tying metaphor), per-component acceptance A-01–A-14 plus
A-ASM, assembly plan with the six gate commands, open questions OQ-01–05.

Reconciliation: component 14-kin-address (delivered earlier this round,
pre-contract) is registered as observed and aliased under RCN-01–03 —
K01–K24 maps to the kin/address namespace, ES0–ES3 aliases into the E0–E3
tag space by a declared mapping recorded at assembly; no delivered record
is renamed or renumbered and no sibling file was edited.

Evidence (local, pre-freeze): lines=338 bytes=48205; YAML parsed clean by
Ruby/Psych (`YAML.safe_load_file`, Date permitted); 96 record ids, zero
duplicates; all 37 distinct cited corpus paths exist; 0 tabs; corpus files
read in <=80-line windows. Digest
`sha256:ea0d67d0179aba4b118016f32f6cbf0d5e0dde92b1e8468ee6535e5026f2ea19`.
Scope: wrote only this component and this log line; no commits made.
## 2026-10-17 — round 3: D2 design drill — component 12-rank-rules (write)

Assignment: write `examples/culture-d2/components/12-rank-rules.yml` (D2, round-3
design drill; non-canon). Deliverable: sumptuary-style rules — who may wear, say,
and touch what — each rule carrying authority, jurisdiction, era, and
prescription-vs-enforcement-reality, with wear rules referencing 11-costumes
garment ids by contract.

Written (607 lines, `canon: not canonized (D2 design drill)`; starts
`component: 12-rank-rules` / `culture: D2`):

- `follows:` — 15 corpus citations with path + section (sumptuary-law-rank-display,
  costume-semiotics, dress-through-eras, textile-technology, trade-economy-lexicon,
  era-periodization-models, costume-language-coupling-table, politeness-taboo-
  euphemism, sociolinguistics-registers, ritual-liminality, cosmology-cosmography,
  and four civilization comparators: mongol, amazigh-berber, finnic-sami,
  newar-nepal). Per-record `follows:` cite alias + section against that list.
- `depends_on:` — the 11-costumes garment-id contract (ids consumed, not copied),
  the packet `lexicon:` field for degree-slot surface forms, and the packet
  `eras:` list; each marked `(to-verify)` because those siblings were not on disk
  at write time (`ls examples/culture-d2` → no such directory).
- 8 required garment ids (`garment_refs`, GAR-01..GAR-08) with the gloss each rule
  assumes, so a sibling id mismatch is remappable by gloss alone.
- 6 degree slots + gender clause; 9 wear rules, 6 speech rules, 6 touch rules;
  authority (4 bodies), jurisdiction (3 altitude bands), enforcement (4 officers),
  sanctions (5), loophole dialect (6), black-market spread (5 rows, the §10.8
  handoff artifact), era staging (3 eras), 5 scene hooks, calibration, handoff.

Spine coupling (declared D2 spine = verticality + wind): every rule keys to an
altitude band; enforcement migrates with the transhumance; storm law suspends and
creates bans; the pitch-accent/script mismatch (a written clause is "mute law"
until recited) makes the pre-writing knot archive legally authoritative. The
`spine.anti_import` field records that no D1 river/binding imagery is used;
`grep -i "river|ferry|tying|binding"` returns only that anti-import line plus
"bale-tying" cord use.

Evidence (commands run, cwd = repo root):
- `ruby -ryaml -e 'YAML.unsafe_load_file("examples/culture-d2/components/12-rank-rules.yml")'`
  → parse OK (initial parse failed twice: a `note:` key mixed with list items
  under five nodes, and one block left indented inside the `degree_slots`
  sequence — both fixed and re-verified).
- structural checker (one-off, /tmp): header + canon markers; all rule records
  have id/follows; prescription/authority/jurisdiction/era/enforcement_reality/
  sanction present on every wear/speech/touch rule; every `follows` alias resolves;
  every GAR id referenced and every reference defined; every id-shaped token in
  the text defined → `ALL CHECKS PASS (70 ids, 8 garments, 15 aliases)`.

Carried to-verify: GAR-* id reconciliation with 11-costumes; LEX-DEG-1..7 surface
forms and pitch-accent class (lexicon component); era-1..3 label reconciliation
(packet `eras:`); felt-days assay reconciled with the material-culture component;
coupling-table §9 audit run at handoff. Touched only the assigned component file
and this log entry; no commits made; no corpus or sibling component edited.

## 2026-10-17 — round 3: component 06-pantheon written (D2 design drill)

Delivered `examples/culture-d2/components/06-pantheon.yml` (round-3 dispatch
stem 06-pantheon; `canon: not canonized (D2 design drill)`; 508 displayed
lines, 507 newline-terminated; sha256
`5c5fbe714186a72a6a1fbbc90d226d6ce039b62fa96c8713bfea5d12944a65bc`).
Content: 7 PAN- agents (storm-law patron, breath/death keeper, high-pasture
power, salt-road keeper, demoted sky-holder, trickster with an institution
and no cult, deified road founder), 15 role rows using all five contract
status marks with deliberate blanks (no creator, no sun/moon deity, no love
deity, war and smith slots merged), 5 MYTH- narratives each with a rival or
variant telling, 5 RIT- rites across the ascent/descent year, 5 pantheon
career events (demotion, rise, deified human, foreign equation, schism),
7 declared blanks, 5 open questions, 38 corpus follows entries and 6
contract_deps rows. Every record carries id, axis and evidence; cross-
component references are IDs only (RG-03); era tags drawn from the fixed
space E0–E3; tally-knots count and never bind (RG-01).

Evidence (local, pre-freeze):
- `python3 tools/gates/myth-consistency-gate.py examples/culture-d2/components/06-pantheon.yml`
  → exit 1, exactly one finding: MC-S00 no symbol ledger present. Disposition:
  expected cross-component hold — `symbols[]` is owned by the symbols
  component (registry C-06; delivered 08-symbols.yml), so the packet-level
  ledger is assembled from that file, not this one.
- Same file plus a minimal conforming symbol ledger (scratch copy
  `/tmp/d2-stub-symbols.yml`) → exit 0, zero findings; proves the PAN, roles,
  RIT and MYTH sections contribute no finding once the packet carries a
  symbol ledger.
- Same file plus the delivered symbols block (08-symbols.yml lines 67–327;
  scratch copy `/tmp/d2-trial-packet.yml`) → exit 1, MC-S00
  under-normalized symbol keys, every instance naming a symbols-component
  record. Not a defect of this component: those records carry no `medium`
  key, which registry acceptance A-06 requires. Reported to the integrator;
  not fixed here (this worker writes only its own file).
- D1 self-scan over record text: D1B-01 clean (no river/water term in record
  text); D1B-02 hits are explicit negations, allowed counting-knots, or the
  linguistic term `bound form` — two plain-English connective uses were
  reworded during self-scan; D1B-04 and D1B-05 not applicable; D1B-06 clean
  (no D1 fixture form or name). Formal D1B review remains a review-class
  check, listed in the file's validation block and not resolved here.

Integration findings handed over, not absorbed (no sibling file edited):
(1) component numbering — dispatch says 06-pantheon, the 01-brief registry
names C-05 as the pantheon slot and 06 as symbols (OQ-P01); (2) era labels —
the delivered symbols file writes E1–E4 while the contract's fixed space is
E0–E3 with an alias rule (OQ-P02); (3) symbol IDs — registry prefix SYM- vs
delivered S1–S9 (OQ-P03); (4) 02-phonology and the lexicon component were
not present at write time, so every spelled form is provisional on the
03-morphosyntax placeholder segment set and every L-/P-/NM-/SYM-/ER-
reference is recorded UNRESOLVED per RG-04, not invented (OQ-P04, OQ-P05).

Scope: wrote only this component file and this log line; no commits made.

Addendum (same worker, after the round's later components landed): 02-phonology,
05-lexicon, 07-myths-motifs, 09-eras-calendar, 10-materials and 11-costumes
appeared after this component was drafted, and two of them bear on it. (1) ID
collision — 07-myths-motifs occupies MYTH-01 and MYTH-04 to MYTH-08, while the
contract's namespace row gives MYTH- to the pantheon component and this file
used MYTH-01 to MYTH-05. The five narratives here were re-prefixed to
PAN-MYTH-01 to PAN-MYTH-05, declared in the file header per RCN-02 and raised
as OQ-P06; no sibling file was edited and no other file references these IDs.
(2) Lexicon mismatch — the delivered lexicon's roots differ from the working
roots in this file, so a lexicon_alignment note now states plainly that no L-
alignment is claimed and the theonyms must be re-derived from the delivered
L- records at assembly. OQ-P02 and OQ-P04 were updated for the delivered era
range (E0-E5 in 09-eras-calendar) and for the late delivery. Re-verified after
the amendments: standalone gate run exit 1 with the single expected MC-S00
cross-component hold; run with a minimal conforming symbol ledger exit 0, zero
findings; 22 record ids, all unique, no bare MYTH- ids remain. Final digest for
the frozen component: sha256
`381720ad04d0562942fca8dd98cdb337b91b09fa9f9f25177e053bd891d084af`, 510 lines.
The digest in the entry above is superseded by this addendum. Scope unchanged:
wrote only this component file and LOG.md entries; no commits made.## 2026-10-17 — round 3: component 06-pantheon reviewed (findings; all repairable)

Review written: `examples/culture-d2/reviews/06-pantheon.md`; target revision
507 lines, sha256 `5c5fbe71…` (mtime 14:35:14Z). Six minor defects listed in
the `component-id | violation | corpus path:section` format: two dead corpus
citation paths (PF-33/34 cite `synthesis/comparative-frameworks.md`,
PF-37 cites `synthesis/symbolism-synthesis-method.md`; both files live in
`myth-symbol/` — verified), PH-01…PH-05 missing `follows:` (RG-02), TP-01…03
missing per-record `evidence` with TP-01 asserting an M- compounding record
that 03-morphosyntax does not deliver, one role row without reason/scope,
one status-token drift (`EXPLICITLY-UNEXPLAINED`). No FAIL-class violation:
role coverage, no real-pantheon renaming, and era consistency all pass.

Evidence (cwd = repo root):
- `python3 tools/gates/myth-consistency-gate.py examples/culture-d2/components/06-pantheon.yml`
  → exit 1, single finding MC-S00 (no symbol ledger) — reproduced the writer's
  V-P01; every other evaluated check clean.
- cited-path loop over every `corpus/…md` cite → only the two `synthesis/`
  paths missed; all other cites resolve to real sections.
- real-theonym scan (Zeus, Indra, Perun, Þórr, Baal, Marduk, Osiris, Yama,
  Óðinn, Amaterasu, Inanna, Aphrodite, Ares, Mars, Hades, Hel, Loki,
  Prometheus, Māui, Raven, Coyote) → zero record-text hits; D1 term scan →
  only guard negations and RG-01 counting-knots.
- freeze digest cross-check: the file's claimed digest matches LOG.md's
  round-3 (06-pantheon) entry and the reviewed bytes, `5c5fbe71…`.

Escalations verified and left with the integrator: OQ-P01 numbering,
OQ-P02 era tags (08 writes E1–E4, 09 writes E0–E5; contract fixes E0–E3).
Scope: wrote only the review file and this log line; no component or corpus
file edited; no commits made.

Digest correction (06-pantheon worker, same round): after one final edit (the
unresolved list in the validation block, now OQ-P01 to OQ-P06) the frozen
component's digest is sha256
`ef0ebf64f787d04730b6a22c7cf9fafb4de0c5e6dae2db223f57cf53de460478`, 511 lines.
The digest quoted in the addendum above (381720…, 510 lines) is superseded by
this line. Re-verified at this revision: standalone gate run exit 1 with the
single expected MC-S00 cross-component hold; run with a minimal conforming
symbol ledger exit 0, zero findings. No further edits to that file are
planned by this worker.## 2026-10-17 — round 3: D2 12-rank-rules — post-landing contract alignment

After the 12-rank-rules write entry above, sibling components landed on disk
(01-brief.yml 11:33, 11-costumes.yml 11:35, 09-eras-calendar.yml 11:33). Read them
in chunks and aligned this component to the live handoff contract; only the
assigned component file was edited.

What was checked and changed:

- `11-costumes.yml` scopes ten garment records GAR-01..GAR-10 and states that
  GAR-01..GAR-08 are written to be compatible with this file's `garment_refs`
  (ids and glosses matched) — so the id contract this component declared blind is
  now satisfied by the sibling. Verified: its `deps` ids
  [WR-01..WR-09, TR-02, TR-03, TR-05, TR-06, LO-01, LO-02, LO-05, DEG-1] all
  resolve here (17/17, ruby check).
- Renumbered this file's loophole ids LO-1..LO-6 -> LO-01..LO-06 (the sibling's
  deps already cite the two-digit form, and its deps were read off this file
  while the two-digit refs were still in `garment_refs`); updated the three
  `garment_refs.appears_in` rows and the `axis_by_record` keys; `grep -c
  "LO-[0-9]\b"` now returns 0 (no stale single-digit refs).
- 01-brief.yml contract: added `brief_ref` + `contract_conformance` declaring
  RG-01 (knots are record geometry only), RG-02 (every record carries follows),
  RG-03 (cross-component references by id only), RG-05 (per-record axis) and
  CP-07/CP-09/CP-11. Because the brief landed after this file, the pre-contract
  handles are aliased by declaration, per CP-07 ("pre-contract components alias
  their own era prefixes in, never silently").
- Added `axis_by_record` (62 ids; neutral entries carry the RG-05 coupling_note).
- Added `brief_tag: E0 / E1 / E2` to eras ER-1/ER-2/ER-3, with era *names*
  deferred to 09-eras (E0 Open Grazing, E1 First Ascent, E2 Salt Turn — read from
  that component's era tables, not asserted here).
- Added `follows:` to all six degree slots and to the gender clause (RG-02).

Evidence (cwd = repo root):
- `ruby -ryaml -e 'YAML.unsafe_load_file(...)'` -> "YAML parse: OK".
- structural checker (one-off, /tmp) -> `ALL CHECKS PASS (70 ids, 8 garments,
  15 aliases)`; rule-record field coverage for `id/prescription/authority/
  jurisdiction/era/enforcement_reality/sanction/follows` -> no misses;
  `axis_by_record` covers all 21 rank-rule ids.
- cross-ref resolution -> 17/17 of 11-costumes' deps ids resolve here.

Remaining to-verify: GAR-09/GAR-10 are the sibling's own records and take no
rules from this component (its own note); LEX-DEG-1..7 surface forms and pitch
accent classes stay with the lexicon component; the felt-days assay should be
reconciled with 10-materials before assembly; E3 (brief tag) is not claimed here.
Touched only examples/culture-d2/components/12-rank-rules.yml and this log entry;
no commits made.### addendum to the entry above (same day)

Aligned two more items after reading 10-materials.yml:

- Assay reconciled: 10-materials already works the **felt-day** as an
  action/substance unit (its measures note cites trade-econ §2 alongside the
  salt-cake) and assumes the **G1-G3** grade slots this component uses, so the
  felt-days `(to-verify)` in `calibration.design_flags` and `open_checks` is
  cleared and replaced with the reconciliation note.
- Added `garment_refs_note` recording that GAR-01..GAR-08 are the records the
  rules consume (11-costumes matches ids and glosses) and that its GAR-09/GAR-10
  are outside this component's rule set.
- Open item carried for the integrator (not this component's to resolve):
  10-materials.yml works era slots E1-E4, which do not line up with the brief's
  fixed E0-E3 space (11-costumes' own reconciliation table already warns of the
  same class of mismatch). This file carries brief tags E0/E1/E2 plus its own
  pre-contract handles, so it is not party to the mismatch.

Re-verified: `YAML parse: OK; lines=691`; checker `ALL CHECKS PASS (70 ids,
8 garments, 15 aliases)`. Only the assigned component file and this log entry
were touched; no commits made.Correction (round 3, 14:40Z): the 06-pantheon review pins revision
`ef0ebf64…` (510 lines, mtime 14:37:46Z), not the `5c5fbe71…` named in this
worker's entry above — the writer revised the component after the review
draft (narratives re-prefixed to PAN-MYTH-*, OQ-P02/OQ-P04 updated, OQ-P06
added for the MYTH- namespace collision with 07-myths-motifs). All six
findings were re-verified against the new revision and stand; the writer's
LOG digest above corresponds to the intermediate 507-line revision and
should be recomputed at assembly. `examples/culture-d2/reviews/06-pantheon.md`
updated accordingly (no component or corpus file touched).## 2026-10-17 — round 3 D2: component 11-costumes written

Delivered `examples/culture-d2/components/11-costumes.yml` (round-3 D2 design drill,
non-canon): 10 garment records (GAR-01..GAR-10), 9 material records (CMAT-01..CMAT-09),
3 cloth sources (CS-01..CS-03), plus the reading tables the component is judged by
(wearer institutions, two-wardrobe calendar, legibility stations, enforcement economy,
reading ledger, misread scenes, drift plan, form slots).

Contract handling (components landed mid-write were read and reconciled, not ignored):
- GAR-01..GAR-08 match the garment refs 12-rank-rules had already declared in its
  `garment_refs` block; its rule ids are carried per garment as typed I-edges; GAR-09 and
  GAR-10 are this component's own (pack-ox down under-tunic, leather gale legging). This
  file writes no rank-rule records — the law stays in 12-rank-rules and is consumed by id.
- Material ids were re-lettered CMAT-* because 10-materials owns MAT-01..MAT-22; every
  record carries a `maps_to` slot mapping, per that file's instruction to map by slot
  rather than by label. Two dispatch-mandated materials have no counterpart in that
  inventory (pack-ox down: their pack-ox yields only hair cordage; silk: their anchor-era
  luxury is lowland-broadcloth MAT-07) — carried as REPORT-don't-merge findings (OQ-3),
  not silently dropped or merged. The competing local dye was withdrawn in favour of
  10-materials' hearth-dark slot.
- Era tags E0-E2 of the contract's fixed space; 09-eras-calendar uses the same tags and
  agrees on both costume seams it states (felt layers from the earliest stratum; lowland
  cloth not before the E0/E1 seam). era_reconciliation maps the 10-materials,
  12-rank-rules, 08-symbols, 05-lexicon and 14-kin-address label sets at slot level.
- Surface forms are the lexicon component's: no form coined here; 10 LEX-GAR-* slots
  requested with (to-verify) forms (L35 mirken and L34 mir referenced as landed).
- D1 self-scan: no river/water/binding imagery in record text; the banned-word hits are
  explicit negations; 10-materials' local nettle-bast is noted and no garment row is bast;
  hem cords are record geometry (RG-01) and never obligation.

Evidence (local, pre-freeze):
- `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d2/components/11-costumes.yml`
  → first run exit 2 (G-DATA: input is not one mapping): two keys sat at the same indent
  as their sibling list items (era_reconciliation.warning, form_slots.note), invalid YAML
  there. Re-placed; every later revision re-run.
  Final run after the reconciliation: exit 0, zero findings.
- Structural check on the same file: 10 GAR records carrying all eight contract fields
  (garment, material, wearer_rank, rite, era, route, axis, evidence); 9 CMAT entries each
  with kind/stage routes and a composition; 3 cloth sources with max_width_m and eras;
  spine_coupling, registration and validation blocks present.

Handed to the integrator, not absorbed (no sibling file edited): OQ-1 era-label sets;
OQ-2 the storm-cloak naming in 08-symbols; OQ-3 material-set conflicts; OQ-4 mapping
12-rank-rules' records into the gate's `rank_rules:` schema; OQ-6 felt grades G1-G3;
OQ-7 `materials`/`cloth_sources` packet-key overlap with 10-materials and that file's own
RCN-02 registration debt; this component's RCN-02 registration row is supplied in-file
for the integrator to append.

Scope: wrote only this component file and this log line; no commits made.## 2026-10-17 — round 3: component 05-lexicon written (D2 design drill)

Delivered `examples/culture-d2/components/05-lexicon.yml` (827 lines): 40 lexicon
records across the dispatched semantic fields plus the audit's seven-field matrix
(subsistence 7, weather 5, landscape 5, religion 5, kinship 4, trade 4, body 3,
war 3, costume 2, social_order 2 = 40; layers native 34, sacred 3, loan 2,
taboo 1; stages E0 36, E1 3, E2 1).

Contract discovery and adoption (the material event of this component): the
round-3 coupling contract is `examples/culture-d2/components/01-brief.yml` and
the authoritative inventory is `examples/culture-d2/components/02-phonology.yml`.
The first draft was written before either was read; on discovery it was rebuilt
to the contract rather than patched — era tags from the fixed space E0–E3,
`axis:` and `evidence:` on every record, record-level `follows:` citations, id
namespace L-01…L-40, typed `deps:` edges to 02/03/06/09/10/11/12/14 by ID
namespaces (L-, P-, M-, K-, PAN-, ER-, MAT-, GAR-, REC-/SGN-; no prefix invented:
the rank component is referenced by name with ids: [] per RG-04). 13 first-draft
forms were illegal under 02 (coda set {n l r s}, no geminates) and were
re-lexified: im→ir, wem→wen, nem→nen, tok→tol, mik→mil, sak→ban, sir/sirra→
sin/sinra, vel→bel, kat→kas, pert→per, toksa→tolsa; the 02 accent handoff was
discharged by assigning senses to the `sara` pair (sára valley camp locus, sará
ridge camp locus), the only accent-marked forms in the file (RG-07).

Measured evidence (all commands re-runnable):
- `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d2/components/05-lexicon.yml`
  exit 0, no FINDING lines (C, D and L clean); gate `--selftest` exit 0.
- `python3 tools/gates/phonology-sanity-gate.py examples/culture-d2/components/05-lexicon.yml`
  exit 0 (the provisional mirror block is gate-clean).
- Loan adaptation reproduced independently of the gate: L-26 kas < donor gas,
  L-27 per < donor bher, both matching under their layer substitutions, with
  record stage >= layer entry stage.
- Machine checks run at write time: all 40 forms legal under (C)V(C) with coda
  {n l r s}, no clusters or geminates, no segment outside 02's inventory (zero
  violations); D1 overlap scan against worked-example-mini-culture.md §8 gives
  exact collisions 0, distance-1 0, distance-2 38 pairs, no shared sense domain.
- Structural self-check through the gate's own parser: 40 records, no record
  missing a contract field, every neutral axis record carrying its coupling_note,
  the taboo record carrying its recorded sanction.

Declared delta, not hidden: A-04's floors assume >= 60 records (weather >= 10,
landscape >= 10, loan >= 6, sacred >= 4, taboo >= 2, native >= 40, seven fields
>= 4 each); this dispatch specified 40, so body 3 and war 3, weather 5,
landscape 5, native 34, loan 2, sacred 3 and taboo 1 sit below those floors. The
delta is stated in the file's `acceptance_delta` and in this log; expansion is
additive because every record is already contract-complete.

Also read for compliance (not edited): 01-brief.yml contract block and registry,
02-phonology.yml header/inventory lines, worked-example-mini-culture.md §8 for
the required scan. Touched only the assigned component file and this log entry;
no commits made.

## 2026-10-17 — round 3: missing D2 naming, packet assembly and frozen measurements

Evidence motivating the work: `examples/culture-d2/components/13-naming.yml` was
missing while the fourteen sibling components were present; the gate headers and
fixtures require actual shared-schema ledgers, not their component wrappers.
Read all 510 lines of `02-phonology.yml`, the requested source ledgers, and
`corpus/knowledge/linguistics/naming-systems.md` before authoring the names.

Delivered `examples/culture-d2/components/13-naming.yml`: eight etymologized names
(two persons, two clans, two places, two proposed cult addresses), slots and
life-stage licenses, L-32's finite death avoidance with the 06/07 tension flagged,
and three institutionally rejected but phonotactically legal candidates. All
11 strings independently satisfy 02's inventory, (C)V(C), n/l/r/s codas and
no-geminate constraint; all eight accepted concatenations reproduce from recorded
05-lexicon roots. The missing 03 derivation adapter is not concealed with opacity.

Delivered stdlib-only `tools/assemble-d2.py` and its deterministic output
`examples/culture-d2/packet.d2.yml`: 40 lexemes, 27 morphology records, seven agents,
ten symbols, ten costumes, eight names, nine eras, plus eight constructions, two
loan layers, 23 roles, nine motifs, nine costume-facing materials and three cloth
sources. Optional role/motif ledgers come from 06 and 07; owner base ledgers stay
separate from 07's reference views/proposals. Source hashes and extraction limits
are carried in the packet. `python3 tools/assemble-d2.py --check` exits 0.

Actual final runs are frozen byte-exactly under `tools/gates/frozen/round-3/`, with
seven rows in `MANIFEST.tsv`, gate/input/output SHA-256 values, actual exits and
finding-line counts, commands, and byte-copy input snapshots. Results:
- phonology-sanity-gate: exit 1, three A-NEUTRAL reviews;
- lexicon-coverage-audit: exit 0, zero findings;
- myth-consistency-gate: exit 1, one aggregate MC-S00 (ten missing symbol media);
- costume-era-consistency-gate: exit 1, ten G-ERA holds (seven E0, two E1, one E2
  garment tags absent from 09's named-era inventory);
- naming-collision-gate: exit 1, 20 findings: Humweha's illegal /m/ coda, ten English
  garment labels treated as D2 names, eight missing derivation replay adapters,
  and one absent bounded cross-cultural review;
- provenance-audit on mesoamerica-primary-sources.md: exit 0, zero findings,
  39 to-verify marks on 32 lines;
- provenance-audit on gate-frozen-run-standard.md: exit 0, zero findings,
  one to-verify mark on one line.

One assembly-level fix was necessary: 09's optional `era_dates` uses non-CE descent
coordinates and open bounds; copied into the costume gate's numeric CE field it
caused exit 2, G-DATA (expected a number, got None). The merger now preserves that
mapping intact under `source_era_dates`, without inventing a conversion. Every
initial output/input/manifest is retained under `frozen/round-3/attempt-1/`.
No component changed between gate attempts. Final packet SHA-256:
`54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4`.

Verification: both seven-row manifests' gate/input-copy/output hashes match; all
seven final commands reproduce exact exit codes and output bytes; independent
sibling gate readers confirm the selected source ledgers survive extraction and
emission unchanged (including all 40 lexemes and 27 morphology records). Six
relevant gate `--selftest` runs all exit 0, outputs retained under
`frozen/round-3/selftests/`, and fixture hashes are unchanged. No standard package
build exists; the merger and existing executable-gate selftests are the runnable
checks for this deliverable.

`examples/culture-d2/ASSEMBLY.md` records extraction paths, authored names, counts,
ranked findings, the parse fix, and missing reviews. No rank-rule adapter, material
union, era alias arbitration, cross-cultural clearance or canon decision is
claimed. This TSV/output freeze is worktree evidence, not the corpus standard's
committed per-gate expected.json baseline: the operator prohibited commits.
Scope: only this repo; no git commits; no corpus/knowledge files edited. Existing
uncommitted component/corpus/log work was retained; only new naming, merger,
packet, frozen artifacts, ASSEMBLY.md and this append were authored here.

## 2026-10-17 — round 3: D2 end-to-end build + direct triage (ADMITTED)

Claims (declared before dispatch):
1. depth — execute an end-to-end miniature-culture task: build D2 from the
   corpus via swarm, assemble packet.d2.yml, grade with gates, freeze
   outputs. Measured: components 14/15 (swarm) → 15/15 (assembly authored
   13-naming after its writer failed); packet assembled by
   tools/assemble-d2.py; 5 culture-gate runs + 2 provenance runs frozen
   under tools/gates/frozen/round-3/ (MANIFEST.tsv, sha256-pinned);
   findings: phonology 3 REVIEW, lexicon clean, myth 1, costume 10 G-ERA,
   naming 20 (1 real coda violation + noise classes). Task executed and
   logged end-to-end (SHONEN box 2 evidence). VERDICT: improved, verified.
2. freshness — triage the 7 provider-blocked files' flags; orchestrator
   triages the 2 non-civ files directly after 3 filter strikes each.
   Measured: 12 flag-lines examined, 9 resolved (5 CONFIRM, 1 DOWNGRADE,
   3 declared-debt), 3 policy mentions documented; the 5 civ files (39
   flags) carried to round 5 zai lane. VERDICT: improved, verified.
Other axes: operability improved (merger script + frozen-run manifest
pattern); calibration improved (policy-mention counting caveat recorded);
coverage unchanged (2/3 gap-fills landed); adjacency unchanged.
No axis harmed. Round ADMITS.

Dispatch record: round swarm 34 agents on token-plan key 1 — 25 completed,
3 launch failures (13-naming writer, 09 review, africa gap-fill), 6 items
absent from the swarm result; disk inventory used as truth. Assembly moved
to a sol-high subagent after two opencode-go routing failures (lesson).
Deviations recorded: orchestrator-direct triage (goal clause), sol-high
assembly (lane outage).

## 2026-10-17 — README: visitor map (no craft-byte change)

Operator request: give this lane a front-door README. Evidence:

- `ls` of the repo root before this commit had no `README.md` (confirmed
  across the sibling checkout: only kimi-shokunin, the fleet root, and the
  2026-10 public-era remotes already carried one).
- Domain sentences, owns/refuses, and gate commands are restated from
  `PROVINCE.md`, `SKILL.md` (when present), and the cited tool headers.
  No new craft claim is introduced; no scorecard cell is moved.
- Devin wiki URLs were not added. The only verified org wiki link in
  this fleet is the fleet-root line in `VeigaPunk/shokunin` README.md
  (`https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/shokunin?branch=master`);
  GitHub code search `org:VeigaPunk app.devin.ai wiki` returned that file
  and `ufo-fsd-alpha` only.

Not a craft round. No axis claim.
