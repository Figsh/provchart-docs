"""
Flask app with ProvChart integration.
Serves API endpoints and HTML with charts.
"""

from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flask + ProvChart</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)

    .chart {
      width: 100%;
      max-width: 500px;
      height: 200px;
      border-radius: 20px;
      position: relative;
      overflow: hidden;
      background: var(--st-surface);
    }

    .chart-fill, .chart-line {
      transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
    }
  </style>
</head>
<body>
  <h1>Flask + ProvChart Dashboard</h1>

  <div class="chart" id="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
  </div>

  <script>
    async function loadChart() {
      const res = await fetch('/api/chart-data');
      const { points } = await res.json();

      const chartFill = document.querySelector('.chart-fill');
      const chartLine = document.querySelector('.chart-line');

      const vars = points.map((v, i) => `--st-p${i + 1}: ${100 - v}%`).join('; ');
      chartFill.style.cssText = vars;
      chartLine.style.cssText = vars;
    }

    loadChart();
  </script>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/chart-data')
def chart_data():
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    return jsonify({'points': points})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
