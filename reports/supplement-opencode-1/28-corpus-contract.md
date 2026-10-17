# 28 — corpus contract scout: 179 entry headers at `fe34faa` (supplement-opencode-1)

- Role: SCOUT (read-only corpus census + bounded source rechecks). Lane-local report; non-canon; author-side evidence only.
- Baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404` (`git rev-parse HEAD` at start; worktree clean except untracked `reports/`).
- Date: 2026-10-17 (UTC timestamps inline).
- Write scope: this file only (plus scratch under `reports/supplement-opencode-1/scratch/28-corpus-contract/`). No entry, README, fleet rule, packet, or frozen artifact was modified.
- Provenance of every count below: the command/census procedure is stated; the raw per-file census is `reports/supplement-opencode-1/scratch/28-corpus-contract/header-census.txt` (scratch, not durable evidence).

## 1. The contract under audit

- Fleet `CORPUS.md` (read-only, `/home/vgpnk/Projects/shokunin/CORPUS.md`), Layout section: "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`".
- Lane `corpus/README.md` revision 1.1 (sha256 `462ac120f43ccba7787ad1b98c494122d8a26b6959bc195decc09cc472ca7d00`, identical at baseline and worktree): "Every entry carries provenance (`- sources:`) and coupling (`- couples:`)".
- Lane gate `tools/gates/provenance-audit.py` (sha256 `4aaea6e98b9776922708692e6e0f38f76ef7323e3c748cbdf82c789eb77e1e7a`): `FIELD_NAMES = ("topic", "sources", "couples")` at line 72, `FIELD_RE = re.compile(r"^- (topic|sources|couples):...")` at line 73. The gate does not test `verified-at` or `recheck` anywhere (`grep -n 'verified-at\|recheck' tools/gates/provenance-audit.py` → no hits; the only `tools/` files containing those strings are two frozen round-3 input snapshots).

So the *operational* contract in this repo is the opening `topic/sources/couples` triple, while the *fleet-document* contract is the `source/verified-at/recheck` profile. This report measures the gap; it does not rule on which text should change (see §6).

## 2. Exact counts (all 179 files)

Counting command (one-off Python over the 179 files, read-only; per-file output in the scratch census):

```
python3 - <<'EOF'   # top block = lines before the first '## ' heading; "structural" = line starts with "- key:"
… fields(): first "- key:" plus any "; key:" later on the same line …
EOF
```

- Knowledge files at baseline: **179** — `find corpus/knowledge -name '*.md' -type f | wc -l` (dirs: civilizations 94, synthesis 24, culture-material 16, linguistics 16, myth-symbol 16, verification 13).
- Files carrying the legacy opening triple `topic`+`sources`+`couples`: **179 / 179** (each appears exactly 179 times).
- Files whose top block opens with the CORPUS.md trio as **dedicated lines** (`- source:` / `- verified-at:` / `- recheck:` at line start): **1 / 179** — `synthesis/glossary-registry-format.md` (lines 6, 7, 8).
- Files satisfying CORPUS.md as **file-level content** including bundled clauses after the opening: **9 / 179** carry a `source:`-form entry anywhere; **14 / 179** carry `verified-at:`; **13 / 179** carry `recheck:`.
- Location split for the modern fields:
  - top-level dedicated lines, before the first heading: `- verified-at:` **8** files (`china-shang-zhou:5`, `japan-heian:5`, `moche:5`, `rome:5`, `ryukyu:5`, `coupling-model:5`, `glossary-registry-format:7`, `gate-frozen-run-standard:5`); `- recheck:` **7** files (same set minus `gate-frozen-run-standard`).
  - inside the body (after a heading): `verified-at`/`recheck` bundles at `burma.md:12` and `mali-songhai.md:14` (one line: `- source: …; verified-at: 2026-10-17; recheck: …`); `amazigh-berber.md:16–18` (`- source:` line 16, `- verified-at:` 17, `- recheck:` 18, after the "Sources and editions" heading); `myth-consistency-gate.md:9–11`, `citation-format-and-source-registry.md:15–17`, `provenance-audit-ledger-format.md:9–11`, `gate-frozen-run-standard.md:18`, `coupling-model.md:14–15`.
  - incidental `source:`-form lines in body prose: `egypt-ancient.md:55,165`, `maya-classic.md:63` (not header fields).
