# Oath entry: three weak-line repairs (round 99, wave 1, seat ScribeOath99)

- Entry (only file edited): `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` (round-96 entry, sources S975–S984).
- Routed by: round-98 closure §6 item 5; verdicts and repair list from `.ufo/waves/round-98/w1/stage/ReviewerOath98/support.md` (weak rows L49/S978, L51/S980, L53/S981; Repairs items 2, 3, 4, 10).
- Captures: `reports/round-96/evidence/` only. No new source opened, no network request made this round (no curl, so no UNREACHABLE record).
- Capture integrity re-checked against `reports/round-96/evidence/manifest.json`: 3/3 sha256 match (S978 `42b907c3…`, S980 `4e7f3189…`, S981 `08431da0…`), rc 0.

## Repairs (before → after, verbatim)

### L49 (S978) — hedge marked as conjecture, truncated quote fixed

- before: `The oath form in this material is defined by what it takes with it — the curse is part of the binding — and the source states that "curse-enhanced oaths or vows lie behind the notion of the geis" (S978).`
- after: `The oath form in this material is defined by what it takes with it — the curse is part of the binding — and the source reports Mees's conjecture that "curse-enhanced oaths or vows lie behind the notion of" the geis-supported fír of early Irish tradition; his hedge is explicit: "It may well be, then, that" (S978).`
- What the defect was: the entry reported Mees's speculation flat ("the source states that") and ended the quotation mid-compound at `the geis`, while the capture continues `geissupported fír`.
- What the repair does: (a) the reporting verb is now `reports Mees's conjecture`, and the source's own hedge is quoted verbatim; (b) the quotation now stops at a word boundary (`…lie behind the notion of`) and the compound continues outside quotation marks. The reviewer's option "stop at '…lie behind the notion of'" was taken because the capture's rendering of the compound (`geissupported`) is a line-break artifact: the stored raw of the same capture, laid out two-column, breaks the word as `the geis-` / `supported fír` (`pdftotext -layout reports/round-96/evidence/S978.raw.pdf geis.txt`, rc 0; `sed -n '186,196p' geis.txt` shows `vows lie behind the notion of the geis-` then `supported fír of early Irish tradition`). The hyphenated spelling `geis-supported` is therefore prose, not quotation; the capture's literal string `geissupported fír` occurs once and is recorded below.

### L51 (S980) — the dangling "The same account" replaced by a proper introduction

- before: `The same account takes the whole family as a single class of performative utterance, and it enumerates the class as "a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra" (S980).`
- after: `Frangulov's 2023 Oxford MPhil thesis on ritual speech and performativity takes the whole family as a single class of performative utterance, and it enumerates the class as "a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra" (S980).`
- What the defect was: "The same account" pointed at §2's previous source (S978, the Mees review), a different account; the Oxford thesis was introduced only later, at §3's L67.
- What the repair does: names the source at first use in §2 — author, year, degree, institution and topic, all from the thesis title page (`Ritual speech, Performativity, and Modality Alexander Maxim Frangulov Balliol College University of Oxford A thesis submitted for the degree of Master of Philosophy Trinity 2023`). §3's L67 ("A semantic and pragmatic account of the same frame") is now a resolved anaphor; it was not edited.

### L53 (S981) — the sectional division recast as the commentator's device

- before: `The norito material treats the formula as a text with an internal sectional structure that a practitioner has to know, and the source describes one such division as "divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections" (S981).`
- after: `The norito material shows the formula as a text with an internal sectional structure, though the division the source records is a commentator's: Ōkuni Takamasa's work, following Mabuchi and Norinaga, "divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections, and provides commentary for each" (S981).`
- What the defect was: the entry attributed the ten-section division to the text and added "a practitioner has to know", which the capture never says (`practitioner` → 0 hits in S981.txt, `grep -c 'practitioner'` on the capture; entry now 0 hits too).
- What the repair does: the division is attributed to Ōkuni Takamasa's commentary work, which the capture names as its agent and places after Mabuchi and Norinaga; the quotation is extended through `and provides commentary for each`, which is the clause that makes the division a commentary device rather than a property of the recitation. The unsupported obligation clause is deleted, not hedged.

### Item 10 (S980 sentence with no "sanction" in the capture) — already applied in round 98, verified

- The routed sentence (`The sanction clause in the same account is read as part of the performative content rather than as an appended condition, so the class it belongs to is the one it "a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra" (S980).`) is **not present** in the current file. It was deleted by the round-98 commit, not by this seat:
  - `git show 7ff35e6c -- corpus/knowledge/linguistics/oath-blessing-curse-formulae.md | grep -c '^-.*S980'` → `1` (the removed line), rc 0.
  - `grep -c 'performative content' corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` → `0`, rc 1 (no residual).
- No further edit was needed; the two surviving S980 sentences (L51, L67) make no sanction claim, and `sanction` occurs 0 times in S980.txt. The routed repair set (items 1–11) is therefore closed: 7 applied in round 98 (1, 5, 6, 7, 8, 9, 11), 3 applied here (2, 3, 4), 1 already applied (10).

