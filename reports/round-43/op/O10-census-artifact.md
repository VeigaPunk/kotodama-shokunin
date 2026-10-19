# O10 — census artifact (claim O)

- Seat: O10 | executor | claim O | date 2026-10-19 | baseline `7ceff59`
- Out: `reports/round-43/op/O10-census-artifact.md`
- Mission (`reports/round-43/targets.json`, seat `O10`): "write the exact calib/census artifact the integrator files (four-class totals, every fallback mapping, the corrected 334/319/15 comparison). Reference shape only; integrator fills live numbers post-run."
- Method: read-only. No filed byte edited; no corpus staging; no `reports/round-*/run-validation.py` executed; no git/network/install. All runs from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

This file is a **fill-ready artifact contract plus a measured prediction**, not the filed census. The integrator files the two artifacts in §1 after the round's landing state is fixed. Every number below is labelled `MEASURED`, `PREDICTED`, or `TO-VERIFY`.

---

## 0. Three findings that change what the integrator should file

### 0.1 A durable successor instrument already exists at HEAD — the claim's `before` is stale as to durability

`reports/round-43/claims.json:27` says "no durable instrument implements the r39 basename-couples policy; the only resolver that ever ran (r39 I-C05) lives in ephemeral `.scratch`". At the declared baseline `7ceff59` that is not true of the tree:

- `tools/harness/couples-reference-extractor.py` is tracked at HEAD (`git log --oneline -1 -- tools/harness/couples-reference-extractor.py` → `7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore`).
- Its selftest is green, 8/8, exit 0: wrapped positive 4/4 (`sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`, `writing-systems.md`), soft-wrap heal, unwrapped regression, over-capture trap, phantom negative, two N6 regression guards, glob-fragment class (`python3 -B tools/harness/couples-reference-extractor.py --selftest`, 2026-10-19).
- It has a block parser (`couples_block`, `:50-73`), a hyphen-aware join (`join_parts`, `:76-93`), the four policy classes plus two disposition labels (`classify`, `:134-150`), per-entry records (`resolve_entry`, `:153-183`), and a corpus census (`census`, `:186-211`; CLI `:298-330`).
- `reports/round-42/validation.json` records claim O as `"passed": true` with `selftest_tail` ending "PASS glob fragment classified". The r42 commit message itself says "O verified".

What is still genuinely owed by r43, and what this artifact supplies:

1. The **four-class** presentation the r43 claim requires (`claims.json:28`), where the existing tool emits six buckets (`direct`, `fallback`, `ambiguous`, `unresolved`, `prospective`, `glob-fragment`). §5 reconciles the two without dropping a token.
2. The **disposition leg** at census granularity (every fallback mapping; every unresolved/ambiguous row with a named reason), §7-§8.
3. A **durable, filed capital-C Census** at `reports/round-43/calib/` with provenance (tool digest, population digest, command, arithmetic checks), §1-§3. The r42 corrected census (`reports/round-42/op/couples-census-corrected.json`, 1,371 bytes, schema `kotodama-couples-census-v2`) carried aggregate figures only, no per-row dispositions and no population digest.

The parent should not score claim O as "tool built from zero". The honest axis move is **census artifact + four-class reconciliation + disposition leg**, on top of an already-durable r42 instrument. If the integrator lands a second tool (`basename-couples-resolver.py`) it must either wrap or supersede the r42 tool explicitly, and the census must name which tool produced it (the JSON `tool.path`/`tool.sha256` fields force this).

### 0.2 The live census at 223 entries — measured

Command: `python3 -B tools/harness/couples-reference-extractor.py --census` (2026-10-19, HEAD `7ceff59`, 223 entries):

```
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
```

- `ambiguous=0` is omitted by the tool's `if v` print filter; it is present in the totals dict as 0.
- The six buckets sum exactly: `2556 + 166 + 0 + 2 + 5 + 1 = 2730`.
- Policy-strict four-class view (§5): `direct=2556`, `fallback=166`, `ambiguous=0`, `unresolved=7` (`2` wrong-path + `5` declared-prospective), plus `1` named glob-fragment exclusion; `2556 + 166 + 0 + 7 = 2729`, `2729 + 1 = 2730`.
- Population manifest: `sha256` over sorted `path:sha256` lines = `444ff801727604b614e1eca302ff77314ebbd0f5f064a82d1c167e7f02125e35` (223 entries). Recipe in §11.

### 0.3 Two landing hazards the census must record, not smooth over

1. **The r42 C01 spare duplicates a live topic.** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists at HEAD (26-entry partition; landed by r42 commit `7ceff59`). The spare's own integrator ruling says C04's lithic entry landed and "THIS draft is routed as the named spare for a future re-scoped claim" (`reports/round-42/cov/C01-mineral-spare.md:1`). Claim C (`reports/round-43/claims.json:40-41`) asks to land that spare as the lithic register at myth-symbol 26→27, but the slot is already occupied. The C seats must resolve this before the 224 count is real; the census **records the live entry count it ran on** and never back-fills 224. Shared rule: "never overwrite an existing entry; report collisions".
2. **The wrapped-field read changes a token's identity, not the class totals.** The r42 C01 spare's fenced `- couples:` is a single line with 30 tokens, all `direct` at a myth-symbol entry directory (measured, §10). If it lands unmodified the census grows by 30 direct tokens; if the C landing is blocked or lands different bytes, the census delta changes. The artifact's post-landing row is therefore a `PREDICTED` placeholder until the tool runs on the closed tree.

---

## 1. What the integrator files

Two files, both under `reports/round-43/calib/` (the path named by `claims.json:28`):

| file | role | schema / shape |
|---|---|---|
| `reports/round-43/calib/basename-couples-census.json` | machine-readable census; the durable record | `kotodama-couples-census-v3` (§2) |
| `reports/round-43/calib/basename-couples-census.md` | human summary, provenance, comparison bridge, disposition table, raw stdout | §3 skeleton |

