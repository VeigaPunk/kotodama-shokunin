- Seat: P01 | planner | cross | date 2026-10-19 | baseline `7ceff59`
- Claim: cross (plans O, C, Ca; implements none) | out: `reports/round-43/plan/P01-plan.md`

# Round-43 plans — O (operability), C (coverage), Ca (calibration)

Planner's note. This seat is read-only: every **MEASURED** line below was produced by a
command this seat ran against the live tree at `7ceff59`, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; the command or its output is
quoted so a verifier can reproduce it. No `run-validation.py` was executed. Nothing was
written outside this out path.

Two of the three claim premises do not survive contact with HEAD:

1. **Claim C is blocked at a hard collision.** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`
   already exists and is byte-equal to r42's C04 fenced block. The lithic slot is **built**,
   not "named but unbuilt" (`reports/round-43/claims.json:40`). The C01 spare is the *same
   topic*; landing it would either overwrite a filed corpus entry or create a duplicate
   topic. §2 gates on this and proposes no route around it.
2. **Claim O's `before` is stale.** A durable successor instrument already exists:
   `tools/harness/couples-reference-extractor.py` (r42 claim O, sha256 below). It passes
   8/8 selftest controls, reads the wrapped field 4/4, and classifies the corpus. What is
   genuinely missing is narrower: the **per-fallback mapping list**, the **disposition leg**
   for unresolved/ambiguous rows, a **census artifact**, and three control types. §1
   re-scopes O to "harden the existing successor" and says so explicitly, so the round does
   not score a build that already happened.

Claim Ca's premise holds: the four queue rows are still `carried-with-owner` and no
per-finding disposition exists in any round record (`grep -c 'R01-' reports/round-39/validation.json`
→ **0**, confirmed by this seat). §3 fixes the row enumeration at 19.

---

## 0. Anchors measured at plan time

All commands from the lane root, read-only.

| # | anchor | measured value |
|---|---|---|
| 0.1 | partition size | `ls corpus/knowledge/myth-symbol/*.md \| wc -l` → **26**; `find corpus/knowledge -name '*.md' \| wc -l` → **223** |
| 0.2 | live lithic entry | `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, 61,343 bytes, 192 lines, sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f` |
| 0.3 | C04 block identity | `reports/round-42/cov/C04-entry-4.md` fenced block + `"\n"` hashes to **the same** `c99f44ca…`; `live == block + newline` → **True** |
| 0.4 | C01 spare block | `reports/round-42/cov/C01-mineral-spare.md` fenced block, 54,730 chars, sha256 `8bd33addf3aea4a46be5154e77fc25bfff4b0ae6e9bd05647876dbe6d50ef2f6` |
| 0.5 | r42 C verdict | `reports/round-42/validation.json` → **FAILED as declared**: `myth_symbol 26 != 27, total 223 != 224`; ruling: "C04 lands, C01 routes as the named spare" |
| 0.6 | README state | `corpus/README.md:5-12` rev **2.4**: "three myth-symbol entries landed (`mineral-stone-symbolism.md`, …); a fourth draft (C01's lithic register) collided with C04's and is routed as a named spare" |
| 0.7 | extractor identity | `tools/harness/couples-reference-extractor.py`, sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` |
| 0.8 | extractor selftest | `python3 tools/harness/couples-reference-extractor.py --selftest` → exit 0, **8/8 PASS**, incl. `wrapped positive 4/4 tokens` and `N6 regression guard: block read yields 4 tokens` |
| 0.9 | live census | `--census` → `entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1`; `wrapped fields: 1`; `unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)`; `misaligned: none` |
| 0.10 | fallback population | 166 per-entry fallback rows = **50 distinct** `token -> corpus-relative path` mappings (all 50 one-to-one) |
| 0.11 | ambiguity state | live basename index over `corpus/knowledge/*/*.md`: **0 duplicate basenames**; `ambiguous=0` |
| 0.12 | O07 evidence | `wc -c reports/round-38/op/O07-scribe.md` → **0** |
| 0.13 | O02 filed bytes vs the queue row | The queue's D-1/D-2 quotes are **not in the filed fragment**. `git show dfb0719:reports/round-38/op/O02-isolated.md` sha256 `e314dbf3e54f9e846c4fed68be6811fcb9dfd4e6589ede0554ae6d9ade066f9d` = HEAD; `grep -c '44 controls'` → **0**, `grep -c '45 controls'` → **3**; no `58-member`/`59-member` text. O03 `:255-279` measured a pre-filing variant. D-3's alleged prediction is also not verbatim: filed `O02-isolated.md:161-162` already names the per-component digest leg |
| 0.14 | O08 digest provenance | `reports/round-38/op/O08-regression.md:83` asserts `ae22013b…` "is exactly the digest O01 §6 declares"; `O03-verify.md:308-341` measures O01's declared digest as `e5812751…` and O08's as its own `m15b` variant |
| 0.15 | landed r39 protocol | `reports/round-39/calib/isolation-replay-protocol.md` is **52 lines / 2,829 bytes**, ends at the bare heading `## 3. Step 0 — determine the close commit`; it names **three** absolute runners (`:10-13`) and carries no Tier-B discriminator, no clone-vs-worktree deviation note, no `or True` line |
| 0.16 | r39 policy filed vs successor | `reports/round-39/calib/basename-couples-policy.md` is **107 lines**, ends mid-§6 (`:104-107`); `reports/round-42/calib/basename-couples-policy-full.md` is **263 lines** with the full §6 script + §7. The r42 successor restores the truncation; it does **not** add D1/D2 text (grep `blocker\|C12\|disposition` → only incidental hits) |
| 0.17 | R01 disposition debt | `grep -c 'R01-' reports/round-39/validation.json` → **0**; only R01-1 is folded in `reports/round-39/calib/recount-ledger-successor.json:8` |

