# CriticClaimD — falsify.md (round 82, hyaku 15, wave 1)

Seat: CriticClaimD (leaf, no subagents). All paths absolute; every command and raw output below was
run this round. Base revision `c285b2afb19d4b64320e18df1f55e426bf2d0b0c` ("base"); D lands `277fdf4a`;
freeze `25907323` (per L1 status message). Scratch `/fast/scratch/hyaku/kotodama-r82/CriticClaimD/`
(removed before yield; stage files kept).

## 1) Absence census re-run at base — claim ground

Filename sweep at base:

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only c285b2afb19d4b64320e18df1f55e426bf2d0b0c -- corpus/knowledge | wc -l
255
$ git -C ... ls-tree -r --name-only c285... -- corpus/knowledge | grep -c "guest"
0
```

Topic sweep at base (`git grep -n -i -E "guest|hospitalit|xenia|hospes" c285... -- corpus/`):
no file owns the surface. Adjacent owners found (subsections, not owners):

- `corpus/knowledge/culture-material/cuisine-food-lexicon.md:95,138,170` — "Guest-right and the salt
  covenant" as food-lexicon material (khleb-sol, namak-halāl): owns the *lexicalization*, not the
  institution. The new entry must couple to it and not restate it.
- `corpus/knowledge/myth-symbol/ritual-liminality.md:21` — threshold/safe-conduct ("the guest's
  token") framing owned by liminality.
- `corpus/knowledge/myth-symbol/creation-myths-taxonomy.md:49`, `direction-symbolism.md:99`,
  `number-symbolism.md:28,118` — incidental craft hooks (muskrat guest-right, honored-guest side,
  Loki-as-13th-guest, the last explicitly flagged as modern reconstruction).
- Per-civilization hospitality rows (ainu, arabia-pre-islamic, celts, pacific-northwest, igbo, ...)
  — instance rows, not the sacral-legal institution.

Exact-phrase check `git grep -n -i "guest-right" c285... -- corpus/` hits only the subsections above.
**Verdict: ground is free — 0 of 255 knowledge files at base carries a guest-right filename and no
file owns guest-right as a sacral-legal institution. Claim D's ground stands.** This independently
reproduces the frozen claim `before` text ("filename sweep ... -> 0 of 255 files").

## 2) Counter attack — `reports/round-82/accept-d82.py` (read at working tree; legs read from lines 153-333)

### (a) ENTRY — can an entry hit every marker and be a stub?

No, post-freeze the leg is a pure equality test: `if sha_bytes(eb) != cfg["entry_sha256"]: ok=False`.
The frozen config pins `entry_sha256 = c7fb9bc4bfdfa64c084f770e70bdd9057cc0c10b5b8071786fcf3b95e75d2a35`,
`entry_min_bytes = 8000`, `entry_max_bytes = 120000`. So the smallest file passing ENTRY+COUPLES+NOCANON
is **exactly the pinned entry** — no other byte sequence can pass. Measured at lands:

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 277fdf4a:corpus/knowledge/myth-symbol/guest-right-hospitality-law.md | wc -c
29020
$ ... | sha256sum
c7fb9bc4bfdfa64c084f770e70bdd9057cc0c10b5b8071786fcf3b95e75d2a35  -
```

29020 — `git show 277fdf4a:<entry> | wc -c` (3.6x the 8000 floor; not a floor-hugger). Sha matches the
pin. Residual defect: the pin was computed at freeze time and the counter cannot audit *that* step; under
a sha equality test the marker/size sub-checks are redundant. Stub risk is bounded to freeze-time honesty,
which no leg covers.

### (b) ROWS — does it bind the quote to the right row?

No. The leg only checks the anchor quote's *shape*: a span inside 「…」 in registry cell 5 with ≤ 25 words
(`re.search(r"\u300c([^\u300d]+)\u300d", cells[5])`), plus `cfg["entry_path"] in cells[10]` (used-by text),
plus the capture record existing and containing the literal substring `"row: S904"`. It never compares the
quote against the source bytes or the capture record's content. **A pasted/fabricated quote passes ROWS.**
Strongest observed form: the entire *source identity* of S905 changed mid-round — planned *The Poetic
Edda* trans. Bellows (Hovamol) per the round plan; landed row is **Tacitus, *Germania*, trans. Church &
Brodribb (Wikisource)** — and no leg notices, because rows are bound only by kind/tier/status/opened
strings (`book`/`A`/`mined`/`2026-11-04`). The swap is documented in the registry row and capture record
(`reports/round-82/evidence/S905.txt` at lands), so it is evidentially grounded, but it is invisible to
the instrument: had Germania not been fetched either, no leg would have failed.

