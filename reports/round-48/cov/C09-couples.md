# C09 — Couples verifier (right-sized cartography entry, claim C)

- **Seat:** `C09` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- **Out:** `reports/round-48/cov/C09-couples.md` (this file; the only path this seat wrote)
- **Baseline:** HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`a01405d`), equal to `reports/round-48/claims.json:7`
- **Observed:** 2026-10-19T19:40Z, from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
- **Artifact under test:** the `- couples:` field in the fenced head block of `reports/round-48/cov/C02-header.md:130` (263-line fragment), digest-pinned in §3
- **Scope:** couples-token resolution and the resolver delta **only**. The truth of each boundary sentence is C07/C15/A02's; the truth of each `path:line` anchor is C04/C06's; post-landing census is V01/F01's.

**Verdict.** **PASS on resolution and delta; P2 on completeness.** The filed draft's field is one physical line (`wrapped=False`), carries **19 tokens**, and **19/19 resolve Tier-1 `direct`** at HEAD `a01405d` — zero dangling, ambiguous, prospective-seed, glob or brace tokens. A staged 224-entry census measures delta **+1 entry / +19 refs / +19 direct**, conservation True, every other class unchanged. The finding is that the field **omits two tokens the r47 review mandates** — `celestial-symbolism-calendars.md` and `sacred-kingship-mythic-charter.md` (`reports/round-47/review/R03-c-content.md:133,208`; rows at `reports/round-47/cov/C08-boundary.md:234,236`). Adding them yields **21/21 direct**, delta **+21/+21**. This is an additive fix, not a redesign: each addition is one `direct` token, no fallback/ambiguous/unresolved movement.

---

## 1. Target state and write surface

```console
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git log --oneline -1
a01405d round-47: NOT ADMITTED on C; O+Ca improved — ...
$ git status --porcelain -- corpus/
(empty)
$ git ls-tree -r --name-only HEAD corpus/knowledge | wc -l
223
$ git cat-file -e HEAD:corpus/knowledge/culture-material/cartography-and-mapmaking.md
fatal: path 'corpus/knowledge/culture-material/cartography-and-mapmaking.md' does not exist in 'HEAD'
```

The landing is an **A** at a free path; no existing entry is overwritten, so the new entry is the only source of new couples refs in the delta.

## 2. Instrument health and pre-landing census

```console
$ sha256sum tools/harness/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
$ python3 -B tools/harness/basename-couples-resolver.py --selftest | tail -1
SELFTEST OK: 27/27 controls
$ python3 -B tools/harness/basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  misaligned: none
```

Arithmetic: `2556 + 166 + 0 + 7 = 2729`; `+ 1` glob fragment `= 2730`. ✓

The seven unresolved tokens are five pre-existing declared prospective seeds (`language-contact.md` ×3, `phonetics-phonology.md` ×2) and two dangling `../linguistics/phonology-sanity.md` refs (`synthesis/typed-label-routing-workflow.md`, `verification/label-channel-routing-verification.md`). None involves cartography; the landing neither repairs nor worsens them.

Corpus drift since the r47 verification HEAD:

```console
$ git diff --stat 6e9a30d..a01405d -- corpus/knowledge
(empty)
```

Every target file is byte-identical to what r47's C13 verified; only round bookkeeping advanced.

## 3. The filed field: 19/19 Tier-1 direct

```console
$ python3 -B (resolver couples_block/join_parts/field_refs/classify on the fenced head)
couples line chars 3071
sha256 af0fc57419ab4c5a73f8ce62ead2d07c744e99051d5359f4b527def119d16e37
block parts 1   wrapped False
tokens 19
```

Classification used the resolver's own functions with the **real** entry directory `corpus/knowledge/culture-material`, and HEAD existence was checked with `git ls-tree` on repo-relative paths (not the filesystem).

