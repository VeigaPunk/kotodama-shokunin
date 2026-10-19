# C13 — Couples verifier (cartography entry, claim C)

- **Seat:** C13 · role: verifier · claim: **C** (coverage)
- **Out:** `reports/round-47/cov/C13-couples.md` (the only path this seat wrote; all other writes are disposable `.scratch/c13-*` staging)
- **Observed:** 2026-10-19T18:01:14Z
- **Baseline:** HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`6e9a30d`), equal to `reports/round-47/claims.json:7`
- **Artifact under test:** `reports/round-47/cov/C04-entry-header.md` — container sha256 observed at three reads: `b4ae4736556d98e9f4175d74c25f0e81bee5e5d78cdf5ea7b79015ae4f81ec8a` (18:01Z), `6285ad623fe6d301db8b259c019a5be2b1d3277d54561eb950bb54a862cb1af2` (18:03Z), `cb5a7489676de47e146e5055e07be9c8fa9d2df624c8872b0d438efcd67b68b0` (18:05Z). The header was revised repeatedly while this seat verified; the **`- couples:` line was byte-identical across all reads**.
- **The verified field (binding pin):** the single `- couples:` line in C04's fenced head block, sha256 `cf59ba1f311619dbe527bfb1d3c716ae338f56d601af675e52e343384e9f5663` (4096 characters). Pin the **line**, not the container file: unrelated header edits change the file sha but do not change the field this verdict covers.

**Verdict: PASS.** All **21/21** `- couples:` tokens name a file that exists at HEAD `6e9a30d` and resolve **Tier-1 direct** from the entry's real directory (`corpus/knowledge/culture-material/`), using the lane's own resolver policy. Zero dangling, zero guessed, zero ambiguous, zero prospective-seed tokens. If the head block lands verbatim, the resolver census moves by exactly **+1 entry, +21 refs, +21 direct** and nothing else.

Scope limit: this seat verifies **token resolution and the resolver delta only**. The truth of each boundary sentence is C08/A02's job; the truth of each line anchor is C06's; the post-landing census is V01's.

---

## 1. Target state at HEAD (A, not M)

```console
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git ls-tree -r --name-only HEAD corpus/knowledge | wc -l
223
$ git status --porcelain -- corpus/
(empty)
$ git cat-file -e HEAD:corpus/knowledge/culture-material/cartography-and-mapmaking.md
fatal: path 'corpus/knowledge/culture-material/cartography-and-mapmaking.md' does not exist in 'HEAD'
```

The landing is an **addition** at a free path. No existing entry is overwritten, so the new entry is the only source of new couples references in this delta.

## 2. Instrument health and pre-landing census

The resolver is the durable r43 instrument, not a scratch prototype:

```console
$ sha256sum tools/harness/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
$ python3 -B tools/harness/basename-couples-resolver.py --selftest
...
SELFTEST OK: 27/27 controls
(exit 0)
$ python3 -B tools/harness/basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  misaligned: none
```

The seven pre-existing `unresolved` tokens are five declared prospective seeds (`language-contact.md` ×3, `phonetics-phonology.md` ×2) and two dangling `../linguistics/phonology-sanity.md` references (`synthesis/typed-label-routing-workflow.md`, `verification/label-channel-routing-verification.md`). **None involves cartography**, so the new landing neither repairs nor worsens them.

## 3. Token-by-token verification (21/21 direct)

Method: extracted C04's fenced head block, captured the `- couples:` field with the resolver's own `couples_block()`/`join_parts()`/`field_refs()`, then classified every token with the resolver's own `classify()` using the **real entry directory** `corpus/knowledge/culture-material`. HEAD existence was checked with `git ls-tree`/`git cat-file`, not the worktree.

