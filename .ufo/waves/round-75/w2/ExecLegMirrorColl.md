# ExecLegMirrorColl — claim-C legs SCRATCHMIRROR + COLLCHECK (round 75, wave 2)

Seat: executor (leaf). Lane `kotodama-shokunin`, base `f556d1049fe651d3d63975600b13acd9fb686f15`.
Written: `.ufo/waves/round-75/w2/parts/leg-mirror-coll.py` (the only part file; nothing else in
the lane was modified) and this report. `claims.json` / `ledger.json` read, never edited;
`accept-c.py`, `scripts/`, `templates/`, `.ufo/state`, the fleet repo and the shokuknow tree were
read only. No git/jj state touched in the lane (every git call in the fixture work named
`-C <scratch fixture>` after asserting its toplevel). No tool installed or upgraded.

Part file (final bytes):

    41a962f7b84fec514abf3ac93bf8b91e1e88872fcba31c00b87c21850ce97cc1  leg-mirror-coll.py
    343 lines; definitions: _mirrorcoll_ids _mirrorcoll_brief _mirrorcoll_detail
    _mirrorcoll_text leg_scratch_mirror _guard_files _negated leg_collcheck
    (module-level: docstring + defs only, AST-checked; no imports;
    `python3 -B -m py_compile` clean standalone)

## 1. The leg wording as I read it

Frozen text (`reports/round-75/claims.json`, claim C `legs[]`, quoted verbatim):

> **SCRATCHMIRROR**: `.ufo/waves/round-75/assimilation/validate-receipt.txt` shows
> `validate --file` exit 0 on a mirrored corpus carrying the frozen rows and entries, committed
> strictly before the registry-append commit

> **COLLCHECK**: reg-ids/staged-ids/collisions files and guard-proof show a planted
> 1-3-space-indented collision found and a 4-space one not found; no adopted lane id is in
> reg-ids; the map maps staged->lane by document for every adopted id

Split into graded predicates:

SCRATCHMIRROR — (a) the receipt exists at `<lands>` at the frozen path; (b) its bytes show a
`validate … --file` invocation and `exit` 0; (c) they carry every frozen adopted id; (d) they
carry every frozen entry basename; (e) the commit that adds the receipt is strictly before the
commit that adds the first frozen row to `corpus/SOURCES.md`, both on `<lands>`' first-parent
chain above the claim base.

COLLCHECK — (f) the three lists exist and are non-empty; (g) no adopted lane id is in `reg-ids`
or in `collisions`; (h) every staged id the frozen `row_set` names is in `staged-ids`;
(i) `reg-ids` is the claim-base registry's id set; (j) `collisions` is `comm -12` of the two
lists; (k) the guard proof carries a planted 1-3-space row whose id is a staged id the registry
does not hold, with a positive detection marker and no 4+-space form; (l) it carries a 4-space
control that is *not* matched by the 1-3-space grammar, with a not-found marker; (m) the frozen
by-document map has, for every adopted id, at least one staged->lane record, covers every staged
id of that row, and every record's URL names a document the landed row's source cell names.

## 2. Ambiguities and how I resolved them

1. **"committed strictly before the registry-append commit" — which chain?** Graded on
   `<lands>`' **first-parent** chain in `base..<lands>` (the seat prompt's instruction), not on a
   per-path `rev-list`: a side-branch receipt commit that is not on the chain the L1 lands on is
   not "before". The append commit is the first chain commit whose `corpus/SOURCES.md` blob
   holds the first frozen row id (S885). A receipt added *in* that commit fails
   (`in the registry-append commit (not before)`); a receipt *touched after* it fails
   (`touched after`), because the graded receipt bytes would then not be the pre-append receipt.
   The chain walk is seeded from the claim base's own blob, so a file that already existed at
   the base can never be read as this round's commit.
2. **"carrying the frozen rows and entries" — receipt text or re-run?** Graded from the
   committed receipt's named ids and entry **basenames**. The mirror tree is a scratch artifact
   and is not required to be committed; re-running `validate --file` inside a leg would grade a
   live input, and CENSUS already owns execution. A receipt that names every frozen id and every
   entry basename is what the frozen wording asks the receipt to *show*.
3. **Entry basenames are matched exactly**, `narrative-structure-frameworks.md`,
   `…​.amend-2026-10-23.md`, `…​.amend-2026-10-23b.md` — the third is not a substring of either
   other, so a two-entry receipt cannot pass by accident.
