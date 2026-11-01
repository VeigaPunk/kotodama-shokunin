# Round 81 — kotodama (Windows host, 2026-11-01)

Base `1c0e3d4d712da2fae25d27ece1eb799d26db0975` (round-80 verifier
spot-check commit). Freeze `b1ebb6097e3a269c2dc53fe73d5ea07316c7bd25`,
superseded for grading by the re-freeze `d583ccae9a8f999a2428ea94d033293f760265cc`
(claim C source-marker over-specification; r79/r80 precedent, recorded in
`reports/round-81/counter-revisions.md`). Claim O lands
`d284058fef871363c34d33a57194158c36ddf357`; claim C lands
`1ede6961ed6979a0a44f1a58232f3ef7bad2d776` then counter r2
`c9dd27a10b7702e386e9a84a9b5bf3793928170f`; claim D lands
`4ad08c83767bb6c7fb9bd4421a778b2550a0dc5a`.

## Gate

Candidates considered and dispositioned (frozen pre-data at
`reports/round-81/claims.json`, which carries the fresh-start dispositions):

- **ADMITTED — claim O (operability): the round-80 W2 mutation pass made
  re-runnable from committed bytes, plus the replace-ref junk template
  completed by a committed builder** (the round-80 spot-check's routed notes 6
  and 5). `reports/round-81/mutants/w2-mutants.py` (sha `048f1c74…`): reads
  the hardened guard at the pinned revision (sha `cca7db17…` asserted), runs
  the clean selftest green first, builds five single-hardening-removal
  mutants with pinned shas — **m1 and m3 are byte-exact reproductions of the
  r80 recorded shas** (`ba5d8b91…`, `f998e41b…`), m2/m4/m5 are deterministic
  new pins (`71143bea…`, `6f1c3379…`, `942f4c85…`) with the r80 scratch shas
  kept historical in the receipt header — and verifies 5/5 caught plus the
  hardened env-probe control (0 of 4 injected `GIT_*` variables leak).
  `reports/round-81/fixtures/replacerefs/build-fixture.py` (sha `aaefc366…`):
  builds a scratch fixture repo (good/evil `probe.txt` commits + `git
  replace`), completes the r80 template in place (fills both placeholders,
  adds `observe.line`, sets the stated values to the shadowed view), and
  re-derives the r80 receipt pair from committed bytes: r79 bytes exit 0
  `PASS pairs=1` (the lie blessed), hardened bytes exit 2 `REFUSED --repo
  carries refs/replace entries`. Counters: `ACCEPT-O-81: PASS legs=6/6` at
  the re-freeze lands (`telemetry/lands-o81-graded.txt`,
  `lands-o81-graded-r2.txt`); standalone tip receipts
  `telemetry/w2-rerun-at-tip.txt`, `replacerefs-at-tip.txt`.
- **ADMITTED — claim C (calibration, capability acquisition): the
  orphaned-evidence sweep** (the round-80 closure's carry-in duty 4, made
  mechanical). `tools/check-orphan-evidence.py` (sha `e99658df…`, 11-check
  selftest) scans all 71 closed fleet round reports plus the lane's 32
  verifier spot-checks (103 documents, 510 distinct cited paths) and
  classifies every cited lane-side path against the committed tree. Red-before
  at base: **3 orphans over 510 cited paths, exit 1**
  (`telemetry/orphan-sweep-red.txt`, landed first with the dispositions record
  in the carry-in commit `316641d8`). Zero ORPHAN-ONDISK: nothing landable
  exists; the three ORPHAN-ABSENT citations are dispositioned honestly in
  `reports/round-81/annotations/r81-orphan-dispositions.md` (the r68
  fixture-hypothetical prose path; the r78 S884 drift already bounded by the
  r79 correction with unknowable bytes; the r63 spot-check's own historical
  quote of its then-repaired dead pointer). Counters:
  `ACCEPT-C-81: PASS legs=6/6` at its lands `c9dd27a1` (`telemetry/
  lands-c81-graded-r3.txt`); the capability row enters the SCORECARD
  capabilities table this round.
