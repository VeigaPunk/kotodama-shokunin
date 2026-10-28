# ScoutCoverageSweep — WAVE 1, round 77 — ground sweep for claim C's negative before-state

Base: `211f9526800906e0c585d878d265c37e5e090c15` (all `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin` commands read-only at that rev).
Claim under test (CLAIMS-DRAFT.md L15-20): the base `corpus/knowledge` holds **no** Chinese-language *system-level* account of personal naming — the 姓/名 structure (名 predates 姓; 姓+名 a contact-era acquisition) — and **no** onomastics finite lexeme-inventory classification of Chinese given names.
Staged entry read at `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` (READ-ONLY source tree; no writes).

## Assigned sweeps — commands and raw output

### Sweep 1 — venue/title markers over `corpus/knowledge`
```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -l -E 'lishisuo\.cssn|onomastica\.ijppan|單名與雙名|姓（氏）|名 predates' 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge
(no output)  EXIT:1
```
No file at base names the cssn URL, the onomastica URL, the 單名與雙名 paper, the 姓（氏） pattern, or "名 predates". Confirms the draft's `prints nothing` prediction verbatim.

### Sweep 2 — generation-character patterns over `corpus/knowledge/linguistics`
```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -l -E 'generation.character|輩行|避祖|courtesy name|字 ' 211f9526800906e0c585d878d265c37e5e090c15 -- corpus/knowledge/linguistics
211f9526800906e0c585d878d265c37e5e090c15:corpus/knowledge/linguistics/naming-systems.md   EXIT:0
```
Matching lines (`grep -n` same pattern): only `naming-systems.md:55` and `:98` — both **Japanese** "courtesy name" (azana/gō) rows. Per-pattern `grep -l`:
```
generation.character → EXIT:1 (no match)
輩行                 → EXIT:1 (no match)
避祖                 → EXIT:1 (no match)
字<space>            → EXIT:1 (no match)
```
So in `corpus/knowledge/linguistics` at base: **no** 輩行/避祖/字 Chinese-naming content at all. Caveat on sweep granularity: the `generation.character` pattern requires *adjacent* words, so it did not match "generation-pool character" or "generation names" — the corpus's actual generation-name coverage (below) lives under those spellings plus `corpus/knowledge/civilizations/china-ming.md:181` "Lineage generation characters" (outside this sweep's directory scope). The draft ground doesn't claim absence of generation-name coverage, only of the 姓/名 structure + lexeme-inventory account — unaffected.

### Read — `corpus/knowledge/linguistics/naming-systems.md` at base
Command: `git show 211f…:corpus/knowledge/linguistics/naming-systems.md` (136 lines; sha256 `d972a1d65e7a8fba34f44e1cd57019c175a8ed24671ef95f3e0ea3d1ed9ffb3d`; byte-identical copy staged at `stage/ScoutCoverageSweep/naming-systems.base.md`).

Staged entry's claims (amend file L26-27) vs what the base file already states:

