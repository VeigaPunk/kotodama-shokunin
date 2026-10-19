- Seat: X00 | role connector | claim cross | date 2026-10-19 | baseline `7ceff59`
- Write surface: this file only. No corpus staging, no filed-byte edits, no `run-validation.py` execution, no git/network.
- Method: all commands read-only from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Quote style below is command → observed output.

# X00 — cross-claim connector: O → census, C → couples index, Ca → O/C evidence

## 1. Top line: two of the three declared before-states are stale at HEAD

| claim | declared `before` (`reports/round-43/claims.json`) | measured at `7ceff59` | consequence |
|---|---|---|---|
| **O** | "no durable instrument implements the r39 basename-couples policy; the only resolver that ever ran (r39 I-C05) lives in ephemeral `.scratch`" (`claims.json:27`) | `tools/harness/couples-reference-extractor.py` exists (332 lines), `--selftest` → exit 0, 8/8 PASS; `--census` → `entries=223 refs=2730` (§2.1) | O is a **superset/delta**, not a from-scratch build. The r43 tool must add the per-entry mapping and disposition legs the r42 tool lacks; the claim's `after_required` already permits a "wave-named equivalent" (`claims.json:28`). |
| **C** | "myth-symbol 26 (lithic slot named but unbuilt since r42's C01/C04 collision routed this draft to spare)" (`claims.json:39`) | `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists, 192 lines, 61 884 B, sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f` — byte-identical to the **C04** draft's fenced body (`reports/round-42/cov/C04-entry-4.md:54-245`); README row at `corpus/README.md:219`; header `## myth-symbol/ (26)` at `:205` | The lithic slot is **built**, by C04. The r42 spare's own first line says C04 lands and the spare waits for "a future **re-scoped** claim" (`reports/round-42/cov/C01-mineral-spare.md:1`). r43 claim C is not re-scoped: it asks for the spare "as the partition's stone/gem/metal register entry" (`claims.json:39`). **Collision; report, do not route around** (§3). |
| **Ca** | four carried rows assert defects with no disposition (`claims.json:53`) | Holds, with one addition: the first r38-O02 finding does **not** reproduce against the filed artifact (§4.2) | Ca is still executable, but its evidence must be re-measured, not copied from the queue's reasons. |

`reports/round-42/validation.json` already states the C outcome: `"claim C: C1: C: claim FAILED as declared — myth-symbol 26 != 27, total 223 != 224 … a successor round can land the spare under a re-scoped claim."` The r42 LOG entry records the same (`LOG.md`, round-42 section: "C01/C04 authored the same lithic register; integrator ruling lands C04, routes C01 as the named spare").

---

## 2. O → census: what the resolver feeds, with measured arithmetic

### 2.1 The durable instrument that already exists

