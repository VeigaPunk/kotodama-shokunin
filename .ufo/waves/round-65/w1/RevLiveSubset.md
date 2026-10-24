# RevLiveSubset — attack on claim C's LIVE leg (round 65)

Seat: reviewer (attack), read-only. Instruments attacked, as assigned:
`reports/round-65/accept-c.py` LIVE leg and `reports/round-61/reopen-quote.py`
(the pinned locator). Context read before attacking: `reports/round-65/claims.json`,
`telemetry/dry-run-c.txt`, `telemetry/controls-c.txt`, `telemetry/census-start.txt`,
`corpus/QUALITY.md` criterion 16, `tools/reopen-row.py`, `reports/round-62/locate-control.py`.

All `accept-c.py` line citations below are re-verified against revision 3 at
sha256 `bc35de5ca421a70b72064632fd1bea088890296719033eca277a0cb4033f55f2`
(481 lines, mtime 2026-10-24 01:58:03).

## Mid-review instrument motion (observed, not a defect claim)

`accept-c.py` changed **twice during this review**. My first read (01:52) was 448 lines with
`LIVE_IDS` at :79; rev2/2a landed at 01:56:46 (467 lines); rev3 landed at 01:58:03 (481
lines, sha above). `claims.json` moved at 01:55:32 and `controls-c.txt` at 01:56. The
in-file history (:52-58) records: rev2 `RESTATE` requires `len(cited) == len(NEW_IDS)`
(closing the vacuous zero-citation PASS routed by `w1/CriticControlC.md`); rev2a `NOHARM`
tolerates the pre-declared Ca R7 land; rev3 `HOSTS` strips userinfo so it cannot mask the
host (`host = host.rsplit("@", 1)[-1]`). The frozen predicate sentence and the leg list in
`claims.json` are unchanged, so the predicate still holds.

The **LIVE leg itself is substantively unchanged** across all three revisions — same pin,
same 3×20 s retries, same `startswith("LOCATED")` check and same discard of the locating
URL — only line numbers moved (:440-473). The pinned locator is untouched: its working-tree
sha256 `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390`
still equals `git show BASE:reports/round-61/reopen-quote.py`.

Commit state matters here: `reports/round-65/` is committed at `f107e84` (accept-c rev2)
and `git status` shows `M reports/round-65/accept-c.py` (plus `accept-o.py`, `accept-ca.py`)
— the counter is being edited on top of its commit while seats run. Only the *locator* is
pinned; the counter's own bytes are pinned by nothing (M3).

## What I ran / did not run

- Ran: static read of both instruments with line numbers; a sha256 pin comparison
  (working tree vs `git show BASE:`); an in-memory probe that imports the pinned locator
  and feeds it synthetic HTML (no files written, no network); arithmetic on `LIVE_IDS`;
  read-only git queries (`git replace -l`, `git check-attr -a`, `git config core.autocrlf`,
  `git status`, `git log`).
- Did not run: `accept-c.py` (no row data exists yet — `.ufo/waves/round-65/rows/` was
  empty per `w1/ScoutReopenA.md`), neither locator against the network, and no fixture run
  of the LIVE leg. No live URL of S750–S775 was fetched by this seat, so no claim below
  rests on a fetch I made.
- No tool installed or updated (nothing was needed).

## The three assigned questions

### (1) CAPTION_ONLY — can a caption-only quote still print LOCATED? Does the pinned locator separate it?

**Yes, and no.** The pinned locator has no notion of caption or chrome material:

- `reports/round-61/reopen-quote.py:64-70` — `handle_starttag` suppresses only
  `script`/`style`; every other element's text is kept, including `<figcaption>`,
  `<caption>`, `<nav>`, `<footer>`.
- `:72-75` — `handle_data` appends every text node.
- `:138-143` — `locate_in` is whole-document containment
  (`" "+want+" " in " "+normalise(text)+" "`).
- `:110` / `_strings` — a JSON or `{`/`[` body is flattened into *all* of its string
  values, so API `caption`/`credit`/`description` fields are body text.
