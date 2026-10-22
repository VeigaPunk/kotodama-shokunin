# ReviewDRowNumerals: attack on claim D, row 47 (`numerals-and-measures.md:101`)

- **Seat:** KotodamaR51a3.ReviewDRowNumerals (leaf; read-only on the lane; no subagents, no background jobs).
- **Lane:** /home/vgpnk/Projects/shokunin/kotodama-shokunin. HEAD = main = `9feb69e`. Claim base `bff83ba`. Claim D commit `35f0d49`.
- **Item:** D row 47 at `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:47`, anchor `corpus/knowledge/linguistics/numerals-and-measures.md:101`. Body seam at `pastoralism-animal-husbandry.md:93` (§5 spans `:79`–`:93`).
- **Reads:** in-corpus, re-read in the lane on 2026-10-22.

## Verdict for row 47: HOLDS-WITH-FIXES

Row 47 passes the claim's falsifier as written. Its anchored line supports the ownership cell. The §5 body line narrows the boundary in so many words. D adds no forbidden citation. No other row owns "head of cattle".

Depth is the weak axis. One body sentence carries the seam. The herd-count recording medium and "composition" are not developed. The fixes are small. The one medium finding that touches D's measurement (A1) is adjacent: it concerns row 43 and the counter's rule, not row 47.

## Answers

**1. Does the anchored line support the cell? Yes, with one category drift.**

Quoted from `corpus/knowledge/linguistics/numerals-and-measures.md:101` (§4 "The numeral–noun interface", header at `:84`):

> Where the measures side lives: unit systems, standards, and money-words belong to `culture-material/trade-economy-lexicon.md`. This entry owns only the *words* — mensural classifiers, counting units (*pair*, *head of cattle*, *dozen*, *score*), and the way a classifier system maps a noun inventory into count classes.

Cell (`pastoralism-animal-husbandry.md:47`): "counting words and mensural classifiers, including the unit "head of cattle"". The ownership claim is supported and does not overclaim.

Drift: the cell files "head of cattle" under mensural classifiers. The anchor files it under counting units. `numerals-and-measures.md:96` defines mensural classifiers as units for low-countability nouns, and cattle are countable (F4).

The same line hands unit systems, standards and money-words to `trade-economy-lexicon.md`. Row 47 claims none of them, so there is no conflict.

**2. Is the boundary developed or narrowed at the section the cell names (§5)? Narrowed explicitly; developed thinly.**

Quoted from `pastoralism-animal-husbandry.md:93` (inside §5, header at `:79`):

> Counting words and classifiers such as "head of cattle" belong to `numerals-and-measures.md:101`; this entry supplies what a herd count records — composition, age and sex, ownership marks — never the counting system itself.

- "never the counting system itself" is an explicit narrowing.
- "age and sex" is developed by pre-existing row `:86` (Age × sex). "ownership marks" is developed by pre-existing row `:87` (earmark). D's diff touched neither.
- "composition" is asserted in the cell (`:47`) and the body (`:93`), but no §5 line defines it. §5 rows `:85`–`:89` are colour, age × sex, ownership, species set and wealth. The species portfolio is in §4 (`:67`–`:75`), which the cell does not name.
- The lead sentence at `:29` says the body section "develops" each boundary. For row 47 that is one sentence (F3).

**3. Duplicate authority, or laundering a `(to-verify)` claim?**

- *"head of cattle"*: one owner, numerals (`numerals-and-measures.md:9`, `:101`). Pastoral defers. Adjacent claim: `trade-economy-lexicon.md:70`, "capital, cattle, chattel | Lat. *caput* 'head' | wealth counted by heads". That is an etymology and wealth-reckoning claim, not a counting-word claim. It is not carved out (F6).
- *"ownership marks"*: only pastoral (`:87`, `:93`, `:129`). `animal-symbolism.md` owns "the herd's signs" (row `:41`, `:158`). That is a different object. No duplicate.
- *"collective"*: `:88` ("one collective noun") and `:77` ("a culture may name its herd as one set") against `numerals-and-measures.md:78` (collectives, §3) and `:101` (count classes). Overlap in terminology (F7).
- *(to-verify)*: none in the row-47 chain (`pastoralism-animal-husbandry.md:47`, `:93`, §5 `:79`–`:93`; `numerals-and-measures.md:84`–`:101`). The lead's `surplus` hint: the only `surplus` in the entry is `:155` ("offerings drawn from the herd's surplus males `(to-verify)`"). It sits in §10, outside the chain, and keeps its mark. The numerals entry has no "surplus". Nothing is laundered into row 47.

**4. Genuine neighbour or filler? Genuine, thin. Not filler.**

Numerals `:101` names "head of cattle" as a unit it owns, and a herd count is a real seam.