| # | Token | Target | Class | Lines |
|---:|---|---|---|---:|
| 1 | `../myth-symbol/cosmology-cosmography.md` | myth-symbol | direct | 155 |
| 2 | `../myth-symbol/sacred-topography-pilgrimage.md` | myth-symbol | direct | 181 |
| 3 | `../myth-symbol/direction-symbolism.md` | myth-symbol | direct | 202 |
| 4 | `architecture-settlement-lexicon.md` | culture-material | direct | 149 |
| 5 | `writing-media-surface-economy.md` | culture-material | direct | 201 |
| 6 | `transport-mobility-lexicon.md` | culture-material | direct | 129 |
| 7 | `craft-artisan-lexicon.md` | culture-material | direct | 154 |
| 8 | `trade-economy-lexicon.md` | culture-material | direct | 166 |
| 9 | `vessel-container-lexicon.md` | culture-material | direct | 175 |
| 10 | `timekeeping-instruments.md` | culture-material | direct | 140 |
| 11 | `material-culture-inference-method.md` | culture-material | direct | 109 |
| 12 | `../linguistics/naming-systems.md` | linguistics | direct | 136 |
| 13 | `../civilizations/mesoamerica-primary-sources.md` | civilizations | direct | 177 |
| 14 | `../civilizations/polynesia-navigation.md` | civilizations | direct | 210 |
| 15 | `../civilizations/japan-medieval-sengoku.md` | civilizations | direct | 200 |
| 16 | `../verification/calibration-registry.md` | verification | direct | 190 |
| 17 | `../verification/real-world-inspiration-boundaries.md` | verification | direct | 172 |
| 18 | `../verification/myth-consistency-gate.md` | verification | direct | 214 |
| 19 | `../synthesis/worldbible-integration-contract.md` | synthesis | direct | 209 |

Distribution: myth-symbol 3 + culture-material 8 + linguistics 1 + civilizations 3 + verification 3 + synthesis 1 = **19**. ✓

All tokens use a Tier-1 shape: same-partition plain basenames (resolved against the entry directory) and `../<partition>/` paths for cross-partition files. No token falls through to the basename index, so the field adds **no fallback rows**. Every basename occurs exactly once across the 223 files, so a plain-basename rewrite would still resolve — as `fallback`, not `direct`.

### 3.1 What changed against r47's carried field

r47's field (`reports/round-47/cov/C04-entry-header.md:159`, digest `cf59ba1f…`, 4096 chars) was re-verified first: **21/21 direct** at `a01405d`, unchanged digest, same delta +21/+21. The r48 draft is a right-sizing edit of it: it **drops** `../linguistics/writing-systems.md` and `../synthesis/era-material-scoped-reconciliation.md`, and rewrites the parentheticals. Both dropped files still exist and would classify `direct` if re-added; their removal is an editorial trimming consistent with the <=~250-line target, not a resolution defect. One improvement is real: the `craft-artisan-lexicon.md` parenthetical now cites `:54-65` (the ladder) instead of r47's `:44` (the Steel-grading row), closing R03 **B4** inside the field I audit.

## 4. The finding: two mandated tokens are absent

The draft names neither file anywhere — not in couples, not in the handoff:

```console
$ grep -n 'celestial-symbolism\|sacred-kingship\|writing-systems\|era-material-scoped' reports/round-48/cov/C02-header.md
(none)
```

The mandate is explicit in the prior review:

- `reports/round-47/review/R03-c-content.md:133`: "The `- couples:` line names craft and trade-economy but not celestial-symbolism or sacred-kingship. Add the four 'owns / does not restate' rows."
- `reports/round-47/review/R03-c-content.md:208` (P2-7): the four missing rows, sourced from `reports/round-47/cov/C08-boundary.md:232-237`.

Two of the four (`craft-artisan-lexicon.md`, `trade-economy-lexicon.md`) are present as tokens 7 and 8. The two absent:

| Required token | Source row | Class from entry dir | Basename owners |
|---|---|---|---|
| `../myth-symbol/celestial-symbolism-calendars.md` | `C08-boundary.md:234` | **direct** | 1 |
| `../myth-symbol/sacred-kingship-mythic-charter.md` | `C08-boundary.md:236` | **direct** | 1 |

Both need the `../myth-symbol/` prefix. A bare basename classifies `fallback`; a wrong partition prefix (e.g. `../culture-material/celestial-symbolism-calendars.md`) classifies **unresolved** — measured in §6. The resolution is therefore shape-sensitive, which is why the fix must name the prefix.

**Severity.** P2, matching R03's own classification — it does not make the draft unsafe to land, because the resolver surfaces no failure. The risk is silent: a 19-token field passes every automated check while the entry under-couples the star-chart and legal-charter material its body develops. The claim's `after_required` includes "audits PASS", and C15's neighbor check dispositions these rows; landing without the tokens leaves that check incomplete.