- `grep -ci 'caption'` on `reports/round-60/reopen-quote.py` and
  `reports/round-61/reopen-quote.py` returns **0** for both.

Probe against the pinned file (imported as a module, in memory):

| fixture string (inside an otherwise unrelated page) | words | `locate_in` |
|---|---|---|
| `<figcaption>Photo: athletes celebrate after the final whistle at the national stadium</figcaption>` | 11 | **True** |
| `<caption>Table 2: medal standings by nation after the closing ceremony session</caption>` | 11 | **True** |
| `<nav>Skip to content Subscribe to our newsletter for weekly updates on all sports</nav>` | 13 | **True** |
| `<footer>Copyright the sports desk All rights reserved worldwide under applicable law</footer>` | 11 | **True** |
| body paragraph on the row's actual topic | 10 | True |
| `alt`-only string (any length) | — | **False** — `alt` is not in the text stream at all |

So the pinned locator's false-accept set is text-node captions **and** site chrome
(nav/footer/breadcrumb), and its false-reject set is attribute-only quotations. Only
`MIN_WORDS = 8` (`reopen-quote.py:147`) and accept-c's 8–25 word band
(`accept-c.py:256-258`) constrain the quote at all; nothing anywhere separates caption from body.

This is not a violation of the claim's literal sentence — `accept-c.py:43-46` promises only
"each prints LOCATED" — but it is a violation of the lane's own pre-existing standard:

- `corpus/QUALITY.md:49` criterion 16 (appended 2026-10-23, i.e. **before** this wave):
  "A quotation found only in a caption, a figure caption, a gallery or thumbnail overlay,
  or an alt/title/aria-label/content/data-* attribute is not body text: re-scope the entry
  line as a caption or replace the quotation. Check: `python3 -B tools/reopen-row.py <S-id>`
  prints `CAPTION_ONLY` … Shown able to fail: on round-61 bytes S665's entry line states its
  caption as fact while `tools/reopen-row.py --passes 2 --gap 30 S665` prints
  `ROW S665 CAPTION_ONLY`."
- `tools/reopen-row.py:13-17,711` implements exactly that verdict split, and its safety hold
  was lifted at `dd81fd29` (round 63) per `corpus/QUALITY.md:49`.

Claim C pins the **predecessor** that criterion 16 replaced (`accept-c.py:79`,
`LOCATOR = "reports/round-61/reopen-quote.py"`; pin intent at `:43-46`). Consequence:
**ACCEPT-C-65 can print `LIVE PASS` with 6/6 `LOCATED` on caption-only or site-chrome
quotations.** A PASS must not be read as body-scoped sourcing; the round-65 entry is still
bound by criterion 16, and no leg in accept-c checks it (SWEEP checks rows==files and the
README topic only, `accept-c.py:421-436`).

Limitation of the obvious remedy: `tools/reopen-row.py:350-365` returns `(text, "")` for
non-HTML bodies, so a **JSON API's `caption` field is body text under both tools**. The
caption remedy is mechanically real for HTML only; the letter of criterion 16 is unenforced
for JSON sources by either tool.

### (2) The every-5th subset — pattern, and does one host serving 3 of 6 escape?

Pattern over S750–S775 (26 ids): sampled positions **{0, 5, 10, 15, 20, 25}** →
`S750, S755, S760, S765, S770, S775`; constant step 5, both endpoints included,
**6/26 = 23.1 %**; unsampled (20): `S751-S754, S756-S759, S761-S764, S766-S769, S771-S774`.
Round 64 used the same arithmetic (`reports/round-64/accept-c.py:81`,
`[f"S{n}" for n in range(718,744) if (n-717)%5==1]`); round 65 hardcodes the literal list
(`accept-c.py:83`), which equals the derived formula `(n-750)%5 == 0`.

**Yes, one host serving 3 of 6 escapes.** The subset is a systematic sample of *id space*,
and nothing else:

- Ids follow append order — `APPEND` only requires base rows preserved plus exactly 26
  appended (`accept-c.py:398-403`). The mining seat chooses which rows occupy the sampled
  slots, and the sampled slots are public pre-data (claims.json + on-disk counter).