**Preferred generation.** The tool writes the JSON itself, e.g.:

```
python3 -B tools/harness/basename-couples-resolver.py --census --json \
  > reports/round-43/calib/basename-couples-census.json
```

The r42 tool's `--census` currently prints text only (`tools/harness/couples-reference-extractor.py:305-317`); if the landed r43 tool also lacks `--json`, the integrator must either add the flag (a tool change, not a corpus change) or capture the text in the Markdown's `raw_stdout` block and fill the JSON from it. **Never hand-enter a count that the tool did not print**; if a field cannot be recovered, write `null` with `"recoverable": false` and a reason — the shared rule says unknown counters stay `null`, not inferred.

**Do not** file this `op/` file as the census. It contains placeholders and a prediction; filing it would be a false measurement.

---

## 2. JSON skeleton — `kotodama-couples-census-v3`

Fenced block. Replace every `<FILL: ...>`; keep every invariant. The two example rows (`per_entry`, `fallbacks`) are shape examples, not data — the live arrays carry one row per entry (223 at the 2026-10-19 tree) and one row per fallback occurrence (166 at that tree).

```json
{
  "schema": "kotodama-couples-census-v3",
  "round": 43,
  "status": "filed",
  "generated_at_utc": "<FILL: ISO-8601 Z, from `date -u +%Y-%m-%dT%H:%M:%SZ`>",
  "declared_baseline_commit": "7ceff59",
  "run_head": "<FILL: git rev-parse --short HEAD>",
  "supersedes": "reports/round-42/op/couples-census-corrected.json (kotodama-couples-census-v2, 220-entry aggregate)",
  "tool": {
    "path": "<FILL: tools/harness/basename-couples-resolver.py | tools/harness/couples-reference-extractor.py>",
    "sha256": "<FILL: 64-hex sha256 of the tool bytes>",
    "selftest_command": "python3 -B <FILL: tool path> --selftest",
    "selftest_exit": 0,
    "selftest_controls": {"passed": "<FILL: int>", "total": "<FILL: int>"},
    "relationship_to_r42": "<FILL: 'same instrument' | 'wrapper over' | 'supersedes; reason'>"
  },
  "command": "<FILL: exact --census command and redirection>",
  "exit_code": 0,
  "population": {
    "entries": "<FILL: int>",
    "partitions": {
      "linguistics": "<FILL: int>",
      "myth-symbol": "<FILL: int>",
      "culture-material": "<FILL: int>",
      "synthesis": "<FILL: int>",
      "verification": "<FILL: int>",
      "civilizations": "<FILL: int>"
    },
    "partition_sum_check": "<FILL: bool; partitions sum == entries>",
    "manifest_sha256": "<FILL: sha256 over sorted 'path:sha256' lines; recipe §11>",
    "manifest_recipe": "sha256( '\\n'.join(f'{path}:{sha256(bytes)}' for path in sorted(glob('corpus/knowledge/*/*.md'))) )"
  },
  "class_model": {
    "policy_classes": ["direct", "fallback", "ambiguous", "unresolved"],
    "disposition_labels_not_classes": {
      "prospective": "an unresolved token whose field explicitly declares it as a prospective/seed file; re-labelled unresolved with reason 'declared-prospective' in the strict view",
      "glob_fragment": "an extractor artifact (policy §5.6); excluded from couples classes, listed, never counted as unresolved"
    },
    "identities": [
      "totals_policy_strict.classified == direct + fallback + ambiguous + unresolved",
      "totals_policy_strict.extracted == classified + excluded_total",
      "totals_tool_native.refs == direct + fallback + ambiguous + unresolved + prospective + glob_fragment",
      "totals_policy_strict.unresolved == totals_tool_native.unresolved + totals_tool_native.prospective",
      "totals_policy_strict.excluded_total == totals_tool_native.glob_fragment"
    ]
  },
  "totals_policy_strict": {
    "extracted": "<FILL: int>",
    "classified": "<FILL: int>",
    "direct": "<FILL: int>",
    "fallback": "<FILL: int>",
    "ambiguous": "<FILL: int>",
    "unresolved": "<FILL: int; includes the 5 prospective re-labels>",
    "excluded_total": "<FILL: int>",
    "excluded": {"glob_fragment": "<FILL: int>", "prospective": 0}
  },
  "totals_tool_native": {
    "refs": "<FILL: int>",
    "direct": "<FILL: int>",
    "fallback": "<FILL: int>",
    "ambiguous": "<FILL: int>",
    "unresolved": "<FILL: int>",
    "prospective": "<FILL: int>",
    "glob_fragment": "<FILL: int>"
  },
  "reconciliation": {
    "strict_unresolved_equals_native_unresolved_plus_prospective": "<FILL: bool>",
    "extracted_equals_classified_plus_excluded": "<FILL: bool>",
    "zero_tokens_dropped": "<FILL: bool>",
    "native_refs_equals_strict_extracted": "<FILL: bool>"
  },
  "wrapped_fields": [
    {
      "path": "corpus/knowledge/linguistics/phonetics-phonology.md",
      "couples_span": "72-77",
      "header_line": 72,
      "continuation_lines": [73, 74, 75, 76, 77],
      "single_line_tokens": 0,
      "block_tokens": 4,
      "tokens": ["sound-change.md", "sound-symbolism.md", "tone-prosody.md", "writing-systems.md"],
      "soft_wrap_repairs": [
        {"raw": "tone-<LF>  prosody.md", "joined": "tone-prosody.md", "at": "76-77"}
      ],
      "token_classes": {
        "sound-change.md": "prospective",
        "sound-symbolism.md": "direct",
        "tone-prosody.md": "prospective",
        "writing-systems.md": "direct"
      },
      "phantom_tokens_rejected": ["prosody.md", "toneprosody.md"]
    }
  ],
  "per_entry": [
    {
      "path": "corpus/knowledge/<FILL: partition>/<FILL: file>.md",
      "partition": "<FILL>",
      "refs": 0,
      "direct": 0,
      "fallback": 0,
      "ambiguous": 0,
      "unresolved": 0,
      "prospective": 0,
      "glob_fragment": 0,
      "policy_strict_unresolved": 0,
      "wrapped": false,
      "couples_span": "<FILL: start-end or null>"
    }
  ],
  "fallbacks": [
    {
      "entry": "corpus/knowledge/<FILL: entry>.md",
      "line": 0,
      "token": "<FILL: bare basename>.md",
      "target": "corpus/knowledge/<FILL: partition>/<FILL: file>.md",
      "group": "<FILL: myth-symbol | linguistics | culture-material | civilizations | verification | synthesis | null>",
      "aligned": "<FILL: true | false | null when group is null>"
    }
  ],
  "unresolved": [
    {
      "entry": "corpus/knowledge/<FILL: entry>.md",
      "line": 0,
      "token": "<FILL: token>",
      "native_class": "<FILL: unresolved | prospective | glob-fragment>",
      "strict_class": "<FILL: unresolved | excluded>",
      "disposition": "<FILL: wrong-path-phantom | declared-prospective | glob-fragment>",
      "reason": "<FILL: one sentence, no inference beyond the field bytes>",
      "owner": "<FILL: named seat/role>",
      "evidence": "<FILL: file:line or command output path>"
    }
  ],
  "ambiguous": [],
  "ambiguous_branch": {
    "live_instances": 0,
    "status": "unexercised-live",
    "control": "REQUIRED from the landed tool: a synthetic ambiguous pair (two files with the same basename -> ambiguous). The r42 selftest does NOT carry this control (it has the phantom negative only); if the landed r43 tool also lacks it, set status 'unexercised-live-and-uncontrolled' and record the claim-threshold miss.",
    "note": "no duplicate basename exists under corpus/knowledge/*/*.md at the census tree; the four-class census reports ambiguous=0 and the branch is unexercised live"
  },
  "alignment": {
    "labeled_fallback_rows": "<FILL: int>",
    "aligned": "<FILL: int>",
    "misaligned": 0,
    "unlabeled_fallback_rows": "<FILL: int>",
    "findings": []
  },
  "comparisons": {
    "r37_eleven_entry": {
      "entries": 11,
      "refs": 334,
      "direct": 319,
      "fallback": 15,
      "ambiguous": 0,
      "unresolved": 0,
      "manifest_sha256": "9d97bde0713879c700f8070087096ff226a9b3880f831d893609ea890d0e2aee",
      "r43_result": "REPRODUCED at HEAD 7ceff59 (see §4)"
    },
    "r39_corpus_212": {
      "entries": 212, "refs": 2504, "direct": 2335, "fallback": 163,
      "ambiguous": 0, "unresolved": 6,
      "source": "reports/round-39/calib/basename-couples-policy.md §6 Part 2 (filed run at dfb0719)"
    },
    "r42_corpus_220_single_line": {
      "entries": 220, "refs": 2607, "direct": 2435, "fallback": 166,
      "ambiguous": 0, "unresolved": 6,
      "source": "reports/round-42/calib/Ca01-gap-fill.md:74-79 (recount table)"
    },
    "r42_corpus_220_block": {
      "entries": 220, "refs": 2611, "direct": 2437, "fallback": 166,
      "ambiguous": 0, "unresolved": 8,
      "source": "reports/round-42/op/couples-census-corrected.json:figures"
    },
    "r43_prelanding_223": {
      "entries": 223, "refs": 2730, "direct": 2556, "fallback": 166,
      "ambiguous": 0, "unresolved_strict": 7, "prospective": 5, "glob_fragment": 1,
      "manifest_sha256": "444ff801727604b614e1eca302ff77314ebbd0f5f064a82d1c167e7f02125e35",
      "status": "MEASURED 2026-10-19 at 7ceff59"
    },
    "r43_closed_tree": {
      "entries": "<FILL: int>",
      "refs": "<FILL: int>",
      "direct": "<FILL: int>",
      "fallback": "<FILL: int>",
      "ambiguous": "<FILL: int>",
      "unresolved_strict": "<FILL: int>",
      "prospective": "<FILL: int>",
      "glob_fragment": "<FILL: int>",
      "manifest_sha256": "<FILL: recomputed on the closed tree>",
      "status": "MEASURED at the round's closed tree"
    }
  },
  "delta_bridge": [
    {"from": "r39_212", "to": "r42_220_block", "entries": 8, "refs": 107, "direct": 102, "fallback": 3, "unresolved": 2},
    {"from": "r42_220_block", "to": "r43_prelanding_223", "entries": 3, "refs": 119, "direct": 119, "fallback": 0, "unresolved": 0},
    {"from": "r43_prelanding_223", "to": "r43_closed_tree", "entries": "<FILL>", "refs": "<FILL>", "direct": "<FILL>", "fallback": "<FILL>", "unresolved": "<FILL>"}
  ],
  "controls": {
    "wrapped_positive_4_of_4": "<FILL: bool; tokens exactly the four in wrapped_fields>",
    "soft_wrap_heals_tone_prosody": "<FILL: bool; 'prosody.md' absent from every token set>",
    "phantom_negative_absent_target_visible": "<FILL: bool>",
    "ambiguous_synthetic_pair": "<FILL: bool>",
    "glob_fragment_excluded": "<FILL: bool>",
    "over_capture_prose_excluded": "<FILL: bool>",
    "single_line_regression_zero_tokens": "<FILL: bool>"
  },
  "raw_stdout": "<FILL: verbatim --census stdout, or null when --json emitted this file>"
}
```

