# R8-M09 — metadata sweep: corpus/knowledge/myth-symbol/ (16 entries)

- Round 8 (loop 1 of 3, build round 1 of 4) · Date: 2026-10-17 (UTC 2026-10-17T20:26:43Z at final hash capture)
- Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- Assignment: `reports/round-8/targets.json` → `metadata_sweep` — "audit corpus/knowledge/* frontmatter (source/verified-at/recheck), partition-sharded: … linguistics, myth-symbol, culture-material, verification (1 each). Fixes applied in place on own-lane files only; per-file fragment under reports/round-8/metadata/."
- Writes: the 16 partition entries and this fragment only. No commit — the orchestrator integrates once per round. No file outside `corpus/knowledge/myth-symbol/` was modified.

## 0. Protocol basis — and the convergence observed mid-sweep

At worker start there was no shared metadata-protocol artifact: `ls reports/round-8/` → `metadata/` absent; `find . -name 'm0*'` → empty; `targets.json` carries only the one-sentence `metadata_sweep` scope above. Protocol was taken from in-repo sources:

- Fleet contract `/home/vgpnk/Projects/shokunin/CORPUS.md:17` — "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`".
- Lane precedent `corpus/knowledge/civilizations/rome.md:5-6` — bullet order topic/sources/couples/verified-at/recheck; `verified-at` states what was actually checked and points at the stated limits; `recheck` states the reuse trigger.
- Lane known gap `corpus/README.md:245-246` — "Most historical entries lack the fleet's complete `source`, `verified-at`, `recheck` header."

Mid-sweep, sibling fragments landed (`m01`, `m03`–`m08`, `m10`) and showed two shapes: M01/M06/M07/M10 add a one-line `- source:` summary alongside the existing `- sources:` block, so all three CORPUS.md fields are literally present; M08 treats `- sources:` as satisfying the source slot and adds only `verified-at`/`recheck`. This shard aligned to the **triple** (`source` + `verified-at` + `recheck`, placed after `couples`), matching the fleet contract and the majority shape. The first pass (two fields) was measured before the alignment; both states are recorded in §1–§3 rather than overwritten.

Semantics used, uniform across all 16 entries:

- `source:` — one-line provenance summary naming what the `sources:` block contains and pointing at the section that states its limits; no new source claimed.
- `verified-at:` — the audit scope actually performed, explicitly "round-8 metadata sweep … metadata-level audit only, no per-source retrieval in this sweep". Where an entry already carried its own verification record, it is cited: `comparative-frameworks.md` L19 and `trickster.md` L4 (triage round-2 web-verified notes), `celestial-symbolism-calendars.md` L17–L18 (in-source access dates), `motif-index-usage.md` §7 (spot-check record), `hero-journey-variants.md` (citation-check record at close).
- `recheck:` — trigger conditions drawn from the file's own calibration/limits sections.

Placement note for the parent: this shard (like M01/M10 and the synthesis shard) places the fields after `couples`, per the `rome.md` precedent; M08 (linguistics) places them before `couples`. Cross-shard placement is not uniform.

## 1. Before-state (measured 2026-10-17)

Command (from repo root):

```
python3 - <<'EOF'
import re, glob
for f in sorted(glob.glob('corpus/knowledge/myth-symbol/*.md')):
    t = open(f, encoding='utf-8').read()
    for k in ('topic','sources','couples','verified-at','recheck'):
        print(f.split('/')[-1], k, 'yes' if re.search(r'^- '+k+':', t, re.M) else 'NO')
EOF
```

Output summary: 16/16 files had `topic: yes`, `sources: yes`, `couples: yes`, `verified-at: NO`, `recheck: NO` (80 lines; both fields absent in every entry). README index-row check: 16/16 rows present (`^- \`<file>\` — ` in `corpus/README.md`). Gate baseline on HEAD copies (§3) → `files=16 marks=9 mark-lines=9 findings=0`.

## 2. Fixes applied in place (own-lane files only)

