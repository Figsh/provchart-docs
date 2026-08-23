# Installation

ProvChart offers two installation methods: CDN runtime for prototyping, and compiled CSS for production.

## Option 1: CDN Runtime (Development/Prototyping)

Add the FSCSS runtime and st-core import to your HTML:

```html
<script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

<style>
  @import((*) from st-core)

  @st-root()
  @st-container(body)
</style>
```

**Weight**: ~10 kb for FSCSS runtime. st-core is fetched as a ~5 kb `.fscss` file and compiled on first load.

## Option 2: Compiled CSS (Production)

### Install FSCSS

```bash
npm install -g fscss
```

### Create Your Stylesheet

```scss
// style.fscss
@import((*) from st-core)

@st-root()
@st-container(body)

@st-chart-fill(.chart-fill)
@st-chart-line(.chart-line)

.chart {
  width: 100%;
  height: 200px;
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  background: var(--st-surface);

  @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
}
```

### Compile

```bash
fscss style.fscss style.css
```

The output is standard CSS. No FSCSS runtime needed.

**Weight**: ~0.5 kb added to your stylesheet.

## Option 3: npm Package

```bash
npm install fscss
```

Add compile scripts to `package.json`:

```json
{
  "scripts": {
    "predev": "fscss src/styles/chart.fscss src/styles/chart.css",
    "prebuild": "fscss src/styles/chart.fscss src/styles/chart.css"
  }
}
```

## VS Code Extension

Install the FSCSS extension from the VS Code marketplace for syntax highlighting and auto-compilation on save.

## Requirements

- Modern browser with `clip-path` support
- FSCSS v1.1.24+ (for CDN mode)
- Node.js (for CLI compilation)

## Comparison

| Feature | CDN Runtime | Compiled CSS |
|---------|-------------|--------------|
| Setup | Drop in script tag | CLI command |
| Performance | JS parses before render | Instant CSS render |
| JS disabled | Chart won't show | Chart still works |
| Bundle size | Runtime included | Zero runtime cost |
| Best for | Prototyping | Production |

## Next Steps

- [Getting Started](03-getting-started.md)

---

[Previous: Introduction](01-introduction.md) | [Back to Documentation](../README.md)