- **ADMITTED — claim D (depth): judicial proof as a lexical surface.**
  `corpus/knowledge/myth-symbol/ordeal-judicial-proof-rituals.md` lands as the
  255th knowledge file: topic/gap/sources/couples/source/verified-at/recheck/
  scope header, six-decision table (reach, carrier, boundary, element,
  administration, exit), attested anchors with exactly one S-id per cited
  line (`tools/check-cited-lines.py` sha `a9b0fbd5…` prints 0 findings),
  craft checklist, NON-CANON worked example, lore handoff. Three rows opened
  this round by ordinary means (plain curl, HTTP 200 each, same-page Wayback
  captures on file, automation: none; capture records
  `reports/round-81/evidence/S901.txt`–`S903.txt`):
  - **S901** — Henry Charles Lea, *Superstition and Force* (essays first
    issued 1866), Gutenberg #58750, fetched 2026-11-01 (HTTP 200, 1460416
    bytes); Wayback capture 2026-01-14, status 200. Located quote (12 words):
    「I swear alone, if thou darest, deny my oath and fight me」 Tier A for
    the 19th-century standard history of the wager of law, wager of battle
    and the ordeal.
  - **S902** — J. G. Millingen, *The History of Duelling* vol. 1 (London,
    1841), Gutenberg #57326, fetched 2026-11-01 (HTTP 200, 574813 bytes);
    Wayback capture 2026-02-16, status 200. Located quote (23 words):
    「The first legal establishment of these ordeals is to be found in the
    laws of Gundebald, King of the Burgundians, A. D. 501」 Tier A for the
    judicial-combat record and its transition into the duel of honour.
  - **S903** — "Ordeal", *Encyclopaedia Britannica* 11th edn, vol. 20 (1911),
    Wikisource transcription (article fully transcluded server-side — a plain
    fetcher receives the prose; the EB11 "Coin"/"Mint" articles were probed
    first and rejected: "Coin" is a stub, "Mint" renders only via client-side
    transclusion, so a plain fetcher cannot find quotes there), fetched
    2026-11-01 (HTTP 200, 87230 bytes); Wayback capture 2026-07-11, status
    200. Located quote (16 words): 「in a Scandinavian law it is prescribed
    that the red-hot iron shall be carried nine steps」 Tier B (survey, a
    century old; period claims stop at 1911).
  Frozen counter `ACCEPT-D-81: PASS legs=7/7`, exit 0, at the re-freeze lands
  (`telemetry/lands-d81-graded.txt`, `lands-d81-graded-r2.txt`). Gap
  discipline: the topic-line sweep at base returns 0 owners; the oath-side
  (`binding-speech-complex.md`), omen-side (`divination-omen-systems.md`),
  rite-side (`ritual-liminality.md`) and liturgical-register neighbours are
  pointed one-way in §1; the entry owns no canon decision.
- **Junk landings (QUALITY 26b shape, post-landing):** seven junk commits —
  w2 generator deleted (GEN), claims shrunk in the graded tree (FROZENCFG),
  checker deleted (TOOL), red receipt deleted (RECEIPT), entry deleted
  (ENTRY), decision-table-row S-id mutant (LINT), S902 status flipped (ROWS)
  — each FAILs on its named leg (`telemetry/junk-landings.txt`, generator
  `counters/junk-fixtures.py`, run against a checkout-free plumbing clone on
  each claim's own lands, the original freeze `b1ebb609` as the freeze —
  see R81-M4).
- **REJECTED (carried): naming-systems expansion** — reviewed and not
  admitted r77, upheld r78/r79/r80; no new evidence this round.
- **REJECTED (carried): dining/tableware knowledge entry** — ground already
  held (r79 Gate); unchanged.
- **REJECTED (fresh disposition): heraldry/emblems entry** — considered as a
  depth candidate and ruled out before declaring: ground already held
  (`myth-symbol/heraldry-emblems-identity-marks.md` exists at base).
- **Fresh-start dispositions (spot-checked on committed bytes before
  declaring):** r76 — the frozen counter's FAIL is on file
  (`reports/round-76/telemetry/measures-c-final-c28ea.txt`: `ACCEPT-C-76:
  FAIL legs=11/13`); not re-run for a flip (a do-nothing artifact). r77 —
  `grep -c '^## Gate' corpus/lessons/round-77.md` = 0 (the records-discipline
  defect named then; this round files its Gate first-class). r78 — the S884
  drift is bound by the r79 correction
  (`reports/round-79/corrections/ca79-r78-s884.md` names the
  `amend-2026-10-23.md` registry row). **Ruled out before declaring:**
  (a) re-litigating the carried rejects with no new evidence; (b) a freshness
  move — paused by the open round-11 L0 question, no stagnation-nudge
  evidence on file (SCORECARD carries no saturation line/window);
  (c) re-running r76's frozen counters for a flip; (d) editing frozen r79/r80
  graded bytes; (e) the heraldry entry (ground held); (f) transport/road and
  market-measure entries (ground held by `transport-mobility-lexicon.md` and
  `trade-economy-lexicon.md`).
- **Freshness (historically the lowest non-retired axis): paused** by the
  unresolved round-11 L0 question — operator ruling, same disposition as
  rounds 77–80. The stagnation nudge is not invoked; the pause is the
  recorded reason no freshness move was declared.