Pass 1 added `- verified-at:` and `- recheck:` after `- couples:` in each entry; pass 2 added `- source:` in the same position (sibling-shape alignment, §0) and corrected two section pointers found by self-audit (§4). Final: `git diff --numstat corpus/knowledge/myth-symbol/` → **3 insertions, 0 deletions per file, 16/16**.

| entry | source @line | verified-at @line | recheck @line | evidence named in the added header |
|---|---|---|---|---|
| animal-symbolism.md | 17 | 18 | 19 | §9 fossil/geomythology flags; §12 canon boundary |
| celestial-symbolism-calendars.md | 21 | 22 | 23 | §9 calibration; §11 canon boundary; sources-block access dates L17–L18 |
| color-symbolism.md | 5 | 6 | 7 | §11 calibration flags; §12 application protocol |
| comparative-frameworks.md | 21 | 22 | 23 | L19 web-verified triage note; §7 calibration; §9 canon boundary |
| cosmology-cosmography.md | 21 | 22 | 23 | §10 calibration checklist; §11 canon boundary |
| creation-myths-taxonomy.md | 19 | 20 | 21 | §12 calibration; §14 canon boundary |
| flood-traditions.md | 20 | 21 | 22 | §7 calibration; source-integrity flags at §7 end |
| hero-journey-variants.md | 21 | 22 | 23 | §7 calibration; citation-check record (Faulkner, Rank, Schmidt) at close |
| motif-index-usage.md | 15 | 16 | 17 | §7 in-file verification record (chapter list, ATU ranges, FFC numbers, exemplar IDs; triage pass 2026-10-17) |
| myth-folktale-genres.md | 21 | 22 | 23 | §7 calibration; §9 canon boundary; §3 unresolved type-age mark |
| myth-ritual-theories.md | 20 | 21 | 22 | §2–§9 calibration; §13 canon boundary |
| number-symbolism.md | 6 | 7 | 8 | §11 calibration flags; §12 application protocol |
| pantheon-archetypes.md | 26 | 27 | 28 | §4/§6 calibration banks; §7 build protocol |
| ritual-liminality.md | 15 | 16 | 17 | §8 calibration; §9 canon boundary; live debates §3–§4 |
| symbolism-synthesis-method.md | 17 | 18 | 19 | §7 audit checklist; §8 calibration; §10 handoff |
| trickster.md | 6 | 7 | 8 | L4 web-verified triage note; §9 calibration; §11 coupling notes |

## 3. After-state (measured 2026-10-17)

- Six-field order check (same script shape as §1, plus an order assertion over `topic < sources < couples < source < verified-at < recheck`): **16/16 files conform**.
- Gate, post-edit: `python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/` → `INFO scan: files=16 marks=9 mark-lines=9 findings=0 blocked=0`, exit 0.
- Pre-edit control, same gate: HEAD copies extracted with `git show HEAD:./<file>` into `/tmp/m09-before/myth-symbol/`, then `python3 tools/gates/provenance-audit.py /tmp/m09-before/myth-symbol/` → `files=16 marks=9 mark-lines=9 findings=0 blocked=0`. Identical inventory — the fix added no findings and no marker drift.
- README index rows still 16/16.
- Gate binary used both times: working-tree `tools/gates/provenance-audit.py` sha256 `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a` (modified this round by a sibling operability worker; HEAD version sha256 `4aaea6e98b9776922708692e6e0f38f76ef7323e3c748cbdf82c789eb77e1e7a`). This worker did not touch `tools/`.
- Post-edit sha256 (`sha256sum corpus/knowledge/myth-symbol/*.md`, 2026-10-17T20:26:43Z):

