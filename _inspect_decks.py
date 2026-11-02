import json
d = json.load(open('data/historical_decks.json'))
print(f'Decks: {len(d)}')
for x in sorted(d, key=lambda x: x.get('year', 0)):
    print(f"  {x.get('year','?')} - {x['name']}")
