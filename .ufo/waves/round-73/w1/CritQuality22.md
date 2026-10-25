# CritQuality22 — attack on the QUALITY 22 plan (UA-record clause)

Seat: critic, round 73 wave 1. Date 2026-10-25. Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Scope: the QUALITY 22 plan named in `reports/round-73/claims.json` `frontier_step.quality_candidate`
and briefed at `.ufo/waves/round-73/build-w1.py:46`. I do not edit the claim file, `corpus/QUALITY.md`,
the lesson, or any other seat's bytes. This report is my only write.

Read for this review: `corpus/QUALITY.md` criteria 10, 12, 13, 16, 21 (and 11, 15, 17, 19, 20 for the
check discipline); `corpus/lessons/round-72.md` `## Gate` + both `## Routed to round 73` sections;
`corpus/lessons/round-71.md` reject sweep; `corpus/lessons/round-6[1-4]*.md` reject lines;
`.ufo/waves/round-72/w1/ScoutCDXCanonical.md` §1 and `ScoutCapoeiraReopen.md` §1/F4;
this round's wave-1 seats `.ufo/waves/round-73/w1/{RevSowersAccess,ScoutQuarantineConlang,ScoutAmendTriage}.md`;
`tools/check-source-access.py` (whole docstring + `BYPASS` + `selftest`), `tools/check-gate-quotes.py`
docstring, `tools/reopen-row.py` header/`USER_AGENT`.

**No live fetch was made by this seat** (all evidence below is committed bytes plus synthetic fixtures),
so no User-Agent record is owed for my own probes; downloads: none. Fixtures and greps live in
`/tmp/CritQuality22/`.

---

## 0. Verdict, counterexample, axes, correction

**Counterexample (decisive, from local bytes).** The planned requirement — "records the exact UA string
and the retry with a browser-shaped UA, with verbatim status lines" — is *satisfied while vacuous* on the
two cases that motivate it, because the wall and the content both answer **HTTP 200**:

- round-72 UNESCO, `.ufo/waves/round-72/w1/ScoutCapoeiraReopen.md:86-92`: browser UA → `http=200`,
  154,208/154,144 B narrative; default curl UA → `http=200`, ~45 KB TSPD interstitial; **empty** UA →
  full page ("the trigger is the *default curl token*, not 'no UA'"). Both status lines read `200`.
- round-73 Springer, `.ufo/waves/round-73/w1/ScoutAmendTriage.md:41` and `RevSowersAccess.md:37-39`:
  `https://link.springer.com/…` → **200**, 3,038 B, body is `<title>Client Challenge</title>`.

So a record of the form `UA "curl/8.23.0" -> HTTP 200; UA "Mozilla/…" -> HTTP 200` passes the planned
clause and proves nothing. Tested: the plan's shape accepts 4 of my 7 fixtures, mine accepts 3 (§3.4).

**Second counterexample.** The plan's own "browser automation / solved captchas remain forbidden
(criterion 10)" is a *reminder*, not a check: a headless-browser request carries a browser-shaped UA, so
the shape check passes an automation record (fixture 3, §3.2 line 3). And the lane's existing
criterion-10 vocabulary cannot supply that check: `tools/check-source-access.py`'s `BYPASS` regex flags
**every honest disclosure sentence** I tested, including "no headless browser was used" (7/7, §3.5).
A criterion that reuses that vocabulary on Gate lines would void its own compliant records.

**Impacted axes.** Coverage: none (no source, row or entry moves). Calibration: the criterion text itself,
plus its check and controls (QUALITY 11/9). Discernment: only if the criterion is *shown able to fail* and
lands with a pre-dispatch control receipt — as drafted it is named in `claims.json` only as
`quality_candidate`, and **no claim leg binds it** (`grep -n quality_candidate reports/round-73/claims.json`
→ line 59; legs of C and Ca never name QUALITY 22). Landing it unexercised and unchecked is
calibration, not discernment (QUALITY 20), and an unverified clause (QUALITY 11).

**Smallest safe correction.** Keep the plan's two probes, but make the *response* the unit and the
*observable* the discriminator: each User-Agent in the record is immediately followed by that request's
own status **plus byte count and wall marker**, the exact string is inline (no alias, no `…`), a fixed
ground token opens the reason cell so a line-oriented check has a sound scope, and `automation: none` is
a positive disclosure token instead of a keyword scan. Final text in §4.

