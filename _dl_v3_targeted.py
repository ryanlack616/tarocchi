"""
_dl_v3_targeted.py — Targeted downloader using REAL Wikimedia categories
discovered by _probe_commons.py. Public-domain only.

Each deck gets specific categories + file-search queries that we know exist.
BnF "btv1b" categories are full-deck high-res scans (numbered 'N of M').

Idempotent: skips files already on disk and entries already in manifest.
"""
import json, re, time, urllib.request, urllib.parse, urllib.error
from pathlib import Path

OUT   = Path("data/images")
MAN   = OUT / "manifest.json"
W     = 400  # slightly bigger than v2's 300px — better quality for atlas
DELAY = 0.4

API = "https://commons.wikimedia.org/w/api.php"
UA  = "tarocchi-dl/4.0 (https://tarocchi.help research; ryan@tarocchi.help)"
IMG_EXTS = {".jpg", ".jpeg", ".png"}

# ─── Trump name regex (FR / IT / EN, accent-folded) ──────────────────────────

ROMAN = {
    "XXI":21,"XX":20,"XVIIII":19,"XIX":19,"XVIII":18,"XVII":17,"XVI":16,"XV":15,
    "XIIII":14,"XIV":14,"XIII":13,"XII":12,"XI":11,"X":10,"VIIII":9,"IX":9,
    "VIII":8,"VII":7,"VI":6,"V":5,"IIII":4,"IV":4,"III":3,"II":2,"I":1,
}
TRUMP_RE = [
    (r"\b(le\s*mat|fool|matto|der\s*narr|le\s*fou|la\s*folie)\b", "major-00"),
    (r"\b(bagatto|bagatella|bateleur|magician|juggler|mago|magicien)\b", "major-01"),
    (r"\b(papess|popess|papesse|priestess|papessa|junon|juno)\b", "major-02"),
    (r"\b(empress|imperatrice|empereuratrice)\b", "major-03"),
    (r"\b(emperor|empereur|imperatore|jupiter)\b", "major-04"),
    (r"\b(pope\b|le\s*pape|hierophant|hierofant|papa\b|grand\s*pretre|grand[-_ ]?pr[eê]tre)\b", "major-05"),
    (r"\b(lovers|amoureux|amanti|innamorati|le\s*lover|mariage)\b", "major-06"),
    (r"\b(chariot|char\b|carro|le\s*chariot)\b", "major-07"),
    (r"\b(justice|giustizia|la\s*justice)\b", "major-08"),
    (r"\b(hermit|ermite|eremita|hermite|capucin)\b", "major-09"),
    (r"(roue\s*de\s*fortune|wheel\s*of\s*fortune|ruota.*fortuna|la\s*roue|fortuna)", "major-10"),
    (r"\b(strength|force\b|la\s*forza|fortitude|fortezza)\b", "major-11"),
    (r"(hanged\s*man|le\s*pendu|pendu\b|appeso|impiccato|repos)", "major-12"),
    (r"\b(death|la\s*mort|mort\b|morte|la\s*morte)\b", "major-13"),
    (r"\b(temperance|temperanza|astres)\b", "major-14"),
    (r"\b(devil|le\s*diable|diavolo|diable)\b", "major-15"),
    (r"(tower|maison\s*dieu|la\s*tour|la\s*torre|casa.*dio|foudre)", "major-16"),
    (r"\b(star\b|etoile|stella|astres)\b", "major-17"),
    (r"\b(moon|lune|luna|la\s*lune)\b", "major-18"),
    (r"\b(sun\b|soleil|sole|le\s*soleil)\b", "major-19"),
    (r"\b(judgement|judgment|jugement|giudizio|angel)\b", "major-20"),
    (r"\b(world|monde|mondo|le\s*monde|il\s*mondo|universe)\b", "major-21"),
]

def _fold(s):
    s = s.lower()
    repl = {"é":"e","è":"e","ê":"e","ï":"i","î":"i","ô":"o","ç":"c","à":"a","â":"a","ù":"u","û":"u"}
    for k,v in repl.items():
        s = s.replace(k,v)
    return s

def parse_card_id(fn):
    """Map a Commons filename to major-NN if recognizable, else None."""
    stem = Path(fn).stem
    folded = _fold(stem)
    # Leading 2-digit: "00 La Folie..."
    m = re.match(r"^\s*(\d{1,2})\b", stem)
    if m:
        n = int(m.group(1))
        if 0 <= n <= 21:
            return f"major-{n:02d}"
    # "Trump 02", "trump 21", "atout 06", "arcanum-15"
    m = re.search(r"(?:trump|atout|arcanum|arcana|arcane|atou)[- _]*(\d{1,2})", stem, re.I)
    if m:
        n = int(m.group(1))
        if 0 <= n <= 21:
            return f"major-{n:02d}"
    # Roman numerals as standalone token
    up = stem.upper()
    for rom, n in sorted(ROMAN.items(), key=lambda x: -len(x[0])):
        if re.search(r"(?:^|[^A-Z])" + rom + r"(?:[^A-Z]|$)", up):
            if 0 <= n <= 21:
                return f"major-{n:02d}"
    # Trump name regex
    for pat, cid in TRUMP_RE:
        if re.search(pat, folded):
            return cid
    return None

