// ProvChart Developer API — Node.js example
// Docs: https://chart.devtem.org/docs#dev-api-overview
//
// Usage:
//   PROVCHART_API_KEY=pc_live_xxxx node node-example.js

const API_URL = "https://provchart-api.devtem.org/api/v1/generate";

async function generateChart() {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-Key": process.env.PROVCHART_API_KEY,
    },
    body: JSON.stringify({
      type: "line",
      series: [
        { name: "Revenue", color: "#8b7bff", points: [20, 35, 45, 30, 50] },
        { name: "Cost", color: "#4fd8c4", points: [15, 28, 30, 22, 40] },
      ],
      axisX: ["Jan", "Feb", "Mar", "Apr", "May"],
    }),
  });

  const data = await res.json();

  if (!data.success) {
    // See error codes: INVALID_API_KEY, SUBSCRIPTION_REQUIRED, MONTHLY_LIMIT_REACHED
    console.error(`ProvChart error [${data.code}]: ${data.error}`);
    process.exit(1);
  }

  // data.html + data.css — static output, no chart-library runtime needed
  console.log(data.html);
  console.log(data.css);

  return data;
}

generateChart();

// Express route example — proxy the key server-side, never ship it to the client
//
// app.post("/api/chart", async (req, res) => {
//   const upstream = await fetch(API_URL, {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//       "X-API-Key": process.env.PROVCHART_API_KEY,
//     },
//     body: JSON.stringify(req.body),
//   });
//   const data = await upstream.json();
//   res.status(upstream.status).json(data);
// });
