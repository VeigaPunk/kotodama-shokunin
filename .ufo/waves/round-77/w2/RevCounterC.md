# RevCounterC — falsification review of staged `accept-c.py` (round 77, wave 2)

Seat: `RevCounterC` (leaf, reviewer). Target: the **final staged** ACCEPT-C-77
counter `.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py` (3303 lines,
sha256 `5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4`),
checked against `CLAIMS-DRAFT.md` and the routed r76 defects (ROWS predicate
scope, duplicate INDEX / missing SCRATCHMIRROR, COLLCHECK substring identity,
hand-typed legs). Method: full line-level read of the counter + config loaders
+ fixture suite, r76 file diff for the routed defects, and a 16-case mutation
probe suite built on the counter's own `_st_build` machinery
(`stage/RevCounterC/probe.py`, results `probe-results.json`). No lane file
modified; probes ran in `/fast/scratch/hyaku/kotodama-r77/RevCounterC`.

**Verdict: the staged counter is substantially sound — every routed r76 defect
is verifiably fixed — but I falsify it on FOUR graded surfaces: (F1) ROWS's
non-row blind spot was overcorrected into a *whole-document* blind spot
(non-row deletions/edits in `corpus/SOURCES.md` are invisible to every leg and
to the real census); (F2) `required_sections` patterns are not section-scoped,
so the required Paths/Search-log lines can be satisfied in the wrong section;
(F3) INDEX's `base_knowledge` exemption lets fabricated index rows for
pre-existing entries pass unchecked; (F4) FROZENCFG never requires the
`frozen:` stamp key — an *absent* stamp passes. Plus minor dead-code and
coverage nits. None of these makes a clean landing fail; all are falsifier
surface, i.e. ways a mutated landing or freeze slips through.**

## Verified clean (probe-tested or code-confirmed)

| item | result | evidence |
|---|---|---|
| LEGS (13 unique, 1 INDEX, SCRATCHMIRROR present) | OK — `legs_generated()` is the only list; `--emit-legs` prints the draft order verbatim; `_ST_CASES` + my probes confirm reordered/renamed/duplicated frozen lists are *refused* (exit 2, `legs=0/13`, no LEG line) | `LEGS` tuple L2381-2395; `main()` L3246-3258; probes P4b/P4c (exit 2, LEGCOUNT refusal); `--emit-legs` rerun prints the same 13 |
| `lands == base` do-nothing | refused, exit 2, `FAIL legs=0/13` | `main()` L3235-3237; selftest `lands-eq-base` |
| `lands == freeze` do-nothing | graded, FAIL (data legs red; CENSUS/SCRATCHMIRROR/FROZENCFG green) | selftest + my P10: a squash containing the whole landing still fails EVIDENCE because `claims-source` can't name the squash sha |
| ROWS row-line scope (r76 defect 1, first half) | OK — only `| S### |` ids are counted; required non-row additions never fail ROWS; rule-2 cells only on pre-existing rows | `leg_rows` L1440-1557; selftest `index-required-section` fails INDEX only |
| ROWS duplicate *row-set* rows | caught (verbatim twin of a *new* row) — but see F1-class for the base-row blind spots | `line_counts` L1491-1496 |
| COLLCHECK document identity | OK — `_doc_url_key` folds `web.archive.org/web/<ts><mod>/<orig>` to the original, decodes %-escapes, strips `www.`, drops query; path differs → different doc; archive carrier accepted as same doc | `_doc_url_key` L420-443; selftest `collcheck-alias` red / `collcheck-archive-identity` green; my P11 (archive-only source line) green |
| COLLCHECK pinned-map cross-check | OK — `row_set`-only form legal; a pinned map disagreeing with the frozen doc fails COLLCHECK | `_map_pairs`/`leg_collcheck` L1617-1705; selftest `collcheck-map-alias` |
| REPOINTED | OK — exactly one id per `source:` line, line URL must name the row's document, inline ids must resolve to lane/base rows, `removed_ids` flagged, campaign-namespace staged ids flagged | `leg_repointed` L1256-1338; selftest `repointed-legacy-id`, `repointed-source-no-url` |
| SCRATCHMIRROR | OK — reg-ids == base id set, staged-ids covers row_set staged ids, collisions == reg∩staged, adopted lane ids banned from reg-ids, 1-3-space vs 4-space guard both ways on committed bytes | `leg_scratchmirror` L2266-2376; selftest `scratchmirror-*`; real-artifact receipt `scratchmirror-real.txt` |
| FROZENCFG byte-identity + checkout-is-lands | OK — lands claims.json sha vs freeze blob; base ancestry; round/status stamps; clone HEAD/tree == lands; pinned map sha | `leg_frozencfg` L1181-1253; selftest `J3-shrunk-claims`, `map-sha-mismatch` |
| INDEX README leg | OK — one index row per entry inside its partition, verbatim `- topic:` text, live heading counts, last footer total+vector, older footers preserved | `leg_index` L1708-1906; selftest `index-footer`, `counts-extra-knowledge` |
| CENSUS exit-status guard | OK — real `sources-census.sh validate` exits 1 on E-codes; counter treats rc≠0 as fail | `leg_census` L2133-2182; `census-mutated.txt` |
| LEGCOUNT refusal (frozen list differs) | refused, exit 2 | `main()` L3246-3258; probes P4b/P4c |
| scratch discipline | OK — `--work`/`$HYAKU_SCRATCH`/operator `$TMPDIR`/default `/fast/scratch`; `/tmp` refused; no literal `/tmp` in source | `_scratch_root`/`_forbidden_scratch` L2481-2506; `scratch-probe.txt` |
| selftest 37/37 | re-verified on the staged bytes: `SELFTEST: 37/37`, exit 0 | `stage/RevCounterC/selftest-rerun.txt` |

