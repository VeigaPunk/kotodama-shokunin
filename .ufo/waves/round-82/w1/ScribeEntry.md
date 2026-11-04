# ScribeEntry — round 82 wave 1, claim D draft (guest-right / hospitality law)

Seat: ScribeEntry (scribe). Round: kotodama R82 (hyaku run 15), wave 1, milestone r82-v1.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `c285b2afb19d4b64320e18df1f55e426bf2d0b0c`. Date: 2026-11-04.
Verdict: **draft delivered, lint-clean, quote-verified.** Nothing installed; the L1 installs.

## 1. Deliverable

Draft path (lane-relative, as assigned):
`corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`

Absolute path:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`

- 29046 bytes — `wc -c <draft>` (target 8000+; 3.6x margin, no filler: every section carries either a row anchor, a design lever, or a labelled craft artefact)
- 128 lines — `wc -l <draft>`
- 22 anchor bullets — `grep -c '^- S9' <draft>` → 22, one row id per line
- id histogram — `grep -o '\bS9[0-9][0-9]\b' <draft> | sort | uniq -c` → `7 S904`, `7 S905`, `6 S906`, `2 S907`
- headings — `grep -n '^## ' <draft>`:
  - `## 1. Partial owners (pointed to one-way)`
  - `## 2. Six design decisions`
  - `## 2.1 Lexicon interface — the five fields the institution forces`
  - `## 3. Attested anchors`
  - `## 4. Craft checklist`
  - `## 5. Worked example (NON-CANON)`
  - `## 6. Lore handoff`