- No host-diversity rule exists: `HOSTS` rejects ten hard-coded placeholder names
  (`:371-383`); `LINK` dedups **normalized URLs**, not hosts (`:386-395`). One host may own
  all 26 rows with 26 distinct paths and pass. Rev3's userinfo strip (`:379`) closes
  placeholder masking, not concentration.
- The LIVE receipt has no host column at all (`:473` prints `subset=… bad=[]`).

Two distinct escapes, both real:
(i) **shared-host template defect** — if a host repeats chrome, or serves a soft-404 /
wrong-article shell, its sampled rows all locate on the same sentences (finding 1);
the sample treats rows as independent units while the failure unit is the host.
(ii) **unsampled rows** — the other 20 rows (76.9 %) receive *zero* live evidence; any
defect confined to them is invisible, and the seat controls whether a suspect host's rows
land there. `ROWS`/`RESTATE`/`LINK` never fetch, so for 20 rows only quote length, URL
identity and lexical overlap are tested.

**Recommendation: keep the subset frozen for round 65 — do not change it.** Reasons:
the predicate sentence and the LIVE description are in `claims.json` and in the dry-run
receipt; re-drawing the sample after rows exist is a data-dependent re-draw, the exact
class the lane bans ("frozen-predicate rule: the predicate sentence never changes",
claims.json `controls`); and a wider sample would not fix the actual gap, which is host
stratification, not coverage of ids.

Round-66 pre-data design (not applied here):
1. stratify the sample by registrable host (at least one row per host, then the every-5th
   rule inside each stratum), or budget a full sweep;
