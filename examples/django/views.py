"""
Django views for ProvChart integration.
"""

from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def chart_data(request):
    """Return chart data as JSON."""
    points = [20, 35, 48, 66, 58, 72, 80, 95]
    labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Now']
    return JsonResponse({
        'points': points,
        'labels': labels
    })


@require_GET
def revenue_data(request):
    """Return revenue data as JSON."""
    points = [1200, 1800, 2400, 1600, 2100, 2800, 3200, 2900]
    return JsonResponse({
        'points': points,
        'currency': 'USD'
    })
