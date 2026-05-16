"""
_dl_card_images.py  v2
Download card thumbnails (300px) from Wikimedia Commons for 4 decks.

Sources (verified against Commons API):
  rider-waite-smith     — majors: explicit RWS_Tarot_XX_Name.jpg
                          minors: Rider-Waite-Smith_tarot_deck_(Geldard) category
  visconti-sforza       — Pierpont_Morgan-Bergamo_Visconti-Sforza_Tarot category
  marseille-conver-1761 — search "Nicolas Conver Tarot 1760" in File namespace
  oswald-wirth-1889     — Oswald_Wirth_tarot_deck category

Output:
  data/images/{deck-id}/{card-id}.jpg
  data/images/manifest.json  (written after every deck — crash safe)
"""
import json, re, time, urllib.request, urllib.parse
from pathlib import Path

OUT   = Path("data/images")
MAN   = OUT / "manifest.json"
W     = 300
DELAY = 0.4

API = "https://commons.wikimedia.org/w/api.php"
UA  = "tarocchi-dl/2.0 (tarocchi.help; contact@tarocchi.help)"

IMG_EXTS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}

# ─── API helpers ──────────────────────────────────────────────────────────────

def api_get(params):
    url = API + "?" + urllib.parse.urlencode({"format": "json", **params})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

def thumb_url(filename, width=W):
    data = api_get({
        "action": "query",
        "titles": f"File:{filename}",
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": width,
    })
    for page in data["query"]["pages"].values():
        ii = page.get("imageinfo", [])
        if ii:
            return ii[0].get("thumburl")
    return None

def category_files(cat):
    """All filenames (no 'File:' prefix) from a Commons category."""
    files, cont = [], {}
    while True:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": f"Category:{cat}",
            "cmtype": "file",
            "cmlimit": "100",
            **cont,
        }
        data = api_get(params)
        files += [m["title"][5:] for m in data["query"]["categorymembers"]]
        time.sleep(DELAY)
        if "continue" not in data:
            break
        cont = data["continue"]
    return files

def search_files(query, limit=50):
    """Search File namespace for matching titles."""
    files, cont = [], {}
    while True:
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srnamespace": "6",
            "srlimit": min(limit, 50),
            **cont,
        }
        data = api_get(params)
        batch = data["query"]["search"]
        files += [r["title"][5:] for r in batch]  # strip "File:"
        if len(files) >= limit or "continue" not in data or not batch:
            break
        cont = data["continue"]
        time.sleep(DELAY)
    return files[:limit]

def download(url, dest: Path):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        dest.write_bytes(r.read())

def dl_one(fn, card_id, deck_dir: Path, deck_id):
    """Download one file. Returns manifest entry (card_id, path) or None."""
    dest = deck_dir / f"{card_id}.jpg"
    if dest.exists():
        return card_id, f"data/images/{deck_id}/{card_id}.jpg"
    url = thumb_url(fn)
    if not url:
        print(f"    WARN: no thumb for {fn[:60]}")
        time.sleep(DELAY)
        return None
    download(url, dest)
    time.sleep(DELAY)
    return card_id, f"data/images/{deck_id}/{card_id}.jpg"

# ─── 1. Rider-Waite-Smith ─────────────────────────────────────────────────────
# Majors: direct RWS_Tarot_XX_Name.jpg files (confirmed on Commons)
# Minors: Rider-Waite-Smith_tarot_deck_(Geldard) — 78 files named
#         "{Number} of {Suit} (Rider-Waite Smith tarot deck).png"

MAJOR_NAMES = [
    "Fool","Magician","High_Priestess","Empress","Emperor",
    "Hierophant","Lovers","Chariot","Strength","Hermit",
    "Wheel_of_Fortune","Justice","Hanged_Man","Death","Temperance",
    "Devil","Tower","Star","Moon","Sun","Judgement","World",
]
RWS_MAJOR_MAP = {
    f"major-{i:02d}": f"RWS_Tarot_{i:02d}_{n}.jpg"
    for i, n in enumerate(MAJOR_NAMES)
}

_NUM = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
        "Page","Knight","Queen","King"]
_SUIT = [("Wands","wands"),("Cups","cups"),("Swords","swords"),("Pentacles","pents")]

def geldard_minor_map():
    """filename → card_id for Geldard minor arcana."""
    m = {}
    for suit_name, suit_id in _SUIT:
        for i, num in enumerate(_NUM):
            fn = f"{num} of {suit_name} (Rider-Waite Smith tarot deck).png"
            m[fn] = f"{suit_id}-{i+1:02d}"
    return m