2. add two **non-network** legs — `HOSTMIX` (≥ N distinct registrable hosts; no host above
   a set share of 26) and `QUOTEUNIQ` (no two rows' normalised anchor quotes are equal);
   both are counting legs over the registry, so they cost no fetches and cannot be
   satisfied by a fetch flake. They close the arithmetic class only — a footer with a
   per-page breadcrumb defeats `QUOTEUNIQ`, so these complement, not replace, review;
3. print the locating URL and require it to normalize-equal the row's live URL (finding 3);
4. run the locator from a temp copy of the pinned bytes and pass a frozen registry snapshot
   (finding 5).

### (3) The pin resolves from BASE at runtime — trace an edit to `reopen-quote.py` mid-round

Code path (`accept-c.py:440-449`): read the working-tree locator bytes (`:442`), sha256
(`:443`); `git show BASE:LOCATOR` (`:446-447`), sha256 → `pin` (`:448`, or the literal
`"unresolvable"` when git produces no bytes); on mismatch append to `live_bad` (`:449-450`).
Execution (`:459`) is `[sys.executable, "-B", LOCATOR]` with `cwd=root`, i.e. the
**working-tree file**, not a copy of the base blob.

Trace:
1. **An edit makes the claim fail, fail-closed.** `digest != pin` → `LIVE FAIL` →
   `ACCEPT-C-65: FAIL`, exit 1. No exception path, no silent pass. Measured today:
   working-tree and base both sha256 `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390`
   (verified with `sha256sum` and `git show BASE:… | sha256sum`), so the pin is currently honest.
2. **The pin is a detector, not a sandbox.** On mismatch the loop still runs all six rows
   (`:450-473`) against the *edited* file; its verdicts are discarded but its code executes
   with repo privileges. `accept-c.py` itself is pinned by nothing; only the locator is.
3. **Check-then-use (TOCTOU).** The hash is taken once, before the loop. An edit between
   `:442` and any `:459` is invisible, and the window is at least the whole LIVE leg
   (6 rows × up to 3 attempts × 1500 s each, `:457-470`). A mid-run edit yields
   `ACCEPT-C-65: PASS` with unpinned bytes having produced the LOCATED lines. The two
   mid-review edits documented above show that writes to this directory do happen while
   seats are running.
4. **The row data is not pinned either.** accept-c reads `corpus/SOURCES.md` once for
   `ROWS`/`RESTATE` (`:205`), but the locator re-opens the registry per row
   (`reopen-quote.py:236`). A row's anchor or source cell can therefore change after
   `ROWS`/`RESTATE` validated it and before its `LOCATE`; with seats writing rows during
   the wave this is a live race, not a theoretical one.
5. **`git show` return code is unchecked** (`:446-448`): on failure `pin="unresolvable"`,
   the leg reports `locator_sha=…!=unresolvable` — a tamper-looking detail for what is an
   input error. Contrast the registry read, which returns 2 on the same class of failure
   (`:205-214`). A shallow clone is caught earlier by the registry read, so the
   misdiagnosis is confined to a locator-only resolution failure.
6. **The pin's trust root is the local repo.** `git show` honours replacement objects and
   grafts unless told otherwise, and `accept-c.py` passes neither `--no-replace-objects`
   nor `GIT_NO_REPLACE_OBJECTS`. A local `git replace <BASE> <crafted>` would make
   `SHA256(git show BASE:LOCATOR)` hash the crafted locator, so `digest == pin` with an
   edited file — and `ROWS`/`APPEND` read the base registry through the same channel.
   [INFERENCE on git's default replace-ref behaviour; I did not demonstrate it, because
   that requires mutating lane git state, which this seat is forbidden to do. Checked
   read-only: `git replace -l` is empty and no grafts file is in use.]
7. **Portability.** `open(...,"rb")` compares checkout bytes with blob bytes; with
   `core.autocrlf` or an `eol` attribute set, the same tree would FAIL LIVE spuriously.
   Checked here: `git check-attr -a -- reports/round-61/reopen-quote.py` prints nothing and
   `core.autocrlf` is unset, so today the comparison is byte-honest.
8. **Consequence for the wave.** Because the pin is to BASE, *any* locator edit — even a
   comment — cannot ship this round; the only legal state is bit-identical base bytes. If a
   sampled row fails to locate because of a locator defect (UA-blocked host, paywall), the
   honest outcome is FAIL, not a repaired locator. A scribe who edits the locator for a
   pre-filing check and reverts bit-exactly leaves no trace: the final PASS is honest about
   the final bytes, but the pre-filing evidence is unreceipted.
9. **Sub-case, stored archive only.** Each new row must carry a same-page capture
   (`:260-276`), and the locator tries the live URL first but falls back to the archive
   (`reopen-quote.py:200`). For a persistently dead live URL, `LOCATED` attests the 2026
   archive, not the live page. Intended by the claim, but "live" is a misnomer for those
   rows and the receipt does not say which URL answered.

## Findings by severity

### HIGH

**H1 — CAPTION_ONLY / chrome quotes pass the pinned locator; the lane's own criterion 16
and `tools/reopen-row.py` say they must not.** Evidence: `reopen-quote.py:64-75,110,138-143`;
`grep -ci caption` = 0 for round-60/61; the probe table above; `accept-c.py:256-258,43-46,79`;
`corpus/QUALITY.md:49` criterion 16 with its S665 shown-able-to-fail case;
`tools/reopen-row.py:13-17,711`. Impact: `LIVE PASS` is consistent with six caption-only or
footer-only quotations; the predicate cannot distinguish them, and the claim's review-only
list does not name caption scope. The round-65 entry is still bound by criterion 16 as a
quality matter, unenforced by any leg. **Do not change the predicate or the locator
mid-round.** Recommend as *review* (outside the frozen claim): run
`python3 -B tools/reopen-row.py` over the 26 ids and require `ROW <id> LOCATED` for each
(exit 0 means every row located, `tools/reopen-row.py:860-862`); treat any `CAPTION_ONLY`
as a quality failure of the entry, not of the counter. Carry "LIVE attests page containment,
not body scope" into the L1 handoff. Round 66 pre-data: pin the body/caption-separating tool
(or both) and require verdict `LOCATED`, not merely exit 0 of a filtered subset.

**H2 — One sentence of site chrome can source many rows; no quote-uniqueness or host-mix
rule exists.** `ROWS` constrains the anchor quote only by word count (`accept-c.py:256-258`);
`HOSTS` names ten placeholders (`:371-383`); `LINK` dedups normalized URLs, not hosts
(`:386-395`); `teaches` is authored by the seat and never fetched, so `RESTATE` binds
bullet↔row, not row↔page. A 26-row "coverage" built from one host's footer/nav sentence —
or from 26 near-identical chrome variants — can be green end to end: `ROWS` (length),
`LINK` (distinct URLs), `RESTATE` (≥3 in-order content words from the chrome sentence + one
novel word), `LIVE` (6/6 containment). Nothing in the frozen predicate can fail it.
Recommendation: close by review now (the reopen-row sweep above plus a host tally of the 26
rows recorded in the receipt); close structurally in round 66 with `HOSTMIX` and `QUOTEUNIQ`
(counting legs, no fetches) — with the stated limitation that per-page chrome variants
defeat `QUOTEUNIQ`.

### MEDIUM

**M1 — `LOCATED` can be earned by a URL that `ROWS`/`LINK` never validated, and the passing
URL is discarded.** The locator tries up to four source-cell URLs in order
(`reopen-quote.py:200`, `row_target` at `:226-229`); accept-c validates only `urls[0]` plus
the requirement that the **last** URL is a same-page capture of `urls[0]`
(`accept-c.py:260-276`). A row may add a second live URL that locates while `urls[0]`'s
quote is absent; the same-page-capture invariant then applies to a URL that never answered
the question. accept-c checks only the output prefix (`:464`) and records `detail` only on
failure (`:469-473`), so a PASS receipt shows no locating URL at all. Mid-round: the L1 can
recover this by running the locator on the six ids manually and recording the URL it names.
Round 66: print the locating URL into the receipt and require `norm_url(locating_url) ==
norm_url(live_urls[sid])`.

**M2 — criterion 16's paired budget control is absent for claim C.** Criterion 16 requires
that a live-fetch budget "has its own paired control (one case that recovers inside the
budget, one that exhausts it)". `accept-c.py:457-470` states the budget (3 reopens, 20 s
apart, 1500 s each) but the pre-data telemetry has no LIVE control: `controls-c.txt` covers
only RESTATE/ROWS fixtures, and `dry-run-c.txt` exercises only the base `no_row` path
(`LIVE FAIL … bad=['S750:no_row', …]`). The lane already has the exact artefact:
`reports/round-62/locate-control.py` imports `reports/round-61/reopen-quote.py` unchanged
and virtualises `fetch`/`url_refusal`/`sleep` with RECOVER/EXHAUST/ABSENT/FIRSTOK/
CAPTUREOK/DNSFAIL cases — reusing it for C's 3×20 s shape is a fixture change, not a new
capability. Since the control is telemetry, not a leg, adding it does not alter the frozen
predicate sentence; whether that is still "pre-data" this late is an L1/operator call. If it
is not added, record the omission as a pre-data miss rather than implying the budget is
controlled.

