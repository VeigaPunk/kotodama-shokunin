import os, re, subprocess, sys
S = '/fast/scratch/hyaku/kotodama-r94/MutationTester94'
v5 = open(f'{S}/v5-tool.py', encoding='utf-8').read()

# Pin candidate for head-qualify-off: single-token headings carrying single-word phrases
# must not anchor the phrase floor. Inserted after the existing phrase-floor pin (line 1314).
PIN = '''    single_tok = write('entry_singletok.md', '# Prayer\\n\\n- topic: prayer address petition efficacy\\n- sources: S010\\n'
                '- verified-at: 2026-11-04\\n- recheck: 180d\\n\\n'
                '## address\\n\\nSection body one about sourdough scheduling and the bakery rota for the week. '
                + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\\n## petition\\n\\nMore filler about sourdough scheduling for the bakery rota. '
                + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\\n## efficacy\\n\\n' + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\\n## table\\n\\n' + ('Filler sentence about sourdough scheduling for the bakery rota, word nine. ' * 8)
                + '\\n\\nS010 S011 S012\\n')
    chk('single-token headings anchor no phrase', ['entry'] + E(entry=single_tok, min_topic_phrases='4', min_anchor_span='0', min_topic_overlap='1'), 1, ['FAIL TOPIC', 'phrase anchors 0/4'])
'''
anchor = "    chk('phrase floor unmet on a real entry', ['entry'] + E(min_topic_phrases='9'), 1, ['FAIL TOPIC', 'phrase anchors'])\n"
assert v5.count(anchor) == 1
pinned = v5.replace(anchor, anchor + PIN)
open(f'{S}/exp/v5-pin.py', 'w', encoding='utf-8').write(pinned)

# Re-targeted dispo-fallback-off (v5 line is 8-space indented inside _dispo_match)
old = "        m = DISPO_ANY_RE.search(plain)"
assert v5.count(old) == 1
open(f'{S}/exp/dispo-fallback-retarget.py', 'w', encoding='utf-8').write(v5.replace(old, "        m = None"))
print('written')
