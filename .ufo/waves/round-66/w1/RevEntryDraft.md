# RevEntryDraft — claim C entry draft vs accept-c.py ONEID/RESTATE

Seat: `RevEntryDraft` (reviewer, leaf). Axis: coverage/calibration. Milestone r66-v2.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base `94209e8`).
Method: LSP not applicable (Markdown corpus, no language server); semantic checks done by
importing the frozen counter `reports/round-66/accept-c.py` as a module and calling its own
helpers (`content_words`, `anchor_quote`, `in_order_coverage`, `norm_url`, `row_urls`,
`CAPTURE_RE`, `ROW_RE`, `cells`) so every number below is the instrument's own semantics,
not a re-derivation. Row-contract text taken from the seat spec (`spec-v2.json`, ScoutRow01
`BULLET=`/`CAPTURE=` lines).

## Verdict

**No authoritative entry draft exists at review time, so no per-line verdict can be issued
against it.** The lane tip is still the frozen base (`git rev-parse main` = `94209e8`,
i.e. 94209e8f80969dbac48d56c5d0e2e623635b8616); `git show main:corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`
is absent; `corpus/README.md` has no `scent-perfume` index row; `corpus/SOURCES.md` has no
row above S775; `.ufo/waves/round-66/rows/` is empty; `.ufo/waves/round-66/stage/entry-spec.md`
(ScribeEntrySpec's deliverable) is absent. This is itself a finding (F0) because the seat's
input does not exist eight minutes into the wave.

What I could audit, and did:

- **P1** `.ufo/waves/round-66/w1/mut-entry-scratch/corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`
  — a 38-line, 24-bullet, all-S777–S800 specimen, self-labelled
  `MUTATION FIXTURE (scratch only, not the round-66 entry)`. Audited line by line (24/24 PASS —
  see F1, which is the point).
- **P2** `/tmp/r66-rc-clone/.../scent-perfume-aromatics-codes.md` (528 B) and
  `/tmp/r66sweep/knowledge/culture-material/scent-perfume-aromatics-codes.md` (617 B) — stubs;
  both are unreviewable drafts (no 24 bullets, no rows).
- **P3** the model entry the scribe is told to copy,
  `corpus/knowledge/culture-material/games-play-sport-contests.md` (126 lines, 13 H2), audited
  against its own rows. It fails RESTATE at one line (F4).

Blocker for the L1: the entry cannot be reviewed for ONEID/RESTATE until the 24 row files
land in `rows/<SEAT>/row-S7xx.txt` and the draft exists. The auditor below reproduces every
leg on either input and should gate integration; run it before the commit, not after.

---

## Update — rows and the spec landed mid-review (measured at 08:5x)

`stage/entry-spec.md` (479 lines, 27 `SLOT` markers, no assembled bullets) and 24 row files
landed while this seat was open. The spec is still a skeleton, so there is still no per-line
draft to judge; its §6 arithmetic is correct and matches the counter by inspection
(membership-not-order for the quote leg, exact word forms, `cov < 0.80`) — the earlier
shorthand "in-order quote words" in the scout prompts is the wrong one, as F2 states.

What *can* be judged now is the input the scribe will assemble: the `BULLET=` lines.

### F12 (HIGH) — 8 of the 20 landed in-claim BULLET lines fail RESTATE verbatim

Run: `audit.py rows .ufo/waves/round-66/rows` (recursive). Rows present: S779–S796, S799,
S800 (20 of 24) plus frontier S801–S804. **Missing: S777, S778, S797, S798** → SET/ROWS
fail today regardless of the entry.

| id | inq | quote content words | bullet (verbatim) | why it fails |
|---|---|---|---|---|
| S781 | 2 | beyond culinary uses olive served base perfumes cosmetics medicines | Athletes carried small flasks of scented olive-oil **base**… | only olive/base; `perfume`→`olive-oil` substitution |
| S782 | **0** | large quantities rose water regularly distilled persia iraq least ninth century | Rosewater production at industrial scale predates any Avicenna innovation story. | entire quote vocabulary avoided (synonym rewrite) |
| S783 | **0** | first named alcohol based perfume | Hungary water, produced around 1370, distilled rosemary into medieval courtly perfumery. | quote is 5 words, none reused |
| S791 | **0** | strong scented substances power disinfect ward plague diseases | Perfume hung at neck or waist served as wearable prophylaxis against corrupted air. | "prophylaxis/corrupted air" replaces every quote word |
| S792 | **0** | como registraron observadores españoles respecto palacios aztecas centroamérica siglo | Scent staged paradise: fragrant blossoms opened banquets in Aztec palaces… | **quote is Spanish**; English bullet cannot match |
| S793 | 2 | hundreds years perfumers categorised quality ambergris according colour | Ambergris, a sperm-whale product graded by **colour**… | ambergris/colour only; add `perfumers` → inq=3 |
| S794 | 1 | gantiers parfumeurs fabriquent gants parfumés dont succès apogée cour louis | Parisian glovers monopolized the perfumer's craft … Louis XIV's Versailles. | **quote is French**; only `louis` matches |
| S800 | 2 | press production perfume textile press | Refitted equipment readings show Herculaneum harbored a **production** line for **perfume**. | needs `press` to reach 3 |

If the scribe copies these `BULLET=` lines into the entry, RESTATE fails on 8 ids and
ACCEPT-C-66 prints FAIL. Two of them (S792 Spanish, S794 French) **cannot be repaired in
English prose at all** — `content_words` does not translate, so the fix is upstream: the scout
must quote an English body sentence from the same page, or the bullet must embed the
original-language term (e.g. `gantiers-parfumeurs`, `gants parfumés`) as the register's
vocabulary. If the term is embedded, S794 reaches inq≈4; S792 stays the weak row. The other
six are one-word edits: reuse three quote content words in their exact inflected form, which
the spec's own §6 examples already demonstrate. Note this contradicts F2's row contract only
in direction — the contract says "in-order"; the rows fail even the weaker membership test.

### F13 (MED) — S795's "live URL" is an archive.org corpus zip, not the cited work
`rows/ScoutRow10/row-S795.txt`: live URL
`https://archive.org/download/wikipedia-scholarly-sources-corpus/10.2307%252F0.650.1.zip/10.2307%252F1005923.pdf`.
`row_urls` accepts it as live (netloc `archive.org` is not `web.archive.org`), so it contributes
a host to HOSTS (`archive.org`, measured) and is subject to LINK as if it were the publisher's
page; the double-encoded `%252F` shows a derived bundle path, not a canonical location. Tier
justification aside, this is the one row where "live URL" does not mean "the work's live page".

### F6 revised with measurement — the host threshold is *not* the risk; spelling is
24 row files yield **23 distinct raw netlocs** (`audit.py hosts`), so HOSTS ≥10 passes with
margin, contrary to my pre-data estimate. What the measurement shows is the counting
artefact I predicted: `collections.vam.ac.uk` ×2 (S790/S791) and `archive.org` counted as
sources, plus `www.`-prefixed hosts that LINK folds but HOSTS does not. The threshold is
safe; the number is not a measure of source diversity, and should not be cited as one.

## Findings

### F0 (HIGH, dependency) — the draft this seat must review does not exist at the lane tip
Evidence: `git rev-parse main` → `94209e8f80969dbac48d56c5d0e2e623635b8616` (= claims.json
`base`); `git show main:corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`
→ `fatal: path ... does not exist in 'main'`; `grep -n scent-perfume corpus/README.md` → no
match; `corpus/SOURCES.md` row count 701, max id S775. Consequence: every RESTATE/ONEID
claim about "the entry" would be speculation; the only complete specimens on disk are
fixtures (F1) and stubs (P2). Recorded, not worked around.

### F1 (HIGH) — RESTATE accepts keyword soup: 24/24 fixture bullets PASS while none is a clause
The fixture bullets are the row quote with stopwords stripped, comma-free, plus one shared
filler phrase appended to every bullet. Measured with the counter's own helpers against the
fixture's own registry:

| fixture line | bullet (truncated) | inq | cov | novel | verdict |
|---|---|---|---|---|---|
| :11 (S777) | games american indians divided general classes games chance games dexterity comparanda note | 10 | 0.00 | 8 | PASS |
| :15 (S781) | variations include teams which pulls rope attempting comparanda note | 7 | 0.00 | 9 | PASS |
| :33 (S795) | london brugte bogstaverne take half down nothing comparanda note | 7 | 0.00 | 8 | PASS |
| :35 (S797) | games consist main divisions which called descriptive singing choral comparanda note | 9 | 0.00 | 6 | PASS |
| :38 (S800) | gambling associated ethnohistorically ball game patolli comparanda note | 6 | 0.00 | 7 | PASS |

All 24 lines: `inq` 6–12, `cov` 0.00–0.12, `novel` 6–14, **FAIL=0**. This is a
reproducible shortcut class for claim C: strip the stopwords out of the anchor quote, append
any one out-of-vocabulary token, and RESTATE passes with no readable restatement. Note the
shared filler is what buys the `novel` leg every time — `novel` tests vocabulary membership
(`accept-c.py:245`), not novelty of claim, so one decorative token repeated 24 times
satisfies it. If a scribe reproduces this shape under time pressure, ACCEPT-C-66 prints PASS
and the entry contains no prose.

### F2 (HIGH) — the predicate is weaker than the row contract the scouts are given
Seat spec (ScoutRow01) requires each `BULLET=` to be "one clause: 6-25 content words, **>=3
in-order** content words from the quote, **no run >12 words copied from the quote**".
`accept-c.py` implements neither "in-order" nor the copied-run cap:

- `inq` is order-free set membership: `inq = sum(1 for w in qw if w in bw)` (`:243`).
  A bullet that scrambles the three quote words passes; the fixture does exactly this
  (e.g. `:15` "variations include teams which pulls rope attempting").
- There is no leg measuring copied runs. A bullet that lifts a 20-word verbatim run from the
  quote passes as long as `cov` (measured against the *teaches* cell) stays <0.8, which it
  does whenever the teaches cell is a paraphrase.

So `ACCEPT-C-66: PASS` is compatible with verbatim quotation and with scrambled quote words —
both of which the round's own row discipline forbids. Coverage evidence should not be read
as "restated in prose" on this predicate alone.

### F3 (HIGH) — ONEID/RESTATE fold-in traps that fail whole ids, measured
`ONEID` counts `(SID)` over the whole file (`:219`); `RESTATE`'s bullet map uses
`re.search(r"\((S\d{3,})\)", l)` — **first match per line only** (`:229`). Measured on real
rows S750/S756:

| draft shape | S750 | S756 |
|---|---|---|
| one id per bullet line (control) | ONEID=1 bullets=1 PASS | ONEID=1 bullets=1 PASS |
| two ids on one line `... (S750) (S756)` | 1/1 PASS | ONEID=1 **bullets=0 FAIL** |
| composite `... (S750; S756)` | ONEID=0 bits=0 **FAIL** | ONEID=0 **FAIL** |
| a later line repeats the id (`Sources: ... (S750)`) | ONEID=2 bits=2 **FAIL** | 1/1 PASS |
| frontmatter/meta line carries `(S750)` | ONEID=2 bits=2 **FAIL** | — |

Consequences for the draft, in order of likely damage:
1. **Any recap/index/'sources' table listing S777–S800 fails every id it lists.** The model
   entry avoids this by declaring "no citation is added here" in its cross-cultural section
   and by citing other entries by path, not by id — that is why it passes. A draft that adds
   a summary table of the 24 rows loses all 24.
2. **Two ids on one bullet**: the second id gets `bullets=0` and fails; the first passes, so
   the failure is silent unless the log is read id by id.
3. The docstring says "cited exactly once in the entry body" but the code scans the whole
   file — a `- verified-at:` or `- source:` meta line carrying `(S777)` double-counts.

### F4 (HIGH) — the model entry the scribe is told to copy already fails RESTATE at S754
`games-play-sport-contests.md:44`: `- Teams each pull one end of a rope during village rites,
treating the contest as a communal ceremony rather than a sport. (S754)` → **inq=2** (only
`teams`, `rope`), so RESTATE FAILs on the very template the scribe is pointed at. Cause is
morphology, not content: the quote (`"Most variations include two teams, each of which pulls
one end of a rope attempting to tug it from the other."`) has `pulls`, the bullet has `pull`;
`content_words` does not stem, and `variations/include/which/attempting` were dropped. Two
verified repairs (same row, measured): `inq=4, cov=0.00, novel=7` for "Two teams each **pulls**
one rope end, attempting to tug it from the other, as village rites stage it."
Verified safe recipe from the same probe set: **copy ≥3 quote content words with their exact
inflection, add one content word the teaches cell does not use.** (S750 probe: `inq=6,
cov=0.05, novel=7`.)

### F5 (MED) — planned S777/S784 are structurally unsatisfiable if the scout quotes the UNESCO inscription line
142 of 701 base rows have **no quoted string at all** in cell 5 (`anchor_quote` → None →
`inq=0` unconditionally); 60 more have a quote with **<3 content words**. The canonical
offender is the UNESCO element record, whose obvious quotable line is
`"Inscribed in 2009 (4.COM)"` → 1 content word (`inscribed`; `4.COM` is not alpha). Base rows
S157 and S186 carry exactly that quote and are therefore RESTATE-unsatisfiable with any
bullet. S777 (UNESCO incense listing) and S784 (Grasse UNESCO) are the two planned rows with
this exposure; the row template's "anchor quote 8-25 body words" is the guard, but nothing
checks it. A row whose quote lands in cell 4 (scope) instead of cell 5 fails the same way —
the fixture's own rows put the quote in cell 5 correctly, older rows do not.

### F6 (MED) — HOSTS silently loses rows and counts spellings, not sites
`hosts` is built from `live_urls`, which only contains rows where `row_urls(c[1])` returned a
live URL (`:254`). Measured: `row_urls('https://web.archive.org/web/2026...id_/https://x.org/a')`
→ `None`. So a row whose source cell carries only a capture (a format violation that still
passes CAPTURE) vanishes from HOSTS **and** from LINK — 24 rows could yield 10 hosts while one
of them is never deduplicated. In the other direction, HOSTS uses raw `netloc` with no `www`
folding, while LINK folds `www`: `x.org` and `www.x.org` count as two hosts. `>=10 hosts` is
therefore satisfiable by one site under two spellings. Planned-source arithmetic makes this a
real threshold risk: UNESCO (`ich.unesco.org`) is the lead for both S777 and S784, the Met for
S780 (and plausibly S797), the British Museum for S781/S798, the V&A for S790/S791 — four
likely pairs collapse to one host each, so the effective count starts near 11–13, not 24.
Run `audit.py hosts rows/` after the rows land, before the counter.

### F7 (MED) — CAPTURE never checks that the capture is of the cited page
`CAPTURE_RE` (`:53`) matches any `web.archive.org/web/<14 digits>` substring anywhere in the
source cell; measured matches: a capture whose original is `https://TOTALLY-DIFFERENT.org/zzz`
→ **True**; a fabricated timestamp `web/99999999999999id_/...` → **True**; the free token
`no-capture` → leg passes without any capture (`:308`). The row contract says the capture's
original must "query-aware-normalize equal to the live URL"; the counter never compares them.
For claim C this means a row can carry a stale or unrelated capture and still print PASS.

### F8 (MED) — LINK is scheme- and query-sensitive despite the docstring
`accept-c.py:12` says the LINK leg is "(scheme/www/query-insensitive)". `norm_url` (`:90-99`)
folds only the `www` prefix and keeps scheme and query in the identity — measured:
`http://cslds.org/a` ≠ `https://cslds.org/a`, `https://x.org/p?a=1` ≠ `https://x.org/p?a=2`,
`https://www.x.org/p` = `https://x.org/p`. Base already contains `http://` rows (S097), so
citing the same page under `https` is a live bypass of the duplicate check. Conversely the
leg is stricter than the docstring implies for any row whose URL carries a query.

### F9 (LOW) — `row_urls` keeps trailing punctuation
`URL_RE = https?://[^\s<>"|`;]+` (`:52`) excludes `|`, `;`, quotes and angle brackets but not
`)`, `,`, or `.`; a markdown/parenthesised URL carries the delimiter into the normalized
identity, so two rows citing one page can both pass LINK. Registry practice (space before the
`;` capture) avoids this today; a scout writing `(https://…/a)` would not.

### F10 (LOW) — the near-copy leg is vacuous on prose and only bites near-verbatim teaches copies
Measured `cov` across all 26 model-entry bullets: 0.00–0.214 (max on S775). Across all 24
fixture bullets: 0.00–0.12. Nothing in either specimen teaches a near-copy of its teaches
cell — the leg cannot fire at these lengths. It fires only when a bullet reproduces ≥80 % of
the teaches cell's content words in order, i.e. a verbatim lift of a two-sentence cell. The
inverse risk is real but small: 60 base rows have teaches cells ≤9 content words, and for a
5-word teaches cell an honest restatement carrying 4 of those words in order hits exactly
0.80 → FAIL. Scouts writing terse teaches cells (`<=9` content words) create that trap for
the scribe; the round's planned teaches budget (≤240 chars) is long enough to avoid it.

### F11 (LOW) — cross-row duplication is invisible to the predicate
Planned pairs share subject matter and will not be caught by any leg: S778 (kyodo ceremony)
vs S799 (kodo games); S779 (kyphi) vs S797 (Egyptian anointing); S781 (Roman/Greek perfume)
vs S798 (perfume vessels); S777 vs S784 (both ICH listings). RESTATE compares each bullet
only to **its own** row's quote/teaches, so two bullets can teach the same claim, and one
bullet can be a near-copy of a *sibling row's* teaches cell, with the counter silent. This
is a review-only check (claims.json lists "blind per-row support" as review_only), so the L1
must read the 24 bullets against each other; the instrument will not.

## Per-SID risk table for the planned rows (S777–S800)

Not a verdict — these rows do not exist yet. Ranked by the leg most likely to fail, from the
planned leads in `spec-v2.json`:

| ids | planned lead | dominant risk |
|---|---|---|
| S777, S784 | UNESCO ICH element listings | F5 (inscription-line quote <3 content words), F6 (same host) |
| S780, S797 | Met Heilbrunn / Met Egyptian | F6 (same host), F11 (overlap with S779/S781) |
| S781, S798 | museum perfume / perfume vessels | F6 (British Museum likely for both), F11 |
| S790, S791 | V&A gloves / pomander | F6 (same host) |
| S778, S799 | kyodo / kodo | F11 near-duplicate teaches |
| S788 | Classen, anthropology of smell | F7 (paywalled → capture of abstract or unrelated page passes CAPTURE) |
| S793 | amber/ambergris | F2 (quote may not carry the scent claim at all; write the bullet from the quote, not the topic) |
| S795 | incense clocks | F11 (adjacency: `timekeeping-instruments.md` owns the register; not a counter leg) |
| all 24 | — | F3: no recap table, no second `(SID)` anywhere, one id per bullet line |

## Tool delivered with this review (for the L1's gate, not a lane artifact)

`.ufo/waves/round-66/w1/RevEntryDraft-scratch/audit.py` — imports the frozen counter and
prints accept-c's own ONEID/RESTATE numbers plus the row-contract warnings the counter omits
(word count outside 6–25, copied run >12). Three modes:

```
python3 audit.py entry <entry.md> [<registry.md>]   # per-line ONEID/RESTATE, exit-ready
python3 audit.py rows  <rows-dir>                   # ROW=/BULLET= preflight before integration
python3 audit.py hosts <rows-dir>                   # F6/F8/F9: distinct hosts + LINK collisions
```

Validated against both calibration inputs: model entry → 26 ids, 1 FAIL (S754, F4);
fixture → 24 ids, 0 FAIL (F1). It writes nothing into the lane; the only files this seat
created are under `w1/RevEntryDraft.md` and `w1/RevEntryDraft-scratch/`.

## Residual risk and verification gaps

- The entry that lands may differ from every specimen audited; F0 stands until a draft exists.
  Re-run `audit.py entry` on it before the L1 commits.
- I did not run `accept-c.py` end to end (it would FAIL FILE/SET/ROWS and exit 2-ish on the
  missing entry, and running the whole counter is another seat's job). All numbers here come
  from importing its helpers, so they match the legs by construction but are not a substitute
  for the counter's own run.
- Legs outside this seat's slice (FILE counts, APPEND, NOHARM, SWEEP, TOPIC) were not
  exercised; TOPIC in particular depends on a README row that does not exist yet.
- F1's fixture is *designed* to pass; I use it as a constructive existence proof of the
  shortcut, not as evidence that the round's scribe intends word salad.
- No tools were installed or upgraded this seat (nothing was needed; no pacman, no uv).

## Reproduce

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
# F4 (model entry): 26 ids, S754 inq=2 FAIL
python3 .ufo/waves/round-66/w1/RevEntryDraft-scratch/audit.py entry \
  corpus/knowledge/culture-material/games-play-sport-contests.md | tail -3
# F1 (fixture): 24 ids, FAIL=0 on word salad
python3 .ufo/waves/round-66/w1/RevEntryDraft-scratch/audit.py entry \
  .ufo/waves/round-66/w1/mut-entry-scratch/corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md \
  .ufo/waves/round-66/w1/mut-entry-scratch/corpus/SOURCES.md | tail -3
# F5: 60 rows with <3 content-word quotes, 142 with none
# F6/F8: normalizer probes (scheme/query/www, archive-only cell)
# F7: CAPTURE_RE accepts a capture of an unrelated URL and a fabricated timestamp
```

Report: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-66/w1/RevEntryDraft.md
