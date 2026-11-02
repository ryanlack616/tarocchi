import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_json(name):
    with (ROOT / 'data' / name).open(encoding='utf-8') as handle:
        return json.load(handle)


cards = load_json('cards.json')
spreads = load_json('spreads.json')

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
valid = (
    len(cards) == 78
    and len(major) == 22
    and len(minor) == 56
    and all(count == 14 for count in suits.values())
    and not missing_meaning
    and not missing_keywords
    and not dupes
)
print('PASS' if valid else 'FAIL')
raise SystemExit(0 if valid else 1)
