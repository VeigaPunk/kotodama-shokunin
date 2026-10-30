# RevAppendOnly — expected digest checking command (round-79 Ca correction binding)

Lane base: `44f76d456c1b326a71ffdb381590af825cbf11be`. All commands run read-only
(`git show` / `git rev-parse` on committed bytes). Measured revision for the round-78
receipt per `corpus/lessons/round-78-verifier-spotcheck.md` (routed defect 2) is the
round-78 head `4b255745dea45a45d88b17e3c3fea4cdb6700cf7`.

## 1. Bound digests (observed 2026-10-30, worktree at base, outputs in `probe/probe-0-lane-canonical.txt`)

| quantity | value |
|---|---|
| receipt git blob sha1 @ `4b255745` | `62eb55b77f44bf47c283c98c5645dd7141e98495` |
| receipt git blob sha1 @ base `44f76d45` | `62eb55b77f44bf47c283c98c5645dd7141e98495` (identical) |
| receipt sha256 @ `4b255745` | `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867` |
| receipt byte size | 3901 |
| introducing commit | `4b255745` only (`git log --follow` lists one commit) |

## 2. Expected digest checking command

```sh
# exit 0: original receipt preserved; exit 1: in-place rewrite detected; exit 2: input error
REPO=/home/vgpnk/Projects/shokunin/kotodama-shokunin
REV=4b255745dea45a45d88b17e3c3fea4cdb6700cf7
PATH_R=reports/round-78/telemetry/census-end.txt
git -C "$REPO" rev-parse --verify --quiet "$REV^{commit}" >/dev/null || { echo "not a commit"; exit 2; }
git -C "$REPO" cat-file -e "$REV:$PATH_R" || exit 2
BLOB=$(git -C "$REPO" rev-parse "$REV:$PATH_R")
SHA=$(git -C "$REPO" show "$REV:$PATH_R" | sha256sum | awk '{print $1}')
[ "$BLOB" = 62eb55b77f44bf47c283c98c5645dd7141e98495 ] && \
[ "$SHA"  = 05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867 ] \
  && echo "DIGEST: PASS" || { echo "DIGEST: FAIL"; exit 1; }
```

A standalone copy of this check (parameterized) is `stage/RevAppendOnly/probe/check-receipt-digest.sh`;
it was exercised in an isolated fixture repo — red/green receipts in `probe/probe-*.txt`.

## 3. Token-binding checks the correction must also carry (observed)

```sh
# old token present verbatim in the historical receipt (exactly once)
git show 4b255745:reports/round-78/telemetry/census-end.txt \
  | grep -cF 'used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md'   # -> 1

# actual token present verbatim in registry row S884 (SOURCES.md line 839) at measured revision
git show 4b255745:corpus/SOURCES.md | sed -n 839p \
  | grep -cF 'worldbuilding-setting-practice.amend-2026-10-23.md'                                                 # -> 1
git show 4b255745:corpus/SOURCES.md | sed -n 839p \
  | grep -cF 'amend-2026-10-24-r13'                                                                               # -> 0

# old-token path has never existed in the lane at the measured revision (missing-path class, not mere drift)
git cat-file -e 4b255745:corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md # -> exit 128
```

Raw outputs: `probe/probe-5-token-bindings.txt`.
