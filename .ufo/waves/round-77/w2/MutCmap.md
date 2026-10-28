# MutCmap — wave-2 falsifier, round 77 (COLLCHECK mutation probes)

Seat: `MutCmap` (leaf, no delegation). Role item: mutation-test **COLLCHECK** in
ACCEPT-C-77 by (1) changing only the staged→lane map document URL to a different
document, (2) changing the Wayback embedded original, (3) using a same-document
URL form; confirm wrong doc fails, live/archive same doc passes.

Attacked W1 artifact: `.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py`
(sha256 `5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4`,
3303 lines). The detector bytes were **never modified** — sha256 identical
before and after every probe (`detector unchanged: True`, summary.json). Each
counter run is a subprocess of the pristine copy (`_st_run` invokes
`sys.executable -B accept-c.py …`); mutations were injected only into fixture
bytes (the freeze-time map document, the frozen `document_url`, or the lands
registry source cell), built with the counter's own fixture machinery
(`_st_build` / `_st_run`, imported read-only from the pristine copy).

**Verdict: all wrong-document mutants KILLED; all same-document URL forms PASS.
No surviving mutant, no false rejection — COLLCHECK's document-identity rule
survives the three named attacks. No coverage finding requiring a contract
change.**

## Baseline (pristine bytes — both green, probes are conclusive)

- Clean fixture: `ACCEPT-C-77: PASS legs=13/13`, exit 0 (`results/P0-clean-baseline.txt`).
- Counter selftest: `SELFTEST: 37/37`, exit 0 (`results/P0b-selftest.txt`), with
  W1's own COLLCHECK matrix reproducing on pristine bytes:
  ```
  CASE collcheck-alias: PASS -- ACCEPT-C-77: FAIL legs=10/13
  CASE collcheck-prose-only: PASS -- ACCEPT-C-77: FAIL legs=10/13
  CASE collcheck-map-alias: PASS -- ACCEPT-C-77: FAIL legs=12/13
  CASE collcheck-archive-identity: PASS -- ACCEPT-C-77: PASS legs=13/13
  ```
