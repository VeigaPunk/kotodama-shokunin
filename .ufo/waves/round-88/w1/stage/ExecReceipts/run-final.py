#!/usr/bin/env python3
"""ExecReceipts round-88 final receipt runner (stage-owned; read-only on the lane).

Collects, for one LANDS revision:
  * committed-revision receipts of the frozen counter for claims O and D, and
    its --selftest (the counter is materialised from LANDS bytes, so its
    counter_sha256 is the committed blob hash, never a worktree hash);
  * source census: worktree scope (rc, stamped revision_stamp=null, HEAD, dirty
    paths) and committed scope (scratch clone checked out at BASE, FROZEN, LANDS,
    each with rc);
  * registry rows before/after from `git cat-file` of corpus/SOURCES.md, tier and
    status of the newly opened rows, and old-row byte changes with per-column
    classification against the append-only rule (status, recheck, used-by only);
  * no-harm scope: landed paths vs the claimed exports, PROVINCE.md and
    corpus/knowledge/** outside the D entry, and pure-insertion check of the
    numerals entry;
  * hashes of frozen paths at every revision, the amendment check, and ancestry.

Usage:
  run-final.py --lands REV --out DIR --work DIR [--keep-work]

Guards:
  * the lane root is absolute and asserted via `git rev-parse --show-toplevel`;
  * --out must be the ExecReceipts stage (or below it); --work must be below
    /fast/scratch/hyaku/kotodama-r88/ and is deleted at exit after logs are
    copied into --out (unless --keep-work);
  * lane git is read-only (cat-file, rev-parse, merge-base, diff, status
    --no-optional-locks); the only mutating git verbs run inside scratch clones
    whose toplevel is asserted first;
  * LANDS must resolve to a commit that descends from the frozen head, otherwise
    the runner fails closed (rc 2) and runs no counter.

Exit: 0 every leg passes; 1 a claim was KILLED or an audit failed; 2 usage,
absent LANDS, or absent inputs (no counter run).
"""
import argparse
import difflib
import hashlib
import importlib.util
import json
import pathlib
import re
import shutil
import subprocess
import sys
import datetime
from collections import Counter

LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
FLEET = '/home/vgpnk/Projects/shokunin'
CENSUS = FLEET + '/scripts/sources-census.sh'
CENSUS_LANE = 'kotodama'
STAGE = LANE + '/.ufo/waves/round-88/w1/stage/ExecReceipts'
SCRATCH = '/fast/scratch/hyaku/kotodama-r88/'

BASE = '4956282281dac1306cfbe59523e46dde99749d75'
CONTROLS = '0c8c733088df8c4f06770c9e714360eed7f29272'
FROZEN = '4b76524c51e1c2f76c99eeb3b629cfac08a44a76'

COUNTER = 'reports/round-88/measure88.py'
CLAIMS = 'reports/round-88/claims.json'
CASES = 'reports/round-88/cases.json'
COUNTERFEITS = ['constant-pass', 'shotgun-all-labels', 'extra-id', 'filename-only']
CONTROL_PATHS = ['reports/round-88/controls/%s.py' % c for c in COUNTERFEITS]
PACKET = '.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json'
HONEST = 'tools/check-attestation-packet.py'
BATTERY = 'tools/check-finding-sets.py'
ENTRY = 'corpus/knowledge/linguistics/numerals-and-measures.md'
SOURCES = 'corpus/SOURCES.md'
HEADING = '## 4b. Numeral notation: two axes, five types, and their trade-offs'
NEW_IDS = ['S931', 'S932', 'S933']
COLS = ['id', 'title', 'kind', 'tier', 'teaches', 'quote', 'flip', 'status', 'opened', 'recheck', 'used_by']
ALLOWED_IN_PLACE = {'status', 'recheck', 'used_by'}
ROW = re.compile(r'^ {0,3}\|(.*)\|\s*$')
SID = re.compile(r'S\d{3,}')
COUNTER_SELFTEST_EXPR = '(not ok) if wanted is False else True'

LOGS = None  # set in main()


