# Points and Dots

Adding data point markers to charts.

## Single Dot (Manual Placement)

Place one dot at a specific position:

```scss
@st-chart-dot(.chart-dot, 70, 60)
```

Parameters:
- `.chart-dot` — CSS class name
- `70` — X position (as % of chart width)
- `60` — Y value (0-100 scale)

```html
<div class="chart">
  <div class="chart-fill"></div>
  <div class="chart-line"></div>
  <div class="chart-dot" data-point="$405.67"></div>
</div>
```

## All Dots (Auto-Generated)

Generate all 8 data point markers:

```scss
@st-chart-dots(.chart-dot-, 9px)
```

Parameters:
- `.chart-dot-` — Base class name (each dot gets `.chart-dot-1` through `.chart-dot-8`)
- `9px` — Dot diameter

Each dot automatically positions itself at its data point.

## Dot Styling

```scss
.chart-dot {
  position: relative;
  overflow: visible;
}
```

## Tooltip on Dot

Use CSS pseudo-elements:

```scss
.chart-dot:after {
  content: attr(data-point);
  background: var(--st-accent);
  padding: 6px 8px;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  border-radius: var(--st-radius-sm);
  position: absolute;
  top: -39px;
  left: -30px;
  white-space: nowrap;
}

.chart-dot:before {
  content: '';
  width: 10px;
  height: 10px;
  background: var(--st-accent);
  transform: rotate(45deg);
  position: absolute;
  top: -18px;
  left: 2px;
}
```

## Local Accent Override

Override accent color for a specific dot:

```scss
.chart-dot {
  --st-accent: #c4a8ff;
}
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chart with Dots</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)
    @st-chart-dot(.chart-dot, 70, 60)

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
    }

    .chart-dot {
      position: relative;
      overflow: visible;
    }

    .chart-dot:after {
      content: attr(data-point);
      background: var(--st-accent);
      padding: 6px 8px;
      font-size: 12px;
      font-weight: 700;
      color: #fff;
      border-radius: var(--st-radius-sm);
      position: absolute;
      top: -39px;
      left: -30px;
      white-space: nowrap;
    }
  </style>
</head>
<body>
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
    <div class="chart-dot" data-point="$405.67"></div>
  </div>
</body>
</html>
```

## Next Steps

- [Grid and Axes](09-grid-and-axes.md)

---

[Previous: Area Charts](07-area-charts.md) | [Back to Documentation](../README.md)