## Support rows for the repaired sentences

Counts are `str.count` on the capture with whitespace collapsed (`re.sub(r"\s+", " ", text)`), decoded UTF-8. Every decisive span is ≤ 25 words and occurs exactly once.

| entry line | S-id | capture file | decisive capture span | words | count | rc |
|---|---|---|---|---|---|---|
| 49 | S978 | `reports/round-96/evidence/S978.txt` | `curse-enhanced oaths or vows lie behind the notion of` | 9 | 1 | 0 |
| 49 | S978 | `reports/round-96/evidence/S978.txt` | `It may well be, then, that` | 6 | 1 | 0 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra` | 10 | 1 | 0 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `A thesis submitted for the degree of Master of Philosophy Trinity 2023` | 12 | 1 | 0 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `Balliol College University of Oxford` | 5 | 1 | 0 |
| 51 | S980 | `reports/round-96/evidence/S980.txt` | `Frangulov` | 1 | 1 | 0 |
| 53 | S981 | `reports/round-96/evidence/S981.txt` | `divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections, and provides commentary for each` | 20 | 1 | 0 |
| 53 | S981 | `reports/round-96/evidence/S981.txt` | `Following the example of Kamo no Mabuchi` | 7 | 1 | 0 |

Corroborating spans, count stated because it is not 1:

| S-id | span | count | use |
|---|---|---|---|
| S978 | `geissupported fír` | 1 | the capture's rendering of the compound the entry spells `geis-supported fír` (hyphen lost at a line break) |
| S980 | `Ritual speech, Performativity, and Modality` | 2 | thesis title, on the title page and again as the first heading |
| S981 | `Ōkuni Takamasa` | 4 | author of the commentary work (two of the four are in the bibliography line) |

Re-runnable count command (the exact loop this seat ran; each line printed its count and `rc=0`):

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
for spec in \
 "S978|curse-enhanced oaths or vows lie behind the notion of" \
 "S978|It may well be, then, that" \
 "S978|geissupported fír" \
 "S980|a ritual, spell, curse, charm, incantation, blessing, hymn, or mantra" \
 "S980|A thesis submitted for the degree of Master of Philosophy Trinity 2023" \
 "S980|Balliol College University of Oxford" \
 "S980|Frangulov" \
 "S981|divides the Great Purification Norito found in Fascicle 8 of the Engishiki into 10 sections, and provides commentary for each" \
 "S981|Following the example of Kamo no Mabuchi"; do
  sid=${spec%%|*}; span=${spec#*|}
  python3 -B -c 'import re,sys; sid,span=sys.argv[1],sys.argv[2]; t=re.sub(r"\s+"," ",open("reports/round-96/evidence/"+sid+".txt",encoding="utf-8").read()); print(sid, t.count(span), len(span.split()), repr(span[:60]))' "$sid" "$span"
  echo "  rc=$?"
done
```

## Verification (all read-only; nothing committed)

- `git diff --stat -- corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` → `1 file changed, 3 insertions(+), 3 deletions(-)`, rc 0. The full diff touches only lines 49, 51 and 53.
- Headings and topic line unchanged: `diff <(grep -E '^#{1,3} |^- topic:' <HEAD copy>) <(grep -E '^#{1,3} |^- topic:' <current>)` → no output, rc 0. All 12 headings (title + §1–§11) and the `- topic:` line are byte-identical to HEAD.
- File length unchanged: `wc -l` → `227` before and after.
- No trailing whitespace introduced: `grep -c ' $' <entry>` → `0`, rc 1.
- `python3 -B tools/check-corpus-index.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin` → `CORPUS-INDEX: OK files=270 rows=270 findings=0`, rc 0.
- `python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` → `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0 (the HEAD copy also scores 0, so no new clause-scoping finding).
- Body citing sentences: `grep -c -E 'S9[0-9]{2}' <entry>` → `31` lines = 10 registry rows + 21 body sentences (22 at base; round 98 deleted one). rc 0.
- Entry sha256 after repair: `37b01cda5deee7c70769c5ee0bdae598d909a484781fbf4db46cf6a0b996dcb5`.

## Limits and residual risks

- `geis-supported fír` is unquoted prose. The capture of record contains `geissupported fír` (count 1); the hyphen is restored from the stored raw PDF's line break, not from the capture text. A verifier who requires every noun phrase to be a capture substring should read the entry's own quotation, which stops at `…notion of` and therefore contains no truncated compound.
- The other routed repairs were checked as present, not re-audited: L47 (Iliad witness frame), L82 (conditional-type framing), L92 (naming then address), L96 (commentary division only), L118 (fear aimed at the swearers), L120 (composition requirements), L124 (treaty borrowing). Re-auditing them is outside this seat's scope.
- No tool was installed or upgraded this round; pacman was not invoked. Nothing was committed, staged or stashed; the entry is left modified in the working tree for the L1.
