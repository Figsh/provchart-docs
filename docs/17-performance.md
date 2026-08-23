# Performance

Performance characteristics of ProvChart.

## Bundle Size

| Mode | Size | Runtime |
|------|------|---------|
| Compiled CSS | ~0.5 kb added to stylesheet | Zero |
| CDN Runtime | ~10 kb FSCSS engine | Compiled once on first load |

## Rendering Performance

- Charts are pure CSS `clip-path` shapes
- No JavaScript rendering step
- No Canvas or SVG creation
- Browser's CSS engine handles painting

## Transitions

- `clip-path` transitions are compositor-accelerated (GPU)
- No layout thrash
- No DOM structure changes
- Native CSS interpolation

## Network

- Compiled mode: Zero third-party requests from chart layer
- CDN mode: One request for FSCSS runtime, one for st-core source

## SEO

- Crawlers see chart content immediately
- No hydration phase
- No render-blocking scripts
- HTML content (labels, axis values, stat cards) is fully indexable

## Large Datasets

- Limited to 8 data points per chart
- For more data, consider multiple charts or alternative libraries

## DOM Complexity

- Minimal DOM elements per chart
- No deep nesting required
- Clean HTML structure

## Caching

- Compiled CSS is cacheable
- CDN mode: FSCSS runtime cached after first load
- st-core source cached after first load

## Recommendations

- Use compiled mode for production
- Use CDN mode for prototyping
- Keep charts simple (8 points max)
- Use CSS transitions for animations
- Avoid unnecessary DOM manipulation

---

[Previous: Dashboards](16-dashboards.md) | [Back to Documentation](../README.md)