- Fixture shape (from `_FX_*`, W1's own constants): rows S004←S901
  (`example.org/docs/alpha`), S005←S902 (`example.org/docs/beta`); map
  `.ufo/waves/round-77/assimilation/id-renumber-map.json` pinned by sha256 in
  `reports/round-77/claims.json`; lands source cell =
  `live <url> ; same page captured <date> at web.archive.org/web/20261027000000id_/<url>`.
  Pristine blob hashes: map@freeze `b142d6c617882fbf…`, registry@lands
  `555d0557ceffb555…`, entry@lands `7a2c6379e470251a…`.

## Probes (expected detector derived from the frozen contract before running)

| probe | smallest mutated point | expected | actual | verdict |
|---|---|---|---|---|
| M1a | map doc for S902 → `https://example.org/docs/beta-alias` (different doc, same host — W1's named case, reproduced independently) | COLLCHECK only | `FAIL legs=12/13`, failing set `{COLLCHECK}` | **killed** |
| M1b | map doc for S902 → `https://other-host.example.org/docs/alpha` (different host *and* path) | COLLCHECK only | `FAIL legs=12/13`, `{COLLCHECK}` | **killed** |
| M2b | map doc for S902 → `https://web.archive.org/web/20240111092427id_/https://example.org/docs/gamma` — Wayback carrier embedding a **wrong original** | COLLCHECK only (wrapper folds to gamma ≠ frozen beta) | `FAIL legs=12/13`, `{COLLCHECK}` | **killed** |
| M2a | lands registry S005 source cell, capture `…/web/20261027000000id_/…docs/beta` → `…id_/…docs/gamma` (embedded original only; live URL untouched) | ROWS (live/capture same-document rule); COLLCHECK must stay green (live URL still names the frozen document) | `FAIL legs=12/13`, `{ROWS}`; COLLCHECK green as predicted | **killed** (by ROWS) |
| M2c | frozen `document_url` for S005 → Wayback carrier of gamma (wrong embedded original on the frozen side) | COLLCHECK + EVIDENCE + GATE | `FAIL legs=10/13`, `{COLLCHECK, EVIDENCE, GATE}` | **killed** |
| M3a | map doc for S902 → `https://www.example.org/docs/beta` (same doc, `www.` form) | all 13 PASS | `PASS legs=13/13` | passes (correct) |
| M3b | map doc for S902 → `https://web.archive.org/web/20200101000000if_/https://example.org/docs/beta` (same embedded original, other timestamp/modifier) | all 13 PASS | `PASS legs=13/13` | passes (correct) |
| M3c | frozen `document_url` for S005 → same-page Wayback carrier of beta (W1 `archive_doc` case: live/archive same doc) | all 13 PASS | `PASS legs=13/13` | passes (correct) |

## Exact fixture outputs (raw, from `results/<probe>.txt`)

```
== M1a ==   ACCEPT-C-77: FAIL legs=12/13
LEG FAIL COLLCHECK
     the map's staged S902 names no document matching the frozen
     example.org/docs/beta | rows=S004,S005 map=.ufo/waves/round-77/assimilation/id-renumber-map.json
== M1b ==   ACCEPT-C-77: FAIL legs=12/13      (same LEG FAIL COLLCHECK line as M1a)
== M2b ==   ACCEPT-C-77: FAIL legs=12/13      (same LEG FAIL COLLCHECK line as M1a)
== M2a ==   ACCEPT-C-77: FAIL legs=12/13
LEG FAIL ROWS
     S005 live URL and captured original are not the same document | added ids=['S004', 'S005'] want=['S004', 'S005']
== M2c ==   ACCEPT-C-77: FAIL legs=10/13
LEG FAIL GATE
     S005 Gate admit row names no URL of the frozen document | gate rows=S004,S005 admit=2
LEG FAIL EVIDENCE
     S005 fetch line does not name the frozen document (example.org/docs/gamma) | rows=S004,S005 windows=305,233
LEG FAIL COLLCHECK
     S005 source cell names a different document than the frozen example.org/docs/gamma
     (document identity, not a raw string); the map's staged S902 names no document matching
     the frozen example.org/docs/gamma | rows=S004,S005 map=.ufo/waves/round-77/assimilation/id-renumber-map.json
== M3a / M3b / M3c ==   ACCEPT-C-77: PASS legs=13/13
```
(Wrapped at ~100 cols here; the receipts hold the unwrapped lines. M1a/M1b/M2b
share one detail string because each leaves exactly one wrong map record: the
folding `(host, decoded path)` — `www.`-strip, `%XX` decode,
`web.archive.org/web/<ts><mod>/<original>` unwrap — puts all three mutants
outside the frozen document key.)

## Restoration evidence

- **M2a (only in-place file mutation):** registry sha256 before
  `555d0557ceffb555…` → mutant `12453f5374d3b540…` → restored `555d0557ceffb555…`
  (byte-identical, `restored_bytes_identical: True`); `git rev-parse
  --show-toplevel` asserted == the fixture lane dir before each commit; counter
  rerun on restored bytes: `PASS legs=13/13` (`M2a-sourcecell-restore.txt`).
- **Builder-injected probes:** each was followed by a pristine rebuild and
  rerun — all eight `-restore` receipts print `PASS legs=13/13`, and every
  restore tree's map blob re-hashes to the pristine `b142d6c617882fbf…`
  (`MATCHES-P0`, measured per tree with `git show <freeze>:<map>`), with
  registry@lands/entry@lands identical to P0. The frozen `claims.json` blob
  differs between any two builds because it embeds the fixture's own base
  commit sha — that is a fresh-rebuild artifact, not incomplete restoration.
- Detector sha256 before/after the whole session: `5ac63e0d…dca4` both sides.
- Counter's operator-default scratch `/fast/scratch/hyaku/kotodama-r77/counter`
  did not exist before or after (selftest ran with `HYAKU_SCRATCH` pointed
  inside the seat's own work dir).

## Findings

1. **Wrong doc fails, same doc passes — exactly as the contract states.** All
   five wrong-document mutants (map alias, map other-host, map Wayback-wrong-
   original, source-cell Wayback-wrong-original, frozen-side Wayback-wrong-
   original) are caught; all three same-document URL forms (`www.` host, other
   timestamp/`if_` wrapper, same-page capture as the frozen `document_url`)
   pass 13/13. The r76 raw-string defect stays fixed and no new alias leak
   exists.
2. **Leg split is by design, and correct:** a wrong Wayback embedded original
   in the *row's capture cell* (M2a) leaves COLLCHECK green because the live
   URL in the same cell still names the frozen document — the capture-fidelity
   kill lives in ROWS' "live URL and captured original are not the same
   document" rule (SCHEMA-NOTE landing-artifacts table: "capture of the *same
   document* | ROWS"). COLLCHECK grades document identity of the frozen
   `document_url` vs the source cell plus the pinned map; M2b/M2c show it kills
   wrong originals wherever the frozen side or the map carries them.
3. **No surviving mutant** → no coverage finding; nothing here licenses a
   contract change. W1's four selftest COLLCHECK cases reproduce on pristine
   bytes (37/37).

## Bounds

Writes: this report, `.ufo/waves/round-77/w2/stage/MutCmap/` (driver +
`results/` receipts, 19 files). Fixture git repos lived only under
`/fast/scratch/hyaku/kotodama-r77/MutCmap` (deleted before this report was
written; verified absent). No fleet/sibling-lane/corpus/reports-production
writes, no lane git/jj/index mutation, no installs (pacman never invoked), no
background jobs, no delegation. Routing: none passed; the counter subprocess
inherits the host environment.

Report: .ufo/waves/round-77/w2/MutCmap.md
