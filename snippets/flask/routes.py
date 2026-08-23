"""
Flask routes for ProvChart data API.
"""

from flask import Blueprint, jsonify

chart_bp = Blueprint('chart', __name__)


@chart_bp.route('/api/chart-data')
def chart_data():
    """Return chart data points."""
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Now']
    return jsonify({
        'points': points,
        'labels': labels
    })


@chart_bp.route('/api/revenue')
def revenue():
    """Return revenue data."""
    points = [1200, 1800, 2400, 1600, 2100, 2800, 3200, 2900]
    return jsonify({
        'points': points,
        'currency': 'USD'
    })