- header fields present: `- topic:`, `- gap filled:`, `- sources:`, `- couples:`, `- source:`, `- verified-at:`, `- recheck:`, `- scope:` (the required seven plus the lane's `- sources:` convention)

Content shape:

- `- gap filled:` names ten partial owners with `path:line` anchors and states what each does **not** own; the census is ScoutGap's (`stage/ScoutGap/gap-census.md`), re-verified by my own sweeps (§3 below).
- `- couples:` names nine `corpus/...md` files, each with an owns/returns clause.
- `## 2` is a six-row decision table (degrees of guest; host's owed package; start/end markers; seal families; breach ladder; guest's obligations) with columns decision / options / attested anchor / worldbuilding consequence; the anchor column points at `## 3` bullet numbers and carries no row id.
- `## 3` gives one bullet per located passage, each with exactly one distinct row id, a 「」 quote <= 25 words, and the locus.
- `## 2.1` is the lexicon section: the five fields (guest, host, bond, violation, parting gift), a worked derivation for the invented language Vethari, a glossed paradigm, the address-direction rule, and the unknown-guest term.
- `## 5` is a NON-CANON worked example (Ashen Quay) instantiating all six decisions plus the stranger-god night.
- `## 6` names `corpus/knowledge/synthesis/worldbible-integration-contract.md` as the handoff contract and states plainly that the entry decides nothing about what is true in any world; canon stays lore's.

## 2. Row identity decision (read this first)

The assignment's planned set had S905 = Bellows Hávámál and S907 = a reject candidate. The delivered draft cites **S904 Butler Odyssey, S905 Tacitus Germania XXI, S906 Ovid Metamorphoses, S907 EB11 "Guest"**, for two independent reasons:

1. ScoutGap's duplicate-document check at base found that the planned Hávámál row is the same Bellows translation already registered as S320 (`corpus/SOURCES.md:349`, full Gutenberg #73533 text opened 2026-10-22). A same-work row adds no source; it would have been a duplicate document.
2. The L1 amendment (IRC, 2026-11-04) fixed the row set to S904 Odyssey / S905 Tacitus / S906 Ovid / S907 EB11 "Guest", and my own fetches confirm its claims: the Tacitus chapter carries the quoted sentence, and the EB11 "Guest" article prose is served by both the live page and the same-page archive capture.

I verified both, rather than taking either on report:

- Tacitus, Wikisource `Germania_(Church_%26_Brodribb)`: HTTP 200, 163266 B, chapter XXI contains 「No nation indulges more profusely in entertainments and hospitality」 verbatim; title block gives the translator pair and 1876.
- EB11 "Guest" live slug: HTTP 200, 60273 B under both the plain and the browser User-Agent, byte-identical; a full HTML parse of `mw-content-text` yields 318 words of visible text and the article sentence `…one who receives hospitality in the house of another, his “host”; hence applied to a parasite.` A raw Parsoid `data-mw` template payload precedes the paragraph; my first, naive tag-strip started inside that payload and truncated the extraction to 985 characters, which I misread as a scaffold. The full parse corrected it: the live slug is openable by ordinary means.
- EB11 "Guest" archive capture `20191023112911`: HTTP 200, 29020 B, 251 words of visible text, prose present including the definition and the *hostis* etymology.
- Namespace positive control `…/1911_Encyclopædia_Britannica/Ordeal`: HTTP 200, 87131 B, 3353 words of visible text — the namespace renders article prose, so the Guest page is normal for its family.

Consequence for the registry seat: the S907 row cites the live slug as served, with the archive capture as the fixed copy; both are on file. The full UA-bound receipts are at `stage/ScribeEntry/fetch-records.md`.

The Hávámál page was fetched before the amendment (HTTP 200, 510701 B, sha256 `a0427c…`) and is recorded as opened-but-not-cited; it is not used for any claim.

## 3. Gates run (command → raw output)

Base and file counts:

```text
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD
c285b2afb19d4b64320e18df1f55e426bf2d0b0c
$ git -C … ls-tree -r --name-only c285b2afb19d4b64320e18df1f55e426bf2d0b0c corpus/knowledge | grep -c '\.md$'
255
```

Gap sweeps (mine, independent of ScoutGap; all at base):

```text
$ git -C … ls-tree -r --name-only <base> corpus/knowledge | grep -icE 'guest|hospital|xenia|hospitium|stranger'
0
$ git -C … grep -inE 'xenia|hospitium|guest-friend|guest-right|guest right|theoxeny|hospitality' <base> -- corpus/knowledge | wc -l
27
$ git -C … grep -ilE 'xenia|hospitium|guest-friend|guest-right|guest right|theoxeny|hospitality' <base> -- corpus/knowledge | wc -l
15
$ git -C … grep -inE 'xenia|hospitium|guest-friend|theoxeny' <base> -- corpus/knowledge | wc -l
0
$ git -C … grep -icE 'ritual' <base> -- corpus/knowledge | wc -l      # positive control on the same file list
220
```

Owner anchors cited in the entry were each read at base and matched their claimed scope: `cuisine-food-lexicon.md:95,138,170`, `ritual-liminality.md:21,110`, `binding-speech-complex.md:62`, `kinship-terminology.md:119`, `furniture-interior-lexicon.md:3`, `bathing-and-body-hygiene.md:3`, `purity-pollution-boundary-systems.md:33`, `creation-myths-taxonomy.md:49`, `myth-folktale-genres.md:55`, `orality-formulaic-language.md:66`, `greece-classical.md:75`, `register-strata-attestation.md:88`.

Clause-scoping lint (the claim-D acceptance check):

```text
$ python3 -B tools/check-cited-lines.py <draft>
CITED-LINES: 0 finding(s) in 1 file(s)
[exit 0]
```

Quote fidelity check (mine, `stage/ScribeEntry/check_quotes.py`): for each 「」 span, the preceding line's single row id selects the fetched page; the span is matched as a whitespace-normalised substring and counted for words.

```text
$ python3 check_quotes.py <draft>
… 22 lines …
BAD 0
```

All 22 quotes are verbatim substrings of the served pages after whitespace normalisation; longest is 23 words (Menelaus), all <= 25. The checker is staged so the L1 can rerun it.

Structure census:

```text
$ wc -c <draft>            → 29046
$ grep -c '^- S9' <draft>  → 22
$ grep -c 'to-verify' <draft> → 2   (both are header policy sentences, see §6)
```

## 4. Touched surfaces

Written (all inside the wave dir):

- `.ufo/waves/round-82/w1/drafts/corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` (the deliverable)
- `.ufo/waves/round-82/w1/stage/ScribeEntry/fetch-records.md` (UA-bound receipts, located passages)
- `.ufo/waves/round-82/w1/stage/ScribeEntry/check_quotes.py` (quote-fidelity checker)
- `.ufo/waves/round-82/w1/stage/ScribeEntry/quote-check.txt` (its output)
- `.ufo/waves/round-82/w1/stage/ScribeEntry/lint.txt` (lint output and exit code)
- `.ufo/waves/round-82/w1/stage/ScribeEntry/structure.txt` (bytes, lines, ids, headings)
- `.ufo/waves/round-82/w1/ScribeEntry.md` (this report)

Not touched: `corpus/**`, `tools/**`, `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, `reports/**`, the lane's git/jj state and index, the fleet root, `shokuknow`. No registry row was written; the rows remain the L1's install.

**Bound incident, disclosed.** One failed `cd` into a not-yet-created stage directory caused three shell redirections to land at the fleet root `/home/vgpnk/Projects/shokunin/`: `lint.txt` (12 B), `quote-check.txt` (110 B), `structure.txt` (670 B). All three were my own scratch output, were untracked (`git ls-files` at the fleet root returned nothing for them), and were removed with `rm -f` within the same minute. `git -C /home/vgpnk/Projects/shokunin status --porcelain` before and after removal lists the same pre-existing entries and nothing else; the fleet tree was restored to its prior state. No fleet-root tracked file was created or modified.

## 5. Findings for the L1

1. **S907 is a live-served row, with the archive capture as the fixed copy.** The live page returns the article prose (318 words of visible text; both User-Agents, identical bytes); the capture `20191023112911` returns the same article (251 words). The page also carries a raw Parsoid `data-mw` template payload before the paragraph, and a naive tag-strip started there truncates the extraction — that is the trap my first probe fell into. The installed row already records the live serve and a capture; keep both.
2. **The planned second row duplicated S320.** Hávámál (Bellows) is the same translation as S320's Gutenberg #73533 text; the Tacitus swap avoids a duplicate document and gives the entry a second prose source with a different institutional profile (flat class, means-scaling, relay, no-return gift).
3. **The entry's six decisions are all anchored, but two families are anchored thinly**: "material token" (salt/tessera) has no primary anchor in these four rows — the token's lexical surface is cuisine's, and the entry says so — and "protection for N days" is a design parameter supported only by the term markers (host speeds the guest at departure; the doorway already protects). Both are marked as design levers, not row claims.
4. **S905's page is a translation titled "The Origin and Situation of the Germans" (1876)** while the registry citation says *Germania*; the row should keep the page title and translator pair so the quote is reproducible.
5. **Install state observed, not authored by me.** At 08:21, before my last draft edits, a 28992-byte version derived from my draft appeared at `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` (the L1's install, with the L1's corrected `- sources:` sentence about the Parsoid block). My draft is now 29046 bytes and differs from the installed copy at exactly four lines: the topic's seal-family wording (five options, not four); the `- sources:` sentence (same fact, my phrasing); the `- recheck:` sentence (the Britannica row is described as live-served with a fixed capture); and the two S907 bullets' loci and etymology span. I did not edit the installed file (`corpus/**` is out of bounds); the L1 should diff the two and choose the install text.

## 6. `(to-verify)` left

`grep -n 'to-verify' <draft>` → 2 hits, both in header fields as policy, none on a factual claim:

- line 7 `- source:` — says unverified material is labelled `(to-verify)`;
- line 9 `- recheck:` — says any claim extended past the edition dates is `(to-verify)` at first use.

No factual claim in the body is left unmarked: every factual sentence is either a §3 anchor restatement, a lane-policy statement, or labelled craft / method / NON-CANON. The invented language (Vethari) and the Ashen Quay example are explicitly NON-CANON; the entry decides nothing about any world.

## 7. Artifact paths

- Draft: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`
- Receipts: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeEntry/fetch-records.md`
- Lint: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeEntry/lint.txt`
- Quote check: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeEntry/quote-check.txt`
- Checker: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeEntry/check_quotes.py`
- Structure census: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/ScribeEntry/structure.txt`
- This report: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/ScribeEntry.md`
