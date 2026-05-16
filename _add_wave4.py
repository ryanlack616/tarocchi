"""
_add_wave4.py — Fourth enrichment pass.

Genealogy edges (3):
  etteilla-grand-etteilla-1789 → eliphas-levi-1855  [reaction_against]
  eliphas-levi-1855            → papus-tarot-1889    [direct_intellectual_source]
  paul-christian-1863          → papus-tarot-1889    [direct_intellectual_source]

Text-deck witnesses (5):
  liber-al-legis-1909  / major-04   — the Tzaddi verse (I:57) commands Emperor's letter swap
  book-of-thoth-1944   / major-01   — systematic astrological/Hebrew attribution table
  book-of-thoth-1944   / wands-14   — court card hierarchy restructuring in text
  pictorial-key-1910   / major-02   — Boaz/Jachin two-pillar framing, TORA scroll
  pictorial-key-1910   / major-10   — four-evangelist corner creatures explained

Motherpeace witnesses (2):
  motherpeace-1981     / major-00   — Fool regendered; round format's structural effect
  motherpeace-1981     / major-08   — Strength shows woman embracing bear, not lion

Run: python -X utf8 _add_wave4.py
"""
import json

DECKS_PATH     = "data/historical_decks.json"
WITNESSES_PATH = "data/card_witnesses.json"


NEW_EDGES = [
    {
        "from": "etteilla-grand-etteilla-1789",
        "to": "eliphas-levi-1855",
        "relation": "reaction_against",
        "notes": (
            "Lévi opens Dogme et Rituel de la Haute Magie (1854) by explicitly "
            "engaging and repudiating Etteilla's card attribution system. Etteilla "
            "had reassigned the Hebrew letters to the Majors according to his own "
            "cartomantic logic — a sequence that Lévi found arbitrary and occultly "
            "ungrounded. Lévi's alternative assignment (Aleph = I/The Juggler, "
            "Bet = II/The High Priestess, etc.) was his counter-proposal, and "
            "Lévi's system — not Etteilla's — is what the Golden Dawn, Waite, "
            "and Crowley all inherited. This reaction-against edge is the fork in "
            "the road: after Lévi, there are two distinct tarot traditions — the "
            "Etteilla cartomantic lineage (Grand Etteilla → Etteilla II → 19th-century "
            "French cartomancy) and the Lévi esoteric lineage (Lévi → GD → RWS → "
            "Thoth). The two lineages rarely interact after this point."
        )
    },
    {
        "from": "eliphas-levi-1855",
        "to": "papus-tarot-1889",
        "relation": "direct_intellectual_source",
        "notes": (
            "Gérard Encausse (Papus, 1865–1916) was Lévi's most systematic French "
            "successor. His Tarot des Bohémiens (1889) explicitly presents itself as "
            "a rigorous elaboration of Lévi's Kabbalistic framework applied to the "
            "78-card tarot. Papus accepts Lévi's 22-Major/22-Hebrew-letter doctrine, "
            "adopts his planetary and elemental correspondences, and extends Lévi's "
            "system into a complete divinatory manual. Where Lévi was often gestural "
            "and provocative, Papus was systematic and teacherly — his deck and text "
            "became the primary vector through which Lévi's ideas reached late "
            "19th-century French occultist circles. Papus was also a founding member "
            "of the Ordre Martiniste and in contact with the Golden Dawn's Paris Ahathoor "
            "temple — making him a transmission point between the French and English "
            "esoteric traditions."
        )
    },
    {
        "from": "paul-christian-1863",
        "to": "papus-tarot-1889",
        "relation": "direct_intellectual_source",
        "notes": (
            "Papus drew directly on Paul Christian's Egyptian temple pseudo-narrative "
            "as the structuring frame for the Major Arcana interpretation in "
            "Tarot des Bohémiens. Christian had described the 22 Majors as 22 "
            "initiatory stations in a secret Egyptian temple — numbered explicitly "
            "from 1 to 22. Papus accepted this numbered sequence and the Egyptian "
            "initiation framework (while knowing it was a fabrication) as a useful "
            "pedagogical myth. Christian's Egyptian pseudo-names for the Majors "
            "(Le Mage, La Porte du Sanctuaire, La Reine du Ciel, etc.) appear "
            "in Papus's text. The transmission of Christian's numbering scheme "
            "through Papus was one route by which the modern numbered Major Arcana "
            "sequence became standardised before the Golden Dawn manuscripts circulated."
        )
    },
]


