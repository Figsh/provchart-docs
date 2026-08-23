# Accessibility

Accessibility considerations for ProvChart charts.

## Semantic HTML

Use proper HTML structure:

```html
<div role="img" aria-label="Revenue chart showing upward trend">
  <div class="chart">
    <div class="chart-fill"></div>
    <div class="chart-line"></div>
  </div>
</div>
```

## Text Alternatives

Provide data tables as alternatives:

```html
<div role="img" aria-label="Weekly revenue chart">
  <div class="chart">...</div>
</div>

<table class="sr-only">
  <caption>Weekly Revenue</caption>
  <thead>
    <tr>
      <th>Day</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Mon</td><td>$20</td></tr>
    <tr><td>Tue</td><td>$35</td></tr>
    <!-- ... -->
  </tbody>
</table>
```

## Screen Reader Only

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## Color Contrast

Ensure sufficient contrast:

- Text: 4.5:1 ratio minimum
- Large text: 3:1 ratio minimum
- Chart elements: Use patterns or labels in addition to color

## Keyboard Accessibility

Charts are visual-only. Ensure:

- Data is available in accessible format
- Interactive elements (buttons, links) are keyboard accessible
- Focus indicators are visible

## Reduced Motion

```scss
@media (prefers-reduced-motion: reduce) {
  .chart-fill, .chart-line {
    transition: none;
  }
}
```

## ARIA Labels

```html
<div class="chart"
     role="img"
     aria-label="Line chart showing revenue growth from January to August"
     aria-describedby="chart-desc">
  <div class="chart-fill"></div>
  <div class="chart-line"></div>
</div>
<div id="chart-desc" class="sr-only">
  Revenue increased from $20,000 in January to $95,000 in August.
</div>
```

## Best Practices

1. Always provide text alternatives
2. Use semantic HTML
3. Ensure color is not the only way to convey information
4. Test with screen readers
5. Respect reduced motion preferences
6. Provide data tables for complex data

---

[Previous: Performance](17-performance.md) | [Back to Documentation](../README.md)
