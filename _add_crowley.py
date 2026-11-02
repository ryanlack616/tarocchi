"""
_add_crowley.py — Deep Crowley/Thoth addition.

Adds:
  1. `book-of-thoth-1944` deck entry to historical_decks.json
  2. 3 new genealogy edges (Lévi→Thoth, Thoth→BookOfThoth, GD→BookOfThoth)
  3. 6 thoth-tarot card witnesses in card_witnesses.json:
       major-08 (Strength → Lust, restored to position XI)
       major-11 (Justice → Adjustment, restored to position VIII)
       major-20 (Judgement → The Aeon, complete theological replacement)
       major-21 (The World → The Universe, renamed)
       major-00 (The Fool, radically reimagined Thelemic iconography)
       wands-14 (King of Wands → Knight of Wands — court hierarchy restructuring)

Run from tarocchi root: python -X utf8 _add_crowley.py
"""
import json, sys, os

DECKS_PATH = "data/historical_decks.json"
WITNESSES_PATH = "data/card_witnesses.json"


# ──────────────────────────────────────────────────────────────────────────────
# 1. BOOK OF THOTH — new deck entry
# ──────────────────────────────────────────────────────────────────────────────

BOOK_OF_THOTH = {
    "id": "book-of-thoth-1944",
    "name": "The Book of Thoth",
    "name_local": "The Book of Thoth: A Short Essay on the Tarot of the Egyptians",
    "region": "London",
    "culture": "Thelema / Crowleyan occultism",
    "date_earliest": 1944,
    "date_latest": 1944,
    "date_display": "1944 (O.T.O. private edition; reprinted 1969)",
    "date_basis": (
        "Written 1938–1944 in parallel with Harris's paintings. First published as a "
        "subscription edition of 200 copies by O.T.O. (Ordo Templi Orientis), 1944. "
        "Crowley died 1947. The Weiser Books reprint appeared in 1969 simultaneously "
        "with the first public edition of the Thoth Tarot deck."
    ),
    "date_confidence": "high",
    "survival_status": "extant",
    "cards_known": 0,
    "cards_original": None,
    "missing_cards": [],
    "missing_cards_unidentified_count": None,
    "missing_cards_notes": (
        "No physical deck — a written treatise. The companion deck (thoth-tarot) "
        "was painted by Lady Frieda Harris 1938–1943 under Crowley's direction."
    ),
    "structure": {
        "total_cards": None,
        "suits": [],
        "ranks_per_suit": None,
        "court_cards": [],
        "trump_cards": 0,
        "notes": (
            "Not a deck. A written treatise of approximately 300 pages organised around "
            "the 78 cards plus introductory essays on Kabbalah, Thelema, astrology, "
            "numerology, and alchemy. Unique among tarot texts for its systematic "
            "I Ching correspondences assigned to each card — a synthesis never attempted "
            "by any prior tarot author. Structured as: Part One (general theory), "
            "Part Two (the trumps, one chapter per card), Part Three (the court cards), "
            "Part Four (the small cards), appendices on Gematria and the Tree of Life."
        )
    },
    "material": ["paper", "letterpress_print"],
    "technique": ["typography"],
    "language_on_cards": ["English"],
    "holdings": [
        {
            "institution": "British Library",
            "city": "London",
            "country": "UK",
            "cards_held": None,
            "accession": None,
            "digitized": False,
            "digitization_url": None
        },
        {
            "institution": "Warburg Institute Library",
            "city": "London",
            "country": "UK",
            "cards_held": None,
            "accession": None,
            "digitized": False,
            "digitization_url": None
        }
    ],
    "attributions": [
        {
            "role": "author",
            "name": "Aleister Crowley",
            "confidence": "high",
            "notes": (
                "Crowley's most systematic tarot exposition; his final major work, "
                "written in his late 60s and early 70s during World War II. "
                "Integrates the complete Thelemic system he had developed across "
                "four decades (Liber 777, Equinox essays, Golden Dawn grade work)."
            )
        },
        {
            "role": "publisher",
            "name": "O.T.O. (Ordo Templi Orientis)",
            "confidence": "high",
            "notes": (
                "Limited subscription edition of 200 copies, 1944. "
                "The subscription price was high and access restricted to initiates. "
                "The Weiser reprint (1969) made it publicly accessible."
            )
        }
    ],
    "patron": None,
    "commissioned_for": "Thelemic practitioners and O.T.O. initiates",
    "primary_purpose": "esoteric_theory",
    "later_uses": ["divination_guide", "initiatory_text", "academic_reference"],
    "purpose": ["esoteric_theory", "divination"],
    "transmission_path": (
        "Weiser Books reprint (1969) appeared simultaneously with the first public "
        "edition of the Thoth Tarot deck, establishing them as an inseparable pair. "
        "Now the authoritative reference for all Thoth-tradition tarot study. "
        "Cited in every serious Thoth commentary including DuQuette (2003) and "
        "Snuffin (2007). The text is the only source for Crowley's own interpretive "
        "framework; Harris's paintings cannot be fully decoded without it."
    ),
    "iconography_notes": (
        "Text-only in original edition. Crowley describes each card's visual symbolism "
        "in detail, cross-referenced with Hebrew letters, astrological attributions, "
        "I Ching hexagrams, and Gematria values. Later Weiser editions occasionally "
        "include black-and-white card reproductions. The text reveals that several "
        "visual choices in the paintings encode specific Thelemic doctrines that are "
        "invisible to viewers unfamiliar with the system — the Lust card's golden cup, "
        "the Aeon's six-pointed star arrangement, the Fool's emptiness."
    ),
    "significance": (
        "The most exhaustive single-author tarot commentary ever written, and the "
        "second axis of modern tarot theory after Waite's Pictorial Key to the Tarot "
        "(1910). Where Waite was allusive and devotional, Crowley is technical and "
        "initiatory. Where Lévi sketched a Kabbalistic skeleton, Crowley built full "
        "architecture — integrating Western esotericism, Eastern (I Ching) systems, "
        "and Thelema into a unified divinatory grammar. The Book of Thoth establishes "
        "that the tarot is not a European folk tradition ornamented with occultism, "
        "but a formal language with grammar rules, and that reading the cards is an "
        "act of applied philosophy rather than intuitive pattern-matching."
    ),
    "sources": [
        "Crowley, Aleister. The Book of Thoth. O.T.O., 1944; Weiser Books reprint, 1969.",
        "DuQuette, Lon Milo. Understanding Aleister Crowley's Thoth Tarot. Weiser, 2003.",
        "Snuffin, Michael. The Thoth Companion. Llewellyn, 2007.",
        "Kaczynski, Richard. Perdurabo: The Life of Aleister Crowley. North Atlantic Books, 2010."
    ],
    "tags": [
        "thelema",
        "golden_dawn",
        "kabbalah",
        "esoteric_text",
        "crowley",
        "oto",
        "english",
        "companion_text",
        "i_ching",
        "gematria"
    ]
}


