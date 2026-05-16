"""
_add_wave3.py — Third enrichment pass.

Fixes:
  1. thoth-tarot major-20 (The Aeon): borrowing_source None → liber-al-legis-1909

Adds:
  2. Sola-Busca witnesses (8): the source cards Smith actually borrowed from —
     wands-10, wands-09, wands-02, cups-11, cups-07, cups-02, swords-08, swords-03
  3. Dodal canonical TdM witnesses (4): major-00 (Le Mat), major-11 (La Force at XI),
     major-12 (Le Pendu), major-16 (La Maison Dieu)
  4. Eliphas Lévi witness (1): major-00 — the 22-Major/22-Hebrew-letter attribution doctrine
  5. Paul-Christian witness (1): major-01 — the Egyptian pseudo-name system

Run: python -X utf8 _add_wave3.py
"""
import json

WITNESSES_PATH = "data/card_witnesses.json"


# ─────────────────────────────────────────────────────────────────────────────
# 1. FIX: Thoth major-20 borrowing_source
# ─────────────────────────────────────────────────────────────────────────────

def fix_thoth_aeon(witnesses):
    fixed = 0
    for w in witnesses:
        if w.get("deck_id") == "thoth-tarot" and w.get("card_id") == "major-20":
            if w.get("borrowing_source") is None:
                w["borrowing_source"] = "liber-al-legis-1909"
                fixed += 1
                print("  Fixed: thoth-tarot/major-20 borrowing_source → liber-al-legis-1909")
    if fixed == 0:
        print("  thoth-tarot/major-20 borrowing_source already set — no fix needed")


# ─────────────────────────────────────────────────────────────────────────────
# 2. NEW WITNESSES
# ─────────────────────────────────────────────────────────────────────────────

