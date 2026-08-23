/**
 * Node.js + Express server with ProvChart integration.
 */

const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/api/chart-data', (req, res) => {
  const points = [20, 35, 48, 66, 58, 72, 80, 95];
  const labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Now'];
  res.json({ points, labels });
});

app.get('/api/revenue', (req, res) => {
  const points = [1200, 1800, 2400, 1600, 2100, 2800, 3200, 2900];
  res.json({ points, currency: 'USD' });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