NEW_WITNESSES = [
    # ── Liber AL ────────────────────────────────────────────────────────────
    {
        "deck_id": "liber-al-legis-1909",
        "card_id": "major-04",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Chapter I, verse 57 of Liber AL vel Legis contains the cryptic line: "
            "'All these old letters of my Book are aright; but Tzaddi is not the Star.' "
            "This single verse is Crowley's sole stated authority for his Hebrew letter "
            "reassignment in the Thoth Tarot. In every prior system — Marseille, "
            "Golden Dawn, Wirth, RWS — The Star is attributed to Tzaddi (the Hebrew "
            "fishhook, value 90, the sign Aquarius). Crowley's swap moved Tzaddi to "
            "The Emperor (major-04, previously attributed to Heh/Aries) and moved "
            "Heh (the Hebrew window, value 5, the sign Aries) to The Star (major-17). "
            "The Emperor is therefore the card that directly *receives* Tzaddi in "
            "Crowley's reassignment — making it the pivot of the swap. Crowley "
            "explains in The Book of Thoth (1944) that the letter Tzaddi means the "
            "'hook' or 'fishhook' — the instrument of capture — and that the Emperor "
            "as the principle of ruling masculine force is the appropriate 'hook' that "
            "snares reality into order. The Star (major-17) then receives Heh, the "
            "window — observation, revelation, the gaze outward — which Crowley reads "
            "as more appropriate to the card's meaning of hope and cosmic vision. "
            "No tarot commentator before Crowley had proposed this swap; no text "
            "after him in the Thelemic tradition has disputed it."
        )
    },

    # ── Book of Thoth ────────────────────────────────────────────────────────
    {
        "deck_id": "book-of-thoth-1944",
        "card_id": "major-01",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "The Book of Thoth (1944) is the first published text to provide a "
            "complete, systematic, cross-referenced attribution table for all 78 "
            "tarot cards: Hebrew letters, zodiacal signs, planets, elements, "
            "Kabbalistic paths on the Tree of Life, I Ching hexagrams, and "
            "magical formulae (the Tetragrammaton, AUMGN, etc.). The Magus (major-01) "
            "is the prototypical example of this system: Crowley attributes the card "
            "to Mercury (planet), Bet (Hebrew letter, value 2, meaning 'house'), "
            "Path 12 on the Tree of Life (connecting Kether to Binah — the path "
            "from the Crown to Understanding through the mind of Mercury). The "
            "astrological correlation is not merely symbolic: Mercury as the "
            "communicator, the trickster, the magician-of-words, is the *identity* "
            "of the Magus. Crowley's attribution table in The Book of Thoth became "
            "the reference standard for all subsequent Thoth-tradition tarot scholarship "
            "and influenced the Hermetic Tarot (Dowson, 1979) and many academic "
            "studies of the occult tarot. It is the most rigorous attribution system "
            "in tarot history, though contested by those who follow GD (Mathers/Waite) "
            "or Lévi's earlier assignments."
        )
    },
    {
        "deck_id": "book-of-thoth-1944",
        "card_id": "wands-14",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "The Book of Thoth devotes a chapter to the court cards and explains "
            "Crowley's restructuring of the court hierarchy. In standard tarot "
            "(TdM, RWS): King → Queen → Knight → Page. In Crowley's system: "
            "Knight (Fire) → Queen (Water) → Prince (Air) → Princess (Earth). "
            "The crucial change is that the King is demoted and renamed Knight: "
            "Crowley argues that the King/Knight confusion in prior decks (where "
            "the mounted figure was sometimes called King, sometimes Knight) "
            "was an error — the mounted figure *is* the Knight, the active Fire "
            "principle in each suit. The Queen remains (Water, the receptive but "
            "not passive force). The prior Knight (mounted, active) becomes the "
            "Prince (Air, the son of the King and Queen, the intellectual force). "
            "The Page becomes the Princess (Earth, the stable but potentially "
            "explosive feminine ground). Each title is elemental, not feudal: "
            "Knight=Fire, Queen=Water, Prince=Air, Princess=Earth — the four "
            "elements as four modes of each suit's energy. The Book of Thoth "
            "explains the rationale in detail in Part Three ('The Small Cards') "
            "and is the only text that makes the Thoth court card system fully "
            "comprehensible. Most modern practitioners who use Thoth-tradition "
            "decks learn the Knight/Queen/Prince/Princess system from this text."
        )
    },

    # ── Pictorial Key ────────────────────────────────────────────────────────
    {
        "deck_id": "pictorial-key-1910",
        "card_id": "major-02",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Waite's treatment of The High Priestess in the Pictorial Key is the "
            "site of two of the text's most enduring contributions to English-language "
            "tarot. First: the two pillars. Waite identifies the columns behind the "
            "High Priestess as Boaz (black, ב, the pillar of Severity in Solomonic "
            "Temple tradition) and Jachin (white, י, the pillar of Mercy) — the two "
            "pillars of Solomon's Temple as described in I Kings 7:21. Smith painted "
            "them with these designations visible, and the B/J pillar framing became "
            "canonical for all RWS-derived High Priestess cards. Second: the TORA "
            "scroll. The scroll on the High Priestess's lap is partially visible, "
            "reading 'TORA' (the rest hidden by her veil). Waite knew this was the "
            "Torah — the Jewish law — but the anagram TARO (Tora → Taro, rotating "
            "the letters) was noted by later commentators and became an influential "
            "mnemonic. Paul Foster Case (BOTA, 1929) explicitly added 'TORA' to the "
            "scroll in his line-art deck and taught the TARO anagram as a key to the "
            "Major Arcana's inner structure. Waite's Key also famously misidentifies "
            "the High Priestess as 'Isis the Egyptian goddess' — a conflation of the "
            "Shekinah (the feminine divine presence of the Hebrew tradition) with the "
            "Egyptian goddess, which has shaped 100 years of Isis-in-tarot "
            "interpretation despite being textually unsupported by the card's own "
            "Kabbalistic symbolism."
        )
    },
    {
        "deck_id": "pictorial-key-1910",
        "card_id": "major-10",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Waite's Pictorial Key explanation of The Wheel of Fortune introduced "
            "two iconographic elements that Smith embedded in the RWS card and that "
            "have been canonical in all RWS-derived versions ever since. First: the "
            "four corner creatures. The four figures in the corners of Smith's Wheel "
            "of Fortune — a winged Man (Aquarius), an Eagle (Scorpio), a Lion (Leo), "
            "and a Bull (Taurus) — are the four Fixed Signs of the zodiac, equated "
            "by Waite with the four Evangelists of Christian tradition (Matthew, Mark, "
            "Luke, John) and with the four Living Creatures of Ezekiel's vision "
            "(Ezekiel 1:5-14) and the Revelation of John (4:7). The Key explains "
            "that these four figures represent the stability of the divine order "
            "within the turning of the Wheel — the fixed points around which Fortune "
            "revolves. Second: the sphinx atop the Wheel. Waite's Key identifies the "
            "sphinx as the 'enigma of Life' — the riddle that stands at the center "
            "of Fortune. In Egyptian tradition, the sphinx represents the synthesis "
            "of the four elements (lion/body=fire, bull/legs=earth, eagle/wings=air, "
            "human face=water or spirit). On the Wheel, the sphinx holds a sword — "
            "the instrument of discriminating wisdom that cuts through Fortune's "
            "illusions. Crowley's Thoth Wheel of Fortune retains the four fixed-sign "
            "creatures but replaces the sphinx with the Sphinx of Giza and adds the "
            "figures of Hermanubis (ascending), Typhon (descending), and the Sphinx "
            "(poised above) as the three modes of the Wheel's operation."
        )
    },

    # ── Motherpeace ─────────────────────────────────────────────────────────
    {
        "deck_id": "motherpeace-1981",
        "card_id": "major-00",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "The Motherpeace Fool is a dancing, ecstatic feminine figure — explicitly "
            "and deliberately regendered from the Waite-tradition Fool (consistently "
            "depicted as masculine). The Fool dances near the edge of a cliff with "
            "arms raised and face upturned, joyfully present to the moment of "
            "beginning. The dog companion remains but is depicted as a spirited "
            "animal dancing alongside rather than nipping at heels. This card is also "
            "the best site for documenting the Motherpeace deck's most radical "
            "physical innovation: the round card format. The 78 cards of Motherpeace "
            "are circular (approximately 4.5 inch diameter) rather than rectangular. "
            "This has structural consequences for interpretation: (1) there is no "
            "upright/reversed binary — instead, card orientation ranges from fully "
            "upright through degrees of tilt to fully inverted, with each degree "
            "indicating a different quality of the card's energy (fully upright = "
            "full expression; tilted = partial, emerging, or waning; fully inverted = "
            "blocked, internalized, or shadow). (2) The round format makes every card "
            "a mandala — a self-contained world — and encourages holistic rather than "
            "positional reading. (3) The format reflects Vogel and Noble's feminist "
            "cosmology: the circle as the ancient symbol of the feminine, the cyclical, "
            "the non-hierarchical, contrasted with the rectangle as a cultural "
            "signifier of the masculine, the linear, the framed and bounded. "
            "No subsequent major-market tarot deck has adopted the round format "
            "as a structural choice (though it has appeared in specialty and art decks), "
            "making Motherpeace's round format its most distinctive and unrepeated contribution."
        )
    },
    {
        "deck_id": "motherpeace-1981",
        "card_id": "major-08",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "In Motherpeace, Strength (following the GD/RWS position of VIII) shows "
            "a woman in a tender, fearless embrace with a large bear — not a lion. "
            "This substitution is both culturally deliberate and iconographically "
            "significant. The bear is the totem animal most associated with the "
            "pre-patriarchal goddess traditions that Vicki Noble and Karen Vogel drew "
            "on: the bear as the Great Goddess in her most primal, protecting form "
            "appears in Old European (Gimbutas) archaeological contexts and in Native "
            "American and Siberian shamanic traditions. By replacing the lion (the "
            "solar king, the masculine principle of tamed animal nature) with the "
            "bear (the lunar, chthonic, maternal power), Motherpeace recentres the "
            "card's meaning from 'the civilizing of nature by spiritual force' to "
            "'the mutual recognition between human consciousness and wild, feminine "
            "earth power.' The woman does not charm or subdue the bear; she "
            "embraces it and is embraced in return — the strength is relational, "
            "not hierarchical. This is the card where Motherpeace's core theological "
            "argument — that strength is not dominion but communion — is most "
            "directly and economically expressed."
        )
    },
]


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved {path}")


