# RevCounterC — attack on reports/round-66/accept-c.py (claim C)

Seat: attack / reviewer. Target: `reports/round-66/accept-c.py` (sha256
`0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86`, identical to the
sha recorded in `reports/round-66/telemetry/dry-run-c.txt:1` — **no stale-receipt
finding**). Lane was not mutated: I cloned the lane read-only to `/tmp/r66-rc-clone`
(`git clone` of base `94209e8…`), copied the untracked counter into the clone, and
committed nothing anywhere. All leg verdicts below are **observed output** of the
unmodified counter on crafted fixture rows unless marked `[INFERENCE]`.

Method: two independent surfaces — (a) the counter run end-to-end on a fixture registry
in the clone (`python3 reports/round-66/accept-c.py --root .`), (b) the counter's own
functions loaded via `importlib` and called with the exact predicate expressions from
lines 240–246 and 258–269. Function-level results are labelled as such; leg-level
strings are quoted verbatim.

---

## Item 1 — minimal bullet = teaches cell + ONE trailing novel word

### Crafted strings

Row S777 (11 cells; c[5]=anchor, c[6]=teaches):

```
| S777 | Synthetic fixture source, S777 page - https://example.org/scent/frankincense ; https://web.archive.org/web/20260101000000id_/https://example.org/scent/frankincense . | docs | B | fixture scope | page body: "frankincense resin burns slowly in the censer" | frankincense resin burns slowly in the censer | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md |
```

Entry bullet (the minimal perturbation — teaches verbatim + one novel token):

```
- Frankincense resin burns slowly in the censer smoke (S777)
```

### Worksheet math

`content_words` (len≥4, alpha, non-stopword) on casefolded NFKC text:

- `tw` (teaches) = `[frankincense, resin, burns, slowly, censer]`, |tw| = 5
- `bw` (bullet)  = `[frankincense, resin, burns, slowly, censer, smoke]`, |bw| = 6
- `qw` (quote)   = same 5 words as `tw`

`in_order_coverage(tw, bw)` (line 121, greedy subsequence, clause=teaches,
reference=bullet): every teaches word is consumed at consecutive `bw` indices
0,1,2,3,4 → `hits = 5`, `cov = 5/5 = 1.0000`.

Predicate at line 246: `inq < 3 or cov >= 0.8 or not novel`.
`inq = 5` (≥3 ✓), `novel = ['smoke']` (✓), `cov = 1.00 ≥ 0.80` → **RESTATE FAIL**.

Observed leg line (fixture run):

```
RESTATE FAIL bad=['S777:quote_words=5 teaches_cov=1.00 novel=1', 'S779:bullets=0', 'S782:bullets=0', 'S783:bullets=0']
```

**Verdict for item 1: the <80% rule DOES fail the teaches-copy-plus-one-word bullet**,
and it fails it on the coverage sub-rule alone (the other two sub-rules pass). Note the
failure is size-independent: with any non-empty `tw`, the copy prefix gives
`hits = |tw| ⇒ cov = 1.00`. Minimality check: deleting the trailing token flips
`novel` to `[]` and *also* fails, so one extra token is exactly what makes the copy
otherwise well-formed.

### The copy guard is defeated by two cheap perturbations (observed, not inferred)

1. **Reorder.** Bullet keeps 100% of the teaches vocabulary but reverses it:
   row S781 teaches `frankincense resin burns slowly censer amber`, bullet
   `- Censer amber slowly burns resin frankincense smoke (S781)`.
   Greedy scan of `tw` over `bw = [censer, amber, slowly, burns, resin, frankincense, smoke]`
   finds only `frankincense` in order → `hits = 1`, `cov = 1/6 = 0.1667 < 0.80`,
   `inq = 4`, `novel = ['smoke']` → **RESTATE PASS**. S781 is absent from the leg's
   `bad` list in the fixture run, confirming the pass at leg level. The bullet is a
   pure teaches-vocabulary copy plus one word; the metric reads reordering as novelty
   because coverage is order-sensitive and one-directional.
