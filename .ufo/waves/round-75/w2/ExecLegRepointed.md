# ExecLegRepointed — round 75, wave 2: claim-C `REPOINTED` leg

Seat: executor (leaf). Lane `kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`.
Built one piece of the round-75 claim-C acceptance counter: `leg_repointed` + `_map_records`.
Read only the CFG contract, the draft claims, PART A, the round-74 template, the by-document map,
`build-map.py`'s record shape, the entry drafts and the nine validate rows. No claim, ledger, map,
counter, registry or knowledge file was edited; nothing under the fleet repo, `scripts/`,
`templates/`, `.ufo/state` or `shokuknow/` was written. No tool installed (nothing needed; `git`,
`python3`, `diff` sufficed). Scratch `/fast/scratch/hyaku/kotodama-r75/ExecLegRepointed/` created,
used and removed before yield (note: `ExecTmpSweep` deleted the round scratch root at 16:53 and I
rebuilt the fixture; the receipts below are from the rebuilt, final-byte run).

Deliverable: `.ufo/waves/round-75/w2/parts/leg-repointed.py` —
sha256 `b9ce1bb7c2bd8234d5a4584aa9122e1d3e850c276e0cb09e9f97334f31c1032a`, 387 lines,
top-level nodes = `FunctionDef` only, **0 imports**, `python3 -B -m py_compile` clean concatenated
after PART A lines 1-510.

## 1. The leg wording as I read it

Frozen text (claims.json claim C `legs[2]`):

> REPOINTED: every `source:` line carries exactly one id whose row URL names the cited document;
> every inline S-id in the entries resolves to a frozen row; no campaign-namespace id is cited as a
> lane row except the staged->lane substitutions in the frozen map; the staged S870 id is replaced
> by lane S893; no unrelated staged id is preserved

Five clauses, implemented in this order: (a) exactly one id per `source:` line, (b) that id's
registered row URL names the cited document, (c) every inline id resolves to a frozen row
(`cfg.allowed_ids`), (d) campaign-namespace ids appear only as the frozen map's substitutions, (e)
S870 is replaced by its lane row.

## 2. Ambiguities and how I resolved them

| # | Ambiguity | Reading taken | Why |
|---|---|---|---|
| R1 | Does "every `source:` line" mean PART A's `source_lines()` (header only, stops at the first `## `) or every source-field line in the entry? | **Every** line matching `^[-*\s]*source:\s*` anywhere in the entry | Measured, not assumed: the frozen entries keep one file per path with a **second** provenance block for their Part 2 (draft lines 49-52 carry S888/S889/S890/S893 after the first `## `). Under the header-only read, deleting row S893 from the registry and putting two ids on a Part-2 source line both stayed **green** (see C5/M3 in §5: they only go red after the change). `sources:` does not match the pattern and is not a source line — its ids are graded by the inline rule. |
| R2 | "whose row URL names the cited document" — string equality, id arithmetic, or document join? | By-document join on the frozen map's `join_key`, cited keys ⊆ row keys | The map says "never arithmetic, never a numeric id comparison". Joining needs the map's own normalisation (below), which PART A's `norm_url` cannot do (it keys `…/doc/page/<slug>/<transcription>` and `…/doc/<slug>` apart). |
| R2a | Which normalisation? | host lowercased, `www.` dropped, **default port dropped** (`:80` under http, `:443` under https), path percent-decoded, `persee.fr/doc/page/<slug>/…` → `/doc/<slug>`, `web.archive.org/web/<8-14 digits>[flag]/…` stripped to the embedded original (loop, ≤3 levels), scheme not part of the key, trailing `/` dropped | The map names all of these except the port. The port is needed because the S891 capture the staged row itself cites is `http://www.unige.ch:80/…` while the live row is `https://www.unige.ch/…`; without it a legitimate capture citation would be a false FAIL, against QUALITY 18's "the capture's original normalizes to the live URL". |
| R2b | Cited URL set vs row URL set: subset, superset or equality? | **Subset** (cited ⊆ row) | The row may carry page-level views the entry does not quote (row S885 carries the document URL plus p. 5/6/11 URLs); equality would make every row that quotes one page fail. |
| R2c | A source line with no URL, or a row whose source cell has no URL | FAIL | "whose row URL names the cited document" cannot be evaluated; a silent pass would be the vacuity class w1 opened. |
| R3 | Scope of "inline S-id" | Every S-id token in the whole entry (header + body; source lines included) | The wording is unqualified. This is what rejects the campaign-scope ids the registry already reuses: S744 resolves in the lane to Dictionary.com's ushanka page, S763 to the tafl article. |
| R4 | Which ids count as "campaign-namespace", given that staged S885/S893 are also lane ids and staged S886-S892 share numbers with lane rows? | The union of: the frozen map's staged ids, the `row_set`/`reused_rows` `staged` values (multi-id lists included), `cfg.forbidden_ids`, `cfg.refused_staged`. Such an id is legal **only** when its map target is itself (staged S885 → lane S885, the sole identity pair); a differing target (S864 → S888) or no lane row (S876, S902, S904, S905, S917, S919, S921, S870) FAILS. Lane ids that are staged numbers but absent from the map (S886…S893) are graded by R2's document join and R3's row resolution | This is CritCCounterVacuity repair 4 and SimplifierRows §8(c): forbid the explicit staged set minus adopted lane ids. A numeric range (`S864..S921`) would ban the required lane ids; the map is the only frozen authority for the namespace, and it does not name staged S886-S893, so no frozen byte distinguishes "lane S890" from "staged S890" — the document join does it on source lines, and no leg can do it for a bare prose mention (recorded as a residual, §7). |
| R5 | Is "the staged S870 id is replaced by lane S893" a constraint to check or just a fact? | Check both directions: S870 fails under R4 (`frozen map: S870 -> S893` in the detail), **and** at least one entry must cite the map's lane target for S870 | A "replacement" that deleted both ids is not a replacement. The target is read from the map (`lane_by_staged.get("S870")`), never hard-coded; the check is skipped if the target is not a frozen row (round-generic). |
| R6 | How much of the map do I trust? | Read with `git show <freeze>:<cfg.map_path>`, blob must hash to `cfg.map_sha256`; empty pin = FAIL; a map that is not one lookup table (one staged id, two targets) = FAIL | The clause's whole content is the map's substitution table. PART A's `urls_compatible`/`norm_url` are not used for the join (see the finding in §6). |
| R7 | An entry with no `source:` line at all | Not graded here | The frozen ENTRIES leg owns the provenance-header field set ("provenance header … first"). Grading it here would be stronger than my wording. |