SOLA_BUSCA_WITNESSES = [
    {
        "deck_id": "sola-busca",
        "card_id": "wands-10",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "The Sola-Busca Ten of Wands shows a triumphant armored figure "
            "carrying ten staves or wands as a tight bundle — an image of military "
            "victory and the fruits of conquest. In the SB system, this card carries "
            "a positive valence: the warrior returns in triumph bearing his spoils. "
            "Smith adopted the visual motif almost directly for the RWS Ten of Wands "
            "but inverted the emotional meaning: her figure bends under the weight of "
            "the staves, making the card a symbol of burden, oppression, and overwork "
            "rather than triumph. The borrowing is confirmed: Smith viewed the British "
            "Museum's newly-acquired Sola-Busca photographs in 1909. The visual "
            "transposition (triumphant carrier → exhausted bearer) is one of the "
            "most striking examples of Smith reinterpreting rather than copying her source."
        )
    },
    {
        "deck_id": "sola-busca",
        "card_id": "wands-09",
        "present": True,
        "borrowing_source": None,
        "confidence": "probable",
        "notes": (
            "The Sola-Busca Nine of Wands shows a figure in armor leaning on a staff "
            "and looking over his shoulder — the posture of a soldier vigilant after "
            "battle, watching for a follow-on attack. The defensive watchfulness "
            "encoded in the body posture (leaning, back-turned gaze, grip on the staff) "
            "is transposed almost directly to Smith's RWS Nine of Wands, which shows "
            "a bandaged figure holding a staff and looking behind him with the same "
            "mixture of weariness and alertness. Smith added the bandaged head (the "
            "wound that explains the weariness) and a row of eight staves behind, "
            "transforming the solitary watchman into a figure defending against a "
            "future assault. Borrowing is probable: the posture and emotional "
            "register are close enough to be more than coincidence."
        )
    },
    {
        "deck_id": "sola-busca",
        "card_id": "wands-02",
        "present": True,
        "borrowing_source": None,
        "confidence": "probable",
        "notes": (
            "The Sola-Busca Two of Wands shows a figure on an elevated position — "
            "a terrace, parapet, or high place — with two wands, surveying the "
            "territory below. The 'lord of his domain looking outward from a height' "
            "motif is the iconographic core Smith transposed to the RWS Two of Wands: "
            "a cloaked figure stands on a castle battlement, holding a wand and a "
            "globe, looking out to the horizon. The globe Smith added is new — it "
            "encodes the aspiration to worldly dominion beyond what is visible — but "
            "the high vantage point and the surveying gaze are directly from SB. "
            "Borrowing is probable."
        )
    },
    {
        "deck_id": "sola-busca",
        "card_id": "cups-11",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "The Sola-Busca equivalent of the Page of Cups (numbered XI of Cups in "
            "some analyses, though SB doesn't use the court card naming of later "
            "decks) shows a youth in military costume with a fish — either carrying "
            "a fish or with a fish as his attribute. This fish-bearer motif is "
            "exactly what Smith transposed to the RWS Page of Cups: a youth in an "
            "ornate floral costume looking at a fish that has leaped out of his cup "
            "to address him. Smith transformed the fish from an attribute or object "
            "being carried into an active participant — the fish speaks to the Page, "
            "turning the card from a portrait into a moment of uncanny encounter. "
            "The fish-and-cups association in this position is distinctive enough "
            "to make the borrowing confirmed."
        )
    },
    {
        "deck_id": "sola-busca",
        "card_id": "cups-07",
        "present": True,
        "borrowing_source": None,
        "confidence": "probable",
        "notes": (
            "The Sola-Busca Seven of Cups contains visual elements distributed across "
            "seven cups — an arrangement of cups each containing or accompanied by a "
            "different figure or motif. This 'cups as vessels of different visions' "
            "format is the iconographic vocabulary Smith elaborated in the RWS Seven "
            "of Cups, which is among the most fantastical pip images in the deck: "
            "seven cups float in clouds, each containing a distinct vision (a "
            "castle, a serpent, a garland, a draped figure, a treasure chest, a "
            "jeweled tower, a skull). Smith greatly expanded the fantastical content, "
            "but the structural idea of multiple cups each holding a different "
            "apparition likely derives from the SB arrangement. Borrowing is probable."
        )
    },
    {
        "deck_id": "sola-busca",
        "card_id": "cups-02",
        "present": True,
        "borrowing_source": None,
        "confidence": "possible",
        "notes": (
            "The Sola-Busca Two of Cups shows two figures in a gesture of exchange "
            "or greeting with cups — the covenant-pledge motif in which two parties "
            "face each other holding their cups. Smith's RWS Two of Cups shows two "
            "figures pledging their cups to each other beneath a Hermetic caduceus "
            "and winged lion's head. The mutual offering posture and the two-figures-"
            "with-cups framing are shared. Smith added the Hermetic imagery above "
            "(the caduceus symbolising the merging of opposites into a unified force) "
            "which deepens the card's meaning from social exchange to alchemical union. "
            "Borrowing is possible; the motif of two-figures-with-cups is not unique "
            "to SB, but the timing (Smith's 1909 SB access) makes it likely."
        )
    },
    {
        "deck_id": "sola-busca",
        "card_id": "swords-08",
        "present": True,
        "borrowing_source": None,
        "confidence": "probable",
        "notes": (
            "The Sola-Busca Eight of Swords shows a figure constrained or surrounded "
            "by eight swords — the image of the prisoner hemmed in by weapons. "
            "Smith developed this into the RWS Eight of Swords: a blindfolded, loosely "
            "bound figure standing on wet ground surrounded by swords stuck upright "
            "around her. Smith's crucial addition is the blindfold and loose bonds — "
            "the figure could walk away if she could see or choose to move, making "
            "the card a study in self-imposed limitation and mental imprisonment "
            "rather than physical capture. The SB card encodes the predicament "
            "(surrounded by weapons, unable to escape); Smith encodes the psychology "
            "of the predicament (blindness and belief in one's bonds as the real "
            "prison). Borrowing is probable."
        )
    },
    {
        "deck_id": "sola-busca",
        "card_id": "swords-03",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "The Sola-Busca Three of Swords is the most direct and unambiguous "
            "visual borrowing in the entire Sola-Busca → Rider-Waite-Smith transfer. "
            "The SB card shows three swords piercing a heart — the same image, with "
            "the same three-sword arrangement, that Smith painted for the RWS Three "
            "of Swords. Smith added a stormy sky and rain (the environmental expression "
            "of grief that she routinely added to emotionally weighted cards), but the "
            "core image — three swords through a heart — is taken directly from SB. "
            "No other prior tarot has this specific image. The heart-pierced-by-swords "
            "iconography appears in Christian devotional art (the Seven Sorrows of the "
            "Virgin, the Immaculate Heart), and SB likely drew on that tradition; "
            "Smith then absorbed it via SB and stripped the explicitly devotional frame, "
            "making it a universal image of heartbreak and sorrow. Borrowing is confirmed."
        )
    },
]


