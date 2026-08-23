# Backend Integration

Using any backend language to provide data for ProvChart.

## Architecture

```
Backend (Python/Node/Go/etc.)
  → Calculate/query data
  → Return JSON
  → Frontend receives JSON
  → JavaScript sets CSS variables
  → ProvChart renders visualization
```

## Important

**ProvChart is a frontend CSS technology.** There are no native Python, Node.js, or other backend SDKs. Backends provide data as JSON; the frontend renders charts.

## Python + Flask Example

### Backend

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/chart-data')
def chart_data():
    # Query your database or calculate
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    return jsonify({
        'points': points,
        'labels': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Now']
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Frontend

```html
<script>
  async function loadChart() {
    const res = await fetch('/api/chart-data');
    const { points } = await res.json();

    const chart = document.querySelector('.chart');
    const vars = points.map((v, i) => `--st-p${i + 1}: ${100 - v}%`).join('; ');
    chart.style.cssText = vars;
  }

  loadChart();
</script>
```

## Node.js + Express Example

### Backend

```javascript
const express = require('express');
const app = express();

app.get('/api/chart-data', (req, res) => {
  const points = [20, 35, 48, 66, 58, 72, 80, 95];
  res.json({ points });
});

app.listen(3000);
```

### Frontend

```html
<script>
  async function loadChart() {
    const res = await fetch('/api/chart-data');
    const { points } = await res.json();

    const chart = document.querySelector('.chart');
    const vars = points.map((v, i) => `--st-p${i + 1}: ${100 - v}%`).join('; ');
    chart.style.cssText = vars;
  }

  loadChart();
</script>
```

## Django Example

### views.py

```python
from django.http import JsonResponse

def chart_data(request):
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    return JsonResponse({'points': points})
```

### urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('api/chart-data', views.chart_data),
]
```

## FastAPI Example

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/chart-data")
def chart_data():
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    return {"points": points}
```

## ProvChart API (Hosted)

For more chart types, use the ProvChart Developer API:

```javascript
const res = await fetch("https://provchart-api.devtem.org/api/v1/generate", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY"
  },
  body: JSON.stringify({
    type: "line",
    series: [
      { name: "Revenue", color: "#8b7bff", points: [20, 35, 48, 66] }
    ],
    axisX: ["Jan", "Feb", "Mar", "Apr"]
  })
});

const data = await res.json();
if (data.success) {
  document.getElementById("chart-container").innerHTML = data.html;
  document.querySelector("head").insertAdjacentHTML(
    "beforeend",
    `<style>${data.css}</style>`
  );
}
```

## Next Steps

- [Live Data](15-live-data.md)

---

[Previous: JavaScript Integration](13-javascript.md) | [Back to Documentation](../README.md)
