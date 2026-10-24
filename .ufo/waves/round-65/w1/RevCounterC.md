# RevCounterC — counter-attack on reports/round-65/accept-c.py

Seat: attack. Target: the frozen claim-C instrument, its legs, and its pre-data receipts.
Method: worksheet math on the instrument's own tokenizer, then an executed fixture run.

## Pin (what was actually attacked)

| item | value |
|---|---|
| instrument sha256 (self) | `ad5540fee4ba64728c51b1325e44fe40ef427c16cd449b48e424d02b019365d8` (revision 2, 19109 B) → re-verified at `e1aedafe782567fba05e1304c33cb57eb53c20276a0a7fa8cb14b8498ce12a51` (revision 2a, 20474 B) → **head at write time `bc35de5ca421a70b72064632fd1bea088890296719033eca277a0cb4033f55f2` (revision 3, 21235 B, 01:58:03)** |
| rev-3 delta (diff read, not re-run) | port guard in `norm_url`, ROWS dup scan seeded from base rows, HOSTS userinfo strip. RESTATE, LINK and `word_tokens`/`in_order_coverage` are **unchanged**, so HIGH-1, MEDIUM-1, MEDIUM-2, MEDIUM-3 and item 3 carry over by diff; item 1/2 verdicts were run at rev 2 and 2a |
| lane base | `17c32302c6845c8f164b985a8cb312d3181c8788` |
| fixture root | `/tmp/revc-65` @ `a0d8206` (copy of the control fixture `/tmp/k65-ctl`, mutated; commit is in the fixture repo, **not** in the lane) |
| receipts | `/tmp/revc-65-run.txt` (rev 2), `/tmp/revc-65-run2.txt` (rev 2a) — same verdicts on every leg in scope |
| line refs | revision 2a: `norm_url` 128-151, `in_order_coverage` 154-171, ROWS norm-dup 256, `clause == teaches` 318, nearcopy 348-349, RESTATE detail 355, `url in text` 379 |

Both runs printed, per leg: `FILE PASS`, `ROWS FAIL bad=['S752:norm_dup_of=S751']`,
`ONEID PASS ... cited_lines=26/26`, `RESTATE FAIL bad=['line5:S750:teaches_nearcopy=0.90',
'line12:S757:in_order=1', ... 'line18:S763:in_order=1']`, `HOSTS FAIL` (fixture placeholder
hosts only), `LINK PASS`, `APPEND PASS base=675 measured=701`, `NOHARM PASS`,
`SWEEP FAIL exit=1` (fixture has no README row). LIVE was not exercised (network; see gaps).

The RESTATE failure list is built in line order and truncated to the first 8 (`:355`). The
printed entries jump from line 5 to line 12, which **proves lines 6-11 raised no RESTATE
finding** — that is the evidence for every "PASS" claim below.

---

## Item 1 — minimal bullet = teaches cell + ONE trailing novel word

### Worksheet (instrument functions, `word_tokens` + `in_order_coverage`, `:101,:154`)

For a clause that is the teaches cell verbatim plus one novel token, with teaches length `T`:
`cov = T/(T+1)`. The leg fails iff `len(clause_tokens) >= 5 and cov >= 0.8` (`:348`).
`T/(T+1) >= 0.8 ⟺ T >= 4`, and `T+1 >= 5 ⟺ T >= 4` — **the length guard and the arithmetic
threshold coincide, so there is no gap at the short end and no boundary slack**. `T=4` gives
`cov = 0.80` exactly and `>=` fires.

Crafted (executed, teaches `games circulate shared rules that children negotiate practice locally`, 9 tokens):

```
- games circulate shared rules that children negotiate practice locally widely (S750)
```
`toks=10 cov=0.9000 content=9 quote_order=7 copy_run=7 novel={locally,widely}` →
**RESTATE FAIL `line5:S750:teaches_nearcopy=0.90`** — observed exactly as predicted, and it is
the *only* condition that fails (no `copy_run`, no `no_novel`, `in_order` = 7 ≥ 3). The
round-64 residual (trailing-word teaches copy) is **closed** for this shape.

### Plural variants (same fixture family)

One plural flip removes the hit for the flipped token, so `cov = (N-m)/N` with `N` clause
tokens and `m` unmatched tokens; the leg fails iff `m <= 0.2N`.

