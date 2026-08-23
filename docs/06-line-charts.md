# Line Charts

Creating line charts with ProvChart.

## Basic Line Chart

```scss
@st-chart-line(.chart-line)
@st-chart-fill(.chart-fill)

.chart {
  width: 300px;
  height: 200px;
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  background: var(--st-surface);

  @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
}
```

```html
<div class="chart">
  <div class="chart-fill"></div>
  <div class="chart-line"></div>
</div>
```

## How the Line Renders

The line is a thin filled polygon:

1. `.chart-line` uses the same `clip-path` as `.chart-fill`
2. The line thickness is controlled by `@st-chart-line-width`
3. Default thickness: 1.5px

## Line Width

```scss
.chart-line {
  @st-chart-line-width(2px);
}
```

## Line Styling

```scss
.chart-line {
  @st-chart-line-width(2px);
  filter: drop-shadow(0 0 8px var(--st-accent));
}
```

## Line Color

Set the line color using `background` or `color`:

```scss
.chart-line {
  background: #8b7bff;
}
```

Or use the accent color from design tokens:

```scss
.chart-line {
  background: var(--st-accent);
}
```

## Line with Dots

```scss
@st-chart-dots(.chart-dot-, 8px)

.chart {
  @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
}
```

This generates 8 dot markers at each data point.

## Line Transitions

Add smooth animations:

```scss
.chart-fill, .chart-line {
  transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Multi-Line Charts

See [Multiple Series](10-multiple-series.md).

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Line Chart</title>
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

    .chart-line {
      @st-chart-line-width(2px);
      filter: drop-shadow(0 0 8px var(--st-accent));
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

- [Area Charts](07-area-charts.md)
- [Points and Dots](08-points-and-dots.md)

---

[Previous: Chart Data](05-chart-data.md) | [Back to Documentation](../README.md)