### (c) ROWCOUNT — four rows appended but the entry cites none?

**Passes.** ROWCOUNT counts rows only: `n_after >= 831` with `rowcount_before (827) < 831`. Measured:

```
$ git show c285...:corpus/SOURCES.md | <RULE-row counter>
827
$ git show 277fdf4a:corpus/SOURCES.md | <RULE-row counter>
832
```

827 — base; 832 — lands (claim `after` says 827 -> 832; counter floor 831 — consistent). The entry side is
not enforced: LINT passes **vacuously on a zero-citation file** (measured, tool sha at lands matches the
pin `a9b0fbd5…`):

```
$ sha256sum tool.py   (extracted: git show 277fdf4a:tools/check-cited-lines.py)
a9b0fbd5809b3764b2309cd8a82625c75ca1d6dd7c498309387050312078804a  tool.py
$ python3 -B tool.py nocite.md     # synthetic 0-citation entry
CITED-LINES: 0 finding(s) in 1 file(s)
rc=0
$ python3 -B tool.py bad.md        # control: 2-id line + table S-id is detected
MULTI-ID ...bad.md:3 S904,S905
TABLE-ID ...bad.md:4 S904
CITED-LINES: 2 finding(s) in 1 file(s)
rc=1
```

So "rows appended, used-by cells name the entry, entry cites zero S-ids" passes ROWS + LINT + ROWCOUNT.
The landed entry does cite its rows (S904 x7, S905 x7, S906 x6, S907 x2 — `grep -o -E "S90[0-9]" | sort
| uniq -c` on the landed bytes), so this is an instrument gap, not an artifact defect.

### (d) SEPARABLE — can the entry land another claim's paths?