| crafted bullet | N | teach hits | cov | leg |
|---|---|---|---|---|
| `game circulate shared rules that children negotiate practice locally widely` (`games`→`game`) | 10 | 8 | 0.800 | FAIL (exact boundary) |
| same + one more filler word | 11 | 8 | 0.727 | **PASS** |
| `children negotiate shared rules while adult player circulate practice widely locally` (`players`→`player`) | 11 | 8 | 0.727 | **PASS** (verified, line 7, absent from the bad list) |
| teaches `…circulate practice across neighborhoods and generations` (13 tok) + 3 fillers | 16 | 13 | 0.812 | FAIL |
| same teaches + 4 fillers | 17 | 13 | 0.765 | **PASS** (verified, line 11) |

So a plural flip buys exactly one token of slack, and the pass/fail line is decided by a word
count, not by semantics: the same copied sentence fails at 10 tokens and passes at 11.

---

## HIGH-1 — the near-copy rule is diluted by padding, and the trailing-word fix does not cover it

`in_order_coverage` divides by the **clause** length, so any teaches copy embedded in a longer
clause scores `T/N`. The round-64 bypass appended one word (0.90, caught). Appending **three**
words drops it to 0.75 and passes:

```
teaches (row S751): children negotiate shared rules while adult players circulate practice      (9 tok)
bullet:  - children negotiate shared rules while adult players circulate practice across neighborhoods generations (S751)
```
`toks=12 cov=0.7500 content=12 quote_order=6 copy_run=3` → **RESTATE PASS** (verified: line 6
absent from the ordered bad list). This bullet reproduces the whole teaches cell verbatim and
only appends quote words, i.e. it is exactly the artifact the rule was written to reject.

Recipe (works at any teaches length): copy the teaches cell verbatim, append `ceil(0.25·T)`
tokens; for `T=13`, 4 tokens suffice (0.7647, verified line 11). No other leg compensates:
`clause == teaches` (`:318`) needs full equality, `copy_run` is measured against the **quote**
only, and `novel content word` is also measured against the quote, so teaches-derived words are
"novel" by construction. Severity high because the frozen claim says the taught residual is
closed and the leg description says ">= 80% in-order … FAIL", which reads as a paraphrase
guarantee it does not deliver.

Suggested repair (for the L1, not applied): test the teaches cell against the clause as a
*contained ordered subsequence with bounded padding* — e.g. reject when the teaches tokens occur
in order inside the clause and the non-matching clause tokens `<= max(2, 0.1·T)` — and measure
coverage over the teaches length, not the clause length.

## MEDIUM-1 — reordering defeats the rule (bag-of-words with order is still a copy)

Same teaches vocabulary, word order shuffled so the greedy subsequence match fails:

```
- rules games circulate shared that children negotiate practice locally (S755)
```
`toks=8 cov=0.6250 content=7 quote_order=4 copy_run=3 novel={locally}` → **RESTATE PASS**
(verified: line 10 absent from the bad list). Full reversal gives `cov=0.111` but trips
`in_order=1` on the quote, so the usable bypass is a partial shuffle that keeps 3+ quote-ordered
content words — trivially reachable, and it yields an ungrammatical bullet that passes every
mechanical leg. This is a `review_only` item ("sentence support"), so it is a residual rather
than a broken predicate: state it as such in the claim's residual list instead of claiming the
copy class is closed.

---

## Item 2 — two rows whose URLs differ only in query: ROWS norm-dup

Executed in the fixture (rows S751/S752, identical page, different query):

```
| S751 | Control Source — https://ctl-twin.example.org/same?page=1 ; web.archive.org/web/20260101000000id_/https://ctl-twin.example.org/same . | … |
| S752 | Control Source — https://ctl-twin.example.org/same?page=2 ; web.archive.org/web/20260101000000id_/https://ctl-twin.example.org/same . | … |
```
`norm_url` both → `https://ctl-twin.example.org/same`; ROWS prints
**`ROWS FAIL bad=['S752:norm_dup_of=S751']`** (`:256`), and the capture-original equality check
(`:274`) passes because the query is dropped there too. Predicate behaviour is as frozen.
Verified components: `norm_url(a) == norm_url(b) == "https://ctl-twin.example.org/same"` for
`https://www.smithsonianmag.com/arts-culture/history-of-chess-180980563/?utm_source=…` vs
`https://smithsonianmag.com/arts-culture/history-of-chess-180980563?ref=…`; `www.`, default
ports and trailing `/` are also collapsed.