## 3. Interface (what the L1's assembly must satisfy)

* Defines: `leg_repointed(ctx)`, `_map_records(ctx)` (contract name; returns
  `{(staged_id, lane_id): url}`) and private helpers `_repointed_source_lines _repointed_unquote
  _repointed_doc_key _repointed_url_keys _repointed_map_blob _repointed_ids _repointed_pairs
  _repointed_staged_universe _repointed_row_keys _repointed_problem`.
* Uses from **PART A** (never redefined): `leg, dedupe, read_tree, parse_rows, row_cells, urls_in,
  git_bytes, REGISTRY, SOURCE, TOKEN_RE`, plus `json/re/hashlib/urlparse` (all PART A imports).
* Does **not** call any `part-cfg.py` helper. `part-cfg.py` landed after this part
  (16:56) and defines `_doc_url_key`/`_url_keys`/`_archive_original` — a normalisation close to,
  but not identical with, the one this leg needs (§6); `_row_url_keys` keys on `(netloc, path)`
  and cannot join the round's page-level/wrapper URLs. Verified against the real file: PART A
  lines 1-510 + `part-cfg.py` + `leg-repointed.py` execute in one namespace with **no name
  collision**, `part-main.py` binds `("REPOINTED", leg_repointed)`, `load_frozen_config` supplies
  every key this leg reads (`row_staged["S885"] == ['S876','S885','S917','S921']`,
  `forbidden_ids == ['S864','S865','S866','S870','S876','S902','S904','S905','S917','S919','S921']`),
  and with the pin filled the leg is **PASS** on the positive mock and **RED** on the staged-id
  mutant (A2/A3 in §5).
* Reads from `cfg`: `freeze, map_path, map_sha256, allowed_ids, entries, row_staged,
  reused_staged, forbidden_ids, refused_staged` (the last four via `.get`, tolerant of a list, a
  `"A/B/C"` string or absence). Reads from `ctx`: `mat, mat_base, root, cfg`. `mat_base` absent →
  the base-row hint is dropped, never a crash. Unreadable registry / missing entry / empty
  `allowed_ids` / empty `entries` → an explicit FAIL detail, never a traceback or a skip.
* Detail is one line capped at 300 characters (CFG contract), truncation marked `...`.

## 4. Mock landing (fixture, in scratch only)

`git clone --quiet --shared --no-checkout` of the lane → assert `rev-parse --show-toplevel` is the
clone → `checkout --detach f556d104…` → **freeze commit** adding `reports/round-75/claims.json` and
`.ufo/waves/round-75/assimilation/id-renumber-map.json` → **lands commit** adding the three drafts
as `corpus/knowledge/myth-symbol/narrative-structure-frameworks{,.amend-2026-10-23,.amend-2026-10-23b}.md`
and the nine rows S885-S893 from `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md`
inserted after S884 (808 + 9 = 817 rows) → base tree materialized with `git archive` for
`mat_base`. All git calls name `-C <fixture>`; no commit ever touched the lane. The leg was run by
`exec()`ing PART A lines 1-510 + the part file in one namespace and calling `leg_repointed(ctx)`
with a hand-built `cfg` per the CFG contract (part-cfg.py did not exist yet).
The probe captures were not needed: this leg reads no evidence file.

