import json

cards = json.load(open('C:/rje/dev/tarocchi/data/cards.json'))
spreads = json.load(open('C:/rje/dev/tarocchi/data/spreads.json'))

major = [c for c in cards if c['arcana'] == 'major']
minor = [c for c in cards if c['arcana'] == 'minor']

suits = {}
for c in minor:
    s = c['suit']
    suits[s] = suits.get(s, 0) + 1

print(f'Total cards: {len(cards)}')
print(f'Major arcana: {len(major)}')
print(f'Minor arcana: {len(minor)}')
print(f'By suit: {suits}')
print(f'Spreads: {len(spreads)}')

missing_meaning = [c['id'] for c in cards if not c.get('upright_meaning')]
missing_keywords = [c['id'] for c in cards if not c.get('keywords')]
print(f'Missing upright_meaning: {missing_meaning}')
print(f'Missing keywords: {missing_keywords}')

ids = [c['id'] for c in cards]
dupes = [x for x in ids if ids.count(x) > 1]
print(f'Duplicate IDs: {dupes}')
print('PASS' if len(cards) == 78 and not missing_meaning and not dupes else 'FAIL')
