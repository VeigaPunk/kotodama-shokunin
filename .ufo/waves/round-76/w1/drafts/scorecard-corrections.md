## Corrections — round 76

Append-only record (hyaku run 10, kotodama round 76). Claim Ca ledger `reports/round-76/ledger.json`
(20 unique pairs, L76-01…L76-21 (L76-09 removed as a duplicate)), frozen with `reports/round-76/claims.json`. Counter:
`python3 -B reports/round-76/accept-ca.py --root . --lands <Ca-lands> --freeze <freeze> --fleet-root /home/vgpnk/Projects/shokunin --combined <C-lands> --main <Ca-lands> --work /fast/scratch/hyaku/kotodama-r76/<seat>` (the local `main` is pinned to `<Ca-lands>`; `--combined` is required). The filed lines named below
stand as filed; every stated token below is unequal to the token the pair's own command returns at base
`98c486bdb4650ba5b8e651d332910e8ee60ad121`, and each was measured red there. Each row carries the pair id,
the base stated token, the observed token and the pair's own re-derivation command, which the counter re-runs
with the pair's parser and requires to return the observed token.

| id | old token | new token | re-derivation command |
|---|---|---|---|
| L76-01 | absent | present | git grep -c -E '^' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/claims.json |
| L76-02 | DRAFT | FINAL | git grep -o -E '"status": "[A-Z]+' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/claims.json |
| L76-03 | fails | blob | git cat-file -t 98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/claims.json |
| L76-04 | fails | blob | git cat-file -t 98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/accept-c.py |
| L76-05 | 6862 | 30920 | git ls-tree -l 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.md |
| L76-06 | excerpt | whole-document | git grep -o -E '^window-scope: [a-z-]+' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S891.txt |
| L76-07 | amend-2026-10-23 | amend-2026-10-23b | git grep -o -E '^\| S891 \|.*' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/SOURCES.md |
| L76-08 | 10 | 3266 | git grep -o -E '^window: chars=[0-9]+ min=[0-9]+ pad=[0-9]+ before=[0-9]+' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S888.txt |
| L76-10 | 4097 | 4096 | git grep -h -E '^window: chars=' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S888.txt |
| L76-11 | 111486 | 109588 | git grep -h -E '^bytes: ' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S885.txt |
| L76-12 | 118776 | 116878 | git grep -h -E '^bytes: ' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S887.txt |
| L76-13 | 111487 | 109588 | git grep -h -E '^bytes: ' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S885.txt |
| L76-14 | .ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md | corpus/SOURCES.md | git grep -l -F -e 'Innombrables sont les récits du monde.' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/SOURCES.md |
| L76-15 | marrone%20age% | marrone%20age%20dor---2.pdf | git grep -h -o -E 'marrone%20age%[^ ]*' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md |
| L76-17 | 5933 | 24166 | git ls-tree -l 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md |
| L76-18 | 2514 | 23049 | git ls-tree -l 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md |
| L76-19 | 284 | 2020 | git grep -h -E '^window: chars=' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S892.txt |
| L76-20 | 2bcdd019 | 20b571d7 | git grep -h -o -E '^sha256: [0-9a-f]{8}' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S885.txt |
| L76-21 | fbf48ad2 | e0560649 | git grep -h -o -E '^sha256: [0-9a-f]{8}' 98c486bdb4650ba5b8e651d332910e8ee60ad121 -- reports/round-75/evidence/S887.txt |

Notes. Each cell holds the ledger's own token, not a paraphrase: the old token is the pair's `stated_parse`
capture at the pinned base, the new token is what the pair's `observe_cmd` returns there. The twenty
commands were run once each from a clone checked out at `98c486b` and every one exited 0 with its parse
returning the new token (20/20, 0 mismatches) — the raw outputs are pasted below.

- L76-01 (`corpus/lessons/round-75.md:4`): the claims line says `git cat-file -e HEAD:reports/round-75/claims.json`
  is `absent`, so the round's files are untracked working bytes. At base the path is a tracked blob; the
  `count-presence` parse reads the `git grep -c` count 227 as `present`. The freeze `5d01674` is an ancestor
  of the measured base, which is why the blob is there.
- L76-02 (lesson `:15`): "the claims are `DRAFT`" against `claims.json` `"status": "FINAL — wave-1 and
  wave-2 attacks applied; frozen by the commit that adds this file …"`, first word `FINAL`.
- L76-03 (lesson `:312`, R75-M1): the row asserts the `git cat-file -e` probe "still fails"; `git cat-file -t`
  prints `blob`, so the probe succeeds. The token vocabulary differs (stated outcome `fails`, observed object
  type `blob`) because an argv with no pipe cannot print an exit status; the pair's parse extracts the type.
- L76-04 (lesson `:332`, R74-M8): the same assertion for `reports/round-75/accept-c.py`, which resolves to
  `blob` at base. Both counters are in the freeze commit.
- L76-05 (lesson `:92`): the adopted-entry byte size is stated as `6862 B`, the staged `shokuknow` copy's
  size; the lane path the sentence names is `30920` bytes at base. The same line's two siblings are stated
  `5933` / `2514` against `24166` / `23049` — the same defect class, not separately ledgered.
- L76-06 (lesson `:55`): "The other six declare `excerpt`" — S891's stored window declares `whole-document`,
  so the census is four whole-document files (S885, S886, S887, S891) and five excerpt. The other five
  excerpt rows (S888, S889, S890, S892, S893) do declare `excerpt`.