TDM_DODAL_WITNESSES = [
    {
        "deck_id": "tarot-de-marseille-dodal",
        "card_id": "major-00",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Le Mat (The Fool) in the Dodal and canonical Marseille tradition is a "
            "ragged wanderer, usually shown mid-stride, carrying a stick with a bundle "
            "and being bitten at the leg or buttocks by a dog or cat. This image is "
            "a significant departure from the Visconti-lineage Fool, who is typically "
            "shown as a crowned or feathered-cap figure of ambiguous status — more "
            "court jester than outcast. The TdM Fool is specifically an outsider: "
            "his torn clothing, his wandering gait, and the animal tearing at him "
            "mark him as someone outside the social order. The animal bite is "
            "particularly distinctive — it appears in Noblet, Dodal, Madenié, and "
            "Conver, and becomes canonical. Smith retained the wandering figure and "
            "the animal companion (her dog watches the Fool approach the precipice "
            "rather than biting him — a softening) while making the precipice "
            "central. Crowley/Harris retained the Fool as the central card of "
            "unlimited potential (Aleph/Air/the Zero-point), but replaced the wanderer "
            "with a more cosmic, ecstatic figure. Both derive from the TdM Fool's "
            "essential premise: the Fool is outside-and-before all systems."
        )
    },
    {
        "deck_id": "tarot-de-marseille-dodal",
        "card_id": "major-11",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "La Force (Strength) appears at position XI in the Dodal and the canonical "
            "Marseille ordering — not at VIII. In TdM, VIII is Justice (La Justice) "
            "and XI is Strength (La Force). This TdM ordering of VIII=Justice, XI=Strength "
            "is the original sequence that preceded the Golden Dawn's inversion (GD: "
            "VIII=Strength/Leo, XI=Justice/Libra). Dodal's La Force shows a woman "
            "opening — not striking or subduing — a lion's mouth: the image of spiritual "
            "force as charm rather than dominion. She is usually shown with a hat that "
            "forms an infinity symbol (the lemniscate, also present in TdM Le Bateleur). "
            "This specific iconography — woman and lion, charm rather than combat — "
            "survived unchanged through GD, Wirth, and RWS; Smith kept the woman-and-lion "
            "image but added the GD's reordering (Strength to position VIII). The Thoth "
            "card Lust (major-08) replaces the charming maiden with Babalon riding the "
            "Beast, but retains the woman-with-lion genetic inheritance."
        )
    },
    {
        "deck_id": "tarot-de-marseille-dodal",
        "card_id": "major-12",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Le Pendu (The Hanged Man) in the Dodal and canonical TdM tradition shows "
            "a man suspended by one foot from a horizontal beam supported by two living "
            "trees (or two posts hung with lopped branches). The free leg is crossed "
            "behind the suspended leg, forming a cross-and-T figure. The hands are "
            "clasped or tied behind the back. The figure's expression is typically calm "
            "or even serene — this is not a punishment image but a voluntary suspension. "
            "This is a radical departure from the Visconti tradition, where the Hanged "
            "Man (Il Traditore) was suspended by both feet in the 'pittura infamante' "
            "(defamation painting) style — an actual punishment in medieval Italy for "
            "traitors and debtors. TdM transforms the image: by suspending only one "
            "foot and crossing the free leg, the card suggests the figure could free "
            "himself but chooses not to. The reversal of perspective (the Hanged Man "
            "sees the world upside-down) becomes central to all later interpretations. "
            "Smith retained the one-foot suspension with crossed leg exactly, adding "
            "only a golden nimbus (halo) around the Hanged Man's calm face. "
            "Crowley/Harris kept the one-foot pose but added Thelemic symbolism "
            "(the figure forms the alchemical cross and triangle with his body)."
        )
    },
    {
        "deck_id": "tarot-de-marseille-dodal",
        "card_id": "major-16",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "La Maison Dieu (The Tower, also called La Foudre or La Foudroyée) in the "
            "Dodal TdM shows a tower being struck by lightning from above, with a "
            "crown-like ball or crenellation blown off the top, and two human figures "
            "falling from the sides. The specific image of the crown or crown-like "
            "element being blown off by lightning is particularly associated with the "
            "TdM tradition. The Italian tarot tradition had called this card various "
            "names (Il Fuoco, La Sagitta) and sometimes showed the lightning as an "
            "arrow rather than a thunderbolt. TdM fixed the 'tower struck by lightning, "
            "crown knocked off, figures falling' interpretation that has been standard "
            "ever since. The card's French name, La Maison Dieu (House of God), "
            "introduced a spiritual rather than merely physical interpretation: "
            "it is not just a tower being destroyed but a false temple, a house built "
            "on wrong foundations, being struck by divine revelation. Smith retained "
            "the crown being blown off and the figures falling, set against a black sky "
            "with stylised lightning. The Thoth Tower (which Crowley kept unnamed, "
            "using the Hebrew letter Peh / the mouth) retains the lightning-and-ruin "
            "imagery but adds a serpentine lightning bolt and the eye of Horus."
        )
    },
]


