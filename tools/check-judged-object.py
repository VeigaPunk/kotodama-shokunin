#!/usr/bin/env python3
"""Judged-object freeze check for kotodama rounds (round 60, claim D).

The round-59 failure was a post-verdict narrowing: the entry that the blind
reviewers judged was edited after the verdicts landed, so the scored object was
not the object that entered the corpus. This tool reads the judged object
identity out of the packet key and compares it with the entry bytes that
actually exist at a revision.

Given a packet key (JSON) with

  {"entry": "<repo-relative path>",        (optional for the round-59 key)
   "entry_sha256": "<sha256 of the judged entry bytes>",
   "cited_ids": ["S600", ...],              (optional; the judged row set)
   "seats": {"<Seat>": {"P01": "S600", ...}}} (optional; round-59 key shape)

it reads the entry bytes at `<rev>` with `git show <rev>:<entry>` and reports:

  * FAIL (exit 1) when the sha256 of those bytes differs from the key's
    `entry_sha256` — the judged object was not the object that landed;
  * the sha256 the key records and the sha256 of the bytes at `<rev>`;
  * the cited S-ids that the judged object carries and `<rev>` lacks (the
    narrowing), and the ids `<rev>` carries that the judged object lacks
    (the widening), when the judged id set is knowable.

The judged id set is resolved in this order (the first that applies wins, and
the source is printed as `JUDGED_ID_SOURCE`):
  1. `cited_ids` / `judged_ids` / `ids` in the key;
  2. `--judged-rev <rev>`: the ids of the entry bytes at that revision;
  3. `seats` in the key: the union of the row ids the seat packets carried
     (the round-59 key shape; `PLANTED` is not an id);
  4. `rows` in the key: the ids that key the row map;
  5. otherwise no id set: only the sha comparison is reported.

The round-59 key (`.ufo/waves/round-59/support/planted-key.json`) carries
`entry_sha256` but no entry path, so it is used with `--entry`. Its
`entry_sha256` `556ddb27…` is the as-reviewed 47-row object; the entry that
actually landed at `d45985b2` hashes to `4e1bef48…` and cites 43 ids, so the
check reports the narrowing S602 S616 S623 S643.

Usage:
  python3 tools/check-judged-object.py --key <planted-key.json> --repo <git dir>
                                       --rev <revision> [--entry <repo-relative path>]
                                       [--judged-rev <revision>]
  python3 tools/check-judged-object.py --selftest

Exit codes: 0 the entry at <rev> is the judged object (PASS); 1 the entry at
<rev> is not the judged object (FAIL); 2 the check could not be evaluated
(input error). An input error prints `JUDGED_OBJECT_INPUT_ERROR: <reason>` on
stderr and still ends stdout with `JUDGED_OBJECT: FAIL`, so the exit code is
the only safe discriminator: exit 2 means "not evaluated", not "failed".

Read-only git: `git cat-file blob <rev>:<path>` only, inside --repo. Stdlib
only. No network.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

EXIT_OK, EXIT_FAIL, EXIT_INPUT = 0, 1, 2
VERDICT = "JUDGED_OBJECT"
ID_RE = re.compile(r"\bS\d{3,}\b")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


class InputError(Exception):
    """The check could not be evaluated: key, repo, revision or path unusable."""


# --------------------------------------------------------------------- git


def _git(repo, args):
    """Run git inside REPO; returns stdout bytes. InputError when git fails."""
    if not repo or not os.path.isdir(repo):
        raise InputError("repo directory %r does not exist" % (repo,))
    proc = subprocess.run(
        ["git", "-C", repo] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=_clean_env(),
    )
    if proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", "replace").strip().splitlines()
        raise InputError(
            "git %s failed in %s: %s"
            % (" ".join(args), repo, detail[-1] if detail else "rc=%d" % proc.returncode)
        )
    return proc.stdout


def _clean_env():
    """Environment without inherited repository pointers."""
    env = dict(os.environ)
    for var in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY"):
        env.pop(var, None)
    return env


def _blob(repo, rev, path):
    """Raw bytes of REV:PATH. InputError when it does not resolve to a blob."""
    out = _git(repo, ["cat-file", "blob", "%s:%s" % (rev, path)])
    return out


def _exists(repo, rev, path):
    """True when REV:PATH resolves to a blob."""
    proc = subprocess.run(
        ["git", "-C", repo, "cat-file", "-e", "%s:%s" % (rev, path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=_clean_env(),
    )
    return proc.returncode == 0


def _resolve_rev(repo, rev):
    """True when REV names a commit-ish in REPO."""
    proc = subprocess.run(
        ["git", "-C", repo, "rev-parse", "--verify", "%s^{commit}" % rev],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=_clean_env(),
    )
    return proc.returncode == 0


# --------------------------------------------------------------------- key


def _load_key(path):
    """The parsed key at PATH. InputError when it is unreadable or malformed."""
    if not os.path.isfile(path):
        raise InputError("key file %r does not exist" % (path,))
    try:
        with open(path, "r", encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError) as exc:
        raise InputError("key file %r is unreadable: %s" % (path, exc))
    if not isinstance(doc, dict):
        raise InputError("key file %r is not a JSON object" % (path,))
    return doc


def _key_sha(doc, path):
    """The judged sha256 recorded in the key. InputError when absent/malformed."""
    for field in ("entry_sha256", "judged_sha256", "sha256"):
        value = doc.get(field)
        if isinstance(value, str) and SHA_RE.match(value.strip().lower()):
            return value.strip().lower()
        if value is not None:
            raise InputError(
                "key field %r is not a 64-hex sha256: %r" % (field, value)
            )
    raise InputError(
        "key %r carries no entry_sha256 field (looked for entry_sha256, "
        "judged_sha256, sha256)" % (path,)
    )


def _key_entry(doc, override):
    """The repo-relative entry path: the override first, then the key fields."""
    if override:
        return override
    for field in ("entry", "entry_path", "path"):
        value = doc.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    raise InputError(
        "key carries no entry path field (looked for entry, entry_path, path); "
        "pass --entry <repo-relative path>"
    )


def _relativise(entry, repo):
    """ENTRY as a repo-relative path; absolute paths are cut at the repo root."""
    entry = entry.strip()
    if not entry.startswith("/"):
        return entry.lstrip("./")
    root = os.path.abspath(repo)
    if entry.startswith(root + "/"):
        return entry[len(root) + 1:]
    marker = "/corpus/"
    idx = entry.find(marker)
    if idx != -1:
        return entry[idx + 1:]
    return entry


def _ids_from_rows(doc):
    """The judged id set from a `rows` map (id -> row object); None if absent."""
    rows = doc.get("rows")
    if not isinstance(rows, dict):
        return None
    ids = {
        k.strip()
        for k in rows
        if isinstance(k, str) and ID_RE.fullmatch(k.strip())
    }
    return ids or None


def _ids_from_seats(doc):
    """Union of the row ids the seat packets carried; None when unavailable."""
    seats = doc.get("seats")
    if not isinstance(seats, dict):
        return None
    ids = set()
    for mapping in seats.values():
        if not isinstance(mapping, dict):
            continue
        for value in mapping.values():
            if isinstance(value, str) and ID_RE.fullmatch(value.strip()):
                ids.add(value.strip())
    return ids or None


def _ids_from_list(doc):
    """The judged id list carried by the key; None when unavailable."""
    for field in ("cited_ids", "judged_ids", "ids"):
        value = doc.get(field)
        if isinstance(value, list):
            ids = {
                v.strip()
                for v in value
                if isinstance(v, str) and ID_RE.fullmatch(v.strip())
            }
            if ids:
                return ids
    return None


# ------------------------------------------------------------------ report


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _ids(data):
    return set(ID_RE.findall(data.decode("utf-8", "replace")))


def _fmt(ids):
    return " ".join(sorted(ids)) if ids else "(none)"


def evaluate(key_path, repo, rev, entry_override=None, judged_rev=None):
    """(lines, exit_code) for one evaluation. Raises InputError."""
    doc = _load_key(key_path)
    key_sha = _key_sha(doc, key_path)
    entry = _relativise(_key_entry(doc, entry_override), repo)

    if not _resolve_rev(repo, rev):
        raise InputError("revision %r does not name a commit in %s" % (rev, repo))
    if not _exists(repo, rev, entry):
        raise InputError("entry %r is absent at revision %s" % (entry, rev))

    data = _blob(repo, rev, entry)
    rev_sha = _sha256(data)
    rev_ids = _ids(data)

    judged_ids, source = None, "none"
    listed = _ids_from_list(doc)
    if listed is not None:
        judged_ids, source = listed, "key.cited_ids"
    elif judged_rev:
        if not _resolve_rev(repo, judged_rev):
            raise InputError(
                "judged revision %r does not name a commit in %s" % (judged_rev, repo)
            )
        if not _exists(repo, judged_rev, entry):
            raise InputError("entry %r is absent at judged revision %s" % (entry, judged_rev))
        judged_ids = _ids(_blob(repo, judged_rev, entry))
        source = "--judged-rev %s" % judged_rev
    else:
        seats = _ids_from_seats(doc)
        if seats is not None:
            judged_ids, source = seats, "key.seats"
        else:
            rows = _ids_from_rows(doc)
            if rows is not None:
                judged_ids, source = rows, "key.rows"

    narrowing = set()
    widening = set()
    if judged_ids is not None:
        narrowing = judged_ids - rev_ids
        widening = rev_ids - judged_ids

    same = rev_sha == key_sha
    lines = [
        "JUDGED_KEY: %s" % key_path,
        "JUDGED_REPO: %s" % repo,
        "JUDGED_REV: %s" % rev,
        "JUDGED_ENTRY: %s" % entry,
        "JUDGED_SHA256_KEY: %s" % key_sha,
        "JUDGED_SHA256_AT_REV: %s" % rev_sha,
        "JUDGED_ID_SOURCE: %s" % source,
        "JUDGED_IDS_COUNT_JUDGED: %d" % (len(judged_ids) if judged_ids is not None else 0),
        "JUDGED_IDS_COUNT_AT_REV: %d" % len(rev_ids),
        "JUDGED_NARROWED_IDS: %s" % _fmt(narrowing),
        "JUDGED_WIDENED_IDS: %s" % _fmt(widening),
    ]
    if same and widening:
        lines.append(
            "JUDGED_NOTE: the entry bytes equal the judged bytes but the key's id "
            "set lists ids the entry does not cite; the key's id set is the "
            "inconsistent side"
        )
    if not same:
        lines.append(
            "JUDGED_NOTE: the entry at %s is not the judged object; the judged "
            "object was changed after it was judged" % rev
        )
    lines.append("%s: %s" % (VERDICT, "PASS" if same else "FAIL"))
    return lines, (EXIT_OK if same else EXIT_FAIL)


# ---------------------------------------------------------------- selftest


def _run(argv):
    """(rc, stdout, stderr) of one run of this script with ARGV."""
    import io

    out, err = io.StringIO(), io.StringIO()
    saved = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = out, err
    try:
        rc = main(argv)
    finally:
        sys.stdout, sys.stderr = saved
    return rc, out.getvalue(), err.getvalue()


def _git_fixture(cwd, *args):
    proc = subprocess.run(
        ["git", "-C", cwd] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=_clean_env(),
    )
    if proc.returncode != 0:
        raise AssertionError(
            "git %s failed: %s" % (" ".join(args), proc.stderr.decode("utf-8", "replace"))
        )
    return proc.stdout.decode("utf-8", "replace").strip()


def _commit(repo, message):
    _git_fixture(repo, "add", "-A")
    _git_fixture(
        repo,
        "-c",
        "user.name=selftest",
        "-c",
        "user.email=selftest@example.invalid",
        "commit",
        "-q",
        "-m",
        message,
    )
    return _git_fixture(repo, "rev-parse", "HEAD")


def _write(root, rel, content):
    dest = os.path.join(root, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(content)


def selftest():
    """Exercise the four cases the check must get right. Returns True on success."""
    ok = True
    with tempfile.TemporaryDirectory(prefix="judged-object-selftest-") as tmp:
        repo = os.path.join(tmp, "repo")
        os.makedirs(repo)
        _git_fixture(repo, "init", "-q")
        rel = "corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md"
        judged_text = (
            "# Amulets\n"
            "\n"
            "- The Met records the wedjat eye amulet (S600).\n"
            "- The Pazuzu amulet guarded a room (S602).\n"
        )
        _write(repo, rel, judged_text)
        judged_rev = _commit(repo, "judged object")
        judged_sha = _sha256(judged_text.encode("utf-8"))
        key_path = os.path.join(repo, "planted-key.json")
        _write(
            repo,
            "planted-key.json",
            json.dumps(
                {
                    "entry": rel,
                    "entry_sha256": judged_sha,
                    "cited_ids": ["S600", "S602"],
                },
                indent=2,
            )
            + "\n",
        )
        _commit(repo, "key")

        # 1. unchanged entry -> PASS
        rc, out, err = _run(
            ["--key", key_path, "--repo", repo, "--rev", judged_rev]
        )
        if rc != EXIT_OK or not out.rstrip().endswith("JUDGED_OBJECT: PASS"):
            ok = False
            print("selftest FAIL unchanged-entry: rc=%d\n%s%s" % (rc, out, err))
        else:
            print("selftest ok unchanged-entry -> PASS")

        # 2. one word changed -> FAIL
        changed = judged_text.replace("guarded a room", "guarded a house")
        _write(repo, rel, changed)
        changed_rev = _commit(repo, "one word changed")
        rc, out, err = _run(["--key", key_path, "--repo", repo, "--rev", changed_rev])
        if rc != EXIT_FAIL or not out.rstrip().endswith("JUDGED_OBJECT: FAIL"):
            ok = False
            print("selftest FAIL one-word-changed: rc=%d\n%s%s" % (rc, out, err))
        elif judged_sha not in out or _sha256(changed.encode("utf-8")) not in out:
            ok = False
            print("selftest FAIL one-word-changed: both hashes not printed\n%s" % out)
        else:
            print("selftest ok one-word-changed -> FAIL")

        # 3. one cited row line removed -> FAIL, the id is listed
        narrowed = "\n".join(
            line for line in judged_text.splitlines() if "S602" not in line
        ) + "\n"
        _write(repo, rel, narrowed)
        narrowed_rev = _commit(repo, "row line removed")
        rc, out, err = _run(
            ["--key", key_path, "--repo", repo, "--rev", narrowed_rev]
        )
        if rc != EXIT_FAIL or not out.rstrip().endswith("JUDGED_OBJECT: FAIL"):
            ok = False
            print("selftest FAIL row-removed: rc=%d\n%s%s" % (rc, out, err))
        elif "JUDGED_NARROWED_IDS: S602" not in out:
            ok = False
            print("selftest FAIL row-removed: S602 not listed as narrowed\n%s" % out)
        else:
            print("selftest ok row-line-removed -> FAIL with S602 listed")

        # 4. missing key -> exit 2
        rc, out, err = _run(
            [
                "--key",
                os.path.join(tmp, "no-such-key.json"),
                "--repo",
                repo,
                "--rev",
                judged_rev,
            ]
        )
        if rc != EXIT_INPUT:
            ok = False
            print("selftest FAIL missing-key: rc=%d (want 2)\n%s%s" % (rc, out, err))
        elif "JUDGED_OBJECT_INPUT_ERROR" not in err:
            ok = False
            print("selftest FAIL missing-key: no input-error marker on stderr\n%s" % err)
        else:
            print("selftest ok missing-key -> exit 2")
    return ok


# -------------------------------------------------------------------- main


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Check that the entry at a revision is the judged object "
        "the packet key names."
    )
    ap.add_argument("--key", help="path to the planted packet key (JSON)")
    ap.add_argument("--repo", help="git directory holding the entry")
    ap.add_argument("--rev", help="revision whose entry bytes are checked")
    ap.add_argument("--entry", help="repo-relative entry path (overrides the key)")
    ap.add_argument(
        "--judged-rev",
        help="revision carrying the judged entry bytes, when the key has no id list",
    )
    ap.add_argument("--selftest", action="store_true", help="run the selftest")
    args = ap.parse_args(argv)

    if args.selftest:
        return EXIT_OK if selftest() else EXIT_FAIL

    missing = [
        name
        for name, value in (
            ("--key", args.key),
            ("--repo", args.repo),
            ("--rev", args.rev),
        )
        if not value
    ]
    if missing:
        sys.stderr.write(
            "%s_INPUT_ERROR: missing %s\n" % (VERDICT, ", ".join(missing))
        )
        print("%s: FAIL" % VERDICT)
        return EXIT_INPUT

    try:
        lines, code = evaluate(
            args.key, args.repo, args.rev, args.entry, args.judged_rev
        )
    except InputError as exc:
        sys.stderr.write("%s_INPUT_ERROR: %s\n" % (VERDICT, exc))
        print("%s: FAIL" % VERDICT)
        return EXIT_INPUT
    for line in lines:
        print(line)
    return code


if __name__ == "__main__":
    sys.exit(main())
