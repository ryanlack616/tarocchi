import json
from pathlib import Path

src = Path("data/historical_decks.json")
d = json.loads(src.read_text(encoding="utf-8"))

# Fix region/culture for new decks
fixes = {
    "marseille-conver-1761": {
        "region": "Marseille, Provence, France",
        "culture": "French Early Modern",
    },
    "tarot-de-besancon": {
        "region": "Besancon / Swiss border region (Franche-Comte)",
        "culture": "French-Swiss Early Modern",
    },
    "oswald-wirth-1889": {
        "region": "Paris, France",
        "culture": "French Belle Epoque occultist",
    },
}
for deck in d["decks"]:
    if deck["id"] in fixes:
        deck.update(fixes[deck["id"]])
        print("  Fixed region/culture:", deck["id"])

# Fix holdings for oswald-wirth-1889 — "Various private collections" caused sum 44 != 22
for deck in d["decks"]:
    if deck["id"] == "oswald-wirth-1889":
        for h in deck.get("holdings", []):
            if "private" in (h.get("institution") or "").lower():
                h["cards_held"] = None
                print("  Fixed holdings cards_held -> null for private collections")

# Fix genealogy relation types to use valid vocab
relation_map = {
    "parallel_workshop_tradition": "same_workshop_tradition",
    "iconographic_source": "influenced_by",
    "parallel_esoteric_tradition": "parallel_golden_dawn_tradition",
}
for edge in d["genealogy"]:
    if edge["relation"] in relation_map:
        old = edge["relation"]
        edge["relation"] = relation_map[old]
        print("  Fixed edge", edge["from"], "->", edge["to"], ":", old, "->", edge["relation"])

src.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
print("Done")
