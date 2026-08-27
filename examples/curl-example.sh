#!/usr/bin/env bash
# ProvChart Developer API — curl examples
# Docs: https://chart.devtem.org/docs#dev-api-overview
#
# Usage:
#   export PROVCHART_API_KEY=pc_live_xxxx
#   ./curl-example.sh

# HTML + CSS output
curl -s -X POST "https://provchart-api.devtem.org/api/v1/generate" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $PROVCHART_API_KEY" \
  -d '{
    "type": "line",
    "series": [
      { "name": "Revenue", "color": "#8b7bff", "points": [20, 35, 48, 66] }
    ],
    "axisX": ["Jan", "Feb", "Mar", "Apr"]
  }'

# SVG output — for READMEs, docs pages, anywhere a <style> block isn't an option
curl -s -X POST "https://provchart-api.devtem.org/api/v1/generate-svg" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $PROVCHART_API_KEY" \
  -d '{
    "type": "area",
    "series": [
      { "name": "Views", "color": "#4fd8c4", "points": [10, 25, 40, 55] }
    ],
    "axisX": ["Mon", "Tue", "Wed", "Thu"],
    "width": 640,
    "height": 240
  }'

# Check usage / quota
curl -s "https://provchart-api.devtem.org/api/v1/usage" \
  -H "X-API-Key: $PROVCHART_API_KEY"