| # | Token | Resolves to at HEAD | Class | Parenthetical line pointers |
|---:|---|---|---|---|
| 1 | `../myth-symbol/cosmology-cosmography.md` | `corpus/knowledge/myth-symbol/cosmology-cosmography.md` (155 L) | direct | `:71`, `:102` |
| 2 | `../myth-symbol/sacred-topography-pilgrimage.md` | `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` (181 L) | direct | `:5` |
| 3 | `../myth-symbol/direction-symbolism.md` | `corpus/knowledge/myth-symbol/direction-symbolism.md` (202 L) | direct | `:51` |
| 4 | `architecture-settlement-lexicon.md` | `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` (149 L) | direct | `:95` |
| 5 | `writing-media-surface-economy.md` | `corpus/knowledge/culture-material/writing-media-surface-economy.md` (201 L) | direct | `:3` |
| 6 | `transport-mobility-lexicon.md` | `corpus/knowledge/culture-material/transport-mobility-lexicon.md` (129 L) | direct | `:28`, `:117` |
| 7 | `timekeeping-instruments.md` | `corpus/knowledge/culture-material/timekeeping-instruments.md` (140 L) | direct | `:50` |
| 8 | `material-culture-inference-method.md` | `corpus/knowledge/culture-material/material-culture-inference-method.md` (109 L) | direct | `:69`, `:76` |
| 9 | `craft-artisan-lexicon.md` | `corpus/knowledge/culture-material/craft-artisan-lexicon.md` (154 L) | direct | `:44` |
| 10 | `trade-economy-lexicon.md` | `corpus/knowledge/culture-material/trade-economy-lexicon.md` (166 L) | direct | `:92`, `:121` |
| 11 | `vessel-container-lexicon.md` | `corpus/knowledge/culture-material/vessel-container-lexicon.md` (175 L) | direct | `:115` |
| 12 | `../linguistics/naming-systems.md` | `corpus/knowledge/linguistics/naming-systems.md` (136 L) | direct | — |
| 13 | `../linguistics/writing-systems.md` | `corpus/knowledge/linguistics/writing-systems.md` (161 L) | direct | `:117`, `:149`, `:156` |
| 14 | `../civilizations/mesoamerica-primary-sources.md` | `corpus/knowledge/civilizations/mesoamerica-primary-sources.md` (177 L) | direct | `:58` |
| 15 | `../civilizations/polynesia-navigation.md` | `corpus/knowledge/civilizations/polynesia-navigation.md` (210 L) | direct | `:52` |
| 16 | `../civilizations/japan-medieval-sengoku.md` | `corpus/knowledge/civilizations/japan-medieval-sengoku.md` (200 L) | direct | `:157` |
| 17 | `../verification/calibration-registry.md` | `corpus/knowledge/verification/calibration-registry.md` (190 L) | direct | `:78–88` |
| 18 | `../verification/real-world-inspiration-boundaries.md` | `corpus/knowledge/verification/real-world-inspiration-boundaries.md` (172 L) | direct | `:6` |
| 19 | `../verification/myth-consistency-gate.md` | `corpus/knowledge/verification/myth-consistency-gate.md` (214 L) | direct | `:34` |
| 20 | `../synthesis/worldbible-integration-contract.md` | `corpus/knowledge/synthesis/worldbible-integration-contract.md` (209 L) | direct | — |
| 21 | `../synthesis/era-material-scoped-reconciliation.md` | `corpus/knowledge/synthesis/era-material-scoped-reconciliation.md` (75 L) | direct | — |

Partition distribution: myth-symbol 3, culture-material 8, linguistics 2, civilizations 3, verification 3, synthesis 2 = **21**.

Line-pointer sanity (existence/range only, not truth — C06 owns truth): every `:NN` in the parentheticals is within its cited file's line count; 24 colon-form occurrences over 23 distinct line numbers, max `:157` (file has 200 L), plus the `78–88` range endpoint (file has 190 L). No pointer points past EOF.

## 4. Negative checks (the ways a couples field fails)