- Per-file shape distribution (structural keys anywhere in the file, legacy triple always present):

| Shape | Files |
|---|---|
| `topic/sources/couples` only | 162 |
| + `source/verified-at/recheck` (complete profile) | 7 |
| + `verified-at/recheck` | 6 |
| + `source` only | 2 |
| + `verified-at` only | 2 |
| **Total** | **179** |

- Fields the legacy triple does **not** replace-rename: no entry drops `- sources:`; the singular `- source:` is purely additive (present in 9 files, never the sole sourcing field).

Command equivalents for the headline numbers:

```
find corpus/knowledge -name '*.md' -type f | wc -l                      # 179
grep -rl '^- sources:' corpus/knowledge --include='*.md' | wc -l        # 179
grep -rl '^- source:'  corpus/knowledge --include='*.md' | wc -l        # 7 (line-start form; 2 more inline)
grep -rl '^- verified-at:' corpus/knowledge --include='*.md' | wc -l    # 12 (line-start anywhere; 8 top-level)
grep -rl '^- recheck:' corpus/knowledge --include='*.md' | wc -l        # 11 (line-start anywhere; 7 top-level)
grep -rln -E '^- source:.*verified-at:.*recheck:' corpus/knowledge --include='*.md'  # 2 (burma, mali-songhai)
```

## 3. Sampled evidence (representative, quoted from baseline)

- Legacy-only, canonical opening — `civilizations/slavs-early.md:2–4`: `- topic: …`, `- sources: Schenker (1995); Derksen (2008); …`, `- couples: Language—…; myth/symbol—…; era/costume—…`.
- Complete modern profile — `synthesis/glossary-registry-format.md:6–8`: `- source: Standards and scholarship identified in §9; …` / `- verified-at: 2026-10-17 — TEI and RFC text checked; …` / `- recheck: On schema migration, language-tag registry change, …`.
- Partial modern profile, correct but non-contract position — `civilizations/rome.md:5–6`: `- verified-at: 2026-10-17; targeted ancient passages, OCRE coin record, …` / `- recheck: before importing an exact inscription, garment reconstruction, …`.
- Bundled clause form — `civilizations/burma.md:12`: `- source: the keyed bibliography below; verified-at: 2026-10-17; recheck: before using an exact inscription date, …`.
- Off-vocabulary header lines that current tooling neither requires nor reads: `verification/gate-frozen-run-standard.md` opens with `topic/sources/couples/follows/canon/verified-at`; `civilizations/mesoamerica-primary-sources.md` opens with a `revision:` line before `topic`.

## 4. Aggregate drift found while sampling (same baseline, read-only)

- `corpus/README.md` revision 1.1 index rows: **178** (`grep -c '^- \`' corpus/README.md`), while the tree holds **179** entries; the missing row is `civilizations/africa-primary-sources.md` — `for f in corpus/knowledge/civilizations/*.md; do grep -q "^- \`$(basename $f)\`" corpus/README.md || echo NOT-IN-INDEX: $f; done` (a new index row is itself a claim per fleet CORPUS.md, and this one is absent, not wrong).
- README section counts total 178 (16+16+16+24+13+93); the civilizations header says `(93)` while the directory holds 94 files. This is prior-round index debt, reported here as scope drift, not corrected in this wave.

## 5. SOURCE-RECHECK audits — assigned entry: `corpus/knowledge/civilizations/slavs-early.md`

Entry chosen because it is one of the five carry-listed civ entries (39 flag-lines → round 5, per `corpus/lessons/round-3-triage/orchestrator-direct.md`) and its flagged claims are couplings, not isolated bibliography facts.