---

## 1. The three required records (+ 4 controls)

All seven are in `/tmp/CritQuality22/rejects.txt`, one record per physical line, in the round-72 Gate
table shape (`| staged entry | refused rows | reason | flip | verdict |`), with the ground token opening
the reason cell.

```
1  | staged S920 | S894 | status: HTTP 403 to plain curl; re-test 403 https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article; automation: none | a copy that answers an ordinary request | rejected |
2  | staged S920 | S894 | status: UA "curl/8.23.0" -> HTTP 403, 1302 B, wall present ("Just a moment..."); UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 403, 1302 B, wall present; discriminator: none, both refused; automation: none | a copy served to an ordinary request | rejected |
3  | staged S903 | S881 | captcha: UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/130.0.0.0 Safari/537.36" -> HTTP 200, 43419 B, wall present (CAPTCHA frame); UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 43419 B, wall present; automation: Playwright headless session | a Wayback capture of the same element | rejected |
4  | staged S745 | S802 | status: UA "Mozilla/5.0 …Firefox/131.0" -> HTTP 403, 0 B; automation: none | a capture | rejected |
5  | staged S910 | S816 | status: UA "curl/8.23.0" -> HTTP 200, 3038 B; UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 3038 B; reason: publisher page unreachable; automation: none | Crossref record | rejected |
6  | — | S881 | wall: UA "curl/8.23.0" -> HTTP 200, 43419 B, wall present ("Please enable JavaScript to view the page content"); UA "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36" -> HTTP 200, 154144 B, wall absent, title "Tango - UNESCO Intangible Cultural Heritage"; discriminator: bytes+marker; automation: none | none needed - opened by ordinary means | admitted |
7  | staged S881 | S881 | wall: UA-B -> HTTP 429, 364 B, wall present; two attempts, retry-after 5 honoured; automation: none | a later retry inside the budget | rejected |
```

| # | what it is | must be |
|---|---|---|
| 1 | **(a)** reject citing `HTTP 403 to plain curl`, no UA record — modelled on committed `corpus/lessons/round-64.md:71` (`re-test 403 https://…`) | FAIL |
| 2 | **(b)** UA + browser-UA retry + both responses; wall persists under both | PASS |
| 3 | **(c)** CAPTCHA-ground reject whose only reader was browser automation; *shape-compliant* on purpose | **VOID** (criterion 10) |
| 4 | control: elided UA (`…`), one probe — modelled on committed `corpus/lessons/round-62.md:43` (`-A 'Mozilla/5.0 …Firefox/131.0'`) | FAIL + ELIDED flag |
| 5 | control: two `200`s, no wall marker, no discriminator — the Springer/UNESCO class; **passes the plan's shape** | FAIL |
| 6 | control: wall present under plain UA, absent under browser UA — the round-72 UNESCO truth | PASS (verdict must be `admitted`) |
| 7 | control: alias `UA-B` — this round's own live convention (`RevSowersAccess.md:10` defines it, `:29` uses it) | FAIL + ALIAS flag |

---

## 2. What the check must match (design)

- **Scope (fail (a) reliably):** the reason cell must open with a fixed ground token `wall:` / `captcha:` /
  `status:`. Without a fixed token the scope is not grep-sound — verified: the natural vocabulary
  (`HTTP 4xx`, `http=4xx`) scores **0 in-scope lines on `corpus/lessons/round-62.md`**, while that file
  really does carry `re-test … \`403\`` on line 43 (§3.6). A narrow ground token produces a false green
  exactly where the defect lives.
- **Shape (pass (b), fail (1), (4), (5), (7)):** two `UA "<exact>" -> HTTP <code>, <bytes> B, wall
  present|absent` cells on the same physical line, in that order, `[^"…]{8,}` so an ellipsized UA cannot
  match. This is the load-bearing sentence: **a User-Agent that is not immediately followed by that
  request's own response is not a record** — a pasted UA string alone cannot satisfy it, and neither can
  a pasted status alone.
- **Automation (flag (c)):** a positive token `automation: none`, not a keyword scan. A record in scope
  without the token, or with a named tool, is VOID. Reason: the keyword scan is negation-blind (§3.5) and
  a headless UA is browser-shaped, so nothing else separates (c) from (b).

---

## 3. Tested output (verbatim; `grep -E`, GNU grep; fixtures in `/tmp/CritQuality22/`)

