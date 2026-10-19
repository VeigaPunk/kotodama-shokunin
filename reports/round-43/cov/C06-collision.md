# C06 — collision verify (claim C): BLOCKING COLLISION

- Seat **C06** | verifier | claim **C** (coverage) | round 43
- Observed at HEAD `7ceff59a0216a8ea21ee43262d9fc72abf770cee` (`git rev-parse HEAD`), 2026-10-19
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
- Mission (verbatim, `reports/round-43/targets.json`, seat `C06`): *"Collision verifier: independently enumerate corpus/knowledge/myth-symbol/ at HEAD, confirm the target filename is unused, and confirm landing the spare changes no other file. Report the full partition listing you observed."*

## Verdict

**FAIL — the claim-C target filename is already occupied at HEAD, and the claim's "before" premise is stale.**

`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists at HEAD as a 192-line, audited entry landed by round 42 (commit `7ceff59`). The live counts the round-43 claim calls "before" (myth-symbol **26**, total **223**) already *include* that lithic entry. Therefore:

- "target filename is unused" — **false**: the file exists.
- "landing the spare changes no other file" — **unsatisfiable at the declared path**: applying the spare writes over an existing entry (`git status` would show `M`, not `A`), violating claim C's own threshold "no existing entry overwritten".
- "myth-symbol 26 → 27, total 223 → 224" — the spare would make 27/224 only by adding a *second* lithic register alongside the existing one (a duplicate-topic partition), or by replacing it. Neither is the landing claim C describes.

**No rerouting is proposed here.** Per the shared rule, a collision is reported, not routed around. Clearing it requires the integrator to re-scope the claim (a different gap-named topic, or an explicit successor/merge decision about the existing entry — the latter outside this claim's declared thresholds).

## 1. Live partition enumeration at HEAD (observed, not inferred)

Command: `ls -1 corpus/knowledge/myth-symbol/` → 26 entries, listed verbatim:

```
animal-symbolism.md
binding-speech-complex.md
celestial-symbolism-calendars.md
color-symbolism.md
comparative-frameworks.md
cosmology-cosmography.md
creation-myths-taxonomy.md
death-afterlife-eschatology.md
direction-symbolism.md
divination-omen-systems.md
eschatology-world-end-systems.md
flood-traditions.md
hero-journey-variants.md
mineral-stone-symbolism.md
motif-index-usage.md
myth-folktale-genres.md
myth-ritual-theories.md
number-symbolism.md
pantheon-archetypes.md
plant-symbolism.md
purity-pollution-boundary-systems.md
ritual-liminality.md
sacred-kingship-mythic-charter.md
sacred-topography-pilgrimage.md
symbolism-synthesis-method.md
trickster.md
```

Measured counts:

```
ls -1 corpus/knowledge/myth-symbol/*.md | wc -l   → 26
find corpus/knowledge -name '*.md' | wc -l        → 223
per-partition: linguistics 25 / myth-symbol 26 / culture-material 25 / synthesis 29 / verification 24 / civilizations 94
```

Full-tree hash enumeration was also taken (`sha256sum corpus/knowledge/myth-symbol/*.md`); the collision-relevant digest is:

```
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  mineral-stone-symbolism.md
```

README state at HEAD (sweep, read-only, `python3 -B reports/round-28/readme/sweep.py`, exit 0):

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 223 totals_ok True
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

So the index already carries 26 myth-symbol rows and a 223 total, including a row for `mineral-stone-symbolism.md` (`corpus/README.md:219`; revision 2.4 text at `corpus/README.md:5-12`; totals at `corpus/README.md:544,548`).

## 2. Provenance of the occupying file (git, not assumption)

```
git log --diff-filter=A --format='%h|%ad|%s' --date=iso -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
7ceff59|2026-10-19 13:36:54 -0300|round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore
```

Parent-tree measurement:

```
git ls-tree --name-only 7ceff59^ corpus/knowledge/myth-symbol/ | wc -l        → 23
git ls-tree -r --name-only 7ceff59^ corpus/knowledge/ | grep -c '\.md$'        → 220
git ls-tree --name-only 7ceff59^ corpus/knowledge/myth-symbol/ | grep -i 'mineral\|stone\|gem\|lithic'
  → (no lithic filename at parent)
```

The r42 commit added exactly three myth-symbol files (`git show --stat 7ceff59 -- corpus/knowledge README.md`): `mineral-stone-symbolism.md` (192 lines), `purity-pollution-boundary-systems.md`, `sacred-topography-pilgrimage.md` — 23 → 26 and 220 → 223. **The lithic slot was built in round 42.** The round-43 claim's `before` state ("lithic slot named but unbuilt") does not match the tree.

## 3. The collision is already on the filed record

- `corpus/README.md:5-12` (rev 2.4): the fourth draft ("C01's lithic register") "collided with C04's and is routed as a named spare by integrator ruling"; myth-symbol moved 23 → **26**, totals 220 → **223**.
- `reports/round-42/validation.json:9` (and `:15`, `:22`): claim C **FAILED as declared** — "myth-symbol 26 != 27, total 223 != 224 (three entries landed, the fourth collided and is routed …)"; ruling: *"C01 and C04 authored the same lithic register mid-wave; C04 lands, C01 routes as the named spare …"*.
- `reports/round-42/cov/C05-audit.md:32`: C01 row — "**PASS-with-named-defects — S2 staging fence; S2 duplicate topic/path with C04**". The audit also states (`:39`) that claim C's 23 → 27 needed four *distinct* new entries.
- `reports/round-42/cov/C01-entry-1.md:3`: C01's proposed landing path = `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`.
- `reports/round-42/cov/C04-entry-4.md:5`: C04's proposed landing path = the same `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`.
- `reports/round-42/cov/C01-mineral-spare.md:1` (the spare this round proposes to land): *"Integrator ruling 2026-10-19: C01 and C04 authored the same lithic topic mid-wave … C04 lands … THIS draft is routed as the named spare for a future re-scoped claim."* The spare's own header requires a **re-scoped** claim; round-43's claim C is the same scope as the one that failed.

## 4. The spare is a distinct document, but the same topic and path

Extracted from the single `markdown` fence (`reports/round-42/cov/C01-mineral-spare.md:3` opens, `:219` closes):

```
wc -l .scratch/c06/spare-body.md            → 215
sha256sum .scratch/c06/spare-body.md        → 6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89
head -1                                     → # Stone, gem, and metal — the lithic register: material properties as symbol, the scarcity ladder, and the lapidary as an institution
```

Landed entry (`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`):

```
wc -l   → 192
sha256  → c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f
head -1 → # Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-regalia chain
```

Byte identity check: no corpus file carries the spare body's digest (`sha256sum corpus/knowledge/*/*.md | awk '$1=="6999a912…"'` → no match). So the spare is **not** a duplicate byte-for-byte; it is a **second entry on the same topic**, and its landing path is the path of the existing entry.

## 5. Landing-impact model

- **At the declared path** (`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`): one write, but it **replaces** the 192-line audited C04 entry (`c99f44ca…`) with the 215-line spare (`6999a912…`). The existing index row's `- topic:` text would then mismatch the new entry's topic (sweep leg `topic_mismatch`), and claim C's "zero M entries / no existing entry overwritten" threshold fails.
- **At any new path**: adds one file, but creates two topic-owners for the lithic register — the exact S2 duplicate-topic defect r42's audit named (`C05-audit.md:32`) — and requires a further README row/totals edit (224). That is not the spare "landing as the partition's stone/gem/metal register entry"; it is a competing register.
- **No r43 prepare artifact names a path at observation time.** `find reports/round-43 -type f` returned only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; `cov/C01-prepare.md` does not exist yet. The only declared paths on record are r42's, both the occupied one. (If C01-prepare appears later and names a different path, re-run §1–§5 against it before applying.)
- **Unintended-change check:** the worktree is clean apart from untracked round-43 evidence (`git status --porcelain` → `?? reports/round-43/` only). Nothing is staged under `corpus/`; no other file would change mechanically from applying one fenced document. The failure is not side-effect spread — it is that the single write target is an existing entry.

## 6. Per-requirement result

| mission requirement | result | evidence |
|---|---|---|
| independently enumerate the live partition | **PASS** | 26 files listed in §1; 223 total; hashes taken |
| confirm the target filename is unused | **FAIL** | `mineral-stone-symbolism.md` present at HEAD, added by `7ceff59`, sha `c99f44ca…` |
| confirm landing the spare changes no other file | **FAIL (cannot be satisfied at the declared path)** | the single write target is the existing 192-line entry; `M` not `A` |
| report the full partition listing observed | **PASS** | §1 |

## 7. What this seat did not do

- Did not edit, stage, or create anything under `corpus/`; the spare body was extracted only into `.scratch/c06/`.
- Did not run any `reports/round-*/run-validation.py` in-tree; the only instrument run was the read-only index sweep at `reports/round-28/readme/sweep.py`.
- Did not modify any filed round-1..42 byte.
- Did not propose a replacement filename; per the shared rule, collisions are reported, not routed around.

## 8. Handoff

- **Claim C as declared is blocked.** The integrator must either (a) re-scope claim C to a gap-named topic that is still unowned (requires a fresh absence sweep — this seat did not perform one, and the spare is not that topic), or (b) file an explicit successor/merge decision about the existing `mineral-stone-symbolism.md` entry, which is a different claim with its own audit and is outside this round's declared non-goals ("no filed byte rewrites").
- If the round proceeds with a different target file, C06's collision check must be re-run against that exact filename at the then-current HEAD; this report only clears the state at `7ceff59`.
- `to-verify`: whether r43 `cov/C01-prepare.md` (not yet written at observation time) names a landing path other than the occupied one. If it does, this verdict does not cover it.