Thin: one body sentence, no herd-count record example, and the recording medium is unanchored. Numerals §5 owns that medium: "**Tally marks** …" (`numerals-and-measures.md:109`) and "**Knotted-cord and rod records** …" (`:110`). The build-wave scribe's draft row carried `:101,:109` (`.ufo/waves/round-51/build/ScribeRowNumeralsAndMeasures.md:17`). The landed row dropped `:109` (F5).

## Forbidden citations in D's diff

`git diff bff83ba -- corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (full text at artifact://12703) has three hunks: the lead sentence and blank at `:29`–`:30`; table rows `:42` and `:44`–`:47`; and the body line and blank at `:93`–`:94`.

None cites `corpus/knowledge/linguistics/sign-languages-manual-modality.md`, an S-id from S071 up, or the round lesson. Pre-existing `:9` ("the round lesson's located quote", no path) is base text outside D's hunks (I3).

## Findings

Ordered by severity. Each has a pointer and the smallest fix.

| ID | Sev | Pointer | Finding | Smallest fix |
|---|---|---|---|---|
| F1 | medium | `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:8` | The `- couples:` line names no numerals neighbour (row 47), no `symbolism-synthesis-method.md` (row 45) and no `celestial-symbolism-calendars.md` (row 46). D's hunks (`:26`, `:37`–`:47`, `:84`–`:90`) leave `:8` unchanged. Bar: `corpus/QUALITY.md:13`–`:15`, criterion 3 (the couples line names the systems and files the entry connects). | Add to `:8` a clause such as: linguistics — `numerals-and-measures.md` (owns counting words and counting units, `:101`; this entry owns what a herd count records, §5). Add the two myth-symbol files with their row roles. Keep one line and the trailing period. |
| A1 | medium (adjacent, table level) | `pastoralism-animal-husbandry.md:43`; `reports/round-51/boundary-count.py:25`, `:46`–`:47` | The counter's "15" counts row 43 (`civilizations/`, pre-existing). That is a directory with 94 `.md` files and no line anchor. The claim requires "a backticked path:line anchor that resolves" per row (`reports/round-51/claims.json:18`). Read-only strict check (command 29): 14 of 15 rows conform. The lesson discloses the row as carried (`corpus/lessons/round-51.md:106`–`:107`). | L1 decision. Either give row 43 one file-level anchor with lines, or split it per file. Or narrow the claim statement to "resolves, one neighbour per row" and say so in the lesson. Not a row-47 defect. |
| F2 | low | `pastoralism-animal-husbandry.md:6`, `:10` | The in-corpus anchor list at `:6` omits `linguistics/numerals-and-measures.md:101`. It is the one new anchor not already in base `:6`; the other three new anchors are there. `:10` (verified-at) still reads 2026-10-21 and records no re-read of the new anchor. | Add `linguistics/numerals-and-measures.md:101` to `:6`. Add a 2026-10-22 re-read note to `:10`. |
| F3 | low | `pastoralism-animal-husbandry.md:47`, `:93`, `:29` | "composition" is owned in the cell and the body, but no §5 line defines it. The cell cites §5 only, while the species table is §4 (`:67`–`:75`). `:29` says "develops"; row 47 has one sentence. | Change the cell to "(§4–§5)". Add one clause in `:93` tying composition to the §4 species table. Or change `:29` to "narrows or develops". |
| F4 | low | `pastoralism-animal-husbandry.md:47`, `:93` vs `numerals-and-measures.md:96`, `:101` | Category drift. The cell says "mensural classifiers, including the unit 'head of cattle'". Body `:93` says "classifiers such as 'head of cattle'". The anchor lists "counting units (… head of cattle …)" separately. `:96` reserves mensural classifiers for low-countability nouns. | `:47` → "counting words and counting units, including 'head of cattle'; mensural classifiers". `:93` → "counting words and counting units such as 'head of cattle'". |
| F5 | low | `pastoralism-animal-husbandry.md:47`; `numerals-and-measures.md:109`–`:110`; `pastoralism-animal-husbandry.md:152` | The herd-count medium is unanchored. §10 `:152` ("tally-stick", S064) presumes a tally record. Numerals §5 owns that medium at `:109`–`:110`. The scribe's draft had `:101,:109`; the landed row has only `:101`. | Change the `:47` anchor to `numerals-and-measures.md:101,:109` and add "tally records" to the cell. Sandbox-verified below: the counter stays 15/15/15, exit 0. The anchor stays outside `:103`–`:108`, the window the critic guarded (`.ufo/waves/round-51/build/CriticClaimD.md:97`), and outside `:107`, which the sign-language entry cites (command 28). If adopted, `corpus/lessons/round-51.md:107` ("exactly one file.md:N anchor") needs the matching records edit. |
| F6 | low | `pastoralism-animal-husbandry.md:93`; `trade-economy-lexicon.md:70` | "wealth counted by heads" sits in trade-economy. The herd "head" wealth sense is not carved out in row 47 or `:93`. Not a same-owner duplicate. | Add to `:93`: "the wealth-reckoning use of 'heads' stays with `trade-economy-lexicon.md:70`". |
| F7 | low | `pastoralism-animal-husbandry.md:88`, `:77`; `numerals-and-measures.md:78`, `:101` | The collective-noun design for a mixed herd overlaps numerals' collectives (§3) and its count-class mapping. | At `:88` add: "count-class or numeral-collective behaviour stays at `numerals-and-measures.md:78,:101`". |
| F8 | low | `pastoralism-animal-husbandry.md:12`, `:212` | The scope lines list the handoffs (field, hunt, dish, cloth, road, market, lexicon field, animal sign, shepherd-king). They do not list the counting words row 47 hands to numerals. | Add "counting words (`numerals-and-measures.md:101`)" to both lines. |
| I1 | info | `corpus/knowledge/linguistics/numerals-and-measures.md` | Numerals never names pastoral or herds (command 15). Its `- couples:` line (`:27`) names no pastoral entry. The seam is one-way. Outside D's lands. | None in D. |
| I2 | info | `pastoralism-animal-husbandry.md:155` | "surplus males `(to-verify)`" sits in §10. Rows 44–46 cite §10 in their cells. The mark is intact. Those seats should check their own rows. | None. |
| I3 | info | `pastoralism-animal-husbandry.md:9` | "the round lesson's located quote": no path, base text, not a D hunk. | None for D. Flag only if the L1 reads "round lesson" literally. |

## Sandbox check (private clone only)

Clone: `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewDRowNumerals`. Created with `git clone -q --shared` at `9feb69e`. Its entry was `cmp`-identical to the lane before mutation. Only row 47 changed.

- Control, anchor `numerals-and-measures.md:999`: `rows=15 resolved=14 distinct=14`, exit 1. The counter catches a broken row-47 anchor.
- Candidate, anchor `numerals-and-measures.md:101,:109` (cell text also edited; the counter reads only the first cell): `rows=15 resolved=15 distinct=15`, exit 0. `git diff --stat` reports 1 file, 1 insertion, 1 deletion.
- Lane counter, unchanged: `rows=15 resolved=15 distinct=15`, exit 0.

## Commands run (exit codes)

| # | Command or tool | Exit / status | Key result |
|---|---|---|---|
| 1 | read `reports/round-51/claims.json` | ok | D statement `:18`, falsifier `:26`, must_not_cite `:27`; C at `:29`–`:45` |
| 2 | read `~/.omp/agent/RULES.md` | ok | Tooling directive; no install needed |
| 3 | read pastoral `:1-140` | ok | §2 table `:31`–`:47` |
| 4 | read `culture-material/numerals-and-measures.md:80-125` (guessed path) | error: path not found | Corrected by glob (#11) |
| 5 | read `reports/round-51/boundary-count.py` | ok | stdlib; "Read-only" docstring; `dir/` resolves at `:46`–`:47`; `:25` makes line numbers optional |
| 6 | read `corpus/QUALITY.md` | ok | criterion 3 at `:13`–`:15` |
| 7 | read `corpus/knowledge/verification/calibration-registry.md:30-45` | ok | codes at `:35`–`:39` |
| 8 | read `xd://lsp` | error | "No such tool: xd://lsp. Mounted devices: ast_edit, debug." |
| 9 | grep pastoral for surplus, to-verify, S07x and others | ok | hits are `to-verify` and `:9`; no S071+ |
| 10 | grep numerals at the guessed culture-material path | error: path not found | Not used |
| 11 | glob `corpus/knowledge/**/numerals*.md` | ok | `linguistics/numerals-and-measures.md` |
| 12 | bash `git --no-optional-locks diff bff83ba -- <pastoral>` | exit 0 | 1 file, +9/−1. Full text at artifact://12703 |
| 13 | bash `python3 -B reports/round-51/boundary-count.py` | exit 0 | `rows=15 resolved=15 distinct=15` |
| 14 | bash `git log --oneline -8; rev-parse HEAD main` | exit 0 | HEAD = main = `9feb69e`; D = `35f0d49` |
| 15 | grep corpus and numerals for "head of cattle", surplus, herd, pastoral (three greps) | ok | "head of cattle" only at numerals `:9`, `:101`; no "surplus" or "pastoral" in numerals |
| 16 | read numerals `:84-106` | ok | anchor quote |
| 17 | read pastoral `:8:raw` | ok | couples line; no numerals |
| 18 | read artifact://12703 | ok | full D diff, three hunks |
| 19 | bash `python3 --version; sha256sum <pastoral> <numerals>; git diff --stat 35f0d49 9feb69e` | exit 0 | Python 3.14.8. Pastoral `5c2e09d0…`, numerals `57fc7669…`. Commits `35f0d49`..`9feb69e` touch 5 files, not pastoral or numerals |
| 20 | read pastoral `:6:raw`, `:12:raw`, `:144-160`, `:146-150` | ok | in-corpus anchor list (no numerals:101); scope; §10 with `:155` |
| 21 | grep trade-economy for head, cattle, unit, count, surplus | ok | `:70` "wealth counted by heads" |
| 22 | bash `git --no-pager show --stat 35f0d49; find corpus/knowledge/civilizations -name '*.md' \| wc -l; ls -d corpus/knowledge/civilizations/` | exit 0 | D touches 1 file (+9/−1). civilizations has 94 `.md` files. Directory exists |
| 23 | read trade `:69-70` | ok | row text |
| 24 | grep lesson round-51 for numerals, head, boundary-count, row 47 | ok | `:8`, `:106`–`:110` |
| 25 | grep build directory for numerals and head | ok | `ScribeRowNumeralsAndMeasures.md:17`, `:30`; `CriticClaimD.md:97` |
| 26 | grep corpus for earmark, ownership mark, herd's sign, counted by heads | ok | earmark only in pastoral; "counted by heads" in trade `:70` |
| 27 | read animal-symbolism `:70-75`, `:108-112` | ok | herd idioms at `:73`, `:110` |
| 28 | grep sign-language entry for `numerals-and-measures.md:1xx` | ok | cites `:107` only (lines 4, 6, 8, 39, 66) |
| 29 | eval py, read-only (bytecode off): strict conformance over section 2 | ok | `strict_conforming_rows = 14 of 15`; row 43 is a DIR token |
| 30 | eval py, read-only: `resolve()` on candidate tokens | ok | `:101` true; `:101,:109` true; `:109-110` true; `:999` false; `civilizations/` true |
| 31 | bash `git --no-optional-locks show bff83ba:<numerals> \| cmp`; `git diff --stat HEAD` on three files; sha256sum counter | exit 0 | numerals base equals HEAD. No uncommitted change to the three files. Counter sha256 `fb1d5c89…` |
| 32 | bash `mkdir -p …; git clone -q --shared … ReviewDRowNumerals; realpath; rev-parse` | exit 0 | Clone at `9feb69e` |
| 33 | bash `realpath; ls -la; cmp clone-file lane-file` | exit 0 | Identical |
| 34 | read clone pastoral `:47` | ok | tag `7D8C` |
| 35 | edit clone `:47` (control, `:999`) | ok | tag now `11FD` |
| 36 | bash clone counter | exit 1 | `rows=15 resolved=14 distinct=14` |
| 37 | edit clone `:47` (candidate, `:101,:109`) | ok | tag now `E3C5` |
| 38 | bash clone counter; lane counter; clone `git diff --stat` | exit 0; exit 0; exit 0 | 15/15/15; 15/15/15; 1 file, +1/−1 |