# ─── HTTP / API ──────────────────────────────────────────────────────────────

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 2:
                wait = 30 * (attempt + 1)
                print(f"      [429] wait {wait}s")
                time.sleep(wait)
                continue
            raise
        except Exception as e:
            if attempt < 2:
                time.sleep(5)
                continue
            raise

def api_get(params):
    url = API + "?" + urllib.parse.urlencode({"format":"json", **params})
    return json.loads(fetch(url, 25))

def thumb_url(filename, width=W):
    try:
        d = api_get({"action":"query","titles":f"File:{filename}",
                     "prop":"imageinfo","iiprop":"url","iiurlwidth":str(width)})
        for p in d["query"]["pages"].values():
            ii = p.get("imageinfo", [])
            if ii:
                return ii[0].get("thumburl") or ii[0].get("url")
    except Exception as e:
        print(f"      thumb err: {e}")
    return None

def cat_files(cat, limit=200):
    files, cont = [], {}
    while len(files) < limit:
        try:
            d = api_get({"action":"query","list":"categorymembers",
                         "cmtitle":f"Category:{cat}","cmtype":"file","cmlimit":"100", **cont})
        except Exception as e:
            print(f"      cat err {cat}: {e}")
            break
        files += [m["title"][5:] for m in d["query"]["categorymembers"]]
        time.sleep(DELAY)
        if "continue" not in d:
            break
        cont = d["continue"]
    return files[:limit]

def search_files(q, limit=100):
    files, cont = [], {}
    while len(files) < limit:
        try:
            d = api_get({"action":"query","list":"search","srsearch":q,
                         "srnamespace":"6","srlimit":"50", **cont})
        except Exception as e:
            print(f"      search err {q}: {e}")
            break
        batch = d["query"]["search"]
        files += [r["title"][5:] for r in batch]
        if "continue" not in d or not batch:
            break
        cont = d["continue"]
        time.sleep(DELAY)
    return files[:limit]

def dl_one(fn, card_id, deck_dir, deck_id):
    src_ext = Path(fn).suffix.lower()
    ext = ".jpg" if src_ext in {".tif",".tiff",".webp"} else (src_ext if src_ext in IMG_EXTS else ".jpg")
    dest = deck_dir / f"{card_id}{ext}"
    if dest.exists():
        return card_id, f"data/images/{deck_id}/{dest.name}"
    url = thumb_url(fn)
    if not url:
        time.sleep(DELAY)
        return None
    try:
        dest.write_bytes(fetch(url, 60))
    except Exception as e:
        print(f"      DL err: {e}")
        time.sleep(DELAY)
        return None
    time.sleep(DELAY)
    return card_id, f"data/images/{deck_id}/{dest.name}"

# ─── Per-deck targets (REAL category names, verified by probe) ───────────────

DECKS = [
    ("sola-busca", [
        ("cat", "Sola-Busca tarot deck"),
        ("cat", "Sola-Busca tarot cards in the Albertina"),
    ], 100),

    ("visconti-di-modrone", [
        ("cat", "Cary-Yale Visconti Tarot"),
        ("search", "Cary-Yale Tarot deck"),
    ], 100),

    ("charles-vi", [
        ("cat", 'Le tarot dit de Charles VI'),
        ("search", "tarot charles6"),
    ], 100),

    ("tarot-de-marseille-noblet", [
        ("cat", 'Jeu de tarot à enseignes italiennes dit "tarot Noblet" - jeu de cartes, estampe - btv1b105109641'),
    ], 100),

    ("jacques-vieville-c1650", [
        ("cat", "Viéville tarot"),
        ("cat", 'Jeu de tarot à enseignes italiennes dit "tarot Viéville" - jeu de cartes, estampe - btv1b10510963k'),
    ], 100),

    ("tarocchino-mitelli-1664", [
        # Files only show via search — the long BnF cat name has special chars
        ("search", "Mitelli tarrochini btv1b10510959v"),
        ("search", "Giuseppe Maria Mitelli tarocchino"),
    ], 100),

    ("minchiate-fiorentine", [
        ("cat", "Minchiate"),
        ("cat", "Earlier Minchiate"),
        ("cat", "Zodiac (Minchiate)"),
        ("cat", "Elements (Minchiate)"),
        ("cat", "Prudence (Minchiate)"),
    ], 100),

    ("tarot-de-besancon", [
        ("cat", "Tarot de Besançon"),
        ("cat", "Tarot de Besançon - Renault"),
    ], 100),

    ("tarot-de-marseille-dodal", [
        ("cat", "Tarot de Marseille - Jean Dodal"),
    ], 100),

    ("1jj-swiss-c1831", [
        ("cat", "Tarot 1JJ"),
        ("search", "1JJ Tarot"),
        ("search", "Swiss Tarot 1JJ Troccas"),
    ], 100),

    ("etteilla-grand-etteilla-1789", [
        ("cat", "Etteilla I tarot deck"),
    ], 100),

    ("madenie-1709", [
        ("search", "Madenié 1709"),
        ("search", "Pierre Madenie tarot"),
        ("search", "Madenie Dijon tarot"),
    ], 100),

    ("papus-tarot-1889", [
        ("cat", "Papus Tarot 1909"),
        ("cat", "Papus Tarot, translate by Troyanovsky, 1912"),
        ("search", "Papus Atout"),
        ("search", "Papus Tarot Arcana"),
    ], 100),

    ("rosenwald-sheet-c1500", [
        ("search", "Italian 15th Century Playing Cards NGA"),
        ("search", "Rosenwald playing cards Italian"),
    ], 60),

    ("cary-sheet-c1500", [
        ("search", "Tarot-cary-collection"),
        ("search", "Cary collection Italian sheet"),
    ], 30),
]