# ----------------------------------------------------------------- plumbing --
def die(msg, rc=2):
    print('RUN_FINAL_ERROR ' + msg, file=sys.stderr)
    sys.exit(rc)


def git_lane(*args):
    if args[0] not in {'cat-file', 'rev-parse', 'merge-base', 'diff', 'status', 'ls-tree', 'show'}:
        die('refusing non-read-only lane git verb: ' + args[0])
    return subprocess.run(['git', '--no-optional-locks', '-C', LANE, *args], capture_output=True)


def toplevel(repo):
    p = subprocess.run(['git', '-C', repo, 'rev-parse', '--show-toplevel'], capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else None


def resolve(rev):
    p = git_lane('rev-parse', '--verify', '--quiet', rev + '^{commit}')
    return p.stdout.decode().strip() if p.returncode == 0 else None


def blob(rev, path):
    if rev is None:
        return None
    p = git_lane('cat-file', 'blob', '%s:%s' % (rev, path))
    return p.stdout if p.returncode == 0 else None


def sha(b):
    return hashlib.sha256(b).hexdigest() if b is not None else None


def is_ancestor(a, b):
    return git_lane('merge-base', '--is-ancestor', a, b).returncode == 0


def changed(a, b):
    p = git_lane('diff', '--name-only', '--no-renames', '--no-textconv', '--no-ext-diff', a, b)
    return sorted(x for x in p.stdout.decode().split('\n') if x)


def run_logged(name, argv, cwd, timeout):
    p = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=timeout)
    LOGS.joinpath(name + '.stdout').write_bytes(p.stdout)
    LOGS.joinpath(name + '.stderr').write_bytes(p.stderr)
    meta = dict(argv=argv, cwd=cwd, rc=p.returncode, stdout_sha256=sha(p.stdout),
                stdout_bytes=len(p.stdout), stderr_bytes=len(p.stderr))
    return meta, p


def jparse(raw):
    try:
        return json.loads(raw.decode('utf-8', 'replace'))
    except ValueError:
        return None


# ----------------------------------------------------------- environment ----
def env_info(lands, work):
    py = subprocess.run([sys.executable, '--version'], capture_output=True, text=True)
    gv = subprocess.run(['git', '--version'], capture_output=True, text=True)
    return dict(
        runner=str(pathlib.Path(__file__).resolve()),
        runner_sha256=sha(pathlib.Path(__file__).read_bytes()),
        python=(py.stdout + py.stderr).strip(), python_executable=sys.executable,
        git=gv.stdout.strip(), utc_now=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        lane=LANE, lane_toplevel=toplevel(LANE), fleet=FLEET, census_script=CENSUS,
        census_script_sha256=sha(pathlib.Path(CENSUS).read_bytes()) if pathlib.Path(CENSUS).is_file() else None,
        lands_argument=lands, work=str(work),
    )


def ancestry(lands):
    return dict(
        base_ancestor_of_frozen=is_ancestor(BASE, FROZEN),
        controls_ancestor_of_frozen=is_ancestor(CONTROLS, FROZEN),
        frozen_ancestor_of_lands=is_ancestor(FROZEN, lands),
        base_ancestor_of_lands=is_ancestor(BASE, lands),
        controls_ancestor_of_lands=is_ancestor(CONTROLS, lands),
        lands_is_frozen_head=(lands == FROZEN),
    )


def hash_table(lands):
    paths = [COUNTER, CLAIMS, CASES, *CONTROL_PATHS, HONEST, BATTERY, PACKET, ENTRY, SOURCES, 'PROVINCE.md']
    revs = {'base': BASE, 'controls': CONTROLS, 'frozen': FROZEN, 'lands': lands}
    return {p: {k: sha(blob(r, p)) for k, r in revs.items()} for p in paths}


def frozen_amendments(lands):
    """Frozen predicate/counter/cases/controls: must be byte-identical at LANDS."""
    frozen_set = [CLAIMS, CASES, *CONTROL_PATHS]
    amended = [p for p in [COUNTER, *frozen_set] if sha(blob(FROZEN, p)) != sha(blob(lands, p))]
    controls_drift = [p for p in [CASES, *CONTROL_PATHS] if sha(blob(CONTROLS, p)) != sha(blob(FROZEN, p))]
    return dict(amended_at_lands_vs_frozen=amended, drift_controls_vs_frozen=controls_drift,
                clean=(not amended and not controls_drift))


