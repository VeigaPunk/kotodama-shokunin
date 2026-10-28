# README integration plan — claim C entry `naming-systems.amend-2026-10-23.md`

Recon for round 77 claim C. Base: `211f9526800906e0c585d878d265c37e5e090c15` (README: 836 lines).
Measured contract: `reports/round-76/accept-c.py` INDEX leg (frozen leg text at lines 4301–4312,
implementation `leg_index` at 4393–4621). Round 77's counter is unfrozen; this plan assumes the
r76 INDEX semantics carry over and flags the one place r77 may harden.

## The full permitted README diff (r76 INDEX exemption set)

The leg permits ONLY: (a) one index row per admitted entry inside its partition section,
(b) partition-heading count parenthetical replacements, (c) one appended footer block at EOF
(`Total knowledge entries: N.` + `Counts checked …` paragraph). No new `## ` section, no new
`revision:` block, no prose paragraph — any line added outside the exemption set fails
(`accept-c.py:4606`).

1. **Line 344**: `## linguistics/ (32)` → `## linguistics/ (33)`
   (leg: "every partition heading equals that partition's live .md count"; enforcement at
   accept-c.py:4466–4473 — graded against the live tree, all six headings).
2. **Insert row after line 355** (`morphological-typology.md`), before line 356
   (`naming-systems.md`) — README filename order, byte-sort `.` < `.md` precedes the base file
   (precedent: lines 451–452 `worldbuilding-setting-practice.amend-…` before `…practice.md`;
   tree order `ls-tree corpus/knowledge/linguistics/`: `naming-systems.md` is slot 14, the amend
   sorts into it).
3. **Append at EOF** (after line 836) the new footer block below.

## Exact index row line (em dash U+2014, single line, no trailing space)

```
- `naming-systems.amend-2026-10-23.md` — two things the naming entry could not say before. First, that a Chinese naming system is a *late cultural acquisition* — 名 precedes 姓, and their combination is a habit formed under contact, not a natural given. Second, that Chinese given names draw on a finite, listable semantic inventory, which the onomastics literature classifies into subcategories and counts.
```

The body is the staged entry's `- topic:` folded verbatim (staged file folds it across 5 lines,
joined with single spaces). SOURCE: staged file lines 10–14 at
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`.
**INTEGRATION PREREQUISITE**: the landed `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`
must carry `- topic:` as ONE physical line equal to the row body — `accept-c.py:4375-4386`
(`_entry_topic`) reads only the `topic:` line itself, never continuation lines, so a folded
`- topic:` in the landed file makes verbatim match impossible. Precedent: landed
`conlang-scholarship.amend-2026-10-23.md` carries its topic as one line (base tree).

## Exact appended footer block (after base line 836; leading blank line shown)

```

Total knowledge entries: 254.

Counts checked 2026-10-27 from the repo root: `find corpus/knowledge -type f -name '*.md' | wc -l` (total 254 files; directory totals 33/32/41/29/24/95).
```

The vector order is README section order (`_readme_sections`, accept-c.py:4342–4346):
`linguistics/myth-symbol/culture-material/synthesis/verification/civilizations`.

## Per-partition counts verified at base (ls-tree | grep -c '\.md$')

| partition | base .md | row count in section | post-landing |
|---|---|---|---|
| linguistics | 32 | 30 rows (+2 in `## Round 73 additions`) | 33 |
| myth-symbol | 32 | — | 32 |
| culture-material | 41 | — | 41 |
| synthesis | 29 | — | 29 |
| verification | 24 | — | 24 |
| civilizations | 95 | — | 95 |
| TOTAL | 253 | — | 254 |

Raw command: `git -C <lane> ls-tree --name-only 211f95… corpus/knowledge/<d>/ | grep -c '\.md$'`
→ civilizations 95, culture-material 41, linguistics 32, myth-symbol 32, synthesis 29,
verification 24; recursive total 253.

## OTHER lines a +1 linguistics file stales (forecast)

1. **L344 `## linguistics/ (32)`** — stale unless repaired to (33); r76 INDEX grades every
   heading against live counts, so this is a REQUIRED in-place edit (only the parenthetical).
2. **L755 `Total knowledge entries: 243.`** — superseded (already 10 stale; preserved as record).
3. **L757–L768 `Counts checked 2026-10-25 … (total 243 files; …)` block** — superseded.
   NOTE: `reports/round-28/readme/sweep.py` parses THIS first footer (README L824 says so) —
   a third 2026-10-27 block changes nothing for it, but its totals legs were already red.
4. **L798 `Total knowledge entries: 247.`** — superseded.
5. **L800 `Counts checked … (total 247 …)`** — superseded.
6. **L819 `Total knowledge entries: 249.`** — superseded.
7. **L821 `Counts checked … (total 249 …)`** — superseded.
8. **L830 `Total knowledge entries: 252.`** — superseded.
9. **L832 `Counts checked 2026-10-27 … (total 252 …)`** — superseded.
10. **L834 `Total knowledge entries: 253.`** — superseded (was live; new block replaces it as
    the last footer).
11. **L836 `Counts checked 2026-10-27 … (total 253 …)`** — superseded as the last footer.
12. **L791 `## Round 73 additions` paragraph** — its "The linguistics partition holds 32 files
    at this landing" clause stales; also its claim that heading edits are append-only-forbidden
    is superseded practice under the r76 INDEX contract (headings MUST match live counts).
    The block itself stays byte-identical.
13. **`## Round 73 additions` rows (L793–794)** — not stale, but they sit OUTSIDE `## linguistics/`;
    a future reconcile may merge them — NOT this landing (out of exemption set).

NOT stale / do not touch: every `revision:` block (historical prose), `## Known gaps`
(L609–753, no live counts), L822–828's "this block is the live reading" claim (already dated
prose in a preserved block), all five other partition headings (still equal to live counts).

## Risk flags for the L1

- **Row placement is mandatory, not optional**: a `## Round 77 additions` trailing section like
  round 73's fails BOTH "row inside partition section" (accept-c.py:4459) and
  "line added outside the exemption set" (:4606). Round 74 put its rows inside the partition
  section — follow that precedent.
- **No `revision:` block this landing**: appendable lines are rows/heading/footer only.
- If the r77 counter keeps `_entry_topic` first-line-only AND the entry lands with a folded
  topic, INDEX fails regardless of the row — fold it to one line at landing.
