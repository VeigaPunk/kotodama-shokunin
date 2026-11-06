# EARLY — CriticO99 confirmed defects in v11 (act before landing)

## Resolution (measured on the landed bytes `717341dc…`)

Both defects below, and the two residual over-refusals found on the intermediate bytes, are
repaired in the final v11
(`717341dcff329a8c8aea9e6e807a16b70bc24818edfc31681780a24f68ee76f2`, `V11-READY` matches):
A-DASH-MC / A-DASH-VIS refuse `HEADING-COMBINING`; OK-VIETNFD / OK-IPA / OK-JAPAN-NFD /
OK-CYR-NFD / OK-FR-PETITION are CLEAN. My driver on the final bytes: assigned benign 28/28
CLEAN, overrefusal 0, probe 0; attacks survivors=32 refused=14 unnamed=0 traceback=0. The six
new survivors versus v10 are all measured anchor-neutral (mark vs mark-deleted twins both
rc 0); no load-bearing reopened forgery remains.

Correction to section 1 below: A-SUFFIX-MC / A-SUFFIX-VIS are **not** forgeries — the same
headings with the mark deleted already pass on v10, so the mark is not load-bearing.
Correction to section 2's proposed fix: treating U+0300–U+036F as neutral on any letter base
would accept `## I<U+0301>. address` x5 (rc 0) while the mark-free twin fails span 1 < 3
(ExecGraderV11's ROMANMARK measurement; I reproduced the twin on the final bytes). The landed
fix is the stronger invariant: a mark must not change `(head_anchors, head_span_anchors)`.
The whole-token phrase match (my second correction) was adopted and OK-FR-PETITION is CLEAN.

v11 under test: `tools/check-advance-evidence.py` sha256
`a56965b5db10a8a6cde7121752ea5a2056179c6efab9e9f40e520ce70e5bf027` (first V11-READY; superseded).
v10 baseline: `d35b13c9a2f2c7abcbf6d808837a254fb5242faf66c0b99f942640a232716af7`
(`.ufo/waves/round-99/w1/stage/ExecGraderV11/v10-base.py`). Driver:
`.ufo/waves/round-99/w1/stage/CriticO99/attacks_critic99.py`, fixtures built with battery99's
own `standard()/grade()` (battery99 sha `87f426aa…c7a26d`).

## 1. REOPENED FORGERY (load-bearing): a non-Latin mark glued to a separator dash

Byte recipe (five h2 heads in the standard battery99 mini-lane; `—` is U+2014, `<U+093E>` is
Devanagari vowel sign AA, category Mc):

```
## 1. address —<U+093E>
## 2. petition —<U+093E>
## 3. efficacy —<U+093E>
## 4. table —<U+093E>
## 5. Notes —<U+093E>
```

Measured (`probe_nomark.py`, rc 0 for the driver):

| fixture | v10 | v11 |
|---|---|---|
| `## 1. address —` (no mark) | rc 1, `TOPIC` span 1 < 3 | rc 1, `TOPIC` span 1 < 3 |
| `## 1. address —<U+093E>` | rc 1, `HEADING-COMBINING` (span 5) | **rc 0, PASS legs=9/9** |

The mark is the only difference and it flips the outcome: without it the dash is a list mark
(`_NUM2` `[\u2010-\u2015-]+`) and the heading has one content token; with it the token `—ा` is
no longer a list mark and counts as content, so a phrase-only heading reaches the span floor.
`_heading_forged_mark()` accepts it because the nearest base `—` (U+2014) is non-ASCII and not a
digit. Same result with visarga U+0903. The Latin twin `—<U+0301>` stays refused
(`COMBINING ACUTE ACCENT` matches the `name.startswith('COMBINING ')` arm), so the hole is
specific to non-Latin marks on a non-ASCII, non-digit base.

Variant with the same root cause: `## 1. address<U+093E> Notes` x5 — v10 rc 1
`HEADING-COMBINING`, v11 rc 0 PASS 9/9 (the mark is a suffix on the phrase word, so `norm()`
still contains `address` as a substring and the second token supplies the span).

Smallest safe correction (route to round 100, not implemented here): in
`_heading_forged_mark()` also refuse a mark whose nearest base is not a letter
(`not unicodedata.category(base).startswith('L')`), and refuse a non-Latin mark on an ASCII
letter base unless the token's script matches the mark's script.

## 2. OVER-REFUSAL: valid Latin-script NFD and IPA headings are still refused

| id | heading added to the standard body | v10 | v11 |
|---|---|---|---|
| OK-VIETNFD | `## 4. Efficacy — tie<U+0302><U+0301>ng Vie<U+0302><U+0323>t` (Vietnamese NFD) | rc 1 `HEADING-COMBINING` | **rc 1 `HEADING-COMBINING` U+0302** |
| OK-IPA | `## 4. Efficacy — n<U+0325> a<U+0303>` (IPA) | rc 1 `HEADING-COMBINING` | **rc 1 `HEADING-COMBINING` U+0325** |

v11 diagnostic on both: `h2 heading carries a combining mark U+0302 (HEADING-COMBINING);
phrase anchors 4/4 spanning 4 heading/table surfaces` — the heading content anchors fine; only
the mark rule refuses. Cause: every Latin combining mark is named `COMBINING …`, so the
`name.startswith('COMBINING ')` arm refuses all NFD Latin text and all IPA diacritics. The same
arm refuses decomposed Japanese (`か<U+3099>`, name `COMBINING KATAKANA-HIRAGANA VOICED SOUND
MARK`). This is the F4 harm class (valid orthography refused) only partly repaired.

Smallest safe correction: decide by base/mark script and by whether the mark degrades an ASCII
anchor token, not by the Unicode name prefix; add NFD Vietnamese, IPA and decomposed Japanese
as selftest benign twins.

## 3. Not a regression (recorded so it is not misread)

`## 1<U+200D>. address` x5 (ZWJ U+200D, Cf, no category-M character) is refused by v10's
`HEADING-NUMBER` loop but passes v11; it has no mark, so `_heading_forged_mark()` never runs.
`## 1<U+0930>. address` x5 (digit + Devanagari letter, no mark) passes both v10 and v11
(pre-existing span weakness, same family as the open H-* classes).

All other measured v10 refusals stay refused on v11 (see `attacks.md`).