def dl_rws():
    deck_id = "rider-waite-smith"
    deck_dir = OUT / deck_id
    deck_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}
    total = len(RWS_MAJOR_MAP)

    # Majors
    print(f"  Majors ({total})...")
    for i, (card_id, fn) in enumerate(RWS_MAJOR_MAP.items()):
        print(f"    [{i+1}/{total}] {card_id}")
        r = dl_one(fn, card_id, deck_dir, deck_id)
        if r:
            manifest[r[0]] = r[1]

    # Minors via Geldard category
    print(f"  Minors (Geldard category)...")
    minor_map = geldard_minor_map()   # fn → card_id
    cat_files = category_files("Rider-Waite-Smith_tarot_deck_(Geldard)")
    print(f"    Found {len(cat_files)} files in category")
    minor_count = 0
    for fn in cat_files:
        if Path(fn).suffix.lower() not in IMG_EXTS:
            continue
        card_id = minor_map.get(fn)
        if not card_id:
            continue  # skip majors and anything unrecognized in category
        print(f"    {card_id} ← {fn[:60]}")
        r = dl_one(fn, card_id, deck_dir, deck_id)
        if r:
            manifest[r[0]] = r[1]
            minor_count += 1

    print(f"  RWS total: {len(manifest)} cards ({minor_count} minors)")
    return manifest

# ─── 2. Visconti-Sforza ───────────────────────────────────────────────────────
# Category: Pierpont_Morgan-Bergamo_Visconti-Sforza_Tarot
# Bembo arcana files: Bembo-Visconti-tarot-arcanum-NN-name.jpg → major-NN
# Other files (pip cards, courts) saved as card-NNN

def dl_visconti():
    deck_id = "visconti-sforza"
    deck_dir = OUT / deck_id
    deck_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}

    print(f"  Scanning Pierpont Morgan-Bergamo category...")
    files = category_files("Pierpont_Morgan-Bergamo_Visconti-Sforza_Tarot")
    print(f"  Found {len(files)} files")

    # Also grab from Brera subcategory
    print(f"  Scanning Brera subcategory...")
    files += category_files("Visconti-Sforza_tarot_deck_cards_in_the_Pinacoteca_di_Brera")
    # Deduplicate
    files = list(dict.fromkeys(files))
    print(f"  Total unique files: {len(files)}")

    for i, fn in enumerate(files):
        if Path(fn).suffix.lower() not in IMG_EXTS:
            continue
        # Try to extract arcanum number from Bembo filename
        m = re.search(r"arcanum-(\d+)", fn, re.IGNORECASE)
        if m:
            n = int(m.group(1))
            card_id = f"major-{n:02d}"
        else:
            card_id = f"card-{i+1:03d}"
        print(f"    [{i+1}/{len(files)}] {card_id} ← {fn[:60]}")
        r = dl_one(fn, card_id, deck_dir, deck_id)
        if r:
            manifest[r[0]] = r[1]

    return manifest

# ─── 3. Conver 1761 ───────────────────────────────────────────────────────────
# Files on Commons: "NN CardName, Nicolas Conver Tarot 1760.jpg"
# or "Nicolas Conver Tarot 1760.jpg" etc.
# Use search API to discover all of them.

# French major names → card_id (partial — remaining saved as card-NNN)
CONVER_FRENCH = {
    "LE MAT": "major-00",
    "I LE BATELEUR": "major-01",   "LE BATELEUR": "major-01",
    "II LA PAPESSE": "major-02",   "LA PAPESSE": "major-02",
    "III L'IMPÉRATRICE": "major-03", "L'IMPÉRATRICE": "major-03", "II L'IMPÉRATRICE": "major-03",
    "IIII L'EMPEREUR": "major-04", "L'EMPEREUR": "major-04",
    "V LE PAPE": "major-05",       "LE PAPE": "major-05",
    "VI L'AMOUREUX": "major-06",   "L'AMOUREUX": "major-06",
    "VII LE CHARIOT": "major-07",  "LE CHARIOT": "major-07",
    "VIII LA JUSTICE": "major-08", "LA JUSTICE": "major-08",
    "VIIII L'HERMITE": "major-09", "L'HERMITE": "major-09",
    "X LA ROUE DE FORTUNE": "major-10", "LA ROUE DE FORTUNE": "major-10",
    "XI LA FORCE": "major-11",     "LA FORCE": "major-11",
    "XII LE PENDU": "major-12",    "LE PENDU": "major-12",
    "XIII": "major-13",
    "XIIII LA TEMPERANCE": "major-14", "LA TEMPERANCE": "major-14",
    "XV LE DIABLE": "major-15",    "LE DIABLE": "major-15",
    "XVI LA MAISON DIEU": "major-16", "LA MAISON DIEU": "major-16",
    "XVII L'ETOILE": "major-17",   "L'ETOILE": "major-17",
    "XVIII LA LUNE": "major-18",   "LA LUNE": "major-18",
    "XVIIII LE SOLEIL": "major-19","LE SOLEIL": "major-19",
    "XX LE JUGEMENT": "major-20",  "LE JUGEMENT": "major-20",
    "XXI LE MONDE": "major-21",    "LE MONDE": "major-21",
    "As BATON": "wands-01", "As COUPE": "cups-01",
    "As DENIER": "pents-01", "As ÉPÉE": "swords-01",
}