**M3 (Q3, core) — the pin is checked once and guards neither the executed bytes nor the row
data.** Traced above: `accept-c.py:442-449` vs `:459`; registry re-read at
`reopen-quote.py:236` vs `accept-c.py:205`. A mid-run edit of the locator or of a row's
anchor leaves `ACCEPT-C-65: PASS`; the counter's own bytes are unpinned and were edited
twice during this review. Round 66: `git show BASE:LOCATOR` into a temp file, hash the temp
bytes, execute that path, and pass a snapshot registry (`--registry`-style) so the validated
bytes and the fetched bytes are the same bytes.

### LOW

**L1 — pin diagnostics and trust root.** Unchecked `git show` return code (`:446-448`) makes
an input failure read as tampering, where the sibling registry read exits 2 (`:205-214`).
Replace refs/grafts are honoured by the pin command; today `git replace -l` is empty. Round
66: `git --no-replace-objects show` (or `GIT_NO_REPLACE_OBJECTS=1`) and a distinct
`ACCEPT_C_INPUT_ERROR locator` exit.

**L2 — the retry budget's worst case is hours, not seconds.** 6 rows × 3 attempts × 1500 s
per locator call (`:457-470`), with no global budget. Each locator call also retries fetches
3× internally (`reopen-quote.py:fetch`), so one sampled row can cost ~9 requests over
~25 minutes. Criterion 16 asks for a bounded budget; the stated budget is technically
stated but operationally unbounded for a reviewer's rerun. Round 66: a wall budget for the
LIVE leg and `start_new_session` process-group kill (round-62 `accept-o`'s tool contract
already requires "tool runs own a process group").

