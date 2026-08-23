# Area Charts

Creating filled area charts with ProvChart.

## Basic Area Chart

```scss
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
</div>
```

## How the Fill Renders

The fill uses `clip-path: polygon()`:

```css
.chart-fill {
  clip-path: polygon(
    0% var(--st-p1),
    14% var(--st-p2),
    28% var(--st-p3),
    42% var(--st-p4),
    57% var(--st-p5),
    71% var(--st-p6),
    85% var(--st-p7),
    100% var(--st-p8),
    100% 100%,
    0% 100%
  );
}
```

The last two points (`100% 100%`, `0% 100%`) close the shape at the bottom.

## Fill Styling

```scss
.chart-fill {
  opacity: 0.85;
}
```

## Gradient Fill

The default fill uses a gradient:

```css
background: linear-gradient(
  180deg,
  color-mix(in srgb, var(--st-accent) 35%, transparent),
  transparent
);
```

Override with custom gradient:

```scss
.chart-fill {
  background: linear-gradient(180deg, rgba(139, 123, 255, 0.4), transparent);
}
```

## Area with Line

Combine fill and line:

```scss
@st-chart-fill(.chart-fill)
@st-chart-line(.chart-line)

.chart {
  @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
}
```

```html
<div class="chart">
  <div class="chart-fill"></div>
  <div class="chart-line"></div>
</div>
```

## Transitions

Animate between data states:

```scss
.chart-fill {
  transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Area Chart</title>
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

    .chart-fill {
      opacity: 0.85;
      transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .chart-line {
      @st-chart-line-width(2px);
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

- [Points and Dots](08-points-and-dots.md)

---

[Previous: Line Charts](06-line-charts.md) | [Back to Documentation](../README.md)