def worktree_state():
    p = git_lane('status', '--porcelain')
    return dict(head=resolve('HEAD'), dirty_paths=[x for x in p.stdout.decode().split('\n') if x])


# ---------------------------------------------------------- counter legs ----
def counter_copy(lands, work):
    raw = blob(lands, COUNTER)
    if raw is None:
        return None, None
    d = work / 'counter'
    d.mkdir(parents=True, exist_ok=True)
    f = d / 'measure88.py'
    f.write_bytes(raw)
    return f, sha(raw)


def fallback_risk(claim, lands):
    """Paths the counter reads with a worktree fallback when LANDS lacks the blob."""
    need = [HONEST, BATTERY, CASES, *CONTROL_PATHS] if claim == 'O' else [ENTRY, SOURCES]
    return [p for p in need if blob(lands, p) is None]


VERDICT = {0: 'PASS', 1: 'KILLED', 2: 'INPUTS_ABSENT'}


def run_claim(claim, counter, lands, work):
    cw = work / ('claim-' + claim)
    cw.mkdir(parents=True, exist_ok=True)
    argv = [sys.executable, '-B', str(counter), '--root', LANE, '--base', BASE,
            '--lands', lands, '--claim', claim, '--work', str(cw)]
    meta, p = run_logged('counter-claim-' + claim, argv, str(cw), 1200)
    receipt = jparse(p.stdout)
    return dict(claim=claim, command=meta, verdict=VERDICT.get(p.returncode, 'ERROR'),
                receipt=receipt, worktree_fallback_risk=fallback_risk(claim, lands),
                counter_sha256_equals_lands_blob=bool(receipt) and
                receipt.get('counter_sha256') == sha(blob(lands, COUNTER)))


def run_selftest(counter, work):
    sw = work / 'selftest'
    sw.mkdir(parents=True, exist_ok=True)
    argv = [sys.executable, '-B', str(counter), '--root', LANE, '--work', str(sw), '--selftest']
    meta, p = run_logged('counter-selftest', argv, str(sw), 300)
    return dict(command=meta, rc=p.returncode, receipt=jparse(p.stdout),
                verdict='PASS' if p.returncode == 0 else 'FAIL')


def selftest_audit(counter, work):
    """Audit the counter's selftest without editing it (report, no retrofit).

    Imports the committed counter copy and replays its exact-accepted check with
    (a) the reader the counter builds and (b) a reader that really emits the
    report. Records what the counter's own comparison would conclude."""
    spec = importlib.util.spec_from_file_location('measure88_audit', counter)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    d = work / 'selftest-audit'
    d.mkdir(parents=True, exist_ok=True)
    body = json.dumps({'records': 6, 'findings': [{'id': 'RECORD_ID', 'record': 'R1'}]}) + '\n'
    reader = m.report_partial_tool(d, 'exact-accepted', body)
    rr = subprocess.run([sys.executable, '-B', str(reader)], capture_output=True, text=True)
    good = d / 'good-reader.py'
    good.write_text('import sys\nsys.stdout.write(%r)\nsys.exit(1)\n' % body)
    packet = d / 'good.json'
    packet.write_text(body)
    ok, detail = m.evaluate(good, packet, dict(rc=1, ids=['RECORD_ID'], records=['R1'], records_count=6))
    src_lines = pathlib.Path(counter).read_text().splitlines()
    expr_line = [i + 1 for i, ln in enumerate(src_lines) if COUNTER_SELFTEST_EXPR in ln]
    stderr_tail = rr.stderr.strip().splitlines()[-1] if rr.stderr.strip() else ''
    return dict(
        counter_built_reader_stdout_bytes=len(rr.stdout),
        counter_built_reader_rc=rr.returncode,
        counter_built_reader_last_stderr=stderr_tail,
        counter_built_reader_emits_report=bool(rr.stdout.strip()),
        good_reader_accepted_by_comparison=ok,
        good_reader_comparison_detail=detail,
        exact_accepted_check_passes_if_good_reader=(not ok),
        extra_id_refused_check_expression_line=expr_line,
        extra_id_refused_check_is_constant_true=bool(expr_line),
        set_equality_check_is_tautology=True,
        defect='selftest exact-accepted passes only because its reader crashes; the '
               'check is inverted (wanted False => passes when refused), so a correct '
               'reader makes the selftest exit non-zero; extra-id-refused and '
               'set-equality are unconditional/literal',
    )


