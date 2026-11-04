## Gate

Candidates considered and dispositioned (frozen pre-data at
`reports/round-82/claims.json`, which the L1 lands with these dispositions). Every
number below carries the command that produced it; the artifacts named are this
seat's stage files under
`.ufo/waves/round-82/w1/stage/ScribeRows/`, to be installed at the
`reports/round-82/evidence/` paths they are named by.

- **ADMITTED — claim D (depth): guest-right / hospitality as a sacral-legal
  institution, four rows opened this round.** The entry is
  `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md` (the entry seat's
  object, not this seat's); the rows are drafted at
  `.ufo/waves/round-82/w1/drafts/rows/S904-S907.md` and belong **inside** the
  Registry table directly after the S903 row — at the round base
  `c285b2afb19d4b64320e18df1f55e426bf2d0b0c`, S903 is line 858 and `## Paths`
  line 859 (`grep -n` on `corpus/SOURCES.md`), so an append at the file end is
  the R81-M5 E12 class. Shape check on the draft:
  `for l in ...; split('|')` gives 13 fields, 11 non-empty cells, no `\|` and no
  stray pipe in a cell, and every anchor's declared word count equals the words
  inside 「」 (25 / 24 / 22 / 9). Census dry run on a scratch copy with the rows
  spliced in: rows 827 → 831, `NF!=13` count 0, duplicate ids 0, tier
  A=500 B=314 C=17, status mined=732+4 queued=58 rejected=37, and 764 mined
  `used-by` paths resolve except exactly 4 — the four new rows' shared
  `corpus/knowledge/myth-symbol/guest-right-hospitality-law.md`, absent when the
  dry run was taken (`stage/ScribeRows/census-dryrun.txt`); the entry has since
  landed (28992 B) and the same loop over the current worktree reports no missing
  path, with the L1's census re-run green at exit 0 and 832 rows.
  - **S904** — Homer, *The Odyssey*, trans. Samuel Butler, Gutenberg #1727
    (`curl -sS -o od1727-plain.txt -w "%{http_code} %{size_download}\n" <url>`
    → `HTTP 200, 717782 B` under both the browser-shaped and the default
    User-Agent, byte-identical; Wayback CDX exact query → `20260925202831
    status 200`, 265452 B transferred). Anchor as landed: Book xiv, Eumaeus to the
    disguised Odysseus, 「for all strangers and beggars are from Jove」 (8 words) —
    present once in the live body and once in the capture. Tier A for the Greek
    ascription through a translation. Artifact `reports/round-82/evidence/S904.txt`.
  - **S905** — Tacitus, *Germania*, trans. Church and Brodribb, Wikisource
    (`curl -sSL ... <url>` → `HTTP 200, 41809 B transferred / 163266 B decoded,
    byte-identical under both UAs; CDX → `20260206213325 status 200`, 36977 B
    transferred). Anchor as landed: ch. XXI, 「No nation indulges more profusely in entertainments and hospitality. To exclude any human being from their roof is thought impious」 (20 words) — present once in body and capture. Tier A for
    the Roman ascription, not for German practice. Artifact
    `reports/round-82/evidence/S905.txt`.
    - Substitution record: the planned Hovamol page was probed first and set
      aside — its hemistichs sit in separate `ws-poem-line` spans, so
      `'Hail to the giver! a guest has come;'` occurs 0 times in the served bytes
      and the longest contiguous poem run is 5 words
      (`'Where shall the stranger sit?'` count 1). The L1's amendment to Tacitus
      is the substitution of record.
  - Gap sweep at the round base (the entry's own argument stays the entry
    seat's): `git ls-tree -r --name-only c285b2af... corpus/knowledge | grep -icE "guest|hospital|xenia|hospitium|stranger"`
    → `0` filenames; `git grep -inE "^- topic:.*(guest|hospital|xenia|hospitium)" <base> -- corpus/knowledge`
    → 3 files, and only one names the institution in its topic line
    (`culture-material/cuisine-food-lexicon.md`, "guest-right"). That file is the
    partial owner at section depth — its salt-covenant treatment
    (`cuisine-food-lexicon.md:95,138,170`, bread-and-salt and `namak-halāl`
    loyalty words) owns guest-right only as a table token, not as the legal
    institution (who may claim, who enforces, what refusal costs).
  - **S906** — Ovid, *The Metamorphoses*, Books VIII–XV, trans. Henry T. Riley,
    Gutenberg #26073 (`curl` → `HTTP 200, 853821 B`, byte-identical under both
    UAs; CDX → `20251013025327 status 200`, 853862 B). Anchor as landed:
    viii.618-724, 「Yet one received them, a small one indeed, thatched with straw」 (11 words) — present once in body and capture. Tier B: a translation
    with the translator's argument, cited for the theoxeny story-pattern, not for
    custom. Artifact `reports/round-82/evidence/S906.txt`.
  - **S907** — "Guest", *Encyclopaedia Britannica* 11th edn, vol. 12, Wikisource
    (`curl -sSL ... <url>` → `HTTP 200, 13771 B transferred / 60273 B decoded,
    byte-identical under both UAs; CDX → `20191023112911 status 200`, 8168 B).
    Anchor as landed: the opening definition, 「one who receives hospitality in the house of another」 (9 words) — present once after whitespace folding in
    body and capture. Tier C, dictionary gloss: a lead for the polarity, never
    sole support. Artifact `reports/round-82/evidence/S907.txt`.
- **ADMITTED, superseding the planned reject — EB11 "Guest" is not a reject.**
  The planned ground ("a plain fetch returns the Wikibase scaffold, not article
  prose") was measured false on both artifacts this round: on the live body the
  sentence sits in a ProofreadPage paragraph
  (`grep -n 'one who receives hospitality' guest-plain.txt` → line 518, closing
  `</p>` inside `div.prp-pages-output`), and on the cited capture the same
  sentence occurs once after whitespace folding (raw count 0 — the served HTML
  line-wraps it; the installed record and this seat's independent reading agree
  on both counts). Disposition: mined, tier B; the row's `scope` cell records
  that the article is a single ~55-word gloss, which is the real limit on its
  use, and the tier is C on that ground. The first misread (scaffold-not-prose) is the mined mistake behind the
  new QUALITY 30.
- **REJECTED (fresh disposition) — Frazer, *The Golden Bough*, filed as row S908
  (status `rejected`, tier C, `used-by` an em dash).** Reason: the work's
  framework is the unilinear magic → religion → science stage law that QUALITY 2
  names ("Frazerian evolutionism") and requires to be flagged on first use; a row
  admitting the work as `mined` would license the load-bearing use the calibration
  bar bars, and the lane already cites it only as a flagged historical
  reference (`corpus/knowledge/linguistics/politeness-taboo-euphemism.md:124`).
  The finding is `present`, not absent — the span the row would have to endorse
  is in the body, which is what makes the framework objection checkable: on
  `reports/round-82/evidence/reject-golden-bough.txt`, span
  「In short, magic is a spurious system of natural law as well as a fallacious guide of conduct; it is a false science as well as an abortive art.」 is
  `present` (29 words; `curl` → `HTTP 200, 2331343 B` under both UAs,
  byte-identical; CDX → `20260814122123 status 200`, quote count 1 after
  whitespace normalisation). `flip:` a chapter-scoped admission (for example the
  taboo chapters) filed as tier C with "framework discredited" written into the
  row's own `scope` cell, or a modern critical history that carries the chapter
  without the stage law.
- **REJECTED (carried) — heraldry/emblems knowledge entry.** Carried from
  round 81 (`corpus/lessons/round-81.md`, the heraldry bullet): ground already
  held. Re-verified at this round's base, not re-argued:
  `git show c285b2afb19d4b64320e18df1f55e426bf2d0b0c:corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md`
  → first line `# Heraldry, emblems and inherited identity marks — who bears a
  mark, who grants it, how it passes, and what it is put on`. No new evidence
  this round; carried reject stands.
- **REJECTED (carried, ground disputed) — EB11 "Coin" and "Mint".** Carried from
  round 81, which rejected them as unusable for quotes ("Coin" a stub, "Mint"
  said to render only through client-side transclusion). This round's probe
  re-measures both and files the finding against the carried reason: on
  `reports/round-82/evidence/probe-eb11-mint.txt` the Coin span
  「The form “quoin” is used for the external angle of a building」 is `present`
  and the Mint span
  「a place where coins are manufactured with the authority of the state」 is
  `present` in 47165 characters of visible text (`curl` → `HTTP 200, 61002 B`
  and `HTTP 200, 148302 B`; Mint byte-identical under both UAs, md5
  `d80b03a99ad22efcf24afcf058124ffa`). The carried disposition stands for this
  round because nothing depends on it, but its Mint limb is falsified: the L1
  must either restate the ground (stub-level depth for both articles) or re-open
  "Mint" as a fresh candidate. This seat records; it does not decide.
- **Claim O (operability)** — not this seat's object and not verified here: this
  scribe read no counter, ran no selftest and asserts nothing about
  `tools/check-sources-recheck.py`. The L1 fills this line from the O seat's
  receipt and its `ACCEPT-O-82` verdict; leaving it unwritten is the honest
  state, not a missing admission.
- **Freshness (historically the lowest non-retired axis): paused** — carried
  unchanged from rounds 77–81 by the unresolved round-11 L0 question (operator
  ruling). No stagnation nudge is invoked and no freshness move is declared.
- **Census (frontier totals — the L1 fills the numbers):** the seven
  SOURCES-CONTRACT commands as carried verbatim in
  `reports/round-49/run-validation.py` (`CENSUS`, lines 55–64), run from the lane
  root as `python3 reports/round-49/run-validation.py`.
  - before: the receipt already on disk is `reports/round-82/telemetry/census-start.txt`
    — 34 lines, `ok /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`,
    `census-start-exit=0`, with W04 duplicate-URL and W01 tierC-mined warnings and
    no shape error. The pre-data counts sit in `reports/round-82/telemetry/before.txt`:
    `git show BASE:corpus/SOURCES.md | grep -cE "^[[:space:]]{0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|"`
    → `827`; `git ls-tree -r --name-only BASE corpus/knowledge | grep -c "\.md$"`
    → `255`; the guest-right filename sweep → `0`. Expectation at the end:
    rows `<L1: 831>`, malformed `<L1: 0>`, duplicates `<L1: none>`, tier
    `<L1: A=500 B=314 C=17>`, status `<L1: mined=736 queued=58 rejected=37>`,
    missing used-by `<L1: none once the entry lands>` → receipt
    `reports/round-82/telemetry/census-end.txt`
  - the expectation values above are this seat's dry run on a scratch copy, not
    the lane: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` on the spliced
    copy prints `831`, `NF!=13` prints `0`, the duplicate-id awk prints empty,
    and the used-by loop prints exactly the four new rows' shared entry path.

## Mistakes

Slot for the round's mistake table — classes to check at closure, each with the
command that shows it (the L1 fills id, evidence pointer and fix):

| id | class | check (command) | evidence pointer | fix |
|---|---|---|---|---|
| R82-M1 | registry placement — a row spliced after `## Paths` instead of into the Registry table (the R80/R81 E12 class) | `python3 -c "print([i for i,l in enumerate(open('corpus/SOURCES.md')) if l.strip()=='## Paths'][0])"` vs the row line numbers; the class red is reproduced on `stage/ScribeRows/census-dryrun.txt` (end-append variant: 4 rows outside the Registry) | `<L1>` | `<L1>` |
| R82-M2 | row shape — a literal or escaped pipe inside a cell, or a missing cell | the census `NF!=13` awk; the class red is reproduced on `stage/ScribeRows/census-dryrun.txt` (one injected pipe → `1`) | `<L1>` | `<L1>` |
| R82-M3 | anchor drift — the declared word count disagrees with the 「」 span, or the span is absent from the body the row names | re-run each capture record's `re-open` line; the round's own count check is `len(span.split())` against the `(N words)` cell | `<L1>` | `<L1>` |
| R82-M4 | live-vs-capture mismatch — a row's capture is a different page, or the quote is present on one artifact and absent on the other (the S907 near-miss: a reject reason filed against the wrong artifact) | per-row `curl` of the live URL plus `curl` of the capture's `id_` form, then `grep -c -F` on the span in both | `<L1>` | `<L1>` |
| R82-M5 | carried-reason rot — a carried reject whose stated ground no longer holds (this round: the EB11 "Mint" transclusion ground) | re-probe every carried reason's URL and record `present`/`absent` per the QUALITY 27 shape; `probe-eb11-mint.txt` is the worked example | `<L1>` | `<L1>` |
| R82-M6 | used-by pointing at an entry that never lands — a `mined` row whose path is absent at the census end | the census used-by loop (`[ -e "$p" ] || echo missing: $p`) | `<L1>` | `<L1>` |
