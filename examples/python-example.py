"""
ProvChart Developer API — Python example
Docs: https://chart.devtem.org/docs#dev-api-overview

Usage:
    PROVCHART_API_KEY=pc_live_xxxx python python-example.py
"""

import os
import requests

API_URL = "https://provchart-api.devtem.org/api/v1/generate"


def generate_chart():
    res = requests.post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "X-API-Key": os.environ["PROVCHART_API_KEY"],
        },
        json={
            "type": "bar",
            "series": [
                {"name": "2025", "color": "#8b7bff", "points": [40, 55, 48, 70]},
                {"name": "2026", "color": "#4fd8c4", "points": [35, 50, 62, 58]},
            ],
            "axisX": ["Q1", "Q2", "Q3", "Q4"],
        },
    )

    data = res.json()

    if not data.get("success"):
        # See error codes: INVALID_API_KEY, SUBSCRIPTION_REQUIRED, MONTHLY_LIMIT_REACHED
        raise RuntimeError(f"ProvChart error [{data.get('code')}]: {data.get('error')}")

    # data["html"] + data["css"] — static output, no chart-library runtime needed
    return data


if __name__ == "__main__":
    result = generate_chart()
    print(result["html"])
    print(result["css"])


# SVG variant — for READMEs, docs pages, anywhere a <style> block isn't an option
#
# def generate_svg():
#     res = requests.post(
#         "https://provchart-api.devtem.org/api/v1/generate-svg",
#         headers={"X-API-Key": os.environ["PROVCHART_API_KEY"]},
#         json={
#             "type": "area",
#             "series": [{"name": "Views", "color": "#4fd8c4", "points": [10, 25, 40, 55]}],
#             "axisX": ["Mon", "Tue", "Wed", "Thu"],
#             "width": 640,
#             "height": 240,
#         },
#     )
#     return res.json()["dataUri"]
