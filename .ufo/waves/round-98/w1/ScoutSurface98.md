# ScoutSurface98 — Report (claim C coverage surface + adjacency)

Frozen context read first, unedited: `reports/round-98/claims.json` (full), `reports/round-98/predispatch.py:1-63`, `reports/round-98/predispatch-base.txt` (full). Detail lives in `.ufo/waves/round-98/w1/stage/ScoutSurface98/surface.md`; this file carries the summary and every command's rc.

## Coverage (content sweep, `corpus/knowledge`)

- Broad assigned sweep `grep -rn -i -E 'toast|wassail|…|boast' corpus/knowledge | wc -l` → **2707** (rc 0). Substring-noise-dominated (`ale` inside `scaled`/`Alexander` etc.).
- Narrowed (word boundaries), rc per command in surface.md §1:
  - `\btoast(s|ed|ing)?\b|\btoastmaster\w*` → **0 matches (rc 1)**.
  - `wassail(s|ing)?|waes ?hael|drinc ?hael|kanpai|ganbei|cheers|sláinte|prosit|propin\w*|l.?chaim|skål|skal` → **0 matches (rc 1)**.
  - `\bbragaf\w*|\bbragarf\w*|\bminni\b|loving cup|stirrup cup|drinking horn|oath-?cups?` → **0** (all 21 matches in that run are `boast`).
  - `\blibations?\b` → **7 matches in 4 files** (rc 0): ainu `:109`, funerary `:8`, vessel-container-lexicon `:5,:36,:38`, death-afterlife `:41,:100`. (claims.json's "before" names 4 files; agrees on files, under-counts occurrences.)
  - `\bhealths?\b` → 47 in 26 files (rc 0), all generic wellness except cuisine `:103` ṣaḥtayn "two healths", `:104` afiyet olsun "may it be health" (eating-register table cells) and sogdian `:63` health-wishes-in-letters lead. `health-drinking` = **0**.
  - `\bsymposi\w*` → 4 in 4 files (3 = "Symposium Proceedings" titles; 1 substantive: furniture `:52` couch/symposium). `\bsupra\b|\btamada\b` → supra-local ×5, tamada 0. `\bmeads?\b|\bales?\b` → 10 in 6 files (poetry-mead `germanic-norse:95`, ale/beer caveat `cuisine:153`, Assize of Bread and Ale ×3, author "Mead" ×3). `\bkylix\b|\bkrater\b` → 4, all in vessel-container-lexicon. `rhyton|kantharos|ealu|medu` → 0; `skyphos` → 1 (vessel `:51`).
  - Owner guard, content-level: `grep -rn -i -E '(^#|^- topic:).*\b(libation|toast|wassail|health-drinking|drinking oath|toastmaster|bragaf|minni)\b' corpus/knowledge` → **0 (rc 1)** — no non-entry topic line or heading carries any frozen phrase; C8 guard independently confirmed.
- `corpus/knowledge/linguistics/toast-drinking-speech-formulae.md` does not exist (42-file listing).

## Adjacency (files read, boundary each new entry must respect)

Owner: `verbal-duelling-ritual-insult.md` (boast formula §6 `:110-122`, explicit deferral-list style §1). Substantive: `oath-blessing-curse-formulae.md` (performative slots; boast as failure mode `:59`), `vessel-container-lexicon.md` (krater/kylix/phiale + naming grammar `:36,:44-51,:55`), `cuisine-food-lexicon.md` (pre/post-meal formula table `:100-108`, feast §3, ale calibration `:153`), `death-afterlife-eschatology.md` (libation as offering medium `:41,:100`), `funerary-material-culture.md` (cross-ref only `:8`), `ainu.md` (ikupasuy/tuki `:109`), `germanic-norse.md` (poetry-mead `:95`, boast register `:68`), `furniture-interior-lexicon.md` (symposium couch `:52`). Content-adjacent with zero term hits: `guest-right-hospitality-law.md` (shared cup as bond marker, topic `:3`), `petitionary-and-votive-formulae.md` (vow = collectable debt), `greeting-leave-taking-formulae.md` (waes hael is a greeting-formula case), `pacific-northwest.md` (owns feast-speech/potlatch oratory `:8,:91,:103`). Full defer/cite table: surface.md §4. Notably `greece-classical.md` has **no** symposium/krater/kylix/libation content — Greek symposium speech-side is unowned.

## Skeleton + partition counts

- 8-h2 skeleton with the six frozen phrases placed: "toast formula" (§2), "health-drinking" (§3), "libation" (§4), "toastmaster" + "toast sequence" (§5), "drinking oath" (§6), refusal/penalty cup (§7), design procedure (§8) — plus a 6×5 toast-sequence order table draft (surface.md §5).
- Partition counts (find/awk/uniq command in surface.md §6): civilizations 95, culture-material 43, linguistics 42, myth-symbol 36, synthesis 29, verification 24. linguistics is the partition: it already owns the five-entry formulae family (oath-blessing-curse, greeting-leave-taking, petitionary-votive, funerary-lament-dirge, lullaby-child-song), all built as speech-act anatomy + slots + design procedure; the frozen surface path fixes linguistics/ regardless.

## Numbers ledger (command → value, rc)

Every command is reproduced verbatim in surface.md §1 with its rc: broad 2707 (rc 0); toast-family 0 (rc 1); cheers-family 0 (rc 1); norse-cup group 21-in-7-files all `boast` (rc 0); libation 7-in-4 (rc 0); health 47-in-26 (rc 0); symposi 4-in-4 (rc 0); supra/tamada 5-in-4 (rc 0); mead/ale 10-in-6 (rc 0); kylix/krater 4-in-1 (rc 0); rhyton/skyphos/kantharos/ealu/medu 1 (rc 0); feast/banquet supplementary 120-in-38 (rc 0); heading/topic owner sweep 0 (rc 1).

## Other

- Tools installed/upgraded: none.
- Pacman: not run. Host sysctls: untouched. No network fetches (sweep only). No git/jj commands beyond none — nothing mutated.
- Scratch `/fast/scratch/hyaku/kotodama-r98/ScoutSurface98/` created for artifact staging, deleted before yield (nothing citable came from it; all captures re-verified from corpus paths).
- Frozen files touched by this seat: none.
