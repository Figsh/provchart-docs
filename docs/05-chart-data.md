# Chart Data

How data flows into ProvChart charts.

## Data Format

ProvChart accepts 8 numeric data points on a 0-100 scale:

```scss
@st-chart-points(20, 35, 48, 66, 58, 72, 80, 95)
```

- **Minimum**: 0 (bottom of chart)
- **Maximum**: 100 (top of chart)
- **Count**: Exactly 8 points

## CSS Variable Mapping

Each value maps to a CSS custom property:

| Argument | CSS Variable | X Position |
|----------|--------------|------------|
| Point 1 | `--st-p1` | 0% (leftmost) |
| Point 2 | `--st-p2` | 14% |
| Point 3 | `--st-p3` | 28% |
| Point 4 | `--st-p4` | 42% |
| Point 5 | `--st-p5` | 57% |
| Point 6 | `--st-p6` | 71% |
| Point 7 | `--st-p7` | 85% |
| Point 8 | `--st-p8` | 100% (rightmost) |

## Value Inversion

Values are inverted internally:

```
Input value:  35
CSS variable: 65% (100 - 35 = 65)
```

This is because CSS coordinates go top-down (0% = top), but chart values go bottom-up (0 = bottom).

## Normalizing Real Data

If your data isn't on a 0-100 scale, normalize it first:

```javascript
function normalizePoint(value, min, max) {
  const normalized = ((value - min) / (max - min)) * 100;
  return `${normalized.toFixed(2)}%`;
}

// Example: Revenue data
const revenue = [1200, 1800, 2400, 1600, 2100, 2800, 3200, 2900];
const min = Math.min(...revenue);  // 1200
const max = Math.max(...revenue);  // 3200

const points = revenue.map(v => normalizePoint(v, min, max));
// ["0%", "30%", "60%", "20%", "45%", "80%", "100%", "85%"]
```

## Multiple Charts

Each chart container has its own independent data:

```scss
.chart-revenue {
  @st-chart-points(20, 35, 48, 66, 58, 72, 80, 95)
}

.chart-users {
  @st-chart-points(40, 55, 48, 62, 58, 75, 58, 70)
}
```

## Default Values

If no `@st-chart-points` is set, the chart uses default values from `@st-root`. This prevents the chart from being invisible before data loads.

## Data Limitations

- **Maximum 8 points** per chart
- **Fixed X positions** (cannot customize)
- **Single Y scale** (0-100)

For more complex data, consider:

- Multiple charts
- The ProvChart API (supports more points)
- Alternative charting libraries

## Next Steps

- [Line Charts](06-line-charts.md)
- [Area Charts](07-area-charts.md)

---

[Previous: Core Concepts](04-core-concepts.md) | [Back to Documentation](../README.md)
