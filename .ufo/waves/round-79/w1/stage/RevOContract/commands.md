# RevOContract — reproducible commands (round-79 W1)

All recon probes were executed 2026-10-30 from cwd
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` (lane, read-only). Raw output:
`probes/recon-2026-10-30.txt` and `probes/fixture-measure.txt`.

## RECON (lane, read-only)

```sh
# P1 — guard absent at base
git cat-file -e 44f76d456c1b326a71ffdb381590af825cbf11be:tools/ledger-token-guard.py   # exit 128
git ls-tree -r --name-only 44f76d456c1b326a71ffdb381590af825cbf11be | grep -c ledger-token-guard   # 0

# P2 — S897 free at base (last registry id, row count)
git show 44f76d456c1b326a71ffdb381590af825cbf11be:corpus/SOURCES.md | grep -oE '^\| S[0-9]+' | tail -1   # | S896
git show 44f76d456c1b326a71ffdb381590af825cbf11be:corpus/SOURCES.md | grep -c '^| S897'                  # 0

# P3 — the drifted used-by target never existed in any commit
git log --all --oneline -- corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md   # empty

# P4 — registry S884 used-by cell at the RECORDED round-78 revision 4b255745
git show 4b255745dea45a45d88b17e3c3fea4cdb6700cf7:corpus/SOURCES.md | sed -n '839p' | tr '|' '\n' | tail -2
# -> corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
# census-end.txt:33 records ...amend-2026-10-24-r13.md  => mismatch=1 at the recorded revision

# P5 — receipt digests (census-end sha matches reports/round-79/telemetry/baseline-census-mismatch.json)
sha256sum reports/round-78/telemetry/census-end.txt reports/round-78/telemetry/census-start.txt

# P9 — ancestry: recorded revision on the base first-parent chain
git merge-base --is-ancestor 4b255745dea45a45d88b17e3c3fea4cdb6700cf7 44f76d456c1b326a71ffdb381590af825cbf11be   # exit 0

# HEAD-class survivor evidence (read-only greps over committed counter bytes)
git show 44f76d45:reports/round-76/accept-ca.py | sed -n '1070p'   # REV_NAMES = ("HEAD", "HEAD^", "HEAD~1", "@")
```

## FIXTURE-REPO (isolated fixture repository — the only git mutation this seat performed)

```sh
cd /fast/scratch/hyaku/kotodama-r79/RevOContract
rm -rf fixture-repo && mkdir fixture-repo && cd fixture-repo
git init -q -b main .
test "$(git rev-parse --show-toplevel)" = "$PWD"   # verified root before any commit
mkdir -p records
printf 'token=green-7\ncount:42\nstatus=stable\n' > records/cal.txt
printf 'the calibration token is token=old-claim-3\nthe entry count is count:41\nthe status flag is status=stale\n' > LOG.md
git add records/cal.txt LOG.md
GIT_AUTHOR_NAME=fix GIT_AUTHOR_EMAIL=fix@example.invalid GIT_AUTHOR_DATE='2026-10-30T00:00:00Z' \
GIT_COMMITTER_NAME=fix GIT_COMMITTER_EMAIL=fix@example.invalid GIT_COMMITTER_DATE='2026-10-30T00:00:00Z' \
  git commit -q -m "fixture: records and log statements v1"
git rev-parse HEAD        # 362e71615521ddb23f1af02306251a9262a1acdb  (must reproduce exactly)
git rev-parse 'HEAD^{tree}' # 38612c028083a5a94183ac19dc44ad73ae218e15 (non-commit pin control)

# truthful observations behind every observed_at_base in the fixtures
git -C . grep -o -E 'token=[a-z0-9-]+'  362e71615521ddb23f1af02306251a9262a1acdb -- records/cal.txt   # :token=green-7
git -C . grep -o -E 'count:[0-9]+'      362e71615521ddb23f1af02306251a9262a1acdb -- records/cal.txt   # :count:42
git -C . grep -o -E 'status=[a-z]+'     362e71615521ddb23f1af02306251a9262a1acdb -- records/cal.txt   # :status=stable
```

## FIXTURES

`make-fixtures.py` (this directory) regenerates all `fixtures/fx-*.json` from
`fixtures/fx-guard-clean-ledger.json`; each mutant is the full clean ledger with
exactly one documented change. Expected verdicts are in each file's
`expected_verdict` and cross-referenced in `o-clause-map.md`.