### 3.1 The two greps

```
$ GROUND='^[|*-].*\| *(wall|captcha|status):'
$ SHAPE='UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent).*UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'
$ echo "GROUND=$(grep -Ec "$GROUND" rejects.txt) SHAPE=$(grep -Ec "$SHAPE" rejects.txt)"
GROUND=7 SHAPE=3
```

### 3.2 Per-record verdict

```
--- per record ---
1 FAIL
2 PASS
3 PASS
4 FAIL
5 FAIL
6 PASS
7 FAIL
```

(3 is PASS on shape only; §3.3 voids it. Verdict rule: a record matching GROUND but not SHAPE is the
finding; the declared check is the two-count comparison, `GROUND == SHAPE`.)

### 3.3 Automation, alias, elision flags

```
=== AUTOMATION flag (in-scope records naming a tool, or lacking the token) ===
3:| staged S903 | S881 | captcha: UA "Mozilla/5.0 (X11; Linux x86_64)
=== ALIAS flag ===
7:| staged S881 | S881 | wall: UA-B -> HTTP 429, 364 B, wall
=== ELIDED UA flag ===
4:| staged S745 | S802 | status: UA "Mozilla/5.0 …Firefox/
```

Flags used: `automation:` absent (`grep -nE "$GROUND" rejects.txt | grep -vE 'automation: none'`),
`\bUA-[A-Z]\b`, `UA "[^"]*(…|\.\.\.)[^"]*"`.

### 3.4 The plan's own shape is vacuous on the motivating class

```
$ PLAN='UA "[^"]+" -> HTTP [1-5][0-9]{2}.*UA "[^"]+" -> HTTP [1-5][0-9]{2}'
PLAN-shape passes=4  (my shape passes=3)
--- lines the PLAN shape accepts ---
2 3 5 6
--- of those, lines my shape rejects (vacuity) ---
5
```

Line 5 is the real Springer record: `200` twice, 3,038 B twice, no wall marker, no discriminator.
The plan accepts it; it is the exact case that motivated the criterion. Line 3 shows the plan also
accepts the automation record.

### 3.5 The lane's existing criterion-10 vocabulary false-positives on honest disclosure

`python3` import of `tools/check-source-access.py` and `.BYPASS.search()` on the sentences this round's
seats actually wrote:

```
honest-disclosure-1    flag=True  :: No browser automation, no challenge bypass used (QUALITY 10)   [RevSowersAccess.md:12]
honest-disclosure-2    flag=True  :: Not a CAPTCHA wall; not bypassed (no browser automation).       [ScoutQuarantineConlang.md:62]
honest-disclosure-3    flag=True  :: No challenge wall bypassed: Springer's JS Client Challenge …   [ScoutAmendTriage.md:20]
bypass-real            flag=True  :: obtained through a headless browser session
captcha-real           flag=True  :: solved a captcha to read the page
playwright-real        flag=True  :: read with a Playwright browser
negated-headless       flag=True  :: no headless browser was used
```

7/7, including three true disclosures. `\bheadless\b` carries no negation guard; the `bypass` guard only
looks back one word (`(?<!\bnot )`), so "no challenge bypass" and "wall bypassed" both match. An ERE
version of this scan flagged 5/5 committed round-73 lines, all of them negations
(`grep -nE '(headless|playwright|puppeteer|selenium|webdriver|bypass|circumvent)'` over the three seats).
Consequence: (c) cannot be checked by a keyword scan; it needs a positive `automation:` token.

### 3.6 Scope: the natural ground vocabulary misses the defect

