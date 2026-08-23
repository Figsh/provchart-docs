# Troubleshooting

Common issues and solutions.

## Chart Not Showing

### Problem: Blank chart area

**Causes:**

1. FSCSS runtime not loaded
2. `clip-path` not supported
3. Missing chart elements

**Solutions:**

```html
<!-- Ensure FSCSS runtime is loaded -->
<script src="https://cdn.jsdelivr.net/npm/fscss@1.1.24/exec.min.js" async></script>
```

```scss
// Ensure chart has proper positioning
.chart {
  position: relative;
  overflow: hidden;
}
```

```html
<!-- Ensure chart elements exist -->
<div class="chart">
  <div class="chart-fill"></div>
  <div class="chart-line"></div>
</div>
```

## Line Not Visible

### Problem: Area shows but line doesn't

**Solution:**

```scss
.chart-line {
  @st-chart-line-width(2px);
}
```

## Colors Not Applying

### Problem: Custom colors not showing

**Solution:**

```scss
// Override at :root
:root {
  --st-accent: #8b7bff;
}

// Or locally
.chart-line {
  background: #8b7bff;
}
```

## Transitions Not Working

### Problem: Data updates not animating

**Solution:**

```scss
.chart-fill, .chart-line {
  transition: clip-path 0.9s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## API Key Errors

### Problem: ProvChart API returns error

**Solution:**

```javascript
// Check API key
const res = await fetch("https://provchart-api.devtem.org/api/v1/generate", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY" // Replace with actual key
  },
  body: JSON.stringify({ /* ... */ })
});

const data = await res.json();
if (!data.success) {
  console.error("API Error:", data.error);
}
```

## Compilation Errors

### Problem: FSCSS compilation fails

**Solution:**

```bash
# Ensure FSCSS is installed
npm install -g fscss

# Check version (requires 1.1.24+)
fscss --version

# Compile with verbose output
fscss style.fscss style.css --verbose
```

## Responsive Issues

### Problem: Chart not resizing

**Solution:**

```scss
.chart {
  width: 100%; /* Use percentage */
  height: 200px; /* Fixed height */
}
```

## Performance Issues

### Problem: Slow rendering

**Solutions:**

- Use compiled CSS instead of CDN runtime
- Minimize DOM complexity
- Use CSS transitions instead of JavaScript animations

---

[Previous: Browser Support](19-browser-support.md) | [Back to Documentation](../README.md)
