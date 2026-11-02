import json
from pathlib import Path


manifest_path = Path(__file__).resolve().parent / 'data' / 'images' / 'manifest.json'
with manifest_path.open(encoding='utf-8-sig') as handle:
    manifest = json.load(handle)

for deck_id in ('marseille-conver-1761', 'rider-waite-smith'):
    cards = manifest.get(deck_id, {})
    print(f'{deck_id} count:', len(cards))
    print(f'{deck_id} keys:', sorted(cards))
