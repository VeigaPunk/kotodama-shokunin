# Round 71 (2026-10-25, hyaku run 6, L1 kotodama-r71)

Claims: C (coverage, sourced dance/performance/movement register · frontier → core),
Ca (calibration, V70-1..V70-5 repairs + item-10 quarantine verdicts), D (depth,
no-git selftest guard, V70-6). Round shape: two v1 waves — wave 1: 37 seats
(10 scout, 1 connector, 5 executor, 1 scribe, 8 reviewer, 7 critic, 3
mutation-tester, 2 sentinel; 18/37 attack roles, 48.6%) dispatched in one
batched task call; wave 2: 41 seats (below). Round total 78 seats, ≤128.

## Gate

All 13 claim-C rows opened 2026-10-25 (URL + access date + ≤25-word located
quote, verbatim from the fetched page; the full quote list is in
`.ufo/waves/round-71/w1/ScoutOpenSourcesC.md` and was re-located by the L1 on
each live/capture URL):

| source | access date | quote (≤25 words) | grounds | verdict |
|---|---|---|---|---|
| S861 — UNESCO Tango 00258 | 2026-10-25 | "the music, dance and poetry of tango both embodies and encourages diversity and cultural dialogue" | element record 00258, inscription narrative ¶2; Wayback capture 20260925201518 | admitted |
| S862 — UNESCO Mevlevi Sema 00100 | 2026-10-25 | "the whirlers begin to rotate on their left feet in short twists" | element record 00100, inscription narrative ¶3; capture 20220323094705 | admitted |
| S863 — UNESCO Chhau 00337 | 2026-10-25 | "Its vocabulary of movement includes mock combat techniques" | element record 00337, inscription narrative ¶2; capture 20210514035531 | admitted |
| S864 — UNESCO Oruro 00003 | 2026-10-25 | "the dancers walk the four kilometres of the processional route" | element record 00003, inscription narrative ¶3; capture 20210227223454 | admitted |
| S865 — UNESCO Flamenco 00363 | 2026-10-25 | "Flamenco baile is a dance of passion, courtship" | element record 00363, inscription narrative ¶2; capture 20210302140159 | admitted |
| S866 — UNESCO Talchum 01742 | 2026-10-25 | "An ensemble of six to ten musicians accompanies masked performers" | element record 01742, inscription narrative ¶1; capture 20241111072724 | admitted |
| S867 — UNESCO Kabuki 00163 | 2026-10-25 | "aragoto (rough style) and wagoto (soft style)" | element record 00163, inscription narrative ¶2; capture 20200330004935 | admitted |
| S868 — ABT Ballet Dictionary | 2026-10-25 | "the positions of the feet are standard in all methods" | Ballet Dictionary page, "Positions of the arms"; live | admitted |
| S869 — RAD Benesh International | 2026-10-25 | "Benesh Movement Notation (BMN) is a system for documenting human movement" | Benesh International page, opening ¶; capture 20260907171642 | admitted |
| S870 — ICKL | 2026-10-25 | "known as Kinetography Laban or Labanotation" | ICKL homepage, opening ¶; live | admitted |
| S871 — Natyashastra (Ghosh) | 2026-10-25 | "the Aṅgahāras consist of six, seven, eight or nine Karaṇas" | chapter IV (karaṇa) aṅgahāra section; live (Wisdom Library) | admitted |
| S872 — Abhinaya-darpana (Coomaraswamy) | 2026-10-25 | "an encyclopedic manual of the art of gesticulation" | mirror-of-gesture edition preamble; live | admitted |
| S873 — SEP The Philosophy of Dance | 2026-10-25 | "This is a vexed methodological question" | entry section 1; live | admitted |

