# Customization

Styling and theming ProvChart charts.

## Design Tokens

`@st-root()` sets CSS custom properties on `:root`:

| Token | Purpose |
|-------|---------|
| `--st-bg` | Background color |
| `--st-surface` | Card/surface background |
| `--st-accent` | Primary accent color |
| `--st-green` | Success/positive color |
| `--st-red` | Error/negative color |
| `--st-radius-lg` | Large border radius |
| `--st-radius-sm` | Small border radius |
| `--st-pad` | Base padding |

## Override Tokens

```scss
:root {
  --st-accent: #8b7bff;
  --st-green: #4fd8c4;
  --st-red: #ff5e7d;
}
```

## Local Token Override

Override tokens for specific elements:

```scss
.chart-dot {
  --st-accent: #c4a8ff;
}
```

## Color Customization

```scss
.chart-line {
  background: #ff5e7d;
}

.chart-fill {
  background: linear-gradient(180deg, rgba(255, 94, 125, 0.4), transparent);
}
```

## Border Radius

```scss
.chart {
  border-radius: 25px;
}
```

## Shadows and Effects

```scss
.chart-line {
  filter: drop-shadow(0 0 8px var(--st-accent));
}
```

## Transitions

```scss
.chart-fill, .chart-line {
  transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Dark Mode

Use media queries:

```scss
@media (prefers-color-scheme: dark) {
  :root {
    --st-bg: #0a0a0a;
    --st-surface: #1a1a1a;
    --st-accent: #8b7bff;
  }
}
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Custom Chart</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)

    :root {
      --st-accent: #ff5e7d;
      --st-green: #4fd8c4;
    }

    .chart {
      width: 300px;
      height: 200px;
      border-radius: 25px;
      position: relative;
      overflow: hidden;
      background: var(--st-surface);
      @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
    }

    .chart-line {
      @st-chart-line-width(2px);
      filter: drop-shadow(0 0 8px var(--st-accent));
    }

    .chart-fill {
      opacity: 0.85;
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

## Next Steps

- [Responsive Charts](12-responsive-charts.md)

---

[Previous: Multiple Series](10-multiple-series.md) | [Back to Documentation](../README.md)
