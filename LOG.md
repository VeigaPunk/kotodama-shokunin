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


## 2026-10-17 — round 4: D2 v1.1 + audits on sol-max (REJECTED as declared)

Dispatch: 32 agents on openai-codex/gpt-6.1-sol; 31 completed, 1 unaccounted
(disk used as truth). Claims and measurements:
1. depth — D2 design findings <= 10 after fixes (from 34). Measured: 24
   (phonology 3 REVIEW honest-remaining, lexicon 0, myth 0 FIXED, costume 0
   FIXED, naming 18). Two finding classes eliminated; naming residual = 10
   PHON-INVENTORY (suspect encoding/segment class, undiagnosed) + 6
   NAME-NEAR + 1 PHON-CODA + 1 CROSS-HOLD (declared gap). Gate integrity
   verified: 7/7 selftests green, fixture bytes unchanged.
   VERDICT: improved in fact; claim falsified as declared.
2. freshness — >=25 gap-entry flags resolved. Measured: 22 (33 -> 11;
   60-row ledger, retained flags carry bases). VERDICT: improved in fact;
   claim falsified as declared (by 3).
3. coverage — africa gap-fill + README regeneration + audit sweep.
   Measured: corpus 178 -> 179 entries; README revision 1.1 (7 partitions);
   17 audit reports, defects named per batch. VERDICT: improved, verified.
Admission: REJECTED (claims 1-2 as declared). No axis harmed. Calibration
lesson (orchestrator-owned target-setting fallacy): round-4 lesson file.

## 2026-10-17 — supplemental OpenCode Go wave: historical corrections

These corrections supersede the numerical and assurance claims named below;
prior entries and commits remain untouched. Baseline for this audit:
`fe34faaafbe0add59ff68827a0df6c5782a72404`.

- Round 4's five committed `.out` files contain **21** finding lines
  (3+0+0+0+18), not 24. `corpus/lessons/round-4-audit/` contains **16**
  Markdown reports, not 17. The depth target of <=10 still failed; this
  correction does not change that round's historical rejection.
- Raw marker-bearing lines by commit are 1258 (`49ac1a5`), 795
  (`291c714`), 587 (`1688790`), 612 (`c610e0a`), 590 (`fe34faa`). These
  are not a monotonic scholarship-resolution curve; new corpus entries and
  policy mentions change the denominator. Counts are lines, not claims or
  occurrences. Reproduce by enumerating `git ls-tree -r --name-only <rev>
  corpus/knowledge`, reading each Markdown blob via `git show`, and
  counting lines containing the exact string `to-verify`.
- Round 4 removed all eight naming `DERIV-HOLD` findings. The old
  `DERIV-REPLAY` residual in lessons/metadata was stale: current component
  03 rules and component 13 complete stems replay already. The ten
  remaining PHON-INVENTORY failures concern English garment descriptions
  with no native forms, not accent marks or segment-encoding evidence.
- Round-3/4 dispatch counts advertised in old prose do not have a committed
  original prompt/result receipt. Do not manufacture absent workers from
  a claimed batch size. This supplement persists its actual 32-item result
  receipt at `reports/supplement-opencode-1/dispatch.json`.
- Five legacy gate selftests regenerate their committed fixtures. A clean
  `git status` or unchanged bytes after deterministic regeneration is NOT
  evidence that no writes occurred. Run those tests in an isolated export.
  Naming/handoff selftests read existing fixtures; all seven still pass.
- A clean myth/costume kernel result does not prove complete role coverage
  or rank-rule enforcement. Missing ledgers leave checks unexercised; see
  supplemental reviews 23 and 24. The handoff checker verifies envelope
  shape, not consent, digest-vs-file truth or canon acceptance. Its current
  run over the legacy YAML produces exit 0 with zero glossary entries;
  the prior pre-freeze YAML exit-1 correction did not reproduce and must
  not be treated as verified. The Markdown contract remains the default.
- The old 0–10 axis estimates lack a reproducible numeric rubric; the
  SCORECARD now labels them historical, records per-axis observations,
  and names numeric calibration as a remaining conformance debt.

Evidence: `reports/supplement-opencode-1/07-historical-corrections.md`,
`06-inventory.md`, `22-label-representation.md`, `25-handoff-boundary.md`,
`29-local-boundaries.md`; re-run commands are retained in those records.

## 2026-10-17 — supplement-opencode-1: source rechecks and runnable evidence (ADMITTED)

Authorization: the operator requested a 32–64-worker native OpenCode Go
DeepSeek v4.1 Flash swarm while non-flash Z.ai GLM-5.3 cooled down. One
32-item AgentSwarm returned 32 completions; the persisted request/result
receipt is `reports/supplement-opencode-1/dispatch.json`. It establishes
requested routing and returned assignments, not observed simultaneous
concurrency or an independent upstream model echo. One existing replay
worker was resumed for path/option-injection hardening; no second batch
was dispatched. This supplement is not numbered round 5 and does not
replace any of the three reserved 16-worker non-flash Z.ai rounds.

Baseline: `fe34faaafbe0add59ff68827a0df6c5782a72404`. The three claims were
declared before dispatch in `reports/supplement-opencode-1/claims.json`:

1. **freshness — improved, verified.** Required >=10 distinct source
   checks and >=5 directly retrieved passages. The 13 assigned ledgers
   contain 148 rows: 118 worker-classified supported, 10 contradicted,
   20 unresolved. The parent independently re-fetched five bounded
   WALS/Frontiers passages; this is not 148 independent confirmations.
   Nine corpus entries carry appended errata with baseline bytes retained.
   Count/schema/hash/append-only checks run in
   `python3 reports/supplement-opencode-1/run-validation.py`; passage
   evidence is `parent-source-spotchecks.json` and the assigned source
   ledgers under `corpus/lessons/supplement-opencode-1/sources/`.
2. **operability — improved, verified.** Assembler selftest absent ->
   42/42 controls; frozen-replay entry point absent -> both seven-row
   round-3 manifests reproduced byte-for-byte, with 79/79 replay controls.
   Digest tampering, traversal and option-like paths are rejected before
   a gate launches. `tools/assemble-d2.py --check` passes. Seven legacy
   gate selftests still pass, run in an isolated export because five
   rewrite fixture files. The bounded craft-example checker passes and
   detects 10/10 planted tamper cases. Exact argv, outputs and tested-file
   hashes are persisted in `reports/supplement-opencode-1/validation.json`.
3. **calibration — improved, verified.** The preceding appended correction
   distinguishes established counts from unresolved dispatch history and
   separates marker counts from scholarship. The read-only inventory
   selftest passes; 179 entries have 592 raw marker-bearing lines versus
   590 at baseline, not a claimed resolution curve. Counting commands are
   in SCORECARD.md and validation.json. No numeric quality score was raised.

Every-axis judgment: depth **improved** as an unclaimed observation
(PAN-03's full `huma + weha` derivation removes one actual coda defect;
the separate non-canon exercise executes nine derivations); coverage
**unchanged** (179 entries, six partitions; missing index row repaired);
operability **improved**; freshness **improved**; calibration **improved**;
adjacency **unchanged** (handoff Markdown still reports 16/16 fields and
20 glossary entries; no lore receipt). No tested axis was harmed. All
three declared claims verify, so this supplemental wave ADMITS under
per-axis judgments, not a scalar score or promotion decision.

Current D2 real calls retain 20 finding lines, versus the corrected
baseline 21: three phonology REVIEWs and 17 naming findings (six era-ID
similarity reviews, ten English-label inventory failures, one cultural
screening hold). Expected red design verdicts are observations, not
failed acceptance assertions or a cleared culture. Myth/costume zeroes
cover only supplied ledgers; role coverage and rank rules remain limited.

Acceptance rerun on the delivered working tree:
`python3 reports/supplement-opencode-1/run-validation.py` exited 0 with
`acceptance_checks_passed: true`; this includes real D2/handoff/craft calls,
all selftests, both frozen replays, source ledger checks and
`git diff --check`. No package/build manifest exists. The assembler packet
was regenerated by the parent, not hand-edited. SKILL.md now records
source-use decisions and actual tool write scopes; PROVINCE.md and the
corpus index cover all six existing partitions. AGENTS.md documents scoped
worker fragments and parent-owned append-only batch logging.

Limits: parser/regex negative controls, missing typed label and rank-rule
adapters, legacy corpus headers, per-gate expected.json layout and an
uncalibrated numeric-axis rubric remain debts, not hidden passes. Reviews
are author-side; no SHONEN box receives independent [x], no rank or canon
changes, no world-bible/sibling/provider-configuration writes. Raw source
downloads and experiment copies remain ignored under this wave's scratch
path; durable records retain URLs, short excerpts, locators and commands.
The lesson is `corpus/lessons/supplement-opencode-1.md`; the final child-local
report will cite the carrying work commit after it exists. Fleet bookkeeping
is outside the operator's write scope, so no fleet closure is claimed.
Four numbered rounds remain recorded; the full requested program is not
complete, and the exact non-flash Z.ai/Grok schedule remains pending.

## 2026-10-17 — README: Devin wiki link

- Operator directive (2026-10-17): insert the Devin wiki link into the README header of every repository with a generated wiki.
- Change: `README.md` created (lane-header convention) with a `**Wiki:**` link to https://app.devin.ai/org/veigapunk/wiki/VeigaPunk/kotodama-shokunin?branch=main.
- Evidence: the org's Devin wiki index lists this repo's generated wiki; sibling lane READMEs carry the same `**Wiki:**` header.
- Documentation-only change; no round run, no axis moved, no verdict changed.

## 2026-10-17 — supplement-opencode-1: remote integration

The supplemental work landed in `c53782ab875e88d7311c8b9b1db310357b944685`.
Meanwhile origin/main advanced from the pinned baseline to
`848417c2d366cae2eb07e48fba53f19cafcb6388`, carrying the README/wiki change
from `dee3089`. A normal merge preserves the remote README byte-for-byte
and both branches' LOG additions. The wiki entry above is preserved from
the remote append; its placement here reflects merge integration, not a
new training round. No force-push, rebase or history rewrite was used.
The acceptance runner will be rerun on the merged deliverable; the
child-local report will cite its committed work revision and outcome.

## 2026-10-17 — supplement-opencode-1: merged-tree check and registry correction

The merged tree at `f7c0ac6a6fa47aa12decc6b0f4eca596c2fd7724` passed
`python3 reports/supplement-opencode-1/run-validation.py` before the merge
commit, including all real domain calls and the isolated test battery.
Preservation assertions confirmed the prior work LOG is an exact prefix,
the remote's seven-line append is retained, and README.md is byte-identical
to `848417c2d366cae2eb07e48fba53f19cafcb6388:README.md`.

Final registry inspection found two documentation omissions: the assembler's
`--check` mode returns a drift verdict and therefore is a gate, not a probe;
the bounded craft-example checker also needed a registry row. SKILL.md now
records both actual interfaces. The craft checker's optional `--report`
reads an existing report; it does not generate one. Its selftest tests ten
mutations of the committed example, so the positive CLI run is separately
required. File/JSON/CLI errors are not yet normalized into a distinct
could-not-evaluate exit; this remains an explicit interface defect, not
claimed hardening. These are integration corrections, not a fourth claim
or another numbered training round. The final report is filed only after
this correction and its refreshed validation receipt are committed.

## 2026-10-17 — operator ordering amendment: Grok after DeepSeek

Operator request: "do a round with the 128 swarm using the grok 4.7xhigh
fast also, after the deepseek rounds". This latest ordering supersedes the
older stored goal draft's Grok-at-round-8 sequence. Preserve the requested
model/count totals and only reorder the undispatched numbered rounds:
5–7 are three non-flash Z.ai GLM-5.3 rounds of 16 workers each; 8–9 are the
two remaining Alibaba token-plan DeepSeek v4.1 Flash rounds of 32–64 workers
each; 10 is the single 128-worker Grok 4.7 xhigh fast round AFTER DeepSeek.
SCORECARD.md's planned queue now carries this order. No pending round has
been dispatched or counted complete by this amendment, and no provider
configuration was changed. Exact native routing must be demonstrated; a
substitute model must never be reported as the requested one. The host's
Grok substrate CLI remains the authorized fallback dispatch path if native
AgentSwarm cannot route that exact model.

The additional OpenCode Go wave is already published at
`82eafdf5df793c8d1f6e9e230a7be385535bec27`; `git ls-remote origin
refs/heads/main` matched local HEAD and tracked `git status --porcelain=v1`
was empty. Its final lane report is
`reports/supplement-opencode-1/kotodama.md`. A clean staged-deliverable export
also passed the entire acceptance runner without ignored source downloads
or experiment trees. This is supplemental closure, not completion of the
ten-round training goal or retrospective repair of old dispatch evidence.

## 2026-10-17 — round 5 preparation attempt 1: native alias rejected before launch

Baseline: `c52f2c07abcfae4d363e6057e3bc7f60b1329efc`. Re-read the lane
SCORECARD/LOG, fleet protocol/appendix/mission/axes/corpus contract and local
quality bar. Declared two causally separable measurable claims before the
attempt in `reports/round-5/claims.json`: freshness (historically lowest;
follow up >=10 unresolved rows with >=3 directly retrieved passages and
parent re-fetches), and operability (standalone isolated seven-gate battery
plus six craft-input errors normalized to exit 2). Numeric-rubric debt is
not replaced by an invented score. The prepared 16 distinct assignments
are ten disjoint two-row source follow-ups, two executors and four bounded
planner/connector/review/critic fragments; template and exact assignment
text are persisted under `reports/round-5/`.