**L3 — adjacent receipts and docs (not LIVE), for the L1's integration hygiene.**
`telemetry/controls-c.txt` (01:56 revision) now annotates control 1's `exit=0` as a pipeline
status with the true `counter exit=1`, but **control 2 is left uncorrected**: it still ends
`ACCEPT-C-65: FAIL` followed by `exit=0`, and still shows only 6 of the 10 legs (no `ONEID`,
`HOSTS`, `SWEEP`, `LIVE`) with no filtering marker. The same receipt's note concedes the
round-65 `teaches_nearcopy` rule was *not* the rule that fired (`S750` failed `in_order=2`),
so revision 1's new rule has no forcing control on disk. Also, the `NOHARM` leg description
still reads "lists exactly the new entry" (`accept-c.py:39-40`) while the code now tolerates
the Ca R7 land (`:411-417`) — the revision history explains it, but the leg text is now
false. Finally `reports/round-65/__pycache__/accept-c.cpython-314.pyc` exists, compiled from
an earlier revision (its docstring citation sits at line 47 where the current file has it at
:43-44) — delete it before the integration commit so no stale bytecode rides into the land.

## Residual risk and verification gaps

- **The 26 rows' sourcing rests on 6 containment checks** (23.1 %), and those 6 accept
  caption and chrome text. The claim routes per-row support to review by design
  (`claims.json` `review_only`), but H1/H2 raise that review's weight: a green ACCEPT-C-65
  is consistent with caption-only sourcing and with a single-host corpus. The reopen-row
  sweep recommended in H1 is the smallest check that would close both for the *entry*.
- **JSON sources are outside both locators' caption separation** (`tools/reopen-row.py:350-365`
  returns `(text, "")`), so the criterion-16 remedy is HTML-only in practice.
- **Live-vs-archive:** for rows whose live URL is dead, `LOCATED` attests the 2026 archive
  capture; the receipt does not say which URL answered (M1).
- **Not demonstrated, therefore labelled:** git replace-ref subversion of the pin
  ([INFERENCE], forbidden to mutate lane git state); the probe's `<nav>`/`<footer>` cases
  are synthetic strings, not the actual S750–S775 pages; no row data existed at attack time.
- **Instrument motion:** the counter was edited twice under this review (rev2/2a at 01:56:46,
  rev3 at 01:58:03) and now carries uncommitted modifications on top of `f107e84`. My line
  numbers are against rev3 `bc35de5c…`; the frozen predicate does not pin the counter's own
  bytes — only the locator's.
- **Gaps this seat could not close:** no fixture execution of the LIVE leg (no rows), no
  network fetch of any sampled URL, and no independent re-open of the six ids — the rows
  directory was empty (`w1/ScoutReopenA.md`). If row fragments land later, the six sampled
  ids plus one id per host should be re-opened with `tools/reopen-row.py` and the URL printed.

## Bottom line

The LIVE leg does what its sentence says and fails closed on a locator edit. It does **not**
attest body-scoped quotations, does **not** bind the locating URL to the validated source,
does **not** constrain host concentration, and pins its bytes only at hash time. All four are
frozen-instrument limits, not draft defects; none is repairable mid-round without breaking the
frozen predicate. They are closable at review (reopen-row sweep + host tally + recorded
locating URLs) and structurally in round 66 (body/caption gate, host-stratified sample,
`HOSTMIX`/`QUOTEUNIQ`, frozen temp-copy execution, paired budget control).

Report: .ufo/waves/round-65/w1/RevLiveSubset.md