## 5. Positive / mutant table (all run; verdicts verbatim)

| run | mutation | verdict | first reason printed |
|---|---|---|---|
| P1 | the three drafts landed as-is (wayback citation for S892; page-level persee URLs inside row cells) | **PASS** | — |
| P2 | S885's source line cites `…/doc/page/..._1113/..._T1_0005_0000` instead of the document URL | **PASS** | — (the collapse works in the tolerant direction) |
| P4 | `row_staged` as the raw multi-id strings (`"S876/S885/S917/S921"`), no `forbidden_ids` | **PASS** | — (cfg shape tolerance) |
| P5 | `row_staged` empty (map + frozen refusals only) | **PASS** | — |
| M1 | staged `S876` kept on a source line | **RED** | `…frameworks.md source line: S876 is a campaign-namespace id cited as a lane row (frozen map: S876 -> S885)` |
| M2 | S886's source line cites S885's document (`…_1120` → `…_1113`) | **RED** | `…amend-2026-10-23.md source line for S886 cites a URL outside the row's document: https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` |
| M3 | two ids on one source line (`source: S885/S888`) | **RED** | `…frameworks.md source line carries 2 ids ['S885', 'S888'] (want exactly one)` |
| M4 | campaign-scope id `S744` cited in prose (registry reuses it for the ushanka page) | **RED** | `…frameworks.md:192 S744 resolves to no frozen row; the lane registry reuses S744 for an unrelated document` |
| M5 | staged `S870` cited as a lane row | **RED** | `…frameworks.md:154 S870 is a campaign-namespace id cited as a lane row (frozen map: S870 -> S893)` |
| M6 | S870 dropped instead of replaced (all `S893` → prose) | **RED** | `no entry cites lane S893: the staged S870 id is not replaced by its lane row` |
| M7 | S892's wayback wrapper carries an **unrelated** document (unige) | **RED** | `…amend-2026-10-23b.md source line for S892 cites a URL outside the row's document: https://web.archive.org/web/20251111222249if_/https://www.unige.ch/…` |
| C1 | `cfg.map_sha256` not the frozen blob's digest | **RED** | `the frozen map …/id-renumber-map.json hashes to 778068a4…5, the claim pins 0000…` |
| C2 | `cfg.map_sha256` empty (unpinned map) | **RED** | `claim map.sha256 is empty at freeze: the by-document map …/id-renumber-map.json is not hash-pinned` |
| C3 | `map_path` the freeze does not carry | **RED** | `cannot read the frozen map …/absent.json at 4e6c20ec8aef: fatal: path '…' does not exist in '4e6c20ec8aef…'` |
| C4 | page-level persee URL of a **different** document under S885 (`…_1114` p. 30) | **RED** | `… source line for S885 cites a URL outside the row's document: https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1114/…T1_0030_0000` |
| C5 | row S893 deleted from the registry at lands | **RED** | `… source line names S893 with no registry row at lands` |
| C6 | map blob with `S876 -> S885` **and** `S876 -> S886` | **RED** | `the frozen map is not one lookup table: S876 -> S885 and S886` |
| A2 | **real assembly** (PART A 1-510 + `part-cfg.py` + this part, `load_frozen_config`, pin filled as the freeze must) | **PASS** | — |
| A3 | same real assembly, staged `S876` kept on a source line | **RED** | `… source line: S876 is a campaign-namespace id cited as a lane row (frozen map: S876 -> S885)` |

P2 and C4 are the pair that proves the collapse discriminates rather than normalising everything
into one bucket: the same `/doc/page/` shape passes for the row's own document and fails for a
sibling persee document. P1/P2 plus M7 prove the wrapper strip does the same for archive carriers.

Normalisation spot checks (same run):

```
key ('persee.fr', '/doc/comm_0588-8018_1966_num_8_1_1113')                    <- …/doc/comm_…_1113
key ('persee.fr', '/doc/comm_0588-8018_1966_num_8_1_1113')                    <- …/doc/page/comm_…_1113/comm_…_T1_0011_0000
key ('iris.unipa.it', '/retrieve/e3ad…/2014 marrone age dor---2.pdf')         <- https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/…%20…
key ('iris.unipa.it', '/retrieve/e3ad…/2014 marrone age dor---2.pdf')         <- https://iris.unipa.it/…/2014 marrone age dor---2.pdf
key ('unige.ch', '/lettres/framo/cernet/biblio/barth70.html')                 <- web.archive.org/web/20041220223357id_/http://www.unige.ch:80/lettres/…
key ('unige.ch', '/lettres/framo/cernet/biblio/barth70.html')                 <- https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html
_map_records: 12 pairs  ['S864->S888','S865->S889','S866->S890','S870->S893','S876->S885',
                         'S885->S885','S902->S886','S904->S887','S905->S891','S917->S885',
                         'S919->S892','S921->S885']
restore: clean
```

