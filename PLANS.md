# tarocchi.help — Project Plans

**Domain:** tarocchi.help (optional future domain)
**Concept:** A serious, reflective tarot reading tool. "The cards help you think."
**Stack:** Single-file HTML SPAs, vanilla JS, CSS 3D, local deterministic synthesis
**Aesthetic:** Deep violet/candlelight gold, Cormorant Garamond serif + IBM Plex Mono, dark background
**Deck art:** Original symbolic SVG design plus locally hosted historical/publicly sourced deck images

---

## Phase 1 — Corpus: `data/cards.json` ✓ COMPLETE

Full 78-card structured dataset. The UMF of tarot.

Schema per card:
```json
{
  "id": "major-00",
  "number": 0,
  "name": "The Fool",
  "name_it": "Il Matto",
  "arcana": "major",
  "suit": null,
  "element": "Air",
  "planet": null,
  "zodiac": "Uranus",
  "hebrew_letter": "Aleph",
  "keywords": ["beginnings", "spontaneity", "a leap of faith"],
  "shadow_keywords": ["recklessness", "naivety", "poor judgment"],
  "upright_meaning": "New beginnings, innocence, spontaneity, a free spirit",
  "reversed_meaning": "Holding back, recklessness, risk-taking",
  "archetype": "The Innocent",
  "numerology": "0 — unlimited potential, the void before creation",
  "visual_symbols": ["cliff", "white dog", "bindle", "sun", "flower"],
  "traditional_phrases": ["Le Mat", "The Unnumbered Card"]
}
```

Also includes `data/spreads.json` — 5 spread layouts:
- Daily Single (1 card)
- Past / Present / Future (3 cards)
- Celtic Cross (10 cards)
- Horseshoe (7 cards)
- Year Ahead (13 cards, one per month + synthesis)

Validation: `_validate.py` — checks all 78 cards, required meanings and keywords, suit counts, and duplicate IDs.

---

## Phase 2 — Reader SPA: `index.html`

Single-file SPA. No dependencies except Google Fonts CDN.

### UI Flow
1. **Landing** — title "tarocchi.help", subtitle "the cards help you think", [Begin Reading] button
2. **Choose Spread** — 5 spread type cards with descriptions
3. **Shuffle** — animated card pile, click to shuffle (visual riffle)
4. **Draw** — click cards from facedown pile, fly to spread position
5. **Flip** — click each card to reveal, CSS 3D flip animation
6. **Reversed** — ~30% chance any card lands reversed, tracked in reading
7. **Synthesis** — per-card meaning and a deterministic synthesis panel at bottom
8. **Share** — encode reading in URL hash (card IDs + orientations + spread), copy-link button
9. **Journal** — localStorage, last 10 readings, accessible from nav

### Card Art
- Original minimal SVGs generated inline — each Major Arcana has a unique symbol
- Minor Arcana: suit icon (wand/cup/sword/pentacle) + pip count + court figure for face cards
- Back design: geometric mandala pattern (CSS/SVG, no external images)

### Synthesis
- Works entirely in the browser with no API key or backend
- Uses position, card orientation, keywords, and meanings to build a deterministic brief
- An authenticated AI endpoint can be added later; do not expose a provider key in this static site

### Color palette
```css
--bg: #0d0a14
--surface: #1a1428
--accent: #c9a84c      /* candlelight gold */
--accent2: #7b4fa6     /* deep violet */
--text: #e8e0f0
--muted: #7a6e8a
--card-back: #1e1632
```

### Typography
- Headings: Cormorant Garamond (Google Fonts)
- Body/UI: Inter
- Synthesis output: IBM Plex Mono (monospace feel for "synthesis")

---

## Phase 3 — Deploy: optional static hosting

The site runs locally with `python3 -m http.server 8000`. It can also be deployed to any static host.
- Files: `index.html`, `explorer.html`, and the required `data/` assets

---

## Phase 4 — Minarealm Bridge (future)

Embed lightweight version in minarealm.shop for Mara Divine / Mandy Kay pre-session readings.
- Client draws before booking, AI synthesizes brief
- CTA → book live session
- Iframe embed or separate subdomain: reader.minarealm.shop

---

## Phase 5 — Historical Decks Database ✓ SCHEMA COMPLETE

**Files:** `data/historical_decks.json` (source), `data/decks.db` (SQLite, built by `_build_decks_db.py`)

49 decks · 83 genealogy edges · 237 card witnesses in the current data snapshot

### Schema design decisions

**Dates as ranges, never a single year.** Every deck gets `date_earliest`, `date_latest`, `date_display` (human string), `date_basis` (evidence cited), `date_confidence` (exact/high/medium/low). The 1392 Charles VI court payment — often cited as "oldest tarot" — refers to plain playing cards, not tarot at all; the deck named "Charles VI Tarot" is actually c. 1440–1470. The date_basis field is where that gets recorded.

