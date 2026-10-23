# CriticEntryContract57 — claim C entry contract attack (round 57)

Seat: KotodamaR57.CriticEntryContract57 (critic, leaf). Axes: coverage, calibration. Read: `corpus/QUALITY.md` criteria 1-6 (and 7, 10 where they bind the entry), `corpus/lessons/round-56.md` `## Falsify` and `## Mistakes`, `corpus/lessons/round-56-verifier-spotcheck.md`, `reports/round-57/claims.json`, `reports/round-57/accept-c.py`, `reports/round-57/reopen-quote.py`, `tools/check-gate-quotes.py`, `tools/check-source-access.py`, `tools/check-draft-ids.py`, `corpus/knowledge/civilizations/kongo-kingdom.md` (round-56 exemplar). All paths below are relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `ENTRY` = `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md`. No installs. Nothing written except this report.

## Findings first (counterexamples measured this session)

1. **The declared partial-owner list is incomplete, and every sub-topic of the brief already has an in-corpus owner.** `claims.json:102` names only animal-symbolism, color-symbolism, costume-semiotics and naming-systems. The sweep this session found these as well:
   - European blazon and the arms/badge/livery/crest stack: `culture-material/warrior-material-culture.md:50-54`.
   - Mamluk blazons: `civilizations/mamluk.md:123-133`, with the hedge at `:125`: "'Rank blazons' must not be mistaken for a universal rank ladder".
   - Ming–Qing buzi rank badges, with the ladder: `culture-material/sumptuary-law-rank-display.md:53-54`; also `costume-semiotics.md:39`, `dress-through-eras.md:46` and `textile-technology.md:86`.
   - Livery statutes: `costume-semiotics.md:43`.
   - Kamon: `civilizations/japan-edo.md:143` ("Assuming every repeated crest proves blood descent" is listed as the error); `japan-medieval-sengoku.md:32` ("a crest does not establish ancestry") and `:114`.
   - Tamga: `civilizations/turkic-steppe.md:40` and `:96-102` ("Treating every similar mark as one clan, alphabet, or coat of arms").
   - Seals and signet rings: `adornment-body-codes.md:20`.
   - Northwest Coast crest rights: `animal-symbolism.md:33,42`.
   - The cardinal's red hat: `color-symbolism.md:81`.
   - The rule of tincture: `color-symbolism.md:129` and `symbolism-synthesis-method.md:64`.

   Risk: a duplicate authority that contradicts a partial owner (a buzi ladder or a Mamluk "rank" reading different from the owner's), or a "gap filled" line that claims virgin ground. Impacted axes: coverage (review-only "uncovered in substance") and calibration.

2. **The corpus already contains the Eurocentric universal the brief warns about.** `warrior-material-culture.md:52` says "Arms are hereditary pictorial property", and `:53` lists "arms (hereditary, court-registrable)", sourced to Fox-Davies 1909 and Wagner 1956. Neither source is in the registry. If the L1 copies or paraphrases those lines into ENTRY, two things go wrong: English law becomes the general rule, and the sentence cites a source nobody opened this round.

3. **The locator takes the first double-quoted span of the anchor cell, whatever it is** (`reopen-quote.py:204-205`). Probe: an anchor `section "Rule of tincture", para 2: "metal should not be placed …"` makes `row_target` return the quote `'Rule of tincture'`. That is 3 words, so the row is NOT_LOCATED. Round-56 style anchors that wrapped a quote in guillemets with an inner curly pair (S376: `«kanda means “group or category,” …»`) also hand the locator the inner fragment.

4. **CJK quotes cannot pass LOCATE.** Probe: `normalise('家紋は家の象徴として用いられ、江戸時代には庶民にも広まった。')` gives **2 words**, under the 8-word floor. The same quote counts as 1 whitespace token, so the 25-word cap means nothing for CJK text. Kamon, buzi and tamga sources quoted in Japanese or Chinese will fail LOCATE.

5. **Round 56's own rows would fail this LOCATE leg.** `reports/round-57/telemetry/locator-calibration.txt` ends `CALIBRATION located 38 of 54`, which is 70%, below the 80% bar. The failure classes:
   - 8 rows: quote under 8 words;
   - PDF text-layer mismatch (S362, S364, S381, S385);
   - a scan-only PDF (S374);
   - an SPA shell instead of the document (S410);
   - host or Wayback errors (S384, S391, S400).

   With a floor of 20 cited ids, at most 4 rows may miss (need = ceil(0.8 × 20) = 16). The closure re-runs LOCATE live later.

6. **Negated access disclaimers trip ACCESS.** `check-source-access.py` BYPASS fires on each of these: "opened by plain curl, no headless browser"; "no VPN or login used"; "not opened with playwright". It does not fire on "Cloudflare challenge met, not passed; read via Wayback capture …" or "direct, HTTP 200 to a default-UA curl". A cited row carrying a disclaimer like that fails ACCESS, both the status leg and the cited leg.

7. **`check-gate-quotes.py` does not enforce "Grounds = teaches".** `truncated-grounds` reports only a proper prefix. Its selftest case `truncated-grounds-shorter-not-prefix-green` (`tools/check-gate-quotes.py:430`) is green by design, so a paraphrased Grounds prints 0 findings.

8. **The RANGE leg's range regex fires on ordinary prose after an S-id.** `accept-c.py:105` matches `S420 – 14 May`, `S420 to 900 CE` and `S413–S480`. It does not match `(S420, pp. 15–16)`, `claim block numbers 413 to 480` or `dated by S420 to 1350`.

9. **SET cannot see edits to base files.** `accept-c.py:84-87` compares path sets only. If the L1 adds a back-pointer to `animal-symbolism.md`, SET and SWEEP still pass, but that edit is an undeclared land outside C's three lands (`separability-manifest.json`) and breaks the "one-way" review clause.

## Checklist for integrating the entry (each item: failure mode → check the L1 runs → smallest safe correction)

Commands run from the lane root on the staged bytes. Put SOURCES rows in a scratch copy first wherever a command reads the registry.

### A. Calibration and scope (criteria 1, 2, 4; axis calibration)

1. **Eurocentric generalisation: "heraldry" used as the umbrella term.**
   - Check: `grep -n -i -E 'herald|blazon|coat of arms|armorial|armiger|\barms\b' ENTRY`. For every hit outside the European-arms section, confirm one of two things:
     - the term is a quoted or attributed scholarly label (Mayer's 1933 title *Saracenic Heraldry*; "Polish heraldry"), or
     - the sentence explicitly compares a system to European arms.
   - Also check the head and §1. They must define three terms once:
     - "arms" / "heraldry" = the European hereditary armory system and its derivatives;
     - "emblem" = the umbrella;
     - "mark" = tamga, house, merchant and livestock marks.
   - Fix: replace the bare term with the system's own name: *kamon*, *buzi* or rank badge, Mamluk blazon (attributed to Mayer), tamga, *herb*, house mark, brand.
   - In-corpus precedent: `turkic-steppe.md:96` (not "coat of arms"); `mamluk.md:125`.

2. **One national practice stated as universal (English cadency, the law of arms, grants).**
   - Check: `grep -n -w -E 'always|never|all|every|must|rule|universal|only|cannot' ENTRY`. Each rule sentence must carry a jurisdiction and a period, and its cited row must be authoritative for exactly that jurisdiction:
     - College of Arms → England;
     - Court of the Lord Lyon → Scotland;
     - Canadian Heraldic Authority → Canada.
   - Counterexamples the table should hold side by side, each only if a row opened this round carries it:
     - English cadency brisures;
     - Scottish differencing by matriculation and bordure;
     - Polish *herb* shared by many unrelated families (the opposite of one-bearer arms);
     - assumed burgher arms on the continent;
     - kamon adopted without a grant.
   - Fix: prefix each rule with "In England …" or "Scottish practice …", or move it into a jurisdiction column. Never copy `warrior-material-culture.md:52-53` (finding 2); point to it one-way as the English-law stack.

3. **Office emblems written as hereditary (Mamluk blazons, buzi, livery badges, ecclesiastical hats).**
   - Check: every sentence about these four names who confers the emblem and whether it passes to heirs, at the strength the cited row states.
   - Grep `inherit|hereditary|descend|family|lineage` within those subsections.
   - Fix: say "office-associated" or "conferred with office", and keep the owner's hedges (`mamluk.md:125-133`; `sumptuary-law-rank-display.md:53-54` dynasty differences).

4. **Kamon or tamga read as proof of descent.**
   - Check: grep `descent|ancestry|bloodline|clan|family crest` near kamon and tamga.
   - It must agree with `japan-edo.md:143`, `japan-medieval-sengoku.md:32` and `turkic-steppe.md:40,96`, or state the disagreement with its own cited row.
   - Fix: "a crest records a claimed or recognised affiliation".

5. **Dropped hedges.**
   - Check: for each seat draft sentence mapped into ENTRY, compare hedge tokens in the seat sentence and the entry sentence:
     `grep -o -i -w -E "may|might|possibly|probably|likely|perhaps|apparently|traditionally|said to|attributed|c\.|about|around|some|often|usually|identified as|earliest surviving|conventionally" <seat report> | sort | uniq -c`
     Run the same grep on the ENTRY sentence. Any token that disappears is a finding.
   - Round-56 fix precedents: "traditionally seen as the founder"; "likely pre-Christian"; "more or less" restored at `masks-masquerade.md:105`.
   - Fix: restore the source's hedge word for word.

6. **Pop-heraldry myths not flagged on first use (criterion 2).**
   - Check: each myth the entry touches carries a code from `verification/calibration-registry.md:35-39` (R/C/B/H/T) on its first mention, with the cited row. Candidate myths:
     - "a coat of arms for a surname";
     - fixed medieval tincture meanings;
     - "bend sinister = bastard";
     - Crusade origin of arms;
     - "kamon = Japanese coat of arms";
     - tamga as the origin of Turkic runes;
     - buzi or Mamluk blazons as "heraldry";
     - NAVA flag "rules".
   - Guard against over-correction:
     - a surname coat of arms is R under English and Scottish law, but B for Polish clan arms;
     - marks of illegitimacy existed in some periods, so a blanket R is itself a calibration error: use B with scope;
     - a flag-design booklet is one association's guidance (H/B), not a standard.
   - Fix: a calibration bank in the shape of `kongo-kingdom.md:136-147`, one code per proposition.

7. **A museum label over-read as a study.**
   - Check: list the rows with `kind` = `record` (object pages, museum APIs). Every entry sentence citing one must name the object or the institution, and claim only what the label says about that object. A label never supports "X practice was general".
   - Exhibition essays are B, not studies.
   - Fix: "The <museum>'s <object> record dates …", or drop the generalising clause. Precedent: round-56 CriticClaimC56 tied "the Saint Anthony staff" to one chief's staff.

8. **Restricted crests described beyond the holder's public statement.** This covers Northwest Coast crests and crest stories, the imperial chrysanthemum, Scottish chiefs' crests versus clansmen's badges, and the Red Cross / Red Crescent protected emblems.
   - Check: `grep -n -i -E 'chrysanthemum|kiku|imperial|Haida|Tlingit|Kwakwaka|Tsimshian|Nisga|Gitxsan|totem|chief|Red Cross|Red Crescent|protected emblem|restricted' ENTRY`. Each hit:
     - cites a row from the holder or the competent authority;
     - states no more than that row's existence, holder and shape of the restriction;
     - gives no reproduction detail and no withheld story;
     - never suggests a worldbuilder adopt the real crest.
   - Ceiling precedent: round-55 Gate S346 ("a community's own public statement can publish the existence, holder and shape of a restriction while expressly withholding its content — that is the ceiling for a world document").
   - Fix: cut to the holder's statement plus a one-way pointer to `animal-symbolism.md:33,42`.

9. **Lore boundary: no canon decisions (criterion 5).**
   - Check: `grep -n -i -E 'bears |should bear|your house|the house of|canon|assign' ENTRY`. No sentence decides which house, faction or person bears an emblem. Worked examples are labelled as designer options.
   - The handoff section re-reads its anchors at the claim base: `sed -n` on each cited line of `synthesis/worldbible-integration-contract.md` and of lore files under `/home/vgpnk/Projects/shokunin/lore-shokunin/`. Do not copy Kongo's `:17,:43,:58,:69,:126,:132` without re-reading them.
   - It states "NON-CANON; this section transfers nothing", as `kongo-kingdom.md:162` does.
   - Fix: "lore selects which faction bears which device; this entry supplies grammar, constraints and calibration flags".

10. **The gap statement overstates the gap.**
    - Check: the `gap filled` line quotes the declared sweep, which gives 0 filename owners (`claims.json:19`), and lists the partial owners in finding 1 by `path:line`.
    - The one-owner table (shape of `kongo-kingdom.md:21-35`) gives each owner its boundary.
    - No ENTRY sentence restates an owner's fact differently without citing its own row.
    - Fix: add the missing rows to the boundary table. Do not edit the owners.

### B. Provenance, tiers and registry shape (criteria 1, 6, 10; axis coverage)

11. **A publisher blurb, abstract or catalogue page filed as tier A (criterion 6).**
    - Check, from the staged registry:
      ```
      python3 -B -c "import re;[print(c[1].strip(),c[3].strip(),c[4].strip(),c[2].strip()[:90]) for l in open('corpus/SOURCES.md',encoding='utf-8') for c in [l.split('|')] if re.match(r'^\|\s*S4(1[3-9]|[2-7]\d|80)\s*\|',l) and c[4].strip()=='A']"
      ```
    - Then verify each tier-A row, using its kind and host:
      - publisher, bookseller, JSTOR first page or Oxford Reference abstract → at most B;
      - `community` (Heraldry of the World / heraldry-wiki, Wikipedia, forums) → never A, and C only as a lead;
      - an official heraldic authority → A only for its own jurisdiction's practice;
      - a museum record → A only for that object's data.
    - Fix: set the tier at filing. These are new rows, so no superseding row is needed.

12. **A tier-C row as sole support** (QUALITY, after criterion 5).
    - Check: for each C-tier id, `grep -n 'S4xx' ENTRY`. Each citing sentence also cites an A or B row.
    - Fix: add the stronger row or cut the sentence.

13. **Author-year citations of sources nobody opened.**
    - Check: `grep -n -E '\(([A-Z][a-z]+[^()]*\b1[0-9]{3}|[A-Z][a-z]+ 20[0-9]{2})\)' ENTRY`. Every author-year citation must sit next to an S413-S480 id or be an attributed in-corpus `path:line` pointer.
    - Fox-Davies 1909, Woodcock & Robinson, Wagner 1956 and Mayer 1933 appear across the corpus without registry rows (finding 2; `mamluk.md:8`).
    - Fix: cite an opened row, or write "per `mamluk.md:126`".

14. **Draft ids left in the text.**
    - Check: `python3 -B tools/check-draft-ids.py ENTRY corpus/SOURCES.md corpus/lessons/round-57.md`. Expect 0 `DRAFT_ID` lines: F1 `NEW-<Seat>-<n>`, F2 `, -N`, F3 `S4xx-N`. Also `grep -c 'NEW-' ENTRY corpus/SOURCES.md` must give 0.
    - Fix: map each draft id 1:1 to its S-id before writing any sentence. Merged duplicate works keep every block's quotes: round 56 lost them on S361, S384 and S404 (ReviewExcludedSources56).

15. **S-ids outside S413-S480, or a foreign S-id pulled in through a pointer.**
    - Check: the RANGE leg of `python3 -B reports/round-57/accept-c.py`. Before that: `grep -n -o -E '\bS[0-9]{3}\b' ENTRY | awk -F: '$3<"S413"||$3>"S480"'`.
    - Typical leak: a couples or boundary pointer such as "kongo-kingdom.md §10 (S384, S397)", or round-56 row ids copied from a sibling. Records rows S481-S499 are never cited by ENTRY.
    - Fix: point by `path:line` only, never by another entry's S-id.

16. **Block rows not equal to the cited set.**
    - Check:
      ```
      python3 -B -c "import re;E='corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md';c=set(re.findall(r'\bS\d{3}\b',open(E,encoding='utf-8').read()));b={m.group(1) for l in open('corpus/SOURCES.md',encoding='utf-8') for m in [re.match(r'^\|\s*(S4(?:1[3-9]|[2-7]\d|80))\s*\|',l)] if m};print('uncited',sorted(b-c),'unrowed',sorted(c-b))"
      ```
      Both lists must be empty. Assign ids from S413 upward; the unused tail stays unassigned (round-56 convention: uncited blocks are not registered).

17. **Used-by and status cells.**
    - Check: the USEDBY and STATUS legs. Pre-empt them in the cell shape:
      - `status` is exactly `mined`;
      - `used-by` holds the exact path `corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md` as a whole comma- or semicolon-separated item, with no `(§3)` suffix;
      - no literal `|` in any cell, because it shifts cell 8 and cell 11. Do not use `&#124;` inside a quote either: it normalises to the token `124` and the quote is not located.

18. **FRESH: URL reuse, including within the round.**
    - Check: the FRESH leg covers rows below S413. For duplicates inside the round, normalise the new rows' URLs the way `accept-c.py:150-153` does, plus `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` (W04 duplicate-URL warnings) in the scratch copy.
    - The britannica.com host is already registered once: check the exact path.
    - Fix: merge duplicates by URL and keep all the quotes.

19. **Access wording (criterion 10).**
    - Check: the ACCESS leg. Pre-empt it by keeping negated disclaimers out of rows (finding 6). Use `Cloudflare challenge met, not passed; read via Wayback capture <id>` or `direct, HTTP 200`.
    - Third-party journal scans with no stated permission are rejected (R56-M4).
    - Fix: rewrite the note. A challenge that was actually passed makes the row unopened.

### C. Quotes, Gate lines and the LOCATE margin (axis coverage)

20. **The anchor's first double-quoted span is not the quote** (finding 3).
    - Check, in the scratch copy with the staged SOURCES:
      `for s in <block ids>; do printf '%s ' $s; python3 -B reports/round-57/reopen-quote.py --row $s; done`
      Every row should print LOCATED.
    - Fix:
      - write locator text with single quotes (`paragraph beginning 'X'`, as round 56 did);
      - put the located quote first, in straight or curly double quotes;
      - no guillemet wrapper around a span containing curly quotes.

21. **The quote changed between the seat's LOCATED line and the anchor cell.**
    - Check: the row-mode run in item 20.
    - Do not add `[sic]` or editorial brackets, do not cut with `…`, and do not change words. Typographic quote marks are harmless, because normalise strips them.
    - The URL that serves the text goes first among at most four in the source cell (`reopen-quote.py:203`; only the first four are tried). No URL slug may repeat three consecutive quote words.

22. **The LOCATE margin is too thin for a live re-run** (finding 5).
    - Check: the integration run shows located ≥ 90% of cited rows, and cited ≥ 20.
    - Avoid rows whose only text-serving URL is fragile: Wayback (fetched one at a time; HTTPError in calibration), scan-only PDFs, SPA `/download` shells, or hosts that returned URLError.
    - Fix: drop or replace a NOT_LOCATED row before landing. Never shrink the floor.

23. **CJK-only quotes** (finding 4).
    - Check: `grep -n -P '[\p{Han}\p{Hiragana}\p{Katakana}]' corpus/SOURCES.md` within the block's anchor cells. Any CJK first quote is a LOCATE miss.
    - Fix: quote an English or romanised passage of the same served page. Keep the CJK term in the teaches cell or the entry as a term, not as the located quote.

24. **Quotes over 25 words, or under 8.**
    - The Gate is checked by `python3 -B tools/check-gate-quotes.py corpus/lessons/round-57.md` (over-cap, ellipsis-joined, doubled-locator, html-entity) and should give 0 findings.
    - ENTRY has no tool. Check it with:
      ```
      python3 -B -c "import re;t=open('corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md',encoding='utf-8').read();[print(len(q.split()),q[:70]) for m in re.finditer(r'\"([^\"]+)\"|“([^“”]+)”|«([^«»]+)»',t) for q in [next(g for g in m.groups() if g)] if len(q.split())>25]"
      ```
      It should print nothing. The 8-word floor is measured by the locator, not by `wc`: a standalone `—` counts as a whitespace word but normalises to nothing.
    - All quotes are plain UTF-8 with no character reference (R56-M1).

25. **A Grounds that is not the teaches cell** (finding 7).
    - Check: the tool cannot catch this, so run an exact comparison:
      ```
      python3 -B - <<'EOF'
      import re
      t={m.group(1):l.split('|')[7].strip() for l in open('corpus/SOURCES.md',encoding='utf-8') for m in [re.match(r'^\|\s*(S\d{3})\s*\|',l)] if m}
      g=open('corpus/lessons/round-57.md',encoding='utf-8').read().split('## Gate',1)[1].split('\n## ',1)[0]
      bad=[s for s,x in re.findall(r'^- (S4(?:1[3-9]|[2-7]\d|80)) .*?Grounds: (.*?) Seat:',g,re.M) if x.rstrip('. ')!=t.get(s,'').rstrip('. ')]
      print('grounds mismatches',bad)
      EOF
      ```
      Expect `[]`.
    - Also check that the Gate quote is byte-identical to the anchor's first quote, and that the Gate URL is the source cell's first URL (ReviewGateLines56 did this).
    - The teaches cell is one sentence of at most 30 words ending in a full stop, with no `|`.

### D. Landing shape and separability (criterion 7; axis coverage)

26. **Range notation.**
    - Check: the RANGE leg's `range_notation=[]`. Pre-empt the matches in finding 8:
      - never follow an S-id with a dash, `to`, `through`, `…` or `~` plus a 2-3 digit number;
      - write `(S420, pp. 15–16)`;
      - write the block in the head as "numbers 413 to 480", with no `S` prefix (the `kongo-kingdom.md:7` form).

27. **ENTRY names a path that another unit lands for the first time.**
    - Check: `grep -n -E 'lessons/round-57|round-57\.md|check-gate-quotes' ENTRY` should print nothing. `round-57.md` is a REC land absent at base, so naming it is a C→REC dependency; O's tool path is on C's must-not-cite list (`claims.json:120`).
    - Then run `python3 -B tools/check-claim-separability.py reports/round-57/separability-manifest.json`, expecting `SEPARABILITY: 0 findings`.
    - Fix: say "this round's lesson", or point to the registry rows only.

28. **Undeclared land (one-way pointers broken)** (finding 9).
    - Check: `git diff --name-only 0314aa981071220d206760b5263467faeea05b60 <C landing commit>` prints exactly `corpus/README.md`, `corpus/SOURCES.md` and ENTRY.
    - Fix: revert any edit to a partial owner. Back-pointers belong to a later round's Frontier.

29. **Size and index.**
    - Check: `wc -l ENTRY` ≤ 230. The brief bounds it and no leg checks it.
    - The SWEEP leg needs the `corpus/README.md` index row in the sweep's expected shape (`reports/round-28/readme/sweep.py`).
    - Write the `verified-at` counts (232 → 233) only after `accept-c.py` has printed them, never before measuring.

30. **The final gate.**
    - Run `python3 -B reports/round-57/accept-c.py` on the landed revision. Every leg must print PASS (SET, SWEEP, FLOOR, RANGE, STATUS, USEDBY, ACCESS, LOCATE, FRESH) and the last line must be `ACCEPT-C-57: PASS`.
    - Record the LOCATE `at=` time and the `not_located` list in the receipt. A miss is reported, not re-scaled (`claims.json:9`).

## Smallest safe corrections, ranked by harm avoided

1. Add the partial owners from finding 1 to ENTRY's boundary table, and copy no partial-owner sentence. This protects against a duplicate authority, an English-law universal and an unopened citation.
2. Fix the anchor shape (quote first, locators in single quotes), quote nothing in CJK, keep negated access notes out of rows, then run row-mode LOCATE on every staged row and replace any miss until located ≥ 90%.
3. Run the exact Grounds = teaches comparison: the shipped tool cannot catch a paraphrase.
4. Scope every rule by jurisdiction and period, retain hedges word for word, and give each myth a calibration code with B/R scoped as in A6.
5. Run the `git diff --name-only` lands check and the `round-57.md` / `check-gate-quotes` grep before the separability run.

## Tradeoffs the judge must weigh (not fixable by the L1 alone)

- The declared review-only partial-owner list (`claims.json:102`) is a frozen declaration and cannot be amended. ENTRY can still exceed it, and the closure should judge "one-way pointers" against the full list in finding 1.
- Line length is bounded by the brief, not by a leg, so a 231-line ENTRY passes ACCEPT-C-57. The L1 must self-enforce it (A29).