4. **`reg-ids` provenance.** The wording only forbids adopted ids in `reg-ids`, which is vacuous
   over an arbitrary list; the seat instruction directs a re-derivation, so the leg re-derives
   the claim-base registry id set (rows at 0-3 leading spaces) and requires equality. A
   post-append `reg-ids` (which would contain S885..S893) therefore fails twice — on the adopted
   id and on the set.
5. **`collisions` provenance.** Its only meaning is `comm -12` of the two lists; the leg
   recomputes the intersection and requires set equality, so a hand-edited or stale collision
   list is red.
6. **"planted 1-3-space-indented collision".** A *collision* needs the planted id to belong to
   the staged universe while absent from the registry — the leg requires
   `planted_id ∈ staged-ids` and `planted_id ∉ reg-ids ∪ base ∪ lands ∪ adopted`. The plant must
   also exist as a **row in the committed proof bytes** (1-3 leading spaces, inside the guard
   dir): prose that only asserts "found" has nothing to re-extract and fails. A plant whose id is
   not a staged id (a fabricated collision) fails. Same for the 4-space control: it must be a
   real 4-space row, must not match the 1-3-space grammar, and must sit next to a negated,
   not-found marker.
7. **Marker lines.** "found" lines must be non-negated and carry a positive token
   (`collision|detect|present|found|…|exit 1`); "not found" lines must be negated
   (`not|no|none|zero|missed|absent|never|n't`) and carry a negative token (`not found`,
   `no collision`, `0`, `missed`). The proof file's own planted-row lines are excluded from the
   marker scan so a row cannot be its own evidence.
8. **"maps staged->lane by document" with multi-id rows.** `row_staged[id]` is a **list**
   (`S885 ← S876/S885/S917/S921`); the leg requires *every* frozen staged id of a row to map to
   it (`want ⊆ olds`, so an extra prose-only record such as S744→S885 in a later map revision
   does not red the leg) and requires at least one record per adopted id. "By document" is
   `urls_compatible` (PART A): exact (host, path), or one path contained in the other — which
   folds the persee page-level transcription view onto its document and the `%20`/space form of
   the iris URL onto itself. A record whose URL names a different document fails.
9. **Where the guard proof lives.** `guard-proof/` under the assimilation tree, with a fallback
   to the whole assimilation tree if that directory is absent (still committed bytes).
10. **`lands == <freeze>` (do-nothing control).** SCRATCHMIRROR is red (no receipt, empty chain);
    **COLLCHECK is green** at the freeze tree, because the id lists, guard proof and map are
    wave-1 provenance artefacts that the freeze commit carries. That is correct for this leg and
    needs no fix, but the L1 should not expect COLLCHECK to redden the freeze control — the
    control's data-legs-red requirement is carried by ENTRIES/ROWS/EVIDENCE/GATE/INDEX.
11. **Detail line bound.** CFG-CONTRACT fixes the first detail line at ≤ 300 chars; multi-clause
    reds are summarised as the first three reasons plus a count and then cut at 296 chars minus
    the info tail (the runner asserts the bound for every leg call; measured max across all
    cases: **297**).

## 3. Test: real mock landing, real inputs, named mutants

Fixture: `git clone --shared` of the lane into scratch, `checkout --detach` at base, toplevel
asserted before every commit. Per case: a **freeze** commit (the real draft `claims.json`, the
real `reg-ids`/`staged-ids`/`collisions`, the real `guard-proof/` tree, the real
`id-renumber-map.json`), then a **receipt** commit, then an **append** commit adding the nine
S885–S893 rows (synthetic rows shaped `| S885 | <document URL> | docs | A | notice | anchor |
teaches | mined | 2026-10-27 | 180d | <entry> |`, so the map/URL limb is exercised). The
**positive receipt is the real draft receipt plus one line naming the third entry**, because no
final receipt exists yet (see §4 finding 1); the two-entry mutant is the real draft receipt
byte-for-byte.

