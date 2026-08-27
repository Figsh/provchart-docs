# 03 · Getting started

This chapter walks through a **first successful chart**: API key → one `generate` call → inject HTML/CSS → confirm paint without a chart library.

Time: a few minutes if you already have a ProvChart account.

| You will | |
|----------|--|
| Create or copy an API key | Dashboard |
| Call `POST /api/v1/generate` | HTML + CSS |
| Inject into a page | Visible chart |
| (Optional) Add runtime | Tooltips |

← [02 · Integration](./02-installation.md) · [Next: Core concepts →](./04-core-concepts.md)

---

## 1. Account and key

1. Go to [chart.devtem.org](https://chart.devtem.org) and sign in (or sign up).  
2. Open **[Dashboard](https://chart.devtem.org/dashboard) → Developer API / API keys**.  
3. **Create** a key and copy it once.

Treat it like a password. For local demos you can paste it into a page; for real apps keep it on the server only (see [02 · Integration](./02-installation.md)).

Free signed-up accounts include **limited monthly test generations**. Each successful generate (HTML or SVG) counts.

---

## 2. Minimal HTML page

Create a file (e.g. `index.html`) or use any static host:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>My first ProvChart</title>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: #0c0a16;
      font-family: system-ui, sans-serif;
    }
    #chart { width: min(560px, 92vw); }
    .err { color: #ff5e7d; font-size: 14px; }
  </style>
</head>
<body>
  <div id="chart"><p style="color:#837da0">Loading…</p></div>

  <script type="module">
    const API = "https://provchart-api.devtem.org/api/v1/generate";
    const API_KEY = "YOUR_API_KEY"; // replace — do not commit real keys

    const payload = {
      type: "area",
      theme: "midnight",
      series: [
        {
          name: "Traffic",
          color: "#4fd8c4",
          points: [30, 45, 40, 60, 55, 70, 65],
        },
        {
          name: "Signups",
          color: "#f0a860",
          points: [8, 12, 11, 18, 16, 22, 20],
        },
      ],
      axisX: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    };

    const mount = document.getElementById("chart");

    try {
      const res = await fetch(API, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-API-Key": API_KEY,
        },
        body: JSON.stringify(payload),
      });

      const data = await res.json();

      if (!data.success) {
        throw new Error(data.error || data.code || `HTTP ${res.status}`);
      }

      let style = document.getElementById("provchart-style");
      if (!style) {
        style = document.createElement("style");
        style.id = "provchart-style";
        document.head.appendChild(style);
      }
      style.textContent = data.css || "";
      mount.innerHTML = data.html || "";
    } catch (err) {
      mount.innerHTML = `<p class="err">${err.message}</p>`;
      console.error(err);
    }
  </script>
</body>
</html>
```

Replace `YOUR_API_KEY` with your key. Open the file via a local static server (or your host). You should see a two-series area chart.

---

## 3. What “success” looks like

Response shape (simplified):

```json
{
  "success": true,
  "html": "<div class=\"pc-…\" data-provchart=\"area\">…</div>",
  "css": ".pc-… { --pc-…-s1-p1: …; /* … */ }"
}
```

| Field | Use |
|-------|-----|
| `html` | Chart markup → put in a container |
| `css` | Scoped rules + variables → put in `<style>` |
| `success: false` | Read `error` / `code` — do not inject |

---

## 4. Common first errors

| Symptom | Likely cause |
|---------|----------------|
| `INVALID_API_KEY` / 401 | Wrong key, extra spaces, or revoked key |
| `MONTHLY_LIMIT_REACHED` | Free/Pro quota used up — wait or upgrade |
| `SUBSCRIPTION_REQUIRED` | Endpoint/feature needs a paid plan |
| Empty chart / broken layout | CSS not injected; only HTML pasted |
| CORS issues | Call from a backend proxy if the browser blocks the request |

Use the [live demo](https://chart.devtem.org/demo) to confirm your key works against multiple types.

---

## 5. Optional: tooltips in two tags

Charts already paint without this. To enhance HTML charts:

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

Place **config before** the runtime script. After inject, the observer should attach; if not, `ProvChartRuntime.refresh()` or `.scan()`.

---

## 6. Second chart type (optional)

Change `payload` to a gauge:

```javascript
const payload = {
  type: "gauge",
  theme: "midnight",
  label: "Health",
  size: 180,
  thickness: 10,
  series: [
    { name: "CPU", value: 72, color: "#ff5e7d" },
    { name: "RAM", value: 54, color: "#4fd8c4" },
    { name: "Disk", value: 38, color: "#8b7bff" },
  ],
};
```

Same inject path. Gauge uses `value` (0–100 style), not `points`.

---

## 7. Checklist

- [ ] Key created in dashboard  
- [ ] `fetch` returns `success: true`  
- [ ] Both `css` and `html` applied  
- [ ] Chart visible  
- [ ] (Optional) Runtime loaded with `defer`  
- [ ] Key not committed to git  

---

## Next step

Understand **compile → paint → enhance**, payloads, and how ProvChart differs from a client chart library.

→ **[04 · Core concepts](./04-core-concepts.md)**

← [02 · Integration](./02-installation.md)