2. **Degenerate teaches cell.** S786 teaches `it is on the go to be up` →
   `tw = []` → `in_order_coverage` returns `0.0` (line 129 `if clause_words else 0.0`),
   `novel` is everything, so *any* bullet carrying 3 quote words passes. Bullet
   `- Frankincense resin slowly censer (S786)` → observed **RESTATE PASS** (S786 absent
   from `bad`). Nothing in ROWS checks that the teaches cell carries content words.

---

## Item 2 — two rows whose URLs differ only in query: LINK verdict

### Crafted strings

```
| S779 | Synthetic fixture source, S779 page - https://example.org/herbs?batch=resin ; https://web.archive.org/web/20260101000000id_/https://example.org/herbs?batch=resin . | docs | B | fixture scope | … | … | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md |
| S780 | Synthetic fixture source, S780 page - https://example.org/herbs?batch=smoke ; https://web.archive.org/web/20260101000000id_/https://example.org/herbs?batch=smoke . | docs | B | fixture scope | … | … | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md |
```

### Observed

```
LINK PASS bad=[]
```

`norm_url` (lines 90–105) **keeps the query**:

```
norm_url("https://example.org/herbs?batch=resin") = "https://example.org/herbs?batch=resin"
norm_url("https://example.org/herbs?batch=smoke") = "https://example.org/herbs?batch=smoke"
→ not equal, so neither `dup-base` nor `dup-S…` fires (lines 262–269)
```