---

## 3. Markdown companion skeleton — `basename-couples-census.md`

```markdown
# Basename-couples census — round 43

- Generated: <FILL ISO-8601 Z> | lane HEAD: <FILL> | declared baseline: 7ceff59
- Tool: `<FILL path>` sha256 `<FILL 64 hex>`
- Command: `<FILL exact command>`, exit `<FILL>`
- Population: <FILL N> entries; manifest sha256 `<FILL>`; partitions `<FILL/…>`
- JSON: `basename-couples-census.json` sha256 `<FILL: computed after write>`

## Totals

| view | refs | direct | fallback | ambiguous | unresolved | prospective | glob-fragment |
|---|---|---|---|---|---|---|---|
| policy-strict four-class | <FILL> | <FILL> | <FILL> | <FILL> | <FILL> | — (re-labelled into unresolved) | — (excluded) |
| tool-native six-bucket | <FILL> | <FILL> | <FILL> | <FILL> | <FILL> | <FILL> | <FILL> |

Identity checks: `<FILL: five booleans from class_model.identities, each true/false>`.

## Wrapped-field proof (D1)

- `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`; single-line 0 tokens; block 4/4.
- Tokens: `sound-change.md` (prospective), `sound-symbolism.md` (direct), `tone-prosody.md` (prospective), `writing-systems.md` (direct).
- Soft wrap repaired: `tone-` + newline + `prosody.md` -> `tone-prosody.md`; the raw block parse's `prosody.md` is a phantom and must not appear in any token set.

## Fallback mappings

All <FILL: 166> rows are in the JSON `fallbacks` array, sorted by (entry, token). Distinct mappings: <FILL: 50>.
Every `fallback` row cites `token -> target`; no row is counted without its mapping.

## Disposition table

One row per extracted token that is not `direct`/`fallback`. At the 223-entry tree: 8 rows
(2 wrong-path, 5 declared-prospective, 1 glob-fragment). <FILL: paste/verify the tool's rows; the expected set is §8>.

## Comparison bridge

`r37 eleven-entry`: 334 = 319 direct + 15 fallback + 0 ambiguous + 0 unresolved — **REPRODUCED** at r43 HEAD.
`r39 212`: 2504 = 2335 + 163 + 0 + 6.
`r42 220 single-line`: 2607 = 2435 + 166 + 0 + 6; block: 2611 = 2437 + 166 + 0 + 8.
`r43 closed tree`: <FILL> = <FILL> + <FILL> + <FILL> + <FILL> (+ <FILL> prospective + <FILL> glob on the native view).

## Drift from the O10 prediction

<FILL: list every field where the closed-tree run differs from §10's prediction, or state "none".
A drift is a finding to file, never a number to overwrite silently.>

## Raw stdout

```
<FILL: verbatim output>
```
```