- `entry_sha256_before` (worktree and baseline identical at check time, 15:36 UTC): `e9c2fb815e18f0040268b15887c4f6eaf778e1bd62fd54a817b283eced1bed0b`.
- No erratum was appended by this scout: nothing sampled proved factually wrong or missing in the entry, so I added no bytes to the entry.
- **Concurrent change noticed after the audit pass (not mine):** the live entry was modified at 15:41 UTC by another supplement worker — 4 appended lines starting `## Erratum appended by source-recheck, 2026-10-17 (prior text preserved)` (now sha256 `b3c2ef4a103db9f9f53a22e3e5c437f28ad09be7797f6464b7214cc2c163250d`; diff vs baseline: 4 insertions, prior bytes preserved). It notes the Slovak/Polish/Sorbian/Russian scissors-noun convergence around the form and keeps the `(to-verify)` flags. My S4 row below grades the baseline text I audited; the appended erratum is sibling work, recorded here for calibration but not authored or verified beyond that notice.

Audit JSON block (also machine-readable in the block below this report's prose):

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "corpus/knowledge/civilizations/slavs-early.md",
  "entry_sha256_before": "e9c2fb815e18f0040268b15887c4f6eaf778e1bd62fd54a817b283eced1bed0b",
  "checked_at_utc": "2026-10-17T15:39:47Z",
  "audits": [
    {
      "id": "S1",
      "claim": "Birch-bark letter Novgorod 752 is a fragmentary love letter; conditional date 1100-1120 with a possible backward shift, stratigraphic 1080s-1100s (preferably 1080s), extra-stratigraphic preference first forty years of the 12th c.; its record carries R. Kovalev and Jos Schaeken/Brill (2019) translations.",
      "entry_locator": "civilizations/slavs-early.md:77-80",
      "source_url": "https://gramoty.ru/birchbark/document/show/novgorod/752/",
      "retrieval_status": "retrieved (HSE/Institute of Slavic Studies birch-bark corpus record, full page)",
      "source_locator": "record fields: 'Условная дата', 'Стратиграфическая дата', 'Внестратиграфическая дата', 'Жанр: частное письмо', translations headed 'English translation (R. Kovalev)' and 'English translation (© Jos Schaeken / Brill Publishers, 2019)'",
      "source_excerpt": "\"Условная дата 1100‒1120 (с вероятным смещением назад)\"; \"Стратиграфическая дата 1080-е – 1100-е гг. [предпочт. 1080-е].\"",
      "verdict": "supported",
      "basis": "All three date fields and both translation attributions match the entry's paraphrase; the letter's opening ('to you three times ... I treated you like a brother') matches the entry's genre characterization.",
      "access_limit": "Date fields read from the live catalog page 2026-10-17; archaeological/linguistic date argumentation inside НГБ X not inspected."
    },
    {
      "id": "S2",
      "claim": "The Rod/rozanicy problem rests on East Slavic Christian denunciations whose textual anchors must be identified before citing offerings: the primary witness is the 'Slovo svjatogo Grigorija' compilation, whose original is lost and whose dating is disputed (Sreznevskij and Galkovskij: late 13th - early 14th c.; Mansikka's lower bound via 'Slovo nekoego khristoljubca'; Anichkov suggested the 1060s).",
      "entry_locator": "civilizations/slavs-early.md:126 (to-verify: recension/witness/dating anchors); context :124 (denunciation framing)",
      "source_url": "https://ru.wikipedia.org/wiki/Слово_святого_Григория,_изобретено_в_толцех",
      "retrieval_status": "retrieved (article wikitext via ru.wikipedia.org API, revid 154005288, 2026-07-18T12:28:53Z)",
      "source_locator": "sections 'Датировка' and 'Текстология/Происхождение' (wikitext, near character offsets 1594, 2241-2560)",
      "source_excerpt": "\"Первоначальный текст памятника не сохранился, но ... его лучше всего передаёт список в Паисиевском сборнике\"; \"Срезневский и Гальковский датировали сочинение концом XIII — началом XIV века. Мансикка считал, что нижней датой ... Аничков предполагал ... 60-х годах XI века\".",
      "verdict": "supported",
      "basis": "The retrieved passage shows the manuscript-witness problem and the exact disputed dating anchors the entry demands before citations; the philological cautions (Rybakov's over-reading vs Anichkov/Klein) also appear in the retrieved article.",
      "access_limit": "Wikipedia article is a tertiary digest of printed scholarship; its own citations (Буланина 1987, Клейн 2004, Зубов 1995/1998) were not fetched in full. This supports the entry's caution, not the eyewitness homily text."
    },
    {
      "id": "S3",
      "claim": "Reconstructed Proto-Slavic stages have 'no contemporary corpus of Proto-Slavic manuscripts', and invented ritual distinctions must be labeled inventions - the entry's language/myth/dress coupling rule (do not derive a uniform costume from a root word).",
      "entry_locator": "civilizations/slavs-early.md:25 (era-staging table row 1) and :187 (costume workflow rule)",
      "source_url": "https://ru.wikipedia.org/wiki/Слово_святого_Григория,_изобретено_в_толцех",
      "retrieval_status": "retrieved (same wikitext fetch as S2)",
      "source_locator": "infobox/date range and textology sections of the OR compilation",
      "source_excerpt": "\"Дата=XI—XIV века\"; \"Рукописи=4 списка\"; Paisievskij sbornik (Kirillo-Belozersk collection no. 4/1081) as best witness",
      "verdict": "unresolved",
      "basis": "The retrieved material covers only Christian literary witnesses (11th-14th c. manuscripts) and does not test how far the surviving Slavic corpus can validate reconstructed lexicon; a negative claim about Proto-Slavic attestation needs its own sweep, which this scoped recheck did not perform.",
      "access_limit": "No full-text source on Proto-Slavic attestation was retrieved; the coupling rule remains a design convention supported by general method, not by a fetched passage."
    },
    {
      "id": "S4",
      "claim": "The noznici label remains unidentified; do not silently correct it to rozanicy or attach a garment or priesthood to it (entry states this as its own unresolved item, not a positive fact).",
      "entry_locator": "civilizations/slavs-early.md:127-128, :197",
      "source_url": "https://ru.wikipedia.org/wiki/Рожаницы",
      "retrieval_status": "multi-source sweep: ru.wikipedia search API (0 hits, 2026-10-17), ru.wikisource search API (0 hits), ru.wiktionary/ru.wikipedia insource searches (0 hits), en.wikipedia insource (1 unrelated hit), HSE birch-bark corpus record for Novgorod 752 (no such term); dedicated rožanicy article retrieved",
      "source_locator": "ru.wikipedia.org article 'Рожаницы' (retrieved 2026-10-17), textual/lexical sections; search-API result sets",
      "source_excerpt": "\"В церковнославянских переводах византийских поучений ... упоминается «рожацная (рожаничная) трапеза»\" — the retrieved article treats rozanicy/rod but names no 'noznici'.",
      "verdict": "unresolved",
      "basis": "No retrieved or indexed source defines or attests 'noznici' as an early Slavic ritual/deity/dress term; the entry's unresolved marking is not contradicted, but neither the homily's own wording nor a scholarly identification was retrieved. An adjacent supplement worker later appended an erratum (2026-10-17, after this audit) linking the form to the ordinary Slavic scissors noun (Slovak noznice, Polish nozyce, Russian noznitsy); that lexical convergence does not by itself identify the homily referent, which stays unresolved.",
      "access_limit": "Absence from public encyclopedias/indexes is weak negative evidence only; the term may appear in printed manuscript editions not indexed online. Searches were resumed-per-URL per the fleet rule on absence claims and remain unresolved."
    },
    {
      "id": "S5",
      "claim": "Dvoeverie is conventionally glossed 'double belief'/'double faith', with the shorthand dvoverie not concealing which language/historical usage is meant.",
      "entry_locator": "civilizations/slavs-early.md:107",
      "source_url": "https://ru.wikipedia.org/wiki/Двоеверие",
      "retrieval_status": "retrieved (ru.wikipedia disambiguation page and en.wikipedia 'Folk Orthodoxy', full pages)",
      "source_locator": "ru.wikipedia 'Двоеверие' items; en.wikipedia 'Folk Orthodoxy' §Etymology/definition",
      "source_excerpt": "en.wikipedia: \"The Russian-language term dvoeverie (\\\"dual faith\\\", двоеверие) appeared during the Middle Ages, used in sermons directed against Christians who continued to worship pagan deities.\"",
      "verdict": "unresolved",
      "basis": "The gloss itself matches, but both retrieved pages are encyclopedia entries; no scholarly source establishing the term's date or usage history was retrieved. Recorded as agreement-by-tertiary-source, not confirmation.",
      "access_limit": "Full scholarly treatments (e.g. Levin's article literature) were not fetched; DV-04 remains a candidate for a future archival recheck."
    }
  ]
}
```

Summary of audit verdicts: supported 2 (S1, S2), unresolved 3 (S3, S4, S5), contradicted 0. No entry bytes changed. Audit coverage is partial by design: 2 of the entry's 4 live `(to-verify)` lines (lines 126 and 127–128) were targeted; line 197 is the same class as 126–128.

## 6. Bounded correction plan (no bulk rewrite)

The 179-entry gap between the fleet CORPUS.md profile and the lane's operative header triple is a **normative choice**, not a backlog to silently burn down — a bulk rewrite of 170+ legacy headers would risk exactly the byte-rewriting and unverified-claim churn the fleet's append-only rules exist to prevent. Owner of the decision: the parent/integrator for fleet-file changes; the lane for its own ground documents. Concrete, checkable steps, each with a falsification condition:

1. **Declare the lane profile where a reader looks first.** Append a dated note (next productive wave, lane-authorized edit) to `corpus/README.md` stating: for this repo the operative entry contract is the gate-enforced `topic/sources/couples` triple, with `source:`/`verified-at:`/`recheck:` as an additive profile used by entries that performed a dated recheck. Falsified if `provenance-audit.py` FIELD_NAMES changes to include the modern fields (then the note and the CORPUS.md reading must be re-synced in the same wave).
2. **Route the fleet-text question to the integrator, do not edit it.** File in the round notes / L0: fleet `CORPUS.md` says every `knowledge/` entry opens with `source:/verified-at:/recheck:` (observed 1/179 in dedicated-line form, 9/179 with any `source:` clause), while the lane's gate requires `topic/sources/couples` (179/179). The integrator either amends CORPUS.md's sentence to a profile-inherits-its-gate rule or declares the lane non-conformant. Falsification: the two contract texts are shown to be equivalent under some reading (interpreter to cite the passage).
3. **Optional, small, verified-only migration.** Only entries that can honestly provide a dated `verified-at` should gain the dedicated lines — i.e. the 8 top-level `verified-at` files and the 12 files with `recheck`/bundle material, one edit per file, each edit logged with the recheck date it actually performed. Do not add empty or boilerplate `verified-at:` to the other ~160 entries; a placeholder date is a fabricated verification. Falsification: any edited file cannot cite the check it claims.
4. **Index debt fix.** Add the missing `africa-primary-sources.md` row to `corpus/README.md` civilizations section and reconcile the `(93)` header with the 94 files; owner: lane (README is lane-owned; do not touch generated packets or frozen artifacts). Falsification: `grep -c '^- \`' corpus/README.md` still below 179 after the fix, or the section count still mislabeled.
5. **Recount command for any future wave.** `.ufo`/lane reviewer can re-derive this report's numbers with the four `grep -rl … | wc -l` lines in §2 plus the shape table procedure; a recount returning different numbers means this report is stale, not that the contract changed silently.

## 7. Limits and unresolved items

- Everything here is author-side evidence at baseline `fe34faa`; no commit was made, no sibling repo or fleet file was written, and no frozen round-3/4 artifact was touched.
- The audit row S4's zero-hit searches are weak negative evidence (see access_limit); S3 and S5 remain unresolved rather than converted to confirmation. Two audits (S2, plus the S1/S3 pair) exercise the language/myth/era/dress coupling question rather than isolated bibliography facts; all five rows are recorded unresolved-or-supported, with no invented sources or page numbers.
- Sampled evidence in §3–§4 is representative, not exhaustive: the full per-file locator table lives only in scratch (`header-census.txt`, non-durable). If the parent wants a durable per-file table, it should be regenerated into an assigned durable path.
- No numeric axis score is claimed by this report; the freshness/calibration moves of this wave are scored by the parent from `claims.json` observables.