LEVI_WITNESSES = [
    {
        "deck_id": "eliphas-levi-1855",
        "card_id": "major-00",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Lévi's treatment of The Fool is the site where his most consequential "
            "theoretical claim — the 22 Major Arcana correspond to the 22 Hebrew letters "
            "of the alphabet — meets its most difficult problem. In Dogme et Rituel de "
            "la Haute Magie (1854-1856), Lévi declares explicitly that the tarot's "
            "22 Major Arcana are the 22 Hebrew letters made pictorial. He assigns "
            "Aleph to The Juggler (I), Bet to The High Priestess (II), and so on "
            "through Shin (XXI) and Taw (XXII). The Fool does not fit cleanly: it is "
            "unnumbered (or numbered 0), and the Hebrew alphabet has only 22 letters. "
            "Lévi variously treats the Fool as the wild card that precedes the "
            "sequence (the zero that generates the digits), as a card associated with "
            "the three 'mother letters' (Aleph, Mem, Shin — air, water, fire), and "
            "as the laughing alchemist who knows the secret of the Philosopher's Stone. "
            "This ambiguity was inherited by the Golden Dawn, which assigned the Fool "
            "to Aleph (Air), and by Crowley, who made the Fool the zero-point of the "
            "Thelemic cosmology. Lévi's 22-letter attribution doctrine is the "
            "foundational theoretical claim of modern Western esoteric tarot: every "
            "subsequent system (GD, RWS, Thoth, BOTA, Hermetic Tarot) either "
            "follows Lévi's mappings, corrects them, or argues against them — but all "
            "take his 22-Major/22-letter claim as the starting point of the debate."
        )
    },
]


PAUL_CHRISTIAN_WITNESSES = [
    {
        "deck_id": "paul-christian-1863",
        "card_id": "major-01",
        "present": True,
        "borrowing_source": None,
        "confidence": "confirmed",
        "notes": (
            "Paul Christian (pseudonym of Jean-Baptiste Pitois, 1811-1877) in "
            "Histoire de la Magie (1863) and L'Homme Rouge des Tuileries (1863/1870) "
            "describes all 22 Major Arcana as sequential stations in an Egyptian "
            "initiatory temple, each with an Egyptian pseudo-name and a corresponding "
            "symbolic lesson. His first arcanum — corresponding to the Magician — he "
            "calls 'Le Mage' (The Magus) or 'L'Arcane du Mage de la Force Divine'. "
            "This is significant: Crowley's later renaming of the RWS 'Magician' to "
            "'The Magus' in the Thoth Tarot (1944) echoes Christian's terminology, "
            "though Crowley arrived at it through his own Hermetic and Thelemic "
            "framework rather than Christian's pseudo-Egyptian system. Christian also "
            "numbered all 22 Major Arcana explicitly from 1 to 22 — the first published "
            "text to do so, predating the GD manuscripts. His numbering matched Etteilla's "
            "cartomantic sequence in some respects and diverged in others. The GD "
            "absorbed Christian's numbered sequence (via Paul Christian → Mathers) "
            "and it became the template for the modern numbered Majors. Christian's "
            "Egyptian pseudo-names (The Magus, The Gate of the Sanctuary, The Queen "
            "of Heaven, The Cubic Stone of Initiation, etc.) circulated widely in "
            "French occultist circles and directly influenced Papus (Tarot des "
            "Bohémiens, 1889), who was Christian's intellectual successor."
        )
    },
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


if __name__ == "__main__":
    print("=== _add_wave3.py ===")
    print()

    cw = load_json(WITNESSES_PATH)
    witnesses = cw["witnesses"]

    print("Fixes:")
    fix_thoth_aeon(witnesses)

    existing_keys = {
        (w.get("deck_id", ""), w.get("card_id", ""))
        for w in witnesses
        if "deck_id" in w and "card_id" in w
    }

    all_new = (
        SOLA_BUSCA_WITNESSES
        + TDM_DODAL_WITNESSES
        + LEVI_WITNESSES
        + PAUL_CHRISTIAN_WITNESSES
    )

    print()
    print("New witnesses:")
    added = 0
    for entry in all_new:
        key = (entry.get("deck_id", ""), entry.get("card_id", ""))
        if key in existing_keys:
            print(f"  {key} already present — skipping")
        else:
            witnesses.append(entry)
            existing_keys.add(key)
            added += 1
            print(f"  + {key[0]}/{key[1]}")

    print()
    print(f"  {added} witnesses added")
    if added > 0:
        save_json(WITNESSES_PATH, cw)

    print()
    print("Next: python -X utf8 _build_decks_db.py")
