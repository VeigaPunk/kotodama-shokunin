# Round-4 audit — myth-symbol partition

- Role: AUDIT; date: 2026-10-17; status: **NON-CANON**. Lore-shokunin retains canon ownership.
- Scope: all 16 `corpus/knowledge/myth-symbol/*.md` entries, read-only. Only this report was written; no entry, gate, fixture, existing ledger, or LOG.md was edited. No commit was made.
- Worktree HEAD at measurement: `c610e0abd8edf90d6c6d86ebebdc7a7cba8d4a0b`.
- Knowledge-input fingerprint: `sha256sum corpus/knowledge/myth-symbol/*.md | sha256sum` → `b71cf551eac471ec375ee7eacd0b11407d0b664100dd61ee6e66aabb3d4bc40f`.

## Audit rule and result

The checked header fields are the lane's `- topic:`, `- sources:`, and `- couples:`. Indented continuation lists count as field content; whitespace-only or placeholder-only values do not. Calibration must contain identifiable status/limits and reasons, not merely the word "calibration". Explicit calibration blocks inside topical sections count; a separately titled consolidated heading is not required by this audit. Every actual unresolved claim flag must have a claim-specific basis row in an existing `corpus/lessons/*triage*/` ledger; a file's appearance in a scope list alone is not a basis.

**Result: PASS for all 16 files; 0 audit defects.**

- Missing/empty header fields: **0**; all **48** required field instances are nonempty.
- Missing calibration content: **0**. Two entries use distributed calibration blocks; their locations are explicit below.
- Literal `(to-verify)` markers: **0**. Broader case-insensitive `to-verify` inventory: **9 occurrences on 9 lines in 6 files**.
- Actual unresolved claim flags among those occurrences: **0**; unbased claim flags: **0**. The nine inventory mentions are classified individually below, rather than silently discarded or reported as nine resolved factual claims.
- Report rows: **16 file-verdict rows + 9 inventory-classification rows**. No fresh triage decisions or source confirmations were made.

## Per-file verdicts

Entry paths in this table are relative to `corpus/knowledge/myth-symbol/`. Header locators are `topic / sources / couples` line numbers. Every listed field is present and nonempty. Calibration locators identify substantive content, not just a matching keyword.

| Entry | Header lines | Calibration evidence | Raw mentions | Verdict |
|---|---|---|---:|---|
| `animal-symbolism.md` | 3 / 4 / 16 | Distributed blocks: §2 at :24–32 rejects universal-stage totemism with reasons; §4 at :48–54 distinguishes modern neo-shamanism from ethnography; §8–9 at :89–106 bound medical-symbol and fossil-story claims | 0 | PASS |
| `celestial-symbolism-calendars.md` | 3 / 4 / 20 | §9, :149–157, discredited and contested sky-myth frameworks | 0 | PASS |
| `color-symbolism.md` | 2 / 3 / 4 | §11, :128–139, contested/discredited color claims and counterexamples | 0 | PASS |
| `comparative-frameworks.md` | 3 / 4 / 20 | §7, :96–105, overclaim checklist; framework-specific status/reasons in §2–5 | 2 | PASS |
| `cosmology-cosmography.md` | 3 / 4 / 20 | §10, :135–148, calibration checklist and source-specific limits | 1 | PASS |
| `creation-myths-taxonomy.md` | 3 / 4 / 18 | §12, :110–126, contested/discredited claims and source caveats | 2 | PASS |
| `flood-traditions.md` | 3 / 4 / 19 | §7, :76–85, contested flood explanations and source-integrity limits | 0 | PASS |
| `hero-journey-variants.md` | 3 / 4 / 20 | §7, :116–125, rejected mechanisms versus surviving craft models | 0 | PASS |
| `motif-index-usage.md` | 3 / 4 / 14 | §4, :71–88, classification correction and limits of comparative inference | 0 | PASS |
| `myth-folktale-genres.md` | 3 / 4 / 20 | §7, :85–93, dead frameworks, idealization limits, and citation erratum | 1 | PASS |
| `myth-ritual-theories.md` | 3 / 4 / 19 | Distributed theory-specific calibration: :31, :37, :45, :51, :57, :61–70; §10 at :78–91 consolidates explicit statuses and failure modes | 1 | PASS |
| `number-symbolism.md` | 3 / 4 / 5 | §11, :108–119, contested/discredited numerical generalizations | 0 | PASS |
| `pantheon-archetypes.md` | 3 / 4 / 25 | §4, :61–76, trifunctionalism limits; §6, :89–97, calibration bank | 0 | PASS |
| `ritual-liminality.md` | 3 / 4 / 14 | §8, :122–129, contested/discredited/over-applied ritual theories | 0 | PASS |
| `symbolism-synthesis-method.md` | 3 / 4 / 16 | §8, :145–153, disputed frameworks versus designer scaffolding | 2 | PASS |
| `trickster.md` | 3 / 4 / 5 | §9, :71–82, contested readings and corpus/survey limits | 0 | PASS |

## Every remaining inventory mention

These are **not unresolved factual-claim flags**. Prior triage classifications are cited where available. A ledger note or a resolved related claim is not misrepresented as a new claim-specific decision row.