**Wrapped field bytes** (the positive control target), `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`:
`- couples:` at `:72`, five two-space continuations `:73-77`, blank line `:78`. The four
`.md` tokens are `sound-change.md`, `tone-prosody.md` (soft-wrapped as `tone-` + `prosody.md`
across `:76-77`), `sound-symbolism.md`, `writing-systems.md`. Under the r42 extractor they
classify **2 direct** (`sound-symbolism.md`, `writing-systems.md`) + **2 prospective**
(`sound-change.md`, `tone-prosody.md` — declared "prospective sibling files" in the field).
This is the correct 4/4 reading; the older r42 note "2 direct / 2 unresolved"
(`reports/round-42/op/O11-final.md:92`) predates the `prospective` class.

---

## 1. Claim O — harden the existing successor instrument

### 1.1 Premise correction (must be recorded, not silently absorbed)

`reports/round-43/claims.json:27` says "no durable instrument implements the r39
basename-couples policy; the only resolver that ever ran (r39 I-C05) lives in ephemeral
`.scratch`". That was true before r42; it is **false at HEAD**. r42 claim O landed
`tools/harness/couples-reference-extractor.py` and its verdict was "operability improved"
(`SCORECARD.md:822`). Re-declaring a build would over-claim.

The honest O before/after for r43:

- **before:** the durable extractor exists and reads the wrapped field, but its `--census`
  emits totals only (no fallback mapping list), its unresolved rows carry no disposition,
  its selftest has no ambiguous control and no clean phantom→`unresolved` control, and its
  detector cannot be regression-tested against a duplicate basename because the live index
  has none.
- **after:** the same file emits the full four-class + auxiliary census with every fallback
  mapping and every unresolved/ambiguous reason, a selftest with all five controls, and a
  filed `reports/round-43/calib/` census artifact whose arithmetic reconciles to r39 and
  r42 line-for-line.

**Do not create a second file named `basename-couples-resolver.py`.** The claim's
"(or wave-named equivalent)" clause is satisfied by the existing host; a second resolver
would fork the policy and violate the single-successor intent of
`reports/round-39/calib/basename-couples-policy.md:8-9`. Record the pre-edit sha256
(`d8d23a26…`) in the O receipt so the delta is reproducible.

### 1.2 Patch spec (O01 drafts as a fenced block; integrator applies)

Target: `tools/harness/couples-reference-extractor.py`. Extend, preserve existing public
behavior (`--selftest`, `--census`, positional paths, exit 0/1/2).

**A. Index injection (for testability only).** Change
`classify(ref, entry_dir, prospective=False)` to
`classify(ref, entry_dir, prospective=False, index=None)`, using `index if index is not None
else basename_index()`. No behavior change on live runs.

**B. Census JSON emitter.** Add `--census-json PATH` (and `--json` as alias writing to
stdout). Schema `kotodama-basename-couples-census-v1`:

```json
{
  "schema": "kotodama-basename-couples-census-v1",
  "round": 43,
  "baseline_commit": "7ceff59",
  "tool": {"path": "tools/harness/couples-reference-extractor.py", "sha256": "<post-edit>"},
  "corpus": {"entries": 223, "refs": 2730},
  "totals": {"direct": 2556, "fallback": 166, "ambiguous": 0, "unresolved": 2,
             "prospective": 5, "glob-fragment": 1},
  "policy_classes": {"direct": 2556, "fallback": 166, "ambiguous": 0, "unresolved": 2},
  "aux_classes": {"prospective": 5, "glob-fragment": 1},
  "wrapped_fields": ["corpus/knowledge/linguistics/phonetics-phonology.md"],
  "fallback_mappings": [{"token": "architecture-settlement-lexicon.md",
                          "path": "corpus/knowledge/culture-material/architecture-settlement-lexicon.md",
                          "entries": ["corpus/knowledge/civilizations/aegean-minoan-mycenaean.md", "..."]}],
  "unresolved": [{"token": "../linguistics/phonology-sanity.md", "entries": ["..."],
                   "reason": "slash-bearing; Tier 1 failed; §5.1 forbids fallback",
                   "disposition": "blocker|documented", "evidence": "..."}],
  "ambiguous": [{"token": "...", "hits": ["...", "..."], "reason": "two or more basenames"}],
  "glob_fragments": [{"token": "-gate.md", "entry": "..."}],
  "prospective": [{"token": "...", "entry": "..."}],
  "accounting": {"sum_of_buckets": 2730, "equals_refs": true, "dropped": 0}
}
```