Actual before-probes on tools/check-craft-exercise.py reproduced exit 1
with a traceback for all six cases: missing argument, missing file,
malformed JSON, non-UTF-8, list instead of object root and missing --report
value. The current --selftest still reports exit 0, 10/10 mutations detected.
No standalone tools/check-gate-battery.py exists. These are baseline defects,
not changes landed or targets satisfied by this attempt.

ONE native AgentSwarm call requested 16 workers using explicit model
`zai-coding-plan/glm-5.3` and its matching non-flash profile. It returned
`Invalid model "zai-coding-plan/glm-5.3"` before launching any worker. The
available-model list contains only the Flash-low Z.ai alias; the exact
refusal, timestamp and prepared-file SHA256 values are retained in
`reports/round-5/availability-attempt-1.json`. This is a host registry
rejection, not an observed provider 429, upstream failure or proof that
GLM-5.3 itself does not work. No alternate alias, implicit default, custom
client, provider/configuration edit or manual executor replacement was used.

Requested -> launched -> completed: **16 -> 0 -> 0**. Reproduce the receipt
count with `python3 -c 'import json; d=json.load(open("reports/round-5/availability-attempt-1.json")); print(d["requested_workers"],d["launched_workers"],d["completed_workers"])'`.
No source ledger, corpus erratum, gate, exercise or packet was changed.
Claims F/O remain pending; no after-verification or admission is claimed.
All six axis verdicts: depth unchanged; coverage unchanged; operability
unchanged; freshness unchanged; calibration unchanged; adjacency unchanged.
This preparation/refusal does NOT count as a dispatched or completed craft
round, and does not advance the four numbered rounds already recorded.

The lesson is `corpus/lessons/round-5-availability.md`; the child-local
availability report is filed after this preparation work is committed.
Round 5 stays pending until the exact native non-flash route is exposed.
This is the first consecutive post-supplement goal turn encountering this
registry blocker; the overall goal is not yet marked blocked. The Z.ai,
DeepSeek and Grok-after-DeepSeek pending sequence remains unchanged.

## 2026-10-17 — operator route amendments: Z.ai Flash and OpenCode DeepSeek

Latest requests: "use the flash zai glm 5.3 flash then" and "also, use the
opencode provider for the deepseek swarm". These explicitly supersede the
older non-flash Z.ai and Alibaba token-plan requirements; they do not change
worker counts or verification targets. Pending rounds 5–7 now use Z.ai
GLM-5.3 Flash, 16 workers each; 8–9 use OpenCode Go DeepSeek v4.1 Flash,
32–64 workers each; 10 remains the 128-worker Grok 4.7 xhigh fast round
AFTER DeepSeek. No provider configuration or credential edits are needed.

The host exposes Z.ai Flash as `zai-coding-plan/glm-5.3-flash-low`; its tool
documentation pins this legacy alias to MAX thinking. The available native
alias is requested explicitly, not an implicit reroute or a claim of an
independent upstream model echo. `reports/round-5/flash-authorization.json`
records both directives; `flash-claims.json` keeps the exact F/O thresholds,
no-harm constraints and 16 disjoint ownership assignments. Before-dispatch
baseline is `1ccb2b7119039d8026ad1d004f20427623838b94`; domain and tool bytes
are unchanged from the earlier measured baseline. Historical non-flash
refusal records stay intact. The authorized Flash attempt is recorded
separately and must not erase or relabel that pre-launch rejection.

## 2026-10-17 — round 5: scoped source follow-up and executable verification — admitted

Baseline: `1ccb2b7119039d8026ad1d004f20427623838b94`. Two measurable claims,
F/freshness (historically lowest non-retired axis) and O/operability, were
declared before the authorized dispatch in `reports/round-5/flash-claims.json`.
The thresholds and no-harm constraints were not relaxed after execution.
The uncalibrated numeric-rubric debt remains explicit; no new scalar score
or exploratory taste claim substitutes for the measurements.

### Actual dispatch and continuity

One executed native AgentSwarm batch requested explicit alias
`zai-coding-plan/glm-5.3-flash-low` with matching profile
`sec-fast-zai-flash-low`: 16 distinct assignments, 16 returned completions,
zero failed workers. The legacy alias name is documented by the host as
MAX thinking; upstream wire-model identity and simultaneous runtime
concurrency were not independently instrumented. Tool call
`call_c0fbf2a3ee764fb681da8d89ff0271aa` reported 1789.607 seconds. Saved
request binding, exact template and assignments resolve under
`reports/round-5/`; canonical argument SHA256 is
`119036a731d817d8df1a7e27c1933790d83a0fa7ea126e0632cf5ae33694b69b`.

This followed the separately preserved zero-launch non-flash refusal, so
there were two native request attempts, not one tool attempt. Only one
actual batch ran after explicit authorization. Nine continuity requests
retained the same identities for four source-schema cleanups, two executor
repairs and three bounded reviews; they are not additional workers or
completed swarms. `dispatch.json` lists identities agent-456 through
agent-471 and continuation scopes. No worker committed or made canon.
Count with `python3 -c 'import json; d=json.load(open("reports/round-5/dispatch.json")); print(d["workers"],d["completed"],d["actual_executed_batches_after_authorization"],len(d["existing_worker_continuations_requested"]))'`
→ **16, 16, 1, 9**. The native binding is author-observed host evidence,
not cryptographic third-party attestation or an independently echoed wire ID.

### Claim F — freshness

Before: 20 unresolved supplemental original questions and no round-5
follow-up ledgers. Target: at least ten original questions rechecked,
three newly retrieved directly relevant passages and three parent
re-fetches, with no catalogue-as-content or partial-claim laundering.
After: **22 raw audit rows, 20 distinct original questions, 17 retrieved
rows and five parent checks**. Re-run `python3 reports/round-5/run-validation.py`;
its F measurement is true and retains exact row evidence. Companion
KIN rows do not inflate the original-question denominator.

The raw worker classifications are 13 supported / eight unresolved / one
contradicted; these are NOT 13 confirmed original cultural claims. Parent
reconciliation (`parent-reconciliation.json`) is **five scoped supported /
15 unresolved / zero whole-claim contradicted**. Supported IDs are TURK-07,
meso-13, meso-14, PHON-A11 and SR-REG-07, each limited to its actual witness,
abstract, metadata or quoted expressive-scope passage. Earlier-thesis versus
later-book, compound catalogue claims, relative-register counts, numerical
kin borrowing and exact oral-epic attribution retain residual uncertainty.

Parent source checks (`parent-source-spotchecks.json`) cover the Solís
publisher-deposited abstract (bark support/pretreatment dates, not painting
dates), Blasi venue metadata (not causal endorsement), Lowie Chapter V
(kin terminology is not a deterministic social-rule map), Haviland quoting
Dixon (expressive replacement is not one-to-one synonymy), and the opening
Zhoushu 50 witness (bounded unnamed she-wolf evidence, not global absence).
Four checks concern non-bibliographic content; the three-passage threshold
does not rely on counting metadata as prose. Public-response curl/PDF
extraction was source research, not a custom provider/model API client.
Full downloaded responses stay ignored rather than being redistributed.

The sole knowledge-entry change is an appended bibliographic erratum to
`corpus/knowledge/linguistics/phonetics-phonology.md`: Science 366 is
superseded by **363(6432):eaav3218**, DOI 10.1126/science.aav3218. It does
not endorse the contested diet/bite-configuration causal argument. Original
entry bytes and historical uncertainty markers remain intact. SKILL.md now
turns these source distinctions into bounded worldbuilding decision rows;
`corpus/README.md` names the residual frontier. Claim F verifies.

### Claim O — operability

Before: the supplemental parent runner could already isolate seven legacy
selftests, but no standalone battery entry point existed. All six declared
malformed craft controls exited 1 with tracebacks, while ten domain
mutations were detected. After:

- `python3 tools/check-gate-battery.py` actually runs all **seven of seven**
  legacy selftests in a disposable copy, exit 0; hashes and original path
  membership are unchanged. The wrapper does not edit legacy gate code.
- `python3 tools/check-gate-battery.py --selftest` passes **10/10** stable
  controls. A recognized stable failure maps to exit 1; crash, timeout,
  missing gate, abnormal exit or tree drift maps to exit 2. A traceback
  veto prevents an earlier FAIL line from hiding a later Python crash.
- All **six of six** original malformed craft cases now exit 2 without
  traceback, with CRAFT-CLI-USAGE / NOT-FOUND / JSON / UTF8 / SHAPE /
  REPORT-VALUE diagnostics. Reviewed nested-shape and ambiguous-argument
  cases are also guarded; no arbitrary-schema completeness is claimed.
- `python3 tools/check-craft-exercise.py --selftest` passes **10/10 domain
  mutations plus 18/18 real CLI subprocess controls**. Positive example,
  existing-report read, declared counts, foreign cwd and actual domain
  finding/exit 1 are separately exercised in `validation.json`.
- Both `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`
  and the `round-3/attempt-1/MANIFEST.tsv` replay reproduce **7/7** recorded
  rows. Expected red remains red. The previous supplemental acceptance
  runner passes again in an isolated input copy, without overwriting its
  historical receipt in this tree.

`python3 reports/round-5/run-validation.py` exits **0**, F=true, O=true,
acceptance_checks_passed=true, errors={}. It records tested code SHA256:
craft `b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5`;
battery `077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67`.
No historical gate, frozen fixture, toy law, exercise or D2 packet changed.
Claim O verifies.

### Review, rejection evidence and limits

The first combined parent run failed honestly on worker-12's lingering
entry_path/entry schema mismatch and a parent probe that removed a
nonexistent root negative-control field instead of D1's actual nested
control. Those coordinates were fixed, not the required exit or threshold.
Review then exposed crash/failure confusion, nested-shape crashes, undetected
fixture additions, invalid timeouts and ambiguous arguments. Existing
executors repaired their assigned files. An intermediate recursive-selftest
mistake was caught and repaired, not accepted. The final bounded review in
`15-cli-review.md` confirms the named counterexamples are fixed; it does
not independently certify promotion or all possible malformed inputs.
`integration-attempts.json` preserves the sequence.

Parent added the final traceback veto and one real mutation check:
`battery-mutation.json` records veto removal in a scratch copy rejected by
CTRL-MARKER-THEN-CRASH (mutant selftest exit 1), while the original remains
exit 0 / 10 of 10 with unchanged bytes. This is one invariant challenged
by one plausible defect, not universal mutation coverage.

The wrapper is not an OS sandbox; original-byte equality is not proof of
no writes, and child exit 0 is trusted. Five old assert-based selftests can
report genuine failures as could-not-evaluate/2, conservatively non-green.
Legacy fixture rewrites, parser/regex issues, independent-expected-value
and expected.json layout debts remain. Craft LAW-ORDER early-return and
declared audit-count metadata limitations remain; the frozen example's
historical scratch counting_command was not silently rewritten.

Reviewer observed 428 historical /tmp craft-selftest directories (~24 MB)
from intermediate repairs, unchanged by final-byte runs. They were left
outside this child-only cleanup scope; the parent's PID-only process check
observed no matching live selftest process. Worker 12 reported creating
then cleaning stray session-root temporary files. No such files are shipped,
but no independently proven claim of zero outside writes ever is made.
These scope deviations are recorded, not hidden by a clean Git status.

### Every-axis verdict and decision

- **Freshness improved** (F): 0 → 20 original-question follow-ups, with
  retrieved evidence and conservative unresolved residuals retained.
- **Operability improved** (O): standalone seven-gate battery and typed
  malformed-input diagnostics pass the declared actual-call checks.
- **Calibration improved** (unclaimed observation): 22 raw rows versus
  20 original IDs, worker labels versus parent whole-claim dispositions,
  source-version bounds and intermediate failures are reconciled explicitly.
- **Depth unchanged**: source-use rules clarified, same nine-derivation
  non-canon exercise and same D2 packet; no new culture task is claimed.
- **Coverage unchanged**: 179 entries, six partitions, totals
  16/16/16/24/13/94; civilization partition is 92 bases + two source maps.
- **Adjacency unchanged**: sample handoff remains 16 fields / 20 glossary
  entries, exit 0; no lore receipt, cultural permission or canon decision.

Inventory command: `python3 tools/source-audit-inventory.py --json --summary
--root corpus/knowledge`; current raw marker-bearing lines remain 592,
raw occurrences 598 (600 case-insensitive; 568 parenthesized marks).
The corpus is not made fresher by erasing markers. D2 still has **20**
findings: three phonology REVIEWs plus 17 naming findings (six era-ID
similarity, ten translated English labels, one cultural-screening hold).
A green supplied subset is not whole-culture clearance.

**Admit round 5:** both measurable claims verify and no tested axis is
harmed. No untested-behavior, numeric-score, rank, canon or shared-fleet
closure claim follows. `corpus/lessons/round-5.md` records candidates,
admission, rejections and limits. Publication must validate the staged
clean export before the work commit; the final child-local report
`reports/round-5/kotodama.md` is filed only after that commit and names the
actual carrying hash. Historical reports and prior round rejections stay
intact; extra metadata/report commits are not new training rounds.

