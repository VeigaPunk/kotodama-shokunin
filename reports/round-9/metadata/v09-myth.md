# V09 — metadata re-audit (round 9): `corpus/knowledge/myth-symbol/` (all 16 entries)

- Round-9 metadata re-audit, shard **V09 (myth-symbol all)** — the same partition round-8's M09 fixed (`reports/round-8/metadata/m09-myth.md`). Shard list: `ls corpus/knowledge/myth-symbol/ | wc -l` → **16** (2026-10-17).
- Date 2026-10-17; final gate/git capture 2026-10-17T20:51:27Z and full-digest capture 2026-10-17T20:51:06Z (`date -u`). Round-8's after-digests were captured 2026-10-17T20:26:43Z.
- Baselines: round-9 `claims.json` `baseline_revision` `e1694bad6ac96aca45a11ca5746582b275929355`; observed HEAD `a7bb205` ("round-9: declare claims F/O/D"), whose diff touches only `reports/round-9/`. `git diff --stat HEAD -- corpus/knowledge/myth-symbol/` → empty; `git status --porcelain corpus/knowledge/myth-symbol/` → empty. The entry text on disk equals the baseline revision, and nothing in this partition has been edited since commit `e1694ba` (`git log --oneline -1 -- corpus/knowledge/myth-symbol/` → `e1694ba`).
- Contract audited: round-9 `targets.json` `metadata_verify` — "11 shards re-audit all 179 corpus/knowledge entries for complete source/verified-at/recheck frontmatter after round 8's sweep; fix stragglers in place"; fleet `CORPUS.md:17` — "Each `knowledge/` entry opens with `source:`, `verified-at:` and `recheck:`". Gate neutrality of the trio re-confirmed against current gate source: `tools/gates/provenance-audit.py:75` `FIELD_NAMES = ("topic", "sources", "couples")`, `:76` `FIELD_RE` — the three metadata fields are not read by the gate; only `MARK_RE` (`:79`, `to-verify`) counts inventory.
- Write scope: this fragment only. **0 entry files changed — no straggler was found.** No commit made.

## Method and commands

Field census (opening block = lines before the first `## ` heading), run from repo root:

```
python3 - <<'EOF'
import re, glob
bad=[]
for f in sorted(glob.glob('corpus/knowledge/myth-symbol/*.md')):
    t=open(f,encoding='utf-8').read(); lines=t.splitlines()
    first=next((i for i,l in enumerate(lines,1) if l.startswith('## ')), None)
    counts={k:len(re.findall(r'^- '+k+r':', t, re.M)) for k in ('topic','sources','couples','source','verified-at','recheck')}
    pos=[re.search(r'^- '+k+r':', t, re.M) for k in ('topic','sources','couples','source','verified-at','recheck')]
    order=[m.start() for m in pos]
    empt=[k for k in ('source','verified-at','recheck') if re.search(r'^- '+k+r':\s*$', t, re.M)]
    ok = all(v==1 for v in counts.values()) and order==sorted(order) and -1 not in order \
         and not empt and max(m.start() for m in pos) < t.index('\n## ') if '## ' in t else False
    if not ok: bad.append(f)
print('files=16 nonconforming=', len(bad), bad)
EOF
```

Result: `files=16 nonconforming= 0 []` — every file carries all six fields **exactly once**, non-empty, in the order `topic < sources < couples < source < verified-at < recheck`, inside the opening block (checked again separately: 0 files with fields past the first heading).

Digest stability vs round-8's recorded after-digests:

```
python3 -c "import hashlib,glob; [print(hashlib.sha256(open(f,'rb').read()).hexdigest()[:16], f.split('/')[-1]) for f in sorted(glob.glob('corpus/knowledge/myth-symbol/*.md'))]"
```
compared line-by-line against the 16 full digests in `reports/round-8/metadata/m09-myth.md` §3 → **16/16 exact match (full 64-hex), 0 drift**.

README index rows:

```
python3 -c "import re; t=open('corpus/README.md',encoding='utf-8').read(); sec=re.search(r'^## myth-symbol/ \(16\)\n(.*?)^## ', t, re.M|re.S); print(len(re.findall(r'^- \`([^\`]+)\`', sec.group(1), re.M)))"
```
→ **16** rows, exact filename match with the partition, under the heading `## myth-symbol/ (16)` at `corpus/README.md:35`.

Gate (2026-10-17T20:51:27Z):

