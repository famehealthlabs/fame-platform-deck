# F.A.M.E. Health — Platform & Capability Deck

A live, interactive version of the F.A.M.E. Health platform deck, built in the
**Squared Circles** design language and structured after the BJ's Wholesale
formulation deck (sticky nav, hairline cell grids, figure-led argument).

## Files

| Path | What it is |
|---|---|
| `index.html` | The whole deck. Self-contained HTML, CSS and vanilla JS. No build step, no dependencies. |
| `img/` | All artwork, extracted from the source PDFs and optimized for web (~4.7 MB total). |
| `assets/` | Working extraction output. Git-ignored, not needed to run the deck. |

## Squared Circles

The system takes its geometry from the F.A.M.E. mark itself: a square glyph
inside a circle.

- **Squares carry information.** Every module is a hairline-ruled cell grid.
  Nothing floats, nothing has a drop shadow, nothing is rounded.
- **Circles carry meaning.** Entity medallions, the orbit diagram, the ring
  charts, the section-divider glyphs and the status pills are all circular.
- **Type is editorial.** Helvetica Neue, tight negative tracking on display
  sizes, tabular numerals on every figure.
- **Color is structural, not decorative.** Ink for the argument, teal for
  what F.A.M.E. owns, terracotta only for the problem state.

Tokens live in `:root` at the top of `index.html`. Light is the default; the
dark palette is a token swap on `:root[data-deck="dark"]`.

## Chapter 11: what the page does that the PDF cannot

The first ten chapters translate the deck. The eleventh is the reason it is a
page at all: it computes rather than claims.

- **Launch math** — sliders for run size, retail price and sell-through resolve
  into real ship dates, an 8-12 week head start and the revenue window inside it.
  Arithmetic on the buyer's own numbers, not a forecast.
- **The live catalog** — the 851-SKU Webflow export, aggregated client-side into
  31 categories with format mix and sample SKUs. The market-category grid in
  chapter 05 deep-links into it. This is the "700+" claim made inspectable.
- **Path finder** — four questions resolve Stock vs Stock+ with the reasoning
  shown, then compose a `mailto:` to Holly carrying the numbers, the category
  and the answers. Nothing sends until the reader presses send.

Regenerate the embedded catalog after a Webflow re-export:

```bash
python3 tools/aggregate_catalog.py ../Claude/data/fame-stock-catalog.csv
```

Paste the JSON over the `var CATALOG=` literal in `index.html`. Only aggregates
ship: category counts, format mix and five sample names each. No pricing, no
customer data.

## Interactions

- Sticky topbar and section rail with live scroll tracking, plus a top progress bar.
- **Ecosystem selector**: click a tab or an orbit node to swap the entity panel.
  Both controls stay in sync and the node is keyboard reachable.
- Light/dark toggle, remembered in `localStorage`.
- Figures animate in on scroll (lead-time bars, reach rings, stat strip).
  All motion is disabled under `prefers-reduced-motion`.

## Live

Production: **https://fame-platform-deck.vercel.app** (Vercel project `fame-platform-deck`, team Vite30).
`git push` to `main` deploys. The page is served with `X-Robots-Tag: noindex, nofollow, noarchive`.

## Running it locally

```bash
python3 -m http.server 8231 --directory .
```

Then open http://localhost:8231.

## Sources

Content is taken from `F.A.M.E. Health Labs (2).pdf` (13-page platform deck) with
imagery supplemented from `F.A.M.E. Health Labs (3).pdf` (12-page image variant).
Facts cross-checked against `FAME-KNOWLEDGE-BASE.md`.

Private and confidential. Do not publish this repository or its contents publicly.