C07's filed boundary review independently reaches the same two neighbors: celestial-symbolism is under-dispositioned (`reports/round-48/cov/C07-boundary.md:94`, "UNDER (U3) — add the row") and sacred-kingship must be promoted into the single table (`C07-boundary.md:95`). Divination is explicitly **not** required (`C07-boundary.md:96,233`; R03 §3.4), so the mandatory correction is exactly +2, not +4.

### 4.1 Cross-check against K01's spec — and an arithmetic error in it

`reports/round-48/scout/K01-rightsized-spec.md:126` enumerates the spec's couples files. Counted from its own list:

| Partition | Files named |
|---|---|
| myth-symbol | 6 (cosmology, sacred-topography, direction, celestial, sacred-kingship, divination) |
| culture-material | 7 (architecture, writing-media, transport, craft, trade, timekeeping, material-culture-inference) |
| civilizations | 3 (mesoamerica, polynesia, japan-sengoku) |
| linguistics | 2 (naming-systems, writing-systems) |
| verification | 3 (calibration-registry, real-world-inspiration, myth-consistency-gate) |
| **Total** | **6+7+3+2+3 = 21** |

The same line calls this "Nineteen files". That label is **off by two** — the enumeration is 21. This is the r47 arithmetic failure class recurring in a r48 artifact, and it matters here because the draft's 19 is a third, different set: the draft keeps `vessel-container-lexicon.md` and `worldbible-integration-contract.md` (not in K01's list) and drops `writing-systems.md` and `divination-omen-systems.md` plus the two mandated neighbors. The integrator should not use "19" as if it were a ratified count from either source. The only defensible minimum is R03's **+2** (§4); the rest is editorial.

## 5. Resolver delta, measured on a staged 224-entry tree

Method: copied `corpus/knowledge` to `.scratch/c09-tree/knowledge` (disposable, not a deliverable), wrote a fixture at `culture-material/cartography-and-mapmaking.md` containing the filed field, then the field plus the two §4 tokens, and ran the resolver's `census(paths)` over the 224 files. No corpus byte was staged or modified.

| Counter | Live 223 | Filed (19) | Δ | Corrected (21) | Δ |
|---|---:|---:|---:|---:|---:|
| entries | 223 | 224 | **+1** | 224 | **+1** |
| refs | 2730 | 2749 | **+19** | 2751 | **+21** |
| direct | 2556 | 2575 | **+19** | 2577 | **+21** |
| fallback | 166 | 166 | 0 | 166 | 0 |
| ambiguous | 0 | 0 | 0 | 0 | 0 |
| unresolved | 7 | 7 | 0 | 7 | 0 |
| glob-fragment | 1 | 1 | 0 | 1 | 0 |
| wrapped fields | 1 | 1 | 0 | 1 | 0 |
| misaligned | 0 | 0 | 0 | 0 | 0 |
| conservation | True | True | — | True | — |

Conservation: filed `2575+166+0+7+1 = 2749`; corrected `2577+166+0+7+1 = 2751`. ✓
Entry read-back: filed `wrapped=False tokens=19 direct=19`; corrected `wrapped=False tokens=21 direct=21`.

## 6. Negative checks — the ways a couples field fails

Run with the resolver's `classify()` against `corpus/knowledge/culture-material` and `git grep` at HEAD.

| Check | Result | Evidence |
|---|---|---|
| Dangling token (names no file at HEAD) | **0 of 19** | `git ls-tree` per token; §3 |
| Ambiguous basename (two corpus files share it) | **0** | every basename in the field occurs exactly once across 223 files |
| Guessed-site control (plausible but absent) | all **unresolved** | `portolan-charts.md`, `surveying-instruments.md`, `projection-systems.md`, `atlas-history.md`, `history-of-cartography.md`, `harley-1989.md`, `cadastral-maps.md` |
| Wrong-shape control | **unresolved** | `culture-material/naming-systems.md`, `../culture-material/celestial-symbolism-calendars.md`, `../myth-symbol/celestial-symbolism.md` (truncated slug) |
| Prospective/sibling-seed marker (`files to seed`, etc.) | **absent** | resolver regex over the joined field → no match |
| Glob fragment (`*`, leading `-`) | **0** | no `*` or leading-`-` token |
| Brace-expanded group (`{a,b}.md`) | **0** | no `{` in the field |
| Over-capture of body prose | **none** | `couples_block()` returns 1 part; the next header field terminates the block |
| Wrapped/multi-line field | **no** | 1 physical line, `wrapped=False` |
| Delta isolation: live entry references the new path | **0** | `git grep -n 'cartography-and-mapmaking' HEAD -- corpus/knowledge` → no output |
| Delta isolation: live couples names the topic | **0** | `git grep -nE '^- couples:.*(cartograph\|mapmaking\|portolan\|cadastr)' HEAD -- corpus/knowledge` → no output |

