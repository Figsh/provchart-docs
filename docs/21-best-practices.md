# Best Practices

Recommended patterns for ProvChart.

## Production Deployment

### Use Compiled CSS

```bash
fscss style.fscss style.css
```

Ship the `.css` file. No FSCSS runtime needed.

### Minimize Bundle

- Only import what you need
- Remove unused components
- Tree-shake if using a bundler

## Data Management

### Normalize Data

```javascript
function normalizePoint(value, min, max) {
  return ((value - min) / (max - min)) * 100;
}
```

### Use Default Values

```scss
@st-chart-points(20, 25, 21, 37, 30, 60, 27, 50)
```

Provides fallback before real data loads.

## Styling

### Use Design Tokens

```scss
:root {
  --st-accent: #8b7bff;
}
```

### Local Overrides

```scss
.chart-specific {
  --st-accent: #c4a8ff;
}
```

## Performance

### Transitions

```scss
.chart-fill, .chart-line {
  transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Avoid JavaScript Animation

Let CSS handle transitions.

## Accessibility

### Always Provide Alternatives

```html
<div role="img" aria-label="Revenue chart">
  <div class="chart">...</div>
</div>
<table class="sr-only">...</table>
```

### Respect Reduced Motion

```scss
@media (prefers-reduced-motion: reduce) {
  .chart-fill, .chart-line {
    transition: none;
  }
}
```

## Code Organization

### Separate Concerns

```
styles/
  tokens.fscss      # Design tokens
  charts.fscss      # Chart components
  dashboard.fscss   # Dashboard layout
```

### Use Consistent Naming

```scss
@st-chart-fill(.chart-fill)
@st-chart-line(.chart-line)
@st-chart-dot(.chart-dot)
```

## Testing

### Visual Regression

- Screenshot charts before/after changes
- Test across browsers
- Verify responsive behavior

### Data Testing

- Test with edge cases (0, 100, empty)
- Verify normalization
- Check API error handling

---

[Previous: Troubleshooting](20-troubleshooting.md) | [Back to Documentation](../README.md)
