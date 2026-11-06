# ScribeOath99 — round 99 wave 1: oath entry, three weak lines repaired

**Seat:** ScribeOath99 (leaf, no subagents). **Milestone:** r99-v1. **Scope:** the three weak lines of `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` routed by the round-98 closure §6 item 5, plus routed repair item 10.

## Behavior

Three sentences rewritten in place; nothing else in the entry touched.

### L49 (S978) — hedge marked, truncated quote fixed

- before: `The oath form in this material is defined by what it takes with it — the curse is part of the binding — and the source states that "curse-enhanced oaths or vows lie behind the notion of the geis" (S978).`
- after: `The oath form in this material is defined by what it takes with it — the curse is part of the binding — and the source reports Mees's conjecture that "curse-enhanced oaths or vows lie behind the notion of" the geis-supported fír of early Irish tradition; his hedge is explicit: "It may well be, then, that" (S978).`
- Defect closed: flat reporting of Mees's speculation, and a quotation cut mid-compound at `the geis` while the capture continues `geissupported fír`. The quotation now ends on a word boundary; the compound continues as prose. Reviewer option "stop at '…lie behind the notion of'" was chosen because the capture's `geissupported` is a line-break artifact: the stored raw of the same capture, laid out two-column, reads `the geis-` / `supported fír` (`pdftotext -layout reports/round-96/evidence/S978.raw.pdf geis.txt`, rc 0; `sed -n '186,196p' geis.txt`).

### L51 (S980) — dangling "The same account" replaced by a proper introduction

- before: `The same account takes the whole family as a single class of performative utterance, and it enumerates the class as "a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra" (S980).`
- after: `Frangulov's 2023 Oxford MPhil thesis on ritual speech and performativity takes the whole family as a single class of performative utterance, and it enumerates the class as "a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra" (S980).`
- Defect closed: "The same account" pointed at §2's previous source (S978, the Mees review), a different account; the thesis was introduced only later at L67. Author, year, degree, institution and topic all come from the thesis title page; §3's L67 now reads as a resolved anaphor and was not edited.

### L53 (S981) — sectional division recast as the commentator's device

- before: `The norito material treats the formula as a text with an internal sectional structure that a practitioner has to know, and the source describes one such division as "divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections" (S981).`
- after: `The norito material shows the formula as a text with an internal sectional structure, though the division the source records is a commentator's: Ōkuni Takamasa's work, following Mabuchi and Norinaga, "divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections, and provides commentary for each" (S981).`
- Defect closed: the division is now attributed to Ōkuni Takamasa's commentary work (the capture's agent for `divides … and provides commentary for each`, placed after Mabuchi and Norinaga); the unsupported obligation clause `that a practitioner has to know` is deleted — `practitioner` has 0 hits in S981.txt and now 0 in the entry.

### Item 10 (S980, no "sanction" in the capture) — already applied in round 98

The routed sentence is absent from the current file and was deleted by the round-98 commit, not by this seat: `git show 7ff35e6c -- corpus/knowledge/linguistics/oath-blessing-curse-formulae.md | grep -c '^-.*S980'` → `1` (the removed line), rc 0; `grep -c 'performative content' <entry>` → `0`, rc 1. No edit needed. Routed repair set now closed: 7 in round 98 (items 1, 5, 6, 7, 8, 9, 11), 3 here (2, 3, 4), 1 already applied (10).

## Support rows (counts on whitespace-collapsed capture, `str.count`, rc 0 each)

| line | S-id | capture | decisive span | words | count |
|---|---|---|---|---|---|
| 49 | S978 | `reports/round-96/evidence/S978.txt` | `curse-enhanced oaths or vows lie behind the notion of` | 9 | 1 |
| 49 | S978 | `reports/round-96/evidence/S978.txt` | `It may well be, then, that` | 6 | 1 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra` | 10 | 1 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `A thesis submitted for the degree of Master of Philosophy Trinity 2023` | 12 | 1 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `Balliol College University of Oxford` | 5 | 1 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `Frangulov` | 1 | 1 |
| 53 | S981 | `reports/round-96/evidence/S981.txt` | `divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections, and provides commentary for each` | 20 | 1 |
| 53 | S981 | `reports/round-96/evidence/S981.txt` | `Following the example of Kamo no Mabuchi` | 7 | 1 |

Corroborating spans (count stated because not 1): S978 `geissupported fír` = 1 (capture rendering of `geis-supported fír`); S980 `Ritual speech, Performativity, and Modality` = 2 (title page + first heading); S981 `Ōkuni Takamasa` = 4. Command and full loop: `stage/ScribeOath99/support.md`; capture sha256 re-verified against `reports/round-96/evidence/manifest.json`, 3/3 match, rc 0.

## Gates run

| gate | command | result | rc |
|---|---|---|---|
| diff scope | `git diff --stat -- corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` | 1 file, 3 insertions(+), 3 deletions(-); only L49/L51/L53 | 0 |
| headings + topic | `diff <(grep -E '^#{1,3} \|^- topic:' HEAD-copy) <(same on current)` | no output; 12 headings and `- topic:` byte-identical | 0 |
| length | `wc -l` | 227 before and after | 0 |
| trailing whitespace | `grep -c ' $' <entry>` | 0 | 1 |
| corpus index | `python3 -B tools/check-corpus-index.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin` | `CORPUS-INDEX: OK files=270 rows=270 findings=0` | 0 |
| cited-line scoping | `python3 -B tools/check-cited-lines.py <entry>` | `CITED-LINES: 0 finding(s) in 1 file(s)` (HEAD copy also 0) | 0 |
| body citations | `grep -c -E 'S9[0-9]{2}' <entry>` | 31 lines = 10 registry + 21 body sentences (22 at base) | 0 |

Entry sha256 after repair: `37b01cda5deee7c70769c5ee0bdae598d909a484781fbf4db46cf6a0b996dcb5`.

## Touched surfaces

- `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` (3 lines, working tree only — not committed, not staged).
- `.ufo/waves/round-99/w1/stage/ScribeOath99/support.md`, `.ufo/waves/round-99/w1/stage/ScribeOath99/DONE`, this Report.
- Scratch `/fast/scratch/hyaku/kotodama-r99/ScribeOath99/` created and deleted before yield.

## Out of scope / not done

- No other sentence of the entry re-audited; the seven round-98 repairs were checked present, not re-judged.
- No source opened, no network request made this round. No tool installed or upgraded (pacman not invoked).
- Nothing committed, staged, stashed or pushed; no jj command run.

## Findings / residual risks

1. `geis-supported fír` is prose, not quotation: the capture of record reads `geissupported fír` (count 1); the hyphen is restored from the stored raw PDF's line break. The entry's own quotation stops at `…notion of`, so no truncated compound remains in quotes.
2. §3's L67 still says "A semantic and pragmatic account of the same frame" — now a resolved anaphor to the Frangulov thesis introduced at L51; left unchanged per scope.
3. The capture `S978.txt` renders a hyphenated compound without its hyphen; a future capture pipeline that preserves soft hyphens would make the prose spelling directly checkable.