The last two mean no existing entry can flip class because of the landing; the only new refs are the entry's own.

Pointer range sanity (existence/range only; **truth is C04/C06's**): no `:NN` in the field's parentheticals points past its cited file's line count.

## 7. Conditional verdict and what voids it

- **Resolution:** PASS — 19/19 direct at `a01405d`, no negative class, delta +19/+19.
- **Completeness:** P2 FAIL — 2 of 4 R03-mandated additions absent; corrected field is 21/21 direct, delta +21/+21. K01's spec independently enumerates 21 files too, though its line mislabels them "Nineteen" (§4.1).
- **Landing:** if applied as filed, no resolver check fails; the omission is invisible to the census. If the omission is accepted deliberately, C15/X00 must record it as a named exception rather than leave it silent.

This verdict **voids** if:

1. the `- couples:` line digest changes from `af0fc57419ab4c5a73f8ce62ead2d07c744e99051d5359f4b527def119d16e37` — re-extract and re-run the command below (the fragment may be revised by its author after this read);
2. either §4 token is added without a recomputed delta (each `direct` addition is exactly +1 ref / +1 direct);
3. a token is written as a bare basename (`fallback`), with a wrong partition prefix (`unresolved`), or names a file absent from `git ls-tree HEAD`;
4. the field is wrapped or split across lines (a truncating editor would silently drop the tail token; the r47 field was 4096 chars and this one is 3071);
5. another seat lands `corpus/knowledge/culture-material/cartography-and-mapmaking.md` first — then this is M, not A, and is a collision to report.

Binding re-run after any revision or after the integrator applies:

```console
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B tools/harness/basename-couples-resolver.py --selftest   # 27/27, exit 0
python3 -B - <<'PY'
import importlib.util, os, subprocess, sys
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("res", "tools/harness/basename-couples-resolver.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
text = open("reports/round-48/cov/C02-header.md", encoding="utf-8").read()
head = text.split("````markdown\n", 1)[1].split("\n````", 1)[0]
ed = os.path.abspath("corpus/knowledge/culture-material")
tree = set(subprocess.run(["git","ls-tree","-r","--name-only","HEAD","corpus/knowledge"],
                          capture_output=True, text=True).stdout.split())
refs = sorted(m.field_refs(head))
bad = []
for r in refs:
    k, mp = m.classify(r, ed)
    p = os.path.relpath(os.path.normpath(os.path.join(ed, r)), ".")
    if k != "direct" or p not in tree:
        bad.append((r, k, p in tree))
print("tokens", len(refs), "bad", bad)
print("wrapped", len(m.couples_block(head)) > 1)
PY
```

Expected as filed: `tokens 19 bad []`, `wrapped False`; post-landing `entries=224 refs=2749 direct=2575 fallback=166 ambiguous=0 unresolved=7`, conservation True.
Expected after the §4 fix: `tokens 21 bad []`; post-landing `entries=224 refs=2751 direct=2577`.
Any other token count: recompute rather than reuse these figures.

## 8. Write surface and scope limits

**Wrote:** this file only. **Read:** `reports/round-47/**`, `reports/round-48/**`, `corpus/**`, `tools/harness/**`. **Staged:** `.scratch/c09-tree/` (disposable copy for the 224-entry census; not a deliverable). No `corpus/**` byte was edited or staged; no filed round byte was edited; no git commit/push, no install, no network; no `reports/round-*/run-validation.py` executed; no re-freeze, no packet surface.

**Not verified here (other seats own them):** the truth of each parenthetical's ownership claim (C07/C15/A02); the truth of each `:NN` anchor (C04/C06); the entry's length, worked example, arithmetic (C03/C05/C14/X03); the README rev 2.5 and sweep (C10/C11); the post-landing live census (V01/F01). The 19-token digest pins what I read at 19:40Z; the author may revise the fragment after that time, in which case §7's void clause applies.