if __name__ == "__main__":
    print("=== _add_wave4.py ===")
    print()

    # Genealogy edges
    print("Genealogy edges:")
    d = load_json(DECKS_PATH)
    existing_edges = {(e.get("from", ""), e.get("to", "")) for e in d["genealogy"]}
    added_edges = 0
    for edge in NEW_EDGES:
        key = (edge["from"], edge["to"])
        if key in existing_edges:
            print(f"  {key} already present — skipping")
        else:
            d["genealogy"].append(edge)
            existing_edges.add(key)
            added_edges += 1
            print(f"  + {key[0]} → {key[1]} [{edge['relation']}]")
    save_json(DECKS_PATH, d)
    print(f"  Total genealogy edges: {len(d['genealogy'])}")

    print()
    print("Witnesses:")
    cw = load_json(WITNESSES_PATH)
    witnesses = cw["witnesses"]
    existing_keys = {
        (w.get("deck_id", ""), w.get("card_id", ""))
        for w in witnesses
        if "deck_id" in w and "card_id" in w
    }

    added_witnesses = 0
    for entry in NEW_WITNESSES:
        key = (entry.get("deck_id", ""), entry.get("card_id", ""))
        if key in existing_keys:
            print(f"  {key} already present — skipping")
        else:
            witnesses.append(entry)
            existing_keys.add(key)
            added_witnesses += 1
            print(f"  + {key[0]}/{key[1]}")

    print(f"  {added_witnesses} witnesses added")
    if added_witnesses > 0:
        save_json(WITNESSES_PATH, cw)

    print()
    print("Next: python -X utf8 _build_decks_db.py")