# ──────────────────────────────────────────────────────────────────────────────
# 2. NEW GENEALOGY EDGES
# ──────────────────────────────────────────────────────────────────────────────

NEW_GENEALOGY_EDGES = [
    {
        "from": "eliphas-levi-1855",
        "to": "thoth-tarot",
        "relation": "direct_intellectual_source",
        "notes": (
            "Crowley absorbed Lévi's Dogme et Rituel de la Haute Magie thoroughly. "
            "The Kabbalistic-astrological-Hebrew letter attribution framework "
            "that underlies the Thoth deck derives ultimately from Lévi's schema "
            "(transmitted through the Golden Dawn). Crowley corrects, extends, and "
            "disputes Lévi throughout The Book of Thoth — an engagement that reveals "
            "how directly he was reading him."
        )
    },
    {
        "from": "thoth-tarot",
        "to": "book-of-thoth-1944",
        "relation": "companion_text",
        "notes": (
            "Harris's paintings and Crowley's text were produced simultaneously "
            "(1938–1943/1944) as a unified system. The text is the interpretive "
            "key to the deck; neither is complete without the other. Published "
            "together by Weiser in 1969. Crowley directed Harris's painting choices "
            "based on the same doctrinal content that appears in the book."
        )
    },
    {
        "from": "golden-dawn-corpus",
        "to": "book-of-thoth-1944",
        "relation": "esoteric_source_material",
        "notes": (
            "The Hebrew letter attributions, astrological correspondences, and "
            "Kabbalistic Tree of Life structure in The Book of Thoth derive from "
            "the unpublished Golden Dawn manuscripts Crowley was initiated into. "
            "Crowley extends the GD system with Thelemic innovations "
            "(the Aeon of Horus doctrine, Liber AL correspondences) but the "
            "structural skeleton is GD material."
        )
    }
]