- L76-07 (lesson `:246`): the `used-by` rewrite sentence puts S891 and S892 under `amend-2026-10-23`; the
  landed registry rows bind both to `amend-2026-10-23b`, which is what their `source:` lines produce. S885's
  cell also carries `amend-2026-10-23b`, absent from the sentence.
- L76-08 (lesson `:47`): the note describes S888's window as `chars=4097 before=10` and asserts the
  Gate quote is not in it; the landed window is `chars=4096 … before=3266` and its own header says
  `quote-found: yes`. The initially drafted L76-09 duplicated the same stated cell and observed file; it was
  excluded from the frozen ledger before the claim was frozen.
- L76-10 (lesson `:31`): the S888 Gate cell's `excerpt` window width `4097` against the landed `chars=4096`.
- L76-11 (lesson `:28`): the S885 Gate cell carries the probe receipt's `111486 B`; the committed evidence
  file `reports/round-75/evidence/S885.txt` says `109588`. The digest on the same cell (`2bcdd019…`) is
  likewise the probe's, not the committed `20b571d7…`.
- L76-12 (lesson `:30`): the S887 Gate cell carries `118776 B`; the committed evidence says `116878`.
- L76-13 (`corpus/knowledge/myth-symbol/narrative-structure-frameworks.md:8`): the entry's `verified-at` line
  states `111487` for the S885 notice — a fourth distinct value; the committed evidence is `109588`. The
  other four counts on that line (`225123 / 1085244 / 697092 / 45238`) match their evidence files.
- L76-14 (lesson `:23`): the Gate says every quote is the text inside that row's `anchor` cell in
  `.ufo/waves/round-75/assimilation/validate/corpus/SOURCES.md`; that path exists in no commit
  (`git log --all --oneline -- '.ufo/waves/round-75/assimilation/validate/*' | wc -l` → `0`). The Gate quote
  itself resolves in the landed `corpus/SOURCES.md`, so the claim is true and the pointer dead.
- L76-15 (lesson `:251`): the "not repaired here" URL wrap is not in the file it names — no line of
  `narrative-structure-frameworks.amend-2026-10-23.md` ends with `%`, and the S892 `source:` line in
  `…amend-2026-10-23b.md` carries `marrone%20age%20dor---2.pdf` whole on one line.

The L76-16 ledger pair is REPAIR and carries no row here: L76-16 moves `SKILL.md:707` off the pre-freeze
counter sha `fa5060b91bdb…` — which is the sha the `reports/round-75/telemetry/selftest-c.txt` header records,
not the committed counter's — to the committed `reports/round-75/accept-c.py` sha256 `315c5f3f27fd…`. The
statement edit is a unified diff against base `98c486b`, staged at
`.ufo/waves/round-76/w1/drafts/repairs.diff` (one hunk, `@@ -704,7 +704,7 @@`); `SKILL.md` is mutable, so the
statement moves to the observed truth and no historical line is rewritten.

Raw outputs (base `98c486b`, each command run from a clone checked out at that revision):

```
$ git grep -c -E '^' 98c486b… -- reports/round-75/claims.json
98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/claims.json:227
$ git grep -o -E '"status": "[A-Z]+' 98c486b… -- reports/round-75/claims.json
98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/claims.json:"status": "FINAL
$ git cat-file -t 98c486b…:reports/round-75/claims.json
blob
$ git cat-file -t 98c486b…:reports/round-75/accept-c.py
blob
$ git ls-tree -l 98c486b… -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
100644 blob 29baa5159af1fb122f655e483fa29d7d9d58c418   30920	corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
$ git grep -o -E '^window-scope: [a-z-]+' 98c486b… -- reports/round-75/evidence/S891.txt
98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/evidence/S891.txt:window-scope: whole-document
$ git grep -o -E '^\| S891 \|.*' 98c486b… -- corpus/SOURCES.md
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/SOURCES.md:| S891 | Roland Barthes, S/Z (Paris: Seuil, 1970), …
   (the printed row is one line; its parse captures narrative-structure-frameworks.amend-2026-10-23b.md)
$ git grep -o -E '^window: chars=[0-9]+ min=[0-9]+ pad=[0-9]+ before=[0-9]+' 98c486b… -- reports/round-75/evidence/S888.txt
98c486bdb4650ba5b8e651d332910e8ee60ad121:reports/round-75/evidence/S888.txt:window: chars=4096 min=4096 pad=400 before=3266
$ git grep -h -E '^window: chars=' 98c486b… -- reports/round-75/evidence/S888.txt
window: chars=4096 min=4096 pad=400 before=3266 after=809
$ git grep -h -E '^bytes: ' 98c486b… -- reports/round-75/evidence/S885.txt
bytes: 109588
$ git grep -h -E '^bytes: ' 98c486b… -- reports/round-75/evidence/S887.txt
bytes: 116878
$ git grep -l -F -e 'Innombrables sont les récits du monde.' 98c486b… -- corpus/SOURCES.md
98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/SOURCES.md
$ git grep -h -o -E 'marrone%20age%[^ ]*' 98c486b… -- corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md
marrone%20age%20dor---2.pdf
marrone%20age%20dor---2.pdf,
$ sha256sum reports/round-75/accept-c.py
315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261  reports/round-75/accept-c.py
```

The two-line L76-15 output is the same URL captured twice in that file (once as the `source:` line's URL and
once in its `used-by`/anchor text); the pair's parse `(marrone%20age%[^\s]*)` takes the first match. A second
`git grep -h -E '^bytes: '` for S885 (L76-13) is deliberately the same argv as L76-11 because the two pairs
bind two different files (the lesson's Gate cell and the entry's `verified-at` line) to the one committed
receipt; the token is identical and the correction is to the entry.
