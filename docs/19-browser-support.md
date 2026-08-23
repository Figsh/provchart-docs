# Browser Support

Browser compatibility for ProvChart.

## Minimum Requirements

ProvChart requires `clip-path: polygon()` support.

| Browser | Minimum Version |
|---------|-----------------|
| Chrome | 88+ |
| Firefox | 97+ |
| Safari | 13.1+ |
| Edge | 88+ |
| iOS Safari | 13.1+ |
| Chrome Android | 88+ |
| Samsung Internet | 15+ |

## Feature Support

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| `clip-path: polygon()` | 88+ | 97+ | 13.1+ | 88+ |
| CSS Custom Properties | 49+ | 31+ | 9.1+ | 15+ |
| `color-mix()` | 111+ | 113+ | 16.2+ | 111+ |

## Progressive Enhancement

Charts degrade gracefully:

- Without `clip-path`: Chart shape not visible
- With `clip-path`: Full chart rendering

## Testing

Test your target browsers:

```html
<div style="clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);">
  Clip-path supported
</div>
```

## Polyfills

No polyfills are provided. For older browsers:

- Use fallback content
- Provide data tables
- Consider alternative charting libraries

## Recommendations

- Use [Can I Use](https://caniuse.com/clip-path) to check support
- Test on real devices
- Provide fallbacks for critical content

---

[Previous: Accessibility](18-accessibility.md) | [Back to Documentation](../README.md)