---

## 4. The corrected 334/319/15 comparison — measured at r43 HEAD

The eleven entries are the r37 population (`reports/round-37/adj/A02-entries-bleed.md:7`; roster `reports/round-37/scout/K04-entries-scout.md:25`). Measured 2026-10-19 at `7ceff59` with the block + hyphen-join reader:

| entry | refs | direct | fallback | ambiguous | unresolved |
|---|---:|---:|---:|---:|---:|
| `agrarian-field-system-lexicon.md` | 22 | 22 | 0 | 0 | 0 |
| `bathing-and-body-hygiene.md` | 25 | 25 | 0 | 0 | 0 |
| `fire-fuel-light.md` | 44 | 44 | 0 | 0 | 0 |
| `funerary-material-culture.md` | 48 | 48 | 0 | 0 | 0 |
| `furniture-interior-lexicon.md` | 19 | 19 | 0 | 0 | 0 |
| `writing-media-surface-economy.md` | 20 | 20 | 0 | 0 | 0 |
| `timekeeping-instruments.md` | 25 | 25 | 0 | 0 | 0 |
| `binding-speech-complex.md` | 40 | 40 | 0 | 0 | 0 |
| `death-afterlife-eschatology.md` | 25 | 25 | 0 | 0 | 0 |
| `eschatology-world-end-systems.md` | 30 | 30 | 0 | 0 | 0 |
| `sacred-kingship-mythic-charter.md` | 36 | 21 | 15 | 0 | 0 |
| **TOTAL** | **334** | **319** | **15** | **0** | **0** |

- Identity: `319 + 15 + 0 + 0 = 334`. **PASS.**
- The 15 fallbacks are all from `sacred-kingship-mythic-charter.md:37`; the r39 policy §4 population is unchanged.
- The population is pinned by `eleven_manifest_sha256 = 9d97bde0713879c700f8070087096ff226a9b3880f831d893609ea890d0e2aee` (sorted `path:sha256` lines; recipe §11). If those bytes move, re-run and record the new digest — do not quote 334/319/15 as a timeless fact.
- This is the **corrected** comparison: the same 334 total as r37, but produced by the block + hyphen-join reader, with zero phantoms. The r37 A06/A08 conditional ("0 unresolved only if the unique-basename fallback is adopted") is now the filed policy, and the r43 re-run confirms it at the current tree.

**What "corrected" does not mean.** The 334/319/15 is the eleven-entry r37 population, not the corpus-wide total. Corpus-wide at 223 is 2730 refs (native six-bucket) / 2729 classified (strict four-class). Keep the units separate; the r37 integration ruling (`reports/round-37/scribe/S04-integration-draft.md:38,80`) is still binding.

---

## 5. Four policy classes vs the tool's six buckets — the reconciliation rule

The r39 policy defines four classes (`reports/round-39/calib/basename-couples-policy.md:27-48`): `direct`, `fallback`, `ambiguous`, `unresolved`. The r42 tool added two **disposition labels** (not resolution classes):

| tool bucket | strict four-class view | rule |
|---|---|---|
| `direct` | `direct` | unchanged |
| `fallback` | `fallback` | unchanged; every row carries `token -> target` |
| `ambiguous` | `ambiguous` | unchanged; zero live, synthetic control only |
| `unresolved` | `unresolved` | unchanged |
| `prospective` | `unresolved` with `disposition: declared-prospective` | the field's own bytes declare the file as a prospective/seed sibling; still not a resolution |
| `glob-fragment` | `excluded` with `disposition: glob-fragment` | policy §5.6: "skip or separately class glob fragments … forbids counting them as unresolved couples findings" |

