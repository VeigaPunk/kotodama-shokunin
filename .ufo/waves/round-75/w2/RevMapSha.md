# RevMapSha — w2 attack: the by-document renumber map (kotodama round 75, hyaku 10, wave 2)

Seat: RevMapSha (leaf) · 2026-10-27 · base `f556d1049fe651d3d63975600b13acd9fb686f15`
Target: `.ufo/waves/round-75/assimilation/id-renumber-map.json` — sha256 verified **`778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155`** (matches the w1-published hash; file untouched by me).
Also attacked: `build-map.py`, `reg-ids`, `staged-ids`, `collisions`, `substitution-table.txt`, `collision-documents.txt`, `guard-proof/` (README, make-fixtures.py, run-guard.sh, out/*).

**Verdict: the map's operative content survives every attack I ran.** The staged→lane join is by document, not arithmetic; all nine lane joins reproduce independently; the three id files are byte-identical to fresh re-derivations from the base registry and the staged package with the prompt's exact 0–3-space pipeline; the guard proof replays clean with fresh 2-space and 4-space plants. Two prose/provenance defects found (F1, F2), neither touching the operative table.

## 1. Re-derived id files (prompt's exact pipeline)

`grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' <reg> | grep -oE 'S[0-9]+' | sort` (plus `-u` set form; both computed) on:

- registry = `git show f556d104…:corpus/SOURCES.md` (blob sha256 `c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614`; working-tree file byte-identical, `git status --porcelain` clean — so the guard proof's `real` run was base-valid);
- staged = `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md`.

Result: reg-ids **808** (no duplicate ids), staged-ids **132**, collisions **26** (S859–S884 contiguous). `cmp` against the lane's `reg-ids`/`staged-ids`/`collisions`: **all three byte-identical**. Adopted ids S885–S893: 0 in reg-ids, 0 in collisions (free).

## 2. By-document join — all nine adopted lanes

Independently recomputed from (a) every staged row's source cell in SOURCES.append.md and (b) the nine registry rows S885–S893 in `assimilation/validate/corpus/SOURCES.md` (lines 840–848; that file = base registry + exactly those nine rows — set-diff checked), with a normalizer written from the map's stated `join_key` spec, not from build-map.py's code:

| lane | document (normalized) | staged rows joined | = assignments | = claim C | agree |
|---|---|---|---|---|---|
| S885 | persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 | S876, S885, S917, S921 | ✔ | ✔ | ✔ |
| S886 | persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 | S902 | ✔ | ✔ | ✔ |
| S887 | persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 | S904 | ✔ | ✔ | ✔ |
| S888 | jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf | S864 | ✔ | ✔ | ✔ |
| S889 | jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf | S865 | ✔ | ✔ | ✔ |
| S890 | jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf | S866 | ✔ | ✔ | ✔ |
| S891 | unige.ch/lettres/framo/cernet/biblio/barth70.html | S905 | ✔ | ✔ | ✔ |
| S892 | iris.unipa.it/retrieve/e3ad891d-…/2014 marrone age dor---2.pdf | S919 | ✔ | ✔ | ✔ |
| S893 | chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | S870 | ✔ | ✔ | ✔ |

Normalization rules exercised for real: persee page-level→doc-level collapse (S917/S921 `/doc/page/…/T1_00xx_0000` → `/doc/comm…1113`), wayback wrapper strip (S919 `web/20251111222249if_/…`; `if_` suffix handled), www-strip + host lowercase + percent-decoding (S892: claim's space-form vs staged `%20` form join identically, and the map's `url` carries the `%20` form with both in `url_variants` — the `url_field_note` is accurate). An "any URL in the row" join (stronger than build-map's first-URL rule) adds nobody. `map`-dict internal consistency: every `normalized_document_url` recomputes from both `staged_url` and lane `url`; `numeric_offset` field correct on all 12 assignments; `url_variants` all normalize to the join key.

## 3. Not arithmetic — proven

Per-assignment offsets: **{-36, -32, -27, -17, -16, -14, 0, +9, +23, +24}** — ten distinct offsets across twelve assignments. No constant k in **[-999, 999]** reproduces the map (`lane = staged + k` fails for every k). The map's `numeric_offsets_note` ("ten distinct offsets across the twelve assignments … NOT arithmetic") is exact. The single same-number pair (staged S885 → lane S885) is a genuine same-document coincidence, as the map's own hazard note states.

## 4. Collisions and collision-documents.txt

All 26 colliding ids (S859–S884) re-checked pairwise: lane doc (base registry) vs staged doc (append) — **0 of 26 share a normalized URL** (my recompute; map's `same_document_pairs: []` and the `class` sentence agree). So all 26 are namespace drift, and the guard's acceptance is correctly framed as *by document*, not "collisions empty". Post-adoption same-number table: staged S885 = lane S885 document (the coincidence); S886–S893 same-number staged docs (Kotobank ×3, NDL search, Kalużyńska, Zhao, RUDN, CyberLeninka) all differ from the lane docs.

## 5. Guard proof — replayed with fresh plants

Fresh fixtures built in my scratch from the base blob, planted row = clone of S884 with id cell → a staged id the lane lacks, URLs → `example.invalid/guard-proof/planted-<id>.pdf`, kind/tier/status/used-by → paper/A/queued/— per the original proof's documented normalization; run with the exact ITEM10 / COLZERO patterns, `comm -12`, and the fleet census:

| fixture | plant | ITEM10 ids | ITEM10 sees plant | collisions | plant in collisions | COLZERO ids | COLZERO sees plant | census rows | validate findings |
|---|---|---|---|---|---|---|---|---|---|
| 2sp-fresh | S990 | **809** | **yes** | **27** | **yes** | 808 | no | 809 | 31 (0 new), exit 0 |
| 4sp-fresh | S985 | 808 | no | 26 | no | 808 | no | 808 | 31 (0 new), exit 0 |

Matches the original `guard-proof/out/` claims exactly (control 808/26; original 2sp plant S986 and 4sp plant S988 show the same signature; `real` 808/132/26). The column-zero false-green is reproduced: COLZERO misses the 2-space plant the census counts (809 rows). The 4-space plant is invisible to extractor *and* census — CORPUS's indented-code rule, so guard and census never disagree. One observation (F5 below): the census is *not* blind to row shape — a first plant attempt that kept S884's `mined` status and real used-by path produced a 32nd validate finding; with the documented normalization the count stays 31, as the README's fixture design states.

## 6. Substitution table and build-map.py

- `substitution-table.txt` ↔ `entry_substitutions`: **36/36 (file, line, staged id, lane id) triples identical, zero either-side deltas**; no occurrence carries `replacement: none`.
- Occurrence coverage: my independent scan of the five staged narrative files finds exactly 36 S-id occurrences; the map lists exactly those 36 — none missing, none invented.
- Single-pass simulation: applying the table simultaneously to each file leaves **zero** leftover S-ids and zero unlisted ids in all five files. (The one-pass rule is also *necessary* contract: staged S885 exists and maps, so a naive re-scanning sweep could re-process produced ids.)
- Prose ids S744/S763 are correctly treated as campaign-scope same-document rewrites with the correct lane targets (S744→S885, S763→S887), and neither is a staged registry row.
- Conditional S893 entry matches `claim C.rejects.refused_staged_not_appended` verbatim ("S870's staged quote … re-opened as S893"), and the `refused_staged_not_appended_note`'s parser warning is correct — the field is prose, not an id list.
- build-map.py's extractor/rows logic uses the same `^ {0,3}\|` anchor family as the prompt pipeline; no divergence found.

## Findings

**F1 · MEDIUM (prose defect in a pre-freeze authority artifact; operative table unaffected).** `id-renumber-map.json → substitution_rule` states "(staged S885 = Kotobank, staged S890 = Kaluzynska, staged S891 = Zhao et al.)". Ground truth: in the round's staged package S885 is **Barthes, Communications 8 (Persee 1113)** — the map's own `map["S885"]` and `round_specific_hazards[2]` say exactly that; the Kotobank rows are staged **S886/S887/S889**. The campaign frame does not rescue it: `shokuknow/lanes/kotodama/ID-REMAP.md` maps round5's S885 → append S911 (「中國的名與字」, sites.google.com), so no verifiable frame makes any S885 a Kotobank row. S890/S891 examples are correct. Risk: a counter or builder trusting the note's example namespace mis-derives the very corruption class the note warns about. Recommend fixing the parenthetical (e.g. "staged S886/S887/S889 = Kotobank rows") before freeze — I have not touched the file.

**F2 · LOW (provenance).** `inputs[2]` cites `/home/vgpnk/Projects/shokuknow/merge/kotodama/ID-REMAP.md`, which does not exist; the real file is `/home/vgpnk/Projects/shokuknow/lanes/kotodama/ID-REMAP.md` (the hazard-#1 quote is verbatim-accurate against its line 9). All three `inputs` entries carry `sha256: null`, so the map binds none of its inputs by hash. Mitigated: I reproduced every derived quantity from the named sources.

**F3 · LOW (docstring).** `guard-proof/make-fixtures.py` docstring annotates the plant ids with wrong documents ("S985 -> katobank", "S986 -> Persee 1120"; staged S985/S986 are Douban rows). Proof mechanics unaffected — plants only need to be staged ∧ ¬reg, which holds.

**F4 · INFO (adjacent tree, observed in passing).** `validate-fetch/urls.txt` lists S885–S892 but no S893 line, although `S893.meta` exists — consistent with urls.txt predating the S893 re-open. `W891.meta` is a deliberate wayback-carrier receipt for S891 (barth70.html capture, content sha256 `69b5987240ccd7287e4e297f7333be9ed2ceb47a91cf697d196d5cd6b1f2b494`), not a typo.

**F5 · INFO.** See §5 observation: the "no new census finding" property of the guard fixtures depends on the documented paper/A/queued/— normalization; the census does react to row shape otherwise.

## Residual risks / verification gaps

- The extractor is fence-blind: a table row inside a fenced code block would be counted by both pattern and census-side grammar per CORPUS's space rule; untested by either proof. No clause violated; noted only.
- Query strings are kept raw (not percent-normalized); a join split via query-encoding asymmetry is theoretically possible but unexercised by the nine documents.
- The fleet census script was executed as-is, not audited.
- My scratch dir was externally wiped once mid-session; everything was re-derived from primary sources afterward, and all receipts below were (re)hashed after the final runs.

## Receipts (copied to `.ufo/waves/round-75/w2/parts/RevMapSha/`)

```
01ad6576b56d150ad9505beda35775a2cf982ab110affd6c425704e21a357754  collisions.txt
6b0d31169f9b5e76dbdab93596f093a114a8127417364c756f13553fe75eacce  fixture-2sp-fresh.SOURCES.md
0c216fcb601892f6077c931dc979ce236d38808131ab1c3fab296d4a7eec40df  fixture-4sp-fresh.SOURCES.md
b2e00ef20918f8f81bdb521ed7661385c4bd3c06cb3134d9b8881178b9e3aa95  join-receipt.json
dd090b02e0f5c1e1b0eca105c9c37f913a9c937930737ec2c6450d74244e859e  reg-ids.txt
c82e2d11ba13f12c6ed2303775fe42b6ffdd118e60acfb22d3d5339087e0cdb1  replay-2sp-fresh.summary.txt
84bea4f6a79258289c425c895fc49f55ccc0a94260a0bf62375e8cd5272f86d7  replay-4sp-fresh.summary.txt
bab11d7d0ee0d84795b1ff80274fe371670fff73a477c747b2fd3cad4c25ddad  staged-ids.txt
778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155  id-renumber-map.json (target, unchanged)
```

Tooling installs: none. Git/jj mutations: none (read-only `git show`/`status`/`rev-parse` on the lane; no fixture repo needed). Scratch `/fast/scratch/hyaku/kotodama-r75/RevMapSha/` deleted before yield. Fleet repo, scripts, templates, `.ufo/state`, watchdog log, sibling lanes: untouched.
