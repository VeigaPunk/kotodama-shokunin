# CritGround — WAVE 2, round 77 — attack on claim C GROUND (negative before-state)

Base: `211f9526800906e0c585d878d265c37e5e090c15` (all `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin` reads at that rev; nothing mutated).
Item attacked: whether claim C's ground — "**no Chinese-language system-level account** of personal naming … in corpus/knowledge at base" (CLAIMS-DRAFT.md L10; restated in staged amend `w1/drafts/.../naming-systems.amend-2026-10-23.md` L10) — overstates absence given the China civilization slot rows, per the seat brief.
W1 artifact re-verified: `w1/ScoutCoverageSweep.md`.

## Verdict

**GROUND HOLDS. No falsifier found.** Under both readings of "Chinese-language system-level account" — (a) an account *written in Chinese*, (b) a *system-level account of Chinese naming* — the strongest local counterexamples fail. The China era files do carry a genuinely broader Chinese-name surface than W1's slot-row summary suggests (full inventory below), but every piece of it is (i) English-language, (ii) slot-level naming practice per era, (iii) silent on the three staged propositions (名 predates 姓; 姓+名 a contact-era acquisition; a finite/counted given-name lexeme inventory). The claim's own parenthetical — "the 姓/名 structure (名 predates 姓; 姓+名 a contact-era acquisition) and the onomastics literature's finite lexeme classification" — defines the absent object precisely enough that the slot rows cannot fill it. Not a tradeoff for the judge: the absence holds as stated.

## Re-run of W1's assigned sweeps (byte-for-byte reproduction)

All commands executed in this seat; exit codes as printed. `REV` = `211f9526800906e0c585d878d265c37e5e090c15`.

