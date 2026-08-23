# Dashboards

Building complete dashboards with ProvChart.

## Dashboard Components

ProvChart provides these components:

| Component | Mixin | Purpose |
|-----------|-------|---------|
| Stat Card | `@st-stat-card` | Label / value / delta badge |
| Line Chart | `@st-chart-line` | Line stroke |
| Area Fill | `@st-chart-fill` | Gradient area fill |
| Data Points | `@st-chart-dots` | Auto-positioned markers |
| Grid | `@st-chart-grid` | Background grid lines |
| X-Axis | `@st-chart-axis-x` | Horizontal labels |
| Y-Axis | `@st-chart-axis-y` | Vertical labels |
| Category Bar | `@st-cat-bar-fill` | Progress bar fill |

## Full Dashboard Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-stat-card(.stat-card)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)
    @st-chart-dot(.chart-dot, 71, 75)
    @st-chart-grid(.chart-grid, 8, 7)
    @st-chart-axis-x(.x-axis)
    @st-cat-bar-fill(.bar-fill, 0)

    .chart {
      width: 100%;
      height: 200px;
      border-radius: var(--st-radius-lg);
      position: relative;
      overflow: hidden;
      background: var(--st-surface);
      @st-chart-points(40, 55, 48, 62, 58, 75, 58, 70)
    }

    .chart-line {
      @st-chart-line-width(2px);
      filter: drop-shadow(0 0 8px var(--st-accent));
    }

    .chart-fill { opacity: 0.85; }

    .stat-row {
      display: flex;
      gap: 16px;
    }

    .source-row {
      margin-bottom: 8px;
    }

    .source-label {
      display: flex;
      justify-content: space-between;
      margin-bottom: 4px;
    }

    .bar-track {
      height: 8px;
      background: var(--st-surface);
      border-radius: 4px;
      overflow: hidden;
    }
  </style>
</head>
<body>
  <div class="wrapper">
    <div>
      <h2>Analytics</h2>
      <p>Last 8 days</p>
    </div>

    <div class="stat-row">
      <div class="stat-card">
        <div class="st-stat-label">TOTAL VISITORS</div>
        <div class="st-stat-value">2,148</div>
        <div class="st-stat-delta up">+12.4% vs last week</div>
      </div>
      <div class="stat-card">
        <div class="st-stat-label">UNIQUE VISITORS</div>
        <div class="st-stat-value">1,602</div>
        <div class="st-stat-delta up">+8.9% vs last week</div>
      </div>
    </div>

    <div class="chart">
      <div class="chart-fill"></div>
      <div class="chart-line"></div>
      <div class="chart-dot" data-point="82 visits"></div>
      <div class="chart-grid"></div>
    </div>

    <div class="x-axis">
      <span>-6d</span>
      <span>-5d</span>
      <span>-4d</span>
      <span>-3d</span>
      <span>-2d</span>
      <span>-1d</span>
      <span>10h</span>
    </div>

    <div class="stat-card sources">
      <div class="st-stat-label">TOP TRAFFIC SOURCES</div>

      <div class="source-row">
        <div class="source-label"><span>Direct</span><span>82%</span></div>
        <div class="bar-track"><div class="bar-fill direct"></div></div>
      </div>
      <div class="source-row">
        <div class="source-label"><span>Google</span><span>64%</span></div>
        <div class="bar-track"><div class="bar-fill google"></div></div>
      </div>
      <div class="source-row">
        <div class="source-label"><span>GitHub</span><span>41%</span></div>
        <div class="bar-track"><div class="bar-fill github"></div></div>
      </div>
    </div>
  </div>
</body>
</html>
```

## Next Steps

- [Performance](17-performance.md)

---

[Previous: Live Data](15-live-data.md) | [Back to Documentation](../README.md)
