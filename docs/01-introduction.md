# Introduction

ProvChart is a pure-CSS charting system built on [st-core.fscss](https://github.com/fscss-ttr/st-core.fscss) and the [FSCSS](https://fscss.devtem.org) preprocessing ecosystem.

## What ProvChart Does

ProvChart renders data visualizations using only CSS. No Canvas. No SVG. No JavaScript charting library shipped to the browser.

Charts are built with:

- **`clip-path: polygon()`** — draws the chart shape
- **CSS custom properties** (`--st-p1` through `--st-p8`) — store data points
- **FSCSS mixins** — generate chart structure at compile time

## Two Components

### st-core.fscss (Open Source)

The rendering engine. Available on [GitHub](https://github.com/fscss-ttr/st-core.fscss), MIT licensed.

- Pure CSS charting library
- Requires FSCSS v1.1.24+
- Compiles to plain CSS
- Zero runtime in production

### ProvChart API (Hosted Service)

A hosted API at [chart.devtem.org](https://chart.devtem.org) that wraps st-core.fscss:

- Visual builder for creating charts
- Developer API for backend integration
- Returns HTML + CSS
- Paid tiers available

## How It Works

Most chart libraries:

1. Ship a large JS library
2. Wait for JS to execute
3. Create DOM / Canvas / SVG
4. Re-render on every data change

ProvChart:

1. Compile data to CSS variables
2. Browser paints with `clip-path`
3. Update = change CSS variables (native interpolation)

## When to Use ProvChart

- Lightweight dashboards
- Stat cards and KPI displays
- Admin panels
- Prototypes
- SEO-sensitive pages
- Projects where JS bundle size matters

## When NOT to Use ProvChart

- Complex interactive charts (tooltips, zooming, panning)
- Charts requiring more than 8 data points
- 3D visualizations
- Real-time streaming with high frequency updates

## Next Steps

- [Installation](02-installation.md)
- [Getting Started](03-getting-started.md)

---

[Back to Documentation](../README.md)
