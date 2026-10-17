# 27 — claims critic: count-based quality claims, marker-deletion freshness, empty reviews, and the admission bar

- **Wave:** `supplement-opencode-1` (supplemental native-OpenCode swarm; NOT a numbered GLM round)
- **Baseline:** `fe34faaafbe0add59ff68827a0df6c5782a72404` (HEAD at start; `git status` clean except untracked `reports/`)
- **Role:** claims critic + SOURCE-RECHECK (27). Author-side evidence only: no `[x]`, no rank promotion, no corpus bytes edited.
- **Checked at (UTC):** 2026-10-17T15:38:24Z
- **Assigned writes:** this file only. The source-recheck JSON required by the round contract is embedded below as a fenced `json` block (§6) because the critic lane owns exactly one path; the parent should split it to its own file at integration if the wave's sink layout requires it.
- **Target of critique:** `reports/supplement-opencode-1/claims.json`, committed `LOG.md` round entries (rounds 0–4), `SCORECARD.md`, `corpus/README.md`, `tools/gates/frozen/**`, `corpus/lessons/round-4-audit/**`, `examples/culture-d2/reviews/**`.

**Method.** Every number below was re-derived from committed bytes at `fe34faa` with the commands printed in §1.4, not quoted from `LOG.md`. Where a committed claim reproduces, it is marked `REPRODUCED`; where it does not, the reproduced value and the counting basis are given. Verdict vocabulary: `REPRODUCED` / `NOT REPRODUCED` / `UNRESOLVED`.

---

## 1. What actually reproduces at the baseline (credit first)

| Committed claim | Source | Re-measured value | Verdict |
|---|---|---|---|
| `knowledge_entries: 179` | claims.json `baseline` | 179 `*.md` under `corpus/knowledge/` | **REPRODUCED** |
| `naming_findings {NAME-NEAR 6, PHON-CODA 1, PHON-INVENTORY 10, CROSS-HOLD 1}` | claims.json `baseline` | counts identical in `tools/gates/frozen/round-4/naming-collision-gate.out` (18 finding lines) | **REPRODUCED** |
| `d2_packet_sha256: d5fb4088…` | claims.json `baseline` | `sha256(git show fe34faa:examples/culture-d2/packet.d2.yml)` = `d5fb408871dcb985…`, 154607 B | **REPRODUCED** |
| `registered_gate_selftests_passed: 7` | claims.json `baseline` | re-ran `for g in tools/gates/*.py; do python3 $g --selftest; done` → **7/7 exit 0** | **REPRODUCED** (re-executed, not quoted) |
| Evidence ordering, round 4 | PROTOCOL §Evidence standard | `frozen/round-4/*.out` mtime 15:18:14Z **before** commit `fe34faa` 15:19:35Z | **no future-dating defect** |
| QUALITY.md header structure | `QUALITY.md` §1/§3 | 179/179 entries carry `- topic:`, `- sources:`, `- couples:`; 179/179 mention calibration; **0 entries couple nothing** | **REPRODUCED** |
| Ledger counts r1/r2 | LOG r1/r2 | `corpus/lessons/round-1-triage` = 42 files, `round-2-triage` = 43 files | **REPRODUCED** |
| Round-1 decision totals | LOG r1 ("503 / 416 / 64") | per-token line counts: CONFIRM 503, DOWNGRADE 416, EXCISE 64 | **REPRODUCED as per-token counts** (see §2.2 for what breaks) |

So the fresh-looking parts of the wave's baseline block are honest. The defects are in the narrative rows the baseline block inherits.

### 1.4 Commands (re-runnable; cwd = repo root)

