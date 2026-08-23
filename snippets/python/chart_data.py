"""
Python helper for generating ProvChart data.
"""


def normalize_points(values):
    """
    Normalize a list of values to 0-100 scale.

    Args:
        values: List of numeric values

    Returns:
        List of normalized values (0-100)
    """
    if not values:
        return [0] * 8

    min_val = min(values)
    max_val = max(values)

    if max_val == min_val:
        return [50] * len(values)

    return [((v - min_val) / (max_val - min_val)) * 100 for v in values]


def prepare_chart_data(raw_data, labels=None):
    """
    Prepare data for ProvChart.

    Args:
        raw_data: List of 8 numeric values
        labels: Optional list of 8 labels for x-axis

    Returns:
        Dictionary with points and labels
    """
    points = normalize_points(raw_data)[:8]

    if labels is None:
        labels = [f"Point {i+1}" for i in range(len(points))]

    return {
        "points": points,
        "labels": labels[:8]
    }
