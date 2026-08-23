"""
Example Python backend for ProvChart.
Returns chart data as JSON for frontend rendering.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/chart-data')
def chart_data():
    """Return chart data points."""
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Now']
    return jsonify({
        'points': points,
        'labels': labels
    })


@app.route('/api/revenue')
def revenue():
    """Return revenue data."""
    points = [1200, 1800, 2400, 1600, 2100, 2800, 3200, 2900]
    return jsonify({
        'points': points,
        'currency': 'USD'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