rejected this round: ScoutOpenSourcesC refused 8 candidates for claim C —
ich.unesco.org live CAPTCHA walls (flip: Wayback captures of the same elements,
used), breaking/b-boying (no UNESCO inscription; flip: Flamenco/Talchum),
Capoeira (no capture; flip: Flamenco), ROH Ballet Terms (live 500, no capture;
flip: ABT), Dance Notation Bureau (stale captures; flip: ICKL), Princeton Noh
(live 403; flip: Kabuki), EFDSS Morris pages (soft-404), Britannica/RAD live
403 (flip: Wayback). None is admitted as a row; each carries reason + flip.
This is the explicit reject-sweep statement (V70-5).

## Mistakes

| class | evidence | captured-by | fix | state |
|---|---|---|---|---|
| stale-premise | claim C's frozen before-sweep `grep -rniE '^- topic:.*(danc|…)…'` matched `funerary-material-culture.md:4` ("avoidance") — the declared "prints nothing" was false as written (ScoutDanceOwners, CritClaimSizing) | word-bounded sweeps (`\b(danc|choreograph|movement culture|performance)\b`) | claim re-frozen pre-data with word-bounded sweep; entry `- gap filled:` names the word-bounded sweep | new |
| number-drift | claims.json wave-1 seat count said 34; 37 seats actually dispatched | counts must match the validated spec | report names actual 37; claims.json wave metadata corrected in report | new |
| landing | running `reports/round-49/run-validation.py` in the lane rewrites its own filed `validation.json` in place (observed transiently by ScoutLessonMistakeSweep; restored) | QUALITY criterion 17/19 (receipts run at the revision they stamp, in clones) | never run historical runners in the lane; derive baselines in a clone | kept |
| attribution | round-70 receipts stamped "measured at lane 6cb51a4+landed edits" while the after-state first exists at acc2d614 (V70-2) | QUALITY criterion 19 | S860 verify-at repointed to acc2d614; full 17/19 headers re-stamped (V70-1) | new |
| control provenance | claim D's declared no-git leg hard-codes -C <lane> and copies the LIVE worktree, so at base it returns the after-state (CritDoNothing); controls-d regenerated rev3 tree-parameterized | none (verbatim control not base-sensitive) | parameterization routed with the D guard fixes (R71-M6/M11) | new |
| counter-gap (fixed) | wave-2 MutCa probes survived two checks in accept-ca.py: preserved-bytes leg accepted any `#` first line; verdict-table id set not pinned to the 21 slice ids — both fixed in-round | wave-2 seat MutCa | hardened counter re-passes ACCEPT-CA-71; receipt re-stamped | fixed |
| governance mismatch | wave context said seats never mutate the lane, yet executor briefs assigned lane-file drafts (accept-d.py / accept-ca.py stubs); writes were brief-authorized but contradicted the context invariant (CritWaveEvidence A4) | none (context vs brief mismatch) | recorded; next rounds' contexts exempt assigned write paths explicitly | new |
| gate-shape blind spot | `tools/check-gate-quotes.py` row pattern only accepts bullet rows, so pipe-table Gate rows (rounds 69-71) parse as 0 rows and report 0 findings for any quote length (RevGate) | none (MutGateQuotes ran only bullet-row selftest fixtures) | routed fix: accept `^\|\s*S\d+` rows, scan the quote cell, add table-form selftest cases; Ca's V70-3 leg measures words directly (25) | new |
| instrument-provenance | `reports/round-71/accept-c.py` first appears in the data-landing commit, not at the freeze commits; the frozen shell counting command is re-verified by wave-2 seats at HEAD (36/243/797 exit 0) | wave-2 seat Filler39 | recorded; the python counter is the committed instrument whose receipt (measures-c.txt, committed c21213ab) matches; non-author closure may re-run either | new |
| guard-gap | claim D's no-git guard only checks `rev-parse --is-inside-work-tree`; shallow clones and git-less copies nested in another repo still false-red (`SELFTEST: 1/2` exit 1) because commit 793f797 cannot be read (RevCounterDM, CritGaming3) | none | routed fix for round 72: guard on `git rev-parse --show-toplevel` == lane root and `git cat-file -e 793f797^{commit}`; declared legs (0/2/0) verified; "never a craft red" scope = exports outside any git work tree | new |
| declared-counter defect | claim Ca's frozen shell counting command ends with an awk leg splitting on `|` (markdown rows start with `|` → 0); found by wave-2 seat Filler35; canonical `accept-ca.py` counts 21/21 | the freeze rule | shell command unedited; defect logged old→new; committed python counter is the named executing instrument | new |
| misroot | wave-1 seat ScoutQuarantineFetch2 wrote seven fetch artifacts to the fleet root (s795.pdf, s796.pdf, s804/s814/s816/s817.html, s820.pdf) | none (write-scope sentinel read dispatch instructions, not the filesystem) | relocated byte-exact into `.ufo/waves/round-71/assimilation/fetches/`, cmp-verified, fleet copies deleted at `ccadb59`; dispatched context will mandate /tmp/<seat>/ downloads + disclosure | new |
| trend-observables | round-71 report filed quality/discernment `improved` while LEARNING.md observables did not fire (no re-verified entry; no outside spot-check; subagent wave seats do not count) — same class as V70-4 | none (criterion absent) | QUALITY criterion 20 added; report Trend verdicts corrected to expansion improved / quality unchanged / discernment unchanged; hyaku non-author closure is the round's spot-check | new |
| vacuous-counter-legs | wave-2 RevCounterC probes: four of accept-c.py's seven legs can pass vacuously (sweep `\bdanc\b` never matches “dance”; opened-date/id floor unchecked; any S-id anywhere counts; Registry-scope ignored) | none | routed counter hardening for a later round (word-stem sweep, opened-date leg, body-citation leg, Registry-scope leg); today's pass is grounded in the actual files | new |

