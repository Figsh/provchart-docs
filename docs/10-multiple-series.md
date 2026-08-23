# Multiple Series

Rendering multiple data series in one chart.

## How It Works

The key concept is **one renderer, multiple datasets**:

1. Declare `@st-chart-line` once
2. Each line element carries its own data via scoped CSS variables
3. Each line gets its own color

## Implementation

```scss
@st-chart-line(.chart-line)

.chart {
  @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
}

.line-revenue {
  @st-chart-points(40, 55, 48, 62, 58, 75, 58, 70)
  background: #8b7bff;
}

.line-users {
  @st-chart-points(12, 28, 35, 42, 48, 55, 62, 80)
  background: #4fd8c4;
}
```

```html
<div class="chart">
  <div class="chart-line line-revenue"></div>
  <div class="chart-line line-users"></div>
</div>
```

## How Data Inheritance Works

1. `.chart` sets default data via `@st-chart-points`
2. `.line-revenue` overrides with its own `@st-chart-points`
3. `.line-users` overrides with its own `@st-chart-points`
4. The `.chart-line` renderer reads whichever `--st-p*` variables are in scope

## Line Styling

```scss
.line-revenue {
  @st-chart-line-width(2px);
  background: #8b7bff;
}

.line-users {
  @st-chart-line-width(1.5px);
  background: #4fd8c4;
}
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Multi-Line Chart</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
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

    .line-revenue {
      @st-chart-line-width(2px);
      background: #8b7bff;
      @st-chart-points(40, 55, 48, 62, 58, 75, 58, 70)
    }

    .line-users {
      @st-chart-line-width(1.5px);
      background: #4fd8c4;
      @st-chart-points(12, 28, 35, 42, 48, 55, 62, 80)
    }
  </style>
</head>
<body>
  <div class="chart">
    <div class="chart-line line-revenue"></div>
    <div class="chart-line line-users"></div>
  </div>
</body>
</html>
```

## Limitations

- Each line uses the same 8 X positions
- Lines cannot have different point counts
- Colors must be set manually

## Next Steps

- [Customization](11-customization.md)

---

[Previous: Grid and Axes](09-grid-and-axes.md) | [Back to Documentation](../README.md)
