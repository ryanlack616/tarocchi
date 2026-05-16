"""
_add_deep.py — Deep structural additions to the Crowley/Thoth/RWS corpus.

Adds:
  1. `pictorial-key-1910`   — Waite's companion text (parallel to book-of-thoth-1944)
  2. `liber-al-legis-1909`  — The Book of the Law: Thelemic root text that directly
                              dictated the Aeon card design and the Tzaddi swap
  3. 5 new genealogy edges connecting the above
  4. 3 new thoth-tarot card witnesses:
       major-01 (The Magus — renamed from The Magician)
       major-14 (Art — renamed from Temperance)
       major-17 (The Star — Tzaddi swap complement to major-04/Emperor)

Run from tarocchi root: python -X utf8 _add_deep.py
"""
import json

DECKS_PATH     = "data/historical_decks.json"
WITNESSES_PATH = "data/card_witnesses.json"


# ─────────────────────────────────────────────────────────────────────────────
# 1. NEW DECKS
# ─────────────────────────────────────────────────────────────────────────────

PICTORIAL_KEY = {
    "id": "pictorial-key-1910",
    "name": "The Pictorial Key to the Tarot",
    "name_local": None,
    "region": "London / New York",
    "culture": "Edwardian British occultism",
    "date_earliest": 1910,
    "date_latest": 1910,
    "date_display": "1910 (first edition, Rider & Co., London)",
    "date_basis": (
        "Published by William Rider and Son, London, in December 1910 — the same "
        "month as the Rider-Waite-Smith deck itself (December 1909 for the deck; "
        "the Key followed within a year). Waite wrote it as the authorised "
        "interpretive companion. The US edition appeared via Dodd, Mead & Co. "
        "simultaneously. It has remained in continuous print, most commonly via "
        "the University Books (1959) and later Weiser Books reprints."
    ),
    "date_confidence": "high",
    "survival_status": "extant",
    "cards_known": 0,
    "cards_original": None,
    "missing_cards": [],
    "missing_cards_unidentified_count": None,
    "missing_cards_notes": (
        "Text document, not a physical deck. The companion reading guide to "
        "the Rider-Waite-Smith Tarot."
    ),
    "structure": {
        "total_cards": None,
        "suits": [],
        "ranks_per_suit": None,
        "court_cards": [],
        "trump_cards": 0,
        "notes": (
            "A prose treatise of approximately 340 pages organised around the 78 cards. "
            "Part I: 'The Veil and Its Symbols' — the Egyptian pseudo-history of tarot "
            "origins that Waite accepted from Court de Gébelin while privately "
            "acknowledging its uncertainty. Part II: 'The Doctrine Behind the Veil' — "
            "the esoteric symbolism of the Major Arcana. Part III: 'The Outer Method of "
            "the Oracles' — divination spreads and reading instructions for all 78 cards. "
            "Part IV: 'The Secret Tradition in Goëtia' — connecting tarot to Solomonic magic. "
            "The Major Arcana interpretations are famously evasive: Waite was bound by "
            "his Golden Dawn oath not to reveal the inner symbolic meanings, so the Key "
            "gestures toward the symbolism while deliberately not explaining it. "
            "This deliberate opacity is part of what drove Crowley to write The Book of "
            "Thoth as a counter-text — he had no such scruples about secrecy."
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
            "institution": "Bodleian Library",
            "city": "Oxford",
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
            "name": "Arthur Edward Waite",
            "confidence": "high",
            "notes": (
                "Waite's primary esoteric text on tarot; the authorised companion to "
                "the deck he designed with Pamela Colman Smith. Waite was a prolific "
                "occultist, co-founder of the Fellowship of the Rosy Cross, and a "
                "long-time member and eventual schismatic from the Golden Dawn. "
                "His approach was always Christian-mystical, not Thelemic or atheist, "
                "which accounts for the Key's pietistic tone and the deck's distinctive "
                "combination of Golden Dawn symbolism with accessible Christian imagery."
            )
        },
        {
            "role": "publisher",
            "name": "William Rider and Son",
            "confidence": "high",
            "notes": (
                "Rider & Co. gave their name to the deck (Rider-Waite) in this period. "
                "They were a major occult publisher in Edwardian London."
            )
        }
    ],
    "patron": None,
    "commissioned_for": "General occult reading public; companion to the RWS deck",
    "primary_purpose": "esoteric_theory",
    "later_uses": ["divination_guide", "initiatory_text", "academic_reference"],
    "purpose": ["esoteric_theory", "divination"],
    "transmission_path": (
        "Continuously in print since 1910. The University Books reprint (1959) and "
        "subsequent Weiser Books edition made it the standard reference for two "
        "generations of English-language tarot readers. It is the most-cited single "
        "tarot text in English and the interpretive foundation for virtually all "
        "RWS-tradition reading systems. Its silence on the deeper symbolism (by "
        "Golden Dawn oath) paradoxically made it more influential: readers projected "
        "their own meanings into the gaps, which is structurally why the RWS "
        "tradition produced the enormous diversity of modern deck interpretations."
    ),
    "iconography_notes": (
        "Text-only in its original form. Later editions (University Books, Weiser) "
        "include black-and-white reproductions of Pamela Colman Smith's images. "
        "The text describes each card's design in detail, often emphasising what "
        "Waite calls 'the secret symbolism' while simultaneously withholding it. "
        "The Key is also the source of the famous error that has propagated into "
        "almost all English-language tarot: Waite misidentified the figure in "
        "The High Priestess as 'Isis' rather than the Shekinah or the Queen of the "
        "West — a conflation that has shaped 100 years of RWS interpretation."
    ),
    "significance": (
        "The interpretive axis of all RWS-tradition tarot. Where The Book of Thoth "
        "is technically exhaustive and initiatory, the Pictorial Key is accessible "
        "and deliberately incomplete — which, paradoxically, made it more generative. "
        "It established the 78-card reading framework (Major → core psychological "
        "forces; Minor → circumstances and events) that all modern tarot teaching "
        "builds on. Together with the deck itself, it created the modern idea of "
        "'tarot interpretation' as a practise distinct from cartomancy. "
        "Its counterpart-in-silence to The Book of Thoth defines the fundamental "
        "split in modern tarot philosophy: Waite's Christian mysticism vs "
        "Crowley's Thelemic initiation, accessible vs technical, gestural vs "
        "precise, devotional vs analytical."
    ),
    "sources": [
        "Waite, Arthur Edward. The Pictorial Key to the Tarot. William Rider and Son, 1910.",
        "Decker, Ronald, Thierry Depaulis, and Michael Dummett. A Wicked Pack of Cards. "
        "St. Martin's Press, 1996.",
        "Greer, Mary K. Women of the Golden Dawn. Park Street Press, 1994."
    ],
    "tags": [
        "rws_tradition",
        "golden_dawn",
        "christian_mysticism",
        "companion_text",
        "waite",
        "english",
        "esoteric_text",
        "divination_guide",
        "edwardian"
    ]
}