Pending sequence remains **6–7: Z.ai Flash, 16 each → 8–9: OpenCode Go
DeepSeek v4.1 Flash, 32–64 each → 10: exact Grok 4.7 xhigh fast, 128**, after
DeepSeek. Round-4's 31-return/missing-original-request provenance debt is
not repaired by this round. Five numbered records are not completion of
the ten-round program, and no fleet roster/ledger or sibling was edited.

## 2026-10-17 — round 6 declaration: early-reference source checks, Flash MAX

Latest operator confirmation: "glm 5.3 flash max". Use Z.ai's native
`zai-coding-plan/glm-5.3-flash-low` / `sec-fast-zai-flash-low`; the legacy
suffix is host-documented at MAX thinking, not a request for low effort.
No configuration change, non-flash relabelling or implicit provider/model
substitution is authorized or needed. The provider/ordering amendments
above remain: round 7 also Flash MAX/16, then OpenCode Go DeepSeek rounds
8–9/32–64, then exact Grok 4.7 xhigh fast round 10/128 after DeepSeek.

Baseline is published `030c3928de74ed514853bc1f7490e0f8bb4d451f`.
Re-read SCORECARD/LOG, fleet protocol/appendix/mission/axes/corpus and the
child quality/operating rules. `reports/round-6/baseline.json` records the
actual SHA256 values of twelve existing early-reference entries and zero
round-6 source ledgers before dispatch. The fixed two questions per entry
are in `targets.json`; they are questions, not presumed historical truths.
This checks new earlier-reference surfaces rather than spending another
wave retrying the same fifteen unresolved round-5 residuals.

Declare ONE measurable claim, **F/freshness**, historically the lowest
non-retired axis. Before: zero round-6 audits. Required after: exactly 24
named question rows across all twelve assigned entries; at least six
distinct newly retrieved directly relevant non-bibliographic passages
across at least four entries; at least three parent non-metadata passage
re-fetches. Count by `python3 reports/round-6/run-validation.py` once the
actual deliverable exists, never by raw supported-label totals. Duplicate
passages, title/TOC/metadata and an unread primary behind a secondary quote
do not meet the direct-content threshold. The declared schema preserves
actual entry locator, original bytes/hash, source type/version, short
excerpt or access failure, scoped verdict, design implication and limits.

Prepared dispatch: exactly one 16-item native AgentSwarm request through
the explicit Flash MAX profile, with one planner/connector, twelve disjoint
source executor/scout/scribe assignments, two source reviewers and one
calibration critic. `dispatch-plan.json` and `prompt-template.txt` retain
exact assignments and operative contract. Reviewers must not predict
passes for absent concurrent output; existing identities may continue on
actual output afterward, not become another swarm. Parent owns shared
integration and publication; no worker commits, delegates, changes gates
or examples, or writes canon/siblings/fleet/configuration/credentials.
Research scratch stays in assigned ignored child subtrees, not /tmp or
session-root artifacts. Historical evidence stays historical; corpus errata
append only if real retrieved evidence warrants them. No new round credit
or admission is claimed by this declaration alone. All six axes are judged
only after actual results and unchanged prior acceptance are measured.

## 2026-10-17 — round 6 development checkpoint before session handoff — not admitted

Operator request: "contnue, push to remote all the developments, ill be
starting a new session". Preserve the actual completed work without
calling unfinished acceptance a pass. The model/provider interruptions
affected the main-session continuation, not the already completed native
source batch. No new swarm is launched to replace or duplicate that work.

Actual dispatch from baseline `030c3928de74ed514853bc1f7490e0f8bb4d451f`:
ONE AgentSwarm, call `call_ca9de43bcc5844c08d4c2a33da728ba0`, explicit
Z.ai alias `zai-coding-plan/glm-5.3-flash-low` and profile
`sec-fast-zai-flash-low` (legacy name, host-documented MAX thinking),
16 distinct assignments, 16 completions, zero failed workers, native
reported runtime 1224.021 seconds. Assignment IDs agent-472 through
agent-487, template and question targets are retained under
`reports/round-6/`. Parent checked the host request against the saved
arguments; canonical SHA256 is
`47ea1a29da86628aa320632541a0a4d25d6347dc2ea5d68eb8b2de8275769906`.
`native-request-binding.json` records the observed event digest and limits;
no upstream wire-model echo or simultaneous concurrency is claimed.

Three existing identities (reviewers 14/15 and critic 16) continued on
actual completed fragments, all returned, and appended to their own
reports. These are not replacement workers or additional swarms. Initial
absent-at-review-time findings remain in those reports as scheduling
history; their later actual-output reviews are separately appended.
There are no running child tasks from this wave at checkpoint preparation.

The twelve source ledgers contain **24 fixed question rows**, all worker
labelled supported: 18 whole-bounded-claim / six partial. Mechanical keys
are distinct, and excluding tertiary/catalogue/unavailable mains leaves
**20 candidates across eleven entries**. These are provisional source
readings, NOT 24 parent-confirmed whole historical facts. Actual-output
reviews identify whole-to-partial candidates 04-A, 05-A, 06-A, 08-A, 08-B,
09-A and 10-A; source-kind mediator corrections and 13-A's wildcard archive
capture still need integration. The full queue is in `checkpoint.json`.
The fifteen older round-5 residual questions remain residual.

`python3 reports/round-6/check-checkpoint.py` exits **0** with
checkpoint_checks_passed=true, round6_admission=pending. It verifies all
24 exact IDs/questions, declared schema/enums/URL/excerpt shapes, twelve
baseline entry hashes, request reconstruction, source-fragment coverage,
append-only LOG prefix and **468 unchanged historical files**. It reruns
round-5 acceptance only in a disposable child-scratch copy, where F/O and
all previous acceptance assertions pass. The original round-5 validation
receipt is not overwritten. Tested craft/battery digests still match
`b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5`
and `077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67`.

This checkpoint checker is an integration/preservation check, NOT the
originally declared F admission instrument. Parent has not yet persisted
three non-metadata source re-fetch receipts or a conservative whole-claim
reconciliation, and `reports/round-6/run-validation.py` is not implemented.
One native Wisdomlib re-fetch returned the full cited chapter before the
interruption, but no durable parent receipt was filed; the two PDF native
fetches did not extract and are not completed checks. No original F
threshold is relaxed. **Round 6 remains unadmitted; all final round-6
axis verdicts are pending.** The last admitted six-axis table stays round 5.
No new end-to-end culture task, capability, rank, lore receipt or canon is
claimed; D2's twenty findings and legacy conformance debts remain.

Worker 09 and worker 11 reported temporary fleet-root writes followed by
cleanup, despite the scoped prompt. They are not in the deliverable; zero
outside writes ever is not independently established. Raw downloaded works,
PDFs and duplicate experiment trees remain ignored rather than being
redistributed. No sibling, fleet roster/ledger, world bible, credential or
provider-configuration changes are committed by this checkpoint.

The separate empty-assistant provider-400 bug was investigated in the CLI
checkout, but no source/configuration/binary patch was made; that checkout
remains clean. The operator's main-model preference is Kimi K2.8 Preview,
selectable via /model; no successful model switch is asserted by this lane.
The checkpoint cannot be represented as a fix for the provider error.

`corpus/lessons/round-6.md` preserves the Gate's pending state and the
source-to-system lessons. Work must be committed before filing
`reports/round-6/kotodama.md`; that child-local checkpoint report cites the
actual carrying hash, includes SHONEN author assertions and names every
unfinished acceptance step. Its existence is NOT a passed-round or fleet
closure signal. On a new session, resume existing round-6 evidence first,
then round 7 Flash MAX/16, rounds 8–9 OpenCode Go DeepSeek Flash/32–64,
and finally round 10 exact Grok 4.7 xhigh fast/128 AFTER DeepSeek. Extra
checkpoint/report commits do not satisfy the ten-round completion count.

## 2026-10-17 — round 6 final integration: bounded freshness admitted

This entry supersedes only the pending acceptance state of the earlier
round-6 checkpoint; its bytes, worker ledgers and reviews remain historical.
Baseline stays `030c3928de74ed514853bc1f7490e0f8bb4d451f`; raw evidence is pinned
at checkpoint `104aa54c737d79c5df1382f65d578b61cbf831f2`. There was **no second
round-6 swarm**. The one actual Z.ai Flash MAX batch returned sixteen
workers plus three same-identity review continuations, as already recorded.

The parent now records five actual successful non-bibliographic re-fetches
in `reports/round-6/parent-source-spotchecks.json`: Śatapatha III.2.1,
Louvre E 12026 technical fields, Gobhila II.8, UT Hittite Lesson 2 and
Stolper/Tavernier ARTA 2007.001. Four native page checks were repeated during
integration; the downloaded ARTA PDF and page boundaries were inspected,
with size 1,242,395 and SHA256
`c7664821696a92d968b8000bdd9ae0b61020680023f3eb29e7bb7d59f79a59f8`.
Its quotation is on PDF/printed **page 9**, correcting the worker locator
separately. The Gobhila archive wildcard resolves to exact capture
`20231003011254`; the parent reads its three timing options and explicit
translator emendation. Failed/oversized/404 retrievals are separately
retained and never count as successful checks.

`parent-reconciliation.json` preserves all 24 raw supported labels and
18-whole/six-partial worker scopes, then applies the strict main-source rule:
**nine scoped-support / eleven partial-support / four unresolved**. The four
tertiary mains R6-02-A, 02-B, 05-B and 07-A are not inspected originals and
do not enter the threshold. Partial assertions can carry substantive
passages without resolving every conjunct. UT teaching text and BMCR
review are normalized to secondary-scholarly; the Science Advances main
kind remains peer-reviewed. Wikipedia-embedded classical quotes remain
tertiary-mediated, and Taube's deposited abstract prose is not surrounding
metadata or unseen full-article content. All readings/reviews remain
author-side; five parent checks are not twenty independent confirmations.

The originally declared command, `python3 reports/round-6/run-validation.py`,
is now implemented and its first actual run exits **0**. Claim **F verifies**:
zero pre-round source rows/checks → **24 fixed questions across twelve
entries; twenty distinct eligible main passages across eleven entries;
five distinct parent URLs/checks across four entries**. The unchanged
minimums are 24 rows, six distinct relevant passages across four entries,
and three parent non-bibliographic re-fetches. Exactly twenty distinct main
URLs contribute; optional corroborations never inflate this count. The
receipt carries all normalized URL/locator/excerpt keys and nine passing
in-memory negative controls. Source relevance is a recorded reading judgment,
not a machine certification of historical truth.

The runner preserves **497 checkpoint files byte-identically**, six named
append-only prefixes, and two explicitly editable bookkeeping files. All
twelve baseline entry hashes still bind the original bytes; only Vedic and
Persian entries gain appended errata. The first clarifies 10 nights / 100
nights / one year instead of arbitrary later timing; the second updates the
ARTA access status and locator without universalizing Old Persian use.
SKILL gains five bounded source-to-system constraints; corpus/README names
the remaining frontier. Original source/gate/example/report bytes are not
rewritten to manufacture a pass, and no raw downloads are published.

Prior round-5 acceptance passes in a disposable child-scratch copy, not by
overwriting its original receipt. It replays both round-3 manifests at 7/7,
runs seven legacy gate selftests through the isolated battery, keeps craft
10/10 domain and 18/18 CLI controls green, and preserves **twenty expected
D2 findings**. The same craft and battery SHA256 pins remain
`b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5`
and `077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67`.
The historical checkpoint checker is not altered; its exact-byte-equality
contract applies to its checkpoint tree, not these legitimate appended
knowledge errata. Final clean-export checks follow before publication.

Every axis, no scalars:
- **Freshness improved (declared F):** the fixed passage/refetch threshold
  passes by the original counting command above and `validation.json`.
- **Calibration improved (unclaimed):** conservative 9/11/4 dispositions,
  accurate mediators, archive pin and page-9 correction replace whole-label
  inflation without changing raw evidence. Same command and reconciliation.
- **Depth unchanged:** five bounded decision rows, but the same executable
  culture tasks; no new end-to-end miniature-culture success claimed.
- **Coverage unchanged:** inventory command in SCORECARD still returns 179
  entries in six partitions (16/16/16/24/13/94), not universal earlier-history
  coverage. Marker inventory stays 592 raw lines / 598 raw occurrences,
  600 case-insensitive and 568 parenthesized occurrences.
- **Operability unchanged:** round-local acceptance/count controls are not
  a new general scholarship gate; old domain executables and examples stay
  identical and prior acceptance passes in isolation.
- **Adjacency unchanged:** no lore receipt, world-bible/canon decision,
  permission or promotion; same handoff checks and province boundary.

Author-side admission: **F verifies and no tested axis is harmed**. The
fifteen round-5 residuals remain unresolved; these twelve earlier-reference
entries are different work, and this round still has eleven partial and
four unresolved questions. Worker outside-write deviations and the separate
unfixed CLI/provider-400 investigation remain disclosed in the checkpoint;
no scope history or model-switch success is retrospectively fabricated.
Commit final integration first under the lane identity, append the final
outcome to the filed checkpoint report citing that real work HEAD, commit
the report last, then push and verify remote equality. Rounds 7–10 remain
pending; extra checkpoint/integration/report commits are not extra rounds.

### Round 6 final instrument review and historical replay

