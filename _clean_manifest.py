"""Clean false-positive downloads from manifest + disk."""
import json, re
from pathlib import Path

MAN = Path("data/images/manifest.json")
m = json.loads(MAN.read_text(encoding="utf-8"))

# Known false positives (filename substrings → delete)
BAD_PATTERNS = [
    r"Enumeration District",          # census sheets in cary
    r"Waite-Smith Tarot Deck, Yale",  # RWS dupes tagged to cary
    r"A Rocky Stream",
    r"Vision of Hell",
    r"Die Hoffnung.*Cary-Yale",       # actually ok-ish but belongs to Cary-Yale deck not Cary Sheet
]
BAD_RE = re.compile("|".join(BAD_PATTERNS), re.I)

# We don't store original filenames post-download, but we can inspect which
# manifest paths exist and selectively prune cary-sheet-c1500 back to hits
# that match the actual sheet (NGA 4131x, cary-collection).
# Strategy: in cary-sheet-c1500, keep ONLY entries whose file on disk came
# from search hit 1 (card-001 only). Drop card-002..card-021.

removed = 0
if "cary-sheet-c1500" in m:
    cary = m["cary-sheet-c1500"]
    # Keep only card-001 (the real Cary sheet)
    keep = {}
    if "card-001" in cary:
        keep["card-001"] = cary["card-001"]
    for cid, path in cary.items():
        if cid not in keep:
            f = Path(path)
            if f.exists():
                f.unlink()
                removed += 1
    m["cary-sheet-c1500"] = keep

# Also clean rosenwald-sheet-c1500: keep only NGA 4131x (3 are all legit)
# (already clean)

# Clean visconti-di-modrone: "Die Hoffnung Cary-Yale" belongs here actually, but
# prior runs might have family-member portraits. Count only; don't auto-prune
# since Cary-Yale Tarot deck cat is valid.

MAN.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Removed {removed} false-positive files.")
print(f"cary-sheet-c1500 now has {len(m.get('cary-sheet-c1500', {}))} entries.")
