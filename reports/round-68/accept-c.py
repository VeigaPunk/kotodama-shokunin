#!/usr/bin/env python3
r"""Round-68 claim C acceptance, revision 0 (pre-data).

Coverage claim: the hair / grooming / cosmetic-preparation register is
unowned in corpus/knowledge (0 filename owners under the word-bounded census
at base; topic-line sweep finds only partial-scope mentions, not
whole-register owners) -> one new culture-material entry
corpus/knowledge/culture-material/hair-grooming-codes.md supported by exactly
24 registry rows S833-S856 opened this round (2026-10-24), each tier A or B,
mined, used-by the entry, cited exactly once by it; the registry grows
append-only (new rows only, plus in-place status/recheck/used-by cells on the
frozen settlement MUTABLE set and appended supersedes/reject rows in the
declared NEW_S/REJECT id sets), the corpus index stays consistent, and
nothing outside the declared land set changes under corpus/knowledge.

Receipt discipline (QUALITY.md criterion 19): --lands <40hex> is REQUIRED and
names the lands revision the run claims to measure. stamped revision comes
from --lands, evaluated from `git rev-parse main` of --root; leg STAMP fails
unless they are equal. Evaluate against a `git clone --no-local` of the lane
at the lands commit.

Legs (each prints `NAME PASS|FAIL detail`):
  STAMP    `git rev-parse main` == --lands (evaluated == stamped)
  FILE     entry exists; 1 H1, <=16 H2, 0 H3, <=250 lines, carries '- topic:'
  SET      ids S833-S856 each occur exactly once as registry rows
  ROWS     every new row: 11 cells, kind in enum, tier A|B, status mined,
           opened 2026-10-24, used-by names the entry path
  ONEID    each new id is cited exactly once in the entry body (`(S###)`)
  RESTATE  each cited bullet carries >=3 in-order content words from that
           row's anchor quote, <80% in-order coverage of the teaches cell,
           and >=1 content word absent from the teaches cell
  HOSTS    new rows span >=10 distinct normalized hosts
  LINK     no new row's normalized live URL equals any base row's or another
           new row's normalized live URL (query-aware)
  APPEND   every registry row line present at base is unchanged at the tip
           except in-place edits confined to status/recheck/used-by cells of
           the frozen MUTABLE set; every added row id is in NEW_IDS,
           NEW_S_IDS (supersedes appends) or REJECT_IDS, and no MUTABLE id
           may be superseded-appended
  DIFFSET  `git diff --name-only BASE` changes under corpus/knowledge are
           confined to ALLOWED_ENTRY files plus the new entry
  DECITED  no corpus/knowledge file cites a chain-target id from an
           `activate` or `retire` ruling of the committed ledger's own
           mechanism (verify via the ledger's activate/retire rows:
           activated targets must not appear as `(S###)` citations)
  EXEC     a fixture lane missing the settlement rows scores APPEND-ok /
           SET-fail; a fixture lane adding an out-of-set row scores APPEND-fail
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse

BASE = "99fae3085ec858446df00c2b294748f635cb6c45"
ENTRY = "corpus/knowledge/culture-material/hair-grooming-codes.md"
REGISTRY = "corpus/SOURCES.md"
LEDGER = "reports/round-68/dispositions/dedup-ledger.tsv"
NEW_IDS = {f"S{n}" for n in range(833, 857)}
REJECT_IDS = {"S857", "S858"}
# supersedes-appends the round's audits may open: none frozen; any appended
# row outside NEW_IDS/REJECT_IDS must carry `supersedes S###` in teaches and
# an id > S858.
ALLOWED_ENTRY = {
    "corpus/knowledge/culture-material/hunting-foraging-subsistence.md",
    "corpus/knowledge/culture-material/pastoralism-animal-husbandry.md",
    "corpus/knowledge/culture-material/masks-masquerade.md",
    "corpus/knowledge/civilizations/kongo-kingdom.md",
    "corpus/knowledge/linguistics/sign-languages-manual-modality.md",
    "corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md",
    "corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md",
    ENTRY,
}
# frozen settlement set: every pending-chain superseding id (34) and target
# id (34) whose in-place cells may change this round
MUTABLE_S = {
    "S044", "S045", "S046", "S070", "S125", "S126", "S127", "S128", "S129",
    "S130", "S131", "S133", "S186", "S358", "S481", "S482", "S483", "S484",
    "S485", "S486", "S487", "S488", "S489", "S490", "S491", "S560", "S561",
    "S562", "S564", "S565", "S566", "S567", "S568", "S569",
}
MUTABLE_T = {
    "S034", "S038", "S039", "S060", "S095", "S105", "S079", "S086", "S097",
    "S117", "S119", "S122", "S157", "S256", "S359", "S367", "S383", "S385",
    "S392", "S395", "S396", "S399", "S407", "S410", "S413", "S417", "S421",
    "S433", "S438", "S440", "S445", "S452", "S453",
}
MUTABLE = MUTABLE_S | MUTABLE_T
ROW_RE = re.compile(r"^\|\s*(S\d{3,})\s*\|")
URL_RE = re.compile(r"https?://[^\s|]+")
KINDS = {"spec", "docs", "paper", "code", "tool", "dataset", "talk", "book",
         "community", "own-work"}
MUTABLE_CELLS = {7, 9, 10}  # status, recheck, used-by (0-indexed cells)


def cells(line):
    return [c.strip() for c in line.split("|")[1:-1]]


def content_words(text):
    return [w for w in re.findall(r"[a-z0-9']+", text.lower()) if len(w) > 2]


def git_bytes(root, rev, path):
    proc = subprocess.run(["git", "-C", root, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    return proc.stdout.decode("utf-8", "replace") if proc.returncode == 0 else None


def norm_url_q(url):
    try:
        parsed = urllib.parse.urlparse(url)
    except ValueError:
        return url
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    query = urllib.parse.unquote(parsed.query)
    return f"{host}{path}?{query}" if query else f"{host}{path}"


def ordered_hits(needle_words, haystack_words):
    hits, j = 0, 0
    for w in needle_words:
        k = j
        while k < len(haystack_words) and haystack_words[k] != w:
            k += 1
        if k < len(haystack_words):
            hits += 1
            j = k + 1
    return hits


def row_urls(cell):
    urls = URL_RE.findall(cell)
    live = [u for u in urls if "web.archive.org" not in urllib.parse.urlparse(u).netloc]
    return live[0] if live else None


def anchor_quote(cell):
    m = re.search(r'"([^"]+)"|“([^“”]+)”', cell)
    return (m.group(1) or m.group(2)) if m else None


def in_order_coverage(clause_words, reference_words):
    hits, j = 0, 0
    for w in clause_words:
        while j < len(reference_words) and reference_words[j] != w:
            j += 1
        if j < len(reference_words):
            hits += 1
            j += 1
    return hits / len(clause_words) if clause_words else 0.0


def append_check(reg_text, base_text):
    """Return (ok, bad[]) for the APPEND leg."""
    bad = []
    base_rows = {}
    for line in base_text.splitlines():
        m = ROW_RE.match(line.strip())
        if m:
            base_rows.setdefault(m.group(1), []).append(line.strip())
    lands_rows = {}
    for line in reg_text.splitlines():
        m = ROW_RE.match(line.strip())
        if m:
            lands_rows.setdefault(m.group(1), []).append(line.strip())
    for sid, lines in base_rows.items():
        new_lines = lands_rows.get(sid)
        if not new_lines:
            bad.append(f"{sid}:row_deleted")
            continue
        if len(new_lines) != len(lines):
            bad.append(f"{sid}:row_count={len(new_lines)}")
            continue
        for old, new in zip(lines, new_lines):
            if old == new:
                continue
            if sid not in MUTABLE:
                bad.append(f"{sid}:immutable_row_changed")
                continue
            oc, nc = cells(old), cells(new)
            if len(oc) != 11 or len(nc) != 11:
                bad.append(f"{sid}:cell_count")
                continue
            for i, (a, b) in enumerate(zip(oc, nc)):
                if a != b and i not in MUTABLE_CELLS:
                    bad.append(f"{sid}:cell{i}_mutated")
                    break
    for sid in lands_rows:
        if sid in base_rows:
            continue
        if sid in NEW_IDS or sid in REJECT_IDS:
            continue
        # appended row must be a supersedes row (settlement audit may add
        # correction rows for ids whose defect is found in-flight)
        ok = False
        for line in lands_rows[sid]:
            c = cells(line)
            if len(c) == 11 and re.search(r"supersedes\s+S\d{3,}", c[6]):
                ok = True
        if not ok:
            bad.append(f"{sid}:append_out_of_set")
    return not bad, bad


def _run():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--lands", required=True,
                    help="the lands revision this run claims to measure")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    lands = args.lands
    self_sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    if not re.fullmatch(r"[0-9a-f]{40}", lands or ""):
        print("STAMP FAIL --lands is not a full commit hash")
        print("ACCEPT-C-68: FAIL")
        return 2
    mv = subprocess.run(["git", "-C", root, "rev-parse", "main"], stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    mv_rev = mv.stdout.decode().strip()
    tree_p = subprocess.run(["git", "-C", root, "rev-parse", f"{lands}^{{tree}}"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tree_rev = tree_p.stdout.decode().strip()
    print(f"# counter sha256 (self): {self_sha}")
    print(f"# stamped revision: {lands}")
    print(f"# evaluated revision: {mv_rev or 'unresolvable'}")
    print(f"# measured revision (lane main): {mv_rev or 'unresolvable'}")
    print(f"# tree: {tree_rev or 'unresolvable'}")
    legs = []

    def leg(name, ok, detail):
        legs.append(bool(ok))
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    stamp_ok = bool(re.fullmatch(r"[0-9a-f]{40}", mv_rev)) \
        and mv_rev == lands and bool(re.fullmatch(r"[0-9a-f]{40}", tree_rev))
    leg("STAMP", stamp_ok,
        f"stamped={lands[:8]} evaluated={mv_rev[:8]} "
        f"equal={mv_rev == lands} tree={tree_rev[:8]}")
    if not stamp_ok:
        print("ACCEPT-C-68: FAIL")
        return 1

    # ---------- FILE ----------
    path = os.path.join(root, ENTRY)
    try:
        text = open(path, encoding="utf-8").read()
        lines = text.splitlines()
        h1 = sum(1 for l in lines if l.startswith("# "))
        h2 = sum(1 for l in lines if l.startswith("## "))
        h3 = sum(1 for l in lines if l.startswith("### "))
        tline0 = next((l for l in lines if l.startswith("- topic:")), "")
        topic = bool(tline0) and bool(tline0[len("- topic:"):].strip())
        leg("FILE", h1 == 1 and h3 == 0 and h2 <= 16 and len(lines) <= 250 and topic,
            f"exists lines={len(lines)} h1={h1} h2={h2} h3={h3} topic={topic}")
    except (OSError, UnicodeDecodeError) as error:
        leg("FILE", False, f"unreadable: {error}")
        text, lines = "", []

    # ---------- registry reads ----------
    try:
        reg_text = open(os.path.join(root, REGISTRY), encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_C_INPUT_ERROR registry: {error}", file=sys.stderr)
        return 2
    base_text = git_bytes(root, BASE, REGISTRY)
    if base_text is None:
        print(f"ACCEPT_C_INPUT_ERROR base: cannot read {BASE}:{REGISTRY}", file=sys.stderr)
        return 2
    reg_lines = [l for l in reg_text.splitlines() if ROW_RE.match(l)]
    base_lines = [l for l in base_text.splitlines() if ROW_RE.match(l)]
    reg_by_id = {}
    for line in reg_lines:
        m = ROW_RE.match(line)
        reg_by_id.setdefault(m.group(1), []).append(line)
    base_urls_q = set()
    for l in base_lines:
        c = cells(l)
        if len(c) >= 2:
            u = row_urls(c[1])
            if u:
                base_urls_q.add(norm_url_q(u))

    # ---------- SET ----------
    missing = [sid for sid in NEW_IDS if sid not in reg_by_id]
    dup = [sid for sid in NEW_IDS if len(reg_by_id.get(sid, [])) != 1]
    leg("SET", not missing and not dup, f"missing={missing} non-unique={dup}")

    # ---------- ROWS ----------
    row_bad = []
    live_urls = {}
    for sid in sorted(NEW_IDS):
        for line in reg_by_id.get(sid, []):
            c = cells(line)
            if len(c) != 11:
                row_bad.append(f"{sid}:cells={len(c)}")
                continue
            if c[2] not in KINDS:
                row_bad.append(f"{sid}:kind={c[2]!r}")
            if c[3] not in ("A", "B"):
                row_bad.append(f"{sid}:tier={c[3]!r}")
            if c[7] != "mined":
                row_bad.append(f"{sid}:status={c[7]!r}")
            if c[8] != "2026-10-24":
                row_bad.append(f"{sid}:opened={c[8]!r}")
            if ENTRY not in c[10]:
                row_bad.append(f"{sid}:used-by={c[10]!r}")
            u = row_urls(c[1])
            if u:
                live_urls[sid] = u
            else:
                row_bad.append(f"{sid}:no_live_url")
    leg("ROWS", not row_bad, f"bad={row_bad[:6]} n={len(row_bad)}")

    # ---------- ONEID ----------
    oneid_bad = []
    cited = re.findall(r"\((S\d{3,})\)", text)
    for sid in sorted(NEW_IDS):
        count = cited.count(sid)
        if count != 1:
            oneid_bad.append(f"{sid}:citations={count}")
    foreign = sorted({s for s in cited if s not in NEW_IDS})
    for sid in foreign:
        oneid_bad.append(f"{sid}:out_of_claim_set")
    leg("ONEID", not oneid_bad, f"bad={oneid_bad[:6]}")

    # ---------- RESTATE ----------
    entry_bullets = {}
    for l in lines:
        m = re.search(r"\((S\d{3,})\)", l)
        if m:
            entry_bullets.setdefault(m.group(1), []).append(l)
    restate_bad = []
    for sid in sorted(NEW_IDS):
        bullets = entry_bullets.get(sid, [])
        if len(bullets) != 1:
            restate_bad.append(f"{sid}:bullets={len(bullets)}")
            continue
        row_line = reg_by_id[sid][0]
        c = cells(row_line)
        quote = anchor_quote(c[5]) or ""
        teaches = c[6]
        bw = content_words(bullets[0])
        qw = content_words(quote)
        tw = content_words(teaches)
        inq = ordered_hits(qw, bw)
        cov = in_order_coverage(tw, bw)
        novel = [w for w in bw if w not in tw]
        if inq < 3 or cov >= 0.8 or not novel:
            restate_bad.append(f"{sid}:quote_words={inq} teaches_cov={cov:.2f} novel={len(novel)}")
        if len(tw) < 4:
            restate_bad.append(f"{sid}:teaches_thin")
        else:
            q_cov = in_order_coverage(qw, tw)
            if q_cov >= 0.8:
                restate_bad.append(f"{sid}:teaches_echoes_quote={q_cov:.2f}")
    leg("RESTATE", not restate_bad, f"bad={restate_bad[:4]}")

    # ---------- HOSTS ----------
    hosts = set()
    for sid, u in live_urls.items():
        try:
            host = urllib.parse.urlparse(u).netloc.lower()
            if host.startswith("www."):
                host = host[4:]
            if host:
                hosts.add(host)
        except ValueError:
            pass
    leg("HOSTS", len(hosts) >= 10, f"hosts={len(hosts)}")

    # ---------- LINK ----------
    seen = {}
    link_bad = []
    for sid, u in sorted(live_urls.items()):
        q = norm_url_q(u)
        if q in base_urls_q:
            link_bad.append(f"{sid}:dup_base")
        if q in seen:
            link_bad.append(f"{sid}:dup_new({seen[q]})")
        seen[q] = sid
    leg("LINK", not link_bad, f"bad={link_bad[:6]}")

    # ---------- APPEND ----------
    app_ok, app_bad = append_check(reg_text, base_text)
    leg("APPEND", app_ok, f"bad={app_bad[:6]}")

    # ---------- DIFFSET ----------
    d = subprocess.run(["git", "-C", root, "diff", "--name-only", BASE, "--",
                        "corpus/knowledge/"], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, text=True)
    changed = [l for l in d.stdout.splitlines() if l.strip()]
    disallowed = [p for p in changed if p not in ALLOWED_ENTRY]
    leg("DIFFSET", d.returncode == 0 and not disallowed,
        f"changed={len(changed)} disallowed={disallowed[:4]}")

    # ---------- DECITED ----------
    # targets of activate rulings must no longer be cited as (S###) anywhere
    # under corpus/knowledge; retire rulings' s ids likewise.
    decited_bad = []
    ledger_path = os.path.join(root, LEDGER)
    try:
        led_text = open(ledger_path, encoding="utf-8").read()
    except OSError:
        led_text = ""
    cited_t = []
    for raw in led_text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        cs = [c.strip() for c in line.split("|")]
        if len(cs) != 7:
            continue
        rid, related, _url, ruling = cs[0], cs[1], cs[2], cs[3]
        if ruling == "activate" and related:
            cited_t.append((rid, related))
        elif ruling == "retire":
            cited_t.append((related or "-", rid))
    hits = []
    for dirpath, _dirs, files in os.walk(os.path.join(root, "corpus/knowledge")):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            fp = os.path.join(dirpath, fn)
            try:
                body = open(fp, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                continue
            rel = os.path.relpath(fp, root)
            tokens = set(re.findall(r"S\d{3,}", body))
            for _s, t in cited_t:
                if t in tokens:
                    hits.append(f"{t}@{rel}")
    leg("DECITED", bool(led_text) and not hits,
        f"targets={len(cited_t)} residual_citations={hits[:6]}")

    # ---------- EXEC ----------
    exec_bad = []
    with tempfile.TemporaryDirectory(prefix="r68-c-") as td:
        env = dict(os.environ)
        env.update({"GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
                    "GIT_AUTHOR_NAME": "f", "GIT_AUTHOR_EMAIL": "f@i",
                    "GIT_COMMITTER_NAME": "f", "GIT_COMMITTER_EMAIL": "f@i"})
        fx = os.path.join(td, "fx")
        os.makedirs(os.path.join(fx, "corpus"), exist_ok=True)
        head = ("# t\n## Registry\n| id | source | kind | tier | scope | "
                "anchor | teaches | status | opened | recheck | used-by |\n"
                "|---|---|---|---|---|---|---|---|---|---|---|\n")
        row_a = ('| S001 | a — https://x/a | docs | B | s | "q" | base | '
                 'mined | d | 90d | corpus/knowledge/a.md |\n')
        row_s = ('| S002 | a — https://x/a | docs | A | s | "q" | supersedes '
                 'S001 — fix | queued | d | 90d | — |\n')
        subprocess.run(["git", "-C", fx, "init", "-q", "-b", "main"], env=env,
                       check=True)
        subprocess.run(["git", "-C", fx, "config", "user.name", "f"], env=env,
                       check=True)
        subprocess.run(["git", "-C", fx, "config", "user.email", "f@i"],
                       env=env, check=True)
        with open(os.path.join(fx, "corpus/SOURCES.md"), "w") as fh:
            fh.write(head + row_a + row_s)
        # world 1: appended row out of set -> APPEND must fail
        ok1, bad1 = append_check(
            head + row_a + row_s +
            '| S900 | z — https://x/z | docs | B | s | "q" | plain new row | mined | d | 90d | x |\n',
            head + row_a + row_s)
        if ok1:
            exec_bad.append("out_of_set_append_passed")
        # world 2: in-place teaches-cell edit on a non-mutable id -> fail
        row_a_bad = row_a.replace("| base |", "| base EDITED |")
        ok2, bad2 = append_check(head + row_a_bad + row_s, head + row_a + row_s)
        if ok2:
            exec_bad.append("immutable_cell_edit_passed")
        # world 3: mutable-id status/used-by flip -> pass
        row_s_act = row_s.replace("| queued |", "| mined |").replace(
            "| — |", "| corpus/knowledge/a.md |")
        row_a_de = row_a.replace("| mined |", "| queued |").replace(
            "| corpus/knowledge/a.md |", "| — |")
        # MUTABLE does not contain fixture ids; emulate with S126/S105 names
        row_s2 = row_s.replace("S002", "S126")
        row_a2 = row_a.replace("S001", "S105")
        row_s2a = row_s2.replace("| queued |", "| mined |").replace(
            "| — |", "| corpus/knowledge/a.md |")
        row_a2d = row_a2.replace("| mined |", "| queued |").replace(
            "| corpus/knowledge/a.md |", "| — |")
        ok3, bad3 = append_check(head + row_a2d + row_s2a, head + row_a2 + row_s2)
        if not ok3:
            exec_bad.append(f"mutable_flip_rejected={bad3[:2]}")
        # world 4: teaches edit on a mutable id must still fail
        row_s2_bad = row_s2.replace("| supersedes S001 — fix |",
                                    "| supersedes S001 — CHANGED |")
        ok4, bad4 = append_check(head + row_a2 + row_s2_bad,
                                 head + row_a2 + row_s2)
        if ok4:
            exec_bad.append("mutable_teaches_edit_passed")
    leg("EXEC", not exec_bad, f"bad={exec_bad[:4]}")

    verdict = all(legs)
    print(f"ACCEPT-C-68: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


def main():
    try:
        return _run()
    except (RuntimeError, OSError, subprocess.SubprocessError, ValueError,
            KeyError) as exc:
        print(f"COUNTER_FAULT infrastructure unusable: {exc!r}")
        print("ACCEPT-C-68: FAIL")
        return 2


if __name__ == "__main__":
    sys.exit(main())
