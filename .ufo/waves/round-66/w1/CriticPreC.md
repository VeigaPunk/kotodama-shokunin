# CriticPreC — pre-data critique of ACCEPT-C-66

Scope: claim C (coverage, sourced) — `reports/round-66/claims.json` claim C +
`reports/round-66/accept-c.py` (332 lines, read in full). Frozen control
`telemetry/dry-run-c.txt` and `controls-c.txt` read; registry row shape
verified against `corpus/SOURCES.md` (11 cells:
id|source|kind|tier|scope|anchor|teaches|status|opened|recheck|used-by).

## (1) Do-nothing control: can a sourceless stub + 24 invented rows pass?

**Yes — mechanically, all 12 legs pass on fully fabricated data.** The frozen
control only proves the counter *fails on an empty tree*; it never proves it
cannot pass on a *fabricated* one. Leg-by-leg:

| Leg | Fabricated-tree result | Why |
|---|---|---|
| FILE | PASS | stub satisfies 1 H1 / ≤16 H2 / 0 H3 / ≤250 lines / `- topic:` trivially |
| SET | PASS | invented `| S777 | ...` rows, one line each |
| ROWS | PASS | every checked cell is self-asserted (kind enum, tier "A", mined, date, used-by substring) |
| ONEID | PASS | cite `(S###)` once per id in the stub |
| RESTATE | PASS | attacker writes the anchor quote *and* the bullet; copying ≥3 quote words, divergent teaches text (<0.8 coverage), one novel word needs no source access |
| HOSTS | PASS | 24 invented URLs across ≥10 fake hosts; nothing is fetched |
| LINK | PASS | invented URLs can't collide with base rows |
| APPEND | PASS | pure append |
| NOHARM | PASS | commit only the declared entry (+ games entry) |
| SWEEP | PASS | README row + footer counts updated to match disk |
| CAPTURE | PASS | append `; no-capture` or a regex-shaped fake capture |
| TOPIC | PASS | README row carries topic text verbatim |

**Strongest single counterexample — a row with no URL at all.** No leg requires
the source cell `c[1]` to contain a live URL. `ROWS` never checks for a URL;
`row_urls` returning `None` silently drops the id from `live_urls` (accept-c.py
:211-213), so `LINK` and `HOSTS` never see it; `CAPTURE` exempts it via the
`no-capture` substring (:308-309). A row whose source cell is literally
"Private collection, no-capture reason" passes every leg while being a
"mined, tier-A, used-by-the-entry" source that cites nothing. For a claim typed
**"learning claim (sourced)"**, the predicate enforces only *sourced-shaped*
rows; the sourcing truth is deferred entirely to the declared
`review_only: blind per-row support`. That is a declared tradeoff (claims.json
:35-38, :120), not a hidden defect — but the frozen predicate cannot by itself
distinguish a mined register from a fabricated one. The Rust judge should weigh
whether "sourced" as a claim *type* survives when every grounding property
(URL presence, capture liveness, quote-at-URL, tier justification) is
review-only.

## (2) Universal-clause audit — universals with no counter enumeration

- **"exactly 24 mined registry rows S777-S800" / "registry 701 → 725+ rows":**
  APPEND asserts `appended=N` but passes for any N (accept-c.py :275-278) and
  no leg bounds the appended set to NEW_IDS. Extra rows S801+, or rows with
  non-`S\d+` ids, or rows in non-row-shaped lines are appended unchecked —
  ROWS/LINK/CAPTURE iterate `NEW_IDS` only. "exactly 24" is enforced on the
  required-id side, not on the appended-set side; the "725+" claim is
  unverified.
- **"every registry row line present at base is unchanged":** APPEND diffs only
  lines matching `^\|\s*(S\d+)\s*\|` (:51,:172-173). Header, prose, and
  separator lines of SOURCES.md are outside the universal — they can be edited
  or deleted freely.
- **Global id uniqueness:** an attacker can append a *second* `| S500 | ...`
  row; the original line is still in `tip_set`, so APPEND stays true and SET
  only checks S777–S800. Duplicate-authority rows for old ids are unenforced.
- **used-by "names the entry":** substring test `ENTRY in c[10]` (:209) — a
  cell containing the path inside a longer string (e.g. `...-codes.md.bak`)
  passes; the row needn't be genuinely used (ONEID is the real binding, so this
  is minor).
- **RESTATE "in-order":** `inq` is an *unordered* membership count
  (`sum(1 for w in qw if w in bw)`, :243) — the claim/leg text says "in-order";
  a bullet with the quote words scrambled passes. Also `re.search` binds a line
  to its *first* `(S###)` only (:227): a line citing `(S777)` and `(S778)`
  attributes the whole line to S777, starving S778 of a bullet (bullets=0 →
  RESTATE fails S778 — a false-negative wart, not a bypass).