# ──────────────────────────────────────────────────────────────────────────────
# 3. THOTH CARD WITNESSES
# ──────────────────────────────────────────────────────────────────────────────
# Added as a named block in card_witnesses.json witnesses array.
# Schema extended with `thoth_name` and `thoth_position` fields for
# the renamed/renumbered cards — these fields are ignored by existing parsers.

THOTH_WITNESSES = [
    {
        "_comment": "═══ Thoth Tarot — renamed, renumbered, and reimagined cards ═══"
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-08",
        "present": True,
        "thoth_name": "Lust",
        "thoth_position": 11,
        "rws_name": "Strength",
        "rws_position": 8,
        "borrowing_source": "golden-dawn-corpus",
        "confidence": "confirmed",
        "notes": (
            "Crowley restored the Marseille ordering (Strength = XI, Justice = VIII) "
            "that Waite had swapped. Beyond renaming, the card is fully reimagined: "
            "the Rider-Waite image of a gentle woman closing a lion's mouth is "
            "replaced entirely by Babalon — the Scarlet Woman, Thelema's goddess "
            "of sacred sexuality — riding the ten-headed Beast of the Apocalypse "
            "(Revelation 17). She holds aloft a golden cup overflowing with blood "
            "and fire, symbolising the dissolution of the ego into divine ecstasy. "
            "The lion becomes a cosmic beast, not a tame animal. Crowley's 'Lust' "
            "is not brute force controlled by piety; it is the creative, generative "
            "energy of the universe — Shakti, Babalon, the Great Mother — as "
            "initiatory power. The projective geometry in Harris's painting makes "
            "the Beast's heads appear to spiral outward from a central vortex."
        )
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-11",
        "present": True,
        "thoth_name": "Adjustment",
        "thoth_position": 8,
        "rws_name": "Justice",
        "rws_position": 11,
        "borrowing_source": "golden-dawn-corpus",
        "confidence": "confirmed",
        "notes": (
            "Crowley restored Justice to Marseille position VIII, correcting Waite's swap. "
            "Beyond the positional correction, the card is reconceived. The robed "
            "seated figure with scales and sword of RWS becomes a perfectly balanced "
            "abstract figure — the goddess Maat — standing on the point of a sword, "
            "extending in all directions simultaneously. The scales are not instruments "
            "of legal judgment but extensions of the figure's own body: perfect "
            "equilibrium is the figure's nature, not a tool it holds. The diamond "
            "frame of the card and Harris's projective geometry make the figure appear "
            "to hover in a state of pure mathematical balance. 'Adjustment' is Crowley's "
            "correction of 'Justice': the universe does not judge; it adjusts. "
            "The card encodes the principle of Karma without the moral overlay."
        )
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-20",
        "present": True,
        "thoth_name": "The Aeon",
        "thoth_position": 20,
        "rws_name": "Judgement",
        "rws_position": 20,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "The most radical departure in the Thoth system — not a renamed card but "
            "a theological replacement. Rider-Waite Judgement (XX) depicts Angel Gabriel "
            "blowing a trumpet over rising dead in Christian resurrection imagery. "
            "Crowley replaces this entirely with Thelemic cosmology. The Aeon shows "
            "the divine triad of the current cosmic age (the Aeon of Horus): "
            "Nuit (the night sky, the infinite, arching over the scene as a starry "
            "body), Hadit (the winged solar disc at the card's centre — the point "
            "of consciousness within infinity), and Ra-Hoor-Khuit (the hawk-headed "
            "child god in the lower portion — the active, martial aspect of Horus). "
            "The card announces that the Aeon of Osiris (characterised by the dying "
            "and resurrecting god, sacrifice, and the Last Judgement) has ended and "
            "the Aeon of Horus has begun — Crowley's central Thelemic doctrine, "
            "received in the Cairo Working of 1904 (Liber AL vel Legis). "
            "Harris's painting uses the six-pointed star of Da'ath (the invisible "
            "sephira of the Abyss) in the lower register. The Christian angel is "
            "absent. Judgement is absent. What remains is cosmological time — "
            "the turning of an aeon."
        )
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-21",
        "present": True,
        "thoth_name": "The Universe",
        "thoth_position": 21,
        "rws_name": "The World",
        "rws_position": 21,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Renamed from 'The World' to 'The Universe' to signal a cosmological "
            "rather than terrestrial completion. The RWS image — a dancing figure "
            "within a laurel wreath, surrounded by the four Living Creatures — is "
            "retained in structural outline but radically transformed. Harris's figure "
            "is a naked dancing woman within an oval of light, but the 'wreath' becomes "
            "a serpent biting its own tail (ouroboros), enclosing the figure within "
            "cyclical time. The four Living Creatures of Ezekiel/Revelation appear at "
            "the corners as in RWS, but more abstract and geometrically rendered. "
            "At the card's centre is the Great Wheel — a complex astrological diagram "
            "encoding Saturn (the planet of the card in GD attributions). "
            "The figure carries a crook and flail (Osirian symbols), encoding "
            "the paradox of the final initiation: to complete the Great Work "
            "(cross the Abyss, unite with the All) is simultaneously to become "
            "the universe itself and to recognise that individuality was always illusion."
        )
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-00",
        "present": True,
        "thoth_name": "The Fool",
        "thoth_position": 0,
        "rws_name": "The Fool",
        "rws_position": 0,
        "borrowing_source": "golden-dawn-corpus",
        "confidence": "confirmed",
        "notes": (
            "The name is unchanged but the card is the most elaborate Fool in the "
            "tarot tradition. Where RWS shows a carefree youth about to step off a "
            "cliff with a small dog at his heels, the Thoth Fool is saturated with "
            "Thelemic symbolism. The central figure is effectively invisible — an "
            "empty, iridescent body that is 'all colours and none.' He is accompanied "
            "by: a crocodile (ancient wisdom, Set, the devouring unconscious) leaping "
            "to bite his leg; a tiger lily (the generative force, Netzach); a dove "
            "descending (the Holy Spirit / Ruach Elohim; the descent of the divine "
            "into matter); clusters of grapes (Dionysus, ecstatic dissolution); "
            "a caduceus staff (Hermes / Mercury — The Fool is attributed to Aleph, "
            "Air, but Mercury is his companion). The multi-coloured quartered circle "
            "behind him is the Rose Cross mandala. The figure holds a bag on a wand "
            "as in traditional decks, but the bag is a sun. Crowley wrote that The Fool "
            "is the most important card in the deck — the precondition for all the rest. "
            "He is 0 = 2: the unmanifest potential that contains all opposites. "
            "Harris's projective geometry makes the figure appear simultaneously "
            "to fall forward and to stand still — Aleph, the ox, the breath."
        )
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "wands-14",
        "present": True,
        "thoth_name": "Knight of Wands",
        "thoth_position": 14,
        "rws_name": "King of Wands",
        "rws_position": 14,
        "borrowing_source": "golden-dawn-corpus",
        "confidence": "confirmed",
        "notes": (
            "The court card hierarchy is restructured throughout the Thoth deck. "
            "What RWS calls 'King' (the seated sovereign) Crowley calls 'Knight' "
            "(the mounted, active warrior). What RWS calls 'Knight' (the mounted "
            "figure) Crowley calls 'Prince' (a figure in a chariot). What RWS calls "
            "'Page' (the standing youth) Crowley calls 'Princess' (who stands on "
            "earth, the materialising force). The Queen remains Queen. "
            "This restructuring derives from the Golden Dawn's elemental grade system: "
            "Knight = Fire of the element (active, swift), Queen = Water of the element "
            "(receptive, sustaining), Prince = Air of the element (mental, mediated), "
            "Princess = Earth of the element (manifest, embodied). "
            "The King of Wands (wands-14) becomes the Knight of Wands — still the "
            "fiery, dynamic principle of Fire, but explicitly warrior-mounted rather "
            "than enthroned. Harris depicts him on a leaping black horse, holding a "
            "flaming club, surrounded by lions. The renaming is not cosmetic: "
            "it reframes the court hierarchy from feudal (King/Queen/Knight/Page) "
            "to elemental (Fire/Water/Air/Earth-of-the-element)."
        )
    }
]