Yes. Frozen `allowed_d_paths = ["corpus/knowledge/myth-symbol/guest-right-hospitality-law.md",
"corpus/SOURCES.md", "reports/round-82/"]` plus `sibling_paths = ["tools/check-sources-recheck.py"]`;
the bad-path test is `p == a or p.startswith(a)`. The directory prefix `reports/round-82/` admits the
whole shared round dir, including **claim O's counter `reports/round-82/accept-o82.py`** and O telemetry
(`controls-o.txt`, `junk-o.txt`, `lands-o82-graded.txt`), and `counters/junk-fixtures.py`. No leg pins
either counter's bytes — accept-d82.py only *stamps* its own sha in the receipt
(`# counter sha256 (self): …`); nothing compares that stamp to a frozen value, so an edited counter would
grade with edited semantics and still stamp honestly. FROZENCFG pins `claims.json` bytes (the one shared
config), which is the only cross-claim integrity anchor. Cross-claim leak is open in the instrument; no
evidence it was exploited at lands (I did not diff O's files — outside my seat).

### Config-vs-narrative divergence (calibration)

The seat assignment says "S907 is a recorded reject (verify or refute)". The frozen entry82 config demands
S907 **mined** with an anchor quote; the landed row is `status='mined' tier='C'` with quote 「one who
receives hospitality in the house of another」, and the row records the refutation of the scaffold-only
reading ("the article prose follows a raw Parsoid template block … a tag-stripper emitting no separator
reads the page as scaffold-only"). The actual reject moved to **S908 (Frazer, *Golden Bough*)** — claim
`after` documents it ("S908 (rejected, Frazer) … 827 -> 832") and `reports/round-82/evidence/
reject-golden-bough.txt` exists at lands. I did not fetch any URL this round (no probes); the S907
refutation and S908 reject stand on the round's recorded fetch receipts, which I inspected as data only.
Consistent once all three artifacts are read together; the seat assignment text is stale relative to the
freeze. No contradiction between frozen counter and landed bytes.

## 3) Public-domain source quality (tiers vs honest scope)

Landed rows and the scope that survives:

- **S904 Butler, *Odyssey* (1900 prose, Gutenberg #1727), tier A** — A only for *what Butler's
  translation says*. Not evidence for Greek usage (ξενία, ξείνιος) or for "Homer's Greek". The row's
  teaches cell already encodes this ("Butler's prose renders Zeus as 'Jove', so cite the translation's
  wording, not Gr…"). Honest; no inflation.
- **S905 Tacitus, *Germania*, Church & Brodribb (1877), tier A** — A as translation-text. As evidence of
  Germanic *practice* it is a Roman senator's second-hand ethnography (one step further from the practice
  than a native text's translation). The teaches cell's phrasing "hospitality is *stated as* a national
  institution with a religious sanction" keeps the claim on the text; the entry must not upgrade it to
  "Germanic peoples did X". Borderline-honest; guarded by the entry's `review_only` note ("cited for what
  they say, not for Greek or Latin usage") — keep that guard on the Germania side too.
- **S906 Riley, *Metamorphoses* VIII–XV (1851, literal prose with editorial fable headings), tier B** —
  B is correct and *not* inflated: the editorial apparatus is 19th-century commentary, not Ovid. Teaches
  cell scopes it to "the narrative pattern". Honest.
- **S907 EB11 (1911) "Guest", tier C** — C, lead-only, is honest and the claim `review_only` forbids sole
  support. Honest.
- **Planned Bellows (1923, Hovamol)** — never landed (superseded by Germania). Had it landed at tier A,
  A-for-translation-text would have been defensible (a 1923 English rendering of the 13th-c. Codex Regius),
  with the same "not Old-Norse philology" scope limit. Not a live defect.

**No R81-V1-class tier inflation found in the landed set.** The tiers match the honest scopes, provided
the entry's citation lines keep each anchor on the translation's wording (spot-checked: entry carries 22
S-id mentions across S904-S907; stance audit of each line is review-only and I did not re-adjudicate it).

## 4) Strongest one-pass entry and its failure mode

Strongest: the **breach-ladder architecture** — degrees of guest → the host's owed package → markers and
seals (hearth, salt, handclasp, gift) → the breach ladder (demand vs request, satiety vs sack) → sacral
sanction (theoxeny verdict in S906, Zeus-guard in S904, feud-coupling in S905) → the guest's reciprocal
half — with the guest/host~hostis double valence (S907) as the lexicon interface and a NON-CANON worked
derivation on an invented culture.

Failure mode that makes it reference rather than craft (QUALITY 3/4): §2 "Six design decisions" written
as an attestation survey — restating what S904/S905/S906 show — instead of six worldbuilder decisions
each with a default answer, a coupling obligation, and an invented-culture application; and §5's worked
example collapsing into a Baucis-and-Philemon retelling (citation-shaped prose) instead of a NON-CANON
derivation. The counter is stance-blind here (LINT/NOCANON/marker legs cannot see epistemic posture);
only the entry's own `review_only` scoping and reviewer eyes catch it. Landed `review_only` keys pre-commit
to exactly this reading, which is the right guard.

## Smallest safe corrections (for the canonical judge; I implemented nothing)

1. ROWS: pin each anchor quote string (and a source-name/URL fingerprint) in the frozen config and have
   the counter compare — closes fabricated quotes and silent source swaps.
2. LINT/ROWS: add the positive direction (each mined row id must occur in the entry text, or ≥1 anchor
   citation per mined row) — closes the measured vacuous pass.
3. SEPARABLE: narrow `reports/round-82/` to the subdirs claim D actually writes (`evidence/`,
   `telemetry/`) plus exact paths, and pin both counters' bytes at freeze, comparing the receipt's
   self-sha at grade time — closes the cross-claim leak and the edited-counter hole.
4. ENTRY: no change (sha pin is correct); document that marker/size sub-checks are redundant under it.

## Checks not run (reported as unrun)

- Any network fetch or fetch-receipt re-verification (S904-S907, S908, Wayback captures) — unrun by
  design (L1 directive: no new probes; leaf seat). Fetch claims stand on the round's recorded receipts.
- Re-execution of accept-d82.py end-to-end at lands — unrun; leg semantics were read from source and the
  graded-green status is the L1's report. Pin equalities that matter (entry sha, lint-tool sha, rowcount)
  were re-measured above.
- O-claim file diff at lands — not attempted (outside seat; noted as unrun).
