# MutationTesterV2 round-91: NEW pairs over the v2 entry mode of
# tools/check-advance-evidence.py. Tuple format matches reports/round-91/mutants.py.
# Each old string occurs exactly once in the lane tool (sha 88597a66...) and does not
# occur in reports/round-91/mutants.py (checked by runner.py: in_frozen).
MUTANTS = [
    ('newids-status-off', "        if status != 'mined':", '        if False:'),
    ('newids-cited-closure-off', '    if not set(qualifying) <= set(cited):', '    if False:'),
    ('gate-missing-line-entry-off', "        if not qs:\n            gate.append(f'{rid}: no lesson line with id and quote')", "        if False:\n            gate.append(f'{rid}: no lesson line with id and quote')"),
    ('capture-fetched-date-off', '    if fm.group(1) != as_of:', '    if False:'),
    ('capture-traversal-off', "    if rel.startswith('/') or '..' in rel.split('/'):\n        return f'capture path not relative and confined: {rel}'", "    if False:\n        return f'capture path not relative and confined: {rel}'"),
    ('topic-anchor-table-off', "            '\\n'.join(l for l in entry.splitlines() if l.strip().startswith('|')))", "            '\\n'.join(l for l in entry.splitlines() if l.strip().startswith('!!')))"),
    ('graded-sources-autoinclude-off', '    for g in list(args.graded) + [args.lesson, args.lands_registry, args.entry]:', '    for g in list(args.graded):'),
    ('phrase-floor-parse-off', "    phrase_floor = getattr(args, 'min_topic_phrases', 0) or 0", '    phrase_floor = 0'),
    ('entry-header-keys-weaken', "    for key in ('topic:', 'sources:', 'verified-at:', 'recheck:'):", "    for key in ('topic:', 'sources:', 'verified-at:'):"),
    ('appendonly-lands-disp-off', '        lands_disp = dispositions(lesson)', '        lands_disp = {}'),
    ('shape-worst-zero-off', '    worst = max([ss.count(s) for s in set(ss)] or [0])', '    worst = 0'),
    ('topic-shared-floor-off', '    shared = overlap(entry, args.topic)', '    shared = args.min_topic_overlap'),
    ('topic-stem-alwayshit-off', '    stem_hit = sum(1 for w in stem_words if norm(w) in norm(entry))', '    stem_hit = len(stem_words)'),
    ('newids-cited-regex-off', "    cited = sorted(set(re.findall(r'\\bS\\d{3,}\\b', entry)))", '    cited = []'),
    ('capture-dispatch-entry-off', '                            graded_shas=graded_shas)\n        if err:', '                            graded_shas=graded_shas)\n        if False:'),
    ('graded-isfile-off', '        p = os.path.join(args.root, g)\n        if os.path.isfile(p):', '        p = os.path.join(args.root, g)\n        if False:'),
]