Nothing was written to the lane. Read-only git used `--no-optional-locks`. Python ran with `-B` and `sys.dont_write_bytecode`.

## Sources opened

None. Row 47, `numerals-and-measures.md:101` and body line `:93` cite no URL. Every anchor is in-corpus and was re-read in the lane on 2026-10-22.

## Tooling

- No installs or updates. Present tools used: python3 3.14.8, git, sha256sum, cmp, realpath, `git clone --shared` (writes alternates only inside the clone).
- LSP: `read xd://lsp` returned "No such tool: xd://lsp. Mounted devices: ast_edit, debug." No server answered the files, so no LSP caller, definition or diagnostic checks ran. Literal text grep is the fallback. Grep output here is textual, not semantic proof.

## Unrun checks

- Outside my item: `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json`; `python3 -B reports/round-51/claims-agree.py`; `python3 -B reports/round-28/readme/sweep.py`; `find corpus/knowledge -name '*.md' | wc -l`; `tools/gates/provenance-audit.py` on the sign-language entry.
- `reports/round-51/telemetry/declaration-dry-run.txt`: not opened.
- Build-wave seat reports and the round lesson were read as context only, never as evidence.

## Residual risk

- A1: the printed 15/15/15 is the declared measure. A reader who takes "15" as strict row conformance overstates it.
- F5 would turn row 47 into two line anchors in one file. The lesson's "exactly one" wording would need the same update.
- "Narrowed" versus "developed" for row 47 is a judgement. I call it narrowed, with thin development.
- Scope: I did not attack rows 42 or 44–46, or the sign-language entry.