```
8f1fce2d21a1a174c3e8e06ae47ecb928c4a9be283c8eb96da7987381b028ffc  animal-symbolism.md
2ef711ca56d5e167629de50cab74623001904e445374613985f098053ce72cce  celestial-symbolism-calendars.md
b6830fe792b2074030632ab9af1bc2b17d4a3a5425f10309dc8a3fbf16c3f77c  color-symbolism.md
532e8e0453602cdabed75306d7b8298ceaf2bf0f4e53dc71027a62ee8e9083cf  comparative-frameworks.md
165f292b95852459842900a091c6a40e1cd39b209b8fe2d84e62ecad6266ed2e  cosmology-cosmography.md
a3736c4c293b66ad601debf803eef683976b64d3b9b54d2822c48980b2f7f21b  creation-myths-taxonomy.md
d02322cd2c2684ad3d792d1df17643c8754e2a5c50e84fdd049d796b55cab88f  flood-traditions.md
5ae1e5b9019c9f9c0eacbdd599b0030cbee2f9f828b874d7337f2783ef65a111  hero-journey-variants.md
e81f3cdc727672ac8ce84db024b89ed1a3cd6005fd941e560dad97c3d204ce3b  motif-index-usage.md
936f0f4f8f3dd1bf5d321e4d421692dc04c7099cbe3805180ce8630067e4f7ee  myth-folktale-genres.md
78fb98725a3376f4f2950290246ab25303959f8dcb0e3e08f5113a9893cdb09b  myth-ritual-theories.md
7149494ed994e155342bfd0b8c8c3485844e169b6b9f84190df214aa11389a4c  number-symbolism.md
59f01b86944cdede754e34122b77ce927f5c69f377c4616248e41ef48adc93d0  pantheon-archetypes.md
b57bf9ac3f8c8bea988b8f1fa49d43e3e5883887ec317849af6e31836e888deb  ritual-liminality.md
8aef07cae6d6c4849ae86696c198dadfe1e79dbd9a4aa78f398f9aa8cb9ffde8  symbolism-synthesis-method.md
c1a2c066deeb139f0acdfcba1d8fe2881c1bff2851285947388d8feb87931715  trickster.md
```

## 4. Caught and repaired during the sweep (calibration)

- **Marker inflation.** First wording of three headers used the literal string `to-verify` in prose ("keep their to-verify marks", "the file's own to-verify mark", "the open to-verify list"). The gate counts `to-verify` occurrences as inventory (`MARK_RE`, `tools/gates/provenance-audit.py:79`), so the partition total rose 9 → 12 with no new real marks. Reworded (`creation-myths-taxonomy.md` → "stay flagged, not resolved"; `myth-folktale-genres.md` → "unresolved type-age mark"; `symbolism-synthesis-method.md` → "open unresolved list"); post-fix inventory back to `marks=9` (§3).
- **Pointer errors.** Self-audit of the added headers found two wrong section pointers, both corrected: `animal-symbolism.md` cited §10 for the fossil/geomythology flags (they are in §9); `myth-folktale-genres.md` cited §4 for the type-age debate (it is in §3, and the file's unresolved mark sits in §8).
- Both are recorded because silent pointer drift and silent marker inflation are exactly the defects a metadata sweep exists to catch.

## 5. Limits and disclosures

- Scope is metadata-level: header fields, README-row presence, and location of each file's own limits/calibration sections. The `- sources:` bibliographies were checked for presence and internal consistency only — not audited against the cited works. No source-truth verification is claimed in the 16 headers or here; that remains a separate, open audit.
- `corpus/README.md:245-246` still says "Most historical entries lack the fleet's complete … header" — true of the repo until the other 11 metadata shards land. README is not in this worker's assignment and was not edited; the integrator should re-measure that sentence after the full sweep.
- The round-8 acceptance runner currently has no metadata counter: `grep -c "verified-at\|recheck" reports/round-8/run-validation.py` → `0`; `grep -n metadata reports/round-8/run-validation.py` → no hits. This fragment is therefore the citable evidence for M09; if the parent wants a machine check, the six-field order script in §3 is the candidate counting command.
- Cross-shard placement of the fields is not uniform (this shard after `couples`; M08 before it) — flagged for the parent, not resolved here.
- No LOG.md, SCORECARD.md or `corpus/lessons/round-8.md` entry was written (parent integrates; workers never race shared bookkeeping per AGENTS.md).
- All dates in this fragment are 2026-10-17.

## 6. Files written

- `corpus/knowledge/myth-symbol/` — 16 entries, +3 lines each (`source`, `verified-at`, `recheck`)
- `reports/round-8/metadata/m09-myth.md` — this fragment