Invariants (the tool's `--census` output must satisfy all five; the filed JSON records them as booleans):

1. `classified == direct + fallback + ambiguous + unresolved` (strict).
2. `extracted == classified + excluded_total` (strict).
3. `refs == direct + fallback + ambiguous + unresolved + prospective + glob_fragment` (native).
4. `strict.unresolved == native.unresolved + native.prospective`.
5. `strict.excluded_total == native.glob_fragment`.

At the 223-entry tree: `2729 = 2556+166+0+7`; `2730 = 2729+1`; `2730 = 2556+166+0+2+5+1`; `7 = 2+5`; `1 = 1`. All five hold.

**Why this matters.** A four-class-only report that silently drops the 5 prospective rows would understate unresolved by 5; a six-bucket report presented as "four classes" would confuse a disposition with a resolution. The census carries both views and the reconciliation, so neither error is possible. The parent's threshold "zero tokens silently dropped" is proven by invariant 2, not asserted.

---

## 6. Wrapped-field proof (D1) — exact bytes and reading

`corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (sha256 prefix `b4f9b00384bc6840` at measurement):

```
72  - couples: language (this file, core method); myth (divine/true names, taboo
73    naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74    bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75    strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76    environment/anatomy design; prospective sibling files: sound-change.md, tone-
77    prosody.md, sound-symbolism.md, writing-systems.md
```

- Single-line capture (`re.search(r"^- couples:\s*(.*)$", text, re.M)`, the r19 shape at `reports/round-19/audit/entry-audit.py:75`) → **0 tokens**.
- Block capture joined with `\n` or a space → 4 tokens but `prosody.md` (phantom), because `tone-` and `prosody.md` are split by the wrap.
- Block capture + hyphen-retained join (`tools/harness/couples-reference-extractor.py:76-93`) → **4/4**: `sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`, `writing-systems.md`. `tone-prosody.md` is confirmed by the entry's body at `phonetics-phonology.md:279` ("Natural partners: `sound-change.md` … `tone-prosody.md`").
- Classes: `sound-symbolism.md` and `writing-systems.md` `direct`; `sound-change.md` and `tone-prosody.md` `prospective` (field says "prospective sibling files"; neither file exists).
- Phantoms that must never appear: `prosody.md`, `toneprosody.md`.
- Corpus-wide, exactly **one** entry's single-line and block captures differ: `phonetics-phonology.md`. A naive `FIELD_RE` that does not stop at all header fields over-captures (r42 measured 3,396 tokens vs 2,611; `reports/round-42/calib/Ca01-gap-fill.md:190-203`). The census's `per_entry` `couples_span` and `wrapped` flags expose the field span so a verifier can re-read the bytes.

The claim's threshold "the wrapped field reads 4/4" is met only with the hyphen-retained join. A space-join gives a false 4/4 with a phantom token; the selftest's phantom negative is the control that catches it.

---

## 7. Fallback mappings — expectation table (50 distinct, 166 rows at 223 entries)

Every fallback occurrence must be listed with its explicit `token -> target`. The 50 distinct mappings below are the complete set at the 223-entry tree, with occurrence counts (sum = 166). The integrator's live `fallbacks` array must reproduce this set (subject only to the C landing, whose tokens are direct). A missing or extra distinct mapping is a finding.

| token | target | occurrences |
|---|---|---:|
| `adornment-body-codes.md` | `corpus/knowledge/culture-material/adornment-body-codes.md` | 2 |
| `animal-symbolism.md` | `corpus/knowledge/myth-symbol/animal-symbolism.md` | 1 |
| `architecture-settlement-lexicon.md` | `corpus/knowledge/culture-material/architecture-settlement-lexicon.md` | 4 |
| `calendar-festival-systems.md` | `corpus/knowledge/culture-material/calendar-festival-systems.md` | 2 |
| `calibration-registry.md` | `corpus/knowledge/verification/calibration-registry.md` | 2 |
| `color-symbolism.md` | `corpus/knowledge/myth-symbol/color-symbolism.md` | 3 |
| `comparative-frameworks.md` | `corpus/knowledge/myth-symbol/comparative-frameworks.md` | 4 |
| `consistency-verification-checklist.md` | `corpus/knowledge/synthesis/consistency-verification-checklist.md` | 1 |
| `cosmology-cosmography.md` | `corpus/knowledge/myth-symbol/cosmology-cosmography.md` | 2 |
| `costume-semiotics.md` | `corpus/knowledge/culture-material/costume-semiotics.md` | 8 |
| `coupling-model.md` | `corpus/knowledge/synthesis/coupling-model.md` | 1 |
| `creation-myths-taxonomy.md` | `corpus/knowledge/myth-symbol/creation-myths-taxonomy.md` | 1 |
| `dress-through-eras.md` | `corpus/knowledge/culture-material/dress-through-eras.md` | 5 |
| `era-language-staging.md` | `corpus/knowledge/synthesis/era-language-staging.md` | 1 |
| `era-periodization-models.md` | `corpus/knowledge/culture-material/era-periodization-models.md` | 1 |
| `garment-lexicon-crosslinguistic.md` | `corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md` | 3 |
| `historical-linguistics.md` | `corpus/knowledge/linguistics/historical-linguistics.md` | 9 |
| `inca.md` | `corpus/knowledge/civilizations/inca.md` | 1 |
| `kinship-terminology.md` | `corpus/knowledge/linguistics/kinship-terminology.md` | 1 |
| `language-contact.md` | `corpus/knowledge/linguistics/language-contact.md` | 10 |
| `lexicon-coverage-audit.md` | `corpus/knowledge/verification/lexicon-coverage-audit.md` | 1 |
| `loanword-material-dating.md` | `corpus/knowledge/synthesis/loanword-material-dating.md` | 1 |
| `material-culture-inference-method.md` | `corpus/knowledge/culture-material/material-culture-inference-method.md` | 10 |
| `maya-classic.md` | `corpus/knowledge/civilizations/maya-classic.md` | 1 |
| `mesopotamia-sumer-akkad.md` | `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` | 1 |
| `morphological-typology.md` | `corpus/knowledge/linguistics/morphological-typology.md` | 2 |
| `music-instrument-lexicon.md` | `corpus/knowledge/culture-material/music-instrument-lexicon.md` | 1 |
| `myth-ritual-theories.md` | `corpus/knowledge/myth-symbol/myth-ritual-theories.md` | 1 |
| `myth-to-language-derivation.md` | `corpus/knowledge/synthesis/myth-to-language-derivation.md` | 1 |
| `naming-systems.md` | `corpus/knowledge/linguistics/naming-systems.md` | 14 |
| `number-symbolism.md` | `corpus/knowledge/myth-symbol/number-symbolism.md` | 1 |
| `orality-formulaic-language.md` | `corpus/knowledge/linguistics/orality-formulaic-language.md` | 4 |
| `pantheon-archetypes.md` | `corpus/knowledge/myth-symbol/pantheon-archetypes.md` | 5 |
| `phonetics-phonology.md` | `corpus/knowledge/linguistics/phonetics-phonology.md` | 1 |
| `politeness-taboo-euphemism.md` | `corpus/knowledge/linguistics/politeness-taboo-euphemism.md` | 2 |
| `real-world-inspiration-boundaries.md` | `corpus/knowledge/verification/real-world-inspiration-boundaries.md` | 2 |
| `register-strata-attestation.md` | `corpus/knowledge/linguistics/register-strata-attestation.md` | 1 |
| `religion-language-co-evolution.md` | `corpus/knowledge/synthesis/religion-language-co-evolution.md` | 1 |
| `ritual-garments.md` | `corpus/knowledge/culture-material/ritual-garments.md` | 6 |
| `ritual-liminality.md` | `corpus/knowledge/myth-symbol/ritual-liminality.md` | 2 |
| `semantics-pragmatics.md` | `corpus/knowledge/linguistics/semantics-pragmatics.md` | 3 |
| `sociolinguistics-registers.md` | `corpus/knowledge/linguistics/sociolinguistics-registers.md` | 7 |
| `source-discipline-calibration.md` | `corpus/knowledge/synthesis/source-discipline-calibration.md` | 1 |
| `sumptuary-law-rank-display.md` | `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` | 3 |
| `symbolism-synthesis-method.md` | `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md` | 10 |
| `taboo-euphemism-lifecycle.md` | `corpus/knowledge/synthesis/taboo-euphemism-lifecycle.md` | 1 |
| `textile-technology.md` | `corpus/knowledge/culture-material/textile-technology.md` | 4 |
| `trade-economy-lexicon.md` | `corpus/knowledge/culture-material/trade-economy-lexicon.md` | 3 |
| `warrior-material-culture.md` | `corpus/knowledge/culture-material/warrior-material-culture.md` | 1 |
| `writing-systems.md` | `corpus/knowledge/linguistics/writing-systems.md` | 13 |

Alignment leg (policy §4): `labeled_fallback_rows = 27`, all aligned (`27/27`); `unlabeled_fallback_rows = 139` (fields with no domain-label grouping, `group: null`, `aligned: null`); `misaligned = 0`. The 15 sacred-kingship fallbacks are inside the 27 labeled rows. A live `ambiguous` would be listed with all candidate targets; there are zero.

---

## 8. Every non-direct/non-fallback token, dispositioned (8 rows at 223 entries)

This is the disposition leg. At the 223-entry tree there are 8 extracted rows outside `direct`/`fallback`: 2 strict `unresolved`, 5 `prospective` re-labelled to unresolved with a named reason, 1 `glob-fragment` excluded. All eight are named; none is dropped.

| # | entry | line | token | native | strict | disposition | reason (from the field's own bytes) | owner / evidence |
|---|---|---|---:|---|---|---|---|---|
| 1 | `corpus/knowledge/verification/label-channel-routing-verification.md` | 14 | `../linguistics/phonology-sanity.md` | unresolved | unresolved | wrong-path-phantom | path `corpus/knowledge/linguistics/phonology-sanity.md` is absent; the same field already cites `verification/phonology-sanity-gate.md` | entry editors; r19 X26-1 (`reports/round-19/audit/x26-spotcheck-entries.md` §3); `find corpus -name phonology-sanity.md` → 0 |
| 2 | `corpus/knowledge/synthesis/typed-label-routing-workflow.md` | 16 | `../linguistics/phonology-sanity.md` | unresolved | unresolved | wrong-path-phantom | same absent path; second live carrier (r42 Ca01 gap-fill identified it; r39 policy Part 2 named only carrier 1) | entry editors; `reports/round-42/calib/Ca01-gap-fill.md:146-160` |
| 3 | `corpus/knowledge/linguistics/language-contact.md` | 7 | `phonology-basics.md` | prospective | unresolved | declared-prospective | field says "sibling knowledge files to seed"; file absent | coverage owner; `reports/round-42/op/O10-gap-fill.md` §4 row 1 |
| 4 | `corpus/knowledge/linguistics/language-contact.md` | 7 | `naming-and-onomastics.md` | prospective | unresolved | declared-prospective | same "to seed" declaration; absent | coverage owner; same |
| 5 | `corpus/knowledge/linguistics/language-contact.md` | 7 | `honorifics-and-register.md` | prospective | unresolved | declared-prospective | same "to seed" declaration; absent | coverage owner; same |
| 6 | `corpus/knowledge/linguistics/phonetics-phonology.md` | 76 | `sound-change.md` | prospective | unresolved | declared-prospective | field says "prospective sibling files"; absent | coverage owner; `phonetics-phonology.md:279` names it a natural partner |
| 7 | `corpus/knowledge/linguistics/phonetics-phonology.md` | 76-77 | `tone-prosody.md` | prospective | unresolved | declared-prospective | same declaration; absent; token recovered across the hyphen wrap | coverage owner; `phonetics-phonology.md:279` |
| 8 | `corpus/knowledge/verification/gate-frozen-run-standard.md` | 15 | `-gate.md` | glob-fragment | excluded | glob-fragment | extractor artifact from `corpus/knowledge/verification/*-gate.md`; policy §5.6 forbids counting it as unresolved | policy; `reports/round-39/calib/basename-couples-policy.md:97-102` |

Controls that keep this table honest:

- Rows 1-2 are a **real corpus defect**, not a phantom: the target path is wrong and the correct gate is in the same field. r42 O10 drafted a corpus fix but did not apply it; the census does not decide the fix, it records the row. If a later round applies the fix, the row disappears and the census delta is a finding.
- Rows 3-7 are **declared-prospective**, not dangling links. Re-labelling them `unresolved` in the strict view is the policy's four-class requirement; the disposition names why they are not blockers. A report that drops them is wrong; a report that calls them "dangling" overstates.
- Row 8 is **excluded**, not unresolved. It is listed so "zero tokens dropped" is provable.

---

## 9. Ambiguous branch

- Live instances: **0** at the 223-entry tree. `IDX` has 223 distinct basenames over 223 files; no cross-partition duplicate (`reports/round-42/calib/Ca01-gap-fill.md:180-184`; re-measured 2026-10-19).
- **The branch is not currently controlled.** The r42 selftest (`tools/harness/couples-reference-extractor.py:242-296`) exercises the wrapped positive, the phantom negative, the over-capture trap and the glob class, but **no synthetic ambiguous pair**. The r43 claim requires "an ambiguous/phantom negative" (`reports/round-43/claims.json:28,34`), so the landed tool must add an ambiguous fixture (two same-basename files → `ambiguous`). If it does not, the filed census records `"status": "unexercised-live-and-uncontrolled"` and the claim's threshold is **not met**; do not silently claim the branch is tested.
- Policy §5.5 re-adjudication trigger: a duplicate basename or a new top-level directory changes the fallback's uniqueness assumption. The census's `population.manifest_sha256` and `ambiguous_branch` fields are the tripwire.

---

## 10. Post-landing prediction — `PREDICTED`, not filed

If the r42 C01 spare lands unmodified as the 224th entry, its fenced `- couples:` (single line, `reports/round-42/cov/C01-mineral-spare.md:22`) carries **30 tokens, all `direct`** at a myth-symbol entry directory (measured by extracting the fenced block and resolving against `corpus/knowledge/myth-symbol/`). Predicted closed-tree totals:

| view | refs | direct | fallback | ambiguous | unresolved | prospective | glob |
|---|---:|---:|---:|---:|---:|---:|---:|
| policy-strict | 2759 classified + 1 excluded = 2760 | 2586 | 166 | 0 | 7 | — | — |
| tool-native | 2760 | 2586 | 166 | 0 | 2 | 5 | 1 |

Delta: `+1 entry`, `+30 refs`, `+30 direct`, all other buckets unchanged. The prediction is **contingent** on:

1. The C landing path and bytes being the spare's fenced block unmodified (the spare's own header sanctions path/front-matter adjustments; any change to the `- couples:` line invalidates the +30).
2. The spare's 30 tokens remaining `direct`; because they are fully qualified `corpus/knowledge/...` paths, they resolve at the lane root independent of the entry filename.
3. No other corpus entry moving in the same integration.

**Hazard:** the live partition already has `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (the lithic register). Landing the spare as a second lithic entry is a duplicate-topic landing; the C seats must resolve the collision. If the C claim instead lands a different entry or no entry, the census records the actual count — 223 is a legitimate closed-tree value, and the claim-C shortfall is a separate finding, not a reason to fake 224. The census must never be adjusted to match a claim's expected count.

---

## 11. Fill checklist and validation commands

Run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

1. **Pin the tree.** `git rev-parse --short HEAD` → `run_head`; `git status --porcelain corpus/` → record any landing delta. If corpus bytes are dirty and not the C landing, stop and report.
2. **Pin the tool.** `sha256sum <tool>` → `tool.sha256`; `python3 -B <tool> --selftest; echo EXIT=$?` → record the full control list and exit 0. No selftest, no census.
3. **Pin the population.** Partition counts: `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do echo "$p $(ls corpus/knowledge/$p/*.md | wc -l)"; done`; `find corpus/knowledge -name '*.md' | wc -l`. Manifest digest (reproduces `444ff801…` at 223):
   ```
   python3 -B - <<'PY'
   import glob, hashlib
   rows = []
   for p in sorted(glob.glob("corpus/knowledge/*/*.md")):
       rows.append(f"{p}:{hashlib.sha256(open(p, 'rb').read()).hexdigest()}")
   print(hashlib.sha256("\n".join(rows).encode()).hexdigest())
   PY
   ```
   The eleven-entry comparison digest (`9d97bde0…`) uses the same recipe over the eleven paths in §4, in the listed order after `sorted()`.
4. **Run the census.** `python3 -B <tool> --census --json > reports/round-43/calib/basename-couples-census.json` (or capture text). Record the full stdout in the Markdown `raw_stdout` block.
5. **Check the five identities** from §5. If any is false, do not file; report the failing leg.
6. **Re-run the eleven-entry leg** (§4) and confirm `334 = 319 + 15 + 0 + 0` with the same manifest digest. If it differs, record the drift; the 334 comparison is byte-pinned, not assumed.
7. **Confirm the wrapped-field proof**: 4/4 tokens, `tone-prosody.md` present, `prosody.md` and `toneprosody.md` absent, single-line 0. This is the D1 control.
8. **Confirm the disposition set** against §8: 8 rows at the 223 tree; after the C landing, still 8 unless the new entry adds a non-direct token (it is predicted all-direct). Every row has an owner and a citation.
9. **Compute the JSON digest** after writing (`sha256sum basename-couples-census.json`) and put it in the Markdown header. Never put a file's own digest inside itself.
10. **Record drift.** Compare the closed-tree numbers with §0.2/§10. Any difference is a finding with a named cause (landing, corpus edit, tool change); never overwrite a predicted number silently.

Quick arithmetic checker for the filed JSON:

```
python3 -B - <<'PY'
import json
d = json.load(open("reports/round-43/calib/basename-couples-census.json"))
s, n = d["totals_policy_strict"], d["totals_tool_native"]
assert s["classified"] == s["direct"] + s["fallback"] + s["ambiguous"] + s["unresolved"]
assert s["extracted"] == s["classified"] + s["excluded_total"]
assert n["refs"] == n["direct"] + n["fallback"] + n["ambiguous"] + n["unresolved"] + n["prospective"] + n["glob_fragment"]
assert s["unresolved"] == n["unresolved"] + n["prospective"]
assert s["excluded_total"] == n["glob_fragment"]
assert s["extracted"] == n["refs"]
assert sum(e["refs"] for e in d["per_entry"]) == n["refs"]
assert len(d["fallbacks"]) == n["fallback"]
print("CENSUS ARITHMETIC PASS")
PY
```

---

## 12. Honesty notes, `to-verify`, and what this seat did not do

- **The claim's `before` is stale.** §0.1 shows the r42 durable instrument at HEAD and r42's O validation green. This seat did not build a tool; it specifies the census and records the live tool as the reference implementation. The parent should judge the axis move on the census/disposition artifacts, not on a from-scratch tool claim.
- **The C landing is unresolved at this seat's write time.** `mineral-stone-symbolism.md` exists; the spare duplicates its topic. The census's closed-tree row is the authority. `224` is a claim target, not a measured fact.
- **The `prospective` label is r42's, not the r39 policy's.** The policy's four classes cannot hold declared-prospective seeds without either dropping them or calling them dangling. This artifact chooses "strict unresolved + named disposition" and proves the reconciliation. If the parent prefers a fifth class in the policy, that is a successor-policy decision, not a census edit; the filed policy bytes stay as filed.
- **The `ambiguous` branch has no live instance.** The synthetic control is the only proof; the census says so.
- **The 50-mapping table is a snapshot at 223 entries.** It is an expectation for the live run, not a substitute for the tool's `fallbacks` array. If the live run differs, the difference is a finding.
- **Not done by this seat:** no tool execution beyond `--selftest`/`--census`/per-entry reads of the existing r42 tool (read-only); no `run-validation.py`; no corpus staging; no filed-byte edit; no git/network/install; no claim-C landing decision; no claim-Ca disposition decision.
- **`to-verify`:** (a) the exact tool the integrator uses and its `--json` surface; (b) the closed-tree entry count and manifest digest; (c) the C landing's effect on the 30-token prediction; (d) whether the r43 runner expects a specific census filename (none exists at write time — `reports/round-43/run-validation.py` is absent).

---

## Citations

- Claim/seat: `reports/round-43/claims.json:24-36`; `reports/round-43/targets.json` seat `O10`.
- Existing instrument: `tools/harness/couples-reference-extractor.py:1-21` (docstring), `:50-73` (`couples_block`), `:76-93` (`join_parts`), `:134-150` (`classify`), `:153-183` (`resolve_entry`), `:186-211` (`census`), `:242-296` (`selftest`), `:298-330` (`main`); sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`.
- r42 landing/verification: `git log --oneline -1 -- tools/harness/couples-reference-extractor.py` → `7ceff59`; `reports/round-42/validation.json` claim O `"passed": true`; `reports/round-42/op/couples-census-corrected.json` (v2, 220 entries, 2611 = 2437 + 166 + 0 + 8).
- Policy: `reports/round-39/calib/basename-couples-policy.md:14-48` (§1-§2), `:50-68` (§3-§4), `:71-102` (§5, incl. §5.6 glob at `:97-102`), `:104-226` (§6 recipe); `reports/round-42/calib/basename-couples-policy-full.md` (full successor).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, intent at `:279`; sha256 prefix `b4f9b00384bc6840`.
- r37 baseline: `reports/round-37/adj/A02-entries-bleed.md:7`; `reports/round-37/adj/A06-verify.md:29`; `reports/round-37/adj/A08-verify.md:17`; `reports/round-37/adj/A12-gap-fill.md:9-38`; `reports/round-37/scout/K04-entries-scout.md:25`.
- r39 baseline: `reports/round-39/calib/basename-couples-policy.md` §6 Part 2 (212 entries, `2504 = 2335 + 163 + 0 + 6`); `reports/round-39/calib/Ca04-verify.md:78-93,114`.
- r42 recount and hazards: `reports/round-42/calib/Ca01-gap-fill.md:56-79` (recount table), `:120-203` (wrapped-field mechanism, over-capture trap, phantom carriers); `reports/round-42/op/O10-gap-fill.md` §1-§6 (unwrap rule D, dispositions).
- Spare: `reports/round-42/cov/C01-mineral-spare.md:1` (integrator ruling), `:22` (couples field, 30 tokens); live collision `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`.
- Command outputs (2026-10-19, HEAD `7ceff59`, read-only):
  - `python3 -B tools/harness/couples-reference-extractor.py --selftest` → 8/8 PASS, exit 0.
  - `python3 -B tools/harness/couples-reference-extractor.py --census` → `entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1`; wrapped fields 1; unresolved distinct 1 (`../linguistics/phonology-sanity.md` x2); misaligned none.
  - Block + hyphen-join eleven-entry probe → `334 -> direct=319 fallback=15 ambiguous=0 unresolved=0`; manifest `9d97bde0…`.
  - 223-entry policy-strict probe → `2730 = 2556 + 166 + 0 + 7 + 1`; manifest `444ff801…`.
  - `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 26; `find corpus/knowledge -name '*.md' | wc -l` → 223; partition vector `25/26/25/29/24/94`.