**This is a defect against the counter's own stated norm.** `accept-c.py:21` says LINK
is "(scheme/www/query-insensitive)"; `norm_url:104` appends `?{parsed.query}` when a
query exists. The instrument contradicts itself, and the code path is the one that
decides the leg. `reports/round-66/claims.json` LINK leg text ("no new row's normalized
live URL collides with any base row or another new row") is silent on normalization, so
the only readable contract in the counter is the docstring that the code violates.

The leg is not dead — an *exact* base-URL duplicate is caught. Fixture variant with
S800 live URL = `https://glottolog.org/about.html` (the base S001 URL):

```
LINK FAIL bad=['S800:dup-base']
```

while in the same run S779/S780 (query-only variants) are **not** listed, and the
scheme variant S799 = `http://glottolog.org/about.html` is also **not** listed
(`norm_url` is scheme-sensitive too: `http`-vs-`https` are distinct identities,
`https://example.org:443/x` vs `https://example.org/x` likewise). Practical
consequence: 24 "distinct" rows can be one page behind 24 query strings and LINK prints
PASS, so the claim's 24-distinct-source leg is not actually verified.

Two further evasions of the same leg (both verified against `row_urls`, lines 108–113):

- **Archive-only source cell** → `live = []` → `row_urls` returns `None` → the row is
  dropped from `live_urls`, so it is invisible to LINK *and* to HOSTS, while CAPTURE
  still passes (the `web.archive.org` URL is present). Verified:
  `row_urls("… https://web.archive.org/web/20260101000000id_/https://www.eriebasin.com/ .") = None`,
  `CAPTURE_RE` matches.
- **First-live-URL-wins**: a row that lists a harmless mirror first and the true
  duplicate second is keyed on the mirror only. Verified: `row_urls` over
  `https://mirror.example.net/frankincense ; https://example.org/herbs?batch=resin`
  returns the mirror.

---

## Item 3 — 8-word bullet, ≥3 in-order quote words, teaches coverage "0.79" must PASS

### 0.79 is arithmetically unreachable with an 8-content-word bullet

`cov = hits/|tw|` and each hit consumes one `bw` position, so `hits ≤ |bw| = 8`.
For `cov = 0.79 = 79/100` we need `|tw| = 100·hits/79`, integral only when `79 | hits`,
i.e. `hits ≥ 79 > 8`. **No 8-word bullet can produce exactly 0.79.** The reachable
neighbours are `7/9 = 0.7778` (pass) and `8/10 = 0.8000` (fail) — so the criterion is
tested at its true boundary rather than at an impossible value.

### Crafted strings (the pass case)

Row S778, teaches = 9 content words, quote shares 4:

```
| S778 | Synthetic fixture source, S778 page - https://perfume.example.net/temple ; https://web.archive.org/web/20260101000000id_/https://perfume.example.net/temple . | docs | B | fixture scope | page body: "frankincense resin slowly in the censer" | frankincense resin burns slowly censer temple amber distillation proportion | mined | 2026-10-24 | 180d | corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md |
```

Bullet (8 content words; quote words in order: frankincense → resin → slowly → censer):

```
- Frankincense resin burns slowly censer temple amber smoke (S778)
```

Worksheet:

- `bw` = `[frankincense, resin, burns, slowly, censer, temple, amber, smoke]` (8)
- `tw` = `[frankincense, resin, burns, slowly, censer, temple, amber, distillation, proportion]` (9)
- greedy hits = 7 (all but `distillation`, `proportion`) → `cov = 7/9 = 0.7778 < 0.80`
- `inq = 4` (≥3 ✓, and in quote order), `novel = ['smoke']` (✓)

**Expected and observed leg verdict: RESTATE PASS** — S778 does not appear in
`bad` in either fixture run (`bad` is built in NEW_IDS order, and S779 is the first
entry after S777, so S778's absence is not truncation).

### Boundary pair (no false negative at 0.80)

Same 8-word bullet, teaches = `frankincense resin burns slowly censer temple amber smoke distillation proportion`
(10 words, 8 hits): `cov = 8/10 = 0.8000 ≥ 0.80` → **RESTATE FAIL** — correct, since
`< 0.8` is strict and the leg is an *exclusion* threshold. Both boundary values were
observed (function-level): `cov=0.7778 → PASS`, `cov=0.8000 → FAIL`.

So the answer to item 3 is: a bullet at 0.78 passes with no false positive, and 0.79
cannot be constructed; the strict `<` comparison is on the correct side.

---

## Findings by severity

**HIGH-1 — LINK is query-sensitive, contradicting its own stated norm.**
`accept-c.py:21` promises query-insensitivity; `norm_url:104` keeps `?query`; `LINK`
(`:261–269`) therefore prints `bad=[]` for `…/herbs?batch=resin` vs `…/herbs?batch=smoke`.
Observed `LINK PASS bad=[]` with both rows present, while an exact duplicate prints
`LINK FAIL bad=['S800:dup-base']`. A PASS here is a false stamp on the claim's
distinct-source leg. Fix before signing: drop the query (and normalize scheme +
default port) inside `norm_url`, or restate claim C's LINK leg explicitly in the round
records — the two cannot both stand as written.

**HIGH-2 — HOSTS counts netloc, not registrable host.** `:254` adds
`urlparse(u).netloc.lower()`; no `www.` strip and no eTLD+1 collapse. Fixture with
`host782…host800.example.com` produced `HOSTS PASS hosts=22` from essentially one
domain, and `www.example.org` + `example.org` count as 2 (`hosts={'www.example.org','example.org'}`).
The "≥10 distinct normalized hosts" leg is trivially satisfiable and cannot distinguish
10 real publishers from 10 subdomains of one.

**MED-3 — `inq` is unordered and duplicate-inflating, though documented as "in-order".**
`:243` is `sum(1 for w in qw if w in bw)` — set membership over the quote's word list,
no order, and repeated quote words count repeatedly. A quote `"amber amber amber"` with
the 4-word bullet `- Amber trade route text (S784)` yields `inq = 3` and passes the ≥3
check with **one distinct word**. The claim text (`claims.json`, RESTATE leg) says
"in-order content words from its row's anchor quote"; the code does not test order.

**MED-4 — RESTATE inspects only the citation line, so a teaches copy elsewhere is
invisible.** `entry_bullets` (`:225–229`) keys on lines containing `(S###)`. Fixture S785:
the teaches cell pasted verbatim as an unmarked prose line plus a compliant 8-word
bullet → observed **RESTATE PASS** (S785 absent from `bad`) although the entry contains
the teaches cell at 100% coverage. The leg's purpose ("bullet not a copy of teaches") is
enforced on one line, not on the entry.

**MED-5 — degenerate teaches cell makes RESTATE vacuous.** `tw = []` → `cov = 0.0`
(`:124`), `novel` trivially non-empty, so any bullet with 3 quote words passes; observed
PASS for S786. ROWS (`:192–220`) checks cells/kind/tier/status/opened/used-by but never
that the teaches cell carries content words.

**MED-6 — archive-only source cells are invisible to LINK and HOSTS while CAPTURE
passes.** `row_urls` (`:108–113`) returns `None` when every URL is `web.archive.org`;
CAPTURE (`:301–311`) only requires a capture to be present. A row can therefore evade
both the dedupe and the host-span legs; a row can equally hide a duplicate behind a
different-first live URL (first-live-URL-wins).

**MED-7 — `--root` does not scope the revision probe.** `mv = subprocess.run(["git",
"rev-parse", "main"])` (`:137–138`) inherits the caller's cwd, while NOHARM correctly
uses `-C root` (`:281`). Running `accept-c.py --root <repo>` from any other directory
prints a `# measured revision` from the wrong repo, so the receipt can attribute the
verdict to a revision it never measured. Observed in the sandbox: the printed revision
came from the cwd repo, not from `--root`.

**LOW-8 — norm_url is also scheme- and default-port-sensitive.** `http://` vs `https://`
and `https://host:443/x` vs `https://host/x` are distinct identities, contradicting
"scheme-insensitive" in `:21`. Rows can duplicate a base source across an http/https
flip and LINK prints PASS.

**Positive checks (no finding).** Counter sha matches the dry-run receipt
(`dry-run-c.txt:1`, `0726b4bc…`), so the frozen instrument has not drifted since the
pre-data control. The naive teaches copy + one word does fail (cov 1.00). Exact-URL
duplicates are caught (`S800:dup-base`). Base dry-run fails all data legs
(`ACCEPT-C-66: FAIL`) as declared in `controls-c.txt`.

**Control gap that explains why these survived the gate.** `controls-c.txt:4` declares
LINK "(dependent)" and the base dry-run prints `LINK PASS bad=[]`; a do-nothing tree
therefore cannot distinguish a live LINK from a dead or partial one. `dry-run-c.txt`
shows `HOSTS FAIL hosts=0` but nothing exercises a near-collision (query/scheme variant)
or a subdomain-padded host set, so HIGH-1/HIGH-2 passed the pre-data control unobserved.
Recommend adding a positive fixture to the control (query-variant row must fail LINK;
one-domain subdomain set must fail HOSTS) before the counter is signed.

---

## Residual risk and verification gaps

- No real round-66 draft rows exist at the tip (`corpus/SOURCES.md` ends at S776; the
  scent entry is absent), so all verdicts above are from synthetic fixture rows. They
  exercise the counter's code paths exactly, but they cannot tell me whether the
  *integrated* S777–S800 rows will actually be query variants or subdomain-padded — only
  that the legs would not catch them if they were. `[INFERENCE]` on the integrated data.
- I did not run the SWEEP leg against a fixture matching `sweep.py`'s row/file census
  (`SWEEP FAIL exit=1 readme_sha256 …` in my fixture was expected: my entry set is not a
  census-consistent corpus). That leg is outside my assignment and its failure is an
  artifact of the fixture, not a finding.
- I did not test `git show BASE:corpus/SOURCES.md` failure paths beyond the empty-tree
  control; the `return 2` input-error path is unexercised here.
- Fixture location `/tmp/r66-rc-clone` is disposable and outside the lane; lane jj/git
  state, index, and fleet repo untouched. No tool installs were needed (python3 + stdlib
  only), so no tooling record applies.

## Reproduction (disposable, outside the lane)

```
git clone /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/r66-rc-clone
mkdir -p /tmp/r66-rc-clone/reports/round-66
cp reports/round-66/accept-c.py /tmp/r66-rc-clone/reports/round-66/
# append the crafted 11-cell rows above to corpus/SOURCES.md, write the entry bullets,
# then:
cd /tmp/r66-rc-clone && python3 reports/round-66/accept-c.py --root .
```

Report: .ufo/waves/round-66/w1/RevCounterC.md