```
python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol/
```
→ `INFO scan: files=16 marks=9 mark-lines=9 findings=0 blocked=0`, exit 0 — byte-identical numbers to round-8's after-run. Gate binary sha256 `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a`, equal to the HEAD blob (`git show HEAD:tools/gates/provenance-audit.py | sha256sum`), so the run reflects committed gate code; this worker did not touch `tools/`.

Pointer/line-reference resolution inside the 48 added header lines (`source`/`verified-at`/`recheck` of all 16 files): every `§N` reference resolves to an existing numbered section (aggregate `missing=[]` across 16 files; per-file refs in the table below), and every `L<n>` reference was verified by printing the referenced line (see §Pointer re-verification).

Mark parity: `to-verify` occurrences per file — `comparative-frameworks.md` 2, `cosmology-cosmography.md` 1, `creation-myths-taxonomy.md` 2, `myth-folktale-genres.md` 1, `myth-ritual-theories.md` 1, `symbolism-synthesis-method.md` 2 = **9 occurrences in 6 files**, identical to round-8's after-state (no marker inflation from the round-8 header wording, which was the round-8 §4 calibration lesson; still holding).

## Per-file result (re-audit)

Field columns are current line numbers; `§refs` are the section references made by the added header triple (all resolve; `missing=[]`); sha256 is the current digest (first 16 hex) and equals round-8's after-digest in every row (full 64-hex equality confirmed).

| # | file | source@ | verified-at@ | recheck@ | first `##` | §refs | sha256 (16) |
|---|---|---|---|---|---|---|---|
| 1 | animal-symbolism.md | 17 | 18 | 19 | 21 | 9, 12 | `8f1fce2d21a1a174` |
| 2 | celestial-symbolism-calendars.md | 21 | 22 | 23 | 25 | 9, 11 + L17, L18 | `2ef711ca56d5e167` |
| 3 | color-symbolism.md | 5 | 6 | 7 | 9 | 1, 11, 12 | `b6830fe792b20740` |
| 4 | comparative-frameworks.md | 21 | 22 | 23 | 25 | 7, 9 + L19 | `532e8e0453602cda` |
| 5 | cosmology-cosmography.md | 21 | 22 | 23 | 25 | 7, 10, 11 | `165f292b95852459` |
| 6 | creation-myths-taxonomy.md | 19 | 20 | 21 | 23 | 12, 14 | `a3736c4c293b66ad` |
| 7 | flood-traditions.md | 20 | 21 | 22 | 24 | 7 | `d02322cd2c2684ad` |
| 8 | hero-journey-variants.md | 21 | 22 | 23 | 25 | 7 | `5ae1e5b9019c9f9c` |
| 9 | motif-index-usage.md | 15 | 16 | 17 | 19 | 7 | `e81f3cdc727672ac` |
| 10 | myth-folktale-genres.md | 21 | 22 | 23 | 25 | 3, 7, 8, 9 | `936f0f4f8f3dd1bf` |
| 11 | myth-ritual-theories.md | 20 | 21 | 22 | 24 | 2–10, 13 | `78fb98725a3376f4` |
| 12 | number-symbolism.md | 6 | 7 | 8 | 10 | 11, 12 | `7149494ed994e155` |
| 13 | pantheon-archetypes.md | 26 | 27 | 28 | 30 | 4, 6, 7 | `59f01b86944cdede` |
| 14 | ritual-liminality.md | 15 | 16 | 17 | 19 | 3, 4, 8, 9 | `b57bf9ac3f8c8bea` |
| 15 | symbolism-synthesis-method.md | 17 | 18 | 19 | 21 | 7, 8, 10 | `8aef07cae6d6c484` |
| 16 | trickster.md | 6 | 7 | 8 | 10 | 4, 9, 11 + L4 | `c1a2c066deeb139f` |

Full digests (`sha256sum corpus/knowledge/myth-symbol/*.md`, 2026-10-17T20:51:06Z) equal the round-8 capture exactly; e.g. `8f1fce2d…b028ffc animal-symbolism.md`, `c1a2c066…931715 trickster.md` (all 16 compared programmatically). Post-write re-verification at 2026-10-17T20:51:49Z (after this fragment was written): `git status --porcelain corpus/knowledge/myth-symbol/` still empty, gate output unchanged (`files=16 marks=9 mark-lines=9 findings=0 blocked=0`), spot digests unchanged.

## Pointer re-verification (line-level)

