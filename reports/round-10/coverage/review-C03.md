# R10-C13 — Reviewer of worker C03's linguistics entry (author-side review)

**Verdict: PASS on all four mandated checks** — frontmatter completeness, source
resolvability, no filler (gap named and genuine), no duplication of an existing
entry — for `corpus/knowledge/linguistics/numerals-and-measures.md`, sha256
`57fc76695c9fed38cf87ddccbaf7e5c5d322125f65b98aea154baf5046129340`. Details,
evidence and limits in §4–§5.

- reviewer scope: `reports/round-10/coverage/review-C03.md` only. No corpus, ledger,
  bookkeeping, canon, or promotion edits. Author-side review evidence only; not an
  admission decision and not independent promotion verification.
- assignment: `reports/round-10/targets.json` → `R10-C11..C20` ("Ten reviewers: one
  per authored entry (poll for it, max 20 min): verify frontmatter completeness,
  source resolvability (re-run the cited command or open the cited path/URL), no
  filler, no duplication of an existing entry; verdict
  `reports/round-10/coverage/review-<id>.md`").
- C03 is the third linguistics-partition author (`R10-C01..C10` seat split:
  linguistics ×3 = C01–C03, myth-symbol ×3 = C04–C06, culture-material ×2 = C07–C08,
  verification ×2 = C09–C10). Expected outputs: fragment
  `reports/round-10/coverage/C03.md` naming one new
  `corpus/knowledge/linguistics/<slug>.md` entry.
- round-10 declared baseline revision: `9dc18ec1339bffd6f81e74f1a5742464ef578749`
  (`reports/round-10/claims.json`); worktree HEAD throughout:
  `e3a1ec9435787328ac9f828f96cb6390e4916b8f` ("round-10: availability attempt 3 —
  opencode-go-5 dry; keys 3/4/5 unprovisioned, retrying key 1").
- date: 2026-10-17, local clock UTC-03:00. Poll window opened 18:26:30 (-03); entry
  landed 18:33:06, author fragment landed ≈18:35; review closed ≈18:39.

## 0. Review status — RESOLVED

At review open (18:26:30–18:31:00) C03's fragment and entry were not inspectable:
`reports/round-10/coverage/` held only sibling reviewer/auditor files and
`corpus/knowledge/linguistics/` still held exactly its 16 committed files, all with
pre-round-10 mtimes. The wave was live in other partitions (verification 13 → 15 at
18:30–18:31; drift shards 01–14; `findings-tracker.json`; the acceptance runner).

The entry landed at **18:33:06** and the author fragment at **≈18:35**. Identification
is decisive on the bytes, not inferred from ordering: the entry's own frontmatter
names the fragment as its receipt store — "saved copies + sha256 in
`reports/round-10/coverage/C03.md`" and "see `reports/round-10/coverage/C03.md` for
the exact commands, hashes and grep receipts" — and the fragment's title is
`R10-C03 — coverage fragment: corpus/knowledge/linguistics/numerals-and-measures.md`,
recording the same sha256 this review measured.

## 1. Method applied (frozen before the entry landed)

The four mandated checks, aligned with the round-10 acceptance runner's own criteria
(`reports/round-10/run-validation.py`, read at 18:32; the runner itself was **not**
executed by this seat, because it writes the shared `reports/round-10/validation.json`
owned by the X03 seat — its regexes were re-implemented instead, in
`.scratch/c13-full-check.py`):

1. **Frontmatter completeness** — `C_FRONTMATTER_FIELDS = ("topic", "sources",
   "verified-at", "recheck", "couples")` (`run-validation.py:81-82`), each matched by
   `^\s*[-*]?\s*<field>\s*:\s*(\S.*)$` (`:316-325`) and non-empty. This is the house
   five-field profile; `corpus/README.md:244-246` records that the fleet's separate
   `source`/`verified-at`/`recheck` header is not corpus-wide, so absence of a
   singular `- source:` head line is corpus-normal, not a defect.
2. **Source resolvability** — open every cited repo path; re-run every cited runnable
   command; give every cited URL a documented access attempt; recompute every digest
   the entry or its fragment publishes. Round-8/9 receipts cited by path count as
   sources per `claims.json` C.
3. **No filler / named gap** — the runner's machine half is a `gap:`-family field or a
   `##`–`####` heading containing "gap" (`:327-331`); its limits block states the
   machine check "verifies that a gap is named, not that the gap is genuine —
   reviewers own that judgement". This seat owns that judgement: the gap must be real
   (a topic no existing entry owns) and the entry must deliver on it.
4. **Decision-record section** — runner regex
   `^#{2,4}[^\n]*decision[- ]record[^\n]*\n+\s*(\S[^\n]*)` (`:332-334`). Baseline: only
   12 of 179 committed entries carry a heading containing "decision" (4 linguistics,
   5 synthesis, 3 verification), so this is a round-10 addition the entry must
   actually deliver.
5. **No duplication** — slug/title/topic collision against the committed baseline plus
   an 8-gram body-shingle Jaccard screen. Calibration measured over **all 15,931
   pairs** of the 179-file corpus at review open: the highest 8-gram Jaccard between
   any two committed entries is **0.0119** (`linguistics/morphological-typology.md` vs
   `linguistics/historical-linguistics.md`). An overlap of a few percent against any
   single entry would therefore be a real signal; corpus-normal genre phrasing sits
   near zero.

## 2. Baseline facts at review open (commands from the repo root, 18:26–18:32 -03)

```
$ for d in corpus/knowledge/*/; do printf '%s %s\n' "$(basename $d)" "$(ls $d | wc -l)"; done
civilizations 94   culture-material 16   linguistics 16   myth-symbol 16
synthesis 24       verification 13                        # 13 at open; 15 by 18:31
$ python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge   # exit 0
totals: files=179 files_with_any_mark=128 files_with_marker=118 lines=33021 raw_lines=610
$ sha256sum corpus/knowledge/linguistics/*.md > .scratch/c13-ling-sha.txt           # 16 lines
```

The 16 linguistics slugs at open: `color-terminology`, `conlang-methodology`,
`historical-linguistics`, `kinship-terminology`, `language-contact`,
`linguistic-anthropology`, `morphological-typology`, `naming-systems`,
`orality-formulaic-language`, `phonetics-phonology`, `politeness-taboo-euphemism`,
`semantic-fields-lexicon-building`, `semantics-pragmatics`,
`sociolinguistics-registers`, `syntax-typology`, `writing-systems`.

README index-vs-files for the target partition at open: `linguistics: claimed=16
rows=16 files=16`, missing NONE, extra NONE, duplicate rows NONE. Corpus-wide
frontmatter census (179 files): `topic` 179, `sources` 179, `couples` 179,
`verified-at` 180, `recheck` 180, `source` 120. Decision-heading census: 12 files.

## 3. Observations outside this seat (reported, not dispositioned)

Recorded read-only for the parent; this seat owns no bookkeeping write:

- **README index is stale at review close.** `corpus/README.md:16` still reads
  `## linguistics/ (16)` and `:273` still reads `Total knowledge entries: 179.`, while
  the live tree now holds 19 linguistics files and 187 corpus files (counts below in
  §4.6). No `numerals-and-measures.md` row exists. The index update is the C21/C22
  assignment, not C03's — the entry and its fragment both state that C03 did not touch
  the README — but claim C's "index rows match actual files" clause is **not yet
  satisfied wave-wide** at review close, and the acceptance runner's own receipt
  already lists the README mismatches among its C failures.
- **`M corpus/README.md`**: one line changed — the
  `civilizations/africa-primary-sources.md` row description rewritten. No C01–C10
  target partition covers civilizations; whether this is an authorised index-updater
  act or an out-of-seat edit is the parent's call.
- **`M reports/round-9/validation.json`** (`4 insertions(+), 14 deletions(-)`): filed
  receipt bytes rewritten, while round-10's F targets say "never rewrite filed report
  bytes — corrections are new entries". Whether authorised or not is the parent's call.
- **The acceptance runner already fails claim C on a sibling entry**
  (`reports/round-10/validation.json`, claims.C.failures:
  `corpus/knowledge/verification/verification-independence-anti-circularity.md: no
  named gap (filler risk)`), and on partition minimums. That is the C09 seat's finding,
  recorded here only because this review applies the same criterion to C03.
- **Evidence durability, corpus-wide pattern.** C03's URL receipt *bytes* live in
  `.scratch/r10c03/` (untracked, ephemeral); the durable record is the digest table in
  the filed fragment. The chain therefore rests on digests plus re-fetchability of
  live URLs, not on durable copies. This review closes it by re-fetching the URLs and
  recomputing the digests (§4.2) — but any later round that needs the original bytes
  will need network access, and the parent may want a durable-receipt rule.
- `.scratch/` is shared by all live workers (sibling `c11-*`, `c14-*`, `c20-*`,
  `audit-*`, `r10c03/` files present); this seat names all its scratch `c13-*`.

## 4. Landed-bytes review

### 4.1 Frontmatter completeness — PASS

`topic`, `sources`, `verified-at`, `recheck`, `couples` are each present exactly once
in the head block (text before the first `## ` heading), all non-empty, none a
placeholder:

- `verified-at` is dated and scope-bearing (2026-10-17; states what was fetched and
  hashed, what was not re-fetched, and that six library-level figures remain
  `(to-verify)`).
- `recheck` names triggers (before quoting the WALS census, before using any
  `(to-verify)` figure, before citing the Pirahã debate as settled).
- `couples` references resolve: every `*.md` token in the entry resolves
  (`locators_missing: []`, 14 existing repo locators — the pre-fragment run had
  exactly one unresolved token, `reports/round-10/coverage/C03.md`, which resolved
  when the fragment landed).

Field census, machine-checked with the runner's own regex:
`frontmatter_missing: []`.

### 4.2 Source resolvability — PASS

**Cited commands re-run by this seat** (read-only):

```
$ grep -ric -e "numeral" corpus/knowledge/linguistics/*.md
historical-linguistics.md:1  language-contact.md:6  linguistic-anthropology.md:2
semantic-fields-lexicon-building.md:2  semantics-pragmatics.md:5
syntax-typology.md:3  writing-systems.md:2            # matches the entry's sweep exactly
$ python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
files: 187                                            # was 179 at review open
$ python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics/numerals-and-measures.md
INFO to-verify-count: …: 12 mark(s) on 12 line(s)
INFO scan: files=1 marks=12 mark-lines=12 findings=0 blocked=0        # exit=0
```

**Cited URLs re-fetched live by this seat** (2026-10-17, via the review seat's own
fetch, independent of the author's `curl`): `wals.info/chapter/131`,
`wals.info/feature/131A`, `wals.info/chapter/55` all resolve and support the claims
made from them:

- ch. 131 text confirms every worked example and every coding rule the entry states —
  the `x·n + y` base definition and Mandarin `èr-shí-lìu`; Diola-Fogny 51 "two twenties
  and eleven"; Basque `berr-eun eta berr-ogei-ta-hama-sei`; Ekari base 60 with 71 =
  "one and ten and sixty" and Sumerian base 60; Kobon 1–12 up the left side and 13–23
  down the right, with `siduŋ` "shoulder" multiply ambiguous (10, 14, 33, 37, 56…);
  extended body-part systems as making no use of an arithmetic base; Mangarrayi to 3
  and Yidiny to 5; Pirahã per Dan Everett p.c.; *pair* excluded as a numeral and
  *seventy* vs *three score and ten*; Igbo base 20 with 1–19 on base 10; Supyire base
  80 with 399 = 80×4+20×3+10+5+4; Chukchi vigesimal with no word for 400; Turkish
  portmanteau tens; Spanish *-enta*; Russian *sorok*; French assigned decimal despite
  *quatre-vingt-dix-sept*; decimal encroachment, and the chapter's closing
  "Non-decimal numeral systems are even more endangered than the languages in which
  they occur" (the sentence the entry quotes).
- feature 131A carries the **exact census the entry prints**: Decimal 125 / Hybrid
  vigesimal-decimal 22 / Pure vigesimal 20 / Other base 5 / Extended body-part 4 /
  Restricted 20 = **196**.
- ch. 55 confirms the absent/optional/obligatory frame with Minangkabau
  *duo (ikue) anjiang*, Tagalog *dalawa=ng aso*, Vietnamese *hai con chó*, the
  sortal-vs-mensural distinction, Mandarin *sān zhī huā* vs *sān duǒ huā*, the
  Vietnamese food-stall register (*ba gà hai bò*), the Toqabaqita noun-class caveat,
  and the East/SE-Asia concentration with the West African / Pacific Northwest /
  Mesoamerican / Amazonian hotbeds.

**Published digests recomputed** (`.scratch/r10c03/`, all four match the fragment's
table byte-for-byte): `wals-131.html` `7cdbce0cfaca245e530da762a329cf279f9190ba883a447689beef8bc77f21e6`;
`wals-55.html` `feaf7b782362bb713ae0281cfbd755401cd22e48b8b535dbf07e255d8f04f2c4`;
`wals-131A.html` `ad60238df8125f1afd6762983b1ea833117389a2c1fe7f64efd6b3e8a932e310`;
`wals-55A.html` `6fb5fbcf2c456bf6955fb5cd763deb8633e2aa80af36c8396b5decbd32469591`.
The fragment's own corroboration greps reproduce on the saved copy: `grep -c "125"`
→ 1, `grep -c "196"` → 5, and all six value labels (`>Decimal<`,
`>Hybrid vigesimal-decimal<`, `>Pure vigesimal<`, `>Other base<`,
`>Extended body-part system<`, `>Restricted<`) present exactly once.

**Bibliographic locators** — spot-checked independently: Epps (2006), *Diachronica*
23(2): 259–288, doi:10.1075/dia.23.2.03epp resolves through multiple independent
listings (MIT OECS numerical-cognition bibliography; a Royal Society *Phil. Trans. B*
reference list; Wikipedia's numeral-systems bibliography). The remaining six locators
were **not** independently re-verified by this seat (see §5, limit 2).

### 4.3 No filler / named gap — PASS

The gap is named in a headed section (`## 0. The gap this entry fills`, matching the
runner's `gap_heading` regex; `gap_ok: true`) and it is **genuine**, verified against
the bytes rather than accepted:

- the corpus names the file itself: `language-contact.md:7` lists
  `numerals-and-measures.md` among sibling knowledge files "to seed" — confirmed by
  direct read of that line;
- `writing-systems.md:7` names `numerals-and-measures` in its `couples:` line —
  confirmed (`grep -c` → 1);
- the coverage sweep (re-run by this seat) shows only incidental prior mentions, no
  entry owning the topic;
- the two adjacent entries defer rather than cover: `number-symbolism.md` owns number
  *meaning* and itself routes base detail to the language files ("→ language files:
  numeral bases and etymology (historical-linguistics)…"), and
  `trade-economy-lexicon.md` owns metrology.

The entry delivers on the gap: 209 lines covering base typology, numeral-word
morphology, the ordinal/collective/distributive family, the classifier interface,
counting technologies, restricted/anumeric systems with the Pirahã dispute
calibrated, diachrony and contact, decision tables, a labelled NON-CANON worked
example (`## 10. Worked example (NON-CANON, illustrative only)`), a plain-language
calibration section, and a decision record. Canon hygiene holds: the entry ends at
the handoff and defers world-bible canon to lore-shokunin.

### 4.4 Decision-record section — PASS

`## 12. Decision record` (line 192) with a six-row table D1–D6, each row carrying a
decision, a rationale, and a reversal condition. Runner regex:
`decision_record_ok: true`. The decisions are substantive, not decorative — D1 fixes
the scope boundary against the two neighbouring entries, D2 adopts the WALS frame
with its coding caveats inline, D3 refuses to take a side in the Pirahã dispute, D6
forbids `(to-verify)` figures inside decision tables.

### 4.5 No duplication — PASS

Slug collision: none (`numerals-and-measures` is unique corpus-wide). 8-gram
body-shingle Jaccard against all 186 other entries in the now-187-file corpus:

| comparison | Jaccard | reading |
|---|---|---|
| corpus-wide maximum (any entry) | **0.0009** (`culture-material/garment-lexicon-crosslinguistic.md`) | two orders of magnitude below the 0.0119 corpus-normal maximum; no reuse |
| declared boundary: `myth-symbol/number-symbolism.md` | **0.0000** | the symbolism file's §10 base table and this entry's §1 base typology share no text; the split is real |
| declared boundary: `culture-material/trade-economy-lexicon.md` | 0.0002 | metrology stays with the economy file |
| new sibling `linguistics/sound-symbolism.md` | 0.0001 | distinct |
| new sibling `linguistics/language-shift-obsolescence-revival.md` | 0.0000 | distinct |

Topic-token overlap is coarse at this granularity: the maximum, 0.333, is shared by
several entries including the declared boundary `number-symbolism.md`, and **no
linguistics entry scores higher than that tie** — no sibling in the same partition
competes for the topic. The decisive check is the body-shingle screen, where the
nearest neighbour anywhere is a garment-lexicon entry at 0.0009 (ordinary shared
English) and the declared boundary file scores 0.0000.

### 4.6 Entry identity and churn

`sha256 57fc76695c9fed38cf87ddccbaf7e5c5d322125f65b98aea154baf5046129340`,
34,831 bytes, 209 lines, mtime 18:33:06 — byte-identical at review open (18:33), at
the full-check re-run, and at review close; the fragment records the same digest, so
entry and fragment agree on the artifact under review. Corpus totals moved during the
window only through *other* authors' entries: 179 → 187 files (linguistics 16 → 19,
myth-symbol 16 → 18, culture-material 16 → 17, verification 13 → 15; civilizations 94
and synthesis 24 unchanged), so the fragment's "total 183" snapshot is a
concurrent-write artifact of its write instant, not an error.

## 5. Verdict and limits

**Verdict: PASS.** All four mandated checks pass on the landed bytes, with the
sources re-fetched and the digests recomputed by this seat rather than taken from the
author's fragment. The entry names a gap the corpus itself asked for, fills it without
duplicating any of the 186 other entries, carries complete five-field frontmatter and
a six-row decision record, and grounds its live claims in sources this review could
independently resolve.

Limits of this review, stated plainly:

1. **Not an admission decision and not independent promotion verification.** This is
   author-side review evidence; admission belongs to the parent and to the acceptance
   runner, which this seat deliberately did not execute (it writes the shared
   `reports/round-10/validation.json`).
2. **Six of seven bibliographic locators are author-asserted.** The entry says they
   were "confirmed via search listing" on 2026-10-17; this seat independently
   confirmed only the Epps 2006 DOI. The library-level citations are not full-text
   retrievable here and are correctly marked `(to-verify)` where figures depend on
   them.
3. **The `(to-verify)` discipline is present, not resolved.** The gate counts 12 marks
   on 12 lines (all INFO, `findings=0`); the entry lists its carried `(to-verify)`
   items in the frontmatter and §11 and forbids their use in decision tables. Whether
   those figures are true is out of this seat's scope and stays open for a
   source-recheck wave.
4. **Receipt bytes are scratch-local.** The URL copies live in `.scratch/r10c03/`
   (untracked). Durability rests on the digests filed in `C03.md` plus re-fetchability
   of live URLs; this review restored that chain by re-fetching, and flags the pattern
   for the parent (§3).
5. **Index staleness is outside this entry's control.** `corpus/README.md` had no
   `numerals-and-measures.md` row at review close; the C21/C22 updaters own it, and
   claim C's index-match clause is not yet satisfied wave-wide.

## 6. Reproduction

```
$ sha256sum corpus/knowledge/linguistics/numerals-and-measures.md
57fc76695c9fed38cf87ddccbaf7e5c5d322125f65b98aea154baf5046129340
$ python3 .scratch/c13-full-check.py corpus/knowledge/linguistics/numerals-and-measures.md
frontmatter_missing: []  gap_ok: True  decision_record_ok: True
locators_missing: []     locators_existing: 14   urls: 4
shingle_top: [0.0009, corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md]
$ python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics/numerals-and-measures.md   # exit 0
INFO to-verify-count: …: 12 mark(s) on 12 line(s); scan: files=1 marks=12 findings=0 blocked=0
$ sha256sum .scratch/r10c03/wals-*.html      # all four match the C03.md digest table (§4.2)
$ grep -ric -e "numeral" corpus/knowledge/linguistics/*.md   # matches the entry's sweep
```

Review-seat scratch: `.scratch/review-harness.py`, `.scratch/c13-full-check.py`,
`.scratch/c13-watch.sh`, `.scratch/c13-poll-receipts.log`, `.scratch/c13-ling-sha.txt`,
`.scratch/c13-ling-slugs.txt`, `.scratch/c13-decision-entries.txt`,
`.scratch/topics-baseline.txt`. All commands from the repo root with
`TMPDIR=$PWD/.scratch` exported.