`_map_records` also verifies the 12-pair shape: four staged ids (S876/S885/S917/S921) collapse onto
lane S885, ten distinct numeric offsets — the join is by document, not by number.

## 6. Findings for the sibling leg owners (not acted on; not my file)

`part-cfg.py`'s shared `_row_url_keys` returns `neutral_url_keys(urls_in(cell))`, i.e. PART A's
`(netloc, path)`. That key **cannot** join the round-75 persee reality: the page-level URL
`…/doc/page/<slug>/<transcription>` and the document URL `…/doc/<slug>` are different keys, and an
archive wrapper is a third. Any leg that compares a cited URL to a row URL through
`_row_url_keys`/`urls_compatible` will be either false-red (a legitimate page-level citation) or
blind (the wrapper). My leg therefore carries its own `_repointed_doc_key`; ROWS/GATE/EVIDENCE/
COLLCHECK owners should either adopt the map's join_key too or accept that the join they check is
weaker than the one the claim states. Flagged for `ExecCtrCfgMain` and the leg owners; not
messaged as blocking, since nobody's interface breaks (my helper is private).
`part-cfg.py` (landed 16:56, after this part) now carries `_doc_url_key`/`_url_keys`/
`_archive_original`, which do most of the same work. They differ from `_repointed_doc_key` in three
ways I measured, and the divergence is not cosmetic:

1. **Default ports are not dropped.** `_doc_url_key` goes through PART A `norm_url`, so the S891
   capture the staged row itself cites (`http://www.unige.ch:80/lettres/framo/cernet/biblio/barth70.html`)
   keys as `('unige.ch:80', …)` and does **not** meet the live row's `('unige.ch', …)`. My key
   drops `:80`/`:443`, so the capture and the live URL are one document (a false-red otherwise).
2. **`/docAsPDF/<slug>.pdf` is collapsed** by `_doc_url_key`; the frozen map collapses only
   `/doc/page/<slug>/…`, and the sentinel recorded `docAsPDF` as the altcha-protected route that is
   not a citation route at all. Mine follows the map; if the L1 prefers the wider collapse, the
   citation is still not evidence (EVIDENCE owns the fetch line).
3. **Trailing punctuation**: mine strips a CJC/punctuation set before parsing; `norm_url` strips
   ASCII only. This only matters for a URL followed immediately by `」`, `。` etc.

If the L1 wants one normalisation across legs, `_doc_url_key` needs the port clause added; my leg
would then call it instead of carrying its own. As filed, no leg is inconsistent *within itself* —
but a ROWS/GATE/COLLCHECK check built on `_row_url_keys`/`_doc_url_key` will disagree with REPOINTED
on exactly the page-level and wrapper citations this round exists to produce.
Also note (no action): the map's `url` and `url_variants` are not consulted by my leg — the
registry row is the URL authority my wording names; the map only supplies the substitution table and
the normalisation rule.

## 7. Residuals, risks, what I did not do

* **DRAFT debt (measured):** `claims.json` claim C `map.sha256` is `null`. Two consequences, both
  observed against the real `part-cfg.py`: `load_frozen_config` **refuses outright**
  (`ConfigError: claim map.sha256 at freeze is not a 64-hex digest (the by-document map cannot be
  pinned): None`), and my leg would report `not hash-pinned`. The L1 must freeze
  `778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155` (the map as filed) or the
  counter never grades at all — so no do-nothing control can be recorded before that byte changes.
* **Residual the leg cannot close:** a bare prose mention of a lane id that is also a staged number
  (e.g. "S890") is indistinguishable from a legitimate lane citation without the staged package,
  which is not a frozen input. Source lines are joined by document, so the harmful direction (a
  source line pointing at the staged document) is caught; a prose misattribution is the reviewer's
  job, as CritCCounterVacuity recorded.
* **Residual:** page-level collapse is only the map's rule (persee `/doc/page/`). Persée `/docAsPDF/`
  is not collapsed — the sentinel recorded that route as altcha-protected and therefore not a
  citation route at all.
* R5 is the one place I could be read as stricter than the wording (§2). If the L1 lands the
  entries without citing S893 while keeping row S893, this leg goes red and the message names the
  substitution — which is the state the claim calls "replaced", so I read the red as correct.
* Not done, by instruction and by scope: no counter run against a real landing (none exists yet), no
  build/lint/test of the assembled counter beyond the `py_compile` the CFG contract requires, no
  edit of `accept-c.py`, claims, ledger or map, no network fetch (this leg grades committed bytes
  only), no verdict on claim C as a whole.
