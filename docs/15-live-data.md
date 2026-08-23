# Live Data

Real-time and polling data updates.

## Polling

Fetch data at regular intervals:

```javascript
async function poll() {
  const res = await fetch('/api/chart-data');
  const { points } = await res.json();
  update(points);
}

poll();
setInterval(poll, 30000); // Every 30 seconds
```

## WebSocket

For real-time streaming:

```javascript
const socket = new WebSocket('wss://your-api.com/data/stream');

socket.onmessage = (event) => {
  const { points } = JSON.parse(event.data);
  update(points);
};
```

## Smooth Transitions

Add CSS transitions for smooth animation:

```scss
.chart-fill, .chart-line {
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
  <title>Live Chart</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
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

    .chart-fill, .chart-line {
      transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
    }
  </style>
</head>
<body>
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
  </div>

  <script>
    const chartFill = document.querySelector('.chart-fill');
    const chartLine = document.querySelector('.chart-line');

    function update(points) {
      const vars = points.map((v, i) => `--st-p${i + 1}: ${100 - v}%`).join('; ');
      chartFill.style.cssText = vars;
      chartLine.style.cssText = vars;
    }

    async function poll() {
      const res = await fetch('/api/chart-data');
      const { points } = await res.json();
      update(points);
    }

    poll();
    setInterval(poll, 30000);
  </script>
</body>
</html>
```

## Performance Considerations

- CSS transitions are compositor-accelerated (GPU)
- Changing CSS variables doesn't touch DOM structure
- No layout thrash or repaints of surrounding content

## Next Steps

- [Dashboards](16-dashboards.md)

---

[Previous: Backend Integration](14-backend-integration.md) | [Back to Documentation](../README.md)
