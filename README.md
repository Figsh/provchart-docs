
<meta
  name="description"
  content="Learn how to build lightweight data visualizations with ProvChart, a CSS-based charting system."
/>

<meta
  name="keywords"
  content="ProvChart, CSS charts, pure CSS charts, FSCSS, data visualization"
/>
# ProvChart

A pure-CSS charting system for the modern web. Build dashboards, stat cards, and data visualizations with zero JavaScript runtime — just HTML + CSS.

## What is ProvChart?

ProvChart has two parts:

| Component | Description |
|-----------|-------------|
| **st-core.fscss** | Open-source CSS charting library ([GitHub](https://github.com/fscss-ttr/st-core.fscss)) |
| **ProvChart API** | Hosted service for generating charts from data ([chart.devtem.org](https://chart.devtem.org)) |

Both render charts using **CSS `clip-path: polygon()`** and **CSS custom properties** — no Canvas, no SVG, no charting library shipped to the browser.

## Why ProvChart?

- **Zero runtime weight** — Charts are pure CSS. No chart.js, no D3, no heavy JS bundle.
- **First-paint rendering** — Charts appear instantly, no JavaScript execution required.
- **SEO-friendly** — Crawlers see your chart content immediately.
- **Simple updates** — Change CSS variables, browser repaints natively.
- **Backend-agnostic** — Use any language (Python, Node, Go) to generate chart data.

## Architecture

```
Data source (any backend)
      ↓
Compile to CSS custom properties (--st-p1 through --st-p8)
      ↓
Browser renders clip-path: polygon()
      ↓
Chart displayed via pure CSS
```

## Quick Start

### Option A: CDN Runtime (prototyping)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ProvChart Example</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)

    .chart {
      width: 300px;
      height: 200px;
      border-radius: 20px;
      position: relative;
      overflow: hidden;
      background: var(--st-surface);
      @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
    }
  </style>
</head>
<body>
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
  </div>
</body>
</html>
```

### Option B: Compiled CSS (production)

```bash
npm install -g fscss
fscss style.fscss style.css
```

## Documentation

| Guide | Description |
|-------|-------------|
| [Introduction](docs/01-introduction.md) | What ProvChart is and how it works |
| [Installation](docs/02-installation.md) | Setup options: CDN, CLI, npm |
| [Getting Started](docs/03-getting-started.md) | Your first chart in 5 minutes |
| [Core Concepts](docs/04-core-concepts.md) | How CSS charting works |
| [Chart Data](docs/05-chart-data.md) | Data format and point system |
| [Line Charts](docs/06-line-charts.md) | Line chart implementation |
| [Area Charts](docs/07-area-charts.md) | Filled area charts |
| [Points and Dots](docs/08-points-and-dots.md) | Data point markers |
| [Grid and Axes](docs/09-grid-and-axes.md) | Grid lines and axis labels |
| [Multiple Series](docs/10-multiple-series.md) | Multi-line charts |
| [Customization](docs/11-customization.md) | Styling and theming |
| [Responsive Charts](docs/12-responsive-charts.md) | Responsive behavior |
| [JavaScript Integration](docs/13-javascript.md) | Dynamic data updates |
| [Backend Integration](docs/14-backend-integration.md) | Server-side data providers |
| [Live Data](docs/15-live-data.md) | Real-time and polling updates |
| [Dashboards](docs/16-dashboards.md) | Building full dashboards |
| [Performance](docs/17-performance.md) | Performance characteristics |
| [Accessibility](docs/18-accessibility.md) | Accessibility considerations |
| [Browser Support](docs/19-browser-support.md) | Compatibility matrix |
| [Troubleshooting](docs/20-troubleshooting.md) | Common issues and fixes |
| [Best Practices](docs/21-best-practices.md) | Recommended patterns |
| [FAQ](docs/22-faq.md) | Frequently asked questions |

## JavaScript Integration

ProvChart is 100% CSS. JavaScript is optional — it only writes CSS variables:

```javascript
// Update chart data with vanilla JS
document.querySelector('.chart').style.cssText = `
  --st-p1: 40%; --st-p2: 75%; --st-p3: 55%;
  --st-p4: 60%; --st-p5: 48%; --st-p6: 66%;
  --st-p7: 52%; --st-p8: 70%;
`;
```

## Backend Integration

Any backend can provide data for ProvChart. Python example:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/chart-data')
def chart_data():
    # Query your data
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    return jsonify({'points': points})
```

Frontend fetches JSON and passes to CSS:

```javascript
const res = await fetch('/api/chart-data');
const { points } = await res.json();
updateChart(points);
```

## Examples

- [HTML/CSS](examples/html-css/) — Static charts
- [JavaScript](examples/javascript/) — Dynamic updates
- [Python/Flask](examples/flask/) — Backend API
- [React](examples/react/) — Component integration
- [Node.js](examples/node/) — Express server

## Browser Support

- Chrome 88+
- Firefox 97+
- Safari 13.1+
- Edge 88+

Requires `clip-path: polygon()` support.

## Performance

- **Compiled mode**: ~0.5 kb added to CSS. Zero runtime.
- **CDN mode**: ~10 kb FSCSS runtime. Compiled once on first load.

## Accessibility

- Use semantic HTML and ARIA labels
- Provide data tables as alternatives
- Ensure color contrast for text elements
- Consider `prefers-reduced-motion`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).

## Credits

- **st-core.fscss** by [fscss-ttr](https://github.com/fscss-ttr/st-core.fscss) — MIT License
- **FSCSS** by [figsh](https://fscss.devtem.org) — CSS preprocessor
- **ProvChart API** by [DevTemple](https://chart.devtem.org) — Hosted chart generation
