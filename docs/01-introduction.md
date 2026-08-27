# 01 introduction

**ProvChart** turns data into **pure CSS charts** (and optional **SVG**) without shipping a JavaScript chart library to the page.

You send JSON. The engine returns **HTML + CSS** (or SVG). The browser paints with custom properties and native geometry. Optional [provchart-runtime](https://github.com/fscss-ttr/provchart-runtime) adds tooltips and motion later—paint never depends on it.

| | |
|---|---|
| **Site** | [chart.devtem.org](https://chart.devtem.org) |
| **API** | `https://provchart-api.devtem.org` |
| **Docs** | [chart.devtem.org/docs](https://chart.devtem.org/docs) |
| **Live demo** | [chart.devtem.org/demo](https://chart.devtem.org/demo) |
| **Open-source roots** | [st-core.fscss](https://github.com/fscss-ttr/st-core.fscss) (same paint philosophy) |
| **Runtime** | [provchart-runtime](https://github.com/fscss-ttr/provchart-runtime) (MIT, optional) |

---

## The problem

Typical chart stacks:

1. Download a chart library  
2. Parse and execute it  
3. Only then draw SVG/canvas  

That costs bandwidth, main-thread time, and often a blank region until JS runs. SEO and Core Web Vitals feel it.

ProvChart’s path:

```text
JSON  →  generate (API or builder)  →  HTML + CSS (or SVG)
      →  first response can already paint the chart
      →  optional runtime for hover / reveal
```

No Chart.js-sized dependency is required for the shape to exist.

---

## What ProvChart is

| Piece | Role |
|-------|------|
| **Visual builder** | Dashboard UI to design charts and copy output |
| **Developer API** | `POST /api/v1/generate` → `{ html, css }` |
| **SVG API** | `POST /api/v1/generate-svg` → `{ svg, dataUri }` for README/docs |
| **Themes & types** | line, area, bar, stackedbar, hbar, scatter, combo, gauge, … |
| **Runtime (optional)** | Progressive enhancement on `[data-provchart]` HTML charts |

**Not required for paint:** provchart-runtime, React chart kits, or a global CSS “chart framework” file.

---

## Core idea

```text
series + axisX + type
        │
        ▼
   ProvChart engine
        │
        ├─► HTML roots + scoped CSS variables (e.g. --pc-…-s1-p1)
        │     browser paints lines/bars/gauges
        │
        └─► SVG string (docs, Markdown, embeds without a <style> pipeline)
```

JavaScript in your app is for **fetch, inject, or auth**—not for running a charting engine on every page view.

---

## Quick taste

```javascript
const res = await fetch("https://provchart-api.devtem.org/api/v1/generate", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY",
  },
  body: JSON.stringify({
    type: "area",
    series: [
      { name: "Traffic", color: "#4fd8c4", points: [30, 45, 40, 60, 55, 70, 65] },
      { name: "Signups", color: "#f0a860", points: [8, 12, 11, 18, 16, 22, 20] },
    ],
    axisX: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  }),
});

const data = await res.json();
if (data.success) {
  document.head.insertAdjacentHTML("beforeend", `<style>${data.css}</style>`);
  document.getElementById("chart").innerHTML = data.html;
}
```

Get a key: [Dashboard → Developer API](https://chart.devtem.org/dashboard). Signed-up free accounts include limited test generations.

---

## When to use ProvChart

**Use it when:**

- You care about payload, LCP, and crawlable markup  
- Data is JSON from a backend, CMS, CI, or an agent  
- You want multi-series line/area/bar/combo/gauge without maintaining polygons by hand  
- README/docs need SVG without a screenshot pipeline  

**Use something else when:**

- You need brush/zoom/streaming as the default UX (put a JS library on *those* routes)  
- You only need a single hand-crafted eight-point card in pure FSCSS → [st-core.fscss](https://github.com/fscss-ttr/st-core.fscss) is enough  

---

## How these docs are organized

| # | Topic |
|---|--------|
| **01** | Introduction *(you are here)* |
| 02 | [Integration](./02-installation.md) — embed HTML/CSS, SVG, CDN runtime |
| 03 | [Getting started](./03-getting-started.md) — key, first generate, inject |
| 04 | [Core concepts](./04-core-concepts.md) — compile → paint → enhance |
| 05 | [Chart data](./05-chart-data.md) — series, axisX, scale, themes |
| 06 | [Line charts](./06-line-charts.md) |
| 07 | [Area charts](./07-area-charts.md) |
| 08 | [Bar, hbar & stacked](./08-points-and-dots.md) |
| 09 | [Scatter, combo & gauge](./09-grid-and-axes.md) |
| 10 | [Multiple series](./10-multiple-series.md) |
| 11 | [Customization & themes](./11-customization.md) |
| 12 | [Responsive layouts](./12-responsive-charts.md) |
| 13 | [Runtime & interactivity](./13-javascript.md) |
| 14 | [Backend integration](./14-backend-integration.md) |
| 15 | [Live data & updates](./15-live-data.md) |
| 16 | [Dashboards](./16-dashboards.md) |
| 17 | [Performance](./17-performance.md) |

Filenames match the repo layout; titles above are the ProvChart topics they carry (e.g. `02-installation.md` = integration).

---

## Next step

Wire ProvChart into a page: API generate, inject, optional runtime.

→ **[02 · Integration](./02-installation.md)**
