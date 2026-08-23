# JavaScript Integration

Using JavaScript with ProvChart for dynamic updates.

## Core Concept

ProvChart is 100% CSS. JavaScript is entirely optional — it only writes CSS custom properties.

## Basic Update Function

```javascript
function updateChart(element, points) {
  const vars = points.map((v, i) => `--st-p${i + 1}: ${100 - v}%`).join('; ');
  element.style.cssText = vars;
}
```

## Usage

```javascript
const chart = document.querySelector('.chart');
updateChart(chart, [20, 35, 48, 66, 58, 72, 80, 95]);
```

## Full Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dynamic Chart</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)
    @st-chart-dot(.chart-dot, 70, 60)

    .chart {
      width: 100%;
      height: 200px;
      border-radius: 20px;
      position: relative;
      overflow: hidden;
      background: var(--st-surface);
      @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
    }

    .chart-fill, .chart-line {
      transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .chart-dot {
      position: relative;
      overflow: visible;
    }
  </style>
</head>
<body>
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
    <div class="chart-dot" data-point="$405.67"></div>
  </div>

  <button onclick="randomize()">Update Data</button>

  <script>
    const chartFill = document.querySelector('.chart-fill');
    const chartLine = document.querySelector('.chart-line');

    function normalize(n) {
      return (100 - n) + '%';
    }

    function update(points) {
      const vars = points.map((v, i) => `--st-p${i + 1}: ${normalize(v)}`).join('; ');
      chartFill.style.cssText = vars;
      chartLine.style.cssText = vars;
    }

    function randomize() {
      const points = Array.from({ length: 8 }, () => Math.floor(Math.random() * 80) + 10);
      update(points);
    }
  </script>
</body>
</html>
```

## Fetching Data from API

```javascript
async function loadChartData() {
  const res = await fetch('/api/chart-data');
  const { points } = await res.json();
  update(points);
}
```

## Periodic Updates

```javascript
setInterval(async () => {
  const res = await fetch('/api/chart-data');
  const { points } = await res.json();
  update(points);
}, 30000);
```

## WebSocket Updates

```javascript
const socket = new WebSocket('wss://your-api.com/data/stream');

socket.onmessage = (event) => {
  const { points } = JSON.parse(event.data);
  update(points);
};
```

## Normalizing Data

```javascript
function normalizePoint(value, min, max) {
  const normalized = ((value - min) / (max - min)) * 100;
  return normalized.toFixed(2) + '%';
}

function updateFromRawData(element, rawData) {
  const min = Math.min(...rawData);
  const max = Math.max(...rawData);
  const vars = rawData.map((v, i) => `--st-p${i + 1}: ${normalizePoint(v, min, max)}`).join('; ');
  element.style.cssText = vars;
}
```

## Next Steps

- [Backend Integration](14-backend-integration.md)
- [Live Data](15-live-data.md)

---

[Previous: Responsive Charts](12-responsive-charts.md) | [Back to Documentation](../README.md)
