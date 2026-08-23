# Core Concepts

Understanding how ProvChart renders charts with pure CSS.

## The Three Pillars

ProvChart uses three browser-native features:

| Feature | Purpose |
|---------|---------|
| `clip-path: polygon()` | Draws the chart shape |
| CSS custom properties | Stores data points |
| FSCSS mixins | Generates structure at compile time |

## How Data Becomes a Shape

### 1. Data Points

You provide 8 Y values (0-100 scale):

```
@st-chart-points(20, 35, 48, 66, 58, 72, 80, 95)
```

### 2. Compile to CSS Variables

FSCSS compiles this to:

```css
.chart {
  --st-p1: 80%;   /* 100 - 20 = 80 */
  --st-p2: 65%;   /* 100 - 35 = 65 */
  --st-p3: 52%;   /* 100 - 48 = 52 */
  --st-p4: 34%;   /* 100 - 66 = 34 */
  --st-p5: 42%;   /* 100 - 58 = 42 */
  --st-p6: 28%;   /* 100 - 72 = 28 */
  --st-p7: 20%;   /* 100 - 80 = 20 */
  --st-p8: 5%;    /* 100 - 95 = 5  */
}
```

Values are inverted because CSS coordinates go top-down.

### 3. Browser Renders Polygon

The `.chart-fill` element has a static `clip-path` rule:

```css
.chart-fill {
  clip-path: polygon(
    0% var(--st-p1),
    14% var(--st-p2),
    28% var(--st-p3),
    42% var(--st-p4),
    57% var(--st-p5),
    71% var(--st-p6),
    85% var(--st-p7),
    100% var(--st-p8),
    100% 100%,
    0% 100%
  );
}
```

The browser resolves the variables and paints the shape.

## X-Axis Stops

The 8 data points map to fixed X positions:

| Point | X Position |
|-------|------------|
| `--st-p1` | 0% |
| `--st-p2` | 14% |
| `--st-p3` | 28% |
| `--st-p4` | 42% |
| `--st-p5` | 57% |
| `--st-p6` | 71% |
| `--st-p7` | 85% |
| `--st-p8` | 100% |

## Y-Axis Scale

- Values range from 0 to 100
- Higher values = higher on the chart
- Internally converted to CSS percentages (inverted)

## Component Hierarchy

```
.chart (container)
  ├── @st-chart-points (sets --st-p1 through --st-p8)
  ├── .chart-fill (area fill via clip-path)
  ├── .chart-line (line stroke via clip-path)
  ├── .chart-dot (optional single point)
  ├── .chart-dots (optional all 8 points)
  └── .chart-grid (optional background grid)
```

All child elements inherit the CSS variables from the parent `.chart`.

## Three Modes

### Development (CDN Runtime)

```html
<script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>
<style>
  @import((*) from st-core)
  /* FSCSS syntax compiled in-browser */
</style>
```

### Production (Compiled)

```bash
fscss style.fscss style.css
```

Output is standard CSS. No FSCSS runtime needed.

### Runtime (JavaScript)

```javascript
// Update chart via CSS variables
chart.style.setProperty('--st-p1', '40%');
```

## Mental Model

- **FSCSS** owns the structure and shape (compile time)
- **JavaScript** owns the numbers (optional, runtime)
- **CSS** owns the motion (transitions, rendering)

## Next Steps

- [Chart Data](05-chart-data.md)

---

[Previous: Getting Started](03-getting-started.md) | [Back to Documentation](../README.md)