- **Append-only carry-in records landed first:** the orphaned-evidence red
  receipt + dispositions record + census-start receipt committed as
  `316641d8` before any claim work, per the carry-in's ordering.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R81-M1 | frozen-config defect — claim C's `tool_markers` over-specified the literal `SELFTEST: PASS`, which exists in the checker's runtime output but not in its source bytes (the source formats the verdict), so the first graded C run failed TOOL/REDRUN at lands `4ad08c83` | `reports/round-81/telemetry/lands-c81-graded-r1-TOOL-marker.txt` (`LEG FAIL TOOL (marker missing: 'SELFTEST: PASS')`, `ACCEPT-C-81: FAIL legs=4/6`, exit 1 — committed as the red-before) | the counter's own graded run at the lands | recorded re-freeze `d583ccae` (supersedes `b1ebb609` for grading, r79/r80 precedent): marker corrected to `SELFTEST:`, no predicate moved; re-freeze note inside claims.json; `counter-revisions.md` row |
| R81-M2 | counter defect — `accept-c81.py` REDRUN invoked the fresh checker with `--repo`, a flag the checker does not define, so the fresh run answered exit 2 (argparse usage error) and the leg read it as an orphan-set mismatch with the checker's stderr swallowed | `reports/round-81/telemetry/lands-c81-graded-r2.txt` (`LEG FAIL REDRUN (orphans [] != frozen set (exit 2))` — committed as the red-before) | the graded run after the re-freeze (the argv bug was invisible to the selftest because the stub checker ignores its argv) | accept-c81 r2 (`QUALITY 23` protocol): argv fixed, no predicate moved, selftest re-run green (`telemetry/selftest-c81-r2.txt`, canonical `selftest-c81.txt` regenerated to the r2 sha), revision row in `counter-revisions.md`; class note: a selftest stub that ignores its argv cannot see argv defects — the next counter's selftest stub should assert it received the expected argv |
| R81-M3 | mechanical (new battery file) — the junk battery's grade helper passed a list into a `*args` wrapper (`sh(argv)`) and its D-section calls omitted the parent argument; the battery died after one fixture on the first run and after four on the second | `reports/round-81/telemetry/junk-landings.txt` first and second runs (superseded in scratch; the committed run is the passing third) | the battery's own TypeError traceback on stdout | `sh(*argv)` and a `parent=None` default (`parent or args.lands`); class note: a subprocess helper with `*args` signature and a caller passing a list is a recurring shape on this host's fixtures — check it before first run |
| R81-M4 | landing geometry — the junk battery's first complete run used the re-freeze `d583ccae` as its freeze, but the junk landings build on each claim's own lands, none of which descend from the re-freeze, so every fixture was refused (`freeze is not an ancestor of lands`, exit 2) before any leg ran | `reports/round-81/telemetry/junk-landings.txt` second run (superseded in scratch; refused verdicts visible in the first complete receipt) | the battery's own refused verdict lines | the battery grades with the ORIGINAL freeze `b1ebb609` (ancestor of all three lands commits); class note: when a round re-freezes, the freeze used by post-landing batteries is the freeze each graded lands actually descends from, not whichever commit is "the freeze" at the tip |
| R81-M5 | registry placement — the three new SOURCES rows were appended at the END of `corpus/SOURCES.md`, past the Registry section's `## Paths` boundary, so the census-end answered `E12 S90x row outside Registry section` and exited 1 (the same E12 class round 80 hit) | `reports/round-81/telemetry/census-end.txt` (the failed run: three E12 lines, `census-end-exit=1`, kept as the red-before) | the round-end census itself | this round's own rows moved into the registry table directly after the S900 row (no filed history rewritten); census re-run green (`census-end-r2.txt`); the D counter re-graded at the fix tip (placement-insensitive line scan, still PASS) — class note: the registry table ends at the `## Paths` heading; an append must land inside the table, which a plain `>>` append cannot do |

## Sources & frontier

Registry rows 824 → 827 (S901, S902, S903 opened this round; no prior-row
cell changed). Counting: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` = 827 (at the claim-D lands `4ad08c83`; 824 at base
`1c0e3d4d`). Knowledge files 254 → 255
(`git ls-tree -r --name-only <rev> corpus/knowledge | grep -c '\.md$'`).
Census receipts: `reports/round-81/telemetry/census-start.txt` (exit 0, 824
rows at the carry-in commit — W01/W04 warnings only, the pre-existing
profile), `census-end.txt` (the failed first run: three E12
row-outside-Registry lines, exit 1 — kept, see R81-M5) and `census-end-r2.txt`
(green after the placement fix).
Sourced claim: D rests on S901/S902/S903 (opened this round). The
EB11 "Coin"/"Mint" articles were probed and rejected before the entry's
sources were chosen (stub / client-side transclusion — a plain fetcher cannot
find quotes there; no rows wasted on them).
