# 02 · Integration

ProvChart has nothing to `npm install` for **paint**. Integration means:

1. Obtain an API key  
2. Call the generate API (or use the builder and paste output)  
3. Inject **HTML + CSS** (or **SVG**) into your page  
4. Optionally load **provchart-runtime** for tooltips / motion  

There is no required client chart-library bundle.

| Resource | URL |
|----------|-----|
| Dashboard / keys | https://chart.devtem.org/dashboard |
| Generate (HTML/CSS) | `POST https://provchart-api.devtem.org/api/v1/generate` |
| Generate (SVG) | `POST https://provchart-api.devtem.org/api/v1/generate-svg` |
| Live demo | https://chart.devtem.org/demo |
| Runtime (optional) | https://www.npmjs.com/package/provchart-runtime |

← [01 · Introduction](./01-introduction.md) · [Next: Getting started →](./03-getting-started.md)

---

## 1. API key

1. Sign in at [chart.devtem.org](https://chart.devtem.org)  
2. Open **Dashboard → Developer API** (or **API keys**)  
3. Create a key  

Use the header:

```http
X-API-Key: YOUR_API_KEY
```

**Never commit live keys.** Prefer env vars (`PROVCHART_API_KEY`) on servers and CI. In public snippets use `YOUR_API_KEY`.

Signed-up **free** accounts include a small monthly test quota. Pro / Business raise limits. HTML and SVG generations share the same pool.

---

## 2. HTML + CSS integration (apps & sites)

### Request

```javascript
const res = await fetch("https://provchart-api.devtem.org/api/v1/generate", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": process.env.PROVCHART_API_KEY, // or YOUR_API_KEY in demos
  },
  body: JSON.stringify({
    type: "line",
    theme: "midnight",
    series: [
      { name: "Revenue", color: "#8b7bff", points: [20, 35, 48, 42, 58] },
    ],
    axisX: ["Mon", "Tue", "Wed", "Thu", "Fri"],
  }),
});

const data = await res.json();
if (!data.success) {
  throw new Error(data.error || data.code || "Generate failed");
}
```

### Inject

```javascript
// CSS once (or merge into your bundle)
let style = document.getElementById("provchart-style");
if (!style) {
  style = document.createElement("style");
  style.id = "provchart-style";
  document.head.appendChild(style);
}
style.textContent = (style.textContent || "") + "\n" + (data.css || "");

// HTML
document.getElementById("chart").innerHTML = data.html || "";
```

```html
<div id="chart"></div>
```

Successful HTML roots typically include `data-provchart="…"`. Scoped classes/variables avoid collisions when several charts share a page.

### Server-side / SSG

Call the API in **CI or getStaticProps / loaders**, then write `html` + `css` into the template. The published page does not need to call the API on every visitor request (unless you want live regeneration).

---

## 3. SVG integration (README, docs, Markdown)

```javascript
const res = await fetch("https://provchart-api.devtem.org/api/v1/generate-svg", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": process.env.PROVCHART_API_KEY,
  },
  body: JSON.stringify({
    type: "area",
    width: 640,
    height: 280,
    series: [
      { name: "Views", color: "#8b7bff", points: [20, 35, 42, 38, 55, 62, 58] },
    ],
    axisX: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
  }),
});

const data = await res.json();
// data.svg  — full <svg>…</svg>
// data.dataUri — optional data:image/svg+xml;… for <img src>
```

**Recommended for GitHub:** write `data.svg` to a file and reference it:

```markdown
![Views](./charts/views.svg)
```

Long `dataUri` values can be awkward in some Markdown hosts. See the [charts in Markdown](https://chart.devtem.org/guides/charts-in-markdown) guide on the site.

---

## 4. Optional runtime (interactivity)

Paint does **not** need this. Add it when you want tooltips, scroll reveal, legend focus.

### CDN

```html
<script>
  window.ProvChartRuntimeConfig = {
    tooltips: true,
    perPointTooltips: true,
    observe: true,
    excludeSvg: true,
  };
</script>
<script
  src="https://cdn.jsdelivr.net/npm/provchart-runtime@1.0.0/dist/provchart-runtime.min.js"
  defer
></script>
```

### npm

```bash
npm install provchart-runtime
```

```js
import "provchart-runtime";
```

After injecting HTML from the API, the runtime’s `MutationObserver` usually picks up new `[data-provchart]` nodes. If needed:

```js
window.ProvChartRuntime?.refresh?.();
// or
window.ProvChartRuntime?.scan?.();
```

Pure **SVG** from `generate-svg` is skipped when `excludeSvg: true`.

---

## 5. Integration recipes by stack

### Static HTML

- Generate once (demo page or CI)  
- Paste `<style>` + chart markup  
- Optional runtime `<script defer>`

### Vanilla / SPA (React, Vue, Svelte)

- `fetch` generate from a backend proxy (keeps the key off the client) **or** use a public demo key only for docs  
- Set `innerHTML` / `v-html` / equivalent for `data.html`  
- Append `data.css` into a style tag or construct a style element  
- Call `ProvChartRuntime.refresh()` after client navigations if the observer misses a mount  

**Security:** prefer a **backend proxy** that attaches `X-API-Key` so the browser never sees the secret.

### Node / CI

```bash
curl -s -X POST "https://provchart-api.devtem.org/api/v1/generate-svg" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $PROVCHART_API_KEY" \
  -d @payload.json | jq -r '.svg' > public/charts/views.svg
```

### Email

HTML email clients are hostile to modern CSS. Prefer **static images** or very simple HTML; ProvChart’s primary target is **web pages and docs**, not full email CSS fidelity. (Product positioning: web + Markdown/SVG.)

---

## 6. Builder-only workflow (no code)

1. Open the [Pro / dashboard builder](https://chart.devtem.org/dashboard)  
2. Configure type, series, theme  
3. Generate and **copy HTML / CSS** (or use SVG tab where available)  
4. Paste into your project  

Same engine family as the API; the API is for automation and apps.

---

## 7. Verify integration

| Check | Expect |
|-------|--------|
| Network | `generate` returns `success: true` and non-empty `html` / `css` |
| Page | Chart visible with JS disabled (runtime blocked) |
| Quota | Free tier: batch demos consume multiple gens — use [/demo](https://chart.devtem.org/demo) carefully |
| Errors | `INVALID_API_KEY`, `MONTHLY_LIMIT_REACHED`, `SUBSCRIPTION_REQUIRED` — handle in UI |

---

## 8. Common mistakes

| Mistake | Fix |
|---------|-----|
| Key in frontend repo | Proxy via backend; env on server only |
| Forgetting to inject `css` | Chart HTML without CSS variables/paint rules |
| Expecting runtime on SVG | Use HTML generate for runtime UX |
| Burning free quota on “generate all” | Generate fewer charts while testing |
| Wrong header name | Use `X-API-Key`, not `Authorization`, for API keys (unless your stack documents Bearer for sessions) |

---

## Next step

Create a key, run one successful generate, and inject it.

→ **[03 · Getting started](./03-getting-started.md)**

← [01 · Introduction](./01-introduction.md)