```bash
# marker counts at any revision (lines / literal occurrences / exact form)
python3 - <<'EOF'
import subprocess
for rev in ['76c105b','49ac1a5','291c714','1688790','c610e0a','fe34faa']:
    paths=[p for p in subprocess.run(['git','ls-tree','-r','-z','--name-only',rev,'corpus/knowledge'],
        capture_output=True,text=True).stdout.split('\0') if p.endswith('.md')]
    L=O=E=0
    for p in paths:
        t=subprocess.run(['git','show',rev+':'+p],capture_output=True,text=True).stdout
        L+=sum(1 for x in t.splitlines() if 'to-verify' in x); O+=t.count('to-verify'); E+=t.count('(to-verify)')
    print(rev,len(paths),'lines',L,'occ',O,'exact',E)
EOF
# round-1 decision tokens: lines-matching-any vs per-token lines
python3 -c "import glob,re;print(sum(1 for p in glob.glob('corpus/lessons/round-1-triage/*.md') for L in open(p,encoding='utf-8') if re.search('CONFIRM|DOWNGRADE|EXCISE',L)))"
# frozen finding-line census
python3 -c "import glob,re,collections;[print(p,collections.Counter(re.findall(r'FINDING ([A-Z][A-Z0-9-]*)',open(p).read())),sum(1 for L in open(p) if L.startswith('FINDING'))) for p in sorted(glob.glob('tools/gates/frozen/round-4/*.out'))]"
# gate battery
for g in tools/gates/*.py; do python3 "$g" --selftest; echo "$g rc=$?"; done
```

---

## 2. Attack A — count-based quality claims that do not survive re-measurement

### 2.1 The freshness series is not monotone; the committed frame hides a regression