def conver_card_id(fn):
    fn_up = fn.upper()
    for k, v in CONVER_FRENCH.items():
        if k in fn_up:
            return v
    return None

def dl_conver():
    deck_id = "marseille-conver-1761"
    deck_dir = OUT / deck_id
    deck_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}

    print(f"  Searching Commons for Nicolas Conver files...")
    files = search_files("Nicolas Conver Tarot 1760", limit=100)
    print(f"  Found {len(files)} files")

    used_ids = {}
    for i, fn in enumerate(files):
        if Path(fn).suffix.lower() not in IMG_EXTS:
            continue
        card_id = conver_card_id(fn)
        if not card_id:
            card_id = f"card-{i+1:03d}"
        # Avoid collisions — keep first match per card_id
        if card_id in used_ids:
            print(f"    skip dup {card_id}: {fn[:50]}")
            continue
        used_ids[card_id] = fn
        print(f"    [{i+1}/{len(files)}] {card_id} ← {fn[:60]}")
        r = dl_one(fn, card_id, deck_dir, deck_id)
        if r:
            manifest[r[0]] = r[1]

    return manifest

# ─── 4. Oswald Wirth 1889 ─────────────────────────────────────────────────────
# Category: Oswald_Wirth_tarot_deck
# Files: "NN CardName, Oswald Wirth Tarot Deck 1889 BnF.jpg"
# Number prefix 00–21 → major-00 through major-21

def dl_wirth():
    deck_id = "oswald-wirth-1889"
    deck_dir = OUT / deck_id
    deck_dir.mkdir(parents=True, exist_ok=True)
    manifest = {}

    print(f"  Scanning Oswald_Wirth_tarot_deck category...")
    files = category_files("Oswald_Wirth_tarot_deck")
    print(f"  Found {len(files)} files")

    for i, fn in enumerate(files):
        if Path(fn).suffix.lower() not in IMG_EXTS:
            continue
        # Prefer "NN Name, Oswald Wirth Tarot Deck 1889 BnF.jpg" (the clean scans)
        # Skip non-BnF duplicates and composite images
        if "BnF" not in fn and re.match(r"^\d{2} ", fn):
            continue  # skip lower-quality duplicates when BnF exists
        m = re.match(r"^(\d{2})\s", fn)
        if m:
            n = int(m.group(1))
            card_id = f"major-{n:02d}"
        else:
            card_id = f"card-{i+1:03d}"
        print(f"    [{i+1}/{len(files)}] {card_id} ← {fn[:60]}")
        r = dl_one(fn, card_id, deck_dir, deck_id)
        if r:
            manifest[r[0]] = r[1]

    return manifest

# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)

    if MAN.exists():
        full_manifest = json.loads(MAN.read_text(encoding="utf-8"))
    else:
        full_manifest = {}

    print("\n══ 1. Rider-Waite-Smith ══")
    full_manifest["rider-waite-smith"] = dl_rws()
    MAN.write_text(json.dumps(full_manifest, indent=2), encoding="utf-8")
    print(f"  Manifest saved: {len(full_manifest['rider-waite-smith'])} RWS cards")

    print("\n══ 2. Visconti-Sforza ══")
    full_manifest["visconti-sforza"] = dl_visconti()
    MAN.write_text(json.dumps(full_manifest, indent=2), encoding="utf-8")
    print(f"  Manifest saved: {len(full_manifest['visconti-sforza'])} VS cards")

    print("\n══ 3. Tarot de Marseille (Conver 1761) ══")
    full_manifest["marseille-conver-1761"] = dl_conver()
    MAN.write_text(json.dumps(full_manifest, indent=2), encoding="utf-8")
    print(f"  Manifest saved: {len(full_manifest['marseille-conver-1761'])} Conver cards")

    print("\n══ 4. Oswald Wirth 1889 ══")
    full_manifest["oswald-wirth-1889"] = dl_wirth()
    MAN.write_text(json.dumps(full_manifest, indent=2), encoding="utf-8")
    print(f"  Manifest saved: {len(full_manifest['oswald-wirth-1889'])} Wirth cards")

    print("\n══ Summary ══")
    for deck, cards in full_manifest.items():
        print(f"  {deck}: {len(cards)} cards")
    print(f"\nManifest → {MAN}")
    print("Done.")
