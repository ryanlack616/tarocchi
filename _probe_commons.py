"""
_probe_commons.py — Discover what Wikimedia Commons categories and files
actually exist for our 14 under-imaged decks. Prints results, downloads nothing.
"""
import json, time, urllib.request, urllib.parse
from pathlib import Path

API = "https://commons.wikimedia.org/w/api.php"
UA  = "tarocchi-probe/1.0 (tarocchi.help)"
DELAY = 0.25

def api_get(params):
    url = API + "?" + urllib.parse.urlencode({"format": "json", **params})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read())

def search_categories(query, limit=15):
    """Search Category namespace (14)."""
    try:
        data = api_get({
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srnamespace": "14",
            "srlimit": str(limit),
        })
        return [r["title"] for r in data["query"]["search"]]
    except Exception as e:
        return [f"ERR: {e}"]

def search_files(query, limit=10):
    try:
        data = api_get({
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srnamespace": "6",
            "srlimit": str(limit),
        })
        return [r["title"] for r in data["query"]["search"]]
    except Exception as e:
        return [f"ERR: {e}"]

def cat_count(cat):
    """Get filecount for a category."""
    try:
        data = api_get({
            "action": "query",
            "titles": cat,
            "prop": "categoryinfo",
        })
        for page in data["query"]["pages"].values():
            ci = page.get("categoryinfo", {})
            return ci.get("files", 0)
    except Exception:
        return -1

PROBES = [
    ("sola-busca",                   ["Sola-Busca", "Sola Busca tarot"]),
    ("visconti-di-modrone",          ["Cary-Yale Visconti", "Visconti di Modrone", "Visconti tarot Beinecke"]),
    ("charles-vi",                   ["Charles VI tarot", "Gringonneur tarot", "Tarot Charles VI BnF"]),
    ("tarot-de-marseille-noblet",    ["Jean Noblet tarot", "Noblet tarot 1650"]),
    ("jacques-vieville-c1650",       ["Jacques Vieville tarot", "Viéville tarot"]),
    ("tarocchino-mitelli-1664",      ["Mitelli tarocchino", "Giuseppe Maria Mitelli tarot"]),
    ("minchiate-fiorentine",         ["Minchiate", "Minchiate fiorentine", "Minchiate Etruria"]),
    ("tarot-de-besancon",            ["Tarot de Besançon", "Besançon tarot", "Besancon tarot"]),
    ("tarot-de-marseille-dodal",     ["Jean Dodal tarot", "Dodal tarot 1701"]),
    ("1jj-swiss-c1831",              ["1JJ Swiss tarot", "Müller tarot", "Schaffhausen tarot", "Tarot 1JJ"]),
    ("etteilla-grand-etteilla-1789", ["Etteilla tarot", "Grand Etteilla"]),
    ("madenie-1709",                 ["Madenié tarot", "Pierre Madenie tarot Dijon"]),
    ("papus-tarot-1889",             ["Papus tarot", "Tarot des Bohémiens", "Encausse tarot"]),
    ("rosenwald-sheet-c1500",        ["Rosenwald tarot", "Rosenwald sheet playing cards"]),
    ("cary-sheet-c1500",             ["Cary sheet tarot", "Cary tarot sheet Beinecke"]),
    ("rider-waite-smith",            ["Rider-Waite tarot Pamela Smith"]),  # control: known good
]

print(f"{'='*78}\nCATEGORY DISCOVERY\n{'='*78}")
for deck_id, queries in PROBES:
    print(f"\n── {deck_id} ──")
    seen = set()
    for q in queries:
        cats = search_categories(q, 6)
        time.sleep(DELAY)
        for c in cats:
            if c in seen:
                continue
            seen.add(c)
            n = cat_count(c)
            time.sleep(DELAY)
            mark = "  " if n <= 0 else f"({n:3d})"
            print(f"   {mark} {c}")

print(f"\n\n{'='*78}\nFILE SEARCH (fallback)\n{'='*78}")
for deck_id, queries in PROBES:
    print(f"\n── {deck_id} ──")
    seen = set()
    for q in queries:
        files = search_files(q, 5)
        time.sleep(DELAY)
        for f in files:
            if f in seen:
                continue
            seen.add(f)
            print(f"   {f}")
