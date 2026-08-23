/**
 * Express routes for ProvChart data API.
 */

const express = require('express');
const router = express.Router();

router.get('/api/chart-data', (req, res) => {
  const points = [20, 35, 48, 66, 58, 72, 80, 95];
  const labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Now'];
  res.json({ points, labels });
});

router.get('/api/revenue', (req, res) => {
  const points = [1200, 1800, 2400, 1600, 2100, 2800, 3200, 2900];
  res.json({ points, currency: 'USD' });
});

module.exports = router;
