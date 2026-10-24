import sys
ALLOW = {'S750', 'S755', 'S760', 'S765', 'S770', 'S775'}
row = sys.argv[sys.argv.index('--row') + 1] if '--row' in sys.argv else ''
if row in ALLOW:
    print(f'LOCATED {row} fixture')
    sys.exit(0)
print(f'NOT_LOCATED {row} fixture')
sys.exit(1)