Requirements:
- `fallback_mappings` is grouped by **distinct token->path** (50 rows now) and each row
  lists every entry that produced it; a per-entry expansion must also be available
  (`--paths` already prints it). The policy requires "every fallback mapping is listed,
  not only counted" (`reports/round-39/calib/basename-couples-policy.md:57-58`).
- `unresolved` / `ambiguous` rows carry a **reason**, never a bare count; `ambiguous` also
  lists every hit path. No token is dropped: `sum_of_buckets == refs`.
- `glob-fragment` and `prospective` stay **separate auxiliary classes**, never folded into
  `unresolved` (policy §5.6; the current extractor already does this — preserve it).
- The policy's four classes are reported both as `policy_classes` and inside `totals`, so a
  reader cannot mistake the six-bucket total for a four-class result.

**C. Disposition leg (per token).** For every `unresolved` token, emit
`disposition: "blocker" | "documented"` per the C12 row-2 rule
(`reports/round-35/cov/C12-audit-runbook.md:37`): a dangling token is a blocker unless the
same field/line marks it `(to-verify`, in which case it is `documented` and named.
Implementation note: the current `documented = bool(TO_VERIFY_RE.search(joined))`
(`tools/harness/couples-reference-extractor.py:160`) is **whole-field**; move the test to
the token's own segment/line so one `(to-verify` elsewhere in a multiline field cannot
launder a different token. For the live phantom, the field carries no `(to-verify`, so the
expected disposition is **blocker** with the named r19 X26-1 provenance
(`reports/round-19/audit/x26-spotcheck-entries.md` §3; `C14-audit-6-10.md:114-119`).

**D. Human summary.** `--census` keeps its one-line totals and adds:
`fallback mappings: 50 distinct / 166 rows (listed in --census-json)`;
`unresolved: 2 rows / 1 distinct (blocker=2)`; `ambiguous: 0`; `accounting: 2730 == 2730`;
`wrapped: 1`.

### 1.3 Selftest controls (all must pass; O02 drafts)

| # | control | fixture | expected |
|---|---|---|---|
| 1 | wrapped positive (existing) | `WRAPPED_POSITIVE` | 4 tokens; `tone-prosody.md` present, `prosody.md` absent |
| 2 | unwrapped regression (existing) | `UNWRAPPED_REGRESSION` | 2 tokens, unchanged |
| 3 | over-capture trap (existing) | `OVER_CAPTURE_TRAP` | prose `.md` mention excluded |
| 4 | **direct positive (new)** | token naming a file in the fixture's own directory | `direct`, mapping `None` |
| 5 | **phantom negative → unresolved (new)** | token with zero index hits, **not** under a prospective marker | `unresolved` + `blocker` (not `prospective`) |
| 6 | **ambiguous negative (new)** | inject `index={"dup.md": ["corpus/knowledge/a/dup.md", "corpus/knowledge/b/dup.md"]}` | `ambiguous`, hits listed, never `fallback` |
| 7 | glob fragment (existing) | `-gate.md` | `glob-fragment`, not `unresolved` |
| 8 | N6 regression guards (existing, 2 checks) | live field | single-line 0 tokens; block read 4 tokens |

Control 6 is why the index-injection refactor (A) is required: the live corpus has **no**
duplicate basenames (0.11), so an ambiguous control cannot be built from real files without
creating a corpus file, which this round forbids. Control 5 is distinct from the existing
phantom check, which asserts `prospective` on a field that declares prospective seeds.

### 1.4 Census artifact and arithmetic reconciliation

File both:
- `reports/round-43/calib/basename-couples-census.json` — the schema above;
- `reports/round-43/calib/basename-couples-census.md` — human summary + the three-era table.

Three-era comparison (each figure from a cited run):

| era | entries | refs | direct | fallback | ambiguous | unresolved | aux |
|---|---|---|---|---|---|---|---|
| r39 policy §6 filed (`reports/round-39/calib/basename-couples-policy.md:228-239`) | 212 | 2504 | 2335 | 163 | 0 | 6 | — |
| r42 pre-landing fixed extractor (`reports/round-42/op/O06-receipt.md:105-106`) | 220 | 2611 | 2437 | 166 | 0 | 8 | — |
| **r43 live** (this seat, `--census`) | **223** | **2730** | **2556** | **166** | **0** | **2** | prospective 5, glob 1 |

Reconciliation the census artifact must state, with arithmetic:
- r42's 8 "unresolved" are **not lost**: under the current classifier they are
  `2 unresolved + 5 prospective + 1 glob-fragment = 8`. The 5 prospective are the three
  never-written `language-contact.md:7` seeds plus the two wrapped-field seeds
  (`sound-change.md`, `tone-prosody.md`); the 1 glob is `-gate.md`
  (`gate-frozen-run-standard.md:15`), which policy §5.6 says must **not** be counted as a
  couples finding.
- +11 entries from 212→223; +226 refs from 2504→2730.
- r42 220→r43 223 adds **+119 refs, all direct** (2556−2437 = 119; fallback unchanged at
  166, ambiguous 0). This is a clean check: the three r42 myth-symbol landings' `couples:`
  tokens all resolve directly at HEAD.