The existing critic identity `agent-487` performed a further read-only
continuation on the final counting instrument and parent receipts. This
is a fourth review continuation after the three in the frozen checkpoint
`dispatch.json`, not another batch or a replacement worker. It reproduced
24/12, 20/11, five parent URLs/four entries, 9/11/4 dispositions, nine
negative controls, 497/6/2 preservation and the request digest in memory,
without rewriting validation.json, and returned **no blocking findings**.
Its nonblocking notes and review limits are preserved in `outcome.json`.
The instrument's reviewed SHA256 is
`c53f100927b8723bea25eeaa06048ace68fdfa3e763811a64e1104323e535c6e`;
commit and report must bind these actual bytes rather than trusting a
self-written hash alone.

Separately, a clean `git archive` export of checkpoint
`104aa54c737d79c5df1382f65d578b61cbf831f2` reran the unmodified historical
`check-checkpoint.py` to exit 0: 468 historical files unchanged and
round6_admission=pending, exactly its original contract. The current
historical receipt was untouched. That reproducible pending state and
the later final F pass are different snapshots, not contradictory labels.

## 2026-10-17 — round 7 declaration: source-bounded culture assembly

Baseline `30caac66a2a382f1c46ba31f0c3c93da62d0762c`; round 6 is already
committed, reported, pushed and remote-equal. Re-read SCORECARD/LOG,
PROTOCOL, MISSION, AXES, CORPUS, QUALITY and PROVINCE before this declaration.
The latest operator amendment requests the final **one sixteen-worker Z.ai
GLM-5.3 Flash MAX batch**, native legacy alias
`zai-coding-plan/glm-5.3-flash-low` / `sec-fast-zai-flash-low`; MAX is the
host-documented pin, not inferred from the old suffix. No route/config edits
or silent substitution. Native request and returned identities will be
recorded separately; no execution success is asserted before dispatch.

Two measurable, causally separable claims in `reports/round-7/claims.json`:
- **F / freshness**, historically lowest non-retired: zero new rule-drift
  records → exactly five fixed source checks, at least three distinct
  substantive main passages across three reference entries, plus two parent
  re-fetches. These recheck current source-derived constraints; they are not
  five new discoveries or closure of older residual questions. Counting
  command: `python3 reports/round-7/run-validation.py`.
- **O / operability, capability acquisition:** zero D3 profile/tool/component
  artifacts → deterministic NON-CANON miniature-culture assembly and a
  read-only evidence/coupling guard, actually exercised through CLI. Minimum
  two eras, twenty constructed lexemes, six replayable names, two attributed
  myth variants, four costume/scene cases, five limited source bridges,
  twelve stable domain-negative controls and four malformed controls.
  Positive exit 0, contradictions exit 1, malformed inputs exit 2; isolated
  selftest, frozen-input tamper rejection, no input writes or tracebacks.
  Same acceptance command; assembler --check and guard --selftest also run.

F reads live sources independently of O. O uses already committed round-6
reference evidence independently of new live-source access. The exact schema,
fixed interface anchors and diagnostic vocabulary are declared before
execution in `reports/round-7/d3-contract.json`; fixed source questions and
baseline counts/hashes are in `targets.json` and `baseline.json`. The
pre-declaration Python count observed zero round-7 source ledgers, zero D3
component files and zero new tools. Old culture exercises do exist; this
is a new bounded profile, not a false absence claim about the whole lane.

One batch has disjoint scopes: planner/connector, checker, assembler, four
component writers, five source scouts/scribes, independent control author,
handoff scribe, reviewer and critic. Workers never commit, delegate or
write outside their assigned child paths. Existing identities can continue
for actual-output review; no replacement/second swarm. Parent owns shared
bookkeeping, evidence reconciliation, acceptance, work commit, report-last
commit and normal push. The operative prompt contract and saved dispatch
payload precede launch. Same-model roles follow the explicit operator
amendment, not a claim that generic fleet buckets were used.

D3 keeps translated labels separate from native forms, written/read/avoided
forms separate by context, reference passages separate from invented rules,
and ground surfaces separate from worn attachments. Fictional timing
numbers deliberately differ from Gobhila; no sacred rite is reconstructed.
Expected legacy CROSS-HOLD or declared costume violation must remain visible,
not be erased to claim clearance. No lore receipt, world-bible edit,
cultural permission, promotion or universal historical coverage.

All historical source/report/lesson/knowledge/gate/example bytes stay frozen;
LOG/SKILL append only and SCORECARD/README may update. Re-run round-6
acceptance on delivered old surfaces in an isolated export/private baseline
index because its round-local whitelist excludes later-round artifacts.
Never rewrite its runner or receipt. D2's twenty findings and every older
residual remain. Measure on the actual clean staged deliverable, judge all
six axes, and admit only if F/O verify with none harmed. Rounds 8–10 remain
later work: two OpenCode Go DeepSeek Flash waves, then exact Grok/128.

### Round 7 integration checkpoint — actual returns and corrected defects

Trigger: the sole native batch `call_7330cf50cf424608b67e9a9cabf4df7c`
returned16/16 in1544.207 tool-reported seconds. Parent read the actual
outputs and retained initial reviews that correctly reported then-absent
files. `reports/round-7/dispatch.json` maps assignments01–16 to agent488–503;
continuations use those identities and are not replacement swarms. Source
ledgers08–12, four components, two new tools, independent controls and D3
outputs are present; completed workers alone do not verify the claims.

Action/evidence: parent persisted two actual native FetchURL readings (UT
and Louvre), all-five conservative reconciliation, native request binding
and integration defects in round7 reports. Main excerpt whitespace counts
are20/35/27/35/36; five distinct keys span four existing entries; scopes
remain three scoped/two partial. Critic agent503 independently rederived
these counts and both canonical request digests, without repeating network
research or claiming parent checks for allfive. No older residual closed.

Prompt fidelity: host event's SHA256 including LF is
`c7e225cdf955f47082381d63709e187bd2fb872d8b0a35031c6f8e4fb0459401`.
Saved canonical args hash `4733dffea5b06ee953326d73e35949aa6578695e476f3dee4385b2945b02451c`
and actual `9f46d717352a1c8f7f428bbf4c7af48733676b287a6a16253a6e8ffe68e1676f`
differ by exactly one documented capability-clause paraphrase. Parent
rechecked this against the original event after compaction. The quoted
contract was not byte-verbatim: semantic retention does not repair that
conformance defect. Pre-dispatch intent is preserved, not rewritten to fit.
No upstream wire identity or simultaneous concurrency is independently
instrumented; the legacy Flash-low alias is host-documented MAX.

Actual defect→correction: independent controls gained a valid scope-
laundering case and fake real-language-sweep flag without weakening expected
diagnostics. The guard rejected the latter as D3-MYTH rather than D3-SCOPE;
same owner489 corrected screening scope labels and retained belief-world-
fact D3-MYTH. A documented boolean/integer alias in frozen expectations
then received strict integer checking and two subprocess controls. Parent
actually ran the positive guard (exit0/findings[]) and selftest (exit0,
5/5positive,16/16domain,4/4malformed,5/5frozen) at guard SHA256
`849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e`.
Unknown extra frozen metadata, set-valued finding IDs and safe in-repo
symlinks remain explicit interface limits. Owner reported separate /tmp
probe files; zero outside writes ever is not claimed. No unrelated routing,
credential, sibling, lore or world-bible changes are shipped.

Reviewer502 found synthetic `coda` versus real `coda_subset` fixture drift
and an inert legacy coda inventory. Existing executor490 owns the scoped
adapter/fixture fix and derived outputs. Parent explicitly expanded that
same executor's assigned ownership to implement `reports/round-7/run-validation.py`
for parent review; this delegation is recorded separately from the original
parent-owned acceptance declaration, with no new authority/worker/batch.
The handoff scribe501 is reconciling actual glossary/names/bridges rather
than shipping stale independent proposals. The final frozen manifest,
content-equivalence checks, original counting command and clean delivered-
tree old-surface regression remain required before any final admission.

Before final bookkeeping, a parent byte comparison found506 frozen baseline
files unchanged, LOG/SKILL prefixes intact and only SCORECARD/corpusREADME
editable. `SKILL.md` now appends bounded D3 decisions/error patterns and
commands; `corpus/README.md` keeps all old frontier debts and links this new
exercise. `corpus/lessons/round-7.md` records useful findings plus honest
pending gate status. No axis verdict or capability is admitted by this
checkpoint. The requested remote publication will use lane identity and a
report-last commit, with a durable restart queue if final checks find a
remaining blocker rather than forcing a green result.

Further observed integration: parent created the24-input computational
`examples/culture-d3/expected.json` (SHA256
`74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080`)
from measured bytes and the predeclared0/[] expectation. The actual frozen
CLI exits0/findings[]. Reviewer502 closed both prior code findings with
behavioral evidence: fake sweep now D3-SCOPE; a real-projection `pinat`
garment mutant now produces PHON-CODA FAIL for forbidden final /t/. Its
seventeen bounded adversarial probes pass, and it corrects its earlier
unproven symlink test in an append-only review section rather than hiding it.
A genuine outside-target symlink is rejected before reading; in-repo aliases
remain an explicitly accepted bounded behavior, not blanket path hardening.

Scribe501's final pass supplies seventeen measured handoff artifact rows,
actual constructed glossary/names/utterances/bridge relations, separate
three independent versus five total positive controls, and the correct four
round6 unresolved IDs (R6-09-B remains partial). Parent independently
compared all20 E0/E1/gloss rows, all6 name/type/label/base rows and all17
artifact digests against delivered bytes. One remaining phrase was corrected
by parent to four closed ledger files for five source bindings. Parent ran
actual legacy calls: naming exit1, exactly CROSS-HOLD×2 plus E0/E1 NAME-NEAR
review and no PHON/DERIV FAIL; costume exit1, exactly C03 R-01 note/noR-02;
handoff exit0, sixteen fields/twenty glossary entries/no findings. Expected
holds are preserved, not failed surprises or fabricated clearance.

Review interpretation correction: one nonblocking review sentence proposes
reissuing the snapshot after prose freeze. The parent does not adopt that
reading: handoff/README are deliberately excluded from computational inputs
and pinned separately by acceptance. Only changes to a listed input require
reverification and a new freeze. The existing24input digests remain correct;
regenerating the manifest merely to make an excluded prose edit look pinned
would create misleading provenance. The reviewer is advisory, not an
admission authority. The original counting command, complete historical
regression and clean staged replay are the remaining acceptance steps.

### User-requested session wrap — round7 remains unadmitted

The user explicitly requested immediate wrap-up, cancelled the goal and
instructed no further background agents. Remaining integration task490 was
stopped; no additional swarm or training round is authorized by this wrap.
Current developments are preserved and published as a checkpoint, not a
completed/admitted round. Start the next session with
`reports/round-7/checkpoint.json`.

The partial runner is syntax-valid (SHA256
`c3b8418445d03bee2ba394ab6e4e4767e5ef07168c1a70dc904b3813e878c1e7`).
Its existing worker receipt says acceptance=false: F's duplicate-parent
negative-control expected-message mismatch and the nested old-surface
private-Git regression remain red. Its O=true is provisional, unreviewed
and not admission. All24 computational snapshot digests still match; the
three new Python files parse and git diff --check is clean. No full clean
staged acceptance pass is claimed. The next model must inspect/fix these
harness defects without weakening thresholds or changing historical gates,
then rerun and record six-axis verdicts. Existing source counts, domain
subchecks and expected holds remain useful evidence, not a forced pass.

### User-requested removal of the round7 checkpoint handoff

Removed `reports/round-7/checkpoint.json` and its active SCORECARD/report
handoff references at the user's request. Development files, original claims,
validation results and reviews remain unchanged; round7 is still unfinished.
Earlier LOG entries describe historical actions and are retained append-only.
No goal, background agent or automatic continuation is started by this cleanup.


## 2026-10-17 — Operator training regimen + round-7 ledger closure

- **Trigger:** operator directive (this session): train kotodama-shokunin in
  3 loops × 7 rounds = lane rounds 8–28; per loop 4 build rounds of 64
  workers on `opencode-go/deepseek-v4.1-flash`, 1 verify round of 64 workers
  on `openai-codex/gpt-6-luna-max`, 1 expand round of 128 workers on
  `xai-oauth/grok-4.7-fast`, 1 integrate round of 32 workers on
  `openai-codex/gpt-6.1-sol` (max effort).
- **Ledger closure:** appended 6 `retroactive-closure` rows (lane rounds
  1–6, status `failed` = fleet reports never landed; lane-side evidence in
  `reports/round-5..7/`; presence-of-evidence only) and 1 `closure` row
  (round 7 `failed`: terminated at operator session wrap, acceptance receipt
  failing per `reports/round-7/validation.json`, no landed report, never
  re-dispatched per the round-7 declaration) to `MANIFEST.json rounds[]`.
- **Supersession:** this directive supersedes the older SCORECARD `Planned`
  mapping (rounds 8–9 DeepSeek / round 10 Grok-128 ordering); the loop
  structure governs rounds 8–28.
- **Evidence:** MANIFEST.json rounds[] tail (7 new entries); SCORECARD.md
  `## Planned`; round-8 declarations in `reports/round-8/claims.json` and
  `reports/round-8/targets.json`.


## 2026-10-17 — Round 8 admitted (loop 1, build 1 of 4; 64-worker opencode-go/deepseek-v4.1-flash)

- **Trigger:** operator regimen (3 loops × 7 rounds, lane rounds 8–28);
  claims F/O/D declared in `reports/round-8/claims.json`, shards in
  `reports/round-8/targets.json`; baseline `cf338a7`.