| # | Command (abridged; full text in W1 report) | W1 result | W2 re-run |
|---|---|---|---|
| 1 | `git grep -l -E 'lishisuo\.cssn\|onomastica\.ijppan\|單名與雙名\|姓（氏）\|名 predates' REV -- corpus/knowledge` | no output, EXIT 1 | **identical**: no output, EXIT 1 |
| 2 | `git grep -l -E 'generation.character\|輩行\|避祖\|courtesy name\|字 ' REV -- corpus/knowledge/linguistics` | `naming-systems.md` only, EXIT 0 | **identical** |
| 3 | `git grep -n -E '單名\|雙名\|单名\|双名\|single.name\|double.name\|monosyllabic name\|disyllabic name' REV -- corpus/knowledge` | EXIT 1 | **identical** |
| 4 | `git grep -n -i -E 'cssn\|onomastica\|Ka.u.y.ska\|魏斌\|predates the surname\|predates 姓\|before surnames' REV -- corpus/knowledge` | 1 hit: `synthesis/religion-language-co-evolution.md:203` (Onomastica **Canadiana** review of Schimmel's *Islamic Names*) | **identical** — still the sole hit; not a falsifier (Canadian journal, Islamic naming) |
| 5 | `git grep -l '姓' REV -- corpus/knowledge` | 4 files: `china-shang-zhou.md`, `china-song.md`, `japan-yayoi-kofun.md`, `korea-joseon.md` | **identical** |
| 6 | `git ls-tree -r --name-only REV -- corpus/knowledge \| wc -l` | 253 | **identical: 253** |

Probe 7 (adjacent method files `language-contact.md`, `semantic-fields-lexicon-building.md`, `taboo-strata-lifecycle.md`, `plant-symbolism.md`, `naming-canon-workflow.md`, `era-language-staging.md` for 姓/名): **no output, EXIT 1** — identical to W1.

Probe 8 (`generation-pool|generation name|generation.character` plus my widened alternates `hangnyeolja|行列字|輩分字|字輩|班輩`): base hits = `naming-systems.md:46,54,114`, `china-ming.md:181`, `korea-joseon.md:141`. W1's caveat confirmed: `generation.character` alone misses `china-ming.md:181` ("Lineage generation characters … `(to-verify)`"); a GROUND leg should use `generation` or the widened pattern — recorded, not a defect in the claim.

## The strongest counterexample, attacked and defeated

**Candidate A — `corpus/knowledge/civilizations/china-shang-zhou.md:167`** (the strongest text in the whole corpus):
> "Do not impose a later, fully regularized **xìng 姓 / shì 氏** distinction on every inscription; exact reconstruction of a named individual's affiliation remains (to-verify)."

Why it fails as a falsifier, three independent reasons:
1. **Wrong distinction.** It is the archaic 姓 (ancestral surname) vs **氏** (lineage/branch name) caution — not the 姓 vs **名** (given name) structure the claim names. The amend's propositions (名 precedes 姓; the 姓（氏）＋名 *pairing* stabilises 春秋戰國 onward; contact spread) concern the *fusion of surname slot with given-name slot*. `:167` says the 姓/氏 contrast is itself "later, fully regularized" — which if anything is *compatible* with the staged periodization, not evidence the corpus already states it.
2. **Wrong register.** It is a negative caution ("do not impose"), not a positive account of any structure. The base names the gap; it does not fill it. Same file, same section: `:163` "do not model them [Fù Hǎo / Mǔ Xīn] as given name plus a modern hereditary surname" — a don't, not a system.
3. **Wrong language, if the claim is read literally.** It is English prose glossing two graphs. Not a Chinese-language account.

**Candidate B — the China-era name-row set as a collective "account".** Full inventory at base (all six `china-*.md` files swept for every CJK-bearing line):

- `china-shang-zhou.md`: `:138-143` gānzhī stems/branches with stem designations in Shang royal ancestral names (Xīn 辛 in Fu Hao's posthumous designation); `:163` Fu Hao/Mu Xin ≠ given+surname caution; `:166` birth-order Bó/zhòng/shū/jì; `:167` 姓/氏 caution (above).
- `china-han.md:144-148`: `董｜仲舒`/`公孫｜弘` surname|given segmentation with explicit "**multi-character personal names** both occur" (closest base datum to 單名/雙名 — but a segmentation note, not a historical single/double-name transition account); zi 字 courtesy names; posthumous 孝武; era titles 建元/元封/太初.
- `china-tang.md:154`: family-name-first slot order, compound surnames (Shangguan Wan'er).
- `china-song.md:176-178`: 姓/名 slot order; 字 zì; 號 hào.
- `china-ming.md:177-182`: ming 名/zi 字/hao 號/office/kin/nickname field split; Ma Huan worked example; reign-name ≠ personal name; generation characters `(to-verify)`; women's `surname + shi 氏` record convention (氏 as post-marital designation — different sense from archaic lineage 氏).
- `china-qing.md:137-143`: surname+personal name + courtesy/literary names; Manchu *hala* clan vs *gebu* personal name; Hongli/Qianlong/Gaozong slot example; name worksheet.

Collective verdict: this is a **per-era slot inventory** — which slots existed and how to keep them apart in a database — assembled in English across six files, with zero historical derivation of the 姓/名 structure and zero counted lexemes. "System-level" in the claim's sense (the structure's own history + a classifiable finite inventory) is exactly what is absent. A hostile reading that counts slot-taxonomy as "system-level" would also have to count Rome (`rome.md:124-130` praenomen/nomen/cognomen table), Bali, Byzantium, Sogdian etc. — which share the identical slot-table genre — collapsing the phrase into meaninglessness. The claim survives because its object is specific.

**Candidate C — `korea-joseon.md:139-146`** (성 姓/bon-gwan, hangnyeolja 行列字 generation characters, pihwi 避諱, jokbo 族譜 registers, siho/myoho): a real system-level naming account — **Korean**, in English, Joseon-scoped. Not Chinese naming; not Chinese-language.

**Candidate D — Chinese-language sources already cited in corpus/knowledge at base** (none falsifies; complete list): `heritage-taxonomy-models.md` (ihchina.gov.cn 国家级名录 registry), `.amend-2026-10-24-r13.md` (same S874), `calendar-festival-systems.amend-2026-10-24.md` (openstd.samr.gov.cn GB/T 33661-2017), `worldbuilding-setting-practice.amend-2026-10-23.md` + `narrative-structure-frameworks.md` (chinawriter.com.cn interviews 三九音域/爱潜水的乌贼 — narratology/web-fiction craft), `china-song.md:198-199` (Fujian Museum excavation report; Zhang Mingwu 2023 Ru-glaze colorimetry — cited for glaze terminology), plus zh.wikisource primary texts (Zhouli, Shiji, Hanshu, Yili, Ming shi, Yingya Shenglan — cited for ritual/dress/mourning/Malacca vocabulary). Command: `git grep -n -P '[\x{4e00}-\x{9fff}]' REV -- corpus/knowledge | grep -oP 'https?://[^ )]+'` surveyed; no Chinese-hosted or Chinese-language *personal-naming* account anywhere. Confirms the literal "Chinese-language" limb.

**Candidate E — `kinship-terminology.md:16,84`**: Feng (1937) + Freedman (1958) cited; tang 堂/biao 表 surname-lineage exogamy. Chinese *kinship* structure in English scholarship — touches the surname lineage, teaches nothing about 名 or name lexicons.

**Candidate F — `synthesis/taboo-euphemism-lifecycle.md:125-137`**: "Reference capsule: imperial Chinese name avoidance" — separates surname/personal name/reign title/temple name/posthumous designation as *taboo-coverage categories* (English, Wilkinson 2022-grounded). A naming *ecology* note for taboo mechanics; not the structure's history. Adjacent corroborating silence: `sogdian-silk-road.md:167` defers Chinese-form names/Kang-An "nine clans" surname mapping to a `(to-verify)` dossier that does not exist — an explicit acknowledgment of the same gap.

**Residual checks:** `japan-yayoi-kofun.md:158-159` uji 氏/kabane 姓 is Japanese; `vietnam.md:128-162` is Vietnamese (姓-order + miếu hiệu/niên hiệu + name taboo); `turkic-steppe.md:162` "Ashina in Chinese accounts" is a transcription note; `era-periodization-models.md` covers nianhao era *names*, not person names; `naming-canon-workflow.md` is process-generic (LGPN Greek inventory is its worked example); `toponymy-place-names.md` owns place-name romanization only. Extra vocabulary probes `昭穆|行第|排行|譜名|族譜|宗譜|派語|小名|乳名|諱名|廟號` → hits only in `korea-joseon.md:143,145` and `vietnam.md:128` — none Chinese-named.

## Noted defects (fixable, not falsifying)

1. **W1 sweep-2 scoping** already self-flagged: `corpus/knowledge/linguistics`-only; `china-ming.md:181` generation coverage lives outside it. Harmless to the claim (generation coverage is not in the claim's scope) but any GROUND leg re-run should widen to `corpus/knowledge` with `generation` unanchored.
2. **W1's "no China row" paraphrase for `naming-systems.md:63`** (surname-law list): accurate — China is indeed absent from the state-mandate paragraph — but the file's §6 taboo rows *are* China rows; wording should stay "no China row in the surname-*law* list" to avoid a hostile misreading.
3. **Amend `ground:` line (staged L10) is verifiable and narrower than the CLAIMS-DRAFT paraphrase** ("no file … carries a system-level account of 姓/名 succession or a counted Chinese name lexicon") — the counter's GROUND leg should check this narrower statement; it is the version the evidence supports.

## Commands / raw outputs (verification trail)

Every read was `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin {ls-tree,grep,show} 211f9526…` — read-only. Key raw results reproduced above; full CJK dumps of all six `china-*.md` files were enumerated in-session via `git grep -n -P '[\x{4e00}-\x{9fff}]' REV -- corpus/knowledge/civilizations/china-*.md` (complete output reviewed; the naming-relevant lines are quoted verbatim above). Working tree files read: `CLAIMS-DRAFT.md`, `w1/ScoutCoverageSweep.md`, `w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`, `w2/spec.json`.

## Bottom line for the counter authors

The ground's wording is aggressive but not overstated: China era files provide slot rows, not a system-level account, in English; the corpus's only Chinese-language documents are off-topic. Impacted axes: none — GROUND leg should pass if the counter checks the amend's narrower `ground:` statement (per-era slot inventory present ≠ system-level account) rather than a phrase-match on "Chinese-language". Smallest safe correction (optional, belt-and-braces): in the frozen ground, append the two sentences "China era files (`china-*.md`) carry per-era name-slot rows including a 姓/氏 regularization caution at `china-shang-zhou.md:167`; none states 名-before-姓, a fusion date/channel, or a counted lexicon." — immunizes the ground against exactly the attack this seat ran. Not required for the claim to hold.

## Receipts

- No installs (git + grep only; pacman not run).
- No fixture repos created; no scratch dir used (`/fast/scratch/hyaku/kotodama-r77/CritGround` never created — nothing to clean).
- Writes: this report only. No fleet/lane production files touched; no git/jj mutations.