LIBER_AL = {
    "id": "liber-al-legis-1909",
    "name": "Liber AL vel Legis (The Book of the Law)",
    "name_local": "Liber Legis; The Book of the Law",
    "region": "Cairo (received); London (published)",
    "culture": "Thelema — founding document",
    "date_earliest": 1904,
    "date_latest": 1909,
    "date_display": "1904 (received in Cairo, April 8–10); 1909 (first print, The Equinox Vol. 1 No. 1)",
    "date_basis": (
        "Aleister Crowley claimed to have received the text through his wife Rose Kelly "
        "(acting as medium) from an entity named Aiwass over three successive noons, "
        "April 8–10, 1904, in Cairo. The original manuscript in Crowley's handwriting "
        "survives at the Warburg Institute, London. Crowley published it in The Equinox, "
        "Vol. 1, No. 1 (March 1909). The date_earliest is 1904 (claimed reception); "
        "date_latest is 1909 (verifiable public record)."
    ),
    "date_confidence": "high",
    "survival_status": "extant",
    "cards_known": 0,
    "cards_original": None,
    "missing_cards": [],
    "missing_cards_unidentified_count": None,
    "missing_cards_notes": (
        "Text document: 220 verses in three chapters, each attributed to one of the "
        "Thelemic divine figures (Nuit, Hadit, Ra-Hoor-Khuit). Not a card deck. "
        "The original handwritten manuscript survives."
    ),
    "structure": {
        "total_cards": None,
        "suits": [],
        "ranks_per_suit": None,
        "court_cards": [],
        "trump_cards": 0,
        "notes": (
            "Three chapters, each attributed to a different divine voice: "
            "Chapter I — Nuit (the infinite sky, the body of the night, the principle of unlimited space). "
            "Chapter II — Hadit (the point within Nuit, the spark of consciousness, the complement of infinite space). "
            "Chapter III — Ra-Hoor-Khuit (the hawk-headed lord, the martial child of Horus, the active force of the current Aeon). "
            "Total text: approximately 9,000 words. The divine triad Nuit/Hadit/Ra-Hoor-Khuit "
            "directly determines the iconography of the Thoth Aeon card (major-20). "
            "Chapter I, verse 57 contains the line 'All these old letters of my Book are aright; "
            "but Tzaddi is not the Star' — the direct textual authority for Crowley's reassignment "
            "of Hebrew letters to The Star (major-17) and The Emperor (major-04) in the Thoth deck."
        )
    },
    "material": ["paper", "ink_manuscript", "letterpress_print"],
    "technique": ["automatic_writing_claimed", "manuscript", "typography"],
    "language_on_cards": ["English"],
    "holdings": [
        {
            "institution": "Warburg Institute (original manuscript)",
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
            "role": "scribe_claimant",
            "name": "Aleister Crowley",
            "confidence": "high",
            "notes": (
                "Crowley claimed the text was dictated by Aiwass, his Holy Guardian Angel "
                "and a preternatural intelligence, speaking through his wife Rose Kelly. "
                "The manuscript is undeniably in Crowley's handwriting. Whether 'dictated' "
                "means authored by Crowley's subconscious or by an external entity is "
                "theologically contested within Thelema and of no concern to card history. "
                "For genealogy purposes: Crowley is the text's effective author."
            )
        },
        {
            "role": "medium",
            "name": "Rose Edith Kelly (later Rose Crowley)",
            "confidence": "high",
            "notes": (
                "Rose Crowley (née Kelly, 1874–1932) identified the communicating entity "
                "as Horus/Ra-Hoor-Khuit after Crowley tested her with images in the "
                "Cairo Museum (she correctly identified the Stele of Revealing, inv. 666, "
                "without being shown it first). Her role in the Cairo Working is documented "
                "in Crowley's diaries and in subsequent Thelemic history."
            )
        }
    ],
    "patron": None,
    "commissioned_for": "Thelemic practitioners; the founding scripture of the Aeon of Horus",
    "primary_purpose": "esoteric_theory",
    "later_uses": [
        "initiatory_scripture",
        "iconographic_source_for_thoth_deck",
        "thelemic_law"
    ],
    "purpose": ["esoteric_theory", "esoteric"],
    "transmission_path": (
        "Published in The Equinox Vol. 1 No. 1 (1909) with scholarly apparatus. "
        "Reprinted in multiple Crowley collections throughout the 20th century. "
        "Now in the public domain and freely available. The text is the foundational "
        "scripture of Thelema — functioning for Thelemites as the Torah, Bible, or "
        "Quran functions in older religious traditions. Its direct influence on the "
        "Thoth Tarot is twofold: (1) the three divine voices of Liber AL become the "
        "three figures on the Aeon card (Nuit/Hadit/Ra-Hoor-Khuit); (2) the "
        "cryptic instruction in I:57 'Tzaddi is not the Star' is Crowley's sole "
        "textual authority for his Hebrew letter reassignment in the Thoth system."
    ),
    "iconography_notes": (
        "The text itself contains no images, but its iconographic impact on the Thoth "
        "deck is systematic. Nuit (Chapter I) is depicted as a great arching starry "
        "figure in the Thoth Aeon card and appears as background cosmology throughout. "
        "Hadit (Chapter II) appears as a winged solar disc. Ra-Hoor-Khuit (Chapter III) "
        "appears as the hawk-headed child god. The Stele of Revealing (Cairo Museum "
        "inventory 666) that triggered the Cairo Working contains an image of "
        "Ra-Hoor-Khuit receiving offerings — this image directly influenced the Thoth "
        "Aeon iconography. The Star card's reassignment of Tzaddi (I:57) also "
        "determined the visual restructuring: the Star receives the Heh attribution "
        "(window, sight, observation, revelation) which is why Harris painted the "
        "figure with a butterfly (Psyche — soul as observer)."
    ),
    "significance": (
        "The root text of the Thelemic system that generated the Thoth Tarot. "
        "Without Liber AL, neither the Aeon card nor the Tzaddi swap exists, "
        "and therefore the Thoth deck lacks its two most radical structural departures "
        "from all prior tarot. The text functions in this genealogy as the Steele "
        "Sermon does for the Marseille tradition — not a deck, but the document that "
        "most directly shaped what followed. The Cairo Working (April 8–10, 1904) "
        "that produced it is, from the perspective of card history, the founding event "
        "of Thelemic tarot: the moment when a received text rather than a designed "
        "system became the authority for card iconography. This makes Liber AL unique "
        "in the entire genealogy — no other deck has a founding scripture that "
        "explicitly dictates card assignments and iconographic elements by name."
    ),
    "sources": [
        "Crowley, Aleister. Liber AL vel Legis (The Book of the Law). "
        "The Equinox, Vol. 1, No. 1. London: Wieland, 1909.",
        "Kaczynski, Richard. Perdurabo: The Life of Aleister Crowley. "
        "North Atlantic Books, 2010.",
        "DuQuette, Lon Milo. Understanding Aleister Crowley's Thoth Tarot. Weiser, 2003."
    ],
    "tags": [
        "thelema",
        "founding_text",
        "crowley",
        "aeon_of_horus",
        "tzaddi_swap",
        "cairo_working",
        "oto",
        "english",
        "esoteric_text",
        "manuscript"
    ]
}


