# Grid and Axes

Adding grid lines and axis labels to charts.

## Grid Lines

```scss
@st-chart-grid(.chart-grid, 10, 7)
```

Parameters:
- `.chart-grid` — CSS class name
- `10` — Number of horizontal grid lines
- `7` — Number of vertical grid lines

```html
<div class="chart">
  <div class="chart-fill"></div>
  <div class="chart-line"></div>
  <div class="chart-grid"></div>
</div>
```

## X-Axis Labels

```scss
@st-chart-axis-x(.x-axis)
```

```html
<div class="x-axis">
  <span>Mon</span>
  <span>Tue</span>
  <span>Wed</span>
  <span>Thu</span>
  <span>Fri</span>
  <span>Sat</span>
  <span>Sun</span>
</div>
```

## Y-Axis Labels

```scss
@st-chart-axis-y(.y-axis)
```

```html
<div class="y-axis">
  <span>0</span>
  <span>10</span>
  <span>20</span>
  <span>30</span>
  <span>40</span>
  <span>50</span>
  <span>60</span>
  <span>70</span>
  <span>80</span>
  <span>90</span>
  <span>100</span>
</div>
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chart with Grid</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)
    @st-chart-grid(.chart-grid, 10, 7)
    @st-chart-axis-x(.x-axis)
    @st-chart-axis-y(.y-axis)

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
  </style>
</head>
<body>
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
    <div class="chart-grid"></div>
  </div>
  <div class="x-axis">
    <span>Mon</span>
    <span>Tue</span>
    <span>Wed</span>
    <span>Thu</span>
    <span>Fri</span>
    <span>Sat</span>
    <span>Sun</span>
  </div>
</body>
</html>
```

## Next Steps

- [Multiple Series](10-multiple-series.md)

---

[Previous: Points and Dots](08-points-and-dots.md) | [Back to Documentation](../README.md)
