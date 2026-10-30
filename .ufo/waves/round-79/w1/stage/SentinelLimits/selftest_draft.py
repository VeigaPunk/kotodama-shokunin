"""Selftest probe for ledger_limits_draft.py (SentinelLimits, W1 draft).

Run:  python3 -B selftest_draft.py --work <explicit scratch dir> \
          --fixture-repo <isolated git repo> --rev <commit in it> \
          [--lane <read-only lane repo for committed ledger bytes> --base <40hex>]

Every case prints `CASE <name> expect=<X> got=<Y> PASS|FAIL`. A `legacy` control
replays the same hostile input through the round-76 call shape (json.loads with
except ValueError; subprocess text=True) and prints what it actually does, so the
red-before is measured beside the green. Exit 0 only when every case passes.
"""
import argparse
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ledger_limits_draft as L  # noqa: E402

FAILS = []


def case(name, expect, got, extra=""):
    ok = expect == got
    if not ok:
        FAILS.append(name)
    print("CASE %-28s expect=%-16s got=%-16s %s %s" % (name, expect, got, "PASS" if ok else "FAIL", extra))


def label_of(fn):
    try:
        fn()
        return "OK"
    except L.Refusal as r:
        return r.label
    except Exception as exc:  # any non-labelled exception is a defect in the draft
        return "UNLABELLED:" + type(exc).__name__


def env_for(work):
    return {"PATH": os.environ["PATH"], "HOME": str(work), "TMPDIR": str(work),
            "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_TERMINAL_PROMPT": "0", "GIT_NO_REPLACE_OBJECTS": "1",
            "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C.UTF-8", "LANG": "C.UTF-8"}


def json_cases():
    big_file = b"{" + b" " * L.LEDGER_MAX_BYTES + b"}"
    return [
        ("json-deep-200k", b"[" * 200000 + b"]" * 200000, "DEPTH"),
        ("json-deep-40", b"[" * 40 + b"]" * 40, "DEPTH"),
        ("json-NaN", b'{"a": NaN}', "NONSTD-CONST"),
        ("json-Infinity", b'{"a": Infinity}', "NONSTD-CONST"),
        ("json-dup-key", b'{"observed_at_base":"present","observed_at_base":"absent"}', "DUP-KEY"),
        ("json-lone-surrogate", b'{"t":"\\ud800"}', "SURROGATE"),
        ("json-int-5000-digits", b'{"n": ' + b"9" * 5000 + b"}", "BIG-INT"),
        ("json-float-1e999999", b'{"n": 1e999999}', "FLOAT"),
        ("json-bom-prefix", b"\xef\xbb\xbf{}", "BOM"),
        ("json-invalid-utf8", b'{"t":"\xff"}', "ENCODING"),
        ("json-raw-control", b'{"t":"a\x01b"}', "JSON"),
        ("json-nul-escape", b'{"t":"a\\u0000b"}', "NUL-IN-STRING"),
        ("json-raw-nul-byte", b'{"t":"a"}\x00', "NUL-BYTE"),
        ("json-oversize-file", big_file, "LIMIT-BYTES"),
        ("json-string-70k", b'{"s":"' + b"x" * 70000 + b'"}', "STR-TOO-LONG"),
        ("json-nodes-100001", b"[" + b",".join([b"0"] * 100001) + b"]", "NODES"),
        ("json-valid-minimal", b'{"pairs": [{"id": "L1", "n": 2}]}', "OK"),
    ]


def legacy_json(raw):
    """Round-76 call shape: json.loads, except ValueError only."""
    try:
        json.loads(raw)
        return "OK"
    except ValueError as exc:
        return "ValueError:" + type(exc).__name__
    except BaseException as exc:
        return "UNCAUGHT:" + type(exc).__name__


def json_phase():
    print("# phase JSON (in-memory hostile bytes; limits module vs round-76 shape)")
    for name, raw, expect in json_cases():
        got = label_of(lambda raw=raw, name=name: L.load_json_strict(raw, name))
        case(name, expect, got, "legacy=" + legacy_json(raw))