## Corrections (round 70)

Full dispositions: `reports/round-71/corrections-r70.md` (V70-1..V70-5).
SCORECARD.md carries the round-70 trend-correction row. The round-70 lesson
Gate quote is trimmed to 25 words. S860 verify-at old `6cb51a4` → new
`acc2d614` (logged in corrections-r70.md).

## Corrections (round 71 declaration, pre-data)

claims.json was re-frozen pre-data after wave-1 attacks with documented
corrections (C word-bounded sweep; Ca per-file header legs, direct quote word
count, marker-preservation leg, explicit scorecard/lesson greps, verdict-table
schema; D no-git leg archives the measured worktree minus .git and
distinguishes genuine absence from git/environment errors). No data had landed;
predicate sentences and targets unchanged.

## Quarantine

Adoption stays CLOSED (wave-4 quarantine-first). The 21-row verdict table:
`reports/round-71/telemetry/quarantine-verdicts.md` (PRESENT 10 · REFUSED 6
· UNVERIFIABLE 5). Id collisions S859/S860 (lane vs package) re-derived and
recorded at `.ufo/waves/round-71/assimilation/` (reg-ids 784, staged-ids 132,
collisions S859 S860; id-renumber-map.json S874→S1005 by document). No
shokuknow bytes adopted, appended or renumbered. `considerthese/` absent for
this lane (recorded).

## Frontier-step

Registry 784 → 797 rows (S861–S873 opened and mined this round); census exit 0
at start (`reports/round-71/telemetry/census-start.txt`) and end
(`census-end.txt`, W04=28 standing); README sweep exit 0. Claim C is the
sourced claim: its 13 rows are this Gate.


Wave-2 re-open refinement (ScoutReopenRows): verdicts 10/6/5 re-confirmed; two REFUSED rows are URL↔quote mispairings rather than payload loss — S779's spans live verbatim on wlt.hubei.gov.cn (national-list article), S814's fragment is an NDC10 classification note in the NDL `NDC10code202206.pdf`. S795/S804 PRESENT anchors need the page-number-stripped/`，`-variant forms. This nuance is logged for the adoption round; adoption stays CLOSED.

Anchor-paragraph bases across the 7 UNESCO rows are inconsistent (2 count narrative-first, 5 count the Inscribed-status line as ¶1) — R71-M14, normalize in a later round; all 13 quotes re-located verbatim (RevRows).