```
$ python3 tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed {... 'sound-change.md': 'prospective', 'tone-prosody.md': 'prospective'}
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens [...]
PASS glob fragment classified
EXIT=0

$ python3 tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

The wrapped positive is the live field at `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`; the exact bytes are:

```
72  - couples: language (this file, core method); myth (divine/true names, taboo
73    naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74    bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75    strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76    environment/anatomy design; prospective sibling files: sound-change.md, tone-
77    prosody.md, sound-symbolism.md, writing-systems.md
```

Per-entry read at HEAD: `wrapped=True tokens=4` — `sound-change.md` **prospective**, `sound-symbolism.md` **direct**, `tone-prosody.md` **prospective**, `writing-systems.md` **direct**. So "4/4 named targets" is satisfied; the two absent future files are *classified* (prospective), not dropped. Caution for O04/O08: the r39 policy would call those two `unresolved`; the r42 tool's fifth class `prospective` is a deliberate addition (`couples-reference-extractor.py:12-14,148-150`). The r43 census must keep the class visible and labeled, or the count silently rewrites policy history.

### 2.2 Census arithmetic chain (every row measured or filed)

| tree | entries | refs | direct | fallback | ambiguous | unresolved | prospective | glob | source |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| r39 `dfb0719` | 212 | 2504 | 2335 | 163 | 0 | 6 | — | — | `reports/round-42/calib/basename-couples-policy-full.md:220-250` (filed run of the r39 policy; the short r39 doc carries no counts) |
| r42 pre-landing `ac47c78` | 220 | 2611 | 2437 | 166 | 0 | 8 | — | — | `reports/round-42/op/couples-census-corrected.json` |
| **live `7ceff59`** | **223** | **2730** | **2556** | **166** | **0** | **2** | **5** | **1** | this seat's `--census` run |

Reconciliation (exact): `2611 + 36 + 39 + 44 = 2730`, where 36/39/44 are the r42 landings' per-entry deduplicated token counts (`purity-pollution-boundary-systems.md` 36, `sacred-topography-pilgrimage.md` 39, `mineral-stone-symbolism.md` 44), all direct. The unresolved drop `8 → 2` is **classification, not repair**: `5 prospective + 1 glob-fragment = 6` tokens moved out of `unresolved` (`-gate.md` is the glob fragment; the five are the never-written seeds plus the wrapped-field pair). If the r43 tool reports only the policy's four classes, the same tree reads `unresolved=8`, not 2. The artifact must state both views.

### 2.3 Gap list: what r43's instrument must add to the r42 one

| requirement (`claims.json:28`) | r42 extractor status | evidence |
|---|---|---|
| four classes reported **per entry** and in totals | partial: totals yes; per-entry only in `paths` mode, and `--census` prints only nonzero classes (`if v`, `couples-reference-extractor.py:309-312`) — `ambiguous=0` is omitted | run above; code line |
| every **fallback mapping** listed, not only counted | **missing** in `--census`: only the count 166; mappings appear only when each path is passed to `paths` mode (`:320-326`) | code |
| each unresolved/ambiguous row carries a **named reason** | **missing**: `resolve_entry()` has no `reason` field; census aggregates unresolved names (`:199-201`) | code |
| synthetic **ambiguous** negative control | **missing**: selftest has wrapped positive, unwrapped regression, over-capture, phantom/prospective, live 4/4, glob — no two-file same-basename control (`:242-295`) | code + selftest output |
| census filed under `reports/round-43/calib/` | r42 filed `reports/round-42/op/couples-census-corrected.json`, not `calib/` | path |
| tool at `tools/harness/basename-couples-resolver.py` | path does not exist at HEAD; only `couples-reference-extractor.py` | `ls tools/harness/` |

The r43 tool may import the r42 module or supersede it, but the census artifact must name the exact extractor path **and its sha256** so the numbers are reproducible. Do not edit the r42 file: it is a filed instrument.

### 2.4 The one live unresolved token is fully attributable (disposition-leg exemplar)

```
$ grep -rn '\.\./linguistics/phonology-sanity\.md' corpus/knowledge/
corpus/knowledge/verification/label-channel-routing-verification.md:14: ... `../linguistics/phonology-sanity.md`, ...
corpus/knowledge/synthesis/typed-label-routing-workflow.md:16: ... `../linguistics/phonology-sanity.md`; ...
```

Both are slash-bearing tokens, so policy §5.1 (`basename-couples-policy-full.md:73-81`) forbids the basename fallback: the correct class is `unresolved`, with the named reason "r19 X26-1 phantom; slash-bearing token exempt from Tier 2" and both carrier paths cited. This is the pattern O06's disposition leg must generalize: `token → class → (mapping | reason) → carrier path(s)`.

### 2.5 Recommended census artifact shape (O06/O10 fill live values)

`reports/round-43/calib/couples-census-r43.json`:

```json
{
  "schema": "kotodama-couples-census-r43",
  "round": 43,
  "date": "2026-10-19",
  "baseline_commit": "7ceff59",
  "extractor": {"path": "tools/harness/basename-couples-resolver.py", "sha256": "<fill>"},
  "policy": "reports/round-42/calib/basename-couples-policy-full.md",
  "entries": 223,
  "refs": 2730,
  "totals_policy_four": {"direct": 0, "fallback": 0, "ambiguous": 0, "unresolved": 0},
  "totals_auxiliary": {"prospective": 0, "glob_fragment": 0},
  "per_entry": [{"path": "...", "wrapped": false, "tokens": {"<ref>": {"class": "...", "mapping": "...|null", "reason": "...|null", "group": "...|null", "alignment": "..."}}}],
  "fallback_mappings": [{"entry": "...", "token": "...", "path": "..."}],
  "ambiguous": [{"entry": "...", "token": "...", "candidates": ["..."]}],
  "unresolved": [{"entry": "...", "token": "...", "reason": "..."}],
  "misaligned": [],
  "cross_checks": {"find_md": 223, "readme_total": 223, "readme_rows": 223},
  "commands": ["python3 tools/harness/basename-couples-resolver.py --selftest", "python3 tools/harness/basename-couples-resolver.py --census"]
}
```

The two `totals_*` blocks keep policy history readable: the four policy classes must always be present **including zeros**, and the auxiliary classes must never be merged into them.

### 2.6 O feeds Ca in three concrete places

- **R01-7 (D1/D2)**: the only carried finding whose disposition *depends* on the r43 artifact. If the resolver ships per-token mappings and the wrapped field reads 4/4 with the two absent targets named, R01-7 can be `fixed-with-evidence` citing the selftest output. If it ships counts only, R01-7 stays `routed-with-owner`. Do not write "fixed" on a count.
- **R01-11 (counting unit)**: the census must declare "per-entry deduplicated tokens" (policy §1) and, if it also cites a global-distinct total, label it separately. Mixing the two re-opens the finding.
- **R01-14 (the +2 anomaly)**: the resolver's `entries` counter is a reproducible cross-check against `find corpus/knowledge -name '*.md' | wc -l`; that makes a future +2 anomaly detectable, but it does not recover the lost observation (see §4.6).

---

## 3. C → couples index: the spare's footprint and the live collision

### 3.1 Live partition (observed)

```
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/myth-symbol/ | grep -iE 'mineral|stone|gem|lithic'
mineral-stone-symbolism.md
```

`corpus/README.md:5` is revision 2.4, describing exactly the three r42 myth-symbol landings including `mineral-stone-symbolism.md`; `:205` is `## myth-symbol/ (26)`; `:219` is the index row; `:548` is `(total 223 files; directory totals 25/26/25/29/24/94)`.

### 3.2 The spare's bytes and its couples footprint

The spare is a single `markdown` fence (`reports/round-42/cov/C01-mineral-spare.md:3-219`), with the integrator ruling above it at `:1`. Extraction by the r35/r42 stager shape yields 55 102 bytes including the fence-line newline, sha256 `4e6816b4069bf20d9c0ff950cad4df4252200e7da7eceaee9b53366babb488a9`; the body as C04 was actually applied (leading newline stripped, the convention that produced the live 61 884 B / `c99f44ca…`) is **55 101 bytes, sha256 `6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89`**. The discrepancy is a fence-capture artifact, not an ambiguity in the entry: report both, apply the stripped form.

Its `- couples:` field is a **single physical line** (`:22`), not wrapped, and carries **30 per-entry deduplicated tokens, all `direct`, 0 fallback / 0 ambiguous / 0 unresolved / 0 prospective / 0 glob**. Hypothetical landing as a 224th entry:

```
pre : entries=223 refs=2730 totals direct=2556 fallback=166 ambiguous=0 unresolved=2 prospective=5 glob-fragment=1
post: entries=224 refs=2760 totals direct=2586 fallback=166 ambiguous=0 unresolved=2 prospective=5 glob-fragment=1
delta: +30 direct only
```

So C's landing would be **census-neutral except +30 direct**: it exercises no fallback, ambiguous or unresolved branch, and it does not change the basename index in any way that affects an existing token (its basename is already indexed by the live C04 file). The idea that C's landing supplies a resolver test case is false; the wrapped-field case is in `linguistics/`, not this entry.

### 3.3 The collision (report, do not route around)

Three independent facts:

1. The target topic is already owned. Live title: `# Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-regalia chain` (`mineral-stone-symbolism.md:1`). Live topic line `:5`: "the lithic register … the mineral slot the register family lacks …". Spare title `:4`: `# Stone, gem, and metal — the lithic register: material properties as symbol, the scarcity ladder, and the lapidary as an institution`; spare topic `:6`: "the **lithic register** a fictional culture's symbolic grammar runs on stone, gem and metal …". Same register, same slot, same authority chain.
2. The live bytes **are** C04's draft. Extraction of `reports/round-42/cov/C04-entry-4.md:54-245` reproduces the live file byte-for-byte (`C04 fenced == live: True`, sha `c99f44ca…` both sides; the r42 C05 audit records the same staged size/digest at `reports/round-42/cov/C05-audit.md:54`).
3. The spare's own header forbids this use: "C04 lands … THIS draft is routed as the named spare for a future re-scoped claim" (`C01-mineral-spare.md:1`).

**Consequence for claim C as declared: there is no non-colliding landing path.** Landing the spare as the stone/gem/metal register duplicates the register; landing it under a different filename duplicates the topic without fixing the ownership conflict (the corpus's own rule against unmarked synonymy is `symbolism-synthesis-method.md:99`, cited in the spare itself); replacing the live entry is an overwrite, which the shared rules forbid and which is the exact r42 incident class (`LOG.md`, round-42: "two existing entries … momentarily overwritten …, restored byte-exact"). The only honest outcomes are:

| option | what it requires | verdict |
|---|---|---|
| **Drop C from r43** (recommended) | record the collision; coverage axis unchanged at 26/223; re-declare a re-scoped claim later | passes the shared rule; no corpus byte moves |
| Re-scope to a genuinely different topic | new authoring; the spare's bytes are **not** the deliverable (its scope is the whole register) | does not satisfy `claims.json:47` "the spare's fenced bytes applied unmodified" |
| Replace `mineral-stone-symbolism.md` | delete/overwrite a live entry | forbidden; r42 incident precedent |

### 3.4 If a valid 27th entry ever lands: README rev 2.5 mechanics

The README is mechanically checked by `python3 -B reports/round-28/readme/sweep.py` (the r42 revision cites 223 rows vs 223 files, exit 0, `corpus/README.md:11-12`). A valid landing must, in one act:

- add the row under `## myth-symbol/` in **filename order** (current section rows run `animal…` → `mineral…` → `motif…`, `:206-230`);
- bump the section header `## myth-symbol/ (26)` → `(27)` (`:205`);
- bump the revision-2.4 footer vector `25/26/25/29/24/94` → `25/27/25/29/24/94` and `(total 223 files …)` → `(total 224 files …)` (`:548`);
- add a revision 2.5 block at the top, dated, naming the landing and the sweep result;
- leave rev 2.4's block intact (append-only convention; the file already preserves 2.0–2.3 blocks).

No rev-2.5 block is pre-written anywhere in the repo; C02's draft is the only source.

### 3.5 Count-only validation is a trap here

The C counting commands are `ls corpus/knowledge/myth-symbol/*.md | wc -l` and `find … | wc -l` (`claims.json:43-44`). Both would read 27/224 for **any** 27th entry, including a duplicate lithic register or an unrelated file. The only guard in the threshold is "the spare's fenced bytes applied unmodified", which is exactly the colliding action. Recommend the validation add: (a) the landed filename's `- topic:` line does not duplicate an existing entry's topic owner (the r42 audit's S2 check, `reports/round-42/cov/C05-audit.md:32,35`), and (b) the README row filename equals the landed file. Without those, a green count can hide a duplicate.

---

## 4. Ca → O/C evidence: how each disposition can cite, and one row that does not reproduce

### 4.1 The four rows and their durable evidence

| queue row | finding(s) | evidence already durable | candidate class | O/C dependency |
|---|---|---|---|---|
| `r39-review-findings-disposition` (`reports/round-40/op/defect-queue-v2.json:343-351`) | R01-2..R01-14 from `reports/round-39/review/R01-review.md:25-34` | R01 file; per-finding sections; r39 C05 audit now exists (`reports/round-39/cov/C05-audit.md`, added at `fd55e1f`, completion seat) | per-finding, §4.2 | R01-7 needs O's artifact; R01-9/R01-10 can cite the r42 C landing |
| `r38-O02-fragment-defects` (`:282-290`) | D-1, D-2, D-3 (`reports/round-38/op/O03-verify.md:255-306`) | O03's command outputs; filed `reports/round-38/op/O02-isolated.md` (sha `e314dbf3…`, unchanged since `dfb0719`) | **D-1 `could-not-recover`/`recorded` — does not reproduce** (§4.3); D-2/D-3 require re-measurement | none |
| `r38-O08-fragment-defect` (`:292-300`) | D-4 digest attribution (`O03-verify.md:308-341`) | two digests: O01 `e5812751…`, O08 `ae22013b…`; one-hunk diff in O03 | `recorded` (correction record; filed bytes immutable) | none |
| `r38-O07-empty-fragment` (`:302-310`) | fragment landed 0 bytes | `wc -c reports/round-38/op/O07-scribe.md` → `0` (re-measured this seat) | `recorded` (cannot "fix" a filed empty fragment); prevention = min-bytes out-path check | none |

### 4.2 R01 family: what can be dispositioned from durable bytes today

| finding | measured state at HEAD | candidate class | citation |
|---|---|---|---|
| R01-2 (protocol names three absolute runners, measured five) | `reports/round-39/calib/isolation-replay-protocol.md:10-12` still names only r34/r35/r36; `grep -n 'five\|discriminator\|clone\|R01-'` on the 52-line file → no matches | `recorded` (filed protocol not amended) or `routed-with-owner` (successor protocol) | R01-review.md:170-188; protocol:10-12 |
| R01-3 (Tier B discriminator missing) | same grep: no "discriminator" in the filed protocol | same | R01-review.md:189-196 |
| R01-4 (r39 C05 audit absent at review close) | **fixed**: `reports/round-39/cov/C05-audit.md` exists, head says "completion seat", "R01-4 recorded C05 absent at its close" | `fixed-with-evidence` | C05-audit.md:1-10; `git log -- reports/round-39/cov/C05-audit.md` → `fd55e1f` |
| R01-5 (Tier A clone-vs-worktree declared deviation) | no "clone" text in the filed protocol; Ca01 documents it | `recorded` / `routed-with-owner` | R01-review.md:197-201 |
| R01-6 (vacuous `or True`, line nits) | `grep -n 'or True' reports/round-39/calib/Ca01-protocol.md` → `166: assert pathlib.Path.cwd() == pathlib.Path("/tmp").resolve().parent or True` | `recorded` (not fixed) | Ca01-protocol.md:166 |
| R01-7 (adopt D1+D2) | r42 extractor fixes D1 and partially D2; r43 O adds the disposition leg | **`fixed-with-evidence` only if O ships mappings+selftest; else `routed-with-owner`** | r42 extractor selftest; r43 artifact |
| R01-8 (C02 provenance label) | filed C02 fragment; note only | `recorded` | R01-review.md:75-82 |
| R01-9 (C04 staged-size pin pre-reword) | r42 successor practice pins staged bytes+sha (`C05-audit.md:54`: 61 884 B / `c99f44ca…` matches live) | `recorded` or `fixed-with-evidence` (successor practice) | C05-audit.md:54; live sha |
| R01-10 (fence-shape heterogeneity) | r42 adopted the three-backtick shape deliberately (`C04-entry-4.md:5,270`; `C05-audit.md:281`) | `fixed-with-evidence` (practice adopted) | those lines |
| R01-11 (C01 head-block calibration) | successor r42 entries carry `- calibration:`; note only | `recorded` | R01-review.md:144-146 |
| R01-12 (taboo 9 vs 10) | note; no artifact fix | `recorded` | R01-review.md:278-292 |
| R01-13 (G2–G4 unallocated) | note; carry on gap list | `recorded` | R01-review.md:293-295 |
| R01-14 (+2 anomaly) | no durable artifact; R01 itself says so | **`could-not-recover`** + owner R01/integrator | R01-review.md:296-307 |

### 4.3 r38-O02 D-1 does not reproduce — measure before copying the queue's reason

The queue row says O02 records `44` controls and the artifact yields `45` (`defect-queue-v2.json:286`), and O03 §4.1 quotes "58-member build … plus 44 controls" (`O03-verify.md:259-266`). The filed O02 artifact at HEAD says the opposite everywhere:

```
$ grep -n '44 controls' reports/round-38/op/O02-isolated.md
(no output; exit 1)
$ grep -n '45 controls' reports/round-38/op/O02-isolated.md
20: `--selftest` is exit 0 with 45 controls (m15a named / m15b green), ...
62: | ... | `selftest: OK — positive run (…) plus 45 controls`, incl. ...
203:    "plus 45 controls" incl. ...
$ sha256sum reports/round-38/op/O02-isolated.md
e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d
$ git show dfb0719:reports/round-38/op/O02-isolated.md | sha256sum
e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d -
```

The file is byte-identical to the r38 commit; there is no `44` variant in it. D-1 therefore cannot be "fixed" or "recorded as an O02 defect" without naming the missing text. The defensible dispositions are `could-not-recover` (the quoted erroneous text is not in the filed artifact; owner: O03/Ca) or `recorded` (a correction to the review's citation, not to O02). Ca02 must run the same grep before agreeing with Ca01.

D-2/D-3 are quote-level claims and must be checked the same way, not inherited. For D-2, the only "names nothing" at HEAD is `O02-isolated.md:99`, about the *rendered-text guard* being vacuous, not about m15b; m15b is described as "green"/"in-sync roster green" at `:20,:62,:203`. For D-3, `O02-isolated.md:160-164` actually names `v3_verify_component_digests` and `E2E-DIGEST` first, then says the guard surfaces through the assembled-vs-frozen compare — O03's characterization ("names the wrong leg") is at minimum an over-reading. Both need Ca02's independent measurement before any class is assigned.

### 4.4 Ordering rule (cross-claim)

1. **O lands first**: the resolver + selftest + census define the counting unit and the disposition evidence.
2. **C decides**: if C fails as declared (recommended), the corpus total stays **223**; if a valid 27th entry ever lands, the total becomes 224 and the census re-runs.
3. **Ca dispositions last**: every count in them cites the final census artifact, never a projected 224 and never "the spare landed". A disposition that says "224" while the tree has 223 is a fabricated measurement.

### 4.5 Citation hygiene for Ca

- Each `fixed` claim needs a **re-run command output**, not a pointer to another fragment. Example: R01-4's fix cites `ls reports/round-39/cov/C05-audit.md` plus the file's completion-seat header, not merely "C05 landed".
- Each `recorded` claim cites the filed bytes and says explicitly "filed bytes immutable; correction is this new record".
- Each `could-not-recover` names the owner and the search performed (e.g. `grep -n '44 controls'` → no match; sha unchanged since `dfb0719`).
- No row may cite the r43 C landing as evidence unless that landing is actually in the tree at the time of writing. The r42 spare is not a landing.

---

## 5. Handoff to the integrator

1. **C is not landable as declared.** The live partition already owns the lithic register with C04's bytes (`c99f44ca…`), and the spare's own header reserves it for a re-scoped claim. Do not apply `C01-mineral-spare.md` to `corpus/knowledge/myth-symbol/`. Record the collision and either drop C or re-declare it.
2. **O is a superset task, not a greenfield one.** Start from `tools/harness/couples-reference-extractor.py`; add the per-entry mapping/disposition leg, the ambiguous control, explicit zeros, and the calib artifact. Keep `prospective`/`glob-fragment` visible; do not merge them into the four policy classes.
3. **Ca can proceed independently of C**, but its first r38-O02 row needs `could-not-recover`/`recorded`, not the queue's "D-1 wrong count" story. Ca02 should re-measure D-1/D-2/D-3 against `O02-isolated.md` (sha `e314dbf3…`) before agreeing.
4. **O→Ca gate**: R01-7's disposition is only `fixed-with-evidence` if the r43 resolver prints token→mapping/reason rows and the wrapped-field selftest. Otherwise it is `routed-with-owner`.

## 6. Commands run (durable evidence for this file)

```text
python3 tools/harness/couples-reference-extractor.py --selftest        # 8 PASS, exit 0
python3 tools/harness/couples-reference-extractor.py --census          # 223 / 2730 / 2556+166+0+2+5+1
python3 tools/harness/couples-reference-extractor.py corpus/knowledge/linguistics/phonetics-phonology.md
                                                                        # wrapped=True, 4 tokens, 2 direct + 2 prospective
nl -ba corpus/knowledge/linguistics/phonetics-phonology.md | sed -n '72,78p'
ls corpus/knowledge/myth-symbol/*.md | wc -l                            # 26
find corpus/knowledge -name '*.md' | wc -l                              # 223
sha256sum corpus/knowledge/myth-symbol/mineral-stone-symbolism.md       # c99f44ca…, 61 884 B
python3 - <<'EOF'  # fence extraction: C04 body == live (True); spare trimmed 55 101 B / 6999a912…
EOF
grep -rn '\.\./linguistics/phonology-sanity\.md' corpus/knowledge/     # two carriers
wc -c reports/round-38/op/O07-scribe.md                                 # 0
grep -n '44 controls' reports/round-38/op/O02-isolated.md               # no match, exit 1
grep -n '45 controls' reports/round-38/op/O02-isolated.md               # :20,:62,:203
sha256sum reports/round-38/op/O02-isolated.md; git show dfb0719:… | sha256sum  # identical e314dbf3…
grep -n 'or True' reports/round-39/calib/Ca01-protocol.md               # :166 still present
grep -n 'five\|discriminator\|clone\|R01-' reports/round-39/calib/isolation-replay-protocol.md  # no matches
```

No `reports/round-43/run-validation.py` was executed (it does not exist at this writing); no filed byte was edited; the only write was this file. Temporary scratch used for the hypothetical 224-entry census was removed (`rm -rf .scratch/x00`).

## 7. To-verify (named, not asserted)

- Whether the integrator has any recorded ruling after r42 that re-scopes the C01 spare. None was found in `LOG.md`, `SCORECARD.md`, `reports/round-42/validation.json`, or `reports/round-43/claims.json`; the r43 claim itself is the only text asserting the unbuilt-slot premise.
- Whether D-2/D-3 reproduce as quoted (Ca02's independent run; §4.3 gives the exact lines and greps).
- The r43 resolver's final sha256 and the census artifact's exact figures — to be filled by O06/O10 after the integrator applies the draft.