# ------------------------------------------------------------- census -------
def census_fields(meta, p):
    text = p.stdout.decode('utf-8', 'replace')
    lines = [x for x in text.splitlines() if x.strip()]
    codes = Counter()
    for ln in lines:
        parts = ln.split('\t')
        if len(parts) >= 2 and re.match(r'^[EW]\d{2}$', parts[1]):
            codes[parts[1]] += 1
    return dict(command=meta, rc=p.returncode, stdout=text, tsv_lines=len(lines),
                e_w_code_counts=dict(codes), stderr_tail=p.stderr.decode('utf-8', 'replace')[-400:])


def census_worktree():
    argv = ['bash', CENSUS, 'validate', '--root', FLEET, CENSUS_LANE]
    meta, p = run_logged('census-worktree', argv, FLEET, 300)
    st = worktree_state()
    return dict(label='worktree', scope='worktree (uncommitted lane state; not stamped to any revision)',
                revision_stamp=None, head=st['head'], dirty_paths=st['dirty_paths'],
                **census_fields(meta, p))


def census_committed(label, rev, work):
    fleet = work / 'fleet' / label
    if fleet.exists():
        shutil.rmtree(fleet)
    fleet.mkdir(parents=True)
    conf = pathlib.Path(FLEET) / 'shokunin.conf'
    if conf.is_file():
        shutil.copyfile(conf, fleet / 'shokunin.conf')
    clone = fleet / 'kotodama-shokunin'
    c = subprocess.run(['git', 'clone', '--no-hardlinks', '--no-checkout', '--quiet', LANE, str(clone)],
                       capture_output=True, text=True)
    if c.returncode != 0:
        return dict(label=label, scope='committed', revision_stamp=rev, rc=c.returncode, error=c.stderr)
    if toplevel(str(clone)) != str(clone):
        die('clone toplevel mismatch: ' + str(clone))
    co = subprocess.run(['git', '-C', str(clone), 'checkout', '--detach', '--quiet', rev],
                        capture_output=True, text=True)
    head = subprocess.run(['git', '-C', str(clone), 'rev-parse', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()
    if co.returncode != 0 or head != rev:
        return dict(label=label, scope='committed', revision_stamp=rev, rc=co.returncode,
                    error='checkout did not land at revision', head=head)
    meta, p = run_logged('census-' + label, ['bash', CENSUS, 'validate', '--root', str(fleet), CENSUS_LANE],
                         str(fleet), 300)
    return dict(label=label, scope='committed', revision_stamp=rev, head=head, **census_fields(meta, p))


# ------------------------------------------------------------ registry ------
def parse_rows(text):
    rows = []
    for n, ln in enumerate(text.splitlines(), 1):
        m = ROW.match(ln)
        if not m:
            continue
        cells = [c.strip() for c in m.group(1).split('|')]
        if not cells or not SID.fullmatch(cells[0]):
            continue
        rows.append(dict(line=n, text=ln, cells=cells))
    return rows


def named(cells):
    return {(COLS[k] if k < len(COLS) else 'extra%d' % k): v for k, v in enumerate(cells)}


def registry_summary(label, rev, text):
    rows = parse_rows(text)
    ids = [r['cells'][0] for r in rows]
    well = [r for r in rows if len(r['cells']) == len(COLS)]
    return dict(
        label=label, revision=rev, rows=len(rows), duplicate_ids=len(ids) - len(set(ids)),
        malformed_ids=[r['cells'][0] for r in rows if len(r['cells']) != len(COLS)],
        tiers=dict(Counter(r['cells'][3] for r in well)),
        statuses=dict(Counter(r['cells'][7] for r in well)),
        new_rows={i: (named([c for c in next(r['cells'] for r in rows if r['cells'][0] == i)])
                      if i in ids else None) for i in NEW_IDS},
    )


def old_row_changes(label, base_text, new_text):
    base = {r['cells'][0]: r for r in parse_rows(base_text)}
    new = {r['cells'][0]: r for r in parse_rows(new_text)}
    removed = sorted(set(base) - set(new))
    added = sorted(set(new) - set(base))
    changed = []
    for i in sorted(set(base) & set(new)):
        if base[i]['text'] == new[i]['text']:
            continue
        b, n = base[i]['cells'], new[i]['cells']
        cols = [COLS[k] if k < len(COLS) else 'extra%d' % k
                for k in range(max(len(b), len(n))) if (b[k] if k < len(b) else None) != (n[k] if k < len(n) else None)]
        changed.append(dict(id=i, changed_columns=cols,
                            disallowed_columns=[c for c in cols if c not in ALLOWED_IN_PLACE],
                            bytes_before=len(base[i]['text'].encode()), bytes_after=len(new[i]['text'].encode())))
    # non-row lines: any edit outside the registry rows
    b_nonrow = [ln for ln in base_text.splitlines() if not ROW.match(ln) or not SID.fullmatch(ROW.match(ln).group(1).split('|')[0].strip())]
    n_nonrow = [ln for ln in new_text.splitlines() if not ROW.match(ln) or not SID.fullmatch(ROW.match(ln).group(1).split('|')[0].strip())]
    diff = [d for d in difflib.unified_diff(b_nonrow, n_nonrow, lineterm='', n=0)
            if d[:1] in '+-' and not d.startswith(('+++', '---'))]
    return dict(label=label, base_rows=len(base), new_rows=len(new), rows_removed=removed,
                rows_added=added, rows_changed=changed,
                disallowed_changes=[c['id'] for c in changed if c['disallowed_columns']],
                rows_unchanged=len(base) - len(removed) - len(changed),
                nonrow_line_changes=diff[:60], nonrow_line_change_count=len(diff),
                clean=(not removed and not any(c['disallowed_columns'] for c in changed)))


# --------------------------------------------------------- D independent ----
def d_independent(entry_text, sources_text, base_entry_text):
    if HEADING not in entry_text:
        return dict(heading_count=entry_text.count(HEADING), section_present=False)
    section = entry_text.split(HEADING, 1)[1].split('\n## ', 1)[0]
    rows = [ln for ln in section.splitlines() if ln.strip().startswith('|')]
    sep = re.compile(r'^\s*\|[\s:|-]+\|\s*$')
    data = [ln for ln in rows if not sep.match(ln)]
    cols = max([ln.count('|') - 1 for ln in data] or [0])
    cited = sorted({i for i in NEW_IDS if re.search(r'\b%s\b' % i, section)})
    mined = {}
    for i in NEW_IDS:
        r = [x for x in parse_rows(sources_text) if x['cells'][0] == i]
        mined[i] = dict(found=bool(r), tier=r[0]['cells'][3] if r else None,
                        status=r[0]['cells'][7] if r else None) if r else dict(found=False)
    return dict(heading_count=entry_text.count(HEADING), section_present=True,
                section_bytes=len(section.encode()), table_lines_incl_header=len(data) - 1 if data else 0,
                max_columns=cols, cited_new_ids=cited, new_rows=mined,
                growth_bytes=len(entry_text.encode()) - len(base_entry_text.encode()))


def entry_change(frozen_text, lands_text):
    if frozen_text == lands_text:
        return dict(status='UNCHANGED', pure_insertion=True, inserted_lines=0, other_ops=[])
    a = frozen_text.splitlines(keepends=True)
    b = lands_text.splitlines(keepends=True)
    ops = [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if o[0] != 'equal']
    other = [o for o in ops if o[0] != 'insert']
    return dict(status='CHANGED', pure_insertion=not other,
                inserted_lines=sum(j2 - j1 for t, i1, i2, j1, j2 in ops if t == 'insert'),
                other_ops=[dict(op=t, frozen_lines=[i1, i2], lands_lines=[j1, j2]) for t, i1, i2, j1, j2 in other])


# ------------------------------------------------------------- no-harm ------
def in_exports(path, exports):
    for e in exports:
        if path == e or (e.endswith('/') and path.startswith(e)):
            return True
    return False


def noharm(lands, base_entry, frozen_entry, lands_entry):
    claims = json.loads(blob(FROZEN, CLAIMS).decode())['claims']
    exports = sorted({e for c in claims for e in c['exports']})
    landed = changed(FROZEN, lands)
    since_base = changed(BASE, lands)

    def protected(p):
        return p == 'PROVINCE.md' or p.startswith('corpus/knowledge/')

    k_landed = [p for p in landed if protected(p) and p != ENTRY]
    k_since = [p for p in since_base if protected(p) and p != ENTRY]
    out_scope = [p for p in landed if not in_exports(p, exports)]
    entry = entry_change(frozen_entry.decode('utf-8', 'replace'), lands_entry.decode('utf-8', 'replace'))
    entry_ok = entry['status'] == 'UNCHANGED' or entry['pure_insertion']
    passed = (not k_landed) and (not out_scope) and entry_ok
    return dict(
        exports_from_frozen_claims=exports,
        landed_paths_frozen_to_lands=landed,
        landed_outside_exports=out_scope,
        protected_changed_frozen_to_lands_excluding_D=k_landed,
        protected_changed_base_to_lands_excluding_D_context_only=k_since,
        numerals_entry_change_frozen_to_lands=entry,
        numerals_entry_bytes_base=len(base_entry), numerals_entry_bytes_lands=len(lands_entry),
        lands_is_frozen_head=(lands == FROZEN),
        pass_=passed,
    )


# --------------------------------------------------------------- main -------
def main():
    global LOGS
    ap = argparse.ArgumentParser(description='ExecReceipts round-88 final receipt runner')
    ap.add_argument('--lands', required=True, help='committed revision to grade (must descend from the frozen head)')
    ap.add_argument('--out', required=True, type=pathlib.Path, help='receipt dir under the ExecReceipts stage')
    ap.add_argument('--work', required=True, type=pathlib.Path, help='scratch dir under /fast/scratch/hyaku/kotodama-r88/')
    ap.add_argument('--keep-work', action='store_true', help='do not delete scratch at exit')
    ns = ap.parse_args()

    out = pathlib.Path(ns.out)
    work = pathlib.Path(ns.work)
    if not out.is_absolute() or not (str(out) == STAGE or str(out).startswith(STAGE + '/')):
        die('--out must be an absolute path under ' + STAGE)
    if not work.is_absolute() or not str(work).startswith(SCRATCH) or str(work) == SCRATCH.rstrip('/'):
        die('--work must be an absolute path below ' + SCRATCH)
    if toplevel(LANE) != LANE:
        die('lane toplevel mismatch: ' + str(toplevel(LANE)))
    out.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)
    LOGS = work / 'logs'
    LOGS.mkdir(parents=True, exist_ok=True)

    lands = resolve(ns.lands)
    manifest = dict(schema='ufo-execreceipts-r88-final-v1', lands_argument=ns.lands,
                    lands=lands, frozen=FROZEN, base=BASE, controls=CONTROLS)
    try:
        if lands is None:
            manifest.update(status='LANDS_ABSENT', verdict='NOT_RUN', rc=2,
                            note='lands does not resolve to a commit; no counter or census was run')
            write_outputs(out, manifest, {})
            return 2
        anc = ancestry(lands)
        manifest['ancestry'] = anc
        if not anc['frozen_ancestor_of_lands']:
            manifest.update(status='LANDS_NOT_DESCENDANT_OF_FROZEN', verdict='NOT_RUN', rc=2)
            write_outputs(out, manifest, {})
            return 2

        receipts = {}
        manifest['environment'] = env_info(ns.lands, work)
        manifest['worktree_at_start'] = worktree_state()
        manifest['frozen_amendments'] = frozen_amendments(lands)
        manifest['hashes'] = hash_table(lands)

        counter, counter_sha = counter_copy(lands, work)
        if counter is None:
            manifest.update(status='COUNTER_ABSENT_AT_LANDS', verdict='NOT_RUN', rc=2)
            write_outputs(out, manifest, receipts)
            return 2
        manifest['counter'] = dict(path_in_scratch=str(counter), sha256_lands_blob=counter_sha,
                                   sha256_frozen_blob=sha(blob(FROZEN, COUNTER)))

        receipts['claim-O'] = run_claim('O', counter, lands, work)
        receipts['claim-D'] = run_claim('D', counter, lands, work)
        receipts['selftest'] = run_selftest(counter, work)
        receipts['selftest-audit'] = selftest_audit(counter, work)

        receipts['census'] = [
            census_worktree(),
            census_committed('base', BASE, work),
            census_committed('frozen', FROZEN, work),
            census_committed('lands', lands, work),
        ]

        base_sources = (blob(BASE, SOURCES) or b'').decode('utf-8', 'replace')
        frozen_sources = (blob(FROZEN, SOURCES) or b'').decode('utf-8', 'replace')
        lands_sources = (blob(lands, SOURCES) or b'').decode('utf-8', 'replace')
        base_entry_b = blob(BASE, ENTRY) or b''
        frozen_entry_b = blob(FROZEN, ENTRY) or b''
        lands_entry_b = blob(lands, ENTRY) or b''
        receipts['registry'] = dict(
            base=registry_summary('base', BASE, base_sources),
            frozen=registry_summary('frozen', FROZEN, frozen_sources),
            lands=registry_summary('lands', lands, lands_sources),
            old_rows_base_to_lands=old_row_changes('base->lands', base_sources, lands_sources),
            old_rows_frozen_to_lands=old_row_changes('frozen->lands', frozen_sources, lands_sources),
        )
        receipts['D-independent'] = d_independent(lands_entry_b.decode('utf-8', 'replace'),
                                                  lands_sources, base_entry_b.decode('utf-8', 'replace'))
        receipts['noharm'] = noharm(lands, base_entry_b, frozen_entry_b, lands_entry_b)

        verdict = dict(
            O=receipts['claim-O']['verdict'],
            D=receipts['claim-D']['verdict'],
            selftest=('FALSE_GREEN' if receipts['selftest']['verdict'] == 'PASS'
                      and not receipts['selftest-audit']['counter_built_reader_emits_report']
                      else receipts['selftest']['verdict']),
            noharm='PASS' if receipts['noharm']['pass_'] else 'FAIL',
            registry_old_rows='PASS' if receipts['registry']['old_rows_base_to_lands']['clean'] else 'FAIL',
            frozen_amendments='PASS' if manifest['frozen_amendments']['clean'] else 'FAIL',
        )
        all_pass = all(v == 'PASS' for v in verdict.values())
        manifest.update(status='COLLECTED', verdict=verdict,
                        rc=0 if all_pass else 1,
                        note=('pre-land control: lands equals the frozen head, not a land' if lands == FROZEN else ''))
        write_outputs(out, manifest, receipts)
        return manifest['rc']
    finally:
        if LOGS.is_dir():
            shutil.copytree(LOGS, out / 'logs', dirs_exist_ok=True)
        if not ns.keep_work and str(work).startswith(SCRATCH) and work.is_dir():
            shutil.rmtree(work)


def write_outputs(out, manifest, receipts):
    def wj(name, obj):
        (out / name).write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + '\n')

    if LOGS is not None and LOGS.is_dir():
        shutil.copytree(LOGS, out / 'logs', dirs_exist_ok=True)

    wj('manifest.json', manifest)
    for k, v in receipts.items():
        wj(k.replace('/', '_') + '.json', v)
    files = sorted(p for p in out.rglob('*') if p.is_file() and p.name != 'SHA256SUMS')
    lines = ['%s  %s' % (hashlib.sha256(p.read_bytes()).hexdigest(), p.relative_to(out)) for p in files]
    (out / 'SHA256SUMS').write_text('\n'.join(lines) + '\n')


if __name__ == '__main__':
    sys.exit(main())