- The corrected unresolved population is 2 rows / 1 distinct, both the X26-1 phantom
  `../linguistics/phonology-sanity.md` (carriers: `verification/label-channel-routing-verification.md:14`
  and `synthesis/typed-label-routing-workflow.md`). It is a **blocker** by C12 row 2 and
  must be reported as such, not silently zeroed.

### 1.5 Verification and commands

Counting commands (the claim's list, corrected — `reports/round-43/run-validation.py` does
**not exist** at plan time; the integrator must author it, or the third command is
`could-not-evaluate`):

```bash
python3 tools/harness/couples-reference-extractor.py --selftest        # exit 0, 10/10 checks
python3 tools/harness/couples-reference-extractor.py --census          # summary + accounting
python3 tools/harness/couples-reference-extractor.py --census-json reports/round-43/calib/basename-couples-census.json
python3 -c 'import json; d=json.load(open("reports/round-43/calib/basename-couples-census.json")); print(d["accounting"], len(d["fallback_mappings"]), d["totals"])'
```

Acceptance:
1. selftest exit 0 with controls 1-8 above;
2. live wrapped field 4/4 with `prosody.md` never emitted;
3. `fallback_mappings` has 50 distinct rows and every one carries a path;
4. `accounting.equals_refs` true and `dropped == 0`;
5. `unresolved` has 2 rows, each with a reason + disposition; `ambiguous` 0 (with control 6
   proving the code path).
6. Two independent verifiers: O04 traces the parse against the wrapped bytes; O05 hunts the
   traps (anchor `:NN`, brace expansion, two-hit basename, couples-as-last-header). A
   verifier may not be the O01 author. O08 checklists against policy §§1-5; O12 proves no
   write outside `tools/harness/` + `reports/round-43/`.

### 1.6 Owed / dependencies

- Integrator: author `reports/round-43/run-validation.py` if the claim is to be graded by
  its declared third command; otherwise the O verdict cites the selftest + census runs.
- Integrator: record the premise correction (§1.1) in the round record. The axis move is
  "hardened successor + filed census", **not** "built missing instrument".
- Owner for the live phantom remains the corpus leg (`r19 X26-1`), not this tool.

---

## 2. Claim C — BLOCKED at the collision gate

### 2.1 What the claim says, and what HEAD says

`reports/round-43/claims.json:40`:
> "myth-symbol 26 (lithic slot named but unbuilt since r42's C01/C04 collision routed this
> draft to spare); total 223"