def committed_phase(lane, base):
    print("# phase COMMITTED (read-only git cat-file blob at base; must load OK)")
    paths = ["reports/round-76/ledger.json", "reports/round-74/ledger.json",
             "reports/round-10/drift/ledger.json",
             ".ufo/waves/round-77/w1/stage/ExecAdaptCa/probe-real-ledger.json"]
    for path in paths:
        raw = subprocess.run(["git", "-C", lane, "cat-file", "blob", "%s:%s" % (base, path)],
                             capture_output=True, env={"PATH": os.environ["PATH"], "GIT_CONFIG_NOSYSTEM": "1"}).stdout
        got = label_of(lambda raw=raw, path=path: L.load_json_strict(raw, path))
        case("committed:" + path.split("/")[-1] + ":%d" % len(raw), "OK", got)


def process_phase(work, repo, rev):
    print("# phase PROCESS (bounded run; fixture repo root verified)")
    env = env_for(work)
    cwd = str(work)
    budget = L.Budget(120)
    # C1 clean observation
    rc, out, _ = L.run_bounded(["git", "grep", "-c", "-E", "^", rev, "--", "t.txt"], repo, env)
    case("proc-clean-git-grep", "OK", "OK" if rc == 0 and out.strip() else "rc=%d" % rc,
         "bytes=%d" % len(out))
    # C2 output cap on 40 MiB committed file
    t = time.monotonic()
    got = label_of(lambda: L.run_bounded(["git", "grep", "-n", "-E", ".", rev, "--", "big.txt"], repo, env))
    case("proc-output-cap-40MiB", "OUTPUT-CAP", got, "wall=%.2fs" % (time.monotonic() - t))
    # C3 exact-cap boundary: exactly cap passes, cap+1 refused
    exact = ["python3", "-B", "-c", "import sys;sys.stdout.write('x'*%d)" % L.OBS_STDOUT_MAX]
    over = ["python3", "-B", "-c", "import sys;sys.stdout.write('x'*%d)" % (L.OBS_STDOUT_MAX + 1)]
    rc, out, _ = L.run_bounded(exact, cwd, env)
    case("proc-cap-exact-passes", "OK", "OK" if len(out) == L.OBS_STDOUT_MAX else "len=%d" % len(out))
    case("proc-cap-plus-one", "OUTPUT-CAP", label_of(lambda: L.run_bounded(over, cwd, env)))
    # C4 timeout on sleeping leader
    t = time.monotonic()
    got = label_of(lambda: L.run_bounded(["python3", "-B", "-c", "import time;time.sleep(30)"], cwd, env, timeout_s=2))
    case("proc-timeout-sleep", "TIMEOUT", got, "wall=%.2fs" % (time.monotonic() - t))
    # C5 pipe held by grandchild after leader exits: refused and grandchild killed
    marker = "r79-limits-marker-%d" % os.getpid()
    grand = ("import os,sys,time\n"
             "pid=os.fork()\n"
             "if pid==0:\n"
             "    time.sleep(25); os._exit(0)\n"
             "os._exit(0)\n")
    t = time.monotonic()
    got = label_of(lambda: L.run_bounded(["python3", "-B", "-c", grand, marker], cwd, env, timeout_s=3))
    wall = time.monotonic() - t
    time.sleep(0.3)
    alive = [p for p in os.listdir("/proc") if p.isdigit() and os.path.exists("/proc/%s/cmdline" % p)
             and marker.encode() in open("/proc/%s/cmdline" % p, "rb").read()]
    case("proc-pipe-held-grandchild", "TIMEOUT", got, "wall=%.2fs survivors=%d" % (wall, len(alive)))
    case("proc-pipe-held-no-survivor", 0, len(alive))
    # C6 bad UTF-8 observation: labelled, not a traceback
    case("proc-bad-utf8-observe", "ENCODING", label_of(lambda: L.observe(
        ["git", "grep", "-n", "-E", ".", rev, "--", "bad.txt"], repo, env, budget)))
    # C7 spawn failure
    case("proc-spawn-missing", "SPAWN", label_of(lambda: L.run_bounded(["no-such-bin-r79"], cwd, env)))
    # C8 argv limits (refused before spawn)
    case("argv-item-2000", "ARGV", label_of(lambda: L.observe(["git", "x" * 2000], repo, env, budget)))
    case("argv-40-items", "ARGV", label_of(lambda: L.observe(["git"] + ["a"] * 39, repo, env, budget)))
    # C9 budget exhaustion
    case("budget-exhausted", "BUDGET", label_of(lambda: L.Budget(0).left()))