## Findings (falsifier surface, severity high→low)

### F1 — ROWS-scope overcorrection: non-row deletions/edits in `corpus/SOURCES.md` are invisible to every leg (and to the real census). MEDIUM.

The routed r76 defect was: ROWS failed *added* non-row lines (the required
Paths/Search-log lines) as out-of-set rows. The fix narrowed ROWS to row-line
ids only — but r76's leg also carried a **line-multiset diff** that failed
every *removed* non-blank line (`accept-c-r76.py` ~L1587-1595: `added_lines`/
`removed_lines` via `Counter(...)`). r77 `leg_rows` (L1440-1557) keeps the
"no other row change" rule but dropped the removed-line half entirely:

- probe **P3**: lands deletes the `## Search log` heading and its historical
  line → `ACCEPT-C-77: PASS legs=13/13`.
- probe **P1**: a verbatim duplicate of a *base* row appended inside
  `## Registry` → PASS (`line_counts` only flags `sid in want`, L1492-1494).
- probe **P2**: a same-id shadow row with *different* cells, corrupt twin
  first → PASS (`parse_rows` last-wins picks the good copy; the corrupt copy
  is invisible).
- probe **P9**: a non-S junk row (`| T001 | …`, 11 cells) inside `## Registry`
  → PASS (never matches `ROW_RE`).

The real census *does* cover P1/P2/P9 (E03/E04/E05/E06/E02, exit 1 —
`census-mutated.txt`), so a real landing can't ship those. **But it exits 0
on P3** — deleting a section heading or rewriting search history is a falsifier
path: kill-rule-adjacent registry vandalism that passes 13/13. The counter's
ROW_SHAPED_LINE_RE (L203) is defined but **never used** (it survives only for
README-side checks in r76). Fix direction: keep additions row-scoped (the r76
false-positive fix) but restore a removed/edited non-blank-line check minus
the declared `required_sections` additions; or add `required_sections`
"absent-if-removed" negative patterns. Claim-side, the draft only promises
ROWS counts row additions — but nothing else protects the registry body.

### F2 — `required_sections` patterns are not section-scoped (and presence-only, not addition-scoped). LOW–MEDIUM.