Re-measured marker series (lines containing `to-verify`, summed per file — the semantics of the SCORECARD's own `grep -rc … | awk` command):

| commit | files | marker lines | literal occurrences |
|---|---|---|---|
| `76c105b` mint seeding | 48 | 223 | 245 |
| `49ac1a5` mint finishing | 176 | **1258** | 1286 |
| `291c714` round 1 | 176 | **795** | 807 |
| `1688790` round 2 | 176 | **587** | 592 |
| `c610e0a` round 3 | 178 | **612** | 623 |
| `fe34faa` round 4 | 179 | **590** | 595 |

`LOG.md` round-1 and round-2 numbers reproduce exactly (1258→795, 795→587). **Round 3 raised the raw marker count by 25** (587 → 612) — the new `mesoamerica-primary-sources.md` alone carries 39 marks on 32 lines — yet `SCORECARD.md` freshness renders the whole history as "1258 → 612 raw sum", which reads as monotone progress. No committed artifact names the increase. The freshness score (`1→4`) is therefore derived from a series whose round-3 step is a regression, presented as an endpoint.

### 2.2 The calibration counting command does not produce the number it is attached to

`SCORECARD.md` calibration row: evidence `983+ basis-carrying triage decisions`; counting command
`grep -h 'CONFIRM\|DOWNGRADE\|EXCISE' corpus/lessons/round-1-triage/*.md | wc -l` **= 983** (stated).

- Re-measured: lines matching any of the three tokens across the 42 round-1 ledgers = **893** (`NOT REPRODUCED`).
- The 983 figure is the **sum of three per-token line counts** (503 + 416 + 64), a different command than the one printed.
- 90 ledger lines carry two tokens (e.g. `CONFIRM/DOWNGRADE` rows), which is exactly the 983 − 893 gap.

A score row whose quoted command returns 893 while the row asserts 983 is an opinion under `AXES.md` §SCORECARD ("a score no reader can re-derive is an opinion, not a measurement").

### 2.3 Audit-report count

`LOG.md` round 4 and `SCORECARD.md` capability row both say **17 audit reports**. `corpus/lessons/round-4-audit/` holds **16** `*.md` (13 `civ-*` + `culture-material` + `linguistics` + `myth-symbol`). `NOT REPRODUCED` (off by one; the missing partitions — `synthesis/`, `verification/` — have no report at all despite 37 entries).

### 2.4 The index undercounts the corpus it indexes

`corpus/README.md` (revision 1.1, regenerated in round 4) says `## civilizations/ (93)` and `Total knowledge entries: 178`, while the tree holds **94** civilization entries and **179** total. The regenerated index carries the *pre*-round-4 count. `NOT REPRODUCED`. (README is on the parent's no-write list; recorded here as a routed defect.)

### 2.5 The round-4 finding total is unreproducible from its own frozen evidence

`LOG.md` round 4: depth "Measured: 24" and the decomposition "phonology 3 REVIEW, lexicon 0, myth 0, costume 0, naming 18".
Frozen census at `fe34faa`:

- `frozen/round-4/phonology-sanity-gate.out` → 3 × `A-NEUTRAL`
- `frozen/round-4/naming-collision-gate.out` → 18 (6+1+10+1)
- `costume-era-consistency-gate.out`, `lexicon-coverage-audit.out`, `myth-consistency-gate.out` → **0 bytes each**

Total = **21**, not 24. Round 3's frozen set does sum to its stated "from 34" (10+0+1+20+3). So the *before* number is evidence-backed and the *after* number is not. No counting command is recorded for either.

### 2.6 Dispatch arithmetic in round 2 is impossible as written

`LOG.md` round 2: "relaunched on key 1 … **46/49 completed, 7 filter-killed**". 46 + 7 = 53 ≠ 49; either the denominator or the parts are wrong. (Rounds 1, 3, 4 reconcile: 47+15=62; 25+3+6=34; 31+1=32.) This is exactly the miscount class `claims.json` claim 3 ("calibration") exists to correct — the correction must name *this* pair, not only item totals.

### 2.7 `590` has no committed derivation

`claims.json` `raw_to_verify_lines: 590` is correct only under the **lines** reading (literal occurrences = 595, exact `(to-verify)` = 537). No committed file names that command, and the field name is the only clue. Three distinct counting bases are in circulation across `LOG.md` (occurrences), `SCORECARD.md` (lines via `grep -rc | awk`), and `claims.json` (lines, unnamed). Inter-round comparison without a fixed command is not a measurement.

---

## 3. Attack B — "freshness" that is marker deletion

1. **Marker removal is certified as work, not as verification.** Round-1's own protocol (`to-verify-triage-protocol.md` §4) defines the *decisions*; the *score* moves on the count. The distribution is the tell: **416 of 983 round-1 decisions are DOWNGRADE (42%) and 64 are EXCISE (6.5%)**. A DOWNGRADE typically *keeps* the mark — so 42% of the "triage decisions" produce no marker movement, and 6.5% produce movement by deletion. The freshness score reads only the residue.
2. **Marker removal explicitly retained a defect on a line that was then "verified".** Round-2 batch M15 removed the flag from `myth-symbol/symbolism-synthesis-method.md:169` and added a source record. The retrieved text of MYS 5:894 gives the kana **「ことだまの さきはふくに」**; the entry prints `kotodama no saiwafu kuni` — the `k` is dropped and no edition reads `saiwafu` (the lane's own sibling entry writes `sakiwau`). Marker gone, error still standing: §6 audit 4.
3. **The same correction was not swept, and the audit suite missed it.** `corpus/lessons/round-1-triage/L4.md:26` records fixing the 894/3254 attribution conflation in `linguistics/naming-systems.md` — but `myth-symbol/ritual-liminality.md:13,109` still carries the **reversed** attribution ("poem 894 (Hitomaro) and 3254 (Yamanoue no Okura)"). PROTOCOL §Evidence standard: "a corrected fact left standing in a sibling file is still a defect". The round-4 myth-symbol audit graded that file PASS. §6 audits 1–2.
4. **Zero-marker batches are not freshness movement.** Round-2 batches V05/V07/V04 and round-2 M15 processed 0 claim flags and were logged as triage work; they are legitimate labour but must not be counted toward a freshness delta. The wave's claim 1 correctly refuses "raw marker removal is not the metric" — the historic SCORECARD does not.
5. **56 of 179 entries carry no marker at all; 123 still do.** Absence of the mark is the *absence of a flag*, never a statement about a source. Any freshness metric that reads only the residue cannot distinguish "checked and supported" from "never flagged because never inspected".

---

## 4. Attack C — review artifacts that cannot fail (the "empty review" class)

1. **The round-4 audit suite is a roll-call.** Census over its 16 reports: **189 `PASS` lines, 0 `FAIL`**; `myth-symbol.md:12` states outright "PASS for all 16 files; 0 audit defects". By `PROTOCOL.md` §Gate standard, "a tool that cannot fail is a probe" — the suite is registered in `SCORECARD.md` as a *capability* ("entry apparatus audit … 17 reports"), which is defensible, but it must not be read as verification of the corpus' claims. `DEFECT`-token hits (20) are dominated by the phrase `header_defects` inside the printed script and by explicit non-defect disclaimers.
2. **The PASS criterion for flags is non-emptiness.** `civ-01-07.md` etc. grade each entry "flags N/N based … all basis cells non-empty". A ledger cell containing `checked, fine` satisfies it. Non-emptiness is a syntactic test that a non-author cannot falsify without re-reading every ledger row — the review is then only as strong as the ledger it points at, and the ledgers are author-written.
3. **The audit's own queue proves the missed defect is a miss, not a coverage gap.** `myth-symbol.md:121` maintains an explicit list of un-repaired cross-file findings (Bascom issue-number; the Smith 1982 essay placement owed by `myth-ritual-theories.md:8,31` and `pantheon-archetypes.md:16`). The 894/3254 reversal in `ritual-liminality.md` — a *corrected* fact left standing — is not on that list, though it is the same class and was corrected in the same round-1 batch's sibling file.
4. **Reviews do not pin the revision they graded.** Of the 15 `examples/culture-d2/reviews/*.md`, six (`02-phonology`, `03-morphosyntax`, `05-lexicon`, `12-rank-rules`, `13-naming`, `14-kin-address`) contain **no digest/`sha256` string**. A review over a moving component cannot be re-verified against the bytes it graded. Round 3's own LOG entry shows the cost: the 06-pantheon review pinned a digest the writer then superseded.
5. **Count-based review claims compound.** The round that claims "defects named per batch" also overcounts its own report set by one (§2.3) — the same failure mode the audit is supposed to catch.

---

## 5. Attack D — operability/replay: what the frozen artifacts can and cannot support

1. **Round 4 is not replayable and does not meet the pre-existing gate standard.** `tools/gates/frozen/round-4/` contains five `.out` files and **no** `MANIFEST.tsv`, **no** `inputs/` snapshot, **no** `expected.json`, **no** recorded exit codes; three outputs are zero bytes. `PROTOCOL.md` §Gate standard "Two evidences" requires a frozen baseline to pin the digest of every snapshot input (else `snapshot_tampered`/`unpinned (legacy)`), and a zero-byte file cannot distinguish "exit 0, no findings" from "the run produced nothing". Only **round 3** is replayable today (`MANIFEST.tsv`, 7 rows, gate/input/output digests, byte-copy inputs).
2. **Concrete replay trap the wave's claim 2 must handle.** In `frozen/round-3/MANIFEST.tsv` the `command` column names the **live** path (`python3 tools/gates/phonology-sanity-gate.py examples/culture-d2/packet.d2.yml`) while `input_sha256` pins the **snapshot copy** (`54be6319…`). The live packet at `fe34faa` is `d5fb4088…` (round-4 v1.1). A replay that executes the recorded command text compares a gate run over the wrong bytes; a replay that verifies digests and rewrites the path argument is the only correct one, and it must record which path it executed. `claims.json` claim 2 promises exactly this ("verifies all pinned input digests before rerunning gates … rejects a tampered scratch input with exit 2 and `snapshot_tampered`") — the trap is why the negative control matters.
3. **Positive result, re-executed:** the 7-gate selftest battery is green at the baseline (7/7 exit 0), so "All 7 existing gate selftests remain passing" is satisfiable and was independently confirmed rather than assumed.
4. **Diagnosis the round-4 LOG failed to make (counts as a calibration defect).** The 18 residual naming findings decompose into classes the frozen output *names*: **6 `NAME-NEAR` are era tags** (`E0` vs `E1`… one edit apart) and **10 `PHON-INVENTORY` are English garment glosses** (`winter valley coat (heavy felted wool…)`, `bale cord`, …) checked against the D2 phoneme inventory. Round 3 had already called the same class "ten English garment labels treated as D2 names" — round 4 re-describes it as "suspect encoding/segment class, **undiagnosed**". The regression is calibration, and ≥16 of the 18 residual findings are non-substantive by construction; the honest residual is 1 real coda violation + 1 declared gap.

---

## 6. Source-recheck (required JSON)

Audited unit note: this lane has no single assigned knowledge entry, so `entry` names the claim-set audited and each row carries its own `entry_locator`. `entry_sha256_before` hashes the primary audited entry (`corpus/knowledge/myth-symbol/ritual-liminality.md` at `fe34faa`); the worktree hash of both entries equals its baseline hash, so no corpus byte changed during this pass. `WebSearch` returned HTTP 403 (5-hour quota) for the whole pass, so retrieval used directly-addressed public texts; no fetch result is quoted from a snippet or a search result.

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "claim set: myth-symbol/ritual-liminality.md (kotodama attestation + authorship) vs linguistics/naming-systems.md; myth-symbol/symbolism-synthesis-method.md romanization; myth-symbol/color-symbolism.md Tang dress-colour edicts",
  "entry_sha256_before": "fd4dcc70e56df283d3e1efc88d22d4f68c23832393ac05a7fe46b9d8e493d691",
  "checked_at_utc": "2026-10-17T15:38:24Z",
  "audits": [
    {
      "id": "27-SR-01",
      "claim": "ritual-liminality.md attributes MYS 894 to Hitomaro and MYS 3254 to Yamanoue no Okura (\"poem 894 (Hitomaro) and 3254 (Yamanoue no Okura)\").",
      "entry_locator": "corpus/knowledge/myth-symbol/ritual-liminality.md:13 and :109 (working tree = fe34faa, sha256 fd4dcc70…)",
      "source_url": "https://ja.wikisource.org/wiki/%E4%B8%87%E8%91%89%E9%9B%86/%E7%AC%AC%E4%BA%94%E5%8D%B7 ; https://ja.wikisource.org/wiki/%E4%B8%87%E8%91%89%E9%9B%86/%E7%AC%AC%E5%8D%81%E4%B8%89%E5%8D%B7",
      "retrieval_status": "retrieved (both pages fetched in full; 61282 and 71470 extracted characters)",
      "source_locator": "book V, entry [歌番号]05/0894, fields [題詞]/[左注]/[事項]; book XIII, entries [歌番号]13/3253 and 13/3254, fields [題詞]/[事項]",
      "source_excerpt": "[05/0894][題詞]好去好来歌一首 … [左注]（天平五年三月一日良宅對面獻三日 山上憶良謹上 大唐大使卿記室）— [13/3253][題詞]柿本朝臣人麻呂歌集歌曰",
      "verdict": "contradicted",
      "basis": "The retrieved text of 894 is the 好去好来歌 whose 左注 is signed by 山上憶良 and whose [事項] author field reads 作者：山上憶良; 13/3253–3254 carry the [題詞] 柿本朝臣人麻呂歌集歌曰 with [事項] 作者：柿本人麻呂歌集. The entry's attribution pair is therefore reversed. The lane's own ledger already recorded this conflation as fixed in the sibling file: corpus/lessons/round-1-triage/L4.md:26.",
      "access_limit": "Wikisource is a public transcription used here as a text witness for poem numbering and the transmitted 左注/[事項] apparatus; a printed critical edition was not collated. The M3 ledger's residual stands: editions differ on whether 894 is Okura's or anonymous, and this audit does not settle that.",
      "coupling_tested": "language/myth"
    },
    {
      "id": "27-SR-02",
      "claim": "naming-systems.md: MYS 5:894 (Yamanoue no Okura, 好去好来の歌, 言霊の幸はふ国); MYS 13:3250 and 13:3253 = kotoage 言挙げ; MYS 13:3254 quoted from the 柿本人麻呂歌集 with individual authorship uncertain.",
      "entry_locator": "corpus/knowledge/linguistics/naming-systems.md:20 and :103 (sha256 9542d71b… at fe34faa)",
      "source_url": "https://ja.wikisource.org/wiki/%E4%B8%87%E8%91%89%E9%9B%86/%E7%AC%AC%E4%BA%94%E5%8D%B7 ; https://ja.wikisource.org/wiki/%E4%B8%87%E8%91%89%E9%9B%86/%E7%AC%AC%E5%8D%81%E4%B8%89%E5%8D%B7",
      "retrieval_status": "retrieved",
      "source_locator": "05/0894 [原文] 言霊能 佐吉播布國等 and [仮名] ことだまの さきはふくに; 13/3250 [訓読] 神からと 言挙げせぬ国; 13/3253 [訓読] 言挙げぞ我がする; 13/3254 [訓読] 磯城島の大和の国は言霊の助くる国ぞ",
      "source_excerpt": "[05/0894][訓読]…大和の国は…言霊の 幸はふ国と 語り継ぎ 言ひ継がひけり — [13/3254][訓読]磯城島の大和の国は言霊の助くる国ぞま幸くありこそ",
      "verdict": "supported",
      "basis": "Poem identification, the 言霊 spellings, the kotoage loci (3250, 3253) and the 柿本人麻呂歌集 provenance of 13:3254 all match the retrieved text field-for-field; authorship uncertainty is preserved in the entry rather than resolved.",
      "access_limit": "MYS 11:2506 (crossroads-divination use) was not retrieved, so the supported verdict covers 894, 13:3250, 13:3253, 13:3254 only.",
      "coupling_tested": "language/myth"
    },
    {
      "id": "27-SR-03",
      "claim": "color-symbolism.md: the Tang yellow-exclusion edict is 668 (總章元年「始一切不許著黃」) and the often-quoted 674 (上元元年) edict is the rank ladder itself.",
      "entry_locator": "corpus/knowledge/myth-symbol/color-symbolism.md:41 (sha256 ae176df1… at fe34faa; round-2 correction recorded in corpus/lessons/round-2-triage/M03.md)",
      "source_url": "https://zh.wikisource.org/wiki/%E8%88%8A%E5%94%90%E6%9B%B8/%E5%8D%B745",
      "retrieval_status": "retrieved (page fetched in full; 舊唐書 卷45 志第二十五 輿服)",
      "source_locator": "卷45 輿服志, Tang 常服 sequence: after 龍朔二年 (孫茂道's 碧/兼服黃 memorial) and before 文明元年",
      "source_excerpt": "總章元年，始一切不許著黃。上元元年八月又制：「…文武三品已上服紫，金玉帶。四品服深緋，五品服淺緋，並金帶。」",
      "verdict": "supported",
      "basis": "The retrieved text places 始一切不許著黃 under 總章元年 (668) and the purple/crimson/green/cyan ladder under 上元元年 (674), exactly as the entry states after its round-2 correction; the ordering of the two edicts in the source matches the entry's distinction between colour exclusion and rank ladder.",
      "access_limit": "One transcription (zh.wikisource) of 舊唐書 卷45; no printed collation, and the entry's further claim that yellow was 'increasingly reserved for the throne' from the mid-7th century is a synthesis, not a quotation.",
      "coupling_tested": "dress/era/rank-colour"
    },
    {
      "id": "27-SR-04",
      "claim": "symbolism-synthesis-method.md renders the MYS 5:894 formula as \"kotodama no saiwafu kuni\".",
      "entry_locator": "corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:169 (sha256 1b0d646c… at fe34faa; flag removed in corpus/lessons/round-2-triage/M15.md)",
      "source_url": "https://ja.wikisource.org/wiki/%E4%B8%87%E8%91%89%E9%9B%86/%E7%AC%AC%E4%BA%94%E5%8D%B7",
      "retrieval_status": "retrieved",
      "source_locator": "05/0894 [原文] …言霊能 佐吉播布國等…; [仮名] ことだまの さきはふくにと; [訓読] 言霊の 幸はふ国と",
      "source_excerpt": "[仮名]…ことだまの さきはふくにと かたりつぎ いひつがひけり",
      "verdict": "contradicted",
      "basis": "The retrieved kana is さきはふ (saki- + -hafu) and the phonogram spelling 佐吉播布 is sa-ki-ha-fu; `saiwafu` drops the medial k and matches no reading in the retrieved text. The lane's sibling entries write `sakiwau` (creation-myths-taxonomy.md:100) / `sakiwau`-class forms. The round-2 pass removed this line's flag and added a source without correcting the transliteration.",
      "access_limit": "Romanization conventions vary (sakihafu / sakiwau); the verdict is that `saiwafu` is unsupported by the retrieved kana, not that a single romanization is canonical.",
      "coupling_tested": "language/myth"
    }
  ]
}
```

**Unresolved, preserved:** (a) authorship caveat for MYS 5:894 across editions (M3 ledger residual — not adjudicated here); (b) MYS 11:2506's use of *kotodama* (book XI not retrieved); (c) whether any printed edition prints `saiwafu`. None of these is upgraded to a confirmation by this pass.

---

## 7. What evidence is required to call `supplement-opencode-1` admitted

`claims.json` is a **plan**, not evidence: each `after_required` needs its own committed artifact plus the command and its observed result. Admission should require, per claim:

**Claim 1 — freshness (the wave's lowest axis).**
1. A row schema that binds each row to retrieval, not to prose: exact fetch command/tool, URL, UTC timestamp, HTTP status, response byte length **and** sha256 of the retrieved body.
2. ≥5 rows where `source_excerpt` is a **verbatim substring of the stored body** — the parent verifies by substring match against the stored bytes, not by re-reading the claim. (Search snippets, metadata pages and blocked fetches stay non-confirming; `retrieval_status` must distinguish `retrieved` / `blocked` / `record-only`.)
3. **≥1 row retained as `contradicted` or `unresolved`.** A batch with 100 % `supported` verdicts is presumptively padded; the two contradictions this pass produced (§6 audits 1 and 4) show what a real one looks like.
4. ≥1 row must test a **coupling** claim (language↔myth, dress↔era↔rank) rather than an isolated bibliography fact; two of the four rows above do.
5. The batch must state the marker count **only** as workload, with the per-batch decision distribution (CONFIRM/DOWNGRADE/EXCISE) reported, DOWNGRADE counted as non-resolution. No freshness score movement on marker deletion alone.

**Claim 2 — operability.**
6. `python3 tools/assemble-d2.py --selftest` and `--check` transcripts with exit codes; the existing 7-gate battery re-run output (I re-ran it: 7/7 exit 0 — the wave must reproduce this itself, not inherit it).
7. Replay transcript over `frozen/round-3` showing, per row: the pinned digest it verified, **the path it actually executed** (snapshot, not the live `examples/culture-d2/packet.d2.yml` the MANIFEST command text names), and the compared verdict.
8. Negative control: a tampered scratch copy → **exit 2 + `snapshot_tampered`**, with the tampered file's digest recorded.
9. An explicit statement that **round 4 is not replayable** until it is re-frozen with `MANIFEST.tsv` + input digests + exit codes (three of its outputs are zero bytes today), and that no replay will silently treat an empty `.out` as a clean verdict.

**Claim 3 — calibration.**
10. The LOG correction must name each superseded number, the text it came from, and the reproduced replacement with its command. The open cases from this pass: `983` vs the command's `893`; `17` vs `16` audit reports; `Total knowledge entries: 178` vs `179` (and civilizations `93` vs `94`); round-4 `24` vs the frozen `21`; round-2 `46/49 + 7`; and `raw_to_verify_lines: 590` with no committed command.
11. An uncertainty inventory that lists every count that could **not** be reproduced and why — and states that marker absence is not validation.
12. No score change without a derivation, and no axis reported as "unharmed" without a per-axis check named in the same entry.

**Wave-level.**
13. Worker reconciliation: `worker_count: 32` must be reconciled against artifacts actually landed under `reports/supplement-opencode-1/` (parent-owned), naming any non-landing worker.
14. `counted_as_reserved_numbered_round: false` must be mirrored in the LOG entry — no round-4/5 style numbering may attach to this wave, and the three non-flash Z.ai rounds stay untouched.
15. Non-author re-execution: at least one claim per axis re-run by a lane that did not produce it, with the command and output in that lane's report.

---

## 8. Recommended errata (append-only; parent/owner applies — this lane edited no corpus byte)

The defects in §3.2–3.3 are live in committed corpus bytes and are the round's only *substantive* source findings. Recommended minimal, dated appends (no old bytes rewritten):

1. `corpus/knowledge/myth-symbol/ritual-liminality.md` — one appended erratum after the affected lines: the attribution pair at :13/:109 is reversed; per the round-1 L4 correction (`corpus/lessons/round-1-triage/L4.md:26`) and the retrieved texts (MYS 5:894 = 好去好来歌, 作者 山上憶良; MYS 13:3253–3254 = 柿本人麻呂歌集, individual authorship uncertain), pointer to this report §6 audits 1–2.
2. `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:169` — append the unsupported-romanization note (`saiwafu` → `sakihafu`/`sakiwau` per the retrieved kana さきはふ), naming this report §6 audit 4; do **not** re-flag the line, which would conflate a transliteration fix with an unresolved source.
3. Route to the owner of `corpus/README.md`: partition total `civilizations/ (93)` → 94 and `Total knowledge entries: 178` → 179 (counted with `find corpus/knowledge -name '*.md' | wc -l`; README is on this lane's no-write list).
4. Route to the `SCORECARD.md` owner: calibration counting command (893 vs 983) and the two strands it hides — the `17/16` audit-report count and the round-3 marker regression (587 → 612) that the freshness row's "1258 → 612" frame conceals. Rows are parent-owned; this report names them, it does not edit them.
5. Route to the `LOG.md` owner: the round-2 dispatch arithmetic and the round-4 finding total (21 from the frozen evidence vs 24 as written).

---

## 9. Limits of this pass

- `WebSearch` was unavailable (HTTP 403, 5-hour quota) for the whole pass, so no independent URL *discovery*; retrieval was limited to directly-addressed public texts. The Nara Prefecture 万葉百科 DB that the lane's own ledgers cite was **not** fetched (no URL to address without search), so this pass corroborates, and does not replace, that citation.
- Wikisource is a community transcription of 万葉集/舊唐書, used as a text witness for poem numbering, apparatus fields and transmitted wording; no printed critical edition, no page-level collation, and no Japanese-language monograph was consulted. The gallery of romanization (`sakihafu`/`sakiwau`) is convention-dependent; the contradicted element is the dropped `k`.
- Review/audit critique is structural and reproducible (counts, PASS/FAIL census, digest presence); it does not re-adjudicate any individual audit verdict.
- No corpus byte, LOG, SCORECARD, README, SKILL, packet or frozen artifact was written by this lane. `git status` shows only untracked `reports/`; the two audited entries' worktree hashes equal their `fe34faa` hashes.
- Author-side evidence only: this report asserts no `[x]` and promotes nothing. The wave is not admitted by this file; it states the bar.