# ─── Junk filter (Commons-wide false positives) ──────────────────────────────

JUNK = re.compile(
    r"(commons-logo|wikimedia|svg-logo|"
    r"\.djvu$|\.pdf$|\.ogv$|\.webm$|\.svg$|\.tif$|\.tiff$|\.gif$|"
    r"villa\s*sola|villa\s*l|della\s*bella|"  # NGA non-Rosenwald, Villa Sola Busca-the-place, etc.
    r"di\s*modrone\s*(family|\d)|mausoleo|marcello|uberto|guido|leonardo|giuseppe\s*visconti|"
    r"violante|"  # the Visconti family member pages
    r"self.?portrait|catalogue|introduction|"  # non-card metadata
    r"loix\s*et\s*constitutions|moreau\s*de\s*saint|"  # vieville junk
    r"momus\s*tarot|"  # not Minchiate
    r"sanctum.regnum|legrandinterprte|petit-albert|nouveau\s*dictionnaire"  # Papus PDF junk
    r")", re.I
)

def is_card_image(fn):
    if Path(fn).suffix.lower() not in IMG_EXTS:
        return False
    if JUNK.search(fn):
        return False
    return True

# ─── Driver ──────────────────────────────────────────────────────────────────

def do_deck(deck_id, sources, cap, full_manifest):
    deck_dir = OUT / deck_id
    deck_dir.mkdir(parents=True, exist_ok=True)
    manifest = dict(full_manifest.get(deck_id, {}))

    raw = []
    for kind, q in sources:
        print(f"  {kind.upper()}: {q[:70]}")
        if kind == "cat":
            got = cat_files(q, limit=cap*2)
        else:
            got = search_files(q, limit=cap*2)
        print(f"    +{len(got)} raw files")
        raw += got

    files = [f for f in dict.fromkeys(raw) if is_card_image(f)]
    print(f"  TOTAL valid images: {len(files)}")

    counter = 1
    for fn in files:
        if len(manifest) >= cap:
            break
        cid = parse_card_id(fn)
        if cid and cid in manifest:
            continue
        if not cid:
            while f"card-{counter:03d}" in manifest:
                counter += 1
            cid = f"card-{counter:03d}"
            counter += 1
        print(f"    {cid:13s} ← {fn[:70]}")
        r = dl_one(fn, cid, deck_dir, deck_id)
        if r:
            manifest[r[0]] = r[1]

    full_manifest[deck_id] = manifest
    return manifest

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    full = json.loads(MAN.read_text(encoding="utf-8")) if MAN.exists() else {}

    summary = {}
    for deck_id, sources, cap in DECKS:
        print(f"\n══ {deck_id} ══")
        before = len(full.get(deck_id, {}))
        try:
            m = do_deck(deck_id, sources, cap, full)
        except Exception as e:
            print(f"  DECK ERR: {e}")
            m = full.get(deck_id, {})
        after = len(m)
        summary[deck_id] = (before, after)
        MAN.write_text(json.dumps(full, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  {deck_id}: {before} → {after}  (+{after-before})")

    print("\n" + "="*60 + "\nSUMMARY\n" + "="*60)
    for d,(b,a) in summary.items():
        print(f"  {d:35s} {b:3d} → {a:3d}  (+{a-b})")
    print(f"\nManifest: {MAN}")

if __name__ == "__main__":
    main()