`leg_index` L1882-1894 greps `spec["pattern"]` per line in the *whole file*
of `spec["path"]`. Nothing ties the hit to a section: probe **P5** moves the
required Paths bullet inside `## Registry` (above the `## Paths` heading) and
the search-log entry inside `## Paths` → PASS 13/13. A `## Paths` pattern
satisfied inside `## Sources` would equally pass. Also, the check passes when
the pattern already existed at base (it isn't an *addition* check) — harmless
for the current ids (S897/S898/round-77 phrase can't pre-exist) but worth
noting for reuse. The skeleton's patterns (`^- [^\n]*S897[^\n]*S898`,
`(?i)^\*\*[^*]*naming-system[^*]*\(round 77\)`) can't match a `| S### |` row
line, so row-padding can't satisfy them — that part is sound. Mitigation:
freeze `label`-ed patterns that include the heading context, or teach the leg
a `section:` key.

### F3 — INDEX `base_knowledge` exemption admits fabricated index rows for pre-existing entries. LOW–MEDIUM.

`leg_index` L1862-1865 exempts every added README line of the form
`- \<file>.md` — …` when the basename exists at base (`base_knowledge` =
*all* basenames under `corpus/knowledge`, md or not — `tree_files` is
unfiltered). Probe **P6a**: lands appends
``- `sample.md` — FABRICATED duplicate index row.`` → PASS 13/13. The
per-entry `hits`/`topic` checks (L1754-1778) only run for the *adopted*
entries, so a duplicated base index row with arbitrary text is invisible —
an asymmetry with the adopted rows (which must be unique and verbatim).
P6b shows a fabricated `## linguistics/ (2)` section heading *is* caught
(it inflates `parts` → footer vector length mismatch — interesting but
working). Fix: restrict the exemption to index rows whose name is the adopted
entry, or dedupe-compare counts for base names too.

### F4 — FROZENCFG: an *absent* `frozen:` stamp passes. LOW.

L1211-1221: `cfg["doc_frozen"]` is checked only when the key is *present* —
`bool False` fails, a 40-hex must equal the freeze sha, a non-hex non-null
value fails — but **`frozen` absent → nothing appended → leg green**. Probe
**P4**: freeze claims.json with `round:77`/`status:"frozen"` but no `frozen`
key → PASS 13/13. SCHEMA-NOTE line 41 names `frozen` ("`true` or the freeze
sha") a document-level stamp the leg reads; `round`/`status` are hard-required
by contrast. One-line fix: append a `bad` when `frozen is None`.

### F5 — CENSUS E-code detector regex can't match the real TSV shape (dead code). NIT.

`leg_census` L2154: `re.findall(r"(?m)^E\d\d\b", out)` — the real script emits
`file\tE03\t…` (E-code in TSV column 2, never column 1). The regex never
matches real output. Harmless because `r.returncode != 0` is what actually
gates (census exits 1 on E-codes — verified), but the declared "no E-code
line" check as written is dead. Fix: `(?m)^\S+\tE\d\d\b` or `\bE\d\d\b`.

### F6 — SCRATCHMIRROR: the planted guard id isn't bound to the row set. NIT.

L2324-2332 requires "exactly one planted row detected" but never checks the
planted id is a row_set id (the real proof plants S897, a row id — confirmed
`reg-ids=820 staged=132 collisions=38 planted=S897`). A proof planting an
unrelated id still satisfies "exactly one". Minor: the proof's purpose is
regex-width evidence, so this is cosmetic.

### F7 — `leg_gate` fallback `if not shown and not bad:` is dead code. NIT.

L2055: `bad` is the leg-global list; once any earlier row failed, `not bad`
is False, and when all rows fail the leg already fails — the `could not be
verified` fallback can never be reached alone. No behavior change; delete or
scope `bad` per row for honest reporting.

### F8 — `lands` ancestry is checked against `base` only, never against `freeze`. NIT (by design?).

`main()` L3238-3241 + `leg_frozencfg` L1201 both require `base` ancestor of
`lands`; nothing requires `freeze` ancestor of `lands`. Probe **P7**: lands
branched from `base` (not descending the freeze) with byte-identical
claims.json → PASS 13/13. Since the graded content is byte-pinned this is
defensible, but if the protocol intends "lands applies the frozen config
on top of the freeze commit", it isn't enforced.

### F9 — COLLCHECK presence-only: extra unrelated URLs in a row's source cell pass. NIT.

`leg_collcheck` L1680-1684 checks `frozen_key ∈ row source keys`; `_doc_pair`
(L456-465) requires ≥1 live + ≥1 matching capture. Probe **P8**: source cell
adds `; also https://unrelated.example.net/page` → PASS 13/13. A row can
smuggle an unopened extra document alongside the frozen pair. Fix direction:
require the source cell's document key set ⊆ {frozen doc} (after archive
folding).

## Probe transcript (all runs; fixture = counter's own `_st_build`, mutated then
re-committed; `--work /fast/scratch/hyaku/kotodama-r77/RevCounterC/work/*`)