| Check | Result | Evidence |
|---|---|---|
| Dangling token (names no file at HEAD) | **0** | all 21 checked with `git ls-tree`/`git cat-file`; table §3 |
| Ambiguous basename (two corpus files share the name) | **0** | basename counter over all 223 HEAD files: every one of the 21 basenames occurs exactly once |
| Unresolved by policy (slash-bearing + no direct hit) | **0** | `classify()` returns `direct` for 21/21 |
| Plain-basename fallback (would add fallback rows) | **0** | same-partition tokens are entry-dir direct; cross-partition tokens carry `../` |
| Prospective/sibling-seed marker (`files to seed`, etc.) | **absent** | regex over the joined field → no match |
| Glob fragment (`*-gate.md`) | **0** | no `*` or leading `-` tokens |
| Brace-expanded group (`{a,b}.md`) | **0** | no `{` in the field |
| Token in body prose captured by mistake | **none** | `couples_block()` returns **1 part**; the next header field is `- source:` |
| Wrapped/multi-line field | **no** | one physical line; `wrapped=False` for the entry |
| Live entry already couples to the new path | **0** | `git grep -n "cartography-and-mapmaking" HEAD -- corpus/knowledge` → no output |
| Live entry's couples names cartography/mapmaking | **0** | `git grep -nE '^- couples:.*(cartograph|mapmaking|portolan|cadastr)' HEAD -- corpus/knowledge` → no output |

The last two matter for the delta: because no existing entry references the new file, the landing cannot flip any other entry's resolution class (e.g. unresolved→direct). The only new refs are the 21 above.

## 5. Expected resolver delta (measured on a 224-entry copy)

Method: copied `corpus/knowledge` to `.scratch/c13-tree/knowledge`, inserted C04's head block at the relative target path, then ran the resolver's `census(paths)` over the resulting 224 files. This exercises the real `classify()` against a real entry directory; no corpus byte was staged.

| Counter | Pre (223) | Post (224) | Delta |
|---|---:|---:|---:|
| entries | 223 | 224 | **+1** |
| refs | 2730 | 2751 | **+21** |
| direct | 2556 | 2577 | **+21** |
| fallback | 166 | 166 | 0 |
| ambiguous | 0 | 0 | 0 |
| unresolved | 7 | 7 | 0 |
| glob-fragment | 1 | 1 | 0 |
| wrapped fields | 1 | 1 | 0 |
| misaligned | 0 | 0 | 0 |
| conservation | True | True | — |

Conservation post-landing: `2577 + 166 + 0 + 7 + 1 = 2751` = refs. The new entry itself reads `wrapped=False, tokens=21, direct=21`.

Expected post-landing commands/results:

```console
$ python3 -B tools/harness/basename-couples-resolver.py --census
entries=224 refs=2751
  policy four-class: direct=2577 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2751 refs=2751)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  misaligned: none
```

The copied-tree run reports the copied path in `wrapped_fields`; in the live tree the one wrapped field remains `corpus/knowledge/linguistics/phonetics-phonology.md`. That path prefix is an artifact of the simulation, not a predicted change.

## 6. Contract checks

- **`corpus/QUALITY.md:13-15` (coupling):** the field is present and names 21 systems via `partition/slug.md` or `../partition/slug.md`, each with the boundary it owns. Not empty, not decorative.
- **Provenance gate (landing gate):** ran on the staged head block:
  ```console
  $ python3 -B tools/gates/provenance-audit.py .scratch/c13-tree/knowledge/culture-material/cartography-and-mapmaking.md
  INFO to-verify-count: ...: 24 mark(s) on 22 line(s)
  INFO scan: files=1 marks=24 mark-lines=22 findings=0 blocked=0
  (exit 0)
  ```
  No `missing-couples` / `empty-couples` finding. The gate's own selftest is green (`7 fixture file(s)`, planted IDs detected, exit 0/1/2 semantics intact).