```
- Merriam-Webster `talaria` (ScribeTalariaMW, tier A candidate): the live page refuses ordinary requests. Re-test (QUALITY 12): `curl -s -o /dev/null -w '%{http_code}' -A 'Mozilla/5.0 …Firefox/131.0' https://www.merriam-webster.com/dictio…
narrow=0 wide=2        # corpus/lessons/round-62.md
```

One committed line carries both defects at once — a bare `403` (invisible to a `HTTP 4xx`/`http=4xx`
scope) and an elided UA — and the narrow ground scores it out of scope: false green.

### 3.7 Red-before on committed bytes (the check can fail on real files)

| file | in-scope (loose ground) | shape-compliant | in-scope (`wall:`/`captcha:`/`status:` prefix) |
|---|---|---|---|
| corpus/lessons/round-61.md | 6 | 0 | 0 |
| corpus/lessons/round-62.md | 2 | 0 | 0 |
| corpus/lessons/round-62-verifier-spotcheck.md | 4 | 0 | 0 |
| corpus/lessons/round-64.md | 15 | 0 | 0 |
| corpus/lessons/round-71.md | 5 | 0 | 0 |
| corpus/lessons/round-72.md | 2 | 0 | 0 |
| .ufo/waves/round-73/w1/RevSowersAccess.md | 13 | 0 | 0 |
| .ufo/waves/round-73/w1/ScoutQuarantineConlang.md | 5 | 0 | 0 |
| .ufo/waves/round-73/w1/ScoutAmendTriage.md | 11 | 0 | 0 |

63 candidate lines under a loose vocabulary, **0 compliant, 0 prefixed**. So: the criterion has no
passing instance anywhere in the repo, it binds from round 73 with nothing retro-fitted, and the *first*
record written under it will invent its own grammar unless the criterion carries the shape — which is
already happening: `RevSowersAccess.md:10` defines `UA-B = Mozilla/5.0 (X11; …) Chrome/130.0 Safari/537.36`
once and its 13 probe rows say `(UA-B)`. That alias form is invisible to the shape grep (tested: a record
copied in that convention matches 0 times) and unrepeatable for a re-opener who reads only the Gate line —
the K71-8 class the round is trying to close.

---

## 4. Final clause text (8 lines)

The **minimal core** — the smallest wording a pasted UA string cannot satisfy without a second response —
is the single sentence in line 3. Everything else is either scope (line 2), the vacuity guard (line 4),
the criterion-10 guard (line 6) or the check (line 7).

```
22. **A wall, CAPTCHA or HTTP-refusal record binds each User-Agent to the response that request got** — adds to criteria 10, 12, 13 and 21, restating criterion 21's field (3).
Scope: any Gate record whose reason cell opens with `wall:`, `captcha:` or `status:`; the record is one physical line, so a line-oriented check binds it.
Each request in the record is `UA "<exact string>" -> HTTP <code>, <bytes> B, wall present ("<marker>")|wall absent`, in that order: a User-Agent with no response of its own is not a record, an alias (`UA-B`) or an elided string (`Mozilla/5.0 …Firefox/131.0`) is not a record, and the literal string a re-opener would send is in the record itself.
The status decides nothing — the wall and the content both answer HTTP 200 (round-72 UNESCO 43,419 B wall vs 154,144 B narrative; round-73 Springer 200/3,038 B `<title>Client Challenge</title>`) — so the bytes and the marker are recorded per request and the reason names the one it rests on.
The second request is `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, and the record says so when it was not made: a wall seen under one UA is UA-unknown, not a source property; a wall persisting under both is a valid reject; a wall present under the plain UA and absent under the browser UA voids the reject and the source is re-opened by ordinary means (round-72: 5/5 wall plain, 5/5 clean browser, full page under an empty UA).
The record carries `automation: none` or names the tool it used; a record naming browser automation, a solved CAPTCHA or a bypassed block is VOID under criterion 10 whatever its status lines say (a headless-browser UA is browser-shaped, so the shape check alone passes it). A 429 records its attempts and gaps per criterion 16 and is never read as UA-gating.
Check (red-before, pre-dispatch): over the round's `## Gate` section `grep -Ec "$GROUND"` must equal `grep -Ec "$SHAPE"` — GROUND `^[|*-].*\| *(wall|captcha|status):`, SHAPE `UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)` twice on the line — with `automation: none` in every in-scope record, and the three controls (missing, compliant, automation) filed with the run. Review-only, criterion 11: that the named observable is the one the reason rests on, and that a difference between the two responses shows up in the verdict.
Limits, stated: grep cannot tell a pasted UA from a sent one, cannot resolve an alias and cannot read a wrapped record; the verbatim output block and the re-open command in the record are what a re-opener repeats. Binds from round 73; no earlier Gate line is retro-fitted.
```

### The grep, as a declared check (single invocation each, no pipe)

```
GROUND='^[|*-].*\| *(wall|captcha|status):'
SHAPE='UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent).*UA "[^"…]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'
g=$(grep -Ec "$GROUND" "$LESSON"); s=$(grep -Ec "$SHAPE" "$LESSON"); test "$g" -eq "$s"
```
`grep -c` exits 1 on zero matches, so neither count may be taken through a pipe (criterion 11's
"no pipe without `pipefail`"); `test` is the leg's exit status.

---

## 5. Defects found in the plan, ranked

| id | defect | evidence | smallest safe correction |
|---|---|---|---|
| Q22-1 | "verbatim status lines" is vacuous: the motivating walls answer 200 | `ScoutCapoeiraReopen.md:86-92` (200 both ways), `ScoutAmendTriage.md:41` (200 + 3,038 B challenge body); §3.4 shows the plan's shape passing the Springer record | require bytes + wall marker per request; record the observable the verdict rests on |
| Q22-2 | the shape check passes a headless-browser record, and the plan's "browser automation remains forbidden" has no check | fixture 3 PASSes the shape; `RevSowersAccess.md:12`, `ScoutQuarantineConlang.md:62`, `ScoutAmendTriage.md:20` are all flagged by the existing `BYPASS` regex (7/7 test) | positive `automation: none` token; VOID on a named tool |
| Q22-3 | alias and elision loopholes are live this round | `RevSowersAccess.md:10` vs `:29`; `corpus/lessons/round-62.md:43` | exact string inline in the Gate record, no alias, `[^"…]` in the shape |
| Q22-4 | no fixed ground token ⇒ the scope regex under-counts | narrow ground scores `corpus/lessons/round-62.md` 0 while line 43 carries `403` (§3.6) | `wall:` / `captcha:` / `status:` opening the reason cell |
| Q22-5 | no claim leg binds the criterion; it is only `quality_candidate` | `reports/round-73/claims.json:59`; C's GATE/REJECTS legs name QUALITY 21 only | commit the three controls pre-dispatch and cite the receipt, or add the leg; otherwise the criterion lands unverified (QUALITY 11) |
| Q22-6 | this round may have no wall-ground reject at all, so the criterion would land unexercised | `RevSowersAccess.md` falsifies the S894/S910 unreachability hypothesis; `ScoutAmendTriage.md:70` says S910 is not an unreachability reject | the S894/S910 Gate rows must carry the publisher-tier `status:` record (Cambridge 429 under one UA only — in scope and currently non-compliant), giving round 73 a real first application |
| Q22-7 | redundancy with criterion 12 is real but must be stated, or scribes will think 12 suffices | `corpus/lessons/round-64.md:71` and `:73` carry `re-test 403 https://…` — measurable, verbatim, no UA | the clause must not say only "verbatim status lines" (that is 12's wording, already satisfied); the UA↔response binding is the increment |
| Q22-8 | "one-line check" against a corpus whose Gate records wrap | `corpus/lessons/round-71.md:34-39` is a 7-line prose sweep with no per-item URL; `tools/check-gate-quotes.py` joins indented continuations by design | require the record to be one physical line (round-72 Gate table rows already are) and say the check reads joined-less records only |

Not a defect, checked and upheld: the criterion does not conflict with criterion 21 — 21's field (3)
(`status, challenge wall?, redirect target`) is exactly the field this clause sharpens, which is why the
clause says "restating criterion 21's field (3)" rather than introducing a second record shape
(criterion 21 already requires "Every Gate reject records the URL it rejected").

---

## 6. What I did not verify

- No live fetch, no CDX query, no capture check: I did not re-probe UNESCO, Springer, Cambridge or
  Merriam-Webster. Every status/byte figure quoted above is taken from the committed seat file named
  beside it, not re-measured by me. The one *live* claim I made is negative and structural (the plan's
  shape passes two 200s), which follows from the recorded bytes alone.
- I did not run the proposed check as a tool (none exists); the greps above are the tested artefact.
  `tools/check-ua-record.py` is named nowhere in the clause on purpose — a grep pair is smaller and the
  round has no wall-ground record yet to validate a tool against.
- I did not test the clause against a Gate record that legitimately needs *three* probes (plain UA,
  browser UA, empty UA). The round-72 evidence (empty UA ⇒ full page) means an empty-UA probe can decide
  a case the two-probe rule cannot; the clause records the empty-UA fact in its evidence but does not
  require the third probe, which is the smaller rule.
- Fixtures 1, 4, 5, 7 are synthetic; 1 and 4 are modelled on the committed lines named in §1, and 5 and 7
  on this round's own Springer and `UA-B` bytes.