- **NOHARM universal:** only covers `corpus/knowledge` via `git diff BASE main`
  (:281-287). `corpus/README.md` and `corpus/SOURCES.md` edits are outside
  NOHARM (partially covered by SWEEP/APPEND). And the diff runs against ref
  `main` while registry reads come from the **working tree**
  (`open(root/REGISTRY)`, :164) — a mixed-revision measurement: uncommitted
  registry rows are judged but invisible to NOHARM, and uncommitted knowledge
  edits are invisible to the diff. At pre-integration run time this admits
  rows/files the committed record never contains.
- **HOSTS normalization inconsistency:** HOSTS uses raw lowercased netloc
  (:253-254); LINK's `norm_url` strips `www.` (:98-100). `www.foo.com` and
  `foo.com` count as **two** hosts for diversity but **one** identity for
  dedup — host-count inflation via `www.`/port variants.
- **LINK single-URL authority:** `row_urls` takes the *first* non-archive URL
  (:108-113). A row can carry a unique dummy URL first (satisfying LINK/HOSTS)
  and a base-duplicated URL second — a hidden duplicate. Query strings are
  retained (:104), so `?a=1` vs `?a=2` dodge dedup; paths are case-sensitive.
- **SWEEP string probe:** `"topic_mismatch" not in stdout.replace("topic_mismatch 0","")`
  (:296) is brittle to output-format drift (e.g. `topic_mismatch 00`).

## (3) Sizing: 24 rows from 12 scouts × 2 + 4 reject candidates

Arithmetically reachable: 12×2 = 24 mined + 4 rejects = 28 candidates, slack
exactly 4. But **zero slack beyond the 4 rejects** — any scout shortfall or a
5th rejected candidate breaks "exactly 24". Worse, the fixed quota creates
tier-inflation pressure: with 24 mandatory slots and tier self-asserted in
`c[3]` (counter cannot distinguish a real A/B from an inflated C), the
rational move under a shortfall is to promote marginal candidates. The counter
structurally cannot detect this; only `review_only` can.

## (4) CAPTURE leg: the 'no-capture' exemption is attackable twice over

- **Exemption is a bare substring**, not a reason: `"no-capture" in
  src.casefold() or "nocapture" in src.casefold()` (:308-309). The leg text in
  claims.json (:25) promises "an explicit no-capture **reason** string" — the
  code requires no reason at all, and even matches incidentally: a live URL
  like `https://example.com/nocapture/page` self-exempts.
- **Fabricated captures pass:** `CAPTURE_RE` accepts any
  `web.archive.org/web/\d{14}.../\S+` (:53-54) — a 14-digit garbage timestamp
  with a target URL that is *not* the row's live URL satisfies the leg; the
  claims.json leg text (:25) promises a "**same-page** web.archive.org
  capture" that the code never verifies. No liveness or target-match check.
- Unbounded: all 24 rows could be `no-capture` and the leg still passes.

## Impacted axes

Coverage (primary): the "sourced" property is enforced only as row *shape*;
the real sourcing axis is wholly delegated to review. Provenance: HOSTS/LINK
single-URL and `www.` inconsistency admit hidden duplicate authority and
inflated diversity. Record integrity: APPEND's row-line-only universal and
unbounded appended set weaken "exactly 24 / 701→725".

## Smallest safe corrections (ranked)

1. **ROWS: require ≥1 non-archive URL in `c[1]`** (`if not u: row_bad.append(...)`).
   Cheapest close of the strongest hole — every mined row must name a live URL.
2. **CAPTURE: bind capture target to live URL and bound the exemption** —
   require the capture's trailing URL to `norm_url`-equal the row's live URL,
   and require the exemption token plus ≥N chars of reason; optionally cap
   `no-capture` rows (e.g. ≤4). Alternative minimal fix: substring-exempt only
   if the token is not part of a URL in the cell.
3. **APPEND: bound the appended set** — assert every appended row's id ∈
   NEW_IDS ∪ declared disposition ids (S776 supersession + disposition rows),
   and assert global id uniqueness across tip rows (kills duplicate-S5xx and
   S801+ smuggling). Extend the diff to all lines, not just ROW_RE lines.
4. **LINK/HOSTS: single normalization + all-URL authority** — run `norm_url`
   on *every* non-archive URL in the cell (reject >1 live URL or check all for
   collision), and reuse `norm_url`'s host normalization in HOSTS so `www.`
   doesn't inflate the count.
5. **NOHARM/measurement coherence:** measure registry + knowledge from the same
   revision (e.g. `git show main:corpus/SOURCES.md`) or document that the
   counter must run post-commit; include `corpus/README.md` in the diff
   whitelist check.
6. **Doc/impl alignment:** either enforce in-order matching for RESTATE's
   quote-word test or fix the leg text; fix the claims.json CAPTURE leg text
   ("same-page") to match what the code checks, or add the check.

## Dependencies recorded

None blocking — all artifacts read at lane tip. No tools installed; no repo
mutation performed.

Report: .ufo/waves/round-66/w1/CriticPreC.md