- **Resolution policy:** the tokens use the shapes policy §2 Tier 1 accepts — entry-direct plain basenames for same-partition files, `../partition/file.md` for cross-partition. This is why 21/21 are `direct` rather than `fallback`; the field adds no fallback-mapping rows.
- **Shape observation (apply-time caution):** the couples line measures exactly **4096 characters** (4176 bytes). It ends with a complete parenthetical and period (`...is not its survey date).`) and the last token is complete, so there is no truncation evidence at the filed artefact. Because it sits on a round editor-buffer boundary, the integrator must lift it **verbatim** and re-count tokens after apply; a truncating editor would silently drop the final token. Do not reflow it into a hard wrap — an unindented wrap truncates the field for the resolver, and an indented one would add the entry to `wrapped_fields`.

## 7. What voids this verdict

1. The **couples-line digest** changes (`cf59ba1f…` no longer matches). A change to the container file alone, with the line unchanged, does not void the verdict — observed across two C04 revisions; re-extract and re-run §8 only if the line moves.
2. The integrator applies a different couples block or edits tokens during assembly.
3. Another seat lands `corpus/knowledge/culture-material/cartography-and-mapmaking.md` first — then this is M, not A, and the collision must be reported rather than overwritten.
4. The apply-time HEAD is no longer `6e9a30d` **and** one of the 21 target files moved/renamed. (A HEAD advance alone is harmless if the 21 paths still exist; re-run to confirm.)
5. Any token is added or removed — recompute the delta; the +21 figure is for this exact field.

## 8. Re-run (integrator / V01)

```console
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD
python3 - <<'PY'   # expect cf59ba1f… — the couples-line digest, not the container file's
import re, hashlib
t = open("reports/round-47/cov/C04-entry-header.md", encoding="utf-8").read()
h = re.findall(r"````markdown\n(.*?)\n````", t, re.S)[0]
l = [x for x in h.splitlines() if x.startswith("- couples:")][0]
print(hashlib.sha256((l + "\n").encode()).hexdigest())
PY
python3 -B tools/harness/basename-couples-resolver.py --selftest   # expect 27/27, exit 0
python3 -B tools/harness/basename-couples-resolver.py --census     # expect 2751/2577 after landing
python3 -B tools/harness/basename-couples-resolver.py --json \
  corpus/knowledge/culture-material/cartography-and-mapmaking.md   # expect wrapped false, 21 direct
python3 -B tools/gates/provenance-audit.py \
  corpus/knowledge/culture-material/cartography-and-mapmaking.md   # expect findings=0, exit 0
```

A one-shot token audit (stdlib only), if the filed header changes:

```console
python3 - <<'PY'
import importlib.util, os, subprocess, sys
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("res", "tools/harness/basename-couples-resolver.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
text = open("reports/round-47/cov/C04-entry-header.md", encoding="utf-8").read()
head = text.split("````markdown\n", 1)[1].split("\n````", 1)[0]
entry_dir = os.path.abspath("corpus/knowledge/culture-material")
tree = set(subprocess.run(["git", "ls-tree", "-r", "--name-only", "HEAD",
                           "corpus/knowledge"], capture_output=True, text=True).stdout.split())
for ref in sorted(m.field_refs(head)):
    klass, mapping = m.classify(ref, entry_dir)
    path = os.path.normpath(os.path.join(entry_dir, ref))
    print(f"{klass:11s} HEAD:{'OK' if path in tree else 'MISS'} {ref}")
PY
```

## 9. Owed / handoff

- **Integrator (C landing):** lift C04's head block verbatim; keep the `- couples:` field on one physical line; re-run §8 after apply.
- **V01 (post-landing):** confirm the census reads `entries=224 refs=2751 direct=2577`, `wrapped=1`, `misaligned=none`, and that the target entry reads 21/21 direct.
- **C06:** verify the **truth** of the parenthetical line claims; this seat checked existence, class and line-range only.
- **C08/A02:** verify the **ownership semantics** of the boundary statements (that each neighbour really owns what the parenthetical says). This seat did not adjudicate ownership.
- No corpus write, no git commit, no round-runner execution. Disposable staging lives under `.scratch/c13-stage/` and `.scratch/c13-tree/`; it is not a deliverable.