Two concrete defects around that leg:

1. **MEDIUM-2 — LINK does not normalize, though the frozen text says it does.** The LINK
   docstring (`:34-36`) says "no two new rows share a query-aware-normalized URL" — that check
   is implemented inside ROWS (`:256`), so a reader validating "LINK PASS" believes LINK
   covered it. More seriously, LINK's two URL tests are **raw substring** (`hits` at `:377`,
   `url in text` at `:379`). Verified: with the entry carrying
   `Background reading: https://ctl-twin.example.org/same?utm_campaign=entry&page=1` while the
   row's live URL is `https://ctl-twin.example.org/same?page=1`, the run prints **`LINK PASS`** —
   the entry repeats the row's page (unmarked, no S-id) and escapes `url_in_entry`. Fix:
   normalize entry URLs with `norm_url` before the membership test, and move the norm-dup text
   into the ROWS docstring (or implement the dup check where the docstring says it lives).
2. **MEDIUM-3 — query-collision is a false positive for legitimately distinct documents.** The
   fixture pair `?page=1` / `?page=2` is two different documents under the frozen rule's own
   terminology ("query and fragment ignored"), and real round-65 sources use query-parameterized
   identity (`scielo.br/...?lang=en`, `?id=`). Any two mined rows distinguished only by a query
   collide and ROWS fails although both are valid; the builder's only recourse is to drop a
   legitimate source. The 26 real rows must be checked for this class before the leg is trusted
   (they are not on disk yet — see gaps).

---

## Item 3 — 8-word bullet, 3 in-order quote words, coverage "0.79": must PASS

**The premise needs a correction: 0.79 is not realizable.** Coverage divides by the clause token
count, so an 8-token bullet can only score `k/8` ∈ {0, .125, …, 1.0}. The maximum passing value
below the threshold is **6/8 = 0.75**; the next value, 7/8 = 0.875, fails. The threshold region
0.75 < cov < 0.875 is a dead band — the rule in practice permits ≤ 75% of the teaches cell for
8-token bullets, and the effective threshold drifts with bullet length (quantization error
`1/N`), which is why the frozen wording ">= 80%" overstates precision.

Two crafted fixtures, both verified **RESTATE PASS** (absent from the ordered bad list):

**(a) 8 tokens, cov 0.75, 6 in-order quote words** (row S753 teaches `games circulate shared
rules that children negotiate practice locally`):
```
- games circulate shared rules negotiate practice rituals freely (S753)
```
`toks=8 cov=0.7500 content=8 quote_order=6 copy_run=4 novel={rituals,freely}` → PASS.

**(b) 8 tokens, exactly 3 in-order quote words, cov 0.625** (row S754 teaches `players learn
rules by watching children negotiate practice`):
```
- players learn rules children internalize practice customs locally (S754)
```
`toks=8 cov=0.6250 content=8 quote_order=3 copy_run=1 novel={customs,internalize,learn,locally}`
→ PASS. This is the no-false-positive control the ticket asked for: it passes every RESTATE
condition without touching any threshold.

---

## MEDIUM-4 — stale pre-data receipts: the forcing controls predate the instrument they force

