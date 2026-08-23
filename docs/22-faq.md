# Frequently Asked Questions

## General

### What is ProvChart?

ProvChart is a pure-CSS charting system. It renders data visualizations using `clip-path: polygon()` and CSS custom properties — no Canvas, no SVG, no JavaScript charting library.

### What is st-core.fscss?

st-core.fscss is the open-source CSS charting library that powers ProvChart. Available on [GitHub](https://github.com/fscss-ttr/st-core.fscss), MIT licensed.

### What is FSCSS?

FSCSS is a lightweight CSS preprocessor. It compiles `.fscss` files to standard CSS.

### Do I need JavaScript?

No. ProvChart is 100% CSS. JavaScript is optional — it only writes CSS custom properties for dynamic updates.

### Do I need a build step?

For development: No. Use the CDN runtime.

For production: Recommended. Compile `.fscss` to `.css` for zero runtime.

## Data

### How many data points can I use?

Exactly 8 points per chart. Values range from 0-100.

### Can I use more than 8 points?

Not with st-core.fscss. The ProvChart API supports more points for some chart types.

### Can I customize X-axis positions?

No. X positions are fixed at 0%, 14%, 28%, 42%, 57%, 71%, 85%, 100%.

### How do I normalize my data?

```javascript
function normalizePoint(value, min, max) {
  return ((value - min) / (max - min)) * 100;
}
```

## Styling

### Can I change colors?

Yes. Override CSS custom properties:

```scss
:root {
  --st-accent: #8b7bff;
}
```

### Can I use dark mode?

Yes. Use media queries:

```scss
@media (prefers-color-scheme: dark) {
  :root {
    --st-bg: #0a0a0a;
    --st-surface: #1a1a1a;
  }
}
```

### Can I add animations?

Yes. Use CSS transitions:

```scss
.chart-fill {
  transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Integration

### Does ProvChart have a Python SDK?

No. ProvChart is a frontend CSS technology. Python backends provide data as JSON; the frontend renders charts.

### Does ProvChart have a React component?

Not officially. You can use compiled CSS in React components.

### How do I fetch data from an API?

```javascript
const res = await fetch('/api/chart-data');
const { points } = await res.json();
update(points);
```

## Performance

### Is ProvChart fast?

Yes. Compiled CSS adds ~0.5 kb. Zero runtime. Charts render instantly.

### Does ProvChart work without JavaScript?

Yes. In compiled mode, charts work with JavaScript disabled.

## Browser Support

### Which browsers are supported?

Chrome 88+, Firefox 97+, Safari 13.1+, Edge 88+.

### Does ProvChart work on mobile?

Yes. All modern mobile browsers support `clip-path`.

## ProvChart API

### What is the ProvChart API?

A hosted service at [chart.devtem.org](https://chart.devtem.org) that generates charts from data.

### Is the API free?

Free tier: 5 generations. Pro: 500/month. Business: 5,000/month.

### How do I get an API key?

1. Go to [chart.devtem.org/dashboard](https://chart.devtem.org/dashboard)
2. Open Developer API tab
3. Click Create key

---

[Previous: Best Practices](21-best-practices.md) | [Back to Documentation](../README.md)