Executed as one namespace: PART A (lines 1-510 of `.ufo/waves/round-75/counters/accept-c.py`) +
`part-cfg.py` **not yet written**, so the two shared helpers my part calls were supplied from the
round-74 template (`_row_url_keys` from part-cfg, `_map_records` from leg-repointed — my part
calls them and defines neither) + my part + a hand-built `cfg` per CFG-CONTRACT (rows S885–S893,
`row_staged` lists, 3 entries, `map_path`/`map_sha256` = `778068a4…56d5155`, `base` = the lane
base) + `ctx` with `mat` = the fixture checkout at lands and `mat_base` = `git archive base`.
The runner is one scratch file (`test.py`): it builds and grades every case in a single pass and
asserts `len(detail) <= 300` per leg. The table below is from the **final** part bytes
(`41a962f7…`), i.e. including the base-seeding of the receipt/append detection (the receipt and
S885 are absent at the claim base, so no case changes behaviour; it only stops a pre-existing
file from being read as this round's commit).

Result table (verbatim leg output; `receipt@i append@j` are first-parent chain indices above the
base; `guard=indent/four`):

```
positive            SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
positive            COLLCHECK      PASS  ids=808 staged=132 collisions=26 guard=ok/ok map=12
lands-freeze        SCRATCH_MIRROR FAIL  receipt missing: .ufo/waves/round-75/assimilation/validate-receipt.txt
lands-freeze        COLLCHECK      PASS  ids=808 staged=132 collisions=26 guard=ok/ok map=12
r-order-same        SCRATCH_MIRROR FAIL  receipt committed in the registry-append commit (not before); receipt@1 append@1 rows=9 entries=3
r-order-same        COLLCHECK      PASS  ids=808 staged=132 collisions=26 guard=ok/ok map=12
r-order-after       SCRATCH_MIRROR FAIL  receipt touched after the registry-append commit; receipt@2 append@1 rows=9 entries=3
r-order-after       COLLCHECK      PASS  ids=808 staged=132 collisions=26 guard=ok/ok map=12
r-exit1             SCRATCH_MIRROR FAIL  receipt does not show exit 0; receipt@1 append@2 rows=9 entries=3
r-exit1             COLLCHECK      PASS  ids=808 staged=132 collisions=26 guard=ok/ok map=12
r-two-entries       SCRATCH_MIRROR FAIL  receipt does not carry the entry narrative-structure-frameworks.amend-2026-10-23b.md; receipt@1 append@2 rows=9 entries=3
r-two-entries       COLLCHECK      PASS  ids=808 staged=132 collisions=26 guard=ok/ok map=12
c-reg-S885          SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-reg-S885          COLLCHECK      FAIL  S885 present in reg-ids (adopted id is not free); reg-ids is not the claim-base registry id set (file 809, base 808; missing -; extra S885); collisions is not comm -12 of the id lists (file 26, derived 27; missing S885; extra -); ids=809 staged=132 collisions=26 guard=ok/ok map=12
c-regids-stale      SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-regids-stale      COLLCHECK      FAIL  reg-ids is not the claim-base registry id set (file 807, base 808; missing S500; extra -); ids=807 staged=132 collisions=26 guard=ok/ok map=12
c-staged-missing    SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-staged-missing    COLLCHECK      FAIL  staged id S921 (-> S885) absent from staged-ids; ids=808 staged=131 collisions=26 guard=ok/ok map=12
c-collisions-stale  SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-collisions-stale  COLLCHECK      FAIL  collisions is not comm -12 of the id lists (file 25, derived 26; missing S884; extra -); ids=808 staged=132 collisions=25 guard=ok/ok map=12
c-coll-adopted      SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-coll-adopted      COLLCHECK      FAIL  S885 listed in collisions; collisions is not comm -12 of the id lists (file 27, derived 26; missing -; extra S885); ids=808 staged=132 collisions=27 guard=ok/ok map=12
c-guard-prose       SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-guard-prose       COLLCHECK      FAIL  no indent-guard proof under .ufo/waves/round-75/assimilation/guard-proof (a staged-id row planted at 1-3 spaces with a positive detection marker); no four-space control under .ufo/waves/round-75/assimilation/guard-proof (a staged-i...; ids=808 staged=132 collisions=26 guard=missing/missing map=12
c-guard-fakeplant   SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-guard-fakeplant   COLLCHECK      FAIL  no indent-guard proof under .ufo/waves/round-75/assimilation/guard-proof (a staged-id row planted at 1-3 spaces with a positive detection marker); ids=808 staged=132 collisions=26 guard=missing/ok map=12
c-guard-no4         SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-guard-no4         COLLCHECK      FAIL  no four-space control under .ufo/waves/round-75/assimilation/guard-proof (a staged-id row planted at 4 spaces with a not-found marker); ids=808 staged=132 collisions=26 guard=ok/missing map=12
c-guard-4sp-found   SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-guard-4sp-found   COLLCHECK      FAIL  no four-space control under .ufo/waves/round-75/assimilation/guard-proof (a staged-id row planted at 4 spaces with a not-found marker); ids=808 staged=132 collisions=26 guard=ok/missing map=12
c-map-missing       SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-map-missing       COLLCHECK      FAIL  map records no staged->lane for S893; ids=808 staged=132 collisions=26 guard=ok/ok map=11
c-map-wrongdoc      SCRATCH_MIRROR PASS  receipt@1 append@2 rows=9 entries=3
c-map-wrongdoc      COLLCHECK      FAIL  map record S870 -> S893 names a document the row does not: https://example.invalid/other-document.pdf; ids=808 staged=132 collisions=26 guard=ok/ok map=12
red legs: 16
```

Mutant → wording clause it violates:

| mutant | mutation | clause | verdict |
|---|---|---|---|
| positive | real receipts/map/guard, receipt in commit 1, rows in commit 2 | — | both PASS |
| lands-freeze | lands = the freeze commit | receipt/order absent | SCRATCHMIRROR red |
| r-order-same | receipt + rows in the same commit | "strictly before" | red |
| r-order-after | receipt commit after the append commit | "strictly before" | red |
| r-exit1 | every `exit=0` → `exit=1` | "exit 0" | red |
| r-two-entries | the real draft receipt, unchanged (names 2 entries) | "the frozen … entries" | red |
| c-reg-S885 | S885 appended to `reg-ids` | "no adopted lane id is in reg-ids" | red |
| c-regids-stale | S500 dropped from `reg-ids` | §2(4) base provenance | red |
| c-staged-missing | S921 dropped from `staged-ids` | frozen `row_set` staged ids | red |
| c-collisions-stale | S884 dropped from `collisions` | `comm -12` | red |
| c-coll-adopted | S885 added to `collisions` | "no adopted lane id … collisions" | red |
| c-guard-prose | planted rows stripped, prose markers kept | "show a planted … collision" | red |
| c-guard-fakeplant | 1-3-space plants re-id'd to S995/S996/S997 (not staged ids) | a *collision* needs a staged counterpart | red |
| c-guard-no4 | 4-space plant + marker removed | "4-space one not found" | red |
| c-guard-4sp-found | 4-space verdict line claims "collision detected, found" | "4-space one not found" | red |
| c-map-missing | S870→S893 record dropped | "maps … for every adopted id" | red |
| c-map-wrongdoc | S870 record URL swapped for another document | "by document" | red |

Junk paths from `CritCCounterVacuity.md` that touch this leg, and their status:

- **COLLCHECK "fabricated guard-proof prose + the expected id files/map" → now rejected** by
  three re-derivations the prose cannot fake: the plant must be a *row* in committed bytes whose
  id is a staged id the registry does not hold (c-guard-prose, c-guard-fakeplant), `reg-ids` must
  equal the base-derived set (c-regids-stale), `collisions` must equal the intersection
  (c-collisions-stale), and each map record's URL must name the landed row's document
  (c-map-wrongdoc).
- **SCRATCHMIRROR "a fabricated receipt committed before the append, naming everything" → still
  passes this leg.** The frozen wording asks the receipt to *show* the run and to be committed
  before the append; it does not ask the counter to re-execute the mirror. Rejecting that junk
  path is `CritCCounterVacuity` repair #2, which **changes the wording** — a leg may not be
  stronger than its frozen text, so the honest position is: the receipt's content and commit
  order are graded, mirror execution is not, and this is a residual risk of the frozen claim
  (not of the implementation). What the leg does reject is every receipt-shaped deviation:
  wrong order (2 mutants), wrong exit, missing adopted ids, missing entry basenames.

## 4. Findings for the L1 (pre-freeze / landing obligations)

1. **The draft receipt cannot be the final receipt.** `assimilation/validate-receipt-draft.txt`
   (23 703 B) contains **0** occurrences of `amend-2026-10-23b` — it was written for the
   two-entry era. With the three frozen entries, SCRATCHMIRROR is red on it as it stands
   (`r-two-entries`). The final `validate-receipt.txt` must be regenerated from a mirror carrying
   all three entries and name all three basenames, and it must be committed in a **commit
   strictly before** the commit that appends S885.
2. **Ordering is a landing obligation, not a counter artefact**: receipt commit, then the
   registry-append commit. Same-commit or later → red.
3. **The id lists, guard proof and map must be committed** inside the lane (they are read from
   `<lands>` via `mat`); at base they are untracked wave-1 drafts.
4. **`map.sha256` must be set at freeze**
   (`778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155`, the current
   `id-renumber-map.json` hash, matching `ExecRenumber.md`). My hand-built test `cfg` used that
   constant; FROZENCFG/part-cfg own its enforcement.
5. **`rejects.refused_staged_not_appended` is prose, not an id list** — `ExecRenumber.md` §5.1.
   `part-cfg`'s `_id_list` would raise `ConfigError` on it; that is the cfg owner's fix, not
   mine, but it blocks every leg from ever grading.
6. **COLLCHECK is green at `lands == freeze`** (§2.10). The freeze control's red must come from
   the data legs.

## 5. Interface notes (siblings)

- `ExecCtrCfgMain` (part-cfg.py): my leg calls `_row_url_keys(lands_rows, sid)` (round-74
  signature) and reads `cfg` keys `rows, row_staged, reused, entries, base, freeze, map_path`.
  `row_staged` values **may be lists** — `_mirrorcoll_ids` normalises list/string/bare-id, so
  either shape works, but the cfg contract's list is what the code prefers.
- Repointed seat (`leg-repointed.py`): my leg calls `_map_records(ctx)` expecting
  `{(old_id, new_id): url}` read from `git show <freeze>:<map.path>`; if that signature changes,
  COLLCHECK's map clauses break (they are the only consumer besides REPOINTED).
- `_guard_files` and `_negated` are defined here as the contract assigns; no sibling part may
  define those names (the assembly is a flat namespace). My own extras are prefixed
  `_mirrorcoll_`.
- No new imports, no top-level code, no network, stdlib only, deterministic;
  `python3 -B -m py_compile` clean standalone and in the assembled namespace (see §3).

## 6. Independent re-derivation of the real inputs (not trusting the landed files)

Run in scratch, read-only, from the real sources:

```
git show f556d104…:corpus/SOURCES.md | grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' | grep -oE 'S[0-9]+' | sort -u
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md | grep -oE 'S[0-9]+' | sort -u
comm -12 reg-ids staged-ids
```

- reg-ids **808** ids, staged-ids **132**, `comm -12` **26** — and all three outputs are
  **byte-identical** to the landed `assimilation/{reg-ids,staged-ids,collisions}`
  (sha256 `dd090b02…44e859e`, `bab11d7d…4c25ddad`, `01ad6576…a357754`); the staged package file
  hashes `7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754`, matching the
  reported inputs. So my leg's two re-derivations (base registry set, `comm -12`) hold on the
  real bytes, and on the real guard proof the positive case reports `808 / 132 / 26 /
  guard=ok/ok / map=12`.
- The real `guard-proof/proof.txt` plants S985/S986/S987 (1/2/3 spaces) and S988 (4 spaces) —
  all four are staged ids the base registry does not hold, exactly the shape §2(6) requires.
- The real map's 12 `assignments` cover the nine adopted ids with exactly the staged sets the
  frozen `row_set` names (S885 ← S876/S885/S917/S921; one staged id for each other row).

## 7. Residual risks

- SCRATCHMIRROR authenticates the receipt's text and commit order, not a mirror execution (§3,
  the frozen wording's own limit; a wording repair would need the L1's freeze-time decision).
- COLLCHECK trusts `staged-ids` content only to the extent of (i) containing every frozen staged
  id and (ii) making `collisions` the intersection; the staged package lives outside the repo,
  so the counter cannot re-read it (the leg grades archived bytes, per the contract). The real
  file was re-derived here (§6) and is byte-identical.
- Duplicate-definition collision on the shared flat namespace (`_negated`, `_guard_files`) is a
  contract-ordered risk, not observed: no sibling part existed when this was written.

## 8. Scratch

Everything lived under `/fast/scratch/hyaku/kotodama-r75/ExecLegMirrorColl/` (per-case fixtures
under `cases/`, the combined builder+runner `test.py`, the leg output `legs.txt`, materialized
base trees under `mat_base/`); the receipts are the verbatim table above.
**The scratch tree was deleted before yield** — and, independently of me, an external sweep wiped
the whole `/fast/scratch/hyaku/kotodama-r75/` tree mid-session (all sibling seat dirs were
recreated with fresh timestamps); the matrix above was rebuilt from scratch and re-run against
the final part bytes after that, so no receipt depends on the pre-sweep fixtures. No `/tmp` path
is cited anywhere. No tool installed.