| Entry:line | Mention and classification | Existing ledger context / basis |
|---|---|---|
| `comparative-frameworks.md:110` | "open to-verify items" is a field in the future myth-handoff metadata schema | Local schema at :109–110; no factual proposition is marked. No dedicated decision row for this schema token was located. The absence of such a row is not an unbased-claim defect. |
| `comparative-frameworks.md:114` | Instruction to flag contested items before handoff; the akītu example is explicitly sourced as contested in §3 | `corpus/lessons/round-2-triage/M04.md:13` resolves that underlying claim and explicitly records the §9 cross-reference update. The handoff rule itself is not another claim flag. |
| `cosmology-cosmography.md:152` | "flagging contested or to-verify items" is a future handoff instruction | `corpus/lessons/round-1-triage/M3.md:7,30` explicitly excludes this canon-boundary meta-reference as non-claim text; related akītu decisions are rows at :14–15. |
| `creation-myths-taxonomy.md:131` | "open to-verify items" is a handoff-schema field | `corpus/lessons/round-1-triage/M3.md:30` explicitly identifies this §13 schema reference as a standing instruction, not a current claim flag. |
| `creation-myths-taxonomy.md:135` | Instruction to flag contested examples before handoff | `corpus/lessons/round-1-triage/M3.md:30` explicitly identifies this §14 canon-boundary reference as non-claim text; related claim decisions remain at :17–22. |
| `myth-folktale-genres.md:111` | Record rule: open questions must carry marks | `corpus/lessons/round-1-triage/M5.md:20` has a named row classifying §8 item 13 as a protocol statement, not a factual claim. |
| `myth-ritual-theories.md:106` | Instruction to flag contested items before handoff | `corpus/lessons/round-1-triage/M6.md:22` has a named row classifying this exact §13 occurrence as non-claim handoff wording. |
| `symbolism-synthesis-method.md:164` | Handoff-artifact name plus a Pleiades-date rerun once the fictional world's final latitude exists | `corpus/lessons/round-2-triage/M15.md:18` has a named row covering both the artifact name and this method-internal rerun instruction. This audit does not assert that the fictional astronomical calculation has been performed. |
| `symbolism-synthesis-method.md:168` | "open to-verify list" is the package's handoff-artifact name | `corpus/lessons/round-2-triage/M15.md:19` has a named row classifying it as a handoff-format term, with no factual claim to verify. |

## Verification and reproduction

All entry text was inspected in windows of at most 120 lines. The unchanged, read-only gate was run against the actual partition:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/gates/provenance-audit.py corpus/knowledge/myth-symbol
```

Observed exit **0**; final output:

```text
INFO scan: files=16 marks=9 mark-lines=9 findings=0 blocked=0
```

The gate inventories every `to-verify` string and accepts calibration vocabulary more broadly than this manual content check. Its clean result alone does not establish ledger coverage, meaningful calibration, or nonempty `topic`; those were checked separately. A streamed supplemental check of all three header values, including continuation lists and the gate's placeholder vocabulary, returned:

```text
TOTAL files=16 nonempty_header_fields=48 header_defects=0 raw_tokens=9 literal_markers=0
```

The supplemental header and inventory counts can be reproduced in a streamed pass without reading large files at once:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import re
from pathlib import Path
paths = sorted(Path('corpus/knowledge/myth-symbol').glob('*.md'))
header_re = re.compile(r'^- (topic|sources|couples):[ \t]*(.*)$')
placeholders = {
    '', '-', '--', '—', '?', '??', '???', 'n/a', 'na', 'none', 'null',
    'tbd', 'todo', 'unknown', 'to-verify', '(to-verify)', '((to-verify))',
}
raw = literal = header_defects = 0
for path in paths:
    fields, current = {}, None
    with path.open(encoding='utf-8') as stream:
        for line in stream:
            match = header_re.match(line.rstrip('\n'))
            if match:
                current = match.group(1)
                fields[current] = [match.group(2)]
            elif current and re.match(r'^[ \t]+\S', line):
                fields[current].append(line.strip())
            else:
                current = None
            raw += len(re.findall(r'to-verify', line, re.I))
            literal += len(re.findall(r'\(to-verify\)', line, re.I))
    header_defects += sum(
        ' '.join(fields.get(name, [])).strip().casefold() in placeholders
        for name in ('topic', 'sources', 'couples')
    )
print(f'TOTAL files={len(paths)} nonempty_header_fields={3 * len(paths) - header_defects} '
      f'header_defects={header_defects} raw_tokens={raw} literal_markers={literal}')
PY
```

Observed output is the supplemental `TOTAL` line quoted above. The per-file field locators make the 48-field content check independently inspectable. The input fingerprint command above was repeated after writing this report and matched; the knowledge entries remained unchanged.

## Limits and existing source debt

- This is the assigned three-rule apparatus/flag-basis audit, **not** a fresh scholarly verification of every cultural claim. A PASS does not certify citation accuracy, resolve contested claims, or assert that older CONFIRM rows inspected full primary texts.
- `animal-symbolism.md` and `myth-ritual-theories.md` have substantive distributed calibration blocks rather than a standalone consolidated calibration heading. Their exact locations are reported, not replaced with the gate's weaker keyword test.
- Existing source debt remains visible and is outside the three counted defect classes: `corpus/lessons/round-1-triage/M5.md:24` records the Bascom issue-number correction still reflected in `comparative-frameworks.md:17` versus `myth-folktale-genres.md:93`; `corpus/lessons/round-2-triage/V01.md:64–72` records the Smith essay-placement correction still owed by `myth-ritual-theories.md:8,31` and `pantheon-archetypes.md:16`. These are prior ledger findings, not sources independently reverified here; no entry was repaired or silently certified.
- Only the scoped provenance scan and supplemental read-only checks were run. The full round-close gate battery is the integrator's responsibility. Gate `--selftest` was deliberately not run because its documented behavior regenerates fixtures outside this worker's allowed write path (`tools/gates/provenance-audit.py:56–60`).
- LOG.md was not appended because the assignment permits writes only to this report; round-level bookkeeping remains with the parent/integrator.