- **F (freshness):** 15/15 residual round-6 rows rechecked with fresh
  retrieved-passage receipts (`reports/round-8/freshness/`); raw 15×
  supported reconciled to 11 partial-support / 4 unresolved; passage vs
  whole-claim separation enforced by harness controls; spot-check audit
  `freshness/audit.md`.
- **O (operability):** round-7 F-check identity-collision defect diagnosed
  (`operability/o01-diagnosis.md`) and fixed in new `tools/harness/r8_checks.py`;
  20 legacy defects inventoried from supplemental reviews 26/29
  (`defect-inventory.json`); 10 isolated negative controls; battery/craft
  selftests green (`battery-rerun.json`); round-3 manifests 7/7 isolated.
  Gate repairs: costume-era/myth/naming/phonology/provenance gates hardened
  (duplicate-key, depth-cap, anchor/tag rejections) — this legitimately
  drifted the D2 packet's reader pin, regenerated by the orchestrator
  (`python3 tools/assemble-d2.py`, byte-identical `--check`).
- **D (depth, capability `d2-typed-labels`):** new `tools/d2-typed-labels.py`
  (five kinds, declaration-based typing, borrow-ledger clock checks);
  selftest 39/39; typed projection `examples/culture-d2/typed-labels.d2.yml`;
  SKILL.md label-typing decision table + error rows landed from
  `reports/round-8/depth/skill-table-draft.md` per its landing instructions.
- **Integration:** acceptance `python3 reports/round-8/run-validation.py`
  exits 0 (`validation.json`, `rerun.json`); metadata sweep repaired
  frontmatter across `corpus/knowledge/` (11 shard fragments,
  `reports/round-8/metadata/`); adjacency clean (`adjacency.md`); one
  escalation to fleet `.ufo/l0-questions.md` (contract digest vs lore r93).
- **Honesty notes:** receipts are rechecks, not historical certifications;
  4 rows stay unresolved; calibration row is an unclaimed observation.


## 2026-10-17 — Round 9 admitted (loop 1, build 2 of 4; 64-worker opencode-go-2/deepseek-v4.1-flash)

- **Trigger:** operator regimen; claims F/O/D in `reports/round-9/claims.json`;
  baseline `a7bb205`.
- **F (freshness):** 4 residuals escalated with 12 hunter receipts
  (primary/museum, scholarly-fulltext, alternate-angle strategies per
  residual) + verifier reports V01–V03 + spot-check audit; reconciled 4/4
  unresolved → partial-support, raw labels preserved
  (`reports/round-9/freshness/`). Headline: R8-F01's round-8 `to-verify` item
  closed at catalogue level (Louvre ark cl010166127 + CDLI P220619 Rimush
  bilingual witness; AO 5477 qualified as a palaeo-Babylonian copy, not a
  contemporaneous object).
- **O (operability):** 7/7 structural gates carry committed expected.json
  drift-pin baselines (`tools/gates/expected/`, `tools/gates/frozen/<gate>/r9-pre/`);
  battery extension validates tampered → could-not-evaluate; audit confirms
  zero gate behavior changes (`reports/round-9/baselines/`).
- **D (depth, capability `culture-d3-acceptance`):** D3 acceptance completed
  as new round-9 work (round 7 stays failed): --check byte-identical,
  evidence-coupling selftest green, frozen replay exit 0/0 findings after the
  orchestrator refreshed three expected.json pins — all three drifts are
  round-8's legitimate committed changes (two gate repairs + one contract
  frontmatter repair), the D2-equivalent re-pin precedent is
  `reports/round-8/depth/test-replay.md` §6.
- **Integration acts (orchestrator):** reconciliation rows normalized to the
  declared flat `raw_label` contract (verdicts untouched); D3 pins refreshed;
  two out-of-lane worker writes swept into scope (fleet-root
  `reports/round-9/metadata/v09-myth.md` moved; junk AccessDenied-XML PDF
  deleted) — conformance defect recorded in the round-9 fleet notes.
- **Environment:** `/tmp` inode table at 100% hit ≥5 shards; workers adapted
  via in-lane scratch; operator cleanup decision queued at L0.
- **Evidence:** `reports/round-9/validation.json` acceptance true;
  `corpus/lessons/round-9.md`; SCORECARD §"Axes — round 9".

## 2026-10-17 — Round 10 admitted (loop 1, build 3 of 4; 64-worker opencode-go/deepseek-v4.1-flash, attempt 4)

- **Trigger:** operator regimen; claims C/F/O in `reports/round-10/claims.json`;
  baseline `eb348f3`. Model availability: keys -3/-4/-5 all returned 402
  insufficient funds at launch (availability-attempt-1/2/3.json, no work
  performed); key 1 quota had reset and carried the round (61/64 completed).
- **C (coverage):** 179 → 189 knowledge entries (ling +3, myth +3, culture +2,
  verification +2), each gap-named with decision records and resolving
  sources; README index reconciled (`reports/round-10/coverage/`).
- **F (freshness):** 192-row drift ledger; 36/36 cited commands covered after
  the integrator re-ran 14 hashless rows, attached 10 fix-evidence pointers,
  and added the one missing cited command (`assemble-culture-d3.py --selftest`,
  SKILL.md:264); stale items fixed or documented (`reports/round-10/drift/`).
- **O (operability):** 24/24 open findings dispositioned (18 fixed-with-control,
  5 wont-fix documented, 1 wrong) with verifier re-runs
  (`reports/round-10/findings-tracker.json`).
- **Conformance defects:** a stale-fixer rewrote filed receipt bytes
  (reports/round-9/validation.json, reports/round-8/run-validation.py) —
  reverted by the integrator; staleness documented in the ledger instead of
  back-patched. Two new entries needed integrator gap-field completion
  (plant-symbolism, transport-mobility-lexicon).
- **Evidence:** `reports/round-10/validation.json` acceptance true.

## 2026-10-17 — Round 11 REJECTED (loop 1, build 4 of 4; F failed as declared)

- **Trigger:** operator regimen; claims D/O/F in `reports/round-11/claims.json`;
  baseline `e3ef171`; 54/64 workers completed (10 late scribe seats failed).
- **D (depth, verified):** typed pipeline wired — derived typed packet +
  `typed-pipeline-gate.py`; five legacy gate scripts untouched; e2e findings
  exactly the expected hold set (15 holds named pre-implementation);
  10/10 PHON-INVENTORY artifacts eliminated; negatives caught.
- **O (operability, verified):** `tools/exercise-handoff-e2e.py` — packet
  assembled from live D2/D3 artifacts, 16/16 fields + 20/20 glossary entries,
  handoff gate green in isolation, frozen baseline with tamper control.
- **F (freshness, FAILED as declared):** 192/192 rows rechecked, 147 stable
  = 0.778 < 0.95; all 45 drifts dispositioned (round-10/11 legitimate changes,
  environmental path embedding, 3 transcription defects incl. truncated ledger
  row 187 — its sha256sum leg reproduces the prior exactly). Threshold assumed
  a quiet tree; build rounds legitimately change it. Not gamed; reported.
- **Integrator acts:** repaired 3 receipt schema defects (1:1 command text,
  row-047 hash contradiction, row-187 disposition); recomputed summary.json.
- **Consequence:** freshness axis-move claims pause pending operator
  recalibration (L0 queued); round 12 (Luna verify) audits this round.

## 2026-10-17 — Round 12 admitted (loop 1 verify round; 64w openai-codex/gpt-6-luna-max)

- **Trigger:** operator regimen; verify claims C/O/A in `reports/round-12/claims.json`;
  baseline `69d0c21`; 25/64 completed (route capacity), coverage completed by
  the integrator (61 commands re-run; ledger normalized to licensed schema).
- **C (calibration, verified):** 89-row recount ledger over rounds 8-11;
  round-11 rejection independently reproduced with the ratio correction
  (147/192 = 0.7656; 0.778 = 147/189 — both now recorded).
- **O (operability, verified):** consolidated 15-entry defect ledger; 7
  fixed-with-control (incl. rounds 8+9 filed `validation.json` clobbered by
  ledger-command re-runs of round validators — restored byte-exact from
  e1694ba/9dc18ec); 8 routed to round 14.
- **A (adjacency, verified):** zero bleed across the 10 new entries + typed
  pipeline; PROVINCE accurate; handoff packet REJECTED on semantics (missing
  uncertainty dimension + bilateral acknowledgment) — routes to rounds 13/14.
- **Evidence:** `reports/round-12/validation.json` acceptance true.

## 2026-10-17 — Operator regimen amendment + round-13 dispatch state

- **Amendment (operator, this session):** each loop gains 2 GLM-flash rounds at
  its end (`zai-coding-plan/glm-5.3-flash`, 16–32 workers each). Loops are now
  9 rounds; lane rounds 8–34 (27 total). GLM rounds are additional to the
  original 7-round structure, not a model substitution.
- **Round-13 dispatch state:** the first 128-worker Grok expand swarm ran
  407 s and was manually interrupted before any worker completed — zero files
  landed; the tree sat clean at declaration commit `3dedab2`. A route probe
  precedes the resume.
- **Provider amendment (operator, this session):** one of the 64-worker
  DeepSeek build rounds uses `hyper/deepseek-v4.1-flash` as provider instead
  of opencode-go. Designated: **round 19** (loop 2, build 3 of 4). All other
  DeepSeek build rounds stay on opencode-go keys 1/2 (keys -3/-4/-5
  unprovisioned). This is an explicit operator route designation, not a
  silent substitution.

## 2026-10-17 — Regimen amendment 3: expand rounds cancelled, GLM rounds pinned

- **Operator directives (this session):** (1) skip the Grok expand rounds
  entirely (both interrupted attempts produced zero output; route abandoned by
  operator decision, not provider failure); (2) the 2 end-of-loop GLM rounds
  are pinned to 16 workers each on `zai-coding-plan/glm-5.3-flash-low` — the
  zai lane whose low alias is host-pinned to MAX thinking effort (documented
  pin flip 2026-10-16).
- **Loop structure now:** 4 build (64w deepseek; r19 = hyper provider) +
  1 verify (64w luna) + 1 integrate (32w sol) + 2 GLM (16w zai-max) = 8
  rounds per loop. Lane map: loop 1 = 8–16 (r13 skipped, r14 integrate,
  r15–16 GLM), loop 2 = 17–24, loop 3 = 25–32.
- **Round 13 status:** operator-skipped before any work landed (two interrupt
  events, 0 files); round-13 claims (D4, civ-map, handoff-v2) are deferred —
  handoff-v2 and civ-map fold into loop-1 GLM rounds 15–16 (16-worker scope),
  D4 into a loop-2 build round.


Prepared 2026-10-17. Owner: R14-C09..C10 integration shard. Parent lands the
append below in `LOG.md` after reconciling the actual retrospective and
round-14 controls. This worker has not changed shared bookkeeping or filed
round-8–12 artifacts. No round-14 admission is asserted by this draft.

## Proposed LOG append

### 2026-10-17 — Round 14 integration: loop-1 recorded-outcome checkpoint

- **Trigger and scope:** round-14 O/D/C declarations in
  `reports/round-14/claims.json`, dispatch-role allocation in `targets.json`,
  declared baseline `926c86f8be3cc9307f8f10dce55768c290b6f94d`. This entry
  consolidates the recorded rounds 8–13 states without reopening filed
  artifacts or counting bookkeeping/report commits as training rounds.
- **Recorded states:** rounds **8, 9, 10 and 12 admitted; 11 rejected;
  13 operator-skipped**. The dated, read-only `C09/C10-CENSUS` command in
  `reports/round-14/scorecard-draft.md` ran on 2026-10-17 and found
  **4 admissions / 1 rejection / 1 skip**, with stored claim flags
  **14 passed / 1 failed**. Receipt flags agree with the final SCORECARD
  sections and LOG entries; they are not an independent replay of every
  literal claim threshold.
- **Per-round claim states and evidence:** round 8 F/O/D passed
  (`reports/round-8/claims.json`, `validation.json`); round 9 F/O/D passed
  (`reports/round-9/claims.json`, `validation.json`); round 10 C/coverage,
  F and O passed (`reports/round-10/claims.json`, `validation.json`);
  round 11 D/O passed and F failed (`reports/round-11/claims.json`,
  `validation.json`); round 12 C/calibration, O and A passed
  (`reports/round-12/claims.json`, `validation.json`). Counts/date/command:
  `C09/C10-CENSUS`, 2026-10-17. The independent literal-threshold assessment
  and conformance taxonomy belong in the integrated
  `reports/round-14/loop1-retrospective.md`, not inferred from booleans alone.
- **Round-11 rejection is retained:** the comparable-row channel is
  **147/189 = 0.777777…**; the all-row channel is
  **147/192 = 0.765625**, recorded as 0.7656 in its summary. Both fail the
  predeclared **0.95** threshold. Command: `C09/C10-CENSUS`, measured
  2026-10-17. Evidence: `reports/round-11/validation.json`
  `claims.F.measurement`, `reports/round-11/recheck/summary.json`, and
  `reports/round-12/recount/dispositions.md:77-79`. The earlier equation
  joining 0.778 to denominator 192 is a documentation error, not a reason
  to admit round 11 or erase its useful D/O evidence.
- **Operator calibration remains pending:** future hash-stability claims
  need an operator-selected measurement contract: a pinned quiet-tree byte
  comparison, or an explicitly declared change-aware/semantic measure that
  separates legitimate changes, environment-dependent output and defects.
  No option is selected here; no retrospective threshold change repairs
  round 11. Freshness axis-move claims remain paused as recorded in
  `SCORECARD.md:201-205` and `LOG.md:3021-3029`.
