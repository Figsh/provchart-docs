# Responsive Charts

Making ProvChart charts responsive.

## Fluid Width

Set width to 100% and use a fixed height:

```scss
.chart {
  width: 100%;
  height: 200px;
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  background: var(--st-surface);
}
```

## Responsive Height

Use viewport units or media queries:

```scss
.chart {
  width: 100%;
  height: 30vh;
  min-height: 150px;
  max-height: 300px;
}
```

## Media Queries

```scss
.chart {
  width: 100%;
  height: 200px;
}

@media (min-width: 768px) {
  .chart {
    height: 300px;
  }
}

@media (min-width: 1024px) {
  .chart {
    height: 400px;
  }
}
```

## Container-Based Sizing

```scss
.chart-container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

.chart {
  width: 100%;
  height: 200px;
}
```

## Phone Frame

Use `@st-phone` for device mockups:

```scss
@st-phone(.phone-frame)
```

```html
<div class="phone-frame">
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
  </div>
</div>
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Chart</title>
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

    @media (min-width: 768px) {
      .chart {
        height: 300px;
      }
    }
  </style>
</head>
<body>
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
  </div>
</body>
</html>
```

## Next Steps

- [JavaScript Integration](13-javascript.md)

---

[Previous: Customization](11-customization.md) | [Back to Documentation](../README.md)