- `celestial-symbolism-calendars.md` L17 = sources entry "(medicinatradicionalmexicana.unam.mx, accessed 2026-10-17)" ✔; L18 = "Daoist canon check, 2026-10-17: 太上玄靈北斗本命延生真經 = DZ 622 …" ✔ — both in the sources block, matching the header's "access dates L17–L18" claim.
- `comparative-frameworks.md` L19 = sources line "triage round-2 additions (2026-10-17; web-verified): Thureau-Dangin (1921) …" ✔ matching "web-verified note (L19)".
- `trickster.md` L4 = sources line "… — triage round-2 additions (2026-10-17; web-verified): Parsons & Beals (1934) …" ✔ matching "L4".
- Named in-file locations verified against content: `animal-symbolism.md` fossil/geomythology flag sits in §9 (L109, "Fossils and megafauna as myth-stock (calibrate!)"); `flood-traditions.md` source-integrity flags are the last bullet of §7 (L88: Bin Gong xu, Gilgamesh XI geometry, Atrahasis III.vii, lúðr) with §8 heading at L90 — "at the end of §7" ✔; `hero-journey-variants.md` citation-check record (Faulkner, Rank, Schmidt) is the last line of the file (L128 of 128, final bullet of §7) ✔; `myth-folktale-genres.md` type-age debate is in §3 (da Silva & Tehrani vs Bottigheimer) and the literal `to-verify` house-rule token is at L114 (§8) ✔; `symbolism-synthesis-method.md` open Pleiades item at §9 L167 and §10 L171 ✔; `trickster.md` §9 contains the frame caution ("Br'er Rabbit … Cite the tale level, distrust the frame") and Radin's dead-as-chronology line, and §8 contains the frame-capture discussion that §2 itself points to ✔.

## Assessed, no edit needed (kept as an audit record, not a defect claim)

- `trickster.md` recheck cites "(§4, §9)" for three items (Radin chronology / sacred-clown generalization / frame-capture). §4 is the Radin cycle; §9 holds both the chronology verdict and the frame caution; the frame-capture *discussion* is §8 (self-cited from §2). The pair is a defensible anchor set, not a clear miss of the round-8-fixed class (animal §10→§9, myth-folktale §4→§3 were clear misses: content absent from the cited section). Left unchanged to avoid digest churn on pins other round-9 workers may hold.
- `myth-folktale-genres.md` "(unresolved type-age mark (§3))" reads as pointing at the §3 debate, where the unresolved item lives; the literal `to-verify` token is the generic §8 house-rule line. Round-8's own fragment described the mark as "sits in §8"; wording is reconcilable and no reader is sent to a nonexistent or wrong topic. Left unchanged.

## Repo-wide context (not this shard's audit — cited from the auditor shard)

- Auditor shard `reports/round-9/metadata/audit.md` pre-state: `files=179 missing_any=83` opening-block reading — 79 entries missing only the singular `source:` bullet (they carry a `- sources:` ledger) plus 4 verification entries whose trio sits in-body after the first heading. This shard's partition is not among them: 16/16 carry the singular `source:`.
- `corpus/README.md:245-246` ("Most historical entries lack the fleet's complete `source`, `verified-at`, `recheck` header") is still accurate as measured (79/179 whole-file reading, `^- source:` sweep above; 83/179 opening-block per audit.md). README was not edited — out of this worker's write scope; the integrator should re-measure after all 11 shards land.
- Cross-shard shape note (carried from round-8 m09): M08-style shards treat `- sources:` as the source slot while this shard uses the triple per `CORPUS.md:17`; that shape difference is a likely source of the 79 `source:`-only gaps. Flagged for the integrator, not resolved here.

## Limits and disclosures

- Metadata-level audit only: field presence/order/uniqueness, README rows, digest stability, gate parity, and section/line-pointer resolution. The `- sources:` bibliographies were not audited against the cited works, and no URL liveness check was performed in this shard (the round-8 M09 fragment likewise made no link check; V02's link method is partition-specific). No source-truth verification is claimed.
- The six-field census counts literal `^- field:` bullets; a file bundling fields behind `; ` on one line would be missed — none of the 16 does (checked visually in the §Pointer dump).
- All dates in this fragment are 2026-10-17. No `LOG.md`, `SCORECARD.md` or `corpus/lessons/` edits (parent integrates; workers never race shared bookkeeping per `AGENTS.md`).
- Machine-check candidate for the metadata acceptance runner: the field-census script in §Method (asserts six-field presence, uniqueness, order, non-empty, opening-block placement over `corpus/knowledge/myth-symbol/*.md`) plus the digest-equality comparison against the round-8 capture.

## Files written

- `reports/round-9/metadata/v09-myth.md` — this fragment (only file written by this shard)
- `corpus/knowledge/myth-symbol/` — 0 files changed (16/16 already conforming; no straggler found)