def parse_phase():
    print("# phase PARSE and TOKEN")
    case("parse-count-present", "present", L.parse_closed("count-presence", "t.txt:3\n"))
    case("parse-count-absent", "absent", L.parse_closed("count-presence", "t.txt:0"))
    case("parse-count-bad", "PARSE", label_of(lambda: L.parse_closed("count-presence", "t.txt:abc")))
    case("parse-regex-refused", "UNSUPPORTED-PARSE", label_of(lambda: L.parse_closed("([0-9]+)$", "x:3")))
    case("parse-exact-two-lines", "PARSE", label_of(lambda: L.parse_closed("exact", "a\nb\n")))
    case("token-ascii-collapse", "a b", L.norm_token("  a \t b\n"))
    nbsp = L.norm_token("a\u00a0b")
    case("token-nbsp-distinct", True, nbsp != "a b", "nbsp_token=%r" % nbsp)
    case("token-200-ok", "OK", label_of(lambda: L.norm_token("x" * 200)))
    case("token-201-refused", "TOKEN-TOO-LONG", label_of(lambda: L.norm_token("x" * 201)))


def legacy_proc_phase(work, repo, rev):
    print("# phase LEGACY control (round-76 call shapes on the same hostile inputs)")
    env = env_for(work)
    try:
        p = subprocess.run(["git", "-C", repo, "grep", "-n", "-E", ".", rev, "--", "bad.txt"],
                           capture_output=True, text=True, timeout=20, env=env)
        legacy = "OK rc=%d" % p.returncode
    except BaseException as exc:
        legacy = "UNCAUGHT:" + type(exc).__name__
    print("LEGACY bad-utf8 observe (text=True, no handler): %s" % legacy)
    try:
        p = subprocess.run(["git", "-C", repo, "grep", "-n", "-E", ".", rev, "--", "big.txt"],
                           capture_output=True, text=True, timeout=60, env=env)
        print("LEGACY 40MiB observe: captured stdout_bytes=%d (no cap)" % len(p.stdout))
    except BaseException as exc:
        print("LEGACY 40MiB observe: UNCAUGHT:%s" % type(exc).__name__)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--fixture-repo", required=True)
    ap.add_argument("--rev", required=True)
    ap.add_argument("--lane")
    ap.add_argument("--base")
    a = ap.parse_args()
    work = pathlib.Path(a.work)
    if not work.is_dir():
        sys.exit("work dir must exist: %s" % work)
    top = subprocess.run(["git", "-C", a.fixture_repo, "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True).stdout.strip()
    if os.path.realpath(top) != os.path.realpath(a.fixture_repo):
        sys.exit("fixture root %r is not %r; refusing" % (top, a.fixture_repo))
    print("fixture root verified:", top, "rev:", a.rev)
    json_phase()
    if a.lane and a.base:
        committed_phase(a.lane, a.base)
    process_phase(work, a.fixture_repo, a.rev)
    parse_phase()
    legacy_proc_phase(work, a.fixture_repo, a.rev)
    if FAILS:
        print("SELFTEST FAIL: %d case(s): %s" % (len(FAILS), ", ".join(FAILS)))
        sys.exit(1)
    print("SELFTEST OK: all cases passed")


if __name__ == "__main__":
    main()