* `reports/round-65/telemetry/dry-run-c.txt` (01:20) prints `RESTATE PASS bad=[] lines=0` — the
  **vacuous pass that revision 2 was added to close** (`:56`, "RESTATE requires every new row
  cited"). The receipt therefore evidences revision 1 and, read literally, certifies a green
  RESTATE with zero cited lines. It carries no self-sha and no `lines=26/26` field.
* `reports/round-65/telemetry/controls-c.txt` (01:23) shows control 2 with `RESTATE … lines=26`
  (revision-1 format) and only 8 of 10 legs (no HOSTS, no SWEEP, no LIVE, no `ACCEPT-C-65` exit
  code line beyond the leg block), and no self-sha. The current instrument prints its own sha
  (`:175-176`) and `lines=26/26` (`:355`), so the control demonstrably ran a different program.
* The instrument was edited **three times during this review** (01:29 → 01:56:46 → 01:58:03:
  revision 2 → 2a → 3; 19109 → 20474 → 21235 B). Verdicts in scope are unchanged across all
  three (diff at rev 3 touches only `norm_url`'s port guard, the ROWS base seeding and the
  HOSTS userinfo strip), but "frozen" is not currently true of the file.

Required before the claim can score: regenerate the base dry-run and both forcing controls at
one pinned sha and keep the `# counter sha256 (self)` header in each receipt.

## LOW-1 — `norm_url` raised on malformed ports (found at rev 2/2a; **closed at rev 3**)

At rev 2/2a `parts.port` was read **outside** the `try` that wraps `urlsplit`. Verified:
`norm_url("https://www.smithsonianmag.com:99999/x")` → `ValueError: Port out of range 0-65535`;
`…:abc/x` → `ValueError: Port could not be cast to integer value`. In the ROWS loop that was an
uncaught traceback: exit 1, no `ACCEPT-C-65:` line, contradicting the documented "2 on unreadable
input" contract and stopping all 10 legs on one mistyped source cell. Revision 3 (`:140-144`)
guards it and fails closed to the stripped literal — confirmed by reading the rev-3 diff, not by
a rerun. The parser hazard that survives: `rstrip(".,;'")` does not strip `)` or `]`, so a URL in
parentheses (markdown link form) keeps the bracket in the path and produces a misleading
`capture_original_mismatch`.

## LOW-3 — rev 3's ROWS seeding is stronger than the frozen ROWS text (contract drift)

Revision 3 seeds `norm_seen` from every URL in every **base** row's source cell, so a new row
whose normalized URL matches a base row (including a base row's `web.archive.org` capture URL)
fails ROWS with `base:S###`. The frozen leg description (`:16-24`) only says "no two new rows
share a query-aware-normalized URL". Consequence: a legitimate re-mine of a source that a base
row already cites — including base rows that are `rejected`/`queued` (e.g. `S744`-`S749`) —
fails ROWS although the claim text does not forbid it, and the freeze record does not describe
the rule. Either the leg text or the claim must name the base-collision rule before scoring.

## LOW-2 — `urls[0]` assumes the live URL precedes the capture

`:266` takes the first `URL_RE` match in the source cell. Every current row writes
`<live> ; capture <archive>`, so this holds, but a row that puts the capture first would have
`live_urls[sid]` point at the archive URL and silently invert the HOSTS/LINK/capture checks
(`capture_original_mismatch` then reports the *live* URL as the mismatch). A cheap assertion
("first URL must not contain `web.archive.org`") would make the failure legible.

---

## Residual risk

* Bullets that are 75%-verbatim paraphrases of a teaches cell, and shuffled-order copies of it,
  pass every mechanical leg (HIGH-1, MEDIUM-1). Only `review_only` sentence-support review
  stands between these and the corpus.
* `copy_run > 12` remains the only verbatim guard against the quote and it permits a 12-token
  verbatim run; combined with HIGH-1 an entry can carry a 9-token teaches run and a 9-token
  quote run in the same bullet (my S751 bullet does exactly that: `copy_run=3` because the
  windows are non-contiguous, while 9 consecutive teaches tokens are copied).
* Query-aware dup detection is a verbatim-identity proxy: it cannot tell tracking parameters
  from pagination, so it is simultaneously bypassable at the entry (MEDIUM-2) and over-strict on
  real query-keyed sources (MEDIUM-3).

## Verification gaps

* **LIVE not exercised** (six-row network reopen, 3×1500 s budget). No claim about the locator
  pin or archived captures beyond the code read: `digest != pin` compares the working-tree
  locator to the base blob (`:420-429`), and the retry loop sleeps 20 s between three attempts.
* **Real 26 rows and entry do not exist at the lane tip** (pre-data). Every verdict here is
  about the instrument over crafted fixtures; the corpus-specific risks are MEDIUM-3 (real
  query-keyed URLs) and the unknown teaches-cell lengths (HIGH-1 scales with `T`).
* SWEEP read `exit=1` and HOSTS read `FAIL` on my fixture for fixture-only reasons (no README
  row, placeholder hosts); neither is a finding about the instrument.
* No `lsp` device is mounted in this seat (`xd://lsp` → "No such tool … Mounted devices:
  ast_edit, debug"), so caller/definition checks are the code reads cited above. I did not use
  text grep as semantic proof for any claim: every leg verdict above is either executed output
  from the pinned instrument or a computation with the instrument's own functions.

## Tools

None installed or upgraded (no package, uv, cargo or npm transaction in this seat).

Report: .ufo/waves/round-65/w1/RevCounterC.md