HEAD:
- `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists (0.2) and is byte-equal
  to r42's **C04** block + newline (0.3). Its title is
  "Stone, gem and metal symbolism — the lithic register: the lapidary code, material
  prestige, and the quarry-to-regalia chain".
- The r42 README rev 2.4 says three entries landed, naming `mineral-stone-symbolism.md`
  first, and the fourth (C01's lithic register) is the routed spare (0.6).
- The r42 validation receipt records the collision ruling and the C failure (0.5).
- The C01 spare's own `- gap filled:` line still asserts "**no entry owns stone**"
  (`reports/round-42/cov/C01-mineral-spare.md:7`), which is **false at HEAD**. Its
  `- couples:` line and body also point at the same neighbours as the live C04 entry.

Conclusion: the lithic slot is **owned**. "Landing the spare" cannot mean
"complete the named lapidary slot"; that slot is complete. The spare is a second,
structurally different draft of the same topic (title at `C01-mineral-spare.md:4`;
headings §1-§11 differ from the live entry's §1-§10). Landing it under any filename
creates a duplicate-topic pair; landing it at `mineral-stone-symbolism.md` overwrites
filed corpus bytes, which the shared rules forbid.

### 2.2 Gate C0 — result: **FAIL**

| check | command | result |
|---|---|---|
| target filename free? | `ls corpus/knowledge/myth-symbol/` | **NO** — `mineral-stone-symbolism.md` present (0.1) |
| live entry is C04's? | block+newline sha vs live sha | **YES** — both `c99f44ca…` (0.3) |
| spare topic distinct? | titles + heading sets | **NO** — both are "the lithic register" |
| spare gap statement true at HEAD? | `grep 'no entry owns stone' C01-mineral-spare.md` | **NO** — line 7 asserts it; live entry contradicts it |
| any other named lithic file? | `ls corpus/knowledge/*/ \| grep -i 'mineral\|stone\|gem\|lithic'` | only `mineral-stone-symbolism.md` |

**No landing path may be proposed from this seat.** Per the shared rule, the collision is
reported, not routed around. The C plan below is a **contingent** sequence that becomes
executable only after an integrator ruling + claims amendment; it is not a proposal to land
the C01 spare.

### 2.3 Admissible integrator rulings (planner's menu, decision theirs)

1. **Re-scope C to a different named, still-unbuilt gap** and amend
   `reports/round-43/claims.json` (new claim id or a restated C). The r42 scout ranked set
   (`reports/round-42/scout/K02-myth-gaps.md` §R1) is the input; the candidate must pass a
   fresh absence sweep at HEAD **before** a draft is selected. This is the only ruling that
   can reach 224 without duplication.
2. **Record C as blocked/could-not-evaluate for r43**, keeping the round's O and Ca moves.
   The r42 spare remains a spare; no corpus byte moves. This is honest and admissible.
3. **Do not** land the C01 spare at a new filename (`lithic-register.md`,
   `mineral-stone-symbolism-2.md`, …). It would duplicate the topic and its own gap
   statement would be false at landing. A future use of the spare requires a **distinct
   topic** — e.g. the quarry/mine production side it already names as "owed" (§Owed) if a
   gap sweep shows that topic unowned — and a fresh authorship/audit cycle, not a rename.

### 2.4 Contingent landing sequence (only after ruling 1 + a claims amendment)

0. **Re-verify the chosen target**: `ls corpus/knowledge/<partition>/`; compute
   `find corpus/knowledge -name '<basename>.md'`; stop on any hit.
1. **Freeze the draft**: extract the single fenced block with a 3- or 4-backtick-aware
   extractor (R01-10 precedent, `reports/round-39/review/R01-review.md:140-143`); record
   byte count + sha256.
2. **Fresh pre-landing audit** against `corpus/QUALITY.md:5-20` and the entry contract
   (topic/sources/couples/verified-at/recheck/scope/calibration), plus every backticked
   in-repo path resolving at HEAD. A draft authored before a prior landing must be re-audited
   because the tree changed.
3. **Collision record**: current partition listing, target absence, and a statement that no
   existing entry was overwritten.
4. **Integrator applies** the fenced bytes to exactly one new file. Seats never stage under
   `corpus/` (`targets.json:6`).
5. **README rev 2.5** (see §2.5).
6. **Sweep**: `python3 -B reports/round-28/readme/sweep.py` → `N rows vs N files`, exit 0.
7. **Post-apply census**: rows vs files, section header, totals line, footer vector, plus
   `git status --porcelain corpus/` showing exactly one new path.
8. **Delta receipt** (C05): predicted staged sha vs delivered sha, per the
   readme-prediction-vs-delivery practice; cite the post-apply sweep.

### 2.5 README rev 2.5 mechanics (contingent)

File: `corpus/README.md` (the corpus index, not the lane `README.md`). Current anchors:
- revision block starts `corpus/README.md:5` (`revision: 2.4 — Round-42 …`);
- section header `## myth-symbol/ (26)` at `:205`;
- section rows are filename-ordered; `mineral-stone-symbolism.md` sits at `:219`;
- totals line `Total knowledge entries: 223.` around `:544`;
- counts footer `(total 223 files; directory totals 25/26/25/29/24/94)` at `:548`.

Edits:
1. Insert a new `revision: 2.5 — Round-43 …` block above the 2.4 block at `:5`, naming the
   entry, the partition move, the totals move, and the sweep result. It must not repeat the
   r42 spare's "lithic slot unbuilt" framing if the entry is a different topic.
2. Bump `## <partition>/ (N)` to `(N+1)`.
3. Insert the row in **filename order** with the entry's own `- topic:` text byte-equal to
   the landed file (the sweep checks topic equality).
4. Bump `Total knowledge entries:` 223 → 224 and the footer vector: myth-symbol `26` → `27`
   if the entry is myth-symbol; other partitions unchanged. For a different partition, change
   only that component: current vector is `25/26/25/29/24/94` in README section order
   (`linguistics/myth-symbol/culture-material/synthesis/verification/civilizations`).
5. Re-measure: `python3 -B reports/round-28/readme/sweep.py`; the expected literal is
   `224 rows vs 224 files, exit 0`. Record the command output, not a promise.

### 2.6 What must not happen

- No overwrite of `mineral-stone-symbolism.md`; no `git mv`, no delete-and-replace.
- No second lithic entry under a new name.
- No README revision that claims a slot was empty when it was not.
- No seat staging under `corpus/`; the integrator applies.

---

## 3. Claim Ca — per-finding disposition list

### 3.1 Artifact and schema

File both (new records; never edit `reports/round-40/op/defect-queue-v2.json`):
- `reports/round-43/calib/dispositions-r38-r39.json` — machine list;
- `reports/round-43/calib/dispositions-r38-r39.md` — human table with the same rows.

Required per-row fields:

```json
{
  "finding_id": "R01-2",
  "parent_row": "r39-review-findings-disposition",
  "statement": "<one-line restatement of the finding, no new claim>",
  "class": "fixed-with-evidence | routed-with-owner | recorded | could-not-recover",
  "owner": "<seat/role>",
  "evidence": ["reports/round-39/review/R01-review.md:182-190"],
  "rerun": {"command": "...", "output": "...", "date": "2026-10-19"} ,
  "filed_bytes_touched": false
}
```

Class rules (binding):
- `fixed-with-evidence` requires a re-run command **and** its output, or a cited successor
  artifact that contains the fix. "Should be fixed" is not a class.
- `routed-with-owner` requires a named owner and a durable destination (queue successor,
  next re-freeze, corpus leg).
- `recorded` is for measured findings whose object is immutable (filed fragment bytes) or
  whose correction is a note, not a change.
- `could-not-recover` requires an owner and the reason the evidence cannot be recovered.
- Every row cites `file:line` or command output; unknowns are `to-verify`.

### 3.2 Row enumeration — 19 rows

R01-2..R01-14 is 13 findings; R01-7 carries two clauses (D1 extraction, D2 disposition), so
it becomes 2 rows. Plus O02 D-1/D-2/D-3 (3), O08 D-4 (1), O07 (1) = **19**.

| row | parent | finding (evidence) | re-run / evidence to cite | candidate class (Ca01 decides) |
|---|---|---|---|---|
| R01-2 | r39-review-findings-disposition | protocol names 3 absolute runners; measured set 5 (`R01-review.md:182-190`) | `grep -n 'r3[4-8].*chdir\|ROOT =' reports/round-34..38/run-validation.py`; landed protocol `isolation-replay-protocol.md:10-13` names 3 and is truncated at `:52` | **routed-with-owner** (protocol successor; landed doc partial) |
| R01-3 | same | Tier B has no wrong-tree discriminator (`:191-202`) | landed protocol grep `discriminator` → no hit; `reports/round-39/calib/Ca01-protocol.md` §? has the design | **routed-with-owner** |
| R01-4 | same | C05 audit missing at review time (`:147-150`) | `ls reports/round-39/cov/C05-audit.md` → exists; `:46` verdict 4/4 PASS | **fixed-with-evidence** (landed C05) |
| R01-5 | same | Tier A substrate is a shared clone, not a worktree (`:203-207`) | landed protocol has no deviation note (grep `clone\|worktree` → no hit) | **routed-with-owner** (record deviation) |
| R01-6 | same | `… or True` vacuous assert; chain-table line offsets (`:208-222`) | landed protocol does not carry §5; Ca01 draft does; verify the offsets with `sed -n` on r34/r35/r36 runners | **routed-with-owner** (protocol successor) |
| R01-7a | same | D1: single-line extractor zeroes wrapped fields (`:262-270`) | `python3 tools/harness/couples-reference-extractor.py --selftest` → `wrapped positive 4/4`; `couples_block` at tool `:50-97` | **fixed-with-evidence** (r42 successor) |
| R01-7b | same | D2: no blocker/documented disposition leg | current tool emits a `documented` flag but no disposition class; O §1.2-C lands it in r43 | **routed-with-owner** (O, r43) |
| R01-8 | same | C02 provenance label inexact (`:75-79`) | `reports/round-39/cov/C05-audit.md` notes it; re-grep the regex claim | **recorded** (label note; conclusions stand) |
| R01-9 | same | C04 staged-size pin is pre-reword (`:128-137`) | `reports/round-39/cov/C05-audit.md:165` F5; recompute fence sha | **recorded** (chain intact via C06) |
| R01-10 | same | fence-shape heterogeneity (`:140-143`) | `reports/round-40/cov/C05-audit.md:40` extractor handles both; the r35 stager regex still does not | **routed-with-owner** (durable stager; no C landing this round) |
| R01-11 | same | C01 lacked a head-block calibration field (`:144-146`) | `grep -n '^- calibration:' reports/round-39/cov/C01-entry-1.md` → no hit; executable bar does not require it | **recorded** (checklist note) |
| R01-12 | same | K01 `grep -lic` counts; taboo 9 vs measured 10 (`:278-287`) | rerun `grep -rli taboo corpus/knowledge \| wc -l` → 10; conclusion stands | **recorded** (corrected count) |
| R01-13 | same | G2/G3/G4 unallocated (`:288-291`) | the three r40 files exist: `taboo-strata-lifecycle.md`, `dialect-register-consistency.md`, `translation-protocol-fidelity.md`; `corpus/README.md:14-19` rev 2.3 | **fixed-with-evidence** (r40 landings) |
| R01-14 | same | transient +2 sweep anomaly, unreproducible (`:292-300`) | no durable artifact; the review itself says so | **could-not-recover** (owner: R01/integrator) |
| O02-D1 | r38-O02-fragment-defects | queue says "selftest count 44"; **absent from the filed bytes** | `git show dfb0719:reports/round-38/op/O02-isolated.md \| sha256sum` → `e314dbf3…` = HEAD; `grep -c '44 controls'` → **0**; `grep -c '45 controls'` → **3**; no `58-member`/`59-member` text | **fixed-with-evidence** (defect not present in the committed fragment; `to-verify` when it was corrected) |
| O02-D2 | same | queue says m15b is described as "names nothing"; **absent from the filed bytes** | filed `O02-isolated.md:20,:62` says "m15b in-sync roster green"; the only `names nothing` (`:99`) is the rendered-text guard control, a different object | **fixed-with-evidence** |
| O02-D3 | same | queue says §7 predicts the frozen-packet leg | filed `:161-162` already names `v3_verify_component_digests` as the firing leg; `:163-165` adds the guard-path compare. O03's measured mechanism agrees with the filed text | **recorded** (precision note; `to-verify` which compare surfaces under the guard) |
| O08-D4 | r38-O08-fragment-defect | `ae22013b…` falsely attributed to O01 (`O03-verify.md:308-341`) | recompute both digests; O01 declares `e5812751…` | **recorded** (provenance correction) |
| O07 | r38-O07-empty-fragment | scribe fragment landed 0 bytes | `wc -c reports/round-38/op/O07-scribe.md` → 0 | **recorded** + prevention `routed-with-owner` (census min-bytes; next re-freeze) |

Notes:
- R01-1 is **already dispositioned** in `recount-ledger-successor.json:8` and is outside
  this row's R01-2..R01-14 scope; the list should say so once, not re-litigate it.
- The landed `isolation-replay-protocol.md` is a **52-line partial** (0.15). No row may be
  marked `fixed-with-evidence` by citing it for R01-2/3/5/6; cite the draft only as the
  fix design and route the landing.
- O02's filed fragment is immutable. Rows D-1/D-2 are **not** "filed corrections owed": the
  committed bytes at `dfb0719` already carry the corrected values (0.13), so the queue's
  reason is stale. Ca01 must quote the committed-byte measurement, not O03's pre-filing
  reading, and must not propose an edit to `O02-isolated.md`.
- O07's prevention belongs to the integration census, not to a filed-byte edit. If the
  integrator adds a min-bytes check to the round runner, the row becomes
  `fixed-with-evidence` **only** with the runner command output; otherwise it stays
  `recorded` + routed prevention.

### 3.3 Queue successor

`reports/round-43/calib/defect-queue-v2-successor.json` (new file; parent sha256 recorded):

```json
{
  "schema": "kotodama-defect-queue-successor-v1",
  "round": 43,
  "parent": "reports/round-40/op/defect-queue-v2.json",
  "parent_sha256_at_assembly": "<sha256>",
  "dispositions": "reports/round-43/calib/dispositions-r38-r39.json",
  "rows": [
    {"id": "r39-review-findings-disposition", "successor_state": "dispositioned",
     "resolution": "19-row list filed; see dispositions-r38-r39.json", "owner": "integrator"},
    {"id": "r38-O02-fragment-defects", "successor_state": "dispositioned",
     "resolution": "D-1/D-2 absent from the committed fragment (already 45 controls / m15b green); D-3 recorded with a precision note; stale queue reason superseded", "owner": "integrator"},
    {"id": "r38-O08-fragment-defect", "successor_state": "dispositioned",
     "resolution": "D-4 recorded; provenance correction note", "owner": "integrator"},
    {"id": "r38-O07-empty-fragment", "successor_state": "dispositioned",
     "resolution": "measured 0 bytes; prevention routed to census min-bytes", "owner": "integrator"}
  ]
}
```

Never edit `reports/round-40/op/defect-queue-v2.json`; never append to it in place. The
successor file's parent sha256 makes the append-only relation checkable.

### 3.4 Verification (Ca02) and hazards

Ca02 independently re-runs:
- `wc -c reports/round-38/op/O07-scribe.md` → 0;
- `grep -n '44 controls' reports/round-38/op/O02-isolated.md` and the O03 counter readings;
- the O08/O01 digest recomputation (`sha256sum` on the two patched trees or the filed
  digests quoted at `O08-regression.md:80-83` and `O03-verify.md:308-341`);
- `grep -c 'R01-' reports/round-39/validation.json` → 0 (the debt is real);
- each R01 finding's cited line opens and says what the row says.
Ca02 must confirm per row: class matches evidence, owner named, no filed byte proposed for
edit. A disagreement is filed as a new row, not smoothed.

Hazards:
- **Truncated protocol.** Any "fixed" claim citing
  `reports/round-39/calib/isolation-replay-protocol.md` is false: the file has no §3 body
  (0.15). Use the draft (`reports/round-39/calib/Ca01-protocol.md`) for design and route the
  landing.
- **Row inflation.** Do not create rows for R01-1 (already folded) or for R01-4 (resolved by
  C05); mark them out of scope once. The 19-row count is the acceptance target; a 20th row
  needs a named reason.
- **Immutable objects.** O02/O08/O07 fragments and the r40 queue are cited, never edited.

---

## 4. Integration order and cross-claim dependencies

1. **O first** (independent). Apply the extractor patch, run selftest + census, file
   `reports/round-43/calib/basename-couples-census.json/.md`. O's census supplies the
   post-landing count that any C landing must re-run (a new entry's `- couples:` line is
   resolver input).
2. **C gate second.** The integrator rules on §2.3 **before** any corpus byte moves. If the
   ruling is "blocked", record it; if "re-scope", amend the claim, then run §2.4. The O
   census must be re-run after any landing because `entries` and `refs` change.
3. **Ca third** (independent of C, but it cites O's disposition leg for R01-7b). File the
   19-row list + queue successor; Ca02 re-measures. Ca must not cite the O census until the
   O patch is applied and the census artifact exists.
4. **Reviewers last:** R01/R02 judge per axis; X01 hunts trades (e.g. O over-claims a build
   that existed, or C lands a duplicate); X02 checks every number is measured. A01 confirms
   the only corpus delta is the ruling's outcome (one new entry or zero).

Cross-claim interfaces:
- O → C: the new entry's `- couples:` field must parse under the patched resolver; a C
  landing adds refs and must not introduce `unresolved`/`ambiguous` rows silently.
- O → Ca: R01-7b's disposition depends on O's per-token disposition leg; if O is not
  applied, R01-7b stays `routed-with-owner`.
- C → Ca: no dependency; Ca's rows are r38/r39 records.
- C → README: rev 2.5 must be re-swept after the O/C changes; the sweep reads files, not
  the resolver.

---

## 5. Named hazards for reviewers

1. **C duplicate-topic landing.** The single largest risk: a seat reads "spare" as
   "unbuilt" and proposes `mineral-stone-symbolism.md` or a variant. Gate C0 fails; report,
   do not route around.
2. **O over-claim.** The claim text says "no durable instrument"; the round record must say
   "hardened successor". If the verdict says "built", it is false.
3. **Census unit drift.** `refs=2730` is per-entry deduplicated tokens; the r37-era 334 is a
   different population (eleven entries). Do not compare 334 to 2730 as if same-unit.
4. **Fallback listing completeness.** 166 rows collapse to 50 distinct mappings; reporting
   only 50 without the per-entry expansion hides where they occur. Report both.
5. **Truncated r39 artifacts.** Both the couples policy (107 lines) and the isolation
   protocol (52 lines) are partial at HEAD; any "fixed" claim must cite the r42 successor
   (policy) or the draft (protocol), not the truncated file.
6. **README totals vector order.** The footer order is README section order
   (`linguistics/myth-symbol/culture-material/synthesis/verification/civilizations`), not
   the order in `claims.json`. A transposed vector passes the totals line but fails the
   footer leg.

---

## Owed

- **Integrator:** rule on C (§2.3) and record the ruling; do not let a seat pick a path.
- **Integrator:** author `reports/round-43/run-validation.py` or drop the third counting
  command with a named reason.
- **O01/O02:** draft the patch + controls against the existing host, not a new file; include
  the pre-edit sha256 in the receipt.
- **O04/O05/O08/O12:** independent verification; no author-verifier overlap.
- **C01/C02/C03/C04/C05/C06/C07 (if C is re-scoped):** fresh gap sweep, fresh audit, README
  rev 2.5, delta receipt. If C is blocked, these seats record `could-not-evaluate` with the
  collision evidence; they do not fabricate a landing.
- **Ca01/Ca02/Ca03:** 19-row disposition list, independent re-measure, queue successor.
- **to-verify:** whether the `synthesis/typed-label-routing-workflow.md` phantom carrier is
  at `:16` (r42 `O11-final.md:288` says `:16`; this seat read the file's couples field but
  did not print its line number). Ca/O should pin the line before citing it.

## Citations

- Contract: `reports/round-43/claims.json:24-36` (O), `:37-48` (C), `:49-59` (Ca);
  `reports/round-43/targets.json:15` (P01 seat), `:6-10` (shared rules).
- Live tree: `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (sha `c99f44ca…`);
  `reports/round-42/cov/C04-entry-4.md` fenced block (byte-equal + newline);
  `reports/round-42/cov/C01-mineral-spare.md:4` (spare title), `:7` (false gap statement);
  `corpus/README.md:5-12` (rev 2.4), `:205` (`## myth-symbol/ (26)`), `:219` (mineral row),
  `:544` (total 223), `:548` (footer vector).
- O instrument: `tools/harness/couples-reference-extractor.py:50-97` (`couples_block`,
  `join_parts`), `:112-118` (`field_refs`), `:134-150` (`classify`), `:153-183`
  (`resolve_entry`), `:186-210` (`census`), `:242-295` (selftest); sha256
  `d8d23a26…`; selftest 8/8 and census output quoted in §0.8-0.9.
- Policy: `reports/round-39/calib/basename-couples-policy.md` §1 `:14-25`, §2 `:27-48`,
  §3 `:50-58`, §4 `:60-69`, §5 `:71-102`, §6 `:104-107` (truncated), §7 absent;
  `reports/round-42/calib/basename-couples-policy-full.md` (263 lines, full §6-§7).
  Ca04 D1/D2: `reports/round-39/calib/Ca04-verify.md:76-105`.
- O history: `reports/round-42/validation.json` (O green, C failed);
  `reports/round-42/op/O06-receipt.md:100-146` (8-row unresolved ledger and the 6→8
  finding); `reports/round-42/op/O11-final.md:286-303` (owed dispositions);
  `SCORECARD.md:822` (r42 O verdict).
- C history: `reports/round-42/validation.json` C failure text; `reports/round-42/cov/C01-mineral-spare.md`;
  `reports/round-42/cov/C05-audit.md:46` (4/4 PASS).
- Ca queue: `reports/round-40/op/defect-queue-v2.json:282` (O02), `:292` (O08), `:302`
  (O07), `:343` (r39 findings disposition); `reports/round-38/op/O03-verify.md:255-341`;
  `reports/round-38/op/O07-scribe.md` (`wc -c` → 0);
  `reports/round-39/review/R01-review.md:25-34,75-79,128-146,147-150,182-222,258-300`;
  `reports/round-39/calib/recount-ledger-successor.json:8` (R01-1);
  `reports/round-39/calib/isolation-replay-protocol.md:10-13,52` (partial);
  `reports/round-35/cov/C12-audit-runbook.md:37` (blocker/`(to-verify` rule).
- README sweep: `reports/round-28/readme/sweep.py` (index + footer + block legs); current
  footer vector `25/26/25/29/24/94` at `corpus/README.md:548`.