- **Handoff assurance stays bounded:** round 12's A pass means the adjacency
  audit and its findings were recorded, not that the handoff is accepted.
  The semantic rejection for missing uncertainty dimension and bilateral
  acknowledgment remains visible (`SCORECARD.md:219-227`,
  `reports/round-12/adjacency/A11-A12-handoff.md`). Passing envelope shape
  is not lore acknowledgment, cultural permission or canon clearance.
- **Round 13 is skipped, not failed provider work or a completed round:**
  the operator abandoned the interrupted expand route before work landed
  (`LOG.md:3065-3080`). Handoff-v2/civ-map moved to the GLM rounds 15–16;
  D4 moved to a loop-2 build round. This checkpoint does not declare the
  amended loop complete or turn deferred claims into delivered capability.

#### Integration controls and unresolved bookkeeping

- **Receipt-clobber mechanism:** live rechecks invoke validators that write
  their own filed `validation.json`. Round 12 restored the round-8/9
  receipts, but restoration alone did not prevent recurrence. Evidence:
  `reports/round-12/defects/ledger.json` `FRR-12a`/`FRR-12b`,
  `reports/round-12/defects/routed.md:10-16`. Round 14 declares a successor
  guard at `tools/harness/receipt_guard.py`: refuse a committed receipt
  overwrite with exit 3 and a named diagnostic unless
  `REFRESH_RECEIPTS=1` is explicitly set. That is the declared acceptance
  contract, not a verified implementation claim in this draft. Required
  control: `python3 tools/harness/receipt_guard.py --selftest`, plus the
  guarded round-14 runner and the assigned negative controls; parent must
  cite their actual dated receipts before recording D as passed.
- **Routed-item closure is not inferred:** the declared round-14 worklist
  requires an explicit item-to-disposition map in
  `reports/round-14/routed-resolution.json`. Each applied fix must name its
  before/after control; documentation-only resolutions must name their
  evidence and remaining limits. Battery roots, audit-count erratum,
  tracker pointer, draft/final reconciliation, runner-hash citation,
  index-updater classification and stale-fixed conflicts cannot be called
  closed merely because this bookkeeping exists.
- **Filed queue-count discrepancy retained:** a read-only census of the
  round-14 declared baseline on 2026-10-17 gives **15 ledger entries:
  8 fixed-with-control / 7 routed**; `R11-DRAFT` is fixed-with-control.
  Command:
  `git show 926c86f8be3cc9307f8f10dce55768c290b6f94d:reports/round-12/defects/ledger.json | python3 -c 'import collections,json,sys; e=json.load(sys.stdin)["entries"]; print(len(e), dict(collections.Counter(x["status"] for x in e)))'`.
  The round-12 SCORECARD/LOG headline instead says 7 fixed / 8 routed, while
  the round-14 declaration requests eight resolutions. New round-14
  append-only exposure entries do not enter that historical total.
  Independent corroboration: `reports/round-14/retrospective-audit-C08.md:7`.
  Parent must reconcile the mapping explicitly without shrinking the
  declared worklist or rewriting historical keys. Named regimen amendments
  at `LOG.md:3048-3080` likewise take precedence over an unverified aggregate
  amendment count.
- **Append-only and regression controls:** retain filed rounds 8–12;
  corrections land as permitted new records/keys, never as replacement
  historical receipts. Run the round-14 guard and documented regression
  entry points in their assigned scopes with `TMPDIR=$PWD/.scratch`.
  Parent acceptance is `python3 reports/round-14/run-validation.py` on the
  delivered tree, including battery/craft/D2/D3 regressions. This shard did
  not run that validator or claim those controls green. A read-only census
  cannot substitute for real regression calls, and no new work commit or
  final report hash is fabricated.

This entry is an integration checkpoint, not the round-14 final verdict.
Parent records O/D/C acceptance and all-axis judgments only after the
retrospective, routed dispositions, guard controls and regression evidence
exist. No rank, independent promotion verification, historical-truth
certification or lore/world-bible ownership is claimed.

## 2026-10-17 — Round 15 admitted (loop 1, GLM round 1 of 2; 16w zai flash MAX)

- **Trigger:** regimen; claims O/D in `reports/round-15/claims.json`; baseline
  `c60b17c`; 12/16 completed (O02 timed out; suite covered it).
- **O (verified):** handoff packet v2 closes the round-12 semantic reject —
  uncertainty dimension + claim-to-record links + atomic D2 edges;
  validators 19/19 + 31/31; frozen expected.json + freeze/verify tool;
  contract audit re-run pass-with-named-gaps.
- **D (verified):** SKILL.md claim-uncertainty decision table landed (BLOCK A
  4,741 chars + 13 error rows; 17/17 cited).
- **Integrator acts:** settled-tree validation rerun (late-landing artifacts);
  SKILL landing repaired after a slicing defect (BLOCK A initially missed);
  three reviewer findings routed to round 16.
- **Evidence:** `reports/round-15/validation.json` acceptance true.

## 2026-10-18 — Round 16 admitted (loop 1, GLM round 2 of 2; 16w zai flash MAX)

- **Trigger:** regimen; claims C/O in `reports/round-16/claims.json`; baseline
  `0ce7714`; 16/16 completed.
- **C (verified):** civ-map 94/94 (82 current / 12 stale-documented with named
  reasons); auditor re-derived independently (20 spot-checks); integrator
  fixed 2 map defects + row-annotation gaps found in audit.
- **O (verified):** F10-1 edge-source validation (38 selftests), F9-1 L-anchor
  collision closed, F9-2 link coverage 33 orphans -> 0 (packet-v2-07,
  83/83 links, frozen baseline re-frozen after the verify seat pinned the
  canonicalization divergence).
- **Loop 1 complete:** rounds 8-16 closed (13 operator-skipped; 11 admitted,
  1 rejected). Loop 2 = rounds 17-24 (r19 on hyper provider per operator).
- **Evidence:** `reports/round-16/validation.json` acceptance true.

## 2026-10-18 — Round 17 REJECTED on claim D (loop 2, build 1 of 4)

- **Trigger:** regimen; claims D/C/O in `reports/round-17/claims.json`; baseline
  `9b49a4a`; 30/64 completed.
- **C (verified):** 7 of 12 stale civ entries fixed with live verified
  replacements; 5 replacement attempts documented; verifier re-runs green.
- **O (verified):** `tools/assemble-culture-d4.py` durable (81/81); integrator
  eras normalization (flat tag list per the projector contract + records under
  era_records); packet regenerated byte-identical.
- **D (failed as declared):** the round-11 typed-pipeline-gate's L1
  assembler-identity leg pins assemble-d2 output and cannot consume a D4
  packet; the typed projection itself runs (74 labels / 15 holds emitted).
  Generalization + re-pin cascade routed to round 18. The D4 tree, assembler,
  and projection remain as delivered artifacts.
- **Design fork recorded:** three D4 concepts competed in design docs; the
  delivered component tree rules. Lesson: design-authority seats must converge
  before component seats build (process checklist for round 18).
- **Evidence:** `reports/round-17/validation.json` (C/O pass, D fail).

## 2026-10-18 — Round 18 admitted (loop 2, build 2 of 4; repairs the r17 rejection)

- **Trigger:** regimen; claims O/D/C in `reports/round-18/claims.json`; baseline
  `c66ac3c`; 19/64 completed; integrator built the missing D4 adapter.
- **O (verified):** gate generalized (declared assembler; D2 default
  byte-identical); re-pin cascade green; L2 D4-family accounting; before/after
  digest table records d96958b6 -> 04ad4bb4.
- **D (verified):** D4 typed pipeline gate-verified 19/19; findings exactly the
  15-hold + 1-note expected set; frozen manifest replays.
- **C (verified):** civ-map r18 revision applies the round-17 patch.
- **Integrator acts:** `tools/assemble-d4-typed.py` built (text transform after
  diagnosing serializer round-trip corruption: regex/boolean/null mangling);
  routing model = one row per translated label (garment + slot), owed slot
  named once; repin-d2 manifest re-pinned to the post-L2 gate sha.
- **Evidence:** `reports/round-18/validation.json` acceptance true.

## 2026-10-18 — Round 19 admitted (loop 2, build 3 of 4; hyper provider per operator)

- **Trigger:** regimen + operator provider substitution
  (`hyper/deepseek-v4.1-flash`); baseline `169c616`; 17/64 completed (slow
  route); integrator-authored validation.
