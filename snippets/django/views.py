"""
Django views for ProvChart data API.
"""

from django.http import JsonResponse


def chart_data(request):
    """Return chart data points."""
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Now']
    return JsonResponse({
        'points': points,
        'labels': labels
    })


def revenue_data(request):
    """Return revenue data."""
    points = [1200, 1800, 2400, 1600, 2100, 2800, 3200, 2900]
    return JsonResponse({
        'points': points,
        'currency': 'USD'
    })
