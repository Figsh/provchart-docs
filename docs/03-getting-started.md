# Getting Started

This guide walks you through creating your first ProvChart chart.

## Prerequisites

A modern browser with `clip-path` support (Chrome 88+, Firefox 97+, Safari 13.1+, Edge 88+).

## Step 1: Create an HTML File

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My First Chart</title>

  <!-- FSCSS Runtime (for development) -->
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)

    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)
  </style>
</head>
<body>

</body>
</html>
```

## Step 2: Add Chart Components

Register the chart fill and line components in your `<style>` block:

```scss
@st-chart-fill(.chart-fill)
@st-chart-line(.chart-line)
```

## Step 3: Create the Chart Container

Add the chart HTML and style it:

```html
<div class="chart">
  <div class="chart-fill"></div>
  <div class="chart-line"></div>
</div>
```

```scss
.chart {
  width: 300px;
  height: 200px;
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  background: var(--st-surface);

  @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
}
```

## Step 4: Add Line Styling

```scss
.chart-line {
  @st-chart-line-width(2px);
  filter: drop-shadow(0 0 8px var(--st-accent));
}
```

## Complete Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>First Chart</title>
  <script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>

  <style>
    @import((*) from st-core)

    @st-root()
    @st-container(body)
    @st-chart-fill(.chart-fill)
    @st-chart-line(.chart-line)

    .chart {
      width: 300px;
      height: 200px;
      border-radius: 20px;
      position: relative;
      overflow: hidden;
      background: var(--st-surface);
      @st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
    }

    .chart-line {
      @st-chart-line-width(2px);
      filter: drop-shadow(0 0 8px var(--st-accent));
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

## What Just Happened?

1. `@st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)` compiled to 8 CSS variables (`--st-p1` through `--st-p8`)
2. `.chart-fill` uses `clip-path: polygon()` with those variables to draw the area
3. `.chart-line` draws a thin polygon stroke on top
4. The browser renders everything as pure CSS

## Next Steps

- [Core Concepts](04-core-concepts.md)
- [Chart Data](05-chart-data.md)

---

[Previous: Installation](02-installation.md) | [Back to Documentation](../README.md)