- **D (verified):** SKILL.md slot-label routing + derivation-replay subsections
  (drafts errata'd; review blockers were pre-repair states, superseded).
- **C (verified):** verification 15->20, synthesis 24->29; zero-defect audit.
- **O (verified):** battery registers 9 gates (2 D4 duty-2 inspected; mode
  documented); D4 baselines committed and valid; 35/35 selftest.
- **Integrator acts:** adapter selftest repaired to 12/12 (mirror faithfulness
  for the projector's D2 alias-component dependency — documented wart routed;
  named-once fixture); availability record closed.
- **Evidence:** `reports/round-19/validation.json` acceptance true.

## 2026-10-18 — Round 20 admitted (loop 2, build 4 of 4)

- **Trigger:** regimen; claims D/O/C in `reports/round-20/claims.json`; baseline
  `122086b`; 20/64 completed.
- **D (verified):** handoff e2e v3 — D4 claims (27 total; census 16/7/4);
  102/102 links; frozen baseline.
- **O (verified):** projector era-alias wart closed per-family; D2 byte-identical;
  repin cascade as new rows.
- **C (verified):** README reconciled command-carried (six partition counts).
- **Integrator acts:** fragment-index collision disposition (kept the dated
  X24 census index alongside X19/X20's; noted in the round notes).
- **Evidence:** `reports/round-20/validation.json` acceptance true.

## 2026-10-18 — Round 21 admitted (loop 2 verify round)

- **Trigger:** regimen; verify claims C/O/A in `reports/round-21/claims.json`;
  baseline `8115eaa`; 20/64 completed; integrator coverage completion.
- **C (verified):** recount ledger complete; r18 repair reproduced; all
  mismatches dispositioned (see `recount/dispositions.md`).
- **O (verified):** 23-entry consolidated defect queue; bounded fixes;
  routed to r22.
- **A (verified):** handoff v3 contract green on the current pair; one filed
  D2->D4 fixture bleed routed; PROVINCE accurate.
- **Evidence:** `reports/round-21/validation.json` acceptance true.

## 2026-10-18 — Round 22 REJECTED on claim D (loop 2 integrate)

- **Trigger:** regimen; claims O/C/D in `reports/round-22/claims.json`; baseline
  `cd9c8e4`; 9 completed + 6 aborted (operator interrupt took the D-impl seats).
- **O (verified):** six routed items resolved (routed-resolution.json); all
  regressions green; controls per item.
- **C (verified):** loop-2 retrospective with the qualified r17/r18 arc
  assessment; auditors green.
- **D (failed as declared):** the D4 bleed fix was analyzed (24-field census,
  injection point, family-clean design) but never implemented — the impl seats
  were interrupted. Routed to round 25 with the full recipe.
- **Evidence:** `reports/round-22/routed-resolution.json`; regressions re-run
  by the integrator (all exit 0).

## 2026-10-18 — Correction to the round-22 entry (append-only; the r22 ledger row stands)

The round-22 entry above records the D-claim implementation as "never
implemented". Subsequent verification (round 23: X04 settled-tree rerun and
the D-rule drafters' source audit) proved the family-clean implementation IS
present at commit `0e81d9d` — the aborted D04-D06 seats had written their
changes to the working tree before the interrupt, and the round-22 close
commit swept them in: projector `2819f687…` carries the `_selftest_family`
dispatch (build_payload only for the default family), selftest 163/163, live
D4 holds 12/0/0. The r22 rejection's verification path (validator legs
requiring the SKILL rule and specific pin rows at close time) was indeed
unmet at close, but the source fix itself had landed; the verdict mis-described
the tree state. Correction recorded per append-only discipline.

## 2026-10-18 — Round 23 admitted (loop 2, GLM round 1 of 2)

- **Trigger:** regimen; claims O/D in `reports/round-23/claims.json`; baseline
  `0e81d9d`; 17/17 completed.
- **O (verified):** wording false positive dispositioned (preferred route);
  six combined-source successor pins landed; regressions green.
- **D (verified):** family-clean projection rule landed in SKILL.md.
- **Conformance:** the round-22 straggler (in-place regression.md completion)
  resolved per X02's adjudication — filed bytes restored, completed report
  preserved as a new file; receipt-guard enforced the close-time refresh.
- **Correction:** see the append-only entry above — the r22 'never
  implemented' wording was wrong; the family-clean impl was in 0e81d9d.
- **Evidence:** `reports/round-23/validation.json` acceptance true.

## 2026-10-18 — Operator amendment 4: devin provider for loop-3 DeepSeek builds

Operator directive (this session): all remaining DeepSeek build rounds use the
devin provider — designated `devin/deepseek-v4-1-flash-high` for loop-3 builds
(rounds 25-28, 64 workers each). This replaces the opencode-go key rotation and
the hyper substitution for those rounds; it is an explicit operator route
designation (provider test), not a silent substitution.

## 2026-10-18 — Round 24 admitted (loop 2 GLM round 2; promotion-review round)

- **Trigger:** regimen; claims C/O/D in `reports/round-24/claims.json`; baseline
  `8fbcee9`; 16/16 completed.
- **C (verified):** promotion-review dossier — boxes 1-4 verified-with-conditions
  by named non-author reviewers; decision operator-owned.
- **O (verified):** box-3 cold-run by four fresh-context seats; 7 fixes landed
  with controls; 7 named conditions.
- **D (verified):** SKILL.md staleness audit complete; F1-F8 fixed; 123-row
  per-row disposition table; zero silent staleness.
- **LOOP 2 COMPLETE (rounds 17-24).** Loop 3 = rounds 25-32 with DeepSeek
  builds on `devin/deepseek-v4-1-flash-high` (operator provider test).
- **Evidence:** `reports/round-24/validation.json` acceptance true.

## 2026-10-18 — Round 25 admitted (loop 3 build 1 of 4; devin provider test)

- **Trigger:** regimen + operator provider test (`devin/deepseek-v4-1-flash-high`);
  baseline `f74fc94`; 26/64 completed (31-min wave).
- **O (verified):** gate typed-input honesty (named input-class refusals +
  nullish guard; false red eliminated; source 19/19 byte-identical); v3 claim
  prose supersession (declared-in-r4).
- **D (verified):** argot-derivation checking leg implemented with real
  negatives; the delivered-vs-forecast delta named (register-form domain empty
  in the delivered packet — design-forecast never built).
- **C (verified):** corpus/lessons/README.md reconciled with open-question queue.
- **Evidence:** `reports/round-25/validation.json` acceptance true.

## 2026-10-18 — Round 26 admitted (loop 3 build 2 of 4; devin)

- **Trigger:** regimen; claims D/O/C in `reports/round-26/claims.json`; baseline
  `1ad491a`; 24/64 completed.
- **D (verified):** the register stratum lands; the round-17 forecast closes
  (8 forms, axis-to-operation rule, replay clean; named gaps recorded).
- **O (verified):** the register read-set change re-pinned through the r5
  chain; pin-repoint checker 17/17; r4 checker superseded-and-recorded.
- **C (verified):** open-question queue 100% dispositioned.
- **Correction:** X64's "stratum not landed" was a stale snapshot; integrator
  measurements confirmed the landing.
- **Evidence:** `reports/round-26/validation.json` acceptance true.

## 2026-10-18 — Round 27 admitted (loop 3 build 3 of 4; devin)

- **Trigger:** regimen; claims D/O/C in `reports/round-27/claims.json`; baseline
  `b95fca1`; 24/64 completed.
- **D (verified):** register law lands (RGL-01..05; A/B-chosen route; 0 new
  holds); syllabify fixed; RL-1/RL-3/RL-4 named.
- **O (verified):** the D4 pin sweep complete; regressions green.
- **C (verified):** register-strata knowledge entry + README.
- **Evidence:** `reports/round-27/validation.json` acceptance true.

## 2026-10-18 — Round 28 admitted (loop 3 build 4 of 4; devin)

- **Trigger:** regimen; claims D/O/C in `reports/round-28/claims.json`; baseline
  `69cecbc`; 24/64 completed.
- **D (verified):** the register-law replay leg lands (6 D4L-LAW-* classes; the
  substring trap designed out); RL-4 fixed; the leg surfaces 4 real
  D4L-LAW-DANGLING findings on the clean packet (design defect, priced for r30).
- **O (verified):** final pin sweep; regressions green.
- **C (verified):** ceiling knowledge recorded; ceilings entry; README.
- **LOOP 3 BUILDS COMPLETE (rounds 25-28).** Remaining: r29 verify (luna),
  r30 integrate (sol), r31-32 GLM (zai).
- **Evidence:** `reports/round-28/validation.json` acceptance true.

## 2026-10-18 — Round 29 admitted (loop 3 verify round)

- **Trigger:** regimen; verify claims C/O/A in `reports/round-29/claims.json`;
  baseline `e923d6e`; 17/64 completed; integrator dispositions post-wave.
- **C (verified):** recount complete; register landing reproduced; law
  calibration dispositioned; R27 sweep reproduced; devin availability
  documented could-not-evaluate with durable records.
- **O (verified):** 24-entry defect queue; bounded fixes; routed to r30.
- **A (verified):** zero unfiled bleed; PROVINCE byte-identical.
- **Evidence:** `reports/round-29/validation.json` acceptance true.

## 2026-10-18 — Round 30 admitted (loop 3 integrate round)

- **Trigger:** regimen; claims O/C/D in `reports/round-30/claims.json`; baseline
  `44145d5`; 19/32 completed; orchestrator executed the parent-action list.
- **O (verified):** 5/5 routed items resolved (QREG, speaker candidate, battery
  registration 10/10, X63-F2, telemetry convention); v3 default chain
  re-pointed to declared-in-r6.
- **C (verified):** loop-3 retrospective + three-loop summary + the
  freshness-threshold restatement with a recommendation.
- **D (verified):** the Register-craft subsection landed; box-1 survey 28/28
  digest-pinned.
- **Evidence:** `reports/round-30/validation.json` acceptance true.

## 2026-10-18 — Operator amendments 5-6 (regimen spec notes)

- (5) The 128-worker xai-grok expand rounds remain skipped (reaffirming
  amendment 3); no grok round exists in the amended regimen.
- (6) Sol-max -> luna-max: where the regimen names a sol-max integrate round,
  luna max is the operator's stated preference. The three integrate rounds of
  THIS regimen (r14, r22, r30) already ran on `openai-codex/gpt-6.1-sol` per
  the earlier explicit spec ("1 last round using openai codex 6.1 sol max")
  and are closed; closed rounds are never re-dispatched. The preference is
  recorded for any future regimen.

## 2026-10-18 — Round 31: the jin'i-ryu self-improvement round (logged per the gate)

Given the round telemetry, the lane proposed and landed ONE falsifiable
improvement to its own operating files: **the telemetry finalization-closure
rule** (`reports/round-31/jinii/draft.md`; analysis at `jinii/analysis.md` —
five availability records filed `open-at-seat-close` in every modern round,
0/5 finalized despite every receipt landing; the r29 restate-hazard where the
disposition cited counts that appear in no record).

Delta landed: AGENTS.md gains the "Close what you open" bullet; SKILL.md's
executable checklist gains the closing-snapshot audit item; five retroactive
closing snapshots land under `reports/round-{19,25,26,27,28}/telemetry/`
(append-only, each naming the record it closes + that record's SHA-256).

Falsification condition (per the gate): (i) the audit leg — if the checklist
audit (`open-at-seat-close` + validation-landed + no closing snapshot) prints
a non-empty list after this round for a round admitted to LOG.md, the rule is
falsified and reverts; (ii) the integrity leg — if a closing snapshot's
`closes_sha256` mismatches its record's current bytes (an in-place edit of a
filed record), the rule is falsified; (iii) the malformed-rule leg — if
compliance is only possible by editing a filed record in place, the rule is
reworded or reverted. Later-round non-compliance fails that round's audit; it
does not by itself falsify the rule.

## 2026-10-18 — Round 31 admitted (loop 3 GLM round 1 of 2; regimen close-out)

- **Trigger:** regimen; claims C/O/D in `reports/round-31/claims.json`; baseline
  `e8d2d0d`; 12/16 completed (+1 seat collision, +3 late scribes).
- **C (verified):** closure-ledger.json — 32/32 lane rounds audited, zero
  missing; 22/22 filed reports commit-ancestor-valid; two honest findings
  (r23's missing Landed-changes heading; r13's documented operator-skip);
  two independent auditors re-verified 13 rows with zero mismatches.
- **O (verified):** the final green sweep — 50/50 capability rows exit 0,
  13 filed-red historical controls at their codes, battery 10/10, the
  r31-post frozen generation replaying 4/4 (the r28-post supersession gap
  closed), all 50 recorded commands re-executed green.
- **D (verified):** the jin'i-ryu delta landed as recorded above.
- **Evidence:** `reports/round-31/validation.json` acceptance true.

## 2026-10-18 — Round 32 admitted — THE REGIMEN IS COMPLETE

- **Trigger:** regimen; final claims C/O/D in `reports/round-32/claims.json`;
  baseline `4d50050`; 12/16 completed.
- **C (verified):** the completion criterion certified end-to-end (audit +
  two independent auditors).
- **O (verified):** the r32 final sweep 51/51 green x3 + 128 auditor
  re-executions zero-findings.
- **D (verified):** the final dossier — box 1 closed, capability inventory,
  operator decision materials.
- **THE REGIMEN:** lane rounds 8-32 = 25 rounds (21 admitted, 3 rejected
  honestly, 1 operator-skipped) across 3 loops with 6 operator amendments;
  every round carries a content-valid fleet report, SCORECARD/LOG records,
  and a MANIFEST closure entry. Rounds 1-7 closed retroactively at the start.
- **Evidence:** `reports/round-32/validation.json` acceptance true.

## 2026-10-19 — Regimen 2 contracted by operator directive (rounds 33–74)

- **Trigger:** operator directive in session (verbatim approved goal text now
  durable at `REGIMEN.md`); goal-mode objective filed against REGIMEN.md the
  same day. Supersedes no closed round; rounds 1–32 stand as filed.
- **Contract:** 3 loops × 14 rounds = 42 lane rounds, numbered 33–74,
  schedule/provider/worker-count table in REGIMEN.md (opencode-go builds with
  per-round key round-robin across live keys, hyper→devin fallback at
  position 4, luna-max verify at positions 5 and 9, swe-2 read-only git audit
  at position 14). Freshness axis-move claims remain paused pending the
  operator ruling queued since round 11.
- **Standing inputs from the closed regimen:** round-32 routed debt (falsifier
  audit filename mismatch, 7 unindexed lessons, 12 standing open items in the
  dossier) is the starting queue for round 33's claim declaration.
- **Evidence:** `REGIMEN.md`; prior regimen close at
  `reports/round-32/validation.json` (admission true); freshness pause
  recorded in `SCORECARD.md` round-11 section.

## 2026-10-19 — Round 33 ADMITTED (regimen 2, loop 1 build 1 of 3)

- **Trigger:** operator regimen (REGIMEN.md; goal filed 2026-10-19); claims
  O/C/A declared at baseline `139e3b6` against the round-32 routed debt
  (`reports/round-33/claims.json`); one 64-worker
  `opencode-go/deepseek-v4.1-flash` batch, observed 64/64
  (`telemetry/observed-dispatch.json`).
- **O (verified):** lessons index reconciled to revision 3 — audit exit 1
  (33 files vs 26 rows; `C31-1`+`C34-2`) → exit 0 (33/33/78, findings 0);
  applied bytes == the seats' verified reconstruction `f752e1d7…`
  (`op/lessons-reconciliation-receipt.json`). The round-32 falsifier debt
  (F-X16-3) located and fixed: the `SKILL.md` close-what-you-open one-liner
  tested `telemetry/closing-snapshot.json` (exists nowhere) and false-fired on
  five closed records; re-keyed content-keyed (`closes` + `closes_sha256`),
  0 rows live, 7/7 fixture scenarios (`op/O05-falsifier-disposition.md` §4).
- **C (verified):** the dossier's twelve standing open items dispositioned
  12/12 (`calib/open-items-ledger.json`); OI-04/05/06/12 fixed-with-evidence
  (C14 Fixes 1-4 + FD-N4/N5 applied, controls green); eight carried with
  owners. The numeral "12" is reconstructed, not quoted (F-C15-1 carried).
  Membership ruling F-C13-4: K03's twelve stand; box-4 readings 3a/3b/3c are
  out-of-set corroboration.
- **A (verified):** consolidated opening boundary audit (`adj/audit-assembled.md`),
  A01-A14 with independent re-runs; scope clean; zero unfiled bleed;
  contested items routed-not-absorbed.
- **Evidence:** `reports/round-33/validation.json` acceptance true (exit 0,
  receipt sha256 `93b28f36…`); fleet report `.ufo/reports/round-33/kotodama.md`;
  telemetry closed via `availability-close-33.json` (closes
  `dispatch-declared.json`, sha256 `139b964e…`).

## 2026-10-19 — F-C13-1 incident record: filed receipts written in-tree during round 33 (restored; record owed, now filed)

- **What:** during the round-33 wave, `reports/round-{5,6,7}/validation.json`
  were rewritten in the working tree (window 03:53:25Z-03:55:27Z; r5/r7
  content-differing, r6 mtime-only) and restored byte-exact by 03:55:27Z
  (`git hash-object` == `git rev-parse HEAD:<path>` for all three at
  04:15:47Z; r5 mutant digest `fe926984…` reproduced byte-identically by an
  isolated `git archive` run — `.scratch/c05-iso/` per `adj/A11` §4).
- **Mechanism:** the historical runners write their own receipt in place
  (`reports/round-5/run-validation.py:194`, `reports/round-7/run-validation.py:1171`,
  `reports/round-6/run-validation.py:336`) and never adopted the round-14
  receipt-guard — a guard-adoption gap, not a guard defect. The r26 runner
  carries the same hazard (`:90`, `:1909`); no round-33 counting command runs
  it in-tree. Probable writer: seat C05, `to-verify` (isolated-run artifacts
  corroborate; attribution not provable).
- **Status:** breached in flight, restored, PREVENTION recorded: no
  historical `run-validation.py` is executed in-tree (isolated copies only);
  the guard-adoption gap is routed as a standing operability debt (owners:
  future integrate rounds; the runners are filed bytes and are not repaired
  in place).

## 2026-10-19 — Supersession records (new rows; no filed byte rewritten)

- **Lessons README pins:** `reports/round-26/run-validation.py:97`
  `README_BASELINE_BLOB = a3187055…` and `reports/round-25/validation.json`
  `input_sha256 = ec7469da…` are superseded by the round-33 revision-3 bytes
  (sha256 `f752e1d7…`), per `op/O02-readme-delta.md` §6g. Affected filed
  runners go red **if re-run**; no round-33 counting command re-runs them.
  Re-pin cascade owner: a future round that re-verifies r25/r26 receipts.
- **SKILL.md digest:** `79fe91d3…` → `f9bd07c2…` (O05 re-key + C14 Fixes
  1-4 + FD-N4/N5). Box-1 survey re-verified green 28/28 at the new digest;
  prior line anchors shift (715 → 732 lines) — A09's R1-R8 exposure list
  stands as the re-survey worklist.
- **AGENTS.md:** round-31 drafting residue (orphan fence line + orphan
  `### 2.2 SKILL.md` heading at old :40/:42) excised per A07-F1 — 42 → 40
  lines, `grep -c '^```'` = 0. Live instruction file repaired; logged here.

## 2026-10-19 — Operator directive recorded (concurrency)

- Operator directive this session: use the outlined number of subagents per
  round (one batch per round at the declared worker count; REGIMEN.md
  schedule). Round 33's post-batch integrator seats (4) are recorded in
  `telemetry/observed-dispatch.json` as integration acts, not craft batches.
  Future rounds: integrator work defaults to in-session unless a round's
  declared shape says otherwise.

## 2026-10-19 — Round 34 (loop 1 build 2 of 3) — integration in progress; errata to the round-33 F-C13-1 record

- **Errata (append-only correction):** the round-33 F-C13-1 LOG entry and the
  round-33 routed-debt record named `reports/round-26/run-validation.py` as an
  unguarded receipt writer (`:90`, `:1909`). Seat K03's round-34 census
  (`reports/round-34/scout/K03-guard-pattern.md`, evidence at
  `reports/round-26/run-validation.py:1855`, `:1906`) shows r26 **is**
  guard-adopted: the r5/r6/r7 runners remain the unguarded class
  (`reports/round-{5,6,7}/run-validation.py:194,:336,:1171`). The round-33
  record stands with this correction pointer; filed bytes are untouched.
- **Adoption census landed:** `tools/harness/receipt_guard_adoption.py`
  (selftest green) + `reports/round-34/op/adoption-inventory.json`: 28 filed
  runners — 17 `guarded-refresh`, 11 `unguarded-in-place` (r5/r6/r7 among
  them). The 11-runner unguarded class is the standing adoption-gap debt
  (owner: future integrate rounds; protocol: isolated-copy-only re-runs).
- **Claim D progress:** `declared-in-r7` frozen (packet `45f57132…`), gate
  16/16 + 20/20 + 0, links 105/105, claims 27 (16/7/4), d4_stale_audit CLEAN,
  preservation 0 rows; `repin.json` records the cascade with measured values;
  named finding R34-N1 (r6-row refusal surfaces as KeyError, not E2E-DIGEST;
  routed to renderer hardening). Full admission record follows the round's
  validation run.

## 2026-10-19 — Round 34 ADMITTED (regimen 2, loop 1 build 2 of 3)

- **Trigger:** operator regimen (REGIMEN.md); claims D/O/C declared at baseline
  `da68a6d` (`reports/round-34/claims.json`); one batch on
  `opencode-go-2/deepseek-v4.1-flash`, key 2 of the round-robin — 63 seats
  authored/dispatched/completed (the declared `seat_count: 64` vs 63 rows is the
  named CO4 deviation, recorded not edited).
- **D (verified):** A02-H1 closed — the wave proved the packet staleness is
  structural (the renderer verbatim-carries the twelve D4 claim rows from filed
  round-20 and hard-codes OQ-V3-05; a re-render reproduces the stale packet
  byte-for-byte). Landed: successor claims-map at
  `declared-in-r7/claims-map.md` (ten replacements + three sweep-finds, 12 rows
  re-parsing under the renderer's own regex) + six renderer edits; frozen packet
  `45f57132…`; live-truth audit CLEAN; gate 16/16 + 20/20 + 0; links 105/105;
  r6 row refuses replay (exit 1, KeyError mechanism — finding R34-N1 routed to
  renderer hardening); `handoff/repin.json` records the cascade; filed r2..r6
  bytes untouched (P1: 0 moved protected paths).
- **O (verified, capability `receipt-guard-adoption-audit`):**
  `tools/harness/receipt_guard_adoption.py` + `op/adoption-inventory.json`:
  29 filed runners — 18 guarded-refresh / 11 unguarded-in-place (r5-r12, r19,
  r21, r29); routing receipt covers the unguarded class (isolated-copy-only
  protocol); zero in-tree runner execution; r26 errata (guard-adopted) filed
  against the round-33 F-C13-1 record.
- **C (verified):** box-1 durable receipt 28/28 at the new digest `f9bd07c2…`
  + A09 anchor reissue table from the citation census (C09-F2 phantom-row
  guard); zero filed-row edits.
- **Evidence:** `reports/round-34/validation.json` acceptance true (exit 0,
  receipt sha256 `ba2fa4dc…`); fleet report `.ufo/reports/round-34/kotodama.md`;
  telemetry closed via `availability-close-34.json` (closes
  `dispatch-declared.json`, sha256 `53e2bb01…`). Two seats (D17, X00) never
  landed; coverage folded by siblings; recorded in `missing_dependencies`.

## 2026-10-19 — Round 35 ADMITTED (regimen 2, loop 1 build 3 of 3)

- **Trigger:** operator regimen (REGIMEN.md); claims C/O/A declared at baseline
  `4a7aede` (`reports/round-35/claims.json`).
- **Route (named deviation):** declared 64 workers on `opencode-go-3`; keys
  3/4/5 returned `402 Insufficient account funds` with zero seats launched
  (three attempts recorded in `telemetry/attempt-availability-{1,2,3}.json`);
  per the live-key rule the batch dispatched on opencode-go key 1 and completed
  64/64. Live-key census recorded: 1-2 funded, 3-5 dry, 6-7 presumed dry.
- **C (verified):** 201 → 211 entries (CM 18→24, MS 19→23) after the mid-wave
  allocation reconciliation (P01 swap-rule; swap chain C01↔C06↔C05 + C03's
  placement recorded in the C receipt material); README revision 2.0,
  sweep-green 211==211; ten entries audited by C13/C14/C17; C04's timekeeping
  alternate routed as a named spare (`reports/round-35/cov/C04-timekeeping-spare.md`).
- **O (verified):** R34-N1 closed — the superseded-row replay now exits 1 with
  the named `E2E-READSET` diagnostic (patch A + controls m13a/m13b/m14a/m14b);
  preserved E2E-DIGEST/E2E-BASELINE paths control-verified; r7 chain exit 0,
  packet `45f57132…`, zero freeze bytes moved. Integration repair recorded: a
  first control insertion that included a driver fence was reverted and
  correctly re-applied.
- **A (verified):** 13-surface assembled audit (`adj/audit-assembled.md` from
  A08 with A07/A11 verifications): zero unfiled bleed; PROVINCE accurate;
  findings F1-F13 owner-assigned.
- **Evidence:** `reports/round-35/validation.json` acceptance true (exit 0,
  receipt sha256 `328e97b3…`); fleet report `.ufo/reports/round-35/kotodama.md`;
  telemetry closed via `availability-close-35.json` (closes
  `dispatch-declared.json`, sha256 `93e205a2…`).

## 2026-10-19 — Round 36 NOT ADMITTED on D (loop 1, position 4; honest stop)

- **Trigger:** regimen; claims D/C/Ca at baseline `ce103bf` (`reports/round-36/claims.json`).
- **Route:** declared hyper/deepseek-v4.1-flash 32w; hyper returned 402 out-of-credits
  on all 32 seats (`telemetry/availability-attempt-1.json`); the REGIMEN-declared
  devin fallback (`devin/deepseek-v4-1-flash-high`) carried the batch 32/32.
- **D (FAILED as declared):** K01's re-read falsified the premise — the
  register-form domain was already closed by rounds 26/27 (argot gate
  derived_pairs=8, law findings=0, both exit 0). Nothing landed under the failed
  claim. Residue routed to a future round with a corrected claim: F-6 counters,
  the `head2` domain, RL-8's era leg, the 13-vs-12 component read-set asymmetry
  (`examples/culture-d4/components/13-register-law.yml` in the packet manifest but
  not the r7 freeze read set — X00/R03's freeze-drift question stays open for the
  next integrate round).
- **C (verified):** the routed timekeeping spare landed (212 total, CM 25);
  README rev 2.1 sweep-green; named defects F1-F5 on file; rev-2.0 row-order
  repair included. Observation: delivered README digest differs from the audit's
  staged prediction with the sweep green — recorded, not smoothed.
- **Ca (verified):** 17-row recount ledger (15 match / 2 dispositioned mismatch).
- **Conformance incident:** a seat briefly executed reports/round-35/run-validation.py
  in-tree during the wave (receipt modified, then byte-identical to HEAD
  `328e97b3…` within ~25 s). The absolute F-C13-1 rule was breached; final state
  clean. Repeat-prevention note re-issued to all future seat prompts.
- **Evidence:** `reports/round-36/validation.json` (exit 1 by design; the receipt
  records the rejection); fleet report `.ufo/reports/round-36/kotodama.md`;
  telemetry closed via `availability-close-36.json`.

## 2026-10-19 — Round 37 ADMITTED (loop 1 position 5 — verify round)

- **Trigger:** regimen; claims Ca/O/A (`reports/round-37/claims.json`); one
  64-worker luna-max batch, 64/64.
- **Ca (verified):** 34-row verify recount of rounds 33-36 (25 match / 5 named
  mismatch / 4 could-not-reproduce); samplers Ca07/Ca08 green.
- **O (verified):** 24-row defect queue; R34-N1 stays closed; new findings
  O10/O12 + the A01 roster defect + the contract-digest lore drift + the
  basename-couples policy question.
- **A (verified):** the freeze-drift question adjudicated — a read-set roster
  defect (13-register-law.yml), pair re-renders faithfully; 334/334 couples
  resolve; r36 rejection preserved (sentinel X04).
- **Integrator repairs (logged against the integrator):** the round-35 README
  apply left two `__E3_PLACEHOLDER__` lines (removed at r37; sweep re-green);
  the r36 receipt's `runner_sha256: null` carried as O10 (filed bytes untouched).
- **Conformance:** one completion subagent (ledger assembly) was
  operator-stopped; the work was completed in-session instead — recorded in
  telemetry. Two seats filed declared-out name variants (recorded in
  missing_dependencies).
- **Evidence:** `reports/round-37/validation.json` acceptance true (receipt
  `616c1c14…`); telemetry closed via `availability-close-37.json`.

## 2026-10-19 — Round 38 ADMITTED (loop 1 position 6)

- **Trigger:** regimen; claims D/O (`reports/round-38/claims.json`).
- **Route (named deviation):** grok 403 out-of-credits on all 32 seats
  (availability-attempt-1.json); devin fallback carried the round: one
  interrupted 32-seat dispatch (22 landed) + one 10-seat completion dispatch =
  32/32.
- **D (verified):** F-6 counters (D01's fenced patch, byte-exact; corrected
  derived_failures formula) + the RL-8 era leg adapted to the argot gate as
  D4L-ARGOT-ERA (X01 T1: the only pipeline-visible, pin-free host/id); selftest
  39/39; live counters 8/8; planted-probe visibility verified; zero pins moved.
- **O (verified):** the manifest-roster guard (O01's patch, sha e5812751…,
  triple-verified pre-application); r7 chain exit 0, packet 45f57132…
  byte-identical; m15a/m15b controls; naming-not-detection recorded.
- **Named findings:** the guard's row-blindness (O03 G5: four asymmetric filed
  rows, not two) filed to the queue's successor; O02/O08 doc defects folded;
  O07's 0-byte fragment recorded.
- **Evidence:** `reports/round-38/validation.json` acceptance true (receipt
  `88db61bf…`); telemetry closed via `availability-close-38.json`.

## 2026-10-19 — Round 39 ADMITTED (loop 1 position 7)

- **Trigger:** regimen; claims C/Ca (`reports/round-39/claims.json`); one 16-seat
  zai glm-flash batch as declared; C05 concurrency-failed and was re-dispatched
  as the completion seat (16/16).
- **C (verified):** verification partition 20 → 24 (total 212 → 216); four
  sourced entries audited 4/4 PASS pre-landing (C05; zero fabrication in 137
  re-resolved citations); README rev 2.2 sweep-green; a seat's stray
  corpus/knowledge/verification/C03-draft.md removed at integration
  (digest-proven provenance).
- **Ca (verified):** the isolation-replay protocol (bwrap mount-namespace,
  Tier A/B/C) addresses O12; Ca02 reproduced all four r37 c-n-r rows
  normalized-identical; the successor ledger re-dispositions them
  reproduced-under-protocol with R01-1's mechanism ruling; the basename-couples
  fallback is documented policy (Ca04 verified; two one-sentence defects filed).
- **Evidence:** `reports/round-39/validation.json` acceptance true (receipt
  `0fefcd56…`); telemetry closed via `availability-close-39.json`.