```
P0-clean                          PASS 13/13  exit 0   (control)
P1-dup-base-row-verbatim          PASS 13/13  exit 0   (F1: invisible)
P2-dup-id-diff-content            PASS 13/13  exit 0   (F1: shadow row invisible)
P3-delete-non-row-lines           PASS 13/13  exit 0   (F1: non-row deletion)
P3b-delete-required-line          FAIL 12/13  exit 1   (INDEX red — correct)
P4-frozen-stamp-absent            PASS 13/13  exit 0   (F4)
P4b-frozen-legs-reordered         refused     exit 2   (LEGCOUNT — correct)
P4c-frozen-legs-renamed           refused     exit 2   (LEGCOUNT — correct)
P5-required-lines-wrong-section   PASS 13/13  exit 0   (F2)
P6a-fabricated-index-row-only     PASS 13/13  exit 0   (F3)
P6b-fabricated-index-row+heading  FAIL 12/13  exit 1   (INDEX red via parts+1)
P7-lands-not-descending-freeze    PASS 13/13  exit 0   (F8, by design?)
P8-extra-url-source-cell          PASS 13/13  exit 0   (F9)
P9-junk-non-S-row                 PASS 13/13  exit 0   (F1-class; real census E02 catches)
P10-lands-eq-freeze-full-landing  FAIL 12/13  exit 1   (EVIDENCE red — squash sha can't be named)
P11-archive-only-source-line      PASS 13/13  exit 0   (correct: archive folds to doc)
```

Real-census cross-check of the mutated registries (`census-mutated.txt`):
`dup-verbatim` → E03/E04 exit 1; `dup-shadow` → E05/E06/E03 exit 1;
`del-nonrow` → ok exit 0; `junk-row` → E02 exit 1; `clean` → ok exit 0.
So F1's row-shaped variants (P1/P2/P9) are backstopped by CENSUS at a real
landing; **P3 (non-row deletion) is not**.

Selftest re-run on the staged bytes: `SELFTEST: 37/37`, exit 0
(`stage/RevCounterC/selftest-rerun.txt`); `--emit-legs` prints the 13-name
draft order.

## Residual risk / freeze obligations (not counter bugs)

- `removed_ids` must carry S886/S888/S889/S890/S891/S896 — the loader
  tolerates an absent list (REPOINTED then can't guard the rewrite clause).
- `required_sections` patterns must be written so only the intended new lines
  match (F2); the skeleton's are adequate.
- `refused_staged` ids that are only *held* (S906/S907/S911) must stay out of
  the refusal keys or GATE owes them a row.
- Evidence producers must emit `claims-source` naming the freeze and
  `claims-frozen: yes` (EVIDENCE requires both; R3 in the W1 report stands).
- `--lands == --freeze` is *legal* (graded, not refused) — a same-commit
  freeze+landing is blocked in practice because `claims-source` can't name a
  not-yet-existing sha (P10 fails EVIDENCE); a freeze containing all landing
  artifacts is still worth a checklist look.

## Tested commands (verbatim)

```
HYAKU_SCRATCH=$SEAT python3 -B selftest-run/accept-c.py --emit-legs
HYAKU_SCRATCH=$SEAT python3 -B selftest-run/accept-c.py --selftest   # 37/37
HYAKU_SCRATCH=$SEAT python3 -B probe.py                              # 16 probes
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
    --file <case>/corpus/SOURCES.md --today 2026-10-27               # 5 runs
git show 211f9526800906e0c585d878d265c37e5e090c15:reports/round-76/accept-c.py
git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md | grep -c '^| S'  # 820
```

## Installs

None. No package, tool or system file was installed, upgraded or removed
(pacman untouched).

## Scratch

All probes ran under `/fast/scratch/hyaku/kotodama-r77/RevCounterC`
(cases/, work/, selftest-run/, probe.py, probe-results.json); every git call
was `git -C <fixture>` against a fixture whose `rev-parse --show-toplevel`
was asserted by the counter's own `_st_build`. Receipts copied to
`.ufo/waves/round-77/w2/stage/RevCounterC/`; scratch deleted on completion.