**Survival as first-class field.** `survival_status` ∈ {extant, fragmentary, documented, lost}. The Mamluk deck (15 of 52 cards) and Visconti-Sforza (74 of 78, split across 3 institutions) are both `fragmentary`. The `cards_known` vs `cards_original` pair quantifies the gap.

**Holdings are a join table.** The Visconti-Sforza is split 35/26/13 across Morgan Library (New York), Accademia Carrara (Bergamo), and Casa Colleoni. A single `location` column cannot represent this.

**Attributions carry roles and confidence.** Bonifacio Bembo gets `artist_primary` with confidence `high` for Visconti-Sforza (Sforza court association documented) but only `medium` for Visconti di Modrone (style-only attribution). Antonio Cicognara gets `low` for the replacement cards. Pamela Colman Smith gets `artist` / `high` for RWS — but note her name was omitted from the deck for decades.

**Genealogy is a typed edge list.** Not a tree — a directed graph. `sola-busca → rider-waite-smith` [direct_iconographic_source] captures that Smith lifted compositions directly. `tarot-de-marseille-dodal → rider-waite-smith` [reaction_against] captures Waite's deliberate departure.

**Structure is deck-relative.** Mamluk: 52 cards, 0 trumps, no human figures. Minchiate: 97 cards, 41 trumps, zodiac. Tarot: 78, 22 trumps. These are not deviations from a standard — they ARE the history.

### Current status
**49 decks · 83 genealogy edges · 237 card witnesses** are represented in the current data files and deployed by `_deploy.py`.
Timeline spans more than 1,100 years, from Tang-era records through contemporary 21st-century decks. The JSON files are the source of truth; do not maintain a second roster in this document.

### Modern deck additions
The current corpus now includes seven influential modern decks in metadata form:
- Morgan-Greer Tarot (1979)
- Universal Waite Tarot (1990)
- Robin Wood Tarot (1991)
- Jodorowsky-Camoin Tarot de Marseille (1997)
- The Wild Unknown Tarot (2012)
- Light Seer's Tarot (2019)
- Modern Witch Tarot (2019)

These records include creators, dates, structure, significance, source notes, official links, and genealogy edges. Their card art is copyrighted and is not mirrored locally. The explorer displays the image-rights status and source link instead.

### Historical Explorer UI
`explorer.html` — standalone SPA that loads `data/historical_decks.json` + `data/card_witnesses.json` via fetch.
- **Timeline tab** — vertical chronological rail, click deck to expand detail panel (holdings, attributions, genealogy edges, significance)
- **Genealogy tab** — SVG force-directed graph of deck relationships; edge type color-coded; click node to highlight lineage
- **Witnesses tab** — filterable table of card borrowings across decks; filter by deck, card, confidence level
- **People tab** — key figures (Waite, Smith, Etteilla, Crowley, Harris, Bembo, Levi, Wirth, de Guaita, Jodorowsky, and modern deck creators) with dates, role, and decks affected

Same aesthetic as index.html (dark violet, Cormorant Garamond, IBM Plex Mono). Nav link from index.html.

---

## File Tree (current)
```
tarocchi/
  index.html          ← reader SPA
  explorer.html       ← historical deck explorer
  PLANS.md            ← project notes and operating plan
  data/
    cards.json        ← 78-card corpus
    spreads.json      ← 5 spread layouts
    historical_decks.json
    card_witnesses.json
    images/            ← local artwork and manifest (copyright status varies)
  _validate.py        ← portable corpus validation
  _deploy.py          ← FTPS deployment
```

---

## Key Decisions
- No external image CDN — all art inline SVG/CSS
- No framework — vanilla JS only
- No backend dependency — the reader works from static assets alone
- Public domain positioning: original art, original data schema
- Copyrighted deck art is linked to official sources rather than copied into the repository
- `.help` TLD frames purpose: this tool helps you think, not predict

---

## Status
- [x] Phase 1: corpus
- [x] Phase 2: reader SPA
- [x] Phase 3: static site ready (local HTTP server verified)
- [ ] Phase 4: minarealm bridge
- [x] Phase 5: historical decks database (49 decks, 83 edges, 237 witnesses)
- [x] Phase 5b: explorer.html UI
- [ ] Phase 6: minarealm bridge embed

## Maintenance Notes

- Keep the local HTTP workflow documented and working: `python3 -m http.server 8000`.
- Keep JSON-backed HTML interpolation escaped.
- Keep copyrighted modern deck art linked to official sources rather than copied into the repository.
- Consolidate the root data-acquisition scripts only after confirming which historical downloads are still reproducible.
- Add a CSP and compressed share encoding before public hosting becomes a priority.