# ─────────────────────────────────────────────────────────────────────────────
# 2. NEW GENEALOGY EDGES
# ─────────────────────────────────────────────────────────────────────────────

NEW_EDGES = [
    {
        "from": "rider-waite-smith",
        "to": "pictorial-key-1910",
        "relation": "companion_text",
        "notes": (
            "The Pictorial Key was written by Waite as the authorised interpretive "
            "guide to the RWS deck, published within a year of the deck itself. "
            "They were designed as a pair: the deck encodes the symbolism, the Key "
            "discloses (partially) what it means. The same publisher (Rider & Co.) "
            "produced both."
        )
    },
    {
        "from": "golden-dawn-corpus",
        "to": "pictorial-key-1910",
        "relation": "esoteric_source_material",
        "notes": (
            "The Key's symbolic system derives from the Golden Dawn curriculum. "
            "Waite's Hebrew letter attributions, Kabbalistic correspondences, and "
            "elemental assignments all come from GD manuscripts. The Key then "
            "partially translates this material for a non-initiated audience, "
            "while carefully omitting the portions Waite considered oath-bound."
        )
    },
    {
        "from": "liber-al-legis-1909",
        "to": "thoth-tarot",
        "relation": "direct_intellectual_source",
        "notes": (
            "Two direct structural dependencies: (1) The Aeon card's entire iconography "
            "— the three divine figures Nuit, Hadit, Ra-Hoor-Khuit — derives from "
            "the three-chapter structure of Liber AL. (2) The Tzaddi swap "
            "(I:57: 'Tzaddi is not the Star') is Crowley's sole stated authority for "
            "reassigning Hebrew letters to The Star (major-17) and The Emperor (major-04). "
            "Without Liber AL there is no Aeon card and no Tzaddi swap — the two "
            "most structurally radical features of the Thoth deck."
        )
    },
    {
        "from": "liber-al-legis-1909",
        "to": "book-of-thoth-1944",
        "relation": "direct_intellectual_source",
        "notes": (
            "The Book of Thoth is in large part an extended commentary on Liber AL's "
            "cosmological system as applied to the 78 cards. Crowley cites Liber AL "
            "throughout; the Aeon chapter (Part Two, Chapter XX) is essentially "
            "an exegesis of the divine triad. The Book of Thoth cannot be "
            "understood without Liber AL as its doctrinal foundation."
        )
    },
    {
        "from": "eliphas-levi-1855",
        "to": "book-of-thoth-1944",
        "relation": "direct_intellectual_source",
        "notes": (
            "Crowley engaged Lévi's Dogme et Rituel throughout The Book of Thoth — "
            "disputing his attributions, correcting his Hebrew, and building on his "
            "foundational claim that the tarot encodes Kabbalistic wisdom. The Book "
            "of Thoth is in part a correction and completion of Lévi's project: "
            "Lévi sketched the Kabbalistic skeleton; Crowley built full architecture "
            "on it, extending with Thelema, I Ching, and his own GD initiatory experience."
        )
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# 3. ADDITIONAL THOTH WITNESSES
# ─────────────────────────────────────────────────────────────────────────────

MORE_THOTH_WITNESSES = [
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-01",
        "present": True,
        "thoth_name": "The Magus",
        "thoth_position": 1,
        "rws_name": "The Magician",
        "rws_position": 1,
        "borrowing_source": "golden-dawn-corpus",
        "confidence": "confirmed",
        "notes": (
            "Renamed from 'The Magician' to 'The Magus' — a shift from practitioner "
            "to initiate. The RWS Magician is a confident showman at a table of "
            "implements (wand, cup, sword, pentacle), the lemniscate above his head. "
            "The Thoth Magus is a figure of pure Hermetic transmission. His central "
            "symbol is the caduceus (Mercury's wand — the card is attributed to Mercury). "
            "The three interlocked rings behind him encode the three stages of the "
            "Hermetic path (and the formula of Tetragrammaton). At the lower left, a "
            "Cynocephalus baboon (Thoth's sacred animal, the ape of Mercury) crouches — "
            "suggesting that magic without wisdom produces the ape who imitates rather "
            "than the god who creates. The four implements of the Magician appear on "
            "the Magus too but are subordinated, scattered around rather than arranged. "
            "Harris's projective geometry makes the figure appear to be in motion at "
            "multiple scales simultaneously. Crowley's attribution: Mercury, Bet (second "
            "Hebrew letter, value 2), the double power of duality-made-unity."
        )
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-14",
        "present": True,
        "thoth_name": "Art",
        "thoth_position": 14,
        "rws_name": "Temperance",
        "rws_position": 14,
        "borrowing_source": "golden-dawn-corpus",
        "confidence": "confirmed",
        "notes": (
            "Renamed from 'Temperance' to 'Art' — one of Crowley's most deliberate "
            "conceptual replacements. The RWS Temperance shows an archangel pouring "
            "liquid between two cups, the Christian virtue of moderation. Crowley "
            "rejected the Christian framing entirely: the card is attributed to "
            "Sagittarius (Fire, the arrow, the archer) and to the alchemical process "
            "of coniunctio — the chemical wedding, the union of opposites. "
            "Harris's image shows a crowned androgynous figure pouring fire and water "
            "simultaneously between two cups, but the cups are now directed back into "
            "the figure's own heart — the Great Work completes within the practitioner. "
            "The lion-eagle of alchemy (Leo + Scorpio, fixed fire + fixed water) "
            "appears below. The six-pointed Star of David behind the figure encodes "
            "the alchemical motto V.I.T.R.I.O.L. (Visita Interiora Terrae Rectificando "
            "Invenies Occultum Lapidem — Visit the interior of the earth, by "
            "rectification you will find the hidden stone). The renaming to 'Art' "
            "encodes Crowley's thesis that the Great Work is the highest art — the "
            "transformation of the self into the Philosopher's Stone."
        )
    },
    {
        "deck_id": "thoth-tarot",
        "card_id": "major-17",
        "present": True,
        "thoth_name": "The Star",
        "thoth_position": 17,
        "rws_name": "The Star",
        "rws_position": 17,
        "borrowing_source": "liber-al-legis-1909",
        "confidence": "confirmed",
        "notes": (
            "The name is unchanged, but the card is structurally reassigned. "
            "In every prior deck (Marseille, GD, RWS), The Star is attributed to "
            "Tzaddi (the Hebrew fishhook, value 90, Aquarius). Crowley broke this "
            "attribution on the authority of Liber AL vel Legis I:57: 'All these old "
            "letters of my Book are aright; but Tzaddi is not the Star.' He moved "
            "Tzaddi to The Emperor (major-04, previously attributed to Heh) and moved "
            "Heh (the Hebrew window, value 5, Aries) to The Star. This swap has no "
            "precedent in any tarot or GD document before Liber AL. It affects the "
            "entire Hebrew letter sequence of the Major Arcana. "
            "Harris's Star card retains the nude figure pouring water as in Marseille "
            "tradition, but adds: a butterfly (Psyche, the soul as observer — the Heh "
            "attribution means 'window,' sight, the gaze that sees without distorting). "
            "The seven-pointed star of Babalon appears behind the figure. The figure "
            "stands on land and water simultaneously, encoding the Aquarian/Arian duality "
            "of the new attribution. Most Thelemites and Thoth readers quietly ignore "
            "the Tzaddi swap in practice — the card still reads as 'The Star' in "
            "most spreads regardless of its Hebrew letter."
        )
    }
]


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved {path}")


def add_to_decks():
    d = load_json(DECKS_PATH)
    existing_ids = {dk["id"] for dk in d["decks"]}

    new_decks = [PICTORIAL_KEY, LIBER_AL]
    for deck in new_decks:
        if deck["id"] in existing_ids:
            print(f"  {deck['id']} already present — skipping")
        else:
            # Insert after rider-waite-smith / thoth-tarot respectively
            if deck["id"] == "pictorial-key-1910":
                idx = next(i for i,dk in enumerate(d["decks"]) if dk["id"] == "rider-waite-smith")
            else:  # liber-al-legis-1909 — insert before thoth-tarot
                idx = next(i for i,dk in enumerate(d["decks"]) if dk["id"] == "thoth-tarot") - 1
            d["decks"].insert(idx + 1, deck)
            existing_ids.add(deck["id"])
            print(f"  Inserted {deck['id']} at index {idx + 1}")

    existing_edges = {(e.get("from", ""), e.get("to", "")) for e in d["genealogy"]}
    added_edges = 0
    for edge in NEW_EDGES:
        key = (edge["from"], edge["to"])
        if key in existing_edges:
            print(f"  Edge {key} already present — skipping")
        else:
            d["genealogy"].append(edge)
            existing_edges.add(key)
            added_edges += 1

    print(f"  Added {added_edges} genealogy edge(s)")
    save_json(DECKS_PATH, d)
    return len(d["decks"]), len(d["genealogy"])


def add_to_witnesses():
    cw = load_json(WITNESSES_PATH)
    existing_keys = {
        (w.get("deck_id", ""), w.get("card_id", ""))
        for w in cw["witnesses"] if "deck_id" in w and "card_id" in w
    }

    added = 0
    for entry in MORE_THOTH_WITNESSES:
        key = (entry.get("deck_id", ""), entry.get("card_id", ""))
        if key in existing_keys:
            print(f"  Witness {key} already present — skipping")
        else:
            cw["witnesses"].append(entry)
            existing_keys.add(key)
            added += 1

    print(f"  Added {added} witness entries")
    if added:
        save_json(WITNESSES_PATH, cw)
    return len(cw["witnesses"])


if __name__ == "__main__":
    print("=== _add_deep.py ===")
    print()
    print("historical_decks.json:")
    deck_count, edge_count = add_to_decks()
    print(f"  Total decks: {deck_count}  |  Total genealogy edges: {edge_count}")
    print()
    print("card_witnesses.json:")
    witness_count = add_to_witnesses()
    print(f"  Total witnesses array entries: {witness_count}")
    print()
    print("Next: python -X utf8 _build_decks_db.py")
