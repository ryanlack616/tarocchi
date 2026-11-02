# tarocchi.help

Tarot reading and tarot history, built as a dependency-light static site.

> The cards help you think.

## What's Included

- A 78-card tarot reader with five spreads:
  - Daily Draw
  - Past / Present / Future
  - Horseshoe
  - Celtic Cross
  - Year Ahead
- Upright and reversed card readings
- Local deterministic synthesis with no API key or backend
- Share links and a local reading journal
- Dark and light themes
- Minimal inline SVG card art
- Historical explorer with timeline, genealogy, witnesses, people, cards, and lineage views
- Historical corpus covering 49 decks, 83 genealogy edges, and 237 card witnesses

## Run Locally

The pages use `fetch()` to load JSON, so serve the repository over HTTP rather than opening `index.html` directly.

```bash
python3 -m http.server 8000
```

Open:

- <http://localhost:8000/index.html>
- <http://localhost:8000/explorer.html>

## Validate

Validate the 78-card corpus:

```bash
python3 _validate.py
```

Rebuild the optional SQLite historical database:

```bash
python3 _build_decks_db.py
```

The project also uses browser smoke tests during development to verify the reader flows, image loading, and explorer tabs.

## Project Files

- `index.html`: tarot reader SPA
- `explorer.html`: historical tarot explorer
- `data/cards.json`: 78-card meanings and correspondences
- `data/spreads.json`: spread definitions
- `data/historical_decks.json`: deck metadata and genealogy
- `data/card_witnesses.json`: documented card relationships and borrowings
- `PLANS.md`: current project notes and corpus status

## Deck Art and Licensing

The reader includes original inline SVG symbols. Historical/publicly sourced deck images may be kept in the local `data/images/` directory when their source permits reuse; that directory is ignored by git because image coverage and rights vary.

Modern commercial decks are represented by metadata, citations, official links, and image-rights notes. Copyrighted card scans are not mirrored in this repository.

## Hosting

This is a static site and can be hosted locally or on any static hosting provider. No application server is required. The optional `CNAME` file is configured for `tarocchi.help`.

## License

The application code and original data schema are provided for personal and educational use. Individual historical images, deck artwork, and quoted source material remain subject to their respective rights holders.