# ──────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved {path}")


def add_to_decks():
    d = load_json(DECKS_PATH)

    # Guard: skip if already added
    existing_ids = {dk["id"] for dk in d["decks"]}
    if "book-of-thoth-1944" in existing_ids:
        print("  book-of-thoth-1944 already present — skipping deck add")
    else:
        # Insert after thoth-tarot (index 19)
        thoth_idx = next(i for i, dk in enumerate(d["decks"]) if dk["id"] == "thoth-tarot")
        d["decks"].insert(thoth_idx + 1, BOOK_OF_THOTH)
        print(f"  Inserted book-of-thoth-1944 at index {thoth_idx + 1}")

    # Guard genealogy: skip edges that already exist
    existing_edges = {(e.get("from",""), e.get("to","")) for e in d["genealogy"]}
    added = 0
    for edge in NEW_GENEALOGY_EDGES:
        key = (edge["from"], edge["to"])
        if key in existing_edges:
            print(f"  Edge {key} already present — skipping")
        else:
            d["genealogy"].append(edge)
            existing_edges.add(key)
            added += 1
    print(f"  Added {added} genealogy edge(s)")

    save_json(DECKS_PATH, d)
    return len(d["decks"]), len(d["genealogy"])


def add_to_witnesses():
    cw = load_json(WITNESSES_PATH)

    # Build set of (deck_id, card_id) already present
    existing_keys = {
        (w.get("deck_id",""), w.get("card_id",""))
        for w in cw["witnesses"] if "deck_id" in w and "card_id" in w
    }

    added = 0
    comment_inserted = False
    new_entries = []
    for entry in THOTH_WITNESSES:
        if "_comment" in entry:
            # Only insert comment block if we're adding at least one real entry
            # (handled after loop)
            continue
        key = (entry.get("deck_id",""), entry.get("card_id",""))
        if key in existing_keys:
            print(f"  Witness {key} already present — skipping")
        else:
            if not comment_inserted:
                new_entries.append({"_comment": "═══ Thoth Tarot — renamed, renumbered, and reimagined cards ═══"})
                comment_inserted = True
            new_entries.append(entry)
            added += 1

    if new_entries:
        cw["witnesses"].extend(new_entries)
        print(f"  Added {added} new witness entries")
        save_json(WITNESSES_PATH, cw)
    else:
        print("  All witnesses already present — no changes")

    return len(cw["witnesses"])


if __name__ == "__main__":
    print("=== _add_crowley.py ===")
    print()
    print("historical_decks.json:")
    deck_count, edge_count = add_to_decks()
    print(f"  Total decks: {deck_count}  |  Total genealogy edges: {edge_count}")
    print()
    print("card_witnesses.json:")
    witness_count = add_to_witnesses()
    print(f"  Total witnesses array entries: {witness_count}")
    print()
    print("Done. Run _build_decks_db.py to rebuild decks.db")