| Staged claim | In base `naming-systems.md`? |
|---|---|
| 姓/名 distinguished | Partially — as slot order only: `:54` "surname first + given + generation-pool character; hereditary surname ~ancient". No 姓/名 terminology, no structural history. |
| 名 predates 姓 | **No.** The file asserts the opposite-flavored "hereditary surname ~ancient" at `:54` with no relative dating of 名 vs 姓. |
| 姓（氏）+名 stable from 春秋戰國 onward; spreads by cultural contact; single/double given-name tracks that spread | **No.** Nothing on historical formation, stability date, contact spread, or 單名/雙名 anywhere in the file. |
| Finite lexeme inventory classification for Chinese given names | **No.** `:61` "name lexicon is a distinct semantic field" (generic; the worked example is Japan's jinmeiyō law, not a Chinese inventory); `:114` lists "plants" as one example source field among seven — a craft heuristic, not an onomastics classification. |
| 88 plant/flower/tree terms | **No.** No count of anything for Chinese given names in the file (or corpus — see attack below). |
| 17 most common lexemes | **No.** |

Base file's actual China coverage: §2 slot-row (`:54`), §6 bìhuì taboo rows (`:94-96`, Wilkinson 2018 + 史记/索隐/正义/集解 primary exhibits + Han Yu 讳辩), surname-law list (`:63`, no China row — China is absent from the state-mandate paragraph). Matches the draft's "covers Chinese *taboo* and surname-first slot behavior, not the structure/inventory claims".

## Falsifier attack — what in base corpus could break "uncovered"

Sweeps run (all at base, scope `corpus/knowledge` unless named):

1. `grep -n -E '單名|雙名|单名|双名|single.name|double.name|monosyllabic name|disyllabic name'` → **no output, EXIT:1**. The single/double given-name axis is entirely absent.
2. `grep -n -i -E 'cssn|onomastica|Ka.u.y.ska|魏斌|predates the surname|predates 姓|before surnames'` → **1 hit**: `synthesis/religion-language-co-evolution.md:203` — an *Onomastica Canadiana* review notice of Schimmel's Islamic Names (Canadian onomastics journal, not `onomastica.ijppan.pl`; about Islamic naming). Not a falsifier.
3. `grep -n -E 'given.name.*(plant|flower|tree)|(plant|flower|tree).*(given.name|lexeme|inventory)|88 |lexeme'` → ~60 hits, all unrelated (conlang lexeme discipline, Yup'ik snow roots, IAU's 88 constellations, `:291` phoneme counts); **zero** connect plants/lexemes to Chinese given names.
4. `grep -l '姓'` over `corpus/knowledge` → 4 files: `china-shang-zhou.md`, `china-song.md`, `japan-yayoi-kofun.md`, `korea-joseon.md`. Inspected the China-relevant content:
   - `china-song.md:176` `| Surname and personal name, 姓 / 名 | Surname normally precedes the personal name in Chinese order | …` — slot-order row only; no historical structure.
   - `china-shang-zhou.md:143` "Stem designations also occur in Shang royal ancestral names; **Xin 辛** in Fu Hao's posthumous designation" — closest base-adjacent datum (Shang royalty had stem names without 姓) but the file never draws the 名-before-姓 conclusion.
   - `korea-joseon.md:139-146` 성 姓/bon-gwan, hangnyeolja 行列字 generation characters, pihwi 避諱 — **Korean** naming system, not the Chinese claim; and it *is* system-level but for Joseon.
   - `china-ming.md:177` "family surname, personal name ming 名, courtesy name zi 字, sobriquet hao 號…" — category list, not structural history.
   - `china-tang.md:154-159`, `china-qing.md:137-141`, `china-han.md:145` — name-category rows (slot order, courtesy names, imperial designations, Manchu hala/gebu). None states the staged claims.
   - `vietnam.md:153` — family-name-first, element counts vary. Not Chinese structure.
5. `grep -n '字' -- corpus/knowledge | grep 'courtesy\|zì\|zi '` → 3 hits: `china-han.md:145`, `china-ming.md:177`, `china-song.md:177` — all 字 zì courtesy-name rows; none covers 姓/名 structure.
6. `grep -i -E 'precede|predate'` ∩ name/surname → only non-pertinent hits (place names, era names, Allah's name, `china-tang.md:154` "Family name precedes personal name" = slot order, not history).
7. `grep -n -E '姓|名' -- linguistics/language-contact.md semantic-fields-lexicon-building.md taboo-strata-lifecycle.md myth-symbol/plant-symbolism.md synthesis/naming-canon-workflow.md synthesis/era-language-staging.md` → **no output, EXIT:1**. The highest-risk adjacent method files carry zero 姓/名 content.
8. `grep -n -E 'generation-pool|generation name|generation.character'` → `naming-systems.md:46,54,114` + `china-ming.md:181` — generation-name coverage exists at slot level (English, no 輩行 terminology); not the staged claim's subject but recorded for completeness.

**No base file falsifies the 'uncovered' ground.** The closest near-misses:
- `china-song.md:176` literally shows 姓/名 but only as a word-order row (English-language, era-scoped).
- `korea-joseon.md:141` is a genuine system-level generation-character account — for Korea, in English.
- `china-shang-zhou.md:143` holds raw evidence compatible with 名-before-姓 (Shang stem names) without asserting it.
- Base `naming-systems.md:54` "hereditary surname ~ancient" is an undated slot claim, arguably in mild *tension* with the staged "contact-era acquisition" framing — the entry will state them as complementary (surname antiquity vs the 姓+名 *combination's* stabilization 春秋戰國), not contradictory; worth a freeze-time check that the amend text doesn't collide with `~ancient` unqualified.

Also verified: `ls-tree -r --name-only … -- corpus/knowledge | wc -l` → **253 files**, matching the draft's "253 → 254" before-count. One Chinese-language source *is* cited at base: `narrative-structure-frameworks.md:4` (`jw.ucass.edu.cn` 叙事学 syllabus) — Chinese-language but narratology, not naming.

## Verdict

**Ground HOLDS at base** (`211f9526`). Every assigned sweep and every falsifier probe confirms: no cssn/onomastica venues, no 單名與雙名 or 姓（氏） material, no Chinese-language system-level naming account anywhere in `corpus/knowledge`, and no finite lexeme-inventory classification of Chinese given names. Base `naming-systems.md` covers Chinese naming at slot level (order, generation-pool, taboo) in English — exactly the gap the staged entry names.

Caveats for the counter authors: (a) `generation.character` is an under-broad probe — use `generation` alone if a GROUND leg re-runs it; (b) sweep 2's directory scope missed `civilizations/` — the era-file slot rows above are already-covered content the draft's "taboo/slot behavior" wording implicitly allows; no need to widen the claim.

## Receipts / notes
- `stage/ScoutCoverageSweep/naming-systems.base.md` — base file extract, sha256 `d972a1d6…9ffb3d` (matches live `git show` output).
- Tooling: none installed (git + find only; no installs this seat).
- No LSP server consulted (not applicable — pure git-grep corpus recon, not symbol tracing).
